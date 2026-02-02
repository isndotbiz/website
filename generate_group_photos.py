#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate group photos with founders together"""

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

def generate(img_urls, prompt, out_path):
    print(f"  Generating: {out_path.name}...")
    result = fal_client.subscribe(
        "fal-ai/gpt-image-1.5/edit",
        arguments={
            "image_urls": img_urls,
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

group_dir = Path("assets/founders/group_photos")
group_dir.mkdir(parents=True, exist_ok=True)

# Upload all founder images
founders = {
    'alicia': '1/a1.png',
    'bri': '1/b1.png',
    'jonathan': '1/j1.png',
    'lilly': '1/l1.png'
}

print("Uploading founder images...")
founder_urls = {}
for name, path in founders.items():
    founder_urls[name] = upload_image(path)
    print(f"  ✅ {name}")

# Group photo scenarios
group_scenarios = [
    {
        'name': 'team_meeting',
        'prompt': 'Professional team meeting with 4 founders sitting around modern conference table, collaborative discussion, some looking at documents or screens, some conversing with each other, professional business attire, modern office conference room, natural corporate photography. Preserve the exact faces from the original images - same facial features, skin tones, and appearances for all people.',
        'urls': list(founder_urls.values())
    },
    {
        'name': 'team_presentation',
        'prompt': 'Startup team of 4 founders giving presentation together, one presenting at whiteboard while others watch and collaborate, professional business casual attire, modern startup office, team collaboration scene. Preserve the exact faces from the original images - same facial features, skin tones, and appearances for all people.',
        'urls': list(founder_urls.values())
    },
    {
        'name': 'team_casual',
        'prompt': 'Casual team photo of 4 startup founders in modern co-working space, standing together in relaxed professional poses, some with arms crossed, some with hands in pockets, smart casual business attire, natural indoor lighting, modern office background. Preserve the exact faces from the original images - same facial features, skin tones, and appearances for all people.',
        'urls': list(founder_urls.values())
    },
    {
        'name': 'team_brainstorm',
        'prompt': 'Creative brainstorming session with 4 founders around whiteboard or large screen, actively discussing and collaborating, varied poses and gestures, professional casual attire, modern innovative workspace, dynamic team interaction. Preserve the exact faces from the original images - same facial features, skin tones, and appearances for all people.',
        'urls': list(founder_urls.values())
    }
]

print("\n" + "="*60)
print("Generating group photos...")
print("="*60)

for scenario in group_scenarios:
    print(f"\n🎨 {scenario['name'].upper()}")
    out_path = group_dir / f"{scenario['name']}.png"
    generate(scenario['urls'], scenario['prompt'], out_path)

print("\n" + "="*60)
print("✅ ALL GROUP PHOTOS COMPLETE!")
print(f"Total images: {len(list(group_dir.glob('*.png')))}/4")
print("="*60)
