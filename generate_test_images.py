#!/usr/bin/env python3
"""
Generate TEST images with fal.ai to compare models
"""
import subprocess
import fal_client
from pathlib import Path

# Get API key
result = subprocess.run([
    'op', 'item', 'get', 'FAL API Key',
    '--vault', 'TrueNAS Infrastructure',
    '--fields', 'credential', '--reveal'
], capture_output=True, text=True)
FAL_KEY = result.stdout.strip()

# Configure fal
fal_client.api_key = FAL_KEY

output_dir = Path("assets/test-samples")
output_dir.mkdir(parents=True, exist_ok=True)

print("🎨 Generating test images with fal.ai models...")
print("="*70)

# Test 1: Hero Background with nano-banana-pro
print("\n1. Testing fal-ai/nano-banana-pro (hero background)...")
try:
    result = fal_client.subscribe(
        "fal-ai/nano-banana-pro",
        arguments={
            "prompt": "Abstract futuristic technology background, dark blue and cyan colors, geometric patterns, professional clean modern digital grid, subtle gradients, high tech aesthetic, wallpaper, 4K",
            "image_size": "landscape_16_9",
            "num_images": 1
        }
    )
    if result and 'images' in result and len(result['images']) > 0:
        image_url = result['images'][0]['url']
        print(f"   ✓ Generated: {image_url}")
        # Download
        import requests
        img_data = requests.get(image_url).content
        with open(output_dir / 'nano-banana-pro_hero.png', 'wb') as f:
            f.write(img_data)
        print(f"   ✓ Saved: assets/test-samples/nano-banana-pro_hero.png")
except Exception as e:
    print(f"   ✗ Error: {e}")

# Test 2: Hero Background with flux-pro/kontext
print("\n2. Testing fal-ai/flux-pro/kontext (hero background)...")
try:
    result = fal_client.subscribe(
        "fal-ai/flux-pro/kontext",
        arguments={
            "prompt": "Abstract futuristic technology background, dark blue (#1E9FF2) and cyan (#5FDFDF) gradient, geometric patterns, professional, modern, digital, clean, high resolution wallpaper",
            "image_size": "landscape_16_9",
            "num_inference_steps": 28
        }
    )
    if result and 'images' in result and len(result['images']) > 0:
        image_url = result['images'][0]['url']
        print(f"   ✓ Generated: {image_url}")
        import requests
        img_data = requests.get(image_url).content
        with open(output_dir / 'flux-pro-kontext_hero.png', 'wb') as f:
            f.write(img_data)
        print(f"   ✓ Saved: assets/test-samples/flux-pro-kontext_hero.png")
except Exception as e:
    print(f"   ✗ Error: {e}")

# Test 3: Service Icon with nano-banana-pro
print("\n3. Testing nano-banana-pro (service icon - AI/ML)...")
try:
    result = fal_client.subscribe(
        "fal-ai/nano-banana-pro",
        arguments={
            "prompt": "Minimalist AI brain icon, geometric neural network design, blue (#1E9FF2) and cyan (#5FDFDF) colors, clean modern lines, professional tech icon, simple, scalable vector style",
            "image_size": "square",
            "num_images": 1
        }
    )
    if result and 'images' in result and len(result['images']) > 0:
        image_url = result['images'][0]['url']
        print(f"   ✓ Generated: {image_url}")
        import requests
        img_data = requests.get(image_url).content
        with open(output_dir / 'nano-banana-pro_icon_ai.png', 'wb') as f:
            f.write(img_data)
        print(f"   ✓ Saved: assets/test-samples/nano-banana-pro_icon_ai.png")
except Exception as e:
    print(f"   ✗ Error: {e}")

print("\n" + "="*70)
print("✓ Test generation complete!")
print("="*70)
print("\nCheck assets/test-samples/ to see results")
print("Compare quality and choose which model to use for full generation")
