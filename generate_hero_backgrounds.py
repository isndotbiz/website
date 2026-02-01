#!/usr/bin/env python3
import requests, io, os, time, boto3
from PIL import Image

FAL_API_KEY = "64b786c3-d6b1-4fbb-9d46-9211ceea552f:d472cdf8c68b4fe873557ca33bfb25eb"
FAL_ENDPOINT = "https://fal.run/fal-ai/gpt-image-1.5"
S3_BUCKET = "isnbiz-assets-1769962280"
BASE_DIR = "D:/workspace/ISNBIZ_Files/assets/premium_v3"
HERO_DIR = os.path.join(BASE_DIR, "hero")
SECTIONS_DIR = os.path.join(BASE_DIR, "sections")
os.makedirs(HERO_DIR, exist_ok=True)
os.makedirs(SECTIONS_DIR, exist_ok=True)

IMAGES = [
    {"name": "hero_home", "local_dir": HERO_DIR, "s3_prefix": "premium_v3/hero",
     "prompt": "Dark charcoal (#0D1117) technology environment. Sparse luminous data streams in electric blue (#1E9FF2) flowing as gentle arcs across the frame. Faint grid of cyan (#5FDFDF) lines barely visible in the deep background. Volumetric light rays creating depth. Extremely subtle, atmospheric, premium. Most of the image is dark negative space. No text, no logos, no people, no watermarks. Intended use: website hero background."},
    {"name": "hero_interior", "local_dir": HERO_DIR, "s3_prefix": "premium_v3/hero",
     "prompt": "Minimalist dark (#0D1117) abstract space with soft ambient glow. Faint circuit traces in blue (#1E9FF2) creating delicate pathways through darkness. Glass-like reflective surfaces catching cyan (#5FDFDF) light. Cinematic, atmospheric, nearly black with subtle light details. Clean negative space on right third. No text, no logos, no people, no watermarks. Intended use: secondary hero background."},
    {"name": "investor_backdrop", "local_dir": SECTIONS_DIR, "s3_prefix": "premium_v3/sections",
     "prompt": "Very dark (#0D1117) financial technology atmosphere. Extremely subtle line graph silhouettes barely visible in background. Soft blue (#1E9FF2) gradient glow along bottom edge. Minimal geometric overlays with faint cyan (#5FDFDF) accents. Refined, restrained, premium. 90 percent dark negative space. No readable numbers, no text, no logos, no watermarks. Intended use: investor section background."},
    {"name": "cta_energy_burst", "local_dir": SECTIONS_DIR, "s3_prefix": "premium_v3/sections",
     "prompt": "Dark void (#0D1117) with a flowing ribbon of blue (#1E9FF2) and cyan (#5FDFDF) light sweeping through the center. Gentle particle glow along the light trail. Energy feels contained and precise, not chaotic. Most of frame is dark. Clean negative space in center for text overlay. No text, no logos, no watermarks. Intended use: call-to-action background."},
]

def generate_image(prompt, name):
    sep = "=" * 60
    print("\n" + sep)
    print("[GENERATE] " + name)
    print(sep)
    print("  Prompt: " + prompt[:80] + "...")
    headers = {"Authorization": "Key " + FAL_API_KEY, "Content-Type": "application/json"}
    payload = {"prompt": prompt, "image_size": "1536x1024", "quality": "low"}
    print("  Sending request to fal.ai (1536x1024, quality=low)...")
    start = time.time()
    resp = requests.post(FAL_ENDPOINT, headers=headers, json=payload, timeout=120)
    elapsed = time.time() - start
    print("  Response status: {} (took {:.1f}s)".format(resp.status_code, elapsed))
    if resp.status_code != 200:
        print("  ERROR: " + resp.text[:500])
        raise RuntimeError("fal.ai returned {}: {}".format(resp.status_code, resp.text[:300]))
    result = resp.json()
    image_url = result["images"][0]["url"]
    print("  Image URL: " + image_url[:100] + "...")
    return image_url

def download_image(url):
    print("  Downloading image...")
    resp = requests.get(url, timeout=60)
    resp.raise_for_status()
    img = Image.open(io.BytesIO(resp.content))
    print("  Downloaded: {}x{} ({})".format(img.size[0], img.size[1], img.mode))
    return img

