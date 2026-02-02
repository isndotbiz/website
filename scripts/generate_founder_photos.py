#!/usr/bin/env python3
"""
Generate ISN.BIZ founder photos using fal.ai GPT-Image 1.5 Edit API
Creates 4 professional candid-style photos per founder:
- Office work
- Presentations
- Team meetings
- Strategic planning

All photos are NOT looking at camera (candid style)
"""

import os
import sys
from pathlib import Path
import fal_client
import requests
import time
from PIL import Image
import io

# Get FAL API key from environment
FAL_API_KEY = os.getenv("FAL_API_KEY")
if not FAL_API_KEY:
    print("ERROR: FAL_API_KEY not found in environment")
    print("Please set it in .env file or export it")
    sys.exit(1)

os.environ['FAL_KEY'] = FAL_API_KEY

# Paths
PROJECT_ROOT = Path(__file__).parent.parent
SOURCE_DIR = PROJECT_ROOT / "assets" / "premium" / "founders"
OUTPUT_DIR = PROJECT_ROOT / "assets" / "founders"

# Founder configurations - 4 candid scenarios each
FOUNDER_CONFIG = {
    "bri": {
        "title": "Secretary/COO",
        "source_photo": SOURCE_DIR / "founder_bri.webp",
        "scenarios": [
            {
                "name": "office_work",
                "prompt": "Professional woman working at standing desk in modern office, reviewing documents on computer screen, side profile view looking at screen not camera, natural office lighting, business casual attire, focused expression, contemporary workspace, candid professional photography"
            },
            {
                "name": "presentation",
                "prompt": "Professional woman giving presentation to small group, gesturing toward screen, three-quarter view looking at audience not camera, modern conference room, business attire, confident body language, professional setting, candid corporate photography"
            },
            {
                "name": "team_meeting",
                "prompt": "Professional woman in collaborative meeting, leaning forward engaged in discussion, looking at colleague not camera, modern meeting room with glass walls, business casual, natural interaction, candid team collaboration photo"
            },
            {
                "name": "strategic_planning",
                "prompt": "Professional woman reviewing strategy documents at desk, hand on chin in thoughtful pose, side view looking down at papers not camera, executive office setting, professional attire, natural window lighting, candid strategic thinking moment"
            }
        ]
    },
    "lilly": {
        "title": "Treasurer/CFO",
        "source_photo": SOURCE_DIR / "founder_lilly.webp",
        "scenarios": [
            {
                "name": "office_work",
                "prompt": "Professional woman analyzing financial data on dual monitors, side profile view looking at screens not camera, modern office workspace, business attire, focused analytical expression, natural office lighting, candid professional photography"
            },
            {
                "name": "presentation",
                "prompt": "Professional woman presenting financial charts to executive team, pointing at projection screen, three-quarter view looking at presentation not camera, boardroom setting, professional business attire, confident posture, candid corporate photography"
            },
            {
                "name": "team_meeting",
                "prompt": "Professional woman in budget review meeting, taking notes while listening to colleague, side view looking at notepad not camera, modern conference room, business professional attire, engaged expression, candid meeting moment"
            },
            {
                "name": "strategic_planning",
                "prompt": "Professional woman reviewing quarterly reports at executive desk, hand holding pen over documents, looking down at spreadsheets not camera, corner office with city view, professional attire, natural lighting, candid strategic analysis"
            }
        ]
    },
    "jonathan": {
        "title": "Chairman/CEO",
        "source_photo": SOURCE_DIR / "founder_jonathan.webp",
        "scenarios": [
            {
                "name": "office_work",
                "prompt": "Professional man working at executive desk with laptop, side profile view looking at screen not camera, modern corner office, business casual attire, focused expression, natural window lighting, candid professional photography"
            },
            {
                "name": "presentation",
                "prompt": "Professional man presenting company vision to board, gesturing while speaking, three-quarter view looking at audience not camera, executive boardroom, suit and tie, confident leadership presence, candid corporate photography"
            },
            {
                "name": "team_meeting",
                "prompt": "Professional man leading strategy meeting, leaning forward on conference table, looking at team members not camera, modern collaborative workspace, business attire, engaging body language, candid leadership moment"
            },
            {
                "name": "strategic_planning",
                "prompt": "Professional man reviewing business plans at desk, arms crossed in thoughtful pose, side view looking at documents not camera, executive office setting, professional business attire, natural office lighting, candid strategic thinking"
            }
        ]
    },
    "alicia": {
        "title": "VP/CPO",
        "source_photo": SOURCE_DIR / "founder_alicia.webp",
        "scenarios": [
            {
                "name": "office_work",
                "prompt": "Professional woman designing product roadmap on whiteboard, side view looking at board not camera, modern innovation lab, business casual attire, creative engaged expression, bright natural lighting, candid professional photography"
            },
            {
                "name": "presentation",
                "prompt": "Professional woman presenting product demo to stakeholders, gesturing toward prototype, three-quarter view looking at product not camera, modern presentation space, professional attire, enthusiastic body language, candid corporate photography"
            },
            {
                "name": "team_meeting",
                "prompt": "Professional woman in product review meeting, sketching ideas on tablet, looking at device not camera, collaborative workspace with natural light, business casual, focused creative expression, candid team collaboration"
            },
            {
                "name": "strategic_planning",
                "prompt": "Professional woman reviewing user feedback at desk, hand on chin analyzing data, side view looking at screen not camera, modern office workspace, professional attire, thoughtful expression, candid strategic product planning"
            }
        ]
    }
}


