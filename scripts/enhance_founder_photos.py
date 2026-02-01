#!/usr/bin/env python3
"""
Enhance HROC founder photos using fal.ai Portrait Enhance API
Uses ACTUAL founder photos and creates professional enhanced versions
"""

import os
import sys
import json
import base64
import requests
from pathlib import Path
from typing import List, Dict
import time

# Configuration
FAL_API_KEY = os.getenv('FAL_API_KEY')
if not FAL_API_KEY:
    print("ERROR: FAL_API_KEY environment variable not set")
    print("Please set it with: export FAL_API_KEY='your-key-here'")
    sys.exit(1)

# Paths
SOURCE_DIR = Path("/mnt/d/workspace/projects/HROC_Files/HROC_Website_New/images/founders")
OUTPUT_DIR = Path("/mnt/d/workspace/ISNBIZ_Files/assets/team")

# Founder photo configurations
FOUNDERS = {
    "alicia": {
        "source_photos": [
            SOURCE_DIR / "a" / "alicia_hero_real.webp",
            SOURCE_DIR / "a" / "alicia_office_real.webp",
            SOURCE_DIR / "a" / "alicia_whiteboard_real.webp",
        ],
        "contexts": ["professional_headshot", "office_setting", "presentation"]
    },
    "bri": {
        "source_photos": [
            SOURCE_DIR / "b" / "bri_varied_01.webp",
            SOURCE_DIR / "b" / "bri_varied_02.webp",
            SOURCE_DIR / "b" / "bri_varied_03.webp",
        ],
        "contexts": ["professional_headshot", "business_casual", "leadership"]
    },
    "jonathan": {
        "source_photos": [
            SOURCE_DIR / "j" / "jonathan_varied_01.webp",
            SOURCE_DIR / "j" / "jonathan_varied_02.webp",
            SOURCE_DIR / "j" / "jonathan_varied_03.webp",
        ],
        "contexts": ["professional_headshot", "tech_leader", "executive"]
    },
    "lilly": {
        "source_photos": [
            SOURCE_DIR / "l" / "lilly_varied_01.webp",
            SOURCE_DIR / "l" / "lilly_varied_02.webp",
            SOURCE_DIR / "l" / "lilly_varied_03.webp",
        ],
        "contexts": ["professional_headshot", "office_professional", "wellness_leader"]
    }
}


def upload_image_to_fal(image_path: Path) -> str:
    """Upload image to fal.ai storage and return URL"""
    print(f"  Uploading {image_path.name}...")

    # Read image file
    with open(image_path, 'rb') as f:
        image_data = f.read()

    # Upload to fal.ai storage
    upload_url = "https://fal.run/fal-ai/files/upload"
    headers = {
        "Authorization": f"Key {FAL_API_KEY}",
        "Content-Type": "application/octet-stream"
    }

    response = requests.post(
        upload_url,
        headers=headers,
        data=image_data
    )

    if response.status_code != 200:
        raise Exception(f"Upload failed: {response.text}")

    result = response.json()
    uploaded_url = result.get('url') or result.get('file_url')
    print(f"  Uploaded to: {uploaded_url}")
    return uploaded_url


def enhance_portrait(image_url: str, output_path: Path) -> bool:
    """Enhance a portrait using fal.ai Portrait Enhance API"""
    print(f"  Enhancing portrait...")

    api_url = "https://fal.run/fal-ai/image-apps-v2/portrait-enhance"
    headers = {
        "Authorization": f"Key {FAL_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "image_url": image_url,
        "aspect_ratio": "3:4"  # Professional portrait aspect ratio
    }

    response = requests.post(api_url, headers=headers, json=payload)

    if response.status_code != 200:
        print(f"  ERROR: Enhancement failed: {response.text}")
        return False

    result = response.json()

    # Download enhanced image
    enhanced_image_url = result.get('image', {}).get('url') if isinstance(result.get('image'), dict) else result.get('image')

    if not enhanced_image_url:
        print(f"  ERROR: No image URL in response: {result}")
        return False

    print(f"  Downloading enhanced image from: {enhanced_image_url}")
    image_response = requests.get(enhanced_image_url)

    if image_response.status_code != 200:
        print(f"  ERROR: Failed to download enhanced image")
        return False

    # Save enhanced image
    with open(output_path, 'wb') as f:
        f.write(image_response.content)

    file_size = len(image_response.content) / 1024  # KB
    print(f"  ✓ Saved enhanced image: {output_path.name} ({file_size:.1f} KB)")
    return True


