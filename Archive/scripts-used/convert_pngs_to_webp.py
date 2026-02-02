#!/usr/bin/env python3
"""
Convert all PNG images in founders directory to WebP format for web optimization.

This script:
1. Finds all PNG files in the assets/founders directory structure
2. Converts each PNG to WebP using Pillow library
3. Maintains directory structure and high quality (quality=85)
4. Keeps original PNGs as backup
5. Creates a manifest file tracking all conversions
"""

import os
import json
from pathlib import Path
from PIL import Image
from datetime import datetime

# Configuration
FOUNDERS_DIR = Path(__file__).parent / "assets" / "founders"
QUALITY = 85
MANIFEST_FILE = FOUNDERS_DIR / "webp_conversion_manifest.json"

# Subdirectories to process
SUBDIRS = [
    "headshots_with_bg",
    "headshots_no_bg",
    "corporate_photos",
    "casual_variants",
    "group_photos"
]

def convert_png_to_webp(png_path, quality=85):
    """
    Convert a single PNG file to WebP format.

    Args:
        png_path: Path to the PNG file
        quality: WebP quality (1-100, default 85)

    Returns:
        dict: Conversion result with success status and details
    """
    try:
        png_path = Path(png_path)
        webp_path = png_path.with_suffix('.webp')

        # Open PNG image
        with Image.open(png_path) as img:
            # Convert RGBA to RGB if necessary (WebP handles both, but RGB is smaller)
            if img.mode in ('RGBA', 'LA', 'P'):
                # Create white background for transparency
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'P':
                    img = img.convert('RGBA')
                background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                img = background
            elif img.mode != 'RGB':
                img = img.convert('RGB')

            # Get original file size
            original_size = png_path.stat().st_size

            # Save as WebP
            img.save(webp_path, 'WEBP', quality=quality, method=6)

            # Get new file size
            new_size = webp_path.stat().st_size

            # Calculate compression ratio
            compression_ratio = (1 - new_size / original_size) * 100

            return {
                'success': True,
                'png_file': str(png_path.relative_to(FOUNDERS_DIR)),
                'webp_file': str(webp_path.relative_to(FOUNDERS_DIR)),
                'original_size_bytes': original_size,
                'webp_size_bytes': new_size,
                'compression_percent': round(compression_ratio, 2),
                'quality': quality,
                'error': None
            }
    except Exception as e:
        return {
            'success': False,
            'png_file': str(png_path.relative_to(FOUNDERS_DIR)) if 'png_path' in locals() else str(png_path),
            'webp_file': None,
            'original_size_bytes': 0,
            'webp_size_bytes': 0,
            'compression_percent': 0,
            'quality': quality,
            'error': str(e)
        }

def main():
    """Main conversion process."""

    if not FOUNDERS_DIR.exists():
        print(f"Error: Founders directory not found: {FOUNDERS_DIR}")
        return False

    print(f"Starting PNG to WebP conversion")
    print(f"Location: {FOUNDERS_DIR}")
    print(f"Quality: {QUALITY}")
    print(f"Timestamp: {datetime.now().isoformat()}")
    print("-" * 80)

    # Check if Pillow is installed
    try:
        from PIL import Image
    except ImportError:
        print("Error: Pillow library not installed. Installing...")
        os.system("pip install Pillow")

    # Find all PNG files
    png_files = sorted(FOUNDERS_DIR.glob("**/*.png"))

    if not png_files:
        print("No PNG files found to convert.")
        return False

    print(f"Found {len(png_files)} PNG files to convert\n")

    # Track conversions
    conversions = []
    total_original_size = 0
    total_webp_size = 0
    success_count = 0
    error_count = 0

    # Convert each PNG
    for i, png_file in enumerate(png_files, 1):
        result = convert_png_to_webp(png_file, QUALITY)
        conversions.append(result)

        relative_path = png_file.relative_to(FOUNDERS_DIR)

        if result['success']:
            total_original_size += result['original_size_bytes']
            total_webp_size += result['webp_size_bytes']
            success_count += 1

            status = f"[OK] [{i:2d}/{len(png_files)}]"
            print(f"{status} {relative_path}")
            print(f"     {result['original_size_bytes']:>10,} bytes -> {result['webp_size_bytes']:>10,} bytes ({result['compression_percent']:>6.1f}% smaller)")
        else:
            error_count += 1
            status = f"[FAIL] [{i:2d}/{len(png_files)}]"
            print(f"{status} {relative_path}")
            print(f"       Error: {result['error']}")

    print("-" * 80)
    print(f"\nConversion Summary:")
    print(f"  Total files: {len(png_files)}")
    print(f"  Successful: {success_count}")
    print(f"  Failed: {error_count}")

    if success_count > 0:
        total_compression = (1 - total_webp_size / total_original_size) * 100
        print(f"\nSize Reduction:")
        print(f"  Original total: {total_original_size:,} bytes ({total_original_size / 1024 / 1024:.2f} MB)")
        print(f"  WebP total: {total_webp_size:,} bytes ({total_webp_size / 1024 / 1024:.2f} MB)")
        print(f"  Overall compression: {total_compression:.1f}%")

    # Create manifest file
    manifest = {
        'timestamp': datetime.now().isoformat(),
        'quality': QUALITY,
        'total_files': len(png_files),
        'successful_conversions': success_count,
        'failed_conversions': error_count,
        'total_original_size_bytes': total_original_size,
        'total_webp_size_bytes': total_webp_size,
        'overall_compression_percent': round((1 - total_webp_size / total_original_size) * 100, 2) if total_original_size > 0 else 0,
        'conversions': conversions
    }

    # Write manifest file
    with open(MANIFEST_FILE, 'w') as f:
        json.dump(manifest, f, indent=2)

    print(f"\nManifest file created: {MANIFEST_FILE.relative_to(FOUNDERS_DIR.parent.parent)}")
    print(f"\nOriginal PNG files have been preserved as backups.")
    print(f"WebP files are now available alongside PNG files in each directory.")

    return error_count == 0

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
