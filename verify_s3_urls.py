#!/usr/bin/env python3
"""
S3 URL Verification Script for ISNBIZ Website
Extracts all S3 URLs from HTML/CSS files and verifies accessibility
"""

import re
import requests
from pathlib import Path
from typing import Dict, List, Tuple
from collections import defaultdict
import time

# S3 base URL patterns
S3_BASE_URL = "https://isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com/premium_v3/"
S3_BASE_URL_ALT = "https://isnbiz-assets-1769962280.s3.us-east-2.amazonaws.com/premium_v3/"

def extract_s3_urls_from_file(file_path: Path) -> List[str]:
    """Extract all S3 URLs from a file"""
    urls = []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

            # Pattern to match S3 URLs
            pattern = r'https://isnbiz-assets-1769962280\.s3\.us-east-[12]\.amazonaws\.com/premium_v3/[^"\'\s)>]+'
            matches = re.findall(pattern, content)
            urls.extend(matches)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

    return urls

def categorize_url(url: str) -> str:
    """Categorize URL by asset type"""
    if '/logos/' in url:
        return 'logos'
    elif '/hero/' in url:
        return 'hero'
    elif '/services/' in url:
        return 'services'
    elif '/portfolio/' in url:
        return 'portfolio'
    elif '/gallery/' in url:
        return 'gallery'
    elif '/founders/' in url:
        return 'founders'
    elif '/sections/' in url:
        return 'sections'
    elif '/og/' in url:
        return 'og'
    else:
        return 'other'

def test_url(url: str) -> Tuple[bool, int, Dict]:
    """Test if URL is accessible and return status info"""
    try:
        response = requests.head(url, timeout=10, allow_redirects=True)
        headers = {
            'status_code': response.status_code,
            'content_type': response.headers.get('Content-Type', 'unknown'),
            'content_length': response.headers.get('Content-Length', '0'),
            'cache_control': response.headers.get('Cache-Control', 'none'),
            'last_modified': response.headers.get('Last-Modified', 'unknown')
        }
        return (response.status_code == 200, response.status_code, headers)
    except requests.exceptions.RequestException as e:
        return (False, 0, {'error': str(e)})

