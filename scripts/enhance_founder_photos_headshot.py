#!/usr/bin/env python3
"""
Enhance HROC founder photos using fal.ai Headshot Generator
Specialized model for creating professional headshot photos
"""

import os
import sys
from pathlib import Path
import base64
import fal_client
import requests
import time

# Configure fal.ai API key
FAL_API_KEY = os.getenv("FAL_KEY")
if not FAL_API_KEY:
    print("ERROR: FAL_KEY environment variable not set!")
    print("Get the key from 1Password 'FAL API Key' and run:")
    print("export FAL_KEY='your-api-key-from-1password'")
    sys.exit(1)

# Source and destination paths
SOURCE_DIR = Path("/mnt/d/workspace/projects/HROC_Files/HROC_Website_New/images/founders")
OUTPUT_DIR = Path("/mnt/d/workspace/ISNBIZ_Files/assets/team")

# Founder photo configurations with headshot-specific settings
FOUNDER_CONFIG = {
    "alicia": {
        "source_photo": SOURCE_DIR / "a/alicia_hero_real.webp",
        "backgrounds": [
            "modern office",
            "professional studio",
            "contemporary workspace"
        ]
    },
    "bri": {
        "source_photo": SOURCE_DIR / "b/bri_varied_01.webp",
        "backgrounds": [
            "modern office",
            "professional studio",
            "contemporary workspace"
        ]
    },
    "jonathan": {
        "source_photo": SOURCE_DIR / "j/jonathan_varied_02.webp",
        "backgrounds": [
            "modern office",
            "professional studio",
            "contemporary workspace"
        ]
    },
    "lilly": {
        "source_photo": SOURCE_DIR / "l/lilly_varied_01.webp",
        "backgrounds": [
            "modern office",
            "professional studio",
            "contemporary workspace"
        ]
    }
}


def image_to_data_uri(image_path):
    """Convert image file to base64 data URI"""
    with open(image_path, 'rb') as f:
        image_data = f.read()

    ext = image_path.suffix.lower()
    mime_types = {
        '.webp': 'image/webp',
        '.png': 'image/png',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
    }
    mime_type = mime_types.get(ext, 'image/webp')
    base64_data = base64.b64encode(image_data).decode('utf-8')
    data_uri = f"data:{mime_type};base64,{base64_data}"
    return data_uri


def enhance_photo_headshot_generator(image_path, background, output_path):
    """
    Use fal.ai Headshot Generator to create professional headshot

    Args:
        image_path: Path to source image
        background: Background style for the headshot
        output_path: Where to save enhanced image

    Returns:
        bool: Success status
    """
    print(f"\n{'='*70}")
    print(f"Enhancing: {image_path.name}")
    print(f"Background: {background}")
    print(f"Output: {output_path.name}")
    print(f"{'='*70}")

    try:
        # Convert image to base64 data URI
        print("Converting image to base64 data URI...")
        image_data_uri = image_to_data_uri(image_path)
        data_uri_size = len(image_data_uri) / (1024 * 1024)
        print(f"✓ Data URI created ({data_uri_size:.2f} MB)")

        # Call Headshot Generator API
        print("Generating professional headshot...")

        result = fal_client.subscribe(
            "fal-ai/image-apps-v2/headshot-photo",
            arguments={
                "image_url": image_data_uri,
                "background": background,
                "output_format": "png"
            },
            with_logs=False,
            on_queue_update=lambda update: print(f"  Status: {update.get('status', 'processing')}...")
        )

        # Extract result
        if result and 'images' in result and len(result['images']) > 0:
            enhanced_url = result['images'][0]['url']
            inference_time = result.get('timings', {}).get('inference', 0)

            print(f"✓ Generated in {inference_time:.2f}s")
            print(f"  URL: {enhanced_url}")

            # Download enhanced image
            print("Downloading enhanced image...")
            response = requests.get(enhanced_url)

            if response.status_code == 200:
                with open(output_path, 'wb') as f:
                    f.write(response.content)
                file_size = len(response.content) / (1024 * 1024)
                print(f"✓ Saved to: {output_path} ({file_size:.2f} MB)")
                return True
            else:
                print(f"✗ Download failed: HTTP {response.status_code}")
                return False
        else:
            print(f"✗ No image in result: {result}")
            return False

    except Exception as e:
        print(f"✗ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Main execution function"""
    print("\n" + "="*70)
    print("HROC FOUNDER PHOTO ENHANCEMENT")
    print("Using fal.ai Headshot Generator API")
    print("="*70)

    # Ensure output directory exists
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"\nOutput directory: {OUTPUT_DIR}")

    # Statistics tracking
    total_generated = 0
    total_failed = 0
    total_time = 0.0
    start_time_overall = time.time()

    # Process each founder
    for founder_key, config in FOUNDER_CONFIG.items():
        source_photo = config['source_photo']
        backgrounds = config['backgrounds']

        print(f"\n{'#'*70}")
        print(f"# FOUNDER: {founder_key.upper()}")
        print(f"# Source: {source_photo.name}")
        print(f"# Variants: {len(backgrounds)}")
        print(f"{'#'*70}")

        # Check if source photo exists
        if not source_photo.exists():
            print(f"✗ Source photo not found: {source_photo}")
            total_failed += len(backgrounds)
            continue

        source_size = source_photo.stat().st_size / (1024 * 1024)
        print(f"Source image size: {source_size:.2f} MB")

        # Generate each variant
        for idx, background in enumerate(backgrounds, 1):
            output_filename = f"{founder_key}_headshot_{idx:02d}.png"
            output_path = OUTPUT_DIR / output_filename

            print(f"\n--- Variant {idx}/{len(backgrounds)} ---")

            start_time = time.time()
            success = enhance_photo_headshot_generator(source_photo, background, output_path)
            elapsed = time.time() - start_time

            if success:
                total_generated += 1
                total_time += elapsed
                print(f"✓ Success! ({elapsed:.1f}s)")
            else:
                total_failed += 1
                print(f"✗ Failed ({elapsed:.1f}s)")

            # Rate limiting
            if idx < len(backgrounds) or founder_key != list(FOUNDER_CONFIG.keys())[-1]:
                print("  Pausing before next request...")
                time.sleep(3)

    # Final summary
    elapsed_overall = time.time() - start_time_overall

    print("\n" + "="*70)
    print("ENHANCEMENT SUMMARY")
    print("="*70)

    total_expected = sum(len(config['backgrounds']) for config in FOUNDER_CONFIG.values())

    print(f"\n✓ Successfully generated: {total_generated}/{total_expected}")
    print(f"✗ Failed: {total_failed}/{total_expected}")
    print(f"\nTotal processing time: {elapsed_overall:.1f}s")
    if total_generated > 0:
        print(f"Average per image: {total_time/total_generated:.1f}s")

    print(f"\nOutput directory: {OUTPUT_DIR}")
    print(f"\nGenerated files:")
    if total_generated > 0:
        for file in sorted(OUTPUT_DIR.glob("*_headshot_*.png")):
            file_size = file.stat().st_size / (1024 * 1024)
            print(f"  - {file.name} ({file_size:.2f} MB)")

    print("\n" + "="*70)
    print("DONE!")
    print("="*70)

    return total_failed == 0


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
