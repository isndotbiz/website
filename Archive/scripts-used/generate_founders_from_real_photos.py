#!/usr/bin/env python3
"""
Generate professional candid founder photos using REAL photos from 1/ folder
Uses fal.ai Edit API to transform real photos into professional candid scenarios
"""

import os
import sys
from pathlib import Path
import fal_client
import requests
import time
from PIL import Image
import io
import base64

# Configure fal.ai API key
FAL_API_KEY = os.getenv("FAL_KEY", "64b786c3-d6b1-4fbb-9d46-9211ceea552f:d472cdf8c68b4fe873557ca33bfb25eb")
os.environ['FAL_KEY'] = FAL_API_KEY

# Directories
INPUT_DIR = Path("/mnt/d/workspace/ISNBIZ_Files/1")
OUTPUT_DIR = Path("/mnt/d/workspace/ISNBIZ_Files/assets/founders")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Founder configurations with their real photos
FOUNDERS = {
    "bri": {
        "name": "Bri",
        "role": "Secretary/COO",
        "real_photo": INPUT_DIR / "b1.png",
        "scenarios": [
            {
                "situation": "office_work",
                "prompt": "Transform this person into a professional candid photo: working at desk reviewing documents, NOT looking at camera, focused on paperwork, modern office environment, natural lighting, authentic work moment, business casual attire"
            },
            {
                "situation": "presentation",
                "prompt": "Transform this person into a professional candid photo: giving presentation to team, NOT looking at camera, gesturing at content, engaged with presentation, modern conference room, natural lighting, professional attire"
            },
            {
                "situation": "team_meeting",
                "prompt": "Transform this person into a professional candid photo: in team meeting, NOT looking at camera, collaborating with colleagues, discussing strategy, modern office, natural window light, business casual attire"
            },
            {
                "situation": "strategic_planning",
                "prompt": "Transform this person into a professional candid photo: reviewing strategic plans, NOT looking at camera, analyzing data on laptop, thoughtful expression, contemporary workspace, soft natural lighting, professional style"
            }
        ]
    },
    "lilly": {
        "name": "Lilly",
        "role": "Treasurer/CFO",
        "real_photo": INPUT_DIR / "l1.png",
        "scenarios": [
            {
                "situation": "office_work",
                "prompt": "Transform this person into a professional candid photo: analyzing financial reports at desk, NOT looking at camera, focused on spreadsheets and documents, modern office, natural lighting, business attire"
            },
            {
                "situation": "presentation",
                "prompt": "Transform this person into a professional candid photo: presenting financial data to board, NOT looking at camera, pointing at charts on screen, confident presenter, modern boardroom, natural lighting, executive attire"
            },
            {
                "situation": "team_meeting",
                "prompt": "Transform this person into a professional candid photo: in financial planning meeting, NOT looking at camera, discussing budget with team, collaborative atmosphere, contemporary office, window light, business professional style"
            },
            {
                "situation": "strategic_planning",
                "prompt": "Transform this person into a professional candid photo: reviewing quarterly reports, NOT looking at camera, deep in analysis, laptop and documents, executive office, soft natural lighting, professional business attire"
            }
        ]
    },
    "jonathan": {
        "name": "Jonathan",
        "role": "Chairman/CEO",
        "real_photo": INPUT_DIR / "j1.png",
        "scenarios": [
            {
                "situation": "office_work",
                "prompt": "Transform this person into a professional candid photo: working at executive desk with monitors, NOT looking at camera, reviewing company data, modern CEO office, natural lighting, business professional attire"
            },
            {
                "situation": "presentation",
                "prompt": "Transform this person into a professional candid photo: presenting company vision to investors, NOT looking at camera, confident speaker gesturing, large presentation screen, modern conference venue, natural lighting, executive business suit"
            },
            {
                "situation": "team_meeting",
                "prompt": "Transform this person into a professional candid photo: leading executive team meeting, NOT looking at camera, engaged in strategic discussion, contemporary boardroom, natural window light, business professional attire"
            },
            {
                "situation": "strategic_planning",
                "prompt": "Transform this person into a professional candid photo: reviewing strategic roadmap, NOT looking at camera, thoughtful analysis, whiteboard with charts, executive workspace, soft natural lighting, business casual professional"
            }
        ]
    },
    "alicia": {
        "name": "Alicia",
        "role": "VP/CPO",
        "real_photo": INPUT_DIR / "a1.png",
        "scenarios": [
            {
                "situation": "office_work",
                "prompt": "Transform this person into a professional candid photo: reviewing product designs at desk, NOT looking at camera, focused on product mockups and screens, modern workspace, natural lighting, creative professional attire"
            },
            {
                "situation": "presentation",
                "prompt": "Transform this person into a professional candid photo: presenting product roadmap to team, NOT looking at camera, gesturing at product visuals, engaged presenter, modern meeting room, natural lighting, business professional attire"
            },
            {
                "situation": "team_meeting",
                "prompt": "Transform this person into a professional candid photo: in product strategy meeting, NOT looking at camera, collaborating on UX designs, creative team atmosphere, contemporary office, window light, creative professional style"
            },
            {
                "situation": "strategic_planning",
                "prompt": "Transform this person into a professional candid photo: analyzing user feedback and metrics, NOT looking at camera, thoughtful product analysis, laptop and design boards, modern office, soft natural lighting, professional business casual"
            }
        ]
    }
}

