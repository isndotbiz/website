#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quick generation of corporate photos for Jonathan and Lilly"""

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
    print(f"Generating: {out_path.name}...")
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
            print(f"✅ {out_path.name}")
            return True
    return False

corp_dir = Path("assets/founders/corporate_photos")
corp_dir.mkdir(parents=True, exist_ok=True)

activities = {
    'presenting': 'presenting at a corporate meeting with presentation screen behind, looking at presentation, professional business setting',
    'working': 'working on laptop in modern office, focused on screen, professional workspace with technology',
    'collaborating': 'collaborating with team in modern conference room, looking at documents or screen, professional business environment',
    'analyzing': 'analyzing data or documents, looking down at papers or tablet, professional office setting'
}

# Jonathan
print("\n=== JONATHAN ===")
j_url = upload_image("1/j1.png")
for act, desc in activities.items():
    prompt = f"""Professional corporate photo of person {desc}. The person should have the EXACT SAME FACE as in the original image - preserve all facial features, skin tone, hair style, and facial structure perfectly. NOT looking directly at camera - looking at work, screen, documents, or colleagues. Professional business attire. Natural corporate environment. Corporate photography style. The face must look identical to the original photo - same person, same features, same appearance."""
    generate(j_url, prompt, corp_dir / f"jonathan_{act}.png")

# Lilly
print("\n=== LILLY ===")
l_url = upload_image("1/l1.png")
for act, desc in activities.items():
    prompt = f"""Professional corporate photo of person {desc}. The person should have the EXACT SAME FACE as in the original image - preserve all facial features, skin tone, hair style, and facial structure perfectly. NOT looking directly at camera - looking at work, screen, documents, or colleagues. Professional business attire. Natural corporate environment. Corporate photography style. The face must look identical to the original photo - same person, same features, same appearance."""
    generate(l_url, prompt, corp_dir / f"lilly_{act}.png")

print("\n✅ ALL CORPORATE PHOTOS COMPLETE!")
