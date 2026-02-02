#!/usr/bin/env python3
"""
Project Icon Generator for ISN.BIZ Portfolio
Generates 8 clean, professional icon-style images with transparent or minimal backgrounds
"""

import os
import sys
import time
import requests
from pathlib import Path
from PIL import Image
from io import BytesIO
import json
import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
FAL_API_KEY = os.getenv('FAL_API_KEY')
if not FAL_API_KEY:
    print("ERROR: FAL_API_KEY not found in .env file")
    sys.exit(1)

BUCKET_NAME = 'isnbiz-assets-1769962280'
BASE_DIR = Path("/home/jdmal/workspace/ISNBIZ_Files/assets/premium_v3/icons")
S3_PREFIX = 'premium_v3/icons/'
MODEL = "fal-ai/flux-pro/v1.1-ultra"

# Brand colors
BRAND_BLUE = '#1E9FF2'
BRAND_CYAN = '#5FDFDF'

# Icon definitions - 512x512, clean professional icons
ICONS = [
    {
        'name': 'infrastructure_icon',
        'prompt': f'Professional minimalist icon of server infrastructure and network, clean geometric server rack with network connections, simple line art style, {BRAND_BLUE} and {BRAND_CYAN} gradient colors on transparent or white background, isometric view, 512x512 icon, ultra clean, corporate design, flat design aesthetic, centered composition',
        'description': 'Infrastructure icon (server/network)'
    },
    {
        'name': 'video_production_icon',
        'prompt': f'Professional minimalist icon of video production and media, clean geometric video camera or play button with film strip, simple line art style, {BRAND_BLUE} and {BRAND_CYAN} gradient colors on transparent or white background, 512x512 icon, ultra clean, corporate design, flat design aesthetic, centered composition',
        'description': 'Video icon (production/media)'
    },
    {
        'name': 'security_icon',
        'prompt': f'Professional minimalist icon of security and protection, clean geometric shield with lock symbol, simple line art style, {BRAND_BLUE} and {BRAND_CYAN} gradient colors on transparent or white background, 512x512 icon, ultra clean, corporate design, flat design aesthetic, centered composition',
        'description': 'Security icon (shield/lock)'
    },
    {
        'name': 'cli_terminal_icon',
        'prompt': f'Professional minimalist icon of command line interface and terminal, clean geometric terminal window with code symbols, simple line art style, {BRAND_BLUE} and {BRAND_CYAN} gradient colors on transparent or white background, 512x512 icon, ultra clean, corporate design, flat design aesthetic, centered composition',
        'description': 'CLI icon (terminal/code)'
    },
    {
        'name': 'ai_comfyui_icon',
        'prompt': f'Professional minimalist icon of AI and neural networks, clean geometric brain with circuit connections or neural pathways, simple line art style, {BRAND_BLUE} and {BRAND_CYAN} gradient colors on transparent or white background, 512x512 icon, ultra clean, corporate design, flat design aesthetic, centered composition',
        'description': 'AI/ComfyUI icon (neural network)'
    },
    {
        'name': 'data_analytics_icon',
        'prompt': f'Professional minimalist icon of data and analytics, clean geometric database with chart or graph, simple line art style, {BRAND_BLUE} and {BRAND_CYAN} gradient colors on transparent or white background, 512x512 icon, ultra clean, corporate design, flat design aesthetic, centered composition',
        'description': 'Data icon (database/chart)'
    },
    {
        'name': 'llm_optimization_icon',
        'prompt': f'Professional minimalist icon of language model optimization, clean geometric brain with optimization symbols or gears, simple line art style, {BRAND_BLUE} and {BRAND_CYAN} gradient colors on transparent or white background, 512x512 icon, ultra clean, corporate design, flat design aesthetic, centered composition',
        'description': 'LLM icon (brain/optimization)'
    },
    {
        'name': 'discovery_search_icon',
        'prompt': f'Professional minimalist icon of discovery and search, clean geometric magnifying glass with data or search elements, simple line art style, {BRAND_BLUE} and {BRAND_CYAN} gradient colors on transparent or white background, 512x512 icon, ultra clean, corporate design, flat design aesthetic, centered composition',
        'description': 'Discovery icon (search/magnify)'
    }
]


def call_fal_api(prompt, seed=None):
    """Call fal.ai API to generate icon"""
    url = f"https://fal.run/{MODEL}"

    headers = {
        "Authorization": f"Key {FAL_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "prompt": prompt,
        "image_size": {
            "width": 512,
            "height": 512
        },
        "num_inference_steps": 28,
        "guidance_scale": 3.5,
        "num_images": 1,
        "enable_safety_checker": False,
        "output_format": "png"
    }

    if seed:
        payload["seed"] = seed

    try:
        print(f"  Calling API...")
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()

        if 'images' in result and len(result['images']) > 0:
            return result['images'][0]['url']
        else:
            print(f"  Unexpected response format: {result}")
            return None

    except Exception as e:
        print(f"  API Error: {str(e)}")
        if hasattr(e, 'response') and e.response:
            print(f"  Response: {e.response.text}")
        return None


