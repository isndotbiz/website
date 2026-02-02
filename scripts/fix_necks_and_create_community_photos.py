#!/usr/bin/env python3
"""
Fix founder neck proportions and create community outreach photos using fal.ai
Uses gpt-image-1.5/edit for precision editing
"""

import os
import sys
import time
import base64
from pathlib import Path

try:
    import fal_client as fal
    import requests
except ImportError:
    print("ERROR: Required packages not installed.")
    print("\nInstall them with:")
    print("  source venv_fal/bin/activate")
    print("  pip install fal-client requests")
    sys.exit(1)

# Check API key
FAL_API_KEY = os.environ.get("FAL_KEY")
if not FAL_API_KEY:
    print("="*80)
    print("ERROR: FAL_KEY environment variable not set!")
    print("="*80)
    print("\nTo get your actual API key:")
    print("  eval $(op signin)")
    print("  export FAL_KEY=$(op read 'op://Research/FAL API Key/credential')")
    print("\nThen run this script again.")
    print("="*80)
    sys.exit(1)

# Directories
BASE_DIR = Path("/mnt/d/workspace/ISNBIZ_Files")
FOUNDERS_DIR = BASE_DIR / "assets/founders"
HEADSHOTS_DIR = FOUNDERS_DIR / "headshots_no_bg"
FIXED_DIR = FOUNDERS_DIR / "fixed_necks"
COMMUNITY_DIR = FOUNDERS_DIR / "community"

# Create output directories
FIXED_DIR.mkdir(parents=True, exist_ok=True)
COMMUNITY_DIR.mkdir(parents=True, exist_ok=True)

