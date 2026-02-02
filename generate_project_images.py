#!/usr/bin/env python3
"""Generate project images for ISN.BIZ using FAL API"""

import os
import requests
import json
from pathlib import Path

# FAL API configuration
FAL_API_KEY = os.getenv('FAL_API_KEY', '')
if not FAL_API_KEY:
    with open('.env') as f:
        for line in f:
            if 'FAL_API_KEY' in line:
                FAL_API_KEY = line.split('=')[1].strip()

print(f"Using FAL API (key: {FAL_API_KEY[:20]}...)")

# Simple test
url = "https://fal.run/fal-ai/gpt-image-1.5"
headers = {
    "Authorization": f"Key {FAL_API_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "prompt": "professional data center server rack, blue LED lights, technical photography",
    "image_size": {"width": 1024, "height": 768},
    "num_images": 1,
    "quality": "low"
}

print("Testing FAL API...")
response = requests.post(url, headers=headers, json=payload, timeout=120)
print(f"Status: {response.status_code}")
print(response.text[:500])