def download_and_save_webp(image_url, output_path, quality=95):
    """Download image and save as WebP with transparency preservation"""
    try:
        print(f"  Downloading image...")
        response = requests.get(image_url)
        response.raise_for_status()

        img = Image.open(BytesIO(response.content))

        # Preserve transparency if present, otherwise convert to RGB
        if img.mode in ('RGBA', 'LA'):
            # Keep transparency
            img.save(output_path, 'WEBP', quality=quality, method=6, lossless=False)
        else:
            # Convert to RGB for solid backgrounds
            if img.mode != 'RGB':
                img = img.convert('RGB')
            img.save(output_path, 'WEBP', quality=quality, method=6)

        print(f"  [OK] Saved: {output_path.name}")
        return True

    except Exception as e:
        print(f"  [FAIL] Error saving {output_path.name}: {str(e)}")
        return False


def upload_to_s3(local_path, s3_key):
    """Upload file to S3 with proper metadata"""
    try:
        s3_client = boto3.client('s3')

        extra_args = {
            'ContentType': 'image/webp',
            'CacheControl': 'public, max-age=31536000'  # 1 year cache
        }

        s3_client.upload_file(
            str(local_path),
            BUCKET_NAME,
            s3_key,
            ExtraArgs=extra_args
        )

        url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{s3_key}"
        print(f"  [OK] Uploaded to S3: {s3_key}")
        return url

    except Exception as e:
        print(f"  [FAIL] S3 upload error: {e}")
        return None


def generate_icons():
    """Generate all project icons"""
    print("=" * 80)
    print("PROJECT ICON GENERATOR")
    print("Generating 8 clean professional icons for ISN.BIZ portfolio")
    print("=" * 80)
    print()

    # Create output directory
    BASE_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Output directory: {BASE_DIR}")
    print()

    # Check AWS credentials
    try:
        s3_client = boto3.client('s3')
        s3_client.head_bucket(Bucket=BUCKET_NAME)
        print(f"[OK] Connected to S3 bucket: {BUCKET_NAME}")
    except Exception as e:
        print(f"[WARNING] Cannot connect to S3: {e}")
        print("  Will generate icons locally only")
    print()

    results = []
    successful = 0
    failed = 0

    for i, icon in enumerate(ICONS, 1):
        print(f"[{i}/{len(ICONS)}] {icon['description']}")
        print(f"  Name: {icon['name']}.webp")

        # Generate image
        image_url = call_fal_api(icon['prompt'])

        if not image_url:
            print(f"  [FAIL] Failed to generate")
            failed += 1
            continue

        # Save locally
        output_path = BASE_DIR / f"{icon['name']}.webp"
        if not download_and_save_webp(image_url, output_path):
            failed += 1
            continue

        # Upload to S3
        s3_key = f"{S3_PREFIX}{icon['name']}.webp"
        s3_url = upload_to_s3(output_path, s3_key)

        if s3_url:
            successful += 1
            results.append({
                'name': icon['name'],
                'description': icon['description'],
                'local_path': str(output_path),
                's3_url': s3_url
            })
        else:
            failed += 1

        print()

        # Rate limiting
        if i < len(ICONS):
            print("  Waiting 2 seconds...")
            time.sleep(2)

    # Summary
    print("=" * 80)
    print("GENERATION COMPLETE")
    print("=" * 80)
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Total: {len(ICONS)}")
    print()

    if results:
        print("GENERATED ICONS:")
        print()
        for result in results:
            print(f"  {result['description']}")
            print(f"    Local:  {result['local_path']}")
            print(f"    S3 URL: {result['s3_url']}")
            print()

        # Save URLs to file
        urls_file = BASE_DIR / 'icon_urls.txt'
        with open(urls_file, 'w') as f:
            f.write("ISN.BIZ Project Icons - S3 URLs\n")
            f.write("=" * 80 + "\n\n")
            for result in results:
                f.write(f"{result['description']}\n")
                f.write(f"{result['s3_url']}\n\n")

        print(f"URLs saved to: {urls_file}")
        print()

        # HTML snippet
        print("HTML USAGE:")
        print()
        for result in results:
            print(f'<img src="{result["s3_url"]}" alt="{result["description"]}" class="project-icon">')
        print()


if __name__ == '__main__':
    generate_icons()