def enhance_with_flux_ultra(image_url: str, prompt: str, output_path: Path) -> bool:
    """Enhance using FLUX 1.1 Pro Ultra for image-to-image enhancement"""
    print(f"  Enhancing with FLUX Ultra...")

    api_url = "https://fal.run/fal-ai/flux-pro/v1.1-ultra"
    headers = {
        "Authorization": f"Key {FAL_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "prompt": prompt,
        "image_url": image_url,
        "image_prompt_strength": 0.75,  # Strong influence from source image
        "num_images": 1,
        "output_format": "png",
        "safety_tolerance": 5
    }

    response = requests.post(api_url, headers=headers, json=payload)

    if response.status_code != 200:
        print(f"  ERROR: FLUX enhancement failed: {response.text}")
        return False

    result = response.json()

    # Get enhanced image URL
    images = result.get('images', [])
    if not images:
        print(f"  ERROR: No images in FLUX response: {result}")
        return False

    enhanced_image_url = images[0].get('url')
    print(f"  Downloading FLUX enhanced image from: {enhanced_image_url}")

    image_response = requests.get(enhanced_image_url)

    if image_response.status_code != 200:
        print(f"  ERROR: Failed to download FLUX enhanced image")
        return False

    # Save enhanced image
    with open(output_path, 'wb') as f:
        f.write(image_response.content)

    file_size = len(image_response.content) / 1024  # KB
    print(f"  ✓ Saved FLUX enhanced image: {output_path.name} ({file_size:.1f} KB)")
    return True


def process_founder(name: str, config: Dict) -> None:
    """Process all photos for a founder"""
    print(f"\n{'='*60}")
    print(f"Processing {name.upper()}")
    print(f"{'='*60}")

    for idx, source_photo in enumerate(config['source_photos'], 1):
        if not source_photo.exists():
            print(f"  WARNING: Source photo not found: {source_photo}")
            continue

        context = config['contexts'][idx - 1]
        print(f"\nPhoto {idx}/3: {source_photo.name} ({context})")

        try:
            # Upload source image
            image_url = upload_image_to_fal(source_photo)

            # Method 1: Portrait Enhance
            output_portrait = OUTPUT_DIR / f"{name}_enhanced_portrait_{idx:02d}.png"
            enhance_portrait(image_url, output_portrait)

            # Wait to avoid rate limiting
            time.sleep(2)

            # Method 2: FLUX Ultra with professional prompt
            professional_prompts = {
                "professional_headshot": "Professional corporate headshot, executive portrait, high-end business photography, studio lighting, confident expression, professional attire, sharp focus, professional color grading",
                "office_setting": "Professional office environment, modern workspace, executive at work, natural office lighting, business professional, confident and approachable, high-end corporate photography",
                "presentation": "Professional presenter, leadership presence, confident speaker, modern professional environment, executive presence, high-quality business photography",
                "business_casual": "Professional business casual portrait, modern professional, approachable leadership style, natural professional setting, high-quality corporate photography",
                "leadership": "Executive leadership portrait, confident professional presence, modern business environment, high-end professional photography, inspirational leader",
                "tech_leader": "Technology executive portrait, modern tech professional, innovative leader, contemporary professional environment, high-quality business photography",
                "executive": "Senior executive portrait, C-suite professional, commanding presence, premium corporate photography, sophisticated professional environment",
                "office_professional": "Professional office portrait, contemporary workspace, confident professional, modern business environment, high-quality corporate photography",
                "wellness_leader": "Professional wellness industry leader, approachable professional presence, modern professional environment, balanced leadership style, high-quality business photography"
            }

            prompt = professional_prompts.get(context, "Professional corporate portrait, high-end business photography, executive presence")
            output_flux = OUTPUT_DIR / f"{name}_enhanced_flux_{idx:02d}.png"
            enhance_with_flux_ultra(image_url, prompt, output_flux)

            # Wait between photos
            time.sleep(2)

        except Exception as e:
            print(f"  ERROR processing {source_photo.name}: {str(e)}")
            continue

    print(f"\n✓ Completed {name}")


def main():
    """Main processing function"""
    print("\n" + "="*60)
    print("HROC FOUNDER PHOTO ENHANCEMENT")
    print("Using fal.ai Portrait Enhance & FLUX 1.1 Pro Ultra")
    print("="*60)

    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"\nOutput directory: {OUTPUT_DIR}")

    # Process each founder
    total_images = 0
    for name, config in FOUNDERS.items():
        process_founder(name, config)
        total_images += len(config['source_photos']) * 2  # 2 versions per photo

    print("\n" + "="*60)
    print(f"✓ ENHANCEMENT COMPLETE!")
    print(f"Generated {total_images} enhanced professional photos")
    print(f"Output location: {OUTPUT_DIR}")
    print("="*60 + "\n")

    # List all generated files
    print("\nGenerated files:")
    for file in sorted(OUTPUT_DIR.glob("*.png")):
        size_kb = file.stat().st_size / 1024
        print(f"  - {file.name} ({size_kb:.1f} KB)")


if __name__ == "__main__":
    main()