def enhance_photo_with_fal(image_path, prompt, output_path):
    """
    Use fal.ai GPT-Image 1.5 Edit API to create professional photo variant

    Args:
        image_path: Path to source image
        prompt: Scenario prompt for the edit
        output_path: Where to save result

    Returns:
        bool: Success status
    """
    print(f"\n{'='*80}")
    print(f"Generating: {output_path.stem}")
    print(f"Prompt: {prompt[:100]}...")
    print(f"{'='*80}")

    try:
        # Upload source image
        print("📤 Uploading source image to fal.ai...")
        image_url = fal_client.upload_file(str(image_path))
        print(f"✓ Uploaded successfully")

        # Generate edited image
        print("🎨 Generating professional photo with GPT-Image 1.5 Edit...")

        result = fal_client.subscribe(
            "fal-ai/gpt-image-1.5/edit",
            arguments={
                "image_url": image_url,
                "prompt": prompt,
                "image_size": "landscape_16_9",  # Professional photo dimensions
                "num_inference_steps": 50,
                "guidance_scale": 7.5,
                "num_images": 1,
                "enable_safety_checker": True,
                "output_format": "png"
            },
            with_logs=False,
            on_queue_update=lambda update: print(f"  ⏳ Status: {update.get('status', 'processing')}...")
        )

        # Extract and download result
        if result and 'images' in result and len(result['images']) > 0:
            generated_url = result['images'][0]['url']
            inference_time = result.get('timings', {}).get('inference', 0)

            print(f"✓ Generated in {inference_time:.2f}s")

            # Download PNG
            print("📥 Downloading generated image...")
            response = requests.get(generated_url)

            if response.status_code == 200:
                # Convert to WebP for smaller file size
                print("🔄 Converting to WebP format...")
                img = Image.open(io.BytesIO(response.content))
                img.save(output_path, 'WEBP', quality=85, method=6)

                file_size = output_path.stat().st_size / 1024  # KB
                print(f"✓ Saved to: {output_path.name} ({file_size:.1f} KB)")
                return True
            else:
                print(f"✗ Download failed: HTTP {response.status_code}")
                return False
        else:
            print(f"✗ No image in result")
            return False

    except Exception as e:
        print(f"✗ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Main execution function"""
    print("\n" + "="*80)
    print(" ISN.BIZ FOUNDER PHOTO GENERATION")
    print(" Using fal.ai GPT-Image 1.5 Edit API")
    print(" 4 professional candid scenarios per founder")
    print("="*80)

    # Ensure output directory exists
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"\nOutput directory: {OUTPUT_DIR}")

    # Statistics
    total_generated = 0
    total_failed = 0
    total_time = 0.0
    start_overall = time.time()

    # Process each founder
    for founder_key, config in FOUNDER_CONFIG.items():
        source_photo = config['source_photo']
        scenarios = config['scenarios']
        title = config['title']

        print(f"\n{'#'*80}")
        print(f"# FOUNDER: {founder_key.upper()} ({title})")
        print(f"# Source: {source_photo.name}")
        print(f"# Scenarios: {len(scenarios)}")
        print(f"{'#'*80}")

        # Check source photo exists
        if not source_photo.exists():
            print(f"✗ Source photo not found: {source_photo}")
            total_failed += len(scenarios)
            continue

        # Generate each scenario
        for idx, scenario in enumerate(scenarios, 1):
            scenario_name = scenario['name']
            prompt = scenario['prompt']

            output_filename = f"{founder_key}_{scenario_name}.webp"
            output_path = OUTPUT_DIR / output_filename

            print(f"\n--- Scenario {idx}/{len(scenarios)}: {scenario_name.replace('_', ' ').title()} ---")

            start_time = time.time()
            success = enhance_photo_with_fal(source_photo, prompt, output_path)
            elapsed = time.time() - start_time

            if success:
                total_generated += 1
                total_time += elapsed
                print(f"✅ Success! ({elapsed:.1f}s)")
            else:
                total_failed += 1
                print(f"❌ Failed ({elapsed:.1f}s)")

            # Rate limiting between requests
            if idx < len(scenarios):
                print("  ⏸️  Pausing 3s before next request...")
                time.sleep(3)

    # Final summary
    overall_time = time.time() - start_overall
    total_expected = sum(len(config['scenarios']) for config in FOUNDER_CONFIG.values())

    print("\n" + "="*80)
    print(" GENERATION SUMMARY")
    print("="*80)

    print(f"\n✅ Successfully generated: {total_generated}/{total_expected}")
    print(f"❌ Failed: {total_failed}/{total_expected}")
    print(f"\n⏱️  Total time: {overall_time:.1f}s")
    print(f"⏱️  Average per photo: {total_time/max(total_generated, 1):.1f}s")

    print(f"\n📁 Output directory: {OUTPUT_DIR}")

    if total_generated > 0:
        print(f"\n📸 Generated photos:")
        for founder_key in FOUNDER_CONFIG.keys():
            print(f"\n  {founder_key.upper()}:")
            for file in sorted(OUTPUT_DIR.glob(f"{founder_key}_*.webp")):
                file_size = file.stat().st_size / 1024  # KB
                print(f"    ✓ {file.name} ({file_size:.1f} KB)")

    print("\n" + "="*80)
    print(" DONE!")
    print("="*80)
    print("\nNext steps:")
    print("  1. Review photos in: D:\\workspace\\ISNBIZ_Files\\assets\\founders\\")
    print("  2. Update website HTML to use new photo paths")
    print("  3. Test responsive display on all devices")

    return total_failed == 0


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
