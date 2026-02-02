#!/usr/bin/env python3
"""
Generate professional candid founder photos using FLUX Pro (text-to-image only)
Faster alternative - generates photos directly without edit API
"""

import os
import sys
from pathlib import Path
import fal_client
import requests
import time
from PIL import Image

# Configure fal.ai API key
FAL_API_KEY = os.getenv("FAL_KEY", "64b786c3-d6b1-4fbb-9d46-9211ceea552f:d472cdf8c68b4fe873557ca33bfb25eb")
os.environ['FAL_KEY'] = FAL_API_KEY

# Output directory
OUTPUT_DIR = Path("/home/jdmal/workspace/ISNBIZ_Files/assets/founders")

# Founder configurations with complete scenario prompts
FOUNDER_SCENARIOS = {
    "bri": [
        {
            "name": "bri_office_work",
            "prompt": "Professional candid photograph of brunette woman in mid-30s, business casual attire, working at modern office desk reviewing documents and laptop, NOT looking at camera, focused on work, natural window lighting, realistic corporate photography, contemporary workspace, authentic work moment, 4K quality"
        },
        {
            "name": "bri_presentation",
            "prompt": "Professional candid photograph of brunette woman in mid-30s, business professional attire, giving presentation to team in modern conference room, NOT looking at camera, gesturing at whiteboard with charts, engaged with content, natural lighting, realistic business photography, authentic moment, 4K quality"
        },
        {
            "name": "bri_team_meeting",
            "prompt": "Professional candid photograph of brunette woman in mid-30s, business casual attire, in collaborative team meeting, NOT looking at camera, discussing strategy with colleagues around table, modern office setting, natural window light, realistic corporate photography, authentic collaboration, 4K quality"
        },
        {
            "name": "bri_strategic_planning",
            "prompt": "Professional candid photograph of brunette woman in mid-30s, business professional attire, reviewing strategic plans and data on laptop, NOT looking at camera, thoughtful analytical expression, contemporary executive workspace, soft natural lighting, realistic corporate photography, authentic leadership moment, 4K quality"
        }
    ],
    "lilly": [
        {
            "name": "lilly_office_work",
            "prompt": "Professional candid photograph of blonde woman in early-40s, business professional attire, analyzing financial reports and spreadsheets at desk, NOT looking at camera, focused on documents and laptop, modern office environment, natural lighting, realistic corporate photography, authentic CFO work, 4K quality"
        },
        {
            "name": "lilly_presentation",
            "prompt": "Professional candid photograph of blonde woman in early-40s, executive business attire, presenting financial data and charts to board meeting, NOT looking at camera, pointing at projection screen, confident presenter, modern boardroom, natural lighting, realistic business photography, authentic executive moment, 4K quality"
        },
        {
            "name": "lilly_team_meeting",
            "prompt": "Professional candid photograph of blonde woman in early-40s, business professional attire, in financial planning meeting, NOT looking at camera, discussing budget and forecasts with team, collaborative atmosphere, contemporary office, window light, realistic corporate photography, authentic leadership, 4K quality"
        },
        {
            "name": "lilly_strategic_planning",
            "prompt": "Professional candid photograph of blonde woman in early-40s, business professional attire, reviewing quarterly financial reports, NOT looking at camera, deep in analysis with laptop and documents, executive office setting, soft natural lighting, realistic corporate photography, authentic CFO work, 4K quality"
        }
    ],
    "jonathan": [
        {
            "name": "jonathan_office_work",
            "prompt": "Professional candid photograph of man in mid-40s with short dark hair, business professional attire, working at executive desk with multiple monitors, NOT looking at camera, reviewing company data and analytics, modern CEO office, natural lighting, realistic corporate photography, authentic leadership work, 4K quality"
        },
        {
            "name": "jonathan_presentation",
            "prompt": "Professional candid photograph of man in mid-40s with short dark hair, executive business suit, presenting company vision to investors, NOT looking at camera, confident speaker gesturing, large presentation screen behind, modern conference venue, natural lighting, realistic CEO photography, authentic leadership moment, 4K quality"
        },
        {
            "name": "jonathan_team_meeting",
            "prompt": "Professional candid photograph of man in mid-40s with short dark hair, business professional attire, leading executive team meeting, NOT looking at camera, engaged in strategic discussion, contemporary boardroom with colleagues, natural window light, realistic corporate photography, authentic leadership, 4K quality"
        },
        {
            "name": "jonathan_strategic_planning",
            "prompt": "Professional candid photograph of man in mid-40s with short dark hair, business casual professional attire, reviewing strategic roadmap, NOT looking at camera, thoughtful analysis mode, whiteboard with business charts, executive workspace, soft natural lighting, realistic CEO photography, authentic planning moment, 4K quality"
        }
    ],
    "alicia": [
        {
            "name": "alicia_office_work",
            "prompt": "Professional candid photograph of woman in late-30s with dark hair, business casual attire, reviewing product designs and mockups at workstation, NOT looking at camera, focused on design screens, modern tech office environment, natural lighting, realistic corporate photography, authentic product work, 4K quality"
        },
        {
            "name": "alicia_presentation",
            "prompt": "Professional candid photograph of woman in late-30s with dark hair, business professional attire, presenting product roadmap and timeline to team, NOT looking at camera, pointing at product charts, engaged presenter, modern meeting space, natural lighting, realistic business photography, authentic CPO moment, 4K quality"
        },
        {
            "name": "alicia_team_meeting",
            "prompt": "Professional candid photograph of woman in late-30s with dark hair, business casual attire, in product planning meeting with developers and designers, NOT looking at camera, collaborating on product strategy, contemporary office, window light, realistic corporate photography, authentic product leadership, 4K quality"
        },
        {
            "name": "alicia_strategic_planning",
            "prompt": "Professional candid photograph of woman in late-30s with dark hair, business professional attire, analyzing user feedback and product metrics, NOT looking at camera, reviewing product analytics on laptop, modern workspace with notes, soft natural lighting, realistic VP photography, authentic strategy work, 4K quality"
        }
    ]
}


