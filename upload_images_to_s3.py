#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Upload all website images to S3 and generate URL mapping
Converts all images to WebP, optimizes them, and uploads to S3
"""

import os
import sys
import io

# Fix Windows console encoding
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

import boto3
import subprocess
from pathlib import Path
from PIL import Image
import json

# S3 Configuration
S3_BUCKET = "isnbiz-assets-1769962280"
S3_REGION = "us-east-1"
S3_BASE_URL = f"https://{S3_BUCKET}.s3.{S3_REGION}.amazonaws.com"

# Directories to process
IMAGE_DIRS = [
    "assets/founders/headshots_with_bg",
    "assets/founders/headshots_no_bg",
    "assets/founders/corporate_photos",
    "assets/founders/casual_variants",
    "assets/founders/group_photos",
    "assets/projects",
    "assets/backgrounds",
    "assets/hero_backgrounds",
]

def optimize_webp(input_path, output_path, quality=85):
    """Convert and optimize image to WebP format"""
    try:
        img = Image.open(input_path)

        # Convert to RGB if necessary
        if img.mode in ('RGBA', 'LA', 'P'):
            background = Image.new('RGB', img.size, (255, 255, 255))
            if img.mode == 'P':
                img = img.convert('RGBA')
            background.paste(img, mask=img.split()[-1] if img.mode in ('RGBA', 'LA') else None)
            img = background
        elif img.mode != 'RGB':
            img = img.convert('RGB')

        # Save as WebP
        img.save(output_path, 'WebP', quality=quality, method=6)

        # Get file sizes
        original_size = os.path.getsize(input_path)
        webp_size = os.path.getsize(output_path)
        savings = ((original_size - webp_size) / original_size) * 100

        return {
            'original_size': original_size,
            'webp_size': webp_size,
            'savings_percent': savings
        }
    except Exception as e:
        print(f"  ❌ Error optimizing {input_path}: {e}")
        return None

def upload_to_s3(local_path, s3_key):
    """Upload file to S3"""
    try:
        s3 = boto3.client('s3', region_name=S3_REGION)

        # Determine content type
        content_type = 'image/webp' if local_path.endswith('.webp') else 'image/png'

        # Upload with proper headers (no ACL - bucket policy handles public access)
        s3.upload_file(
            local_path,
            S3_BUCKET,
            s3_key,
            ExtraArgs={
                'ContentType': content_type,
                'CacheControl': 'max-age=31536000',  # 1 year cache
            }
        )

        url = f"{S3_BASE_URL}/{s3_key}"
        return url
    except Exception as e:
        print(f"  ❌ Error uploading {local_path}: {e}")
        return None

def main():
    print("="*80)
    print("  ISN.BIZ IMAGE OPTIMIZATION & S3 UPLOAD")
    print("="*80)
    print()

    # Create temp directory for optimized images
    temp_dir = Path("/tmp/isn-biz-optimized")
    temp_dir.mkdir(exist_ok=True, parents=True)

    url_mapping = {}
    stats = {
        'total_files': 0,
        'uploaded': 0,
        'failed': 0,
        'total_original_size': 0,
        'total_webp_size': 0,
    }

    # Process each directory
    for img_dir in IMAGE_DIRS:
        img_path = Path(img_dir)
        if not img_path.exists():
            print(f"⚠ Directory not found: {img_dir}")
            continue

        print(f"\n📁 Processing: {img_dir}")
        print("-" * 80)

        # Find all images
        images = list(img_path.glob("*.webp")) + list(img_path.glob("*.png")) + \
                 list(img_path.glob("*.jpg")) + list(img_path.glob("*.jpeg"))

        for img_file in images:
            stats['total_files'] += 1

            # Determine output filename
            if img_file.suffix.lower() == '.webp':
                webp_file = img_file
                optimized_file = temp_dir / img_file.name

                # Copy and re-optimize WebP
                result = optimize_webp(str(img_file), str(optimized_file), quality=85)
            else:
                # Convert to WebP
                webp_name = img_file.stem + '.webp'
                optimized_file = temp_dir / webp_name

                result = optimize_webp(str(img_file), str(optimized_file), quality=85)

            if result:
                stats['total_original_size'] += result['original_size']
                stats['total_webp_size'] += result['webp_size']

                # Generate S3 key (preserve directory structure)
                relative_path = img_file.relative_to("assets")
                s3_key = f"assets/{relative_path.parent}/{optimized_file.name}"

                print(f"  📤 {img_file.name} → {optimized_file.name} ({result['savings_percent']:.1f}% smaller)")

                # Upload to S3
                url = upload_to_s3(str(optimized_file), s3_key)
                if url:
                    stats['uploaded'] += 1
                    # Store mapping (original path → S3 URL)
                    original_path = str(img_file).replace('\\', '/')
                    url_mapping[original_path] = url
                    print(f"    ✅ {url}")
                else:
                    stats['failed'] += 1

    # Save URL mapping
    mapping_file = "s3_url_mapping.json"
    with open(mapping_file, 'w') as f:
        json.dump(url_mapping, f, indent=2)

    print("\n" + "="*80)
    print("  UPLOAD COMPLETE")
    print("="*80)
    print(f"\n📊 Statistics:")
    print(f"  Total files:        {stats['total_files']}")
    print(f"  Uploaded:           {stats['uploaded']}")
    print(f"  Failed:             {stats['failed']}")
    print(f"  Original size:      {stats['total_original_size'] / 1024 / 1024:.2f} MB")
    print(f"  Optimized size:     {stats['total_webp_size'] / 1024 / 1024:.2f} MB")
    print(f"  Total savings:      {((stats['total_original_size'] - stats['total_webp_size']) / stats['total_original_size'] * 100):.1f}%")
    print(f"\n📄 URL mapping saved to: {mapping_file}")
    print(f"   Use this file to update HTML references to S3 URLs")
    print("\n" + "="*80)

if __name__ == "__main__":
    main()
