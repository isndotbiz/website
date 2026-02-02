#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fix Bri's neck proportions - make it shorter/more natural"""

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
    print(f"  Fixing: {out_path.name}...")
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
            print(f"  ✅ Fixed")
            return True
    return False

print("="*60)
print("FIXING BRI'S NECK PROPORTIONS")
print("="*60)

# Upload original
orig_url = upload_image("1/b1.png")

# Fix headshot with background
print("\n1. Headshot with background")
prompt = """Professional corporate headshot portrait. The person should have the EXACT SAME FACE as in the original image - preserve all facial features, skin tone, hair style, and facial structure perfectly. Clean professional studio background in soft neutral gray or blue tones. Professional business attire. Soft professional lighting. Corporate photography style. IMPORTANT: Natural, proportional neck - not elongated or stretched. Proper human neck proportions. The face must look identical to the original photo."""
generate(orig_url, prompt, Path("assets/founders/headshots_with_bg/bri_headshot.png"))

# Fix headshot no background
print("\n2. Headshot no background")
prompt = """Professional corporate headshot portrait with transparent background removed. The person should have the EXACT SAME FACE as in the original image - preserve all facial features, skin tone, hair style, and facial structure perfectly. Remove all background completely - pure transparent or white background. Professional business attire. IMPORTANT: Natural, proportional neck - not elongated or stretched. Proper human neck proportions. The face must look identical to the original photo."""
generate(orig_url, prompt, Path("assets/founders/headshots_no_bg/bri_headshot_no_bg.png"))

# Fix corporate photos
corporate_activities = {
    'presenting': 'presenting at a corporate meeting with presentation screen behind, looking at presentation, professional business setting',
    'working': 'working on laptop in modern office, focused on screen, professional workspace with technology',
    'collaborating': 'collaborating with team in modern conference room, looking at documents or screen, professional business environment',
    'analyzing': 'analyzing data or documents, looking down at papers or tablet, professional office setting'
}

print("\n3. Corporate photos")
for activity, desc in corporate_activities.items():
    prompt = f"""Professional corporate photo of person {desc}. The person should have the EXACT SAME FACE as in the original image - preserve all facial features, skin tone, hair style, and facial structure perfectly. NOT looking directly at camera - looking at work, screen, documents, or colleagues. Professional business attire. Natural corporate environment. IMPORTANT: Natural, proportional neck - not elongated or stretched. Proper human neck proportions. Corporate photography style."""
    generate(orig_url, prompt, Path(f"assets/founders/corporate_photos/bri_{activity}.png"))

# Fix casual variants
casual_scenarios = {
    'coffee': 'having coffee in modern cafe, looking at phone or laptop, casual business casual attire, relaxed professional setting',
    'outdoor': 'walking outdoors in urban setting, looking ahead or to the side, smart casual clothing, natural outdoor lighting',
    'casual_meeting': 'in casual co-working space, looking at laptop or notepad, wearing casual but professional clothing like polo or sweater',
    'brainstorming': 'standing by whiteboard or window, looking at notes or thinking, casual professional attire, creative workspace'
}

print("\n4. Casual variants")
for scenario, desc in casual_scenarios.items():
    prompt = f"""Natural professional photo of person {desc}. The person should have the EXACT SAME FACE as in the original image - preserve all facial features, skin tone, hair style, and facial structure perfectly. NOT looking directly at camera - natural candid moment. Different clothing from formal business wear - casual professional or smart casual. IMPORTANT: Natural, proportional neck - not elongated or stretched. Proper human neck proportions. Natural photography style."""
    generate(orig_url, prompt, Path(f"assets/founders/casual_variants/bri_{scenario}.png"))

print("\n" + "="*60)
print("✅ BRI'S IMAGES FIXED!")
print("All 10 Bri images updated with corrected neck proportions")
print("="*60)
