#!/usr/bin/env python3
"""
Upload Premium Assets to S3
Uploads all generated WebP assets to isnbiz-assets-1769962280 bucket
"""

import os
import sys
import boto3
from pathlib import Path
from botocore.exceptions import ClientError
import mimetypes

# Configuration
BUCKET_NAME = 'isnbiz-assets-1769962280'
BASE_DIR = Path("/mnt/d/workspace/ISNBIZ_Files/assets/premium")
S3_PREFIX = 'premium/'

def get_content_type(file_path):
    """Get content type for file"""
    content_type, _ = mimetypes.guess_type(str(file_path))
    if file_path.suffix == '.webp':
        return 'image/webp'
    return content_type or 'application/octet-stream'


def upload_to_s3(local_path, s3_key, bucket_name):
    """Upload file to S3 with proper metadata"""
    try:
        s3_client = boto3.client('s3')

        content_type = get_content_type(local_path)

        extra_args = {
            'ContentType': content_type,
            'CacheControl': 'public, max-age=31536000'  # 1 year cache
        }

        s3_client.upload_file(
            str(local_path),
            bucket_name,
            s3_key,
            ExtraArgs=extra_args
        )

        # Generate public URL
        url = f"https://{bucket_name}.s3.amazonaws.com/{s3_key}"
        return url

    except ClientError as e:
        print(f"Error uploading {local_path.name}: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error uploading {local_path.name}: {e}")
        return None


def upload_assets():
    """Upload all assets to S3"""
    print("=" * 80)
    print("UPLOADING PREMIUM ASSETS TO S3")
    print(f"Bucket: {BUCKET_NAME}")
    print("=" * 80)
    print()

    if not BASE_DIR.exists():
        print(f"ERROR: Asset directory not found: {BASE_DIR}")
        sys.exit(1)

    # Check AWS credentials
    try:
        s3_client = boto3.client('s3')
        s3_client.head_bucket(Bucket=BUCKET_NAME)
        print(f"✓ Connected to S3 bucket: {BUCKET_NAME}\n")
    except Exception as e:
        print(f"ERROR: Cannot connect to S3 bucket: {e}")
        print("\nMake sure AWS credentials are configured:")
        print("  aws configure")
        sys.exit(1)

    # Find all WebP files
    webp_files = list(BASE_DIR.rglob('*.webp'))

    if not webp_files:
        print(f"ERROR: No WebP files found in {BASE_DIR}")
        sys.exit(1)

    print(f"Found {len(webp_files)} assets to upload\n")

    successful = 0
    failed = 0
    urls = {}

    for i, file_path in enumerate(webp_files, 1):
        # Get relative path from base dir
        rel_path = file_path.relative_to(BASE_DIR)
        s3_key = f"{S3_PREFIX}{rel_path.as_posix()}"

        print(f"[{i}/{len(webp_files)}] Uploading: {rel_path}")

        url = upload_to_s3(file_path, s3_key, BUCKET_NAME)

        if url:
            successful += 1
            print(f"  ✓ URL: {url}")

            # Store URL by category and name
            category = rel_path.parent.name
            name = file_path.stem
            if category not in urls:
                urls[category] = {}
            urls[category][name] = url
        else:
            failed += 1
            print(f"  ✗ Failed")

        print()

    # Summary
    print("=" * 80)
    print("UPLOAD COMPLETE")
    print("=" * 80)
    print(f"Total files: {len(webp_files)}")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Success rate: {(successful/len(webp_files)*100):.1f}%")
    print("=" * 80)

    # Save URL manifest
    import json
    url_manifest_path = BASE_DIR / 'asset_urls.json'
    with open(url_manifest_path, 'w') as f:
        json.dump(urls, f, indent=2)

    print(f"\nAsset URLs saved to: {url_manifest_path}")

    # Generate HTML reference
    generate_html_reference(urls, BASE_DIR / 'asset_reference.html')


