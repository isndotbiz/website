#!/usr/bin/env python3
"""
Generate missing portfolio images for ISN.BIZ website
Uses fal.ai GPT-IMAGE-1.5 model
"""

import requests
import json
import time
import os
from pathlib import Path

# Configuration
FAL_API_KEY = "64b786c3-d6b1-4fbb-9d46-9211ceea552f:d472cdf8c68b4fe873557ca33bfb25eb"
MODEL_URL = "https://queue.fal.run/fal-ai/gpt-image-1.5"
OUTPUT_DIR = Path("D:/workspace/ISNBIZ_Files/assets/premium_v3/portfolio")

# Ensure output directory exists
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Image prompts based on project documentation
PROMPTS = {
    "cli_template": {
        "prompt": """Background/scene: Dark charcoal tech environment (#0D1117) with subtle depth and soft volumetric light.
Subject: Modern CLI terminal interface with holographic command scaffolding floating above it - TypeScript code snippets, directory tree structures, and test coverage indicators displayed as translucent 3D elements.
Details: Glowing blue/cyan accents (#1E9FF2, #5FDFDF) highlight npm commands, testing frameworks, and build pipeline nodes. Abstract geometric shapes represent standardized CLI structure and modular architecture. Professional enterprise developer tool aesthetic with clean lines and minimal clutter.
Constraints: No readable text, no logos, no watermark. Dark #0D1117 background that blends with website.
Intended use: Portfolio project mockup (16:9) for CLI template framework.""",
        "filename": "cli_template.webp"
    },

    "comfyui_wan": {
        "prompt": """Background/scene: Dark enterprise dashboard environment (#0D1117) with soft ambient lighting.
Subject: Holographic workflow visualization showing ComfyUI node graph with interconnected processing blocks - image generation pipeline with floating GPU status indicators, model loading sequences, and batch processing queues displayed as abstract glowing UI elements.
Details: Blue/cyan accents (#1E9FF2, #5FDFDF) illuminate workflow nodes, Flux model connections, and LoRA management panels. Abstract generative art thumbnails float in translucent cards. Clean enterprise automation aesthetic with flowing data streams.
Constraints: No readable text, no logos, no watermark. Dark #0D1117 background.
Intended use: Portfolio project mockup (16:9) for ComfyUI automation system.""",
        "filename": "comfyui_wan.webp"
    },

    "gedcom_processing": {
        "prompt": """Background/scene: Professional data processing environment with dark charcoal backdrop (#0D1117).
Subject: Holographic family tree network visualization with nodes and relationship connections - abstract genealogical graph with data validation indicators, integrity check badges, and processing pipeline status displayed as floating translucent panels.
Details: Blue/cyan accents (#1E9FF2, #5FDFDF) highlight cleaned data nodes, deduplication processes, and audit trail elements. Abstract GEDCOM record cards with before/after comparison states. Clean, precise data engineering aesthetic with relationship-preserving algorithms visualized as glowing pathways.
Constraints: No readable text, no logos, no watermark. Dark #0D1117 background.
Intended use: Portfolio project mockup (16:9) for GEDCOM processing system.""",
        "filename": "gedcom_processing.webp"
    }
}


