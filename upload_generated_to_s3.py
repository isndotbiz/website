#!/usr/bin/env python3
"""
Upload Generated Images to S3
Uploads all generated WebP images to S3 bucket under premium_v3/generated/
"""

import boto3
import os
from pathlib import Path
from botocore.exceptions import ClientError

# S3 configuration
S3_BUCKET = 'isnbiz-assets-1769962280'
S3_PREFIX = 'generated/'

# Input directory
INPUT_DIR = Path('assets/generated')

def upload_to_s3(file_path, s3_key):
    """Upload a file to S3"""
    try:
        s3_client = boto3.client('s3')

        # Set content type for WebP
        extra_args = {
            'ContentType': 'image/webp',
            'CacheControl': 'public, max-age=31536000',  # 1 year cache
        }

        s3_client.upload_file(
            str(file_path),
            S3_BUCKET,
            s3_key,
            ExtraArgs=extra_args
        )

        # Generate public URL
        url = f"https://{S3_BUCKET}.s3.amazonaws.com/{s3_key}"
        return url

    except ClientError as e:
        print(f"[ERROR] Upload error: {e}")
        return None

def main():
    """Upload all generated images to S3"""
    print("=" * 80)
    print("UPLOAD GENERATED IMAGES TO S3")
    print("=" * 80)
    print(f"Source: {INPUT_DIR}")
    print(f"Bucket: {S3_BUCKET}")
    print(f"Prefix: {S3_PREFIX}")
    print("=" * 80)

    # Check if directory exists
    if not INPUT_DIR.exists():
        print(f"✗ Directory not found: {INPUT_DIR}")
        print("Run generate_bulk_images.py first!")
        return

    # Get all WebP files
    webp_files = list(INPUT_DIR.glob('*.webp'))

    if not webp_files:
        print(f"✗ No WebP files found in {INPUT_DIR}")
        return

    print(f"\nFound {len(webp_files)} images to upload\n")

    # Upload each file
    uploaded = []
    failed = []

    for file_path in webp_files:
        s3_key = f"{S3_PREFIX}{file_path.name}"
        print(f"Uploading: {file_path.name} -> {s3_key}")

        url = upload_to_s3(file_path, s3_key)

        if url:
            print(f"[OK] URL: {url}")
            uploaded.append({
                'file': file_path.name,
                'url': url
            })
        else:
            print(f"[FAIL] Failed")
            failed.append(file_path.name)
        print()

    # Summary
    print("=" * 80)
    print("UPLOAD COMPLETE")
    print("=" * 80)
    print(f"[OK] Uploaded: {len(uploaded)}")
    print(f"[FAIL] Failed: {len(failed)}")

    if failed:
        print("\nFailed files:")
        for file in failed:
            print(f"  - {file}")

    # Save URL mapping
    if uploaded:
        import json
        url_map_path = INPUT_DIR / 's3_urls.json'
        with open(url_map_path, 'w') as f:
            json.dump(uploaded, f, indent=2)
        print(f"\nURL mapping saved to: {url_map_path}")

    print("=" * 80)

if __name__ == '__main__':
    main()
