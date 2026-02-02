import os, requests, base64
from pathlib import Path
from PIL import Image
import io

FAL_KEY = "64b786c3-d6b1-4fbb-9d46-9211ceea552f:d472cdf8c68b4fe873557ca33bfb25eb"
source_dir = Path('1')
output_dir = Path('assets/founders')
output_dir.mkdir(parents=True, exist_ok=True)

# Source photos
founders = {
    'bri': '1/b1.png',
    'lilly': '1/l1.png',
    'jonathan': '1/j1.png',
    'alicia': '1/a1.png'
}

# Edit scenarios (NOT looking at camera)
scenarios = [
    'professional office setting working at desk, candid side view, natural lighting',
    'business meeting discussion, engaged with colleagues, profile view',
    'presentation to team, gesturing at screen, three-quarter view',
    'strategic planning session reviewing documents, focused on work'
]

def encode_image(path):
    with open(path, 'rb') as f:
        return base64.b64encode(f.read()).decode()

def gen_edit(name, source, prompt, num):
    print(f"Editing {name}_{num}...")
    try:
        img_b64 = encode_image(source)
        r = requests.post("https://fal.run/fal-ai/gpt-image-1.5/edit",
            headers={"Authorization": f"Key {FAL_KEY}"},
            json={
                "image_url": f"data:image/png;base64,{img_b64}",
                "prompt": prompt,
                "image_size": "1024x1024",
                "num_images": 1
            },
            timeout=120)
        if r.status_code == 200:
            url = r.json()['images'][0]['url']
            img = Image.open(io.BytesIO(requests.get(url).content))
            p = output_dir / f"{name}_{num}.webp"
            img.save(p, 'WEBP', quality=90)
            print(f"  OK: {p}")
            return True
        else:
            print(f"  FAIL: {r.status_code} - {r.text[:100]}")
    except Exception as e:
        print(f"  ERROR: {e}")
    return False

for name, source in founders.items():
    print(f"\n[{name.upper()}]")
    for i, scenario in enumerate(scenarios, 1):
        gen_edit(name, source, scenario, i)

print("\nDone!")
