#!/usr/bin/env python3
"""
Generate professional candid founder photos for ISN.BIZ using fal.ai GPT-Image 1.5 Edit API
Creates 4 different professional situations per founder - NOT looking at camera
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

# Founder configurations with roles and photo scenarios
FOUNDER_CONFIG = {
    "bri": {
        "name": "Bri",
        "role": "Secretary/COO",
        "age": "mid-30s",
        "appearance": "professional woman, brunette hair, confident executive presence",
        "scenarios": [
            {
                "situation": "office_work",
                "prompt": "Professional woman in mid-30s, brunette hair, working at desk reviewing documents, NOT looking at camera, focused on paperwork, modern office environment, natural lighting, candid professional photography, business casual attire, authentic work moment"
            },
            {
                "situation": "presentation",
                "prompt": "Professional woman in mid-30s, brunette hair, giving presentation to team, NOT looking at camera, gesturing at whiteboard, engaged with content, modern conference room, natural lighting, candid business photography, professional attire"
            },
            {
                "situation": "team_meeting",
                "prompt": "Professional woman in mid-30s, brunette hair, in team meeting, NOT looking at camera, collaborating with colleagues, discussing strategy, modern office setting, natural window light, authentic business moment, business casual"
            },
            {
                "situation": "strategic_planning",
                "prompt": "Professional woman in mid-30s, brunette hair, reviewing strategic plans, NOT looking at camera, analyzing data on laptop, thoughtful expression, contemporary workspace, soft natural lighting, candid executive photography, professional style"
            }
        ]
    },
    "lilly": {
        "name": "Lilly",
        "role": "Treasurer/CFO",
        "age": "early-40s",
        "appearance": "professional woman, blonde hair, financial executive demeanor",
        "scenarios": [
            {
                "situation": "office_work",
                "prompt": "Professional woman in early-40s, blonde hair, analyzing financial reports at desk, NOT looking at camera, focused on spreadsheets and documents, modern office, natural lighting, candid professional photography, business attire, authentic work environment"
            },
            {
                "situation": "presentation",
                "prompt": "Professional woman in early-40s, blonde hair, presenting financial data to board, NOT looking at camera, pointing at charts on screen, confident presenter, modern boardroom, natural lighting, candid business photography, executive attire"
            },
            {
                "situation": "team_meeting",
                "prompt": "Professional woman in early-40s, blonde hair, in financial planning meeting, NOT looking at camera, discussing budget with team, collaborative atmosphere, contemporary office, window light, authentic professional moment, business professional style"
            },
            {
                "situation": "strategic_planning",
                "prompt": "Professional woman in early-40s, blonde hair, reviewing quarterly reports, NOT looking at camera, deep in analysis, laptop and documents, executive office setting, soft natural lighting, candid CFO photography, professional business attire"
            }
        ]
    },
    "jonathan": {
        "name": "Jonathan",
        "role": "Chairman/CEO",
        "age": "mid-40s",
        "appearance": "professional man, short dark hair, executive leadership presence",
        "scenarios": [
            {
                "situation": "office_work",
                "prompt": "Professional man in mid-40s, short dark hair, working at executive desk with multiple monitors, NOT looking at camera, reviewing company data, modern CEO office, natural lighting, candid leadership photography, business professional attire, authentic work moment"
            },
            {
                "situation": "presentation",
                "prompt": "Professional man in mid-40s, short dark hair, presenting company vision to investors, NOT looking at camera, confident speaker gesturing, large presentation screen, modern conference venue, natural lighting, candid CEO photography, executive business suit"
            },
            {
                "situation": "team_meeting",
                "prompt": "Professional man in mid-40s, short dark hair, leading executive team meeting, NOT looking at camera, engaged in strategic discussion, contemporary boardroom, natural window light, authentic leadership moment, business professional attire"
            },
            {
                "situation": "strategic_planning",
                "prompt": "Professional man in mid-40s, short dark hair, reviewing strategic roadmap, NOT looking at camera, thoughtful analysis, whiteboard with charts, executive workspace, soft natural lighting, candid CEO photography, business casual professional"
            }
        ]
    },
    "alicia": {
        "name": "Alicia",
        "role": "VP/CPO",
        "age": "late-30s",
        "appearance": "professional woman, dark hair, product leadership presence",
        "scenarios": [
            {
                "situation": "office_work",
                "prompt": "Professional woman in late-30s, dark hair, reviewing product designs at workstation, NOT looking at camera, focused on design mockups, modern tech office, natural lighting, candid product photography, business casual attire, authentic creative work"
            },
            {
                "situation": "presentation",
                "prompt": "Professional woman in late-30s, dark hair, presenting product roadmap to team, NOT looking at camera, pointing at product timeline, engaged presenter, modern meeting space, natural lighting, candid CPO photography, professional business attire"
            },
            {
                "situation": "team_meeting",
                "prompt": "Professional woman in late-30s, dark hair, in product planning meeting, NOT looking at camera, collaborating with developers and designers, contemporary office, window light, authentic product leadership moment, business casual professional"
            },
            {
                "situation": "strategic_planning",
                "prompt": "Professional woman in late-30s, dark hair, analyzing user feedback and metrics, NOT looking at camera, reviewing product analytics, laptop and notes, modern workspace, soft natural lighting, candid VP photography, professional style"
            }
        ]
    }
}


def convert_to_webp(png_path, quality=90):
    """
    Convert PNG to WebP format

    Args:
        png_path: Path to PNG file
        quality: WebP quality (1-100)

    Returns:
        Path to WebP file
    """
    webp_path = png_path.with_suffix('.webp')

    try:
        with Image.open(png_path) as img:
            # Convert RGBA to RGB if necessary
            if img.mode in ('RGBA', 'LA', 'P'):
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'P':
                    img = img.convert('RGBA')
                background.paste(img, mask=img.split()[-1] if img.mode in ('RGBA', 'LA') else None)
                img = background

            img.save(webp_path, 'WEBP', quality=quality, method=6)

        print(f"  [OK] Converted to WebP: {webp_path.name}")

        # Delete original PNG
        png_path.unlink()
        print(f"  [OK] Deleted PNG: {png_path.name}")

        return webp_path

    except Exception as e:
        print(f"  [X] WebP conversion failed: {e}")
        return png_path


def generate_base_photo(founder_key, config):
    """
    Generate base founder photo using text-to-image

    Args:
        founder_key: Founder identifier
        config: Founder configuration

    Returns:
        Path to generated image or None
    """
    print(f"\n{'='*70}")
    print(f"Generating base photo for {config['name']} ({config['role']})")
    print(f"{'='*70}")

    # Create a professional base photo prompt
    base_prompt = f"Professional business portrait photograph of {config['appearance']}, {config['age']}, looking slightly to the side NOT at camera, neutral professional expression, modern office background with soft focus, natural window lighting, high-quality corporate photography, business professional attire, realistic photograph, 4K quality"

    output_path = OUTPUT_DIR / f"{founder_key}_base.png"

    try:
        print(f"Prompt: {base_prompt}")
        print("Generating base image...")

        result = fal_client.subscribe(
            "fal-ai/flux-pro/v1.1",
            arguments={
                "prompt": base_prompt,
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
            print(f"  URL: {image_url}")

            # Download image
            response = requests.get(image_url)
            if response.status_code == 200:
                with open(output_path, 'wb') as f:
                    f.write(response.content)
                print(f"[OK] Saved: {output_path}")
                return output_path
            else:
                print(f"[X] Download failed: HTTP {response.status_code}")
                return None
        else:
            print(f"[X] No image in result")
            return None

    except Exception as e:
        print(f"[X] Error: {e}")
        import traceback
        traceback.print_exc()
        return None


def generate_scenario_photo(base_image_path, founder_key, scenario, scenario_idx):
    """
    Generate scenario-specific photo using edit API

    Args:
        base_image_path: Path to base image
        founder_key: Founder identifier
        scenario: Scenario configuration
        scenario_idx: Scenario index (1-4)

    Returns:
        bool: Success status
    """
    situation = scenario['situation']
    prompt = scenario['prompt']

    output_filename = f"{founder_key}_{situation}.png"
    output_path = OUTPUT_DIR / output_filename

    print(f"\n{'='*70}")
    print(f"Scenario {scenario_idx}/4: {situation}")
    print(f"Prompt: {prompt[:80]}...")
    print(f"Output: {output_filename}")
    print(f"{'='*70}")

    try:
        # Upload base image
        print("Uploading base image...")
        image_url = fal_client.upload_file(str(base_image_path))
        print(f"[OK] Uploaded: {image_url}")

        # Generate scenario photo using edit API
        print("Generating scenario photo with GPT-Image 1.5...")

        result = fal_client.subscribe(
            "fal-ai/gpt-image-1.5/edit",
            arguments={
                "image_urls": [image_url],
                "prompt": prompt,
                "image_size": "1024x1536",  # Portrait format
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
            scenario_url = result['images'][0]['url']
            inference_time = result.get('timings', {}).get('inference', 0)

            print(f"[OK] Generated in {inference_time:.2f}s")
            print(f"  URL: {scenario_url}")

            # Download image
            response = requests.get(scenario_url)
            if response.status_code == 200:
                with open(output_path, 'wb') as f:
                    f.write(response.content)
                print(f"[OK] Saved: {output_path}")

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
        import traceback
        traceback.print_exc()
        return False


def main():
    """Main execution"""
    print("\n" + "="*70)
    print("ISN.BIZ FOUNDER PHOTO GENERATION")
    print("Professional Candid Photos - NOT Looking at Camera")
    print("Using fal.ai GPT-Image 1.5 Edit API")
    print("="*70)

    # Ensure output directory exists
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"\nOutput directory: {OUTPUT_DIR}")

    # Statistics
    total_generated = 0
    total_failed = 0
    total_time = 0.0

    # Process each founder
    for founder_key, config in FOUNDER_CONFIG.items():
        print(f"\n{'#'*70}")
        print(f"# FOUNDER: {config['name']} - {config['role']}")
        print(f"# Scenarios: {len(config['scenarios'])}")
        print(f"{'#'*70}")

        # Step 1: Generate or use existing base photo
        base_webp_path = OUTPUT_DIR / f"{founder_key}_base.webp"
        base_png_path = OUTPUT_DIR / f"{founder_key}_base.png"

        if base_webp_path.exists():
            print(f"[OK] Using existing base photo: {base_webp_path.name}")
            base_image_path = base_webp_path
        elif base_png_path.exists():
            print(f"[OK] Using existing base photo: {base_png_path.name}")
            base_image_path = base_png_path
        else:
            start_time = time.time()
            base_image_path = generate_base_photo(founder_key, config)
            base_elapsed = time.time() - start_time

            if not base_image_path:
                print(f"[X] Failed to generate base photo for {config['name']}")
                total_failed += len(config['scenarios'])
                continue

            print(f"[OK] Base photo ready ({base_elapsed:.1f}s)")

            # Convert base photo to WebP
            base_image_path = convert_to_webp(base_image_path)

        # Pause before scenarios
        print("\nPausing before scenario generation...")
        time.sleep(3)

        # Step 2: Generate scenario photos
        for idx, scenario in enumerate(config['scenarios'], 1):
            start_time = time.time()
            success = generate_scenario_photo(base_image_path, founder_key, scenario, idx)
            elapsed = time.time() - start_time

            if success:
                total_generated += 1
                total_time += elapsed
                print(f"[OK] Success! ({elapsed:.1f}s)")
            else:
                total_failed += 1
                print(f"[X] Failed ({elapsed:.1f}s)")

            # Rate limiting
            if idx < len(config['scenarios']):
                print("  Pausing before next scenario...")
                time.sleep(3)

    # Final summary
    print("\n" + "="*70)
    print("GENERATION SUMMARY")
    print("="*70)

    total_expected = sum(len(config['scenarios']) for config in FOUNDER_CONFIG.values())

    print(f"\n[OK] Successfully generated: {total_generated}/{total_expected}")
    print(f"[X] Failed: {total_failed}/{total_expected}")
    print(f"\nTotal processing time: {total_time:.1f}s")

    if total_generated > 0:
        print(f"Average per image: {total_time/total_generated:.1f}s")

        print(f"\nOutput directory: {OUTPUT_DIR}")
        print(f"\nGenerated files:")
        for file in sorted(OUTPUT_DIR.glob("*.webp")):
            file_size = file.stat().st_size / (1024 * 1024)  # MB
            print(f"  - {file.name} ({file_size:.2f} MB)")

    print("\n" + "="*70)
    print("DONE!")
    print("="*70)

    return total_failed == 0


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
