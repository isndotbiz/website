#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Upload Hero Background to S3
Uploads the generated hero background to S3 bucket
"""

import os
import sys
from pathlib import Path

# Fix Windows console encoding
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

try:
    import boto3
    from botocore.exceptions import ClientError
except ImportError:
    print("Missing boto3. Install with: pip install boto3")
    sys.exit(1)

# S3 configuration
S3_BUCKET = 'isnbiz-assets-1769962280'
S3_KEY = 'premium_v3/backgrounds/hero-background-main.webp'
S3_REGION = 'us-east-1'

# Local file
LOCAL_FILE = Path('assets/backgrounds/hero-background-main.webp')

def upload_to_s3():
    """Upload hero background to S3"""

    print("=" * 60)
    print("UPLOAD HERO BACKGROUND TO S3")
    print("=" * 60)
    print(f"Local file: {LOCAL_FILE}")
    print(f"S3 bucket: {S3_BUCKET}")
    print(f"S3 key: {S3_KEY}")
    print("=" * 60 + "\n")

    # Check file exists
    if not LOCAL_FILE.exists():
        print(f"[!] File not found: {LOCAL_FILE}")
        print("Run generate_hero_background.py first!")
        sys.exit(1)

    # Get file size
    file_size = LOCAL_FILE.stat().st_size / 1024  # KB
    print(f"[*] File size: {file_size:.1f} KB")

    try:
        # Create S3 client
        s3_client = boto3.client('s3', region_name=S3_REGION)

        # Upload to S3
        print(f"[*] Uploading to S3...")

        s3_client.upload_file(
            str(LOCAL_FILE),
            S3_BUCKET,
            S3_KEY,
            ExtraArgs={
                'ContentType': 'image/webp',
                'CacheControl': 'public, max-age=31536000'  # 1 year cache
            }
        )

        # Generate public URL
        s3_url = f"https://{S3_BUCKET}.s3.{S3_REGION}.amazonaws.com/{S3_KEY}"

        print(f"[+] Upload complete!")
        print(f"\nS3 URL: {s3_url}")

        # Update index.html
        update_html(s3_url)

        print("\n" + "=" * 60)
        print("[SUCCESS] HERO BACKGROUND UPLOADED")
        print("=" * 60)
        print(f"URL: {s3_url}")
        print("=" * 60 + "\n")

    except ClientError as e:
        print(f"[!] AWS error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"[!] Upload error: {e}")
        sys.exit(1)


def update_html(s3_url):
    """Update index.html with S3 URL"""

    print(f"\n[*] Updating index.html with S3 URL...")

    try:
        html_path = Path('index.html')

        if not html_path.exists():
            print("[!] index.html not found - skipping update")
            return

        # Read current HTML
        html_content = html_path.read_text(encoding='utf-8')

        # Replace local path with S3 URL
        local_path = 'assets/backgrounds/hero-background-main.webp'
        updated_html = html_content.replace(local_path, s3_url)

        # Write updated HTML
        html_path.write_text(updated_html, encoding='utf-8')

        print(f"[+] index.html updated with S3 URL")

    except Exception as e:
        print(f"[!] Error updating HTML: {e}")
        # Don't fail - HTML update is optional


def main():
    """Main entry point"""
    try:
        upload_to_s3()
    except KeyboardInterrupt:
        print("\n\n[!] Upload interrupted by user")
        sys.exit(1)


if __name__ == '__main__':
    main()
