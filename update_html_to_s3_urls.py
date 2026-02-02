#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Update all HTML files to use S3 URLs instead of local asset paths
Reads the s3_url_mapping.json file and updates all HTML files
"""

import os
import sys
import io

# Fix Windows console encoding
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

import json
import re
from pathlib import Path

def update_html_file(html_file, url_mapping):
    """Update a single HTML file with S3 URLs"""
    print(f"\n📄 Processing: {html_file}")

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    replacements = 0

    # Replace each local path with S3 URL
    for local_path, s3_url in url_mapping.items():
        # Normalize paths for matching
        local_path_unix = local_path.replace('\\', '/')

        # Try different path variations
        patterns = [
            local_path_unix,  # Full path
            local_path_unix.replace('assets/', ''),  # Without assets/ prefix
            f'"{local_path_unix}"',  # Quoted
            f"'{local_path_unix}'",  # Single quoted
        ]

        for pattern in patterns:
            if pattern in content:
                content = content.replace(pattern, s3_url)
                replacements += 1

    if replacements > 0:
        # Backup original
        backup_file = f"{html_file}.backup"
        with open(backup_file, 'w', encoding='utf-8') as f:
            f.write(original_content)

        # Write updated content
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"  ✅ Updated {replacements} references")
        print(f"  📋 Backup saved to: {backup_file}")
    else:
        print(f"  ℹ No changes needed")

    return replacements

def main():
    print("="*80)
    print("  UPDATE HTML FILES TO USE S3 URLS")
    print("="*80)
    print()

    # Load URL mapping
    mapping_file = "s3_url_mapping.json"
    if not os.path.exists(mapping_file):
        print(f"❌ Error: {mapping_file} not found!")
        print("   Run upload_images_to_s3.py first to generate the mapping file.")
        return 1

    with open(mapping_file, 'r') as f:
        url_mapping = json.load(f)

    print(f"📂 Loaded {len(url_mapping)} URL mappings from {mapping_file}")

    # Find all HTML files
    html_files = list(Path('.').glob('*.html'))

    print(f"📝 Found {len(html_files)} HTML files to update")

    total_replacements = 0

    for html_file in html_files:
        # Skip backup files
        if str(html_file).endswith('.backup'):
            continue

        replacements = update_html_file(str(html_file), url_mapping)
        total_replacements += replacements

    print("\n" + "="*80)
    print("  UPDATE COMPLETE")
    print("="*80)
    print(f"\n📊 Summary:")
    print(f"  HTML files processed: {len(html_files)}")
    print(f"  Total replacements:   {total_replacements}")
    print(f"\n✅ All HTML files now reference S3 URLs")
    print(f"   Images will be served from: https://isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com/")
    print(f"\n💡 To restore originals, use the .backup files")
    print("="*80)

if __name__ == "__main__":
    main()
