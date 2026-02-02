#!/usr/bin/env python3
"""
Upload slider images to S3 bucket
Uploads all slider_*.webp images from slider_images/ directory
"""

import os
import sys
import boto3
from pathlib import Path
from botocore.exceptions import ClientError

# S3 configuration
BUCKET_NAME = "isnbiz-assets-1769962280"
S3_PREFIX = "premium_v3/slider/"
LOCAL_DIR = Path(__file__).parent / "slider_images"

# Content type mapping
CONTENT_TYPES = {
    '.webp': 'image/webp',
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.png': 'image/png'
}


def upload_to_s3(local_path, s3_key, content_type):
    """Upload a file to S3"""
    try:
        s3 = boto3.client('s3')

        print(f"[^] Uploading: {local_path.name}")
        print(f"   -> s3://{BUCKET_NAME}/{s3_key}")

        # Upload with proper content type (bucket has public policy, no ACL needed)
        s3.upload_file(
            str(local_path),
            BUCKET_NAME,
            s3_key,
            ExtraArgs={
                'ContentType': content_type,
                'CacheControl': 'public, max-age=31536000'  # 1 year cache
            }
        )

        # Generate URL
        url = f"https://{BUCKET_NAME}.s3.us-east-1.amazonaws.com/{s3_key}"
        print(f"   [+] URL: {url}")
        return url

    except ClientError as e:
        print(f"   [!] Error: {e}")
        return None
    except Exception as e:
        print(f"   [!] Unexpected error: {e}")
        return None


def main():
    """Upload all slider images to S3"""
    print("=" * 70)
    print("ISN.BIZ Slider Images S3 Upload")
    print("=" * 70)
    print(f"Local directory: {LOCAL_DIR}")
    print(f"S3 bucket: {BUCKET_NAME}")
    print(f"S3 prefix: {S3_PREFIX}")

    # Check if directory exists
    if not LOCAL_DIR.exists():
        print(f"\n[!] Error: Directory not found: {LOCAL_DIR}")
        print("Run generate_slider_images.py first!")
        return 1

    # Find all slider images
    images = list(LOCAL_DIR.glob("slider_*.webp"))
    images.extend(LOCAL_DIR.glob("slider_*.jpg"))
    images.extend(LOCAL_DIR.glob("slider_*.jpeg"))
    images.extend(LOCAL_DIR.glob("slider_*.png"))

    if not images:
        print(f"\n[!] Error: No slider images found in {LOCAL_DIR}")
        print("Run generate_slider_images.py first!")
        return 1

    images.sort()
    print(f"\n[*] Found {len(images)} images to upload")

    # Upload each image
    successful = 0
    failed = 0
    urls = []

    for image_path in images:
        print(f"\n{'-' * 70}")

        # Determine content type
        ext = image_path.suffix.lower()
        content_type = CONTENT_TYPES.get(ext, 'application/octet-stream')

        # S3 key
        s3_key = S3_PREFIX + image_path.name

        # Upload
        url = upload_to_s3(image_path, s3_key, content_type)
        if url:
            successful += 1
            urls.append((image_path.name, url))
        else:
            failed += 1

    # Summary
    print("\n" + "=" * 70)
    print("UPLOAD SUMMARY")
    print("=" * 70)
    print(f"[+] Successful: {successful}/{len(images)}")
    print(f"[!] Failed: {failed}/{len(images)}")

    if urls:
        print("\n[>] Generated URLs:")
        print("-" * 70)
        for filename, url in urls:
            print(f"{filename:20} -> {url}")

        # Generate HTML snippet
        print("\n[>] HTML Code Snippet (copy to slider-gallery.html):")
        print("-" * 70)
        for i, (filename, url) in enumerate(urls, 1):
            print(f"""
<!-- Slide {i} -->
<div class="swiper-slide">
    <div class="slide-content">
        <div class="slide-background" style="background: url('{url}') center/cover no-repeat;">
            <div class="slide-pattern"></div>
        </div>
        <div class="slide-info">
            <!-- Add your slide content here -->
        </div>
    </div>
</div>
            """.strip())

    if successful == len(images):
        print("\n[SUCCESS] All images uploaded successfully!")
        print("\nNext steps:")
        print("1. Copy the HTML snippets above")
        print("2. Update slider-gallery.html with new image URLs")
        print("3. Test the slider in your browser")
    else:
        print("\n[WARNING] Some uploads failed. Check errors above.")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
