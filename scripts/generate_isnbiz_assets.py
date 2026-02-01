#!/usr/bin/env python3
"""
Generate targeted premium assets for isn.biz using fal.ai nano-banana-pro.
Outputs WebP files under /mnt/d/workspace/ISNBIZ_Files/assets/premium/<category>.
"""
from __future__ import annotations

import json
import os
import subprocess
import time
from pathlib import Path
from typing import Dict, List, Optional

import requests
from PIL import Image
from io import BytesIO


BASE_DIR = Path("/mnt/d/workspace/ISNBIZ_Files/assets/premium")
MODEL = "fal-ai/nano-banana-pro"


ASSETS: Dict[str, List[Dict[str, str]]] = {
    "hero": [
        {
            "name": "hero_home",
            "size": "landscape_16_9",
            "prompt": (
                "Cinematic abstract enterprise software background, sweeping data lines and luminous nodes, "
                "depth-of-field, brand palette (#1E9FF2 blue, #5FDFDF cyan, charcoal #3F4447), "
                "high-tech, premium, clean, minimal, wide composition, no text, no logos, no watermark"
            ),
        },
        {
            "name": "hero_interior",
            "size": "landscape_16_9",
            "prompt": (
                "Modern corporate technology gradient background, geometric polygons and subtle grid, "
                "blue/cyan highlights on dark charcoal, premium, minimal, wide 16:9 composition, "
                "no text, no logos, no watermark"
            ),
        },
    ],
    "sections": [
        {
            "name": "investor_backdrop",
            "size": "landscape_16_9",
            "prompt": (
                "Elegant dark investor background, subtle financial chart lines and soft glow, "
                "blue #1E9FF2 and cyan #5FDFDF accents, professional and premium, minimal, "
                "no text, no logos, no watermark"
            ),
        },
        {
            "name": "cta_energy",
            "size": "landscape_16_9",
            "prompt": (
                "Energetic call-to-action abstract background, dynamic waves and light trails, "
                "blue/cyan gradient, clean premium corporate aesthetic, wide 16:9 composition, "
                "no text, no logos, no watermark"
            ),
        },
    ],
    "portfolio": [
        {
            "name": "portfolio_opportunity_bot",
            "size": "landscape_16_9",
            "prompt": (
                "AI opportunity discovery dashboard, modern SaaS UI with cards, charts, risk scoring, "
                "and opportunity ranking, brand blue/cyan accents, realistic web app screenshot, "
                "high resolution, no text, no logos, no watermark"
            ),
        },
        {
            "name": "portfolio_credit_automation",
            "size": "landscape_16_9",
            "prompt": (
                "Secure automation monitoring dashboard, workflow timelines, compliance badges, "
                "health status cards, brand blue/cyan accents, clean enterprise UI, realistic web app, "
                "high resolution, no text, no logos, no watermark"
            ),
        },
        {
            "name": "portfolio_hroc_website",
            "size": "landscape_16_9",
            "prompt": (
                "Non-profit website homepage mockup, community-focused hero section, donation CTA, "
                "clean modern web layout, brand blue/cyan accents, realistic web design, "
                "high resolution, no text, no logos, no watermark"
            ),
        },
        {
            "name": "portfolio_rag_bi",
            "size": "landscape_16_9",
            "prompt": (
                "Enterprise RAG analytics platform, search bar, knowledge graph visualization, "
                "vector embeddings panel, KPI cards, brand blue/cyan accents, realistic web UI, "
                "high resolution, no text, no logos, no watermark"
            ),
        },
        {
            "name": "portfolio_android_health",
            "size": "landscape_16_9",
            "prompt": (
                "Mobile healthcare app UI on smartphone, vitals dashboard, appointment schedule, "
                "clean modern design, brand blue/cyan accents, realistic product mockup, "
                "high resolution, no text, no logos, no watermark"
            ),
        },
        {
            "name": "portfolio_infrastructure_ai",
            "size": "landscape_16_9",
            "prompt": (
                "Infrastructure and AI platform dashboard, server health, pipelines, "
                "network topology visualization, brand blue/cyan accents, clean enterprise UI, "
                "realistic web app screenshot, high resolution, no text, no logos, no watermark"
            ),
        },
    ],
    "founders": [
        {
            "name": "founder_alicia",
            "size": "portrait_9_16",
            "prompt": (
                "Professional headshot of a woman in her 30s-40s, confident warm smile, "
                "business professional attire, natural soft lighting, neutral background, "
                "photorealistic, high quality, no text, no logos"
            ),
        },
        {
            "name": "founder_bri",
            "size": "portrait_9_16",
            "prompt": (
                "Professional headshot of an Indigenous woman with glasses, warm genuine smile, "
                "business casual blouse, natural window lighting, soft neutral background, "
                "photorealistic, high quality, no text, no logos"
            ),
        },
        {
            "name": "founder_jonathan",
            "size": "portrait_9_16",
            "prompt": (
                "Professional headshot of a man with short dark hair and neat beard, friendly smile, "
                "business casual button-up shirt, natural lighting, neutral background, "
                "photorealistic, high quality, no text, no logos"
            ),
        },
        {
            "name": "founder_lilly",
            "size": "portrait_9_16",
            "prompt": (
                "Professional headshot of a woman with long dark hair, confident warm expression, "
                "business professional blazer, soft neutral background, natural lighting, "
                "photorealistic, high quality, no text, no logos"
            ),
        },
    ],
}


