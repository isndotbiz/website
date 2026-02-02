#!/usr/bin/env python3
import os, requests, time
from pathlib import Path
from PIL import Image
import io

FAL_KEY = "64b786c3-d6b1-4fbb-9d46-9211ceea552f:d472cdf8c68b4fe873557ca33bfb25eb"
output_dir = Path('assets/projects')
output_dir.mkdir(parents=True, exist_ok=True)

projects = {
    'truenas': ['data center server rack with blue LED, technical photo', 'monitoring dashboard dark UI, graphs metrics', 'container architecture diagram clean', 'AI pipeline neural network blue cyan'],
    'videogen': ['video editing timeline dark UI blue', 'content production pipeline flowchart', 'YouTube analytics dashboard professional', 'AI video generation interface futuristic'],
    'bin-intel': ['fraud detection dashboard cybersecurity', 'payment card analysis data grid', 'real-time threat monitoring', 'intelligence database dark UI'],
    'cli': ['elegant terminal dark syntax highlighting', 'CLI architecture diagram technical', 'colorful command output developer', 'modular framework component diagram'],
    'comfyui': ['AI workflow nodes connections futuristic', 'flux model neural network blue', 'image processing pipeline', 'LoRA training progress UI dark'],
    'ged': ['family tree modern clean technical', 'GEDCOM pipeline flowchart', 'data quality dashboard metrics', 'genealogy database schema diagram'],
    'llm-opt': ['LLM performance dashboard graphs dark', 'model optimization neural curves', 'evaluation framework metrics UI', 'technique comparison chart'],
    'opportunity': ['business discovery dashboard cards', 'AI research pipeline flowchart', 'semantic search dark UI filters', 'scoring system graphs dashboard']
}

def gen(prompt, name):
    print(f"  Gen: {name}...")
    try:
        r = requests.post("https://fal.run/fal-ai/gpt-image-1.5",
            headers={"Authorization": f"Key {FAL_KEY}", "Content-Type": "application/json"},
            json={"prompt": prompt, "image_size": "1024x1024", "num_images": 1, "quality": "low"},
            timeout=120)
        if r.status_code == 200:
            url = r.json()['images'][0]['url']
            img = Image.open(io.BytesIO(requests.get(url, timeout=30).content))
            path = output_dir / f"{name}.webp"
            img.save(path, 'WEBP', quality=85)
            print(f"    ✓ {path}")
            return True
    except Exception as e:
        print(f"    ❌ {e}")
    return False

total, success = 0, 0
for proj, prompts in projects.items():
    print(f"\n📁 {proj.upper()}")
    for i, p in enumerate(prompts, 1):
        total += 1
        if gen(p, f"{proj}_{i}"):
            success += 1
        time.sleep(2)

print(f"\n✅ Done: {success}/{total} images")