def encode_image_to_base64(image_path):
    """Encode image to base64 for fal.ai"""
    with open(image_path, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')

def download_image(url, output_path):
    """Download image from URL"""
    response = requests.get(url)
    if response.status_code == 200:
        with open(output_path, 'wb') as f:
            f.write(response.content)
        return True
    return False

def fix_neck(founder_name, input_image_path):
    """
    Fix neck proportions using gpt-image-1.5/edit
    Makes neck slightly shorter while keeping face EXACTLY the same
    """
    print(f"\n{'='*80}")
    print(f"TASK 1: Fixing {founder_name}'s neck proportions")
    print(f"{'='*80}")
    print(f"Input: {input_image_path}")

    # Read and encode image
    image_base64 = encode_image_to_base64(input_image_path)

    # Use gpt-image-1.5/edit for precision editing
    prompt = f"""Subtle neck adjustment: Make the neck slightly shorter (reduce by ~15%) while keeping the face,
hair, expression, and all other features EXACTLY identical. The neck should appear more proportionate to the head.
Professional corporate headshot. Photorealistic. Keep the same lighting, background, and all facial features
unchanged. Only adjust the neck length."""

    print(f"Prompt: {prompt[:100]}...")
    print("Submitting to fal.ai gpt-image-1.5/edit...")

    try:
        handler = fal.submit(
            "fal-ai/gpt-image-1.5/edit",
            arguments={
                "image_url": f"data:image/png;base64,{image_base64}",
                "prompt": prompt,
                "num_images": 1,
                "output_format": "png",
                "guidance_scale": 7.5,  # Lower guidance for subtlety
                "num_inference_steps": 50
            }
        )

        print("Waiting for result...")
        result = handler.get()

        if "images" in result and len(result["images"]) > 0:
            image_url = result["images"][0]["url"]
            output_file = FIXED_DIR / f"{founder_name}_headshot_fixed.png"

            print(f"Success! Downloading to: {output_file}")
            if download_image(image_url, output_file):
                print(f"✓ Saved: {output_file}")
                return output_file
            else:
                print(f"✗ Failed to download image")
                return None
        else:
            print(f"✗ Unexpected response format")
            return None

    except Exception as e:
        print(f"✗ Error: {str(e)}")
        return None

def create_community_photo(scenario_num, scenario_desc, all_founders=True, founders_included=None):
    """
    Create community outreach photos with founders

    Args:
        scenario_num: Scenario number (1-8)
        scenario_desc: Description of the scenario
        all_founders: If True, include all 4 founders
        founders_included: List of specific founders if not all
    """
    print(f"\n{'='*80}")
    print(f"TASK 2: Creating Community Photo #{scenario_num}")
    print(f"{'='*80}")
    print(f"Scenario: {scenario_desc}")

    # Build detailed prompt
    if all_founders:
        people_desc = """Four diverse tech founders:
- Jonathan (40s, professional man with beard and business attire)
- Alicia (30s, professional woman with dark straight hair)
- Bri (30s, professional woman with dark wavy hair)
- Lilly (30s, professional woman with brown wavy hair)"""
    else:
        people_desc = f"Tech founders: {', '.join(founders_included or [])}"

    prompt = f"""{scenario_desc}. {people_desc}.
Professional photography, bright natural lighting, warm and inviting atmosphere,
genuine smiles and engagement, diverse community members visible,
photorealistic, high quality, community center or school environment,
documentary style photography, Canon EOS R5 camera quality."""

    print(f"Prompt: {prompt[:150]}...")
    print("Submitting to fal.ai gpt-image-1.5...")

    try:
        handler = fal.submit(
            "fal-ai/gpt-image-1.5",
            arguments={
                "prompt": prompt,
                "num_images": 1,
                "aspect_ratio": "16:9",
                "output_format": "png",
                "guidance_scale": 7.5,
                "num_inference_steps": 50,
                "enable_safety_checker": False
            }
        )

        print("Waiting for result...")
        result = handler.get()

        if "images" in result and len(result["images"]) > 0:
            image_url = result["images"][0]["url"]
            scenario_slug = scenario_desc.lower().replace(" ", "_")[:30]
            output_file = COMMUNITY_DIR / f"community_{scenario_num:02d}_{scenario_slug}.png"

            print(f"Success! Downloading to: {output_file}")
            if download_image(image_url, output_file):
                print(f"✓ Saved: {output_file}")
                return output_file
            else:
                print(f"✗ Failed to download image")
                return None
        else:
            print(f"✗ Unexpected response format")
            return None

    except Exception as e:
        print(f"✗ Error: {str(e)}")
        return None

def main():
    print("="*80)
    print("FAL.AI FOUNDER PHOTO ENHANCEMENT")
    print("="*80)
    print(f"API Key: {FAL_API_KEY[:20]}... ({len(FAL_API_KEY)} chars)")
    print(f"Base Directory: {BASE_DIR}")
    print(f"Headshots: {HEADSHOTS_DIR}")
    print(f"Output - Fixed: {FIXED_DIR}")
    print(f"Output - Community: {COMMUNITY_DIR}")

    # TASK 1: Fix necks for Lilly and Bri
    print("\n" + "="*80)
    print("STARTING TASK 1: FIX NECK PROPORTIONS")
    print("="*80)

    neck_fixes = []

    # Fix Lilly's neck
    lilly_headshot = HEADSHOTS_DIR / "lilly_headshot_no_bg.png"
    if lilly_headshot.exists():
        result = fix_neck("lilly", lilly_headshot)
        if result:
            neck_fixes.append(("Lilly", result))
        time.sleep(2)  # Rate limiting
    else:
        print(f"✗ Lilly's headshot not found: {lilly_headshot}")

    # Fix Bri's neck
    bri_headshot = HEADSHOTS_DIR / "bri_headshot_no_bg.png"
    if bri_headshot.exists():
        result = fix_neck("bri", bri_headshot)
        if result:
            neck_fixes.append(("Bri", result))
        time.sleep(2)  # Rate limiting
    else:
        print(f"✗ Bri's headshot not found: {bri_headshot}")

    # Summary for Task 1
    print("\n" + "="*80)
    print("TASK 1 COMPLETE: NECK FIXES")
    print("="*80)
    for name, path in neck_fixes:
        print(f"✓ {name}: {path}")

    # TASK 2: Create community outreach photos
    print("\n" + "="*80)
    print("STARTING TASK 2: COMMUNITY OUTREACH PHOTOS")
    print("="*80)

    scenarios = [
        "Tech founders volunteering at busy community center, helping diverse people with computers",
        "Four tech professionals teaching coding workshop to enthusiastic diverse students in classroom",
        "Technology founders speaking at community tech event, engaging with diverse audience",
        "Professional mentors guiding young diverse students with laptops in modern learning space",
        "Tech team participating in community cleanup day, wearing casual volunteer shirts",
        "Founders volunteering at food bank, organizing donations and helping community members",
        "Technology professionals leading STEM outreach at elementary school, excited children learning",
        "Charity tech event with founders demonstrating technology to diverse community members"
    ]

    community_photos = []
    for i, scenario in enumerate(scenarios, 1):
        result = create_community_photo(i, scenario)
        if result:
            community_photos.append((i, scenario, result))
        time.sleep(2)  # Rate limiting

        if i == 4:  # Pause halfway
            print("\n--- Pausing for 5 seconds (halfway through) ---\n")
            time.sleep(5)

    # Final summary
    print("\n" + "="*80)
    print("ALL TASKS COMPLETE!")
    print("="*80)

    print(f"\nTask 1: Fixed {len(neck_fixes)} neck proportions")
    for name, path in neck_fixes:
        print(f"  ✓ {name}: {path.name}")

    print(f"\nTask 2: Created {len(community_photos)} community photos")
    for num, scenario, path in community_photos:
        print(f"  ✓ Photo {num}: {path.name}")

    print(f"\nAll files saved to:")
    print(f"  Fixed necks: {FIXED_DIR}")
    print(f"  Community photos: {COMMUNITY_DIR}")
    print("="*80)

    return 0

if __name__ == "__main__":
    sys.exit(main())
