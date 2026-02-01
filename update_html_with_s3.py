#!/usr/bin/env python3
"""Update HTML files to use S3 WebP assets"""
from pathlib import Path
import re

S3_BASE = "https://isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com"

html_files = Path("/mnt/d/workspace/ISNBIZ_Files").glob("*.html")

for html_file in html_files:
    content = html_file.read_text()
    original = content
    
    # Update local asset references to S3 WebP
    # Replace PNG with WebP for generated assets
    content = re.sub(
        r'src="assets/generated/([^"]+)\.png"',
        f'src="{S3_BASE}/assets/generated/\\1.webp"',
        content
    )
    
    # Replace local portfolio mockups with S3 WebP
    content = re.sub(
        r'src="assets/generated/portfolio/([^"]+)\.png"',
        f'src="{S3_BASE}/assets/generated/portfolio/\\1.webp"',
        content
    )
    
    # Keep logos as PNG (already optimized)
    content = re.sub(
        r'src="logo-pallete/([^"]+)"',
        f'src="{S3_BASE}/logo-pallete/\\1"',
        content
    )
    
    if content != original:
        html_file.write_text(content)
        print(f"✓ Updated: {html_file.name}")

print("\n✅ All HTML files updated with S3 URLs!")
