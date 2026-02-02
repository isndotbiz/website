#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate headshots for a single founder - for parallel execution
"""

import os
import sys
import fal_client
from pathlib import Path
import json
import requests
from datetime import datetime

# Fix Windows console encoding
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Configure fal.ai API
os.environ['FAL_KEY'] = '64b786c3-d6b1-4fbb-9d46-9211ceea552f:d472cdf8c68b4fe873557ca33bfb25eb'

def upload_image_to_fal(image_path):
    """Upload image to fal.ai and return URL"""
    print(f"  📤 Uploading {image_path}...")
    with open(image_path, 'rb') as f:
        image_data = f.read()
    url = fal_client.upload(image_data, "image/png")
    print(f"  ✅ Uploaded")
    return url

def generate_image(image_url, prompt, output_path):
    """Generate image using gpt-image-1.5/edit"""
    print(f"  🎨 Generating: {output_path.name}")

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
        img_url = result['images'][0]['url']
        response = requests.get(img_url)
        if response.status_code == 200:
            with open(output_path, 'wb') as f:
                f.write(response.content)
            print(f"  ✅ Saved: {output_path.name}")
            return True
    return False

def process_founder(founder_name, image_path):
    """Process all images for one founder"""
    print(f"\n{'='*60}")
    print(f"👤 {founder_name.upper()}")
    print(f"{'='*60}")

    # Create output directories
    output_dir = Path("assets/founders")
    headshots_bg_dir = output_dir / "headshots_with_bg"
    headshots_no_bg_dir = output_dir / "headshots_no_bg"
    corporate_dir = output_dir / "corporate_photos"

    for d in [headshots_bg_dir, headshots_no_bg_dir, corporate_dir]:
        d.mkdir(parents=True, exist_ok=True)

    # Upload original
    image_url = upload_image_to_fal(image_path)

    # 1. Headshot with background
    prompt = f"""Professional corporate headshot portrait. The person should have the EXACT SAME FACE as in the original image - preserve all facial features, skin tone, hair style, and facial structure perfectly. Clean professional studio background in soft neutral gray or blue tones. Professional business attire. Soft professional lighting. Corporate photography style. The face must look identical to the original photo - same person, same features, same appearance."""
    generate_image(image_url, prompt, headshots_bg_dir / f"{founder_name}_headshot.png")

    # 2. Headshot no background
    prompt = f"""Professional corporate headshot portrait with transparent background removed. The person should have the EXACT SAME FACE as in the original image - preserve all facial features, skin tone, hair style, and facial structure perfectly. Remove all background completely - pure transparent or white background. Professional business attire. The face must look identical to the original photo - same person, same features, same appearance. Clean cutout style."""
    generate_image(image_url, prompt, headshots_no_bg_dir / f"{founder_name}_headshot_no_bg.png")

    # 3. Corporate photos
    activities = {
        'presenting': 'presenting at a corporate meeting with presentation screen behind, looking at presentation, professional business setting',
        'working': 'working on laptop in modern office, focused on screen, professional workspace with technology',
        'collaborating': 'collaborating with team in modern conference room, looking at documents or screen, professional business environment',
        'analyzing': 'analyzing data or documents, looking down at papers or tablet, professional office setting'
    }

    for activity, desc in activities.items():
        prompt = f"""Professional corporate photo of person {desc}. The person should have the EXACT SAME FACE as in the original image - preserve all facial features, skin tone, hair style, and facial structure perfectly. NOT looking directly at camera - looking at work, screen, documents, or colleagues. Professional business attire. Natural corporate environment. Corporate photography style. The face must look identical to the original photo - same person, same features, same appearance."""
        generate_image(image_url, prompt, corporate_dir / f"{founder_name}_{activity}.png")

    print(f"✅ {founder_name.upper()} COMPLETE!")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python generate_founder_parallel.py <name> <image_path>")
        sys.exit(1)

    founder_name = sys.argv[1]
    image_path = sys.argv[2]

    if not os.path.exists(image_path):
        print(f"❌ Image not found: {image_path}")
        sys.exit(1)

    process_founder(founder_name, image_path)
