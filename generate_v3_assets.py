#!/usr/bin/env python3
import requests, os, io, time, json
from PIL import Image

FAL_API_KEY = "64b786c3-d6b1-4fbb-9d46-9211ceea552f:d472cdf8c68b4fe873557ca33bfb25eb"
FAL_ENDPOINT = "https://fal.run/fal-ai/gpt-image-1.5"
HEADERS = {"Authorization": "Key " + FAL_API_KEY, "Content-Type": "application/json"}

BASE_DIR = "D:/workspace/ISNBIZ_Files/assets/premium_v3"
SERVICES_DIR = os.path.join(BASE_DIR, "services")
PORTFOLIO_DIR = os.path.join(BASE_DIR, "portfolio")
S3_BUCKET = "isnbiz-assets-1769962280"
S3_PREFIX_SVC = "premium_v3/services"
S3_PREFIX_PF = "premium_v3/portfolio"

SERVICES = [
    {"name": "ai_research", "prompt": "Floating holographic AI research dashboard on pure dark (#0D1117) background. Translucent glass cards showing abstract neural network visualizations, graphs, and node clusters. Blue (#1E9FF2) and cyan (#5FDFDF) glow emanating from the interface elements. Dashboard appears to float in a dark void. No readable text, no logos, no watermarks. Premium enterprise aesthetic."},
    {"name": "enterprise_automation", "prompt": "Holographic automation pipeline interface floating on dark (#0D1117) void. Translucent workflow lanes with connected glowing nodes and status indicators in blue (#1E9FF2). Subtle cyan (#5FDFDF) particle trails connecting pipeline stages. Interface feels weightless, futuristic, hovering in darkness. No readable text, no logos, no watermarks."},
    {"name": "rag_and_search", "prompt": "Floating translucent knowledge graph interface on dark (#0D1117) background. Luminous search bar with expanding node-link visualization below. Analytics cards with abstract data in blue (#1E9FF2) and cyan (#5FDFDF) glow. Interface elements appear as holographic glass panels suspended in dark space. No readable text, no logos, no watermarks."},
]

PORTFOLIO = [
    {"name": "opportunity_bot", "prompt": "Holographic analytics dashboard floating in dark (#0D1117) void. Abstract opportunity ranking list, scoring cards with radial gauges, and trend line chart. All elements translucent with blue (#1E9FF2) glow and cyan (#5FDFDF) accents. Suggests AI-powered intelligence. No readable text, no logos, no watermarks."},
    {"name": "credit_automation", "prompt": "Floating fintech compliance interface on dark (#0D1117) background. Abstract automated pipeline view with glowing checkmarks, risk flag indicators in amber, and report generation cards. Primary glow in blue (#1E9FF2) with subtle cyan (#5FDFDF) data streams. Holographic glass aesthetic. No readable text, no logos, no watermarks."},
    {"name": "hroc_website", "prompt": "Holographic website mockup floating in dark (#0D1117) void. Translucent browser frame showing abstract nonprofit layout with hero banner area, navigation bar, and content blocks. Warm community feel suggested through soft blue (#1E9FF2) glow with cyan (#5FDFDF) accent elements. Modern responsive design. No readable text, no logos, no watermarks."},
    {"name": "rag_bi", "prompt": "Floating high-end analytics platform on dark (#0D1117) background. Translucent search interface, knowledge graph with glowing nodes, vector embedding visualization panel, and KPI cards. Data-dense but clean. Blue (#1E9FF2) primary glow, cyan (#5FDFDF) connection lines. Holographic glass depth. No readable text, no logos, no watermarks."},
    {"name": "androidaps_health", "prompt": "Photorealistic smartphone floating in dark (#0D1117) void with medical dashboard UI glowing on screen. Vitals graphs, heart rate indicator, and appointment cards visible as holographic projections extending beyond the phone screen. Blue (#1E9FF2) medical data glow, cyan (#5FDFDF) accents. No readable text, no logos, no watermarks."},
    {"name": "infrastructure", "prompt": "Holographic infrastructure monitoring dashboard floating on dark (#0D1117) background. Network topology map with glowing nodes, server health cards with status bars, and pipeline status indicators. Blue (#1E9FF2) primary glow with cyan (#5FDFDF) node connections. Enterprise ops aesthetic. No readable text, no logos, no watermarks."},
]


def generate_image(prompt, name):
    print("  [fal.ai] Generating: " + name + " ...")
    payload = {"prompt": prompt, "image_size": "1536x1024", "quality": "low"}
    resp = requests.post(FAL_ENDPOINT, headers=HEADERS, json=payload, timeout=120)
    resp.raise_for_status()
    result = resp.json()
    image_url = result["images"][0]["url"]
    print("  [fal.ai] Got URL for " + name + ": " + image_url[:80] + "...")
    img_resp = requests.get(image_url, timeout=60)
    img_resp.raise_for_status()
    return img_resp.content


