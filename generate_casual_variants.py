#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate casual/different clothing variants for each founder"""

import os
import sys
import fal_client
from pathlib import Path
import requests

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

os.environ['FAL_KEY'] = '64b786c3-d6b1-4fbb-9d46-9211ceea552f:d472cdf8c68b4fe873557ca33bfb25eb'

def upload_image(path):
    with open(path, 'rb') as f:
        return fal_client.upload(f.read(), "image/png")

def generate(img_url, prompt, out_path):
    print(f"  Generating: {out_path.name}...")
    result = fal_client.subscribe(
        "fal-ai/gpt-image-1.5/edit",
        arguments={
            "image_urls": [img_url],
            "prompt": prompt,
            "image_quality": "low",
            "num_images": 1,
            "output_format": "png"
        },
    )
    if result and 'images' in result:
        r = requests.get(result['images'][0]['url'])
        if r.status_code == 200:
            with open(out_path, 'wb') as f:
                f.write(r.content)
            print(f"  ✅ {out_path.name}")
            return True
    print(f"  ❌ Failed")
    return False

casual_dir = Path("assets/founders/casual_variants")
casual_dir.mkdir(parents=True, exist_ok=True)

# Different casual scenarios
scenarios = {
    'coffee': 'having coffee in modern cafe, looking at phone or laptop, casual business casual attire, relaxed professional setting',
    'outdoor': 'walking outdoors in urban setting, looking ahead or to the side, smart casual clothing, natural outdoor lighting',
    'casual_meeting': 'in casual co-working space, looking at laptop or notepad, wearing casual but professional clothing like polo or sweater',
    'brainstorming': 'standing by whiteboard or window, looking at notes or thinking, casual professional attire, creative workspace'
}

founders = {
    'alicia': '1/a1.png',
    'bri': '1/b1.png',
    'jonathan': '1/j1.png',
    'lilly': '1/l1.png'
}

for founder, img_path in founders.items():
    print(f"\n{'='*60}")
    print(f"👤 {founder.upper()} - Casual Variants")
    print(f"{'='*60}")

    img_url = upload_image(img_path)

    for scenario, desc in scenarios.items():
        prompt = f"""Natural professional photo of person {desc}. The person should have the EXACT SAME FACE as in the original image - preserve all facial features, skin tone, hair style, and facial structure perfectly. NOT looking directly at camera - natural candid moment. Different clothing from formal business wear - casual professional or smart casual. The face must look identical to the original photo - same person, same features, same appearance. Natural photography style."""

        out_path = casual_dir / f"{founder}_{scenario}.png"
        generate(img_url, prompt, out_path)

print("\n" + "="*60)
print("✅ ALL CASUAL VARIANTS COMPLETE!")
print(f"Total images: {len(list(casual_dir.glob('*.png')))}/16")
print("="*60)
