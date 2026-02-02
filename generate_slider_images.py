#!/usr/bin/env python3
"""
Generate professional slider images for ISN.BIZ website using FAL API
Generates 8 high-quality tech-themed images at 1536x1024 resolution
"""

import os
import sys
import requests
import time
from pathlib import Path

# FAL API configuration
FAL_API_KEY = "64b786c3-d6b1-4fbb-9d46-9211ceea552f:d472cdf8c68b4fe873557ca33bfb25eb"
FAL_API_URL = "https://fal.run/fal-ai/flux/schnell"

# Image specifications
WIDTH = 1536
HEIGHT = 1024
OUTPUT_DIR = Path(__file__).parent / "slider_images"

# Professional prompts for tech company slider images
PROMPTS = [
    {
        "filename": "slider_1.webp",
        "prompt": "Professional software engineering workspace, modern clean office with multiple monitors displaying code and data visualizations, soft blue and cyan lighting, minimalist design, tech startup aesthetic, ultra high quality, photorealistic, 8k"
    },
    {
        "filename": "slider_2.webp",
        "prompt": "Abstract digital network visualization, glowing blue neural pathways, data flowing through interconnected nodes, AI and machine learning concept, dark background with cyan accents, futuristic technology, ultra detailed, 8k"
    },
    {
        "filename": "slider_3.webp",
        "prompt": "Modern data center server room, rows of sleek black servers with blue LED indicators, clean professional environment, high-tech infrastructure, soft lighting, depth of field, photorealistic, 8k quality"
    },
    {
        "filename": "slider_4.webp",
        "prompt": "Futuristic cloud computing visualization, abstract 3D geometric shapes representing data and connectivity, blue and cyan color scheme, floating in digital space, professional tech aesthetic, high detail, 8k"
    },
    {
        "filename": "slider_5.webp",
        "prompt": "Professional business dashboard on large monitor, data analytics charts and graphs, modern office setting, soft natural lighting, blue accent colors, clean minimal design, photorealistic, 8k quality"
    },
    {
        "filename": "slider_6.webp",
        "prompt": "Abstract AI and machine learning concept art, flowing particle streams forming neural network patterns, blue and cyan gradients, dark background, professional tech visualization, ultra detailed, 8k"
    },
    {
        "filename": "slider_7.webp",
        "prompt": "Modern software development team workspace, collaborative environment with glass walls, natural light, multiple screens showing code and design work, professional tech office, photorealistic, 8k quality"
    },
    {
        "filename": "slider_8.webp",
        "prompt": "Abstract blockchain and cybersecurity visualization, glowing hexagonal network structure, blue and cyan lighting, secure data flow concept, professional tech aesthetic, dark background, high detail, 8k"
    }
]


def generate_image(prompt_data):
    """Generate a single image using FAL API"""
    filename = prompt_data["filename"]
    prompt = prompt_data["prompt"]

    print(f"\n[*] Generating: {filename}")
    print(f"[>] Prompt: {prompt[:80]}...")

    # Prepare API request
    headers = {
        "Authorization": f"Key {FAL_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "prompt": prompt,
        "image_size": {
            "width": WIDTH,
            "height": HEIGHT
        },
        "num_inference_steps": 4,  # Schnell model uses 4 steps
        "num_images": 1,
        "enable_safety_checker": True,
        "output_format": "jpeg",
        "sync_mode": True
    }

    try:
        # Submit generation request
        print("[~] Submitting to FAL API...")
        response = requests.post(FAL_API_URL, json=payload, headers=headers)
        response.raise_for_status()

        result = response.json()

        # Get image URL from response
        if "images" in result and len(result["images"]) > 0:
            image_url = result["images"][0]["url"]
            print(f"[+] Generated! Processing image...")

            # Check if it's a data URL (base64 encoded)
            if image_url.startswith('data:'):
                import base64
                import re
                # Extract base64 data from data URL
                match = re.match(r'data:image/\w+;base64,(.+)', image_url)
                if match:
                    base64_data = match.group(1)
                    image_data = base64.b64decode(base64_data)
                    print(f"[+] Decoded base64 image")
                else:
                    print(f"[!] Error: Could not parse data URL")
                    return False
            else:
                # Regular URL - download it
                print(f"[+] Downloading from: {image_url[:60]}...")
                img_response = requests.get(image_url)
                img_response.raise_for_status()
                image_data = img_response.content

            # Save the image
            output_path = OUTPUT_DIR / filename
            with open(output_path, 'wb') as f:
                f.write(image_data)

            file_size = output_path.stat().st_size / 1024
            print(f"[S] Saved: {output_path} ({file_size:.1f} KB)")
            return True
        else:
            print(f"[!] Error: No images in response")
            print(f"Response: {result}")
            return False

    except requests.exceptions.RequestException as e:
        print(f"[!] API Error: {e}")
        if hasattr(e.response, 'text'):
            print(f"Response: {e.response.text}")
        return False
    except Exception as e:
        print(f"[!] Unexpected error: {e}")
        return False


def main():
    """Generate all slider images"""
    print("=" * 70)
    print("ISN.BIZ Slider Image Generator")
    print("=" * 70)
    print(f"Resolution: {WIDTH}x{HEIGHT}")
    print(f"Images to generate: {len(PROMPTS)}")
    print(f"Output directory: {OUTPUT_DIR}")

    # Create output directory
    OUTPUT_DIR.mkdir(exist_ok=True)
    print(f"\n[+] Output directory ready: {OUTPUT_DIR}")

    # Generate all images
    successful = 0
    failed = 0

    for i, prompt_data in enumerate(PROMPTS, 1):
        print(f"\n{'=' * 70}")
        print(f"Image {i}/{len(PROMPTS)}")
        print(f"{'=' * 70}")

        if generate_image(prompt_data):
            successful += 1
        else:
            failed += 1

        # Rate limiting: wait between requests
        if i < len(PROMPTS):
            print("\n[~] Waiting 2 seconds before next generation...")
            time.sleep(2)

    # Summary
    print("\n" + "=" * 70)
    print("GENERATION SUMMARY")
    print("=" * 70)
    print(f"[+] Successful: {successful}/{len(PROMPTS)}")
    print(f"[!] Failed: {failed}/{len(PROMPTS)}")
    print(f"[>] Output: {OUTPUT_DIR.absolute()}")

    if successful == len(PROMPTS):
        print("\n[SUCCESS] All images generated successfully!")
        print("\nNext steps:")
        print("1. Review images in slider_images/ directory")
        print("2. Run upload_slider_to_s3.py to upload to S3")
        print("3. Update slider-gallery.html with new S3 URLs")
    else:
        print("\n[WARNING] Some images failed to generate. Check errors above.")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