def save_service_image(raw_bytes, name):
    img = Image.open(io.BytesIO(raw_bytes))
    print("  [process] " + name + ": raw size " + str(img.size))
    png_path = os.path.join(SERVICES_DIR, name + ".png")
    img.save(png_path, "PNG")
    print("  [save] PNG: " + png_path + " (" + str(int(os.path.getsize(png_path) / 1024)) + " KB)")
    webp_path = os.path.join(SERVICES_DIR, name + ".webp")
    img.save(webp_path, "WEBP", quality=75)
    print("  [save] WebP: " + webp_path + " (" + str(int(os.path.getsize(webp_path) / 1024)) + " KB)")
    return webp_path


def save_portfolio_image(raw_bytes, name):
    img = Image.open(io.BytesIO(raw_bytes))
    w, h = img.size
    print("  [process] " + name + ": raw size " + str(img.size))
    target_ratio = 7.0 / 5.0
    current_ratio = float(w) / float(h)
    if current_ratio > target_ratio:
        new_w = int(h * target_ratio)
        left = (w - new_w) // 2
        img = img.crop((left, 0, left + new_w, h))
    else:
        new_h = int(w / target_ratio)
        top = (h - new_h) // 2
        img = img.crop((0, top, w, top + new_h))
    print("  [crop] " + name + ": cropped to " + str(img.size))
    img = img.resize((700, 500), Image.LANCZOS)
    print("  [resize] " + name + ": resized to " + str(img.size))
    png_path = os.path.join(PORTFOLIO_DIR, name + ".png")
    img.save(png_path, "PNG")
    print("  [save] PNG: " + png_path + " (" + str(int(os.path.getsize(png_path) / 1024)) + " KB)")
    webp_path = os.path.join(PORTFOLIO_DIR, name + ".webp")
    img.save(webp_path, "WEBP", quality=75)
    print("  [save] WebP: " + webp_path + " (" + str(int(os.path.getsize(webp_path) / 1024)) + " KB)")
    return webp_path


def upload_to_s3(local_path, s3_key):
    import boto3
    s3 = boto3.client("s3")
    print("  [s3] Uploading " + os.path.basename(local_path) + " -> s3://" + S3_BUCKET + "/" + s3_key)
    s3.upload_file(local_path, S3_BUCKET, s3_key,
        ExtraArgs={"ContentType": "image/webp", "CacheControl": "public, max-age=31536000"})
    url = "https://" + S3_BUCKET + ".s3.amazonaws.com/" + s3_key
    return url


def main():
    all_s3_urls = {}
    print("")
    print("=" * 70)
    print("GENERATING SERVICE IMAGES (3)")
    print("=" * 70)
    for item in SERVICES:
        name = item["name"]
        prompt = item["prompt"]
        print("")
        print("--- " + name + " ---")
        raw = generate_image(prompt, name)
        webp_path = save_service_image(raw, name)
        s3_key = S3_PREFIX_SVC + "/" + name + ".webp"
        url = upload_to_s3(webp_path, s3_key)
        all_s3_urls[name] = url
        print("  [done] " + url)
        time.sleep(1)
    print("")
    print("=" * 70)
    print("GENERATING PORTFOLIO IMAGES (6)")
    print("=" * 70)
    for item in PORTFOLIO:
        name = item["name"]
        prompt = item["prompt"]
        print("")
        print("--- " + name + " ---")
        raw = generate_image(prompt, name)
        webp_path = save_portfolio_image(raw, name)
        s3_key = S3_PREFIX_PF + "/" + name + ".webp"
        url = upload_to_s3(webp_path, s3_key)
        all_s3_urls[name] = url
        print("  [done] " + url)
        time.sleep(1)
    print("")
    print("=" * 70)
    print("ALL S3 URLS")
    print("=" * 70)
    print("")
    print("SERVICES:")
    for item in SERVICES:
        name = item["name"]
        print("  " + name + ": " + all_s3_urls[name])
    print("")
    print("PORTFOLIO:")
    for item in PORTFOLIO:
        name = item["name"]
        print("  " + name + ": " + all_s3_urls[name])
    manifest_path = os.path.join(BASE_DIR, "s3_urls.json")
    with open(manifest_path, "w") as mf:
        json.dump(all_s3_urls, mf, indent=2)
    print("")
    print("Manifest saved: " + manifest_path)
    print("")
    print("[COMPLETE] All 9 images generated, processed, and uploaded to S3.")


if __name__ == "__main__":
    main()