def main():
    """Main verification function"""
    print("=" * 80)
    print("S3 URL Verification for ISNBIZ Website")
    print("=" * 80)
    print()

    # Find all HTML and CSS files
    base_dir = Path(__file__).parent
    html_files = list(base_dir.glob('*.html'))
    css_files = list(base_dir.glob('*.css'))

    all_files = html_files + css_files
    print(f"Scanning {len(all_files)} files ({len(html_files)} HTML, {len(css_files)} CSS)")
    print()

    # Extract all URLs
    all_urls = set()
    for file in all_files:
        urls = extract_s3_urls_from_file(file)
        if urls:
            print(f"  {file.name}: {len(urls)} URLs")
            all_urls.update(urls)

    print()
    print(f"Total unique URLs found: {len(all_urls)}")
    print()

    # Categorize URLs
    categorized = defaultdict(list)
    for url in sorted(all_urls):
        category = categorize_url(url)
        categorized[category].append(url)

    print("URLs by category:")
    for category, urls in sorted(categorized.items()):
        print(f"  {category}: {len(urls)}")
    print()

    # Test each URL
    print("Testing URL accessibility...")
    print()

    results = {
        'success': [],
        'failed': [],
        'total_size': 0
    }

    category_results = defaultdict(lambda: {'success': 0, 'failed': 0, 'size': 0})

    for i, url in enumerate(sorted(all_urls), 1):
        category = categorize_url(url)
        filename = url.split('/')[-1]

        print(f"[{i}/{len(all_urls)}] Testing {category}/{filename}...", end=' ')

        success, status_code, headers = test_url(url)

        if success:
            size = int(headers.get('content_length', 0))
            results['success'].append({
                'url': url,
                'category': category,
                'headers': headers,
                'size': size
            })
            results['total_size'] += size
            category_results[category]['success'] += 1
            category_results[category]['size'] += size
            print(f"OK ({status_code}) - {size:,} bytes")
        else:
            results['failed'].append({
                'url': url,
                'category': category,
                'status_code': status_code,
                'error': headers.get('error', 'Unknown error')
            })
            category_results[category]['failed'] += 1
            print(f"FAILED ({status_code}) - {headers.get('error', 'Unknown')}")

        # Small delay to avoid rate limiting
        time.sleep(0.1)

    print()
    print("=" * 80)
    print("VERIFICATION SUMMARY")
    print("=" * 80)
    print()

    print(f"Total URLs tested: {len(all_urls)}")
    print(f"Successful (200 OK): {len(results['success'])} ({len(results['success'])*100//len(all_urls)}%)")
    print(f"Failed: {len(results['failed'])} ({len(results['failed'])*100//len(all_urls) if all_urls else 0}%)")
    print(f"Total bandwidth: {results['total_size']:,} bytes ({results['total_size']/1024/1024:.2f} MB)")
    print()

    print("Results by category:")
    print()
    for category in sorted(category_results.keys()):
        data = category_results[category]
        total = data['success'] + data['failed']
        print(f"  {category:12} - Success: {data['success']:2}/{total:2} ({data['success']*100//total if total else 0:3}%)  "
              f"Size: {data['size']/1024:7.1f} KB")
    print()

    if results['failed']:
        print("FAILED URLs:")
        print()
        for item in results['failed']:
            print(f"  [{item['category']}] {item['url']}")
            print(f"    Status: {item['status_code']} - {item['error']}")
        print()

    # Generate markdown report
    report_path = base_dir / 'assets' / 'premium_v3' / 'S3_VERIFICATION_REPORT.md'
    report_path.parent.mkdir(parents=True, exist_ok=True)

    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("# S3 Asset Verification Report\n\n")
        f.write(f"**Date:** {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"**Base URL:** `{S3_BASE_URL}`\n\n")
        f.write("## Summary\n\n")
        f.write(f"- **Total URLs tested:** {len(all_urls)}\n")
        f.write(f"- **Successful (200 OK):** {len(results['success'])} ({len(results['success'])*100//len(all_urls)}%)\n")
        f.write(f"- **Failed:** {len(results['failed'])} ({len(results['failed'])*100//len(all_urls) if all_urls else 0}%)\n")
        f.write(f"- **Total bandwidth:** {results['total_size']:,} bytes ({results['total_size']/1024/1024:.2f} MB)\n\n")

        f.write("## Results by Category\n\n")
        f.write("| Category | Success | Failed | Total | Success Rate | Size (KB) |\n")
        f.write("|----------|---------|--------|-------|--------------|----------|\n")
        for category in sorted(category_results.keys()):
            data = category_results[category]
            total = data['success'] + data['failed']
            f.write(f"| {category} | {data['success']} | {data['failed']} | {total} | "
                   f"{data['success']*100//total if total else 0}% | {data['size']/1024:.1f} |\n")
        f.write("\n")

        if results['failed']:
            f.write("## Failed URLs\n\n")
            for item in results['failed']:
                f.write(f"### [{item['category']}] {item['url'].split('/')[-1]}\n\n")
                f.write(f"- **URL:** `{item['url']}`\n")
                f.write(f"- **Status Code:** {item['status_code']}\n")
                f.write(f"- **Error:** {item['error']}\n\n")

        f.write("## Successful URLs by Category\n\n")
        for category in sorted(categorized.keys()):
            f.write(f"### {category.upper()}\n\n")
            for url in sorted(categorized[category]):
                filename = url.split('/')[-1]
                # Find size
                size = 0
                for item in results['success']:
                    if item['url'] == url:
                        size = item['size']
                        break
                f.write(f"- OK `{filename}` ({size:,} bytes)\n")
            f.write("\n")

        f.write("## Cache Headers Verification\n\n")
        cache_controls = defaultdict(int)
        for item in results['success']:
            cache_control = item['headers'].get('cache_control', 'none')
            cache_controls[cache_control] += 1

        f.write("| Cache-Control | Count |\n")
        f.write("|---------------|-------|\n")
        for cc, count in sorted(cache_controls.items()):
            f.write(f"| `{cc}` | {count} |\n")
        f.write("\n")

        f.write("## Content Types\n\n")
        content_types = defaultdict(int)
        for item in results['success']:
            content_type = item['headers'].get('content_type', 'unknown')
            content_types[content_type] += 1

        f.write("| Content-Type | Count |\n")
        f.write("|--------------|-------|\n")
        for ct, count in sorted(content_types.items()):
            f.write(f"| `{ct}` | {count} |\n")
        f.write("\n")

        f.write("---\n\n")
        f.write("*Report generated automatically by `verify_s3_urls.py`*\n")

    print(f"Detailed report saved to: {report_path}")
    print()

    return len(results['failed']) == 0

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