def convert_to_webp(png_path, quality=90):
    """Convert PNG to WebP and delete PNG"""
    webp_path = png_path.with_suffix('.webp')

    try:
        with Image.open(png_path) as img:
            if img.mode in ('RGBA', 'LA', 'P'):
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'P':
                    img = img.convert('RGBA')
                background.paste(img, mask=img.split()[-1] if img.mode in ('RGBA', 'LA') else None)
                img = background

            img.save(webp_path, 'WEBP', quality=quality, method=6)

        print(f"  [OK] Converted to WebP: {webp_path.name}")
        png_path.unlink()
        print(f"  [OK] Deleted PNG")

        return webp_path

    except Exception as e:
        print(f"  [X] WebP conversion failed: {e}")
        return png_path


def generate_photo(scenario_name, prompt):
    """Generate photo using FLUX Pro"""
    output_path = OUTPUT_DIR / f"{scenario_name}.png"

    # Skip if already exists as WebP
    webp_path = OUTPUT_DIR / f"{scenario_name}.webp"
    if webp_path.exists():
        print(f"[SKIP] {scenario_name} already exists")
        return True

    print(f"\n{'='*70}")
    print(f"Generating: {scenario_name}")
    print(f"Prompt: {prompt[:80]}...")
    print(f"{'='*70}")

    try:
        result = fal_client.subscribe(
            "fal-ai/flux-pro/v1.1",
            arguments={
                "prompt": prompt,
                "image_size": {
                    "width": 1024,
                    "height": 1536
                },
                "num_inference_steps": 50,
                "guidance_scale": 7.5,
                "num_images": 1,
                "enable_safety_checker": True,
                "output_format": "png"
            },
            with_logs=False,
            on_queue_update=lambda update: print(f"  Status: {getattr(update, 'status', 'processing')}...")
        )

        if result and 'images' in result and len(result['images']) > 0:
            image_url = result['images'][0]['url']
            inference_time = result.get('timings', {}).get('inference', 0)

            print(f"[OK] Generated in {inference_time:.2f}s")

            # Download
            response = requests.get(image_url)
            if response.status_code == 200:
                with open(output_path, 'wb') as f:
                    f.write(response.content)
                print(f"[OK] Saved: {output_path.name}")

                # Convert to WebP
                convert_to_webp(output_path)
                return True
            else:
                print(f"[X] Download failed: HTTP {response.status_code}")
                return False
        else:
            print(f"[X] No image in result")
            return False

    except Exception as e:
        print(f"[X] Error: {e}")
        return False


def main():
    """Main execution"""
    print("\n" + "="*70)
    print("ISN.BIZ FOUNDER PHOTOS - FLUX PRO TEXT-TO-IMAGE")
    print("Faster direct generation method")
    print("="*70)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    total_generated = 0
    total_skipped = 0
    total_failed = 0
    start_time = time.time()

    # Generate all photos
    for founder_key, scenarios in FOUNDER_SCENARIOS.items():
        print(f"\n{'#'*70}")
        print(f"# FOUNDER: {founder_key.upper()}")
        print(f"# Photos: {len(scenarios)}")
        print(f"{'#'*70}")

        for scenario in scenarios:
            if generate_photo(scenario['name'], scenario['prompt']):
                if (OUTPUT_DIR / f"{scenario['name']}.webp").exists():
                    total_skipped += 1 if scenario['name'] in str(list(OUTPUT_DIR.glob("*.webp"))) else 0
                    total_generated += 1
            else:
                total_failed += 1

            # Rate limiting
            time.sleep(2)

    total_time = time.time() - start_time

    # Summary
    print("\n" + "="*70)
    print("GENERATION SUMMARY")
    print("="*70)

    total_expected = sum(len(scenarios) for scenarios in FOUNDER_SCENARIOS.values())

    print(f"\n[OK] Successfully generated: {total_generated}/{total_expected}")
    print(f"[X] Failed: {total_failed}/{total_expected}")
    print(f"\nTotal time: {total_time:.1f}s")

    if total_generated > 0:
        print(f"Average per image: {total_time/total_generated:.1f}s")

    print(f"\nOutput directory: {OUTPUT_DIR}")
    print(f"\nAll files:")
    for file in sorted(OUTPUT_DIR.glob("*.webp")):
        file_size = file.stat().st_size / (1024)  # KB
        print(f"  - {file.name} ({file_size:.1f} KB)")

    print("\n" + "="*70)
    print("DONE!")
    print("="*70)

    return total_failed == 0


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