def crop_to_16_9(img):
    w, h = img.size
    target_ratio = 16.0 / 9.0
    current_ratio = float(w) / float(h)
    if abs(current_ratio - target_ratio) < 0.01:
        print("  Already 16:9, no crop needed.")
        return img
    if current_ratio > target_ratio:
        new_w = int(h * target_ratio)
        left = (w - new_w) // 2
        box = (left, 0, left + new_w, h)
    else:
        new_h = int(w / target_ratio)
        top = (h - new_h) // 2
        box = (0, top, w, top + new_h)
    cropped = img.crop(box)
    print("  Cropped: {}x{} -> {}x{} (16:9)".format(w, h, cropped.size[0], cropped.size[1]))
    return cropped

def save_images(img, local_dir, name):
    png_path = os.path.join(local_dir, name + ".png")
    webp_path = os.path.join(local_dir, name + ".webp")
    img.save(png_path, "PNG", optimize=True)
    png_size = os.path.getsize(png_path)
    print("  Saved PNG: {} ({:.0f} KB)".format(png_path, png_size / 1024))
    img.save(webp_path, "WEBP", quality=75, method=6)
    webp_size = os.path.getsize(webp_path)
    print("  Saved WebP: {} ({:.0f} KB)".format(webp_path, webp_size / 1024))
    print("  Compression ratio: {:.0f}% of PNG size".format(webp_size / png_size * 100))
    return png_path, webp_path

def upload_to_s3(webp_path, s3_prefix, name):
    s3_key = s3_prefix + "/" + name + ".webp"
    print("  Uploading to s3://{}/{} ...".format(S3_BUCKET, s3_key))
    s3 = boto3.client("s3")
    s3.upload_file(webp_path, S3_BUCKET, s3_key,
        ExtraArgs={"ContentType": "image/webp", "CacheControl": "public, max-age=31536000"})
    s3_url = "https://{}.s3.amazonaws.com/{}".format(S3_BUCKET, s3_key)
    print("  Uploaded: " + s3_url)
    return s3_url

def main():
    sep = "=" * 60
    print(sep)
    print("ISN.BIZ Hero & Section Background Generator")
    print(sep)
    print("Output dirs:")
    print("  Hero:     " + HERO_DIR)
    print("  Sections: " + SECTIONS_DIR)
    print("  S3:       s3://{}/premium_v3/".format(S3_BUCKET))
    print("  Images:   {}".format(len(IMAGES)))
    results = []
    for img_def in IMAGES:
        name = img_def["name"]
        local_dir = img_def["local_dir"]
        s3_prefix = img_def["s3_prefix"]
        prompt = img_def["prompt"]
        try:
            image_url = generate_image(prompt, name)
            img = download_image(image_url)
            img = crop_to_16_9(img)
            png_path, webp_path = save_images(img, local_dir, name)
            s3_url = upload_to_s3(webp_path, s3_prefix, name)
            results.append({"name": name, "status": "SUCCESS", "png_path": png_path,
                            "webp_path": webp_path, "s3_url": s3_url,
                            "dimensions": "{}x{}".format(img.size[0], img.size[1])})
        except Exception as e:
            print("\n  FAILED: {} - {}".format(name, e))
            results.append({"name": name, "status": "FAILED: {}".format(e), "s3_url": None})
    print("\n")
    print(sep)
    print("SUMMARY")
    print(sep)
    for r in results:
        if r["status"] == "SUCCESS":
            print("\n  [OK] " + r["name"])
            print("       Dimensions: " + r["dimensions"])
            print("       PNG:  " + r["png_path"])
            print("       WebP: " + r["webp_path"])
            print("       S3:   " + r["s3_url"])
        else:
            print("\n  [FAIL] {}: {}".format(r["name"], r["status"]))
    print("\n" + sep)
    print("S3 URLs (for CSS/HTML):")
    print(sep)
    for r in results:
        if r.get("s3_url"):
            print("  {}: {}".format(r["name"], r["s3_url"]))
    success_count = sum(1 for r in results if r["status"] == "SUCCESS")
    print("\nCompleted: {}/{} images generated and uploaded.".format(success_count, len(IMAGES)))

if __name__ == "__main__":
    main()