def load_fal_key() -> str:
    key = os.getenv("FAL_API_KEY") or os.getenv("FAL_KEY")
    if key:
        return key

    try:
        result = subprocess.run(
            [
                "op",
                "read",
                "op://TrueNAS Infrastructure/FAL API Key/credential",
                "--force",
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        key = result.stdout.strip()
    except Exception:
        key = ""

    if not key:
        raise RuntimeError("FAL API key not found. Set FAL_API_KEY or unlock 1Password CLI.")

    os.environ["FAL_API_KEY"] = key
    return key


def call_fal_api(prompt: str, image_size: str, api_key: str) -> Optional[str]:
    url = f"https://fal.run/{MODEL}"
    headers = {
        "Authorization": f"Key {api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "prompt": prompt,
        "image_size": image_size,
        "num_inference_steps": 4,
        "num_images": 1,
        "enable_safety_checker": False,
    }
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=120)
        response.raise_for_status()
        result = response.json()
        images = result.get("images", [])
        if images:
            return images[0].get("url")
        return None
    except Exception as exc:
        print(f"API error: {exc}")
        if hasattr(exc, "response") and exc.response is not None:
            print(exc.response.text)
        return None


def download_to_webp(image_url: str, output_path: Path, quality: int = 90) -> bool:
    try:
        response = requests.get(image_url, timeout=120)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content))
        if img.mode in ("RGBA", "LA", "P"):
            background = Image.new("RGB", img.size, (255, 255, 255))
            if img.mode == "P":
                img = img.convert("RGBA")
            background.paste(img, mask=img.split()[-1] if img.mode in ("RGBA", "LA") else None)
            img = background
        output_path.parent.mkdir(parents=True, exist_ok=True)
        img.save(output_path, "WEBP", quality=quality, method=6)
        print(f"✓ Saved {output_path.name}")
        return True
    except Exception as exc:
        print(f"✗ Failed to save {output_path.name}: {exc}")
        return False


def generate_assets() -> None:
    api_key = load_fal_key()
    total = sum(len(items) for items in ASSETS.values())
    done = 0
    manifest = {"model": MODEL, "assets": {}}

    print("=" * 80)
    print("ISN.BIZ TARGETED ASSET GENERATION (NANO-BANANA-PRO)")
    print("=" * 80)

    for category, items in ASSETS.items():
        print(f"\n-- {category.upper()} ({len(items)} assets) --")
        manifest["assets"][category] = []
        for asset in items:
            done += 1
            name = asset["name"]
            size = asset["size"]
            prompt = asset["prompt"]
            print(f"[{done}/{total}] {name} ({size})")
            image_url = call_fal_api(prompt, size, api_key)
            output_path = BASE_DIR / category / f"{name}.webp"
            success = False
            if image_url:
                success = download_to_webp(image_url, output_path)
            manifest["assets"][category].append(
                {
                    "name": name,
                    "size": size,
                    "prompt": prompt,
                    "output": str(output_path),
                    "source_url": image_url,
                    "success": success,
                }
            )
            time.sleep(2)

    manifest_path = BASE_DIR / "isnbiz_asset_manifest.json"
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)
    print(f"\nManifest saved to {manifest_path}")


if __name__ == "__main__":
    generate_assets()