def generate_image(prompt: str, filename: str) -> dict:
    """Generate a single image using fal.ai API"""

    headers = {
        "Authorization": f"Key {FAL_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "prompt": prompt,
        "image_size": {
            "width": 1600,
            "height": 900
        },
        "num_images": 1,
        "quality": "low",  # Cost control
        "output_format": "webp"
    }

    print(f"\n{'='*80}")
    print(f"Generating: {filename}")
    print(f"{'='*80}")
    print(f"Prompt: {prompt[:150]}...")

    # Submit request
    response = requests.post(MODEL_URL, headers=headers, json=payload)

    if response.status_code != 200:
        print(f"ERROR: HTTP {response.status_code}")
        print(f"Response: {response.text}")
        return None

    result = response.json()
    request_id = result.get("request_id")

    print(f"Request ID: {request_id}")
    print("Waiting for generation...")

    # Poll for completion
    status_url = f"{MODEL_URL}/requests/{request_id}"
    max_attempts = 60
    attempt = 0

    while attempt < max_attempts:
        time.sleep(2)
        attempt += 1

        status_response = requests.get(status_url, headers=headers)
        status_data = status_response.json()

        status = status_data.get("status")
        print(f"  [{attempt}/{max_attempts}] Status: {status}")

        if status == "COMPLETED":
            image_url = status_data.get("output", {}).get("images", [{}])[0].get("url")
            if image_url:
                print(f"SUCCESS: {image_url}")
                return {
                    "filename": filename,
                    "url": image_url,
                    "prompt": prompt
                }
            else:
                print("ERROR: No image URL in response")
                return None

        elif status in ["FAILED", "CANCELLED"]:
            print(f"ERROR: Generation {status}")
            print(f"Details: {status_data}")
            return None

    print("ERROR: Timeout waiting for generation")
    return None


def download_image(url: str, filepath: Path) -> bool:
    """Download image from URL to local file"""
    print(f"Downloading to: {filepath}")

    response = requests.get(url)
    if response.status_code == 200:
        filepath.write_bytes(response.content)
        size_kb = len(response.content) / 1024
        print(f"Downloaded: {size_kb:.1f} KB")
        return True
    else:
        print(f"ERROR: Download failed with HTTP {response.status_code}")
        return False


def create_responsive_variants(base_image: Path):
    """Create responsive variants using simple resize (placeholder for future optimization)"""
    # For now, just note that responsive variants should be created
    # In production, you'd use PIL/Pillow to create _desktop, _tablet, _mobile variants
    print(f"NOTE: Create responsive variants for {base_image.name} using image optimization tools")
    # Example sizes:
    # _desktop: 1600x900
    # _tablet: 1024x576
    # _mobile: 800x450


def main():
    """Generate all missing portfolio images"""

    print("="*80)
    print("ISN.BIZ Portfolio Image Generator")
    print("="*80)
    print(f"Output directory: {OUTPUT_DIR}")
    print(f"Model: fal-ai/gpt-image-1.5")
    print(f"Quality: low (cost control)")
    print(f"Size: 1600x900 WebP")
    print()

    results = []

    # Generate each image
    for project_key, config in PROMPTS.items():
        result = generate_image(config["prompt"], config["filename"])

        if result:
            # Download the image
            filepath = OUTPUT_DIR / config["filename"]
            if download_image(result["url"], filepath):
                result["local_path"] = str(filepath)
                results.append(result)

                # Note about responsive variants
                create_responsive_variants(filepath)

        # Rate limiting
        time.sleep(3)

    # Summary
    print("\n" + "="*80)
    print("GENERATION COMPLETE")
    print("="*80)

    if results:
        print(f"\nSuccessfully generated {len(results)}/3 images:")
        for r in results:
            print(f"\n  {r['filename']}")
            print(f"    Local: {r['local_path']}")
            print(f"    URL: {r['url']}")

        # Save manifest
        manifest_path = OUTPUT_DIR / "generation_manifest.json"
        with open(manifest_path, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"\nManifest saved: {manifest_path}")

        # S3 upload instructions
        print("\n" + "="*80)
        print("NEXT STEPS: Upload to S3")
        print("="*80)
        print("\nRun these commands to upload:")
        print(f"\ncd {OUTPUT_DIR}")
        print("aws s3 sync . s3://isnbiz-assets-1769962280/premium_v3/portfolio/ \\")
        print("  --exclude '*' \\")
        print("  --include '*.webp' \\")
        print("  --content-type 'image/webp' \\")
        print("  --cache-control 'max-age=31536000'")

        print("\nS3 URLs will be:")
        for r in results:
            s3_url = f"https://isnbiz-assets-1769962280.s3.amazonaws.com/premium_v3/portfolio/{r['filename']}"
            print(f"  {s3_url}")

    else:
        print("\nERROR: No images were generated successfully")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
