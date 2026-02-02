#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate uniform founder headshots and corporate photos using fal.ai gpt-image-1.5/edit
"""

import os
import sys
import fal_client
import base64
from pathlib import Path
import json
from datetime import datetime

# Fix Windows console encoding
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Configure fal.ai API
os.environ['FAL_KEY'] = '64b786c3-d6b1-4fbb-9d46-9211ceea552f:d472cdf8c68b4fe873557ca33bfb25eb'

# Output directories
OUTPUT_DIR = Path("assets/founders")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

HEADSHOTS_BG_DIR = OUTPUT_DIR / "headshots_with_bg"
HEADSHOTS_NO_BG_DIR = OUTPUT_DIR / "headshots_no_bg"
CORPORATE_DIR = OUTPUT_DIR / "corporate_photos"

HEADSHOTS_BG_DIR.mkdir(exist_ok=True)
HEADSHOTS_NO_BG_DIR.mkdir(exist_ok=True)
CORPORATE_DIR.mkdir(exist_ok=True)

# Founder images
FOUNDERS = {
    'alicia': '1/a1.png',
    'bri': '1/b1.png',
    'jonathan': '1/j1.png',
    'lilly': '1/l1.png'
}

def upload_image_to_fal(image_path):
    """Upload image to fal.ai and return URL"""
    print(f"  📤 Uploading {image_path}...")
    with open(image_path, 'rb') as f:
        image_data = f.read()

    url = fal_client.upload(image_data, "image/png")
    print(f"  ✅ Uploaded to: {url}")
    return url

def generate_headshot_with_bg(founder_name, image_url):
    """Generate professional headshot with uniform background"""
    print(f"\n🎨 Generating professional headshot with background for {founder_name}...")

    prompt = f"""Professional corporate headshot portrait. The person should have the EXACT SAME FACE as in the original image - preserve all facial features, skin tone, hair style, and facial structure perfectly. Clean professional studio background in soft neutral gray or blue tones. Professional business attire. Soft professional lighting. Corporate photography style. The face must look identical to the original photo - same person, same features, same appearance."""

    result = fal_client.subscribe(
        "fal-ai/gpt-image-1.5/edit",
        arguments={
            "image_urls": [image_url],
            "prompt": prompt,
            "image_quality": "low",  # Low quality = high quality but cheaper
            "num_images": 1,
            "output_format": "png"
        },
    )

    if result and 'images' in result and len(result['images']) > 0:
        output_url = result['images'][0]['url']
        print(f"  ✅ Generated: {output_url}")
        return output_url
    else:
        print(f"  ❌ Failed to generate headshot")
        return None

def generate_headshot_no_bg(founder_name, image_url):
    """Generate professional headshot with transparent/no background"""
    print(f"\n🎨 Generating headshot with no background for {founder_name}...")

    prompt = f"""Professional corporate headshot portrait with transparent background removed. The person should have the EXACT SAME FACE as in the original image - preserve all facial features, skin tone, hair style, and facial structure perfectly. Remove all background completely - pure transparent or white background. Professional business attire. The face must look identical to the original photo - same person, same features, same appearance. Clean cutout style."""

    result = fal_client.subscribe(
        "fal-ai/gpt-image-1.5/edit",
        arguments={
            "image_urls": [image_url],
            "prompt": prompt,
            "image_quality": "low",
            "num_images": 1,
            "output_format": "png"
        },
    )

    if result and 'images' in result and len(result['images']) > 0:
        output_url = result['images'][0]['url']
        print(f"  ✅ Generated: {output_url}")
        return output_url
    else:
        print(f"  ❌ Failed to generate no-bg headshot")
        return None

def generate_corporate_photo(founder_name, image_url, activity):
    """Generate corporate activity photo (not looking at camera)"""
    print(f"\n🎨 Generating corporate photo ({activity}) for {founder_name}...")

    activities = {
        'presenting': 'presenting at a corporate meeting with presentation screen behind, looking at presentation, professional business setting',
        'working': 'working on laptop in modern office, focused on screen, professional workspace with technology',
        'collaborating': 'collaborating with team in modern conference room, looking at documents or screen, professional business environment',
        'analyzing': 'analyzing data or documents, looking down at papers or tablet, professional office setting'
    }

    activity_desc = activities.get(activity, activities['working'])

    prompt = f"""Professional corporate photo of person {activity_desc}. The person should have the EXACT SAME FACE as in the original image - preserve all facial features, skin tone, hair style, and facial structure perfectly. NOT looking directly at camera - looking at work, screen, documents, or colleagues. Professional business attire. Natural corporate environment. Corporate photography style. The face must look identical to the original photo - same person, same features, same appearance."""

    result = fal_client.subscribe(
        "fal-ai/gpt-image-1.5/edit",
        arguments={
            "image_urls": [image_url],
            "prompt": prompt,
            "image_quality": "low",
            "num_images": 1,
            "output_format": "png"
        },
    )

    if result and 'images' in result and len(result['images']) > 0:
        output_url = result['images'][0]['url']
        print(f"  ✅ Generated: {output_url}")
        return output_url
    else:
        print(f"  ❌ Failed to generate corporate photo")
        return None

def download_image(url, output_path):
    """Download image from URL"""
    import requests
    print(f"  💾 Downloading to {output_path}...")
    response = requests.get(url)
    if response.status_code == 200:
        with open(output_path, 'wb') as f:
            f.write(response.content)
        print(f"  ✅ Saved!")
        return True
    else:
        print(f"  ❌ Download failed: {response.status_code}")
        return False

def main():
    print("=" * 80)
    print("🎯 FOUNDER HEADSHOT & CORPORATE PHOTO GENERATOR")
    print("=" * 80)
    print(f"Model: fal-ai/gpt-image-1.5/edit")
    print(f"Quality: low (high quality, lower cost)")
    print(f"Founders: {len(FOUNDERS)}")
    print("=" * 80)

    results = {
        'generation_time': datetime.now().isoformat(),
        'model': 'fal-ai/gpt-image-1.5/edit',
        'founders': {}
    }

    # Corporate activities to generate for each founder
    corporate_activities = ['presenting', 'working', 'collaborating', 'analyzing']

    for founder_name, image_path in FOUNDERS.items():
        print(f"\n{'=' * 80}")
        print(f"👤 Processing: {founder_name.upper()}")
        print(f"{'=' * 80}")

        if not os.path.exists(image_path):
            print(f"  ❌ Image not found: {image_path}")
            continue

        results['founders'][founder_name] = {
            'original': image_path,
            'headshot_with_bg': None,
            'headshot_no_bg': None,
            'corporate_photos': {}
        }

        # Upload original image
        try:
            image_url = upload_image_to_fal(image_path)
        except Exception as e:
            print(f"  ❌ Upload failed: {e}")
            continue

        # 1. Generate headshot with background
        try:
            headshot_bg_url = generate_headshot_with_bg(founder_name, image_url)
            if headshot_bg_url:
                output_file = HEADSHOTS_BG_DIR / f"{founder_name}_headshot.png"
                if download_image(headshot_bg_url, output_file):
                    results['founders'][founder_name]['headshot_with_bg'] = str(output_file)
        except Exception as e:
            print(f"  ❌ Headshot with BG failed: {e}")

        # 2. Generate headshot without background
        try:
            headshot_no_bg_url = generate_headshot_no_bg(founder_name, image_url)
            if headshot_no_bg_url:
                output_file = HEADSHOTS_NO_BG_DIR / f"{founder_name}_headshot_no_bg.png"
                if download_image(headshot_no_bg_url, output_file):
                    results['founders'][founder_name]['headshot_no_bg'] = str(output_file)
        except Exception as e:
            print(f"  ❌ Headshot no BG failed: {e}")

        # 3. Generate corporate activity photos
        for activity in corporate_activities:
            try:
                corporate_url = generate_corporate_photo(founder_name, image_url, activity)
                if corporate_url:
                    output_file = CORPORATE_DIR / f"{founder_name}_{activity}.png"
                    if download_image(corporate_url, output_file):
                        results['founders'][founder_name]['corporate_photos'][activity] = str(output_file)
            except Exception as e:
                print(f"  ❌ Corporate photo ({activity}) failed: {e}")

    # Save results manifest
    manifest_file = OUTPUT_DIR / "generation_manifest.json"
    with open(manifest_file, 'w') as f:
        json.dump(results, f, indent=2)

    print("\n" + "=" * 80)
    print("✅ GENERATION COMPLETE!")
    print("=" * 80)
    print(f"\n📁 Output directories:")
    print(f"  • Headshots (with BG): {HEADSHOTS_BG_DIR}")
    print(f"  • Headshots (no BG):   {HEADSHOTS_NO_BG_DIR}")
    print(f"  • Corporate photos:    {CORPORATE_DIR}")
    print(f"  • Manifest:            {manifest_file}")

    print(f"\n📊 Summary:")
    for founder_name, data in results['founders'].items():
        print(f"\n  {founder_name.upper()}:")
        print(f"    ✓ Headshot w/ BG:  {'✅' if data['headshot_with_bg'] else '❌'}")
        print(f"    ✓ Headshot no BG:  {'✅' if data['headshot_no_bg'] else '❌'}")
        print(f"    ✓ Corporate photos: {len(data['corporate_photos'])}/4")

    print("\n" + "=" * 80)

if __name__ == "__main__":
    main()
