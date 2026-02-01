#!/usr/bin/env python3
"""
Generate website assets using fal.ai API
Uses: nano-banana-pro, gpt-image-1.5/edit, flux-pro/kontext
"""

import os
import sys
import json
import subprocess
from pathlib import Path

# Get API key from 1Password
def get_fal_key():
    """Get fal.ai API key from 1Password"""
    result = subprocess.run([
        'op', 'item', 'get', 'FAL API Key',
        '--vault', 'TrueNAS Infrastructure',
        '--fields', 'credential', '--reveal'
    ], capture_output=True, text=True)
    return result.stdout.strip()

# Set API key
FAL_KEY = get_fal_key()
os.environ['FAL_KEY'] = FAL_KEY

print(f"✓ fal.ai API key loaded ({len(FAL_KEY)} chars)")

# Test models with sample generation
test_prompts = {
    'hero_background': {
        'prompt': 'Abstract futuristic technology background, dark blue (#1E9FF2) and cyan (#5FDFDF) colors, geometric patterns, professional, clean, modern, digital grid, subtle gradients, high tech aesthetic, 4K resolution',
        'models': [
            'fal-ai/nano-banana-pro',
            'fal-ai/flux-pro/kontext'
        ]
    },
    'service_icon_ai': {
        'prompt': 'Minimalist AI/ML icon, geometric brain or neural network, blue (#1E9FF2) and cyan (#5FDFDF) colors, clean lines, professional, modern, suitable for website service icon, transparent background if possible',
        'models': [
            'fal-ai/nano-banana-pro',
            'fal-ai/flux-pro/kontext'
        ]
    },
    'portfolio_mockup': {
        'prompt': 'Modern SaaS dashboard interface mockup, clean professional UI, data visualizations, blue (#1E9FF2) accent colors, charts and graphs, professional business software interface, high detail, realistic, 16:9 aspect ratio',
        'models': [
            'fal-ai/nano-banana-pro',
            'fal-ai/flux-pro/kontext'
        ]
    }
}

print("\n" + "="*70)
print("fal.ai Asset Generation - Test Samples")
print("="*70)
print("\nGenerating test images with each model...")
print("This will create comparison samples for you to review.")
print("\nModels to test:")
print("  1. fal-ai/nano-banana-pro")
print("  2. fal-ai/flux-pro/kontext")
print("  3. fal-ai/gpt-image-1.5/edit (for photo enhancement)")
print("  4. fal-ai/nano-banana-pro/edit (for photo enhancement)")
print("\nTest prompts:")
for name, config in test_prompts.items():
    print(f"  - {name}")

print("\n" + "="*70)
print("Ready to generate! Run with fal-client library...")
print("="*70)

# Instructions for next steps
print("\nNEXT: Install fal-client and run generation")
print("pip install fal-client")
print("python3 generate_assets.py --test")