def generate_html_reference(urls, output_path):
    """Generate HTML reference page for all assets"""
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ISN.BIZ Premium Asset Library</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
            background: #f5f5f5;
            padding: 40px 20px;
        }
        .container {
            max-width: 1400px;
            margin: 0 auto;
        }
        h1 {
            color: #1E9FF2;
            margin-bottom: 10px;
            font-size: 2.5em;
        }
        .subtitle {
            color: #666;
            margin-bottom: 40px;
            font-size: 1.1em;
        }
        .category {
            background: white;
            border-radius: 12px;
            padding: 30px;
            margin-bottom: 40px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        .category h2 {
            color: #5FDFDF;
            margin-bottom: 20px;
            text-transform: uppercase;
            font-size: 1.8em;
            border-bottom: 3px solid #1E9FF2;
            padding-bottom: 10px;
        }
        .assets-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
        }
        .asset-card {
            background: #fafafa;
            border-radius: 8px;
            padding: 15px;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .asset-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 4px 12px rgba(30, 159, 242, 0.3);
        }
        .asset-card img {
            width: 100%;
            height: 200px;
            object-fit: cover;
            border-radius: 6px;
            margin-bottom: 10px;
            background: #e0e0e0;
        }
        .asset-name {
            font-weight: 600;
            color: #333;
            margin-bottom: 8px;
            font-size: 0.95em;
        }
        .asset-url {
            font-size: 0.75em;
            color: #1E9FF2;
            word-break: break-all;
            cursor: pointer;
            padding: 8px;
            background: #f0f9ff;
            border-radius: 4px;
        }
        .asset-url:hover {
            background: #e0f3ff;
        }
        .copy-btn {
            background: #1E9FF2;
            color: white;
            border: none;
            padding: 6px 12px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 0.85em;
            margin-top: 8px;
            width: 100%;
        }
        .copy-btn:hover {
            background: #5FDFDF;
        }
        .stats {
            background: linear-gradient(135deg, #1E9FF2, #5FDFDF);
            color: white;
            border-radius: 12px;
            padding: 30px;
            margin-bottom: 40px;
            display: flex;
            justify-content: space-around;
            flex-wrap: wrap;
        }
        .stat-item {
            text-align: center;
            padding: 10px;
        }
        .stat-number {
            font-size: 2.5em;
            font-weight: bold;
        }
        .stat-label {
            font-size: 1em;
            opacity: 0.9;
            margin-top: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>ISN.BIZ Premium Asset Library</h1>
        <p class="subtitle">Award-winning quality assets generated with fal.ai</p>

        <div class="stats">
"""

    total_assets = sum(len(assets) for assets in urls.values())
    html += f"""
            <div class="stat-item">
                <div class="stat-number">{total_assets}</div>
                <div class="stat-label">Total Assets</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">{len(urls)}</div>
                <div class="stat-label">Categories</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">WebP</div>
                <div class="stat-label">Optimized Format</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">90</div>
                <div class="stat-label">Quality</div>
            </div>
        </div>
"""

    category_names = {
        'hero': 'Hero Backgrounds',
        'icons': 'Service Icons',
        'portfolio': 'Portfolio Mockups',
        'backgrounds': 'Abstract Backgrounds',
        'infographics': 'Infographics & Illustrations'
    }

    for category, assets in sorted(urls.items()):
        display_name = category_names.get(category, category.title())
        html += f"""
        <div class="category">
            <h2>{display_name} ({len(assets)})</h2>
            <div class="assets-grid">
"""

        for name, url in sorted(assets.items()):
            html += f"""
                <div class="asset-card">
                    <img src="{url}" alt="{name}" loading="lazy">
                    <div class="asset-name">{name.replace('_', ' ').title()}</div>
                    <div class="asset-url" title="Click to copy">{url}</div>
                    <button class="copy-btn" onclick="copyToClipboard('{url}', this)">Copy URL</button>
                </div>
"""

        html += """
            </div>
        </div>
"""

    html += """
    </div>

    <script>
        function copyToClipboard(text, button) {
            navigator.clipboard.writeText(text).then(() => {
                const originalText = button.textContent;
                button.textContent = '✓ Copied!';
                button.style.background = '#4CAF50';
                setTimeout(() => {
                    button.textContent = originalText;
                    button.style.background = '#1E9FF2';
                }, 2000);
            }).catch(err => {
                alert('Failed to copy: ' + err);
            });
        }
    </script>
</body>
</html>
"""

    with open(output_path, 'w') as f:
        f.write(html)

    print(f"HTML reference page saved to: {output_path}")


if __name__ == '__main__':
    upload_assets()
