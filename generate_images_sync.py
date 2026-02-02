#!/usr/bin/env python3
"""Generate portfolio images synchronously with immediate output"""

import requests
import json
import time
from pathlib import Path

# Configuration
FAL_API_KEY = "64b786c3-d6b1-4fbb-9d46-9211ceea552f:d472cdf8c68b4fe873557ca33bfb25eb"
OUTPUT_DIR = Path("/home/jdmal/workspace/ISNBIZ_Files/assets/premium_v3/portfolio")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Simplified prompts
PROMPTS = {
    "cli_template.webp": "Dark tech environment with holographic CLI terminal interface showing TypeScript code scaffolding, directory trees, and test coverage indicators as glowing 3D elements. Blue and cyan accents highlight npm commands and build pipelines. Professional developer tool aesthetic. Dark #0D1117 background, no text, no logos.",

    "comfyui_wan.webp": "Dark enterprise dashboard showing holographic ComfyUI workflow node graph with interconnected processing blocks, GPU status indicators, and batch processing queues. Blue and cyan accents illuminate Flux model connections and LoRA management. Abstract generative art thumbnails float in translucent cards. Dark #0D1117 background, no text, no logos.",

    "gedcom_processing.webp": "Professional data processing environment with holographic family tree network visualization showing nodes and relationship connections. Blue and cyan accents highlight cleaned data, deduplication processes, and audit trails. Abstract genealogical graph with validation indicators and processing pipeline status. Dark #0D1117 background, no text, no logos."
}

print("Starting image generation...")
print(f"Output: {OUTPUT_DIR}\n")

results = []

for filename, prompt in PROMPTS.items():
    print(f"{'='*80}")
    print(f"Generating: {filename}")
    print(f"{'='*80}")

    # Use fal.ai synchronous endpoint
    url = "https://fal.run/fal-ai/gpt-image-1.5"

    headers = {
        "Authorization": f"Key {FAL_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "prompt": prompt,
        "image_size": "1536x1024",  # Closest to 16:9, landscape orientation
        "num_images": 1,
        "quality": "low",
        "output_format": "webp"
    }

    try:
        print("Sending request...")
        response = requests.post(url, headers=headers, json=payload, timeout=120)

        if response.status_code == 200:
            data = response.json()
            image_url = data.get("images", [{}])[0].get("url")

            if image_url:
                print(f"Generated: {image_url}")

                # Download
                print("Downloading...")
                img_response = requests.get(image_url)

                if img_response.status_code == 200:
                    filepath = OUTPUT_DIR / filename
                    filepath.write_bytes(img_response.content)
                    size_kb = len(img_response.content) / 1024
                    print(f"Saved: {filepath} ({size_kb:.1f} KB)")

                    results.append({
                        "filename": filename,
                        "url": image_url,
                        "local_path": str(filepath),
                        "size_kb": size_kb
                    })
                else:
                    print(f"Download failed: HTTP {img_response.status_code}")
            else:
                print("No image URL in response")
        else:
            print(f"API error: HTTP {response.status_code}")
            print(response.text)

    except Exception as e:
        print(f"Error: {e}")

    print()
    time.sleep(2)  # Rate limiting

# Summary
print("="*80)
print(f"COMPLETE: {len(results)}/3 images generated")
print("="*80)

for r in results:
    print(f"\n{r['filename']}")
    print(f"  Size: {r['size_kb']:.1f} KB")
    print(f"  Local: {r['local_path']}")
    print(f"  URL: {r['url']}")

# Save manifest
if results:
    manifest = OUTPUT_DIR / "manifest.json"
    with open(manifest, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\nManifest: {manifest}")

print("\nS3 URLs (after upload):")
for r in results:
    s3_url = f"https://isnbiz-assets-1769962280.s3.amazonaws.com/premium_v3/portfolio/{r['filename']}"
    print(f"  {s3_url}")