def image_to_data_url(image_path):
    """Convert image file to data URL for API"""
    with open(image_path, 'rb') as f:
        image_data = f.read()
        base64_encoded = base64.b64encode(image_data).decode('utf-8')
        # Detect mime type
        ext = Path(image_path).suffix.lower()
        mime_type = 'image/png' if ext == '.png' else 'image/jpeg'
        return f"data:{mime_type};base64,{base64_encoded}"

def generate_candid_photo(founder_key, scenario, real_photo_path):
    """Generate a candid photo using the real photo as base"""
    situation = scenario['situation']
    prompt = scenario['prompt']
    output_path = OUTPUT_DIR / f"{founder_key}_{situation}.webp"

    # Skip if already exists
    if output_path.exists():
        print(f"  [SKIP] {output_path.name} already exists")
        return output_path

    print(f"\n  Generating: {situation}")
    print(f"  Real photo: {real_photo_path.name}")
    print(f"  Prompt: {prompt[:100]}...")

    try:
        # Convert real photo to data URL
        image_url = image_to_data_url(real_photo_path)

        # Use fal.ai Edit API with LOW QUALITY for more realistic results
        print("  Calling FAL Edit API (low quality for realism)...")
        result = fal_client.subscribe(
            "fal-ai/flux-pro/v1.1/redux",
            arguments={
                "image_url": image_url,
                "prompt": prompt,
                "image_size": {
                    "width": 1024,
                    "height": 1536
                },
                "num_inference_steps": 4,  # Low quality - more realistic!
                "guidance_scale": 2.0,  # Lower guidance
                "num_images": 1,
                "enable_safety_checker": True,
                "output_format": "jpeg",
                "sync_mode": True
            },
            with_logs=False
        )

        # Download and convert to WebP
        if result and 'images' in result and len(result['images']) > 0:
            image_url = result['images'][0]['url']
            print(f"  Got image URL: {image_url[:80]}...")

            # Handle both data URLs and regular URLs
            if image_url.startswith('data:'):
                # Data URL - decode base64
                print("  Decoding base64 data URL...")
                header, encoded = image_url.split(',', 1)
                image_data = base64.b64decode(encoded)
                img = Image.open(io.BytesIO(image_data))
                img.save(output_path, 'WEBP', quality=90)
                file_size = output_path.stat().st_size / 1024
                print(f"  [SUCCESS] Saved: {output_path.name} ({file_size:.1f} KB)")
                return output_path
            else:
                # Regular URL - download
                print(f"  Downloading from URL...")
                response = requests.get(image_url)
                if response.status_code == 200:
                    # Open image and convert to WebP
                    img = Image.open(io.BytesIO(response.content))
                    img.save(output_path, 'WEBP', quality=90)
                    file_size = output_path.stat().st_size / 1024
                    print(f"  [SUCCESS] Saved: {output_path.name} ({file_size:.1f} KB)")
                    return output_path
                else:
                    print(f"  [ERROR] Failed to download image: HTTP {response.status_code}")
                    return None
        else:
            print(f"  [ERROR] No images in API response")
            return None

    except Exception as e:
        print(f"  [ERROR] {str(e)}")
        return None

def main():
    print("\n" + "="*70)
    print("ISN.BIZ FOUNDER PHOTO GENERATION - Using REAL Photos")
    print("Professional Candid Photos from Real Source Images")
    print("Using fal.ai Flux Pro v1.1 Redux (Edit API)")
    print("="*70 + "\n")

    print(f"Input directory: {INPUT_DIR}")
    print(f"Output directory: {OUTPUT_DIR}\n")

    total_photos = 0
    success_count = 0

    for founder_key, config in FOUNDERS.items():
        print("\n" + "#"*70)
        print(f"# FOUNDER: {config['name']} - {config['role']}")
        print(f"# Real Photo: {config['real_photo'].name}")
        print(f"# Scenarios: {len(config['scenarios'])}")
        print("#"*70)

        # Check if real photo exists
        if not config['real_photo'].exists():
            print(f"[ERROR] Real photo not found: {config['real_photo']}")
            continue

        for scenario in config['scenarios']:
            total_photos += 1
            result = generate_candid_photo(founder_key, scenario, config['real_photo'])
            if result:
                success_count += 1
            time.sleep(2)  # Brief pause between API calls

    print("\n" + "="*70)
    print("GENERATION COMPLETE")
    print("="*70)
    print(f"\nTotal photos generated: {success_count}/{total_photos}")
    print(f"Output directory: {OUTPUT_DIR}")
    print("\nNext steps:")
    print("1. Review generated photos in assets/founders/")
    print("2. Deploy to TrueNAS if satisfied")
    print("3. Update website if needed")

if __name__ == "__main__":
    main()
