#!/usr/bin/env python3
"""
optimize_responsive.py - Generate responsive image variants for ISN.BIZ premium_v3 assets.

Takes all WebP images from premium_v3 subdirectories and creates three responsive
variants (desktop, tablet, mobile) with appropriate sizing and quality settings.
Uploads all variants to S3.

Usage:
    python optimize_responsive.py [--dry-run] [--skip-upload]

Options:
    --dry-run       Show what would be done without writing files
    --skip-upload   Generate variants locally but skip S3 upload
"""

import os
import sys
import argparse
from pathlib import Path
from io import BytesIO

try:
    from PIL import Image
except ImportError:
    print("ERROR: Pillow is required. Install with: pip install Pillow")
    sys.exit(1)

try:
    import boto3
    from botocore.exceptions import ClientError, NoCredentialsError
    HAS_BOTO3 = True
except ImportError:
    HAS_BOTO3 = False


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).resolve().parent
S3_BUCKET = "isnbiz-assets-1769962280"
S3_PREFIX = "premium_v3"

# Directories to process (skip logos/)
PROCESS_DIRS = ["hero", "sections", "services", "portfolio", "gallery", "founders"]

# Responsive variant definitions
VARIANTS = {
    "desktop": {"scale": 1.0,  "quality": 80},
    "tablet":  {"scale": 0.5,  "quality": 75},
    "mobile":  {"scale": 0.25, "quality": 70},
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def file_size_kb(path):
    """Return file size in KB."""
    return path.stat().st_size / 1024.0


def bytes_size_kb(data):
    """Return byte-string size in KB."""
    return len(data) / 1024.0


def create_variant(img, scale, quality, preserve_alpha):
    """
    Resize *img* by *scale* using LANCZOS and encode to WebP at *quality*.
    Returns the encoded bytes.
    """
    new_width = max(1, int(img.width * scale))
    new_height = max(1, int(img.height * scale))

    resized = img.resize((new_width, new_height), Image.LANCZOS)

    buf = BytesIO()
    if preserve_alpha and resized.mode == "RGBA":
        resized.save(buf, format="WEBP", quality=quality, method=4)
    else:
        # Convert to RGB if not already (drop alpha for non-founders images)
        if resized.mode not in ("RGB", "L"):
            if not preserve_alpha:
                resized = resized.convert("RGB")
        resized.save(buf, format="WEBP", quality=quality, method=4)

    return buf.getvalue()


def upload_to_s3(s3_client, data, bucket, key):
    """Upload bytes to S3. Returns True on success."""
    try:
        s3_client.put_object(
            Bucket=bucket,
            Key=key,
            Body=data,
            ContentType="image/webp",
            CacheControl="public, max-age=31536000, immutable",
        )
        return True
    except (ClientError, NoCredentialsError) as exc:
        print(f"  S3 upload FAILED for {key}: {exc}")
        return False


# ---------------------------------------------------------------------------
# Main processing
# ---------------------------------------------------------------------------

def process_images(dry_run=False, skip_upload=False):
    """Walk PROCESS_DIRS, generate responsive variants, optionally upload."""

    # Collect all .webp source images
    source_files = []   # list of (category, path)
    for category in PROCESS_DIRS:
        cat_dir = SCRIPT_DIR / category
        if not cat_dir.is_dir():
            print(f"[SKIP] Directory not found: {cat_dir}")
            continue
        for fpath in sorted(cat_dir.iterdir()):
            if fpath.suffix.lower() == ".webp" and fpath.is_file():
                # Skip files that are already responsive variants
                stem = fpath.stem
                if stem.endswith(("_desktop", "_tablet", "_mobile")):
                    continue
                source_files.append((category, fpath))

    if not source_files:
        print("No .webp source images found in any of the target directories.")
        print("Directories searched:")
        for d in PROCESS_DIRS:
            print(f"  {SCRIPT_DIR / d}")
        return

    # Optionally set up S3 client
    s3_client = None
    if not skip_upload and not dry_run:
        if not HAS_BOTO3:
            print("WARNING: boto3 not installed. S3 upload will be skipped.")
            print("         Install with: pip install boto3")
            skip_upload = True
        else:
            try:
                s3_client = boto3.client("s3")
                s3_client.head_bucket(Bucket=S3_BUCKET)
                print(f"S3 bucket verified: {S3_BUCKET}")
                print("")
            except Exception as exc:
                print(f"WARNING: Cannot reach S3 bucket ({exc}). Upload will be skipped.")
                skip_upload = True

    # Report header
    sep = "=" * 90
    print(sep)
    hdr = "{:<40} {:>13} {:>13} {:>13} {:>8}".format(
        "Source File", "Desktop (KB)", "Tablet (KB)", "Mobile (KB)", "Savings")
    print(hdr)
    print(sep)

    total_original_kb = 0.0
    total_desktop_kb = 0.0
    total_tablet_kb = 0.0
    total_mobile_kb = 0.0
    files_processed = 0
    uploads_ok = 0
    uploads_fail = 0

    for category, src_path in source_files:
        stem = src_path.stem
        preserve_alpha = (category == "founders")

        try:
            img = Image.open(src_path)
        except Exception as exc:
            print(f"  ERROR opening {src_path.name}: {exc}")
            continue

        # Detect if the image actually has meaningful alpha
        if preserve_alpha and img.mode != "RGBA":
            preserve_alpha = False

        original_kb = file_size_kb(src_path)
        total_original_kb += original_kb

        variant_sizes = {}
        variant_data = {}

        for vname, vcfg in VARIANTS.items():
            data = create_variant(img, vcfg["scale"], vcfg["quality"], preserve_alpha)
            size_kb = bytes_size_kb(data)
            variant_sizes[vname] = size_kb
            variant_data[vname] = data

        total_desktop_kb += variant_sizes["desktop"]
        total_tablet_kb += variant_sizes["tablet"]
        total_mobile_kb += variant_sizes["mobile"]

        variant_total = sum(variant_sizes.values())
        savings_pct = ((original_kb * 3 - variant_total) / (original_kb * 3) * 100
                       if original_kb > 0 else 0.0)

        label = f"{category}/{src_path.name}"
        row = "{:<40} {:>10.1f}   {:>10.1f}   {:>10.1f}   {:>5.1f}%".format(
            label,
            variant_sizes["desktop"],
            variant_sizes["tablet"],
            variant_sizes["mobile"],
            savings_pct)
        print(row)

        # Write local files and upload
        if not dry_run:
            for vname, data in variant_data.items():
                out_name = f"{stem}_{vname}.webp"
                out_path = src_path.parent / out_name
                out_path.write_bytes(data)

                if not skip_upload and s3_client is not None:
                    s3_key = f"{S3_PREFIX}/{category}/{out_name}"
                    ok = upload_to_s3(s3_client, data, S3_BUCKET, s3_key)
                    if ok:
                        uploads_ok += 1
                    else:
                        uploads_fail += 1

        files_processed += 1
        img.close()

    # Summary
    print(sep)
    total_all_variants = total_desktop_kb + total_tablet_kb + total_mobile_kb
    total_naive = total_original_kb * 3
    overall_savings = ((total_naive - total_all_variants) / total_naive * 100
                       if total_naive > 0 else 0.0)

    print("")
    print("SUMMARY")
    print(f"  Source images processed : {files_processed}")
    print(f"  Variants created        : {files_processed * 3}")
    print(f"  Total original size     : {total_original_kb:,.1f} KB")
    print(f"  Total desktop size      : {total_desktop_kb:,.1f} KB")
    print(f"  Total tablet size       : {total_tablet_kb:,.1f} KB")
    print(f"  Total mobile size       : {total_mobile_kb:,.1f} KB")
    print(f"  Combined variant size   : {total_all_variants:,.1f} KB")
    print(f"  Overall savings         : {overall_savings:.1f}%")

    if not skip_upload and not dry_run:
        print("")
        print(f"  S3 uploads succeeded    : {uploads_ok}")
        print(f"  S3 uploads failed       : {uploads_fail}")
        print(f"  S3 bucket               : {S3_BUCKET}")
        print(f"  S3 prefix               : {S3_PREFIX}/")

    if dry_run:
        print("")
        print("  [DRY RUN] No files were written or uploaded.")

    print("")


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Generate responsive image variants (desktop/tablet/mobile) "
                    "from premium_v3 WebP assets and upload to S3."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without writing any files.",
    )
    parser.add_argument(
        "--skip-upload",
        action="store_true",
        help="Generate variants locally but skip the S3 upload step.",
    )
    args = parser.parse_args()

    print("")
    print("=" * 90)
    print("  ISN.BIZ Premium v3 - Responsive Image Optimizer")
    print("=" * 90)
    print(f"  Source directory : {SCRIPT_DIR}")
    categories_str = ", ".join(PROCESS_DIRS)
    print(f"  Categories       : {categories_str}")
    print("  Variants         : desktop (100%, q80), tablet (50%, q75), mobile (25%, q70)")
    print(f"  S3 bucket        : {S3_BUCKET}")
    print(f"  Dry run          : {args.dry_run}")
    print(f"  Skip upload      : {args.skip_upload}")
    print("")

    process_images(dry_run=args.dry_run, skip_upload=args.skip_upload)


if __name__ == "__main__":
    main()
