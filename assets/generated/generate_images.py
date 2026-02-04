#!/usr/bin/env python3
"""Generate project images using fal.ai gpt-image-1.5 API"""

import requests
import os
import time
from pathlib import Path

FAL_KEY = "64b786c3-d6b1-4fbb-9d46-9211ceea552f:d472cdf8c68b4fe873557ca33bfb25eb"
OUTPUT_DIR = Path(__file__).parent

# Image definitions
IMAGES = [
    {
        "filename": "truenas_infrastructure.webp",
        "prompt": "Professional enterprise server room visualization, blue #1E9FF2 accent lighting, rack-mounted servers with glowing indicators, modern data center aesthetic, clean tech photography style, 4K quality"
    },
    {
        "filename": "videogen_youtube.webp",
        "prompt": "AI video production interface, modern editing timeline, multiple video streams, blue #1E9FF2 UI elements, professional content creation dashboard, clean dark theme"
    },
    {
        "filename": "bin_intelligence.webp",
        "prompt": "Financial fraud detection dashboard, payment card analytics, real-time data visualization, blue #1E9FF2 and cyan #5FDFDF charts, enterprise security interface"
    },
    {
        "filename": "spiritatlas.webp",
        "prompt": "Elegant mobile app interface, spiritual wellness design, soft gradients, mindfulness UI, premium mobile mockup, peaceful aesthetic with blue accents"
    },
    {
        "filename": "comfyui_automation.webp",
        "prompt": "Node-based AI workflow interface, ComfyUI style node graph, image generation pipeline, dark theme with blue #1E9FF2 connection lines"
    },
    {
        "filename": "gedcom_processing.webp",
        "prompt": "Family tree visualization, genealogy network graph, professional data processing interface, blue connections on dark background"
    },
    {
        "filename": "llm_optimization.webp",
        "prompt": "AI model evaluation dashboard, benchmark metrics display, LLM performance graphs, enterprise AI governance interface, blue #1E9FF2 theme"
    },
    {
        "filename": "opportunity_bot.webp",
        "prompt": "Market intelligence dashboard, opportunity discovery interface, scoring metrics, automated research visualization, blue and cyan data charts"
    },
    {
        "filename": "cli_tools.webp",
        "prompt": "Modern terminal interface, command line productivity tools, syntax highlighted code, dark theme with blue #1E9FF2 accents"
    }
]

def generate_image(prompt, filename):
    """Generate a single image using fal.ai API"""
    print(f"\nGenerating: {filename}")
    print(f"Prompt: {prompt[:60]}...")

    try:
        response = requests.post(
            "https://fal.run/fal-ai/gpt-image-1.5",
            headers={
                "Authorization": f"Key {FAL_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "prompt": prompt,
                "image_size": "1536x1024",
                "quality": "low",  # ALWAYS LOW - it's inverted, this is best quality
                "num_images": 1
            },
            timeout=120
        )

        if response.status_code == 200:
            result = response.json()
            # Get the image URL from response
            if "images" in result and len(result["images"]) > 0:
                image_url = result["images"][0]["url"]
                print(f"Image URL: {image_url}")

                # Download the image
                img_response = requests.get(image_url, timeout=60)
                if img_response.status_code == 200:
                    output_path = OUTPUT_DIR / filename
                    with open(output_path, "wb") as f:
                        f.write(img_response.content)
                    print(f"Saved: {output_path}")
                    return str(output_path), image_url
                else:
                    print(f"Failed to download image: {img_response.status_code}")
            else:
                print(f"No images in response: {result}")
        else:
            print(f"API error {response.status_code}: {response.text}")

    except Exception as e:
        print(f"Error generating {filename}: {e}")

    return None, None

def main():
    print("=" * 60)
    print("FAL.AI Image Generation - ISN.BIZ Project Images")
    print("=" * 60)
    print(f"Output directory: {OUTPUT_DIR}")
    print(f"Total images to generate: {len(IMAGES)}")

    results = []

    for i, img in enumerate(IMAGES, 1):
        print(f"\n[{i}/{len(IMAGES)}] ", end="")
        path, url = generate_image(img["prompt"], img["filename"])
        results.append({
            "filename": img["filename"],
            "path": path,
            "url": url,
            "success": path is not None
        })

        # Brief pause between API calls
        if i < len(IMAGES):
            time.sleep(1)

    # Summary
    print("\n" + "=" * 60)
    print("GENERATION COMPLETE")
    print("=" * 60)

    successful = [r for r in results if r["success"]]
    failed = [r for r in results if not r["success"]]

    print(f"\nSuccessful: {len(successful)}/{len(IMAGES)}")

    if successful:
        print("\nGenerated images:")
        for r in successful:
            print(f"  - {r['path']}")

    if failed:
        print("\nFailed images:")
        for r in failed:
            print(f"  - {r['filename']}")

    return results

if __name__ == "__main__":
    main()
