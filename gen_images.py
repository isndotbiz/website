import os, requests, time
from pathlib import Path
from PIL import Image
import io

FAL_KEY = "64b786c3-d6b1-4fbb-9d46-9211ceea552f:d472cdf8c68b4fe873557ca33bfb25eb"
output_dir = Path('assets/projects')
output_dir.mkdir(parents=True, exist_ok=True)

projects = {
    'truenas': ['server rack blue LED technical', 'monitoring dashboard dark', 'container architecture', 'AI pipeline network'],
    'videogen': ['video timeline dark UI', 'production pipeline', 'YouTube dashboard', 'AI video interface'],
    'bin': ['fraud dashboard cybersecurity', 'card analysis grid', 'threat monitoring', 'intel database dark'],
    'cli': ['terminal syntax highlighting', 'CLI diagram', 'command output colorful', 'framework components']
}

def gen(prompt, name):
    print(f"Generating {name}...")
    try:
        r = requests.post("https://fal.run/fal-ai/gpt-image-1.5",
            headers={"Authorization": f"Key {FAL_KEY}"},
            json={"prompt": prompt, "image_size": "1024x1024", "num_images": 1},
            timeout=120)
        if r.status_code == 200:
            url = r.json()['images'][0]['url']
            img = Image.open(io.BytesIO(requests.get(url).content))
            p = output_dir / f"{name}.webp"
            img.save(p, 'WEBP', quality=85)
            print(f"  OK: {p}")
            return True
        else:
            print(f"  FAIL: {r.status_code}")
    except Exception as e:
        print(f"  ERROR: {e}")
    return False

total = 0
for proj, prompts in projects.items():
    print(f"\n[{proj}]")
    for i, p in enumerate(prompts, 1):
        total += 1
        gen(p, f"{proj}_{i}")
        time.sleep(1)

print(f"\nDone: {total} attempted")
