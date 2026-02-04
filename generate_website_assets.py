#!/usr/bin/env python3
"""
Website Asset Generator using fal.ai GPT Image 1.5
Uses advanced prompting techniques for high-quality, award-winning business imagery.
"""

import json
import os
import subprocess
import time
import requests
from datetime import datetime
from pathlib import Path

OUTPUT_DIR = Path("D:/workspace/ISNBIZ_Files/generated_founders/assets")
API_ENDPOINT = "https://queue.fal.run/fal-ai/gpt-image-1.5"  # Generation, not edit

# Advanced Prompting Techniques Applied:
# 1. Style Anchoring - Reference specific photographers/aesthetics
# 2. Technical Specifications - Camera, lens, lighting details
# 3. Compositional Guidance - Rule of thirds, leading lines, negative space
# 4. Mood/Atmosphere Descriptors - Emotional tone
# 5. Anti-AI Markers - Avoid typical AI artifacts
# 6. Structured Negatives - Specific exclusions

ASSET_PROMPTS = {
    # HERO BACKGROUNDS
    "hero_abstract_tech": {
        "prompt": """[STYLE: Award-winning corporate photography, Apple keynote aesthetic, clean minimalism]
[MOOD: Innovative, forward-thinking, premium technology]

Abstract visualization of artificial intelligence and data flow. Subtle blue (#1E9FF2) and cyan (#5FDFDF)
luminescent particles forming elegant neural network patterns against deep charcoal (#3F4447) gradient.
Organic flowing lines suggesting connectivity and intelligence. Bokeh light points at varying depths.

[TECHNICAL: Shot on Phase One IQ4, 80mm lens, f/2.8, studio lighting with subtle rim light]
[COMPOSITION: Asymmetric balance, negative space on left third for text overlay, depth layers]

Negative: text, logos, watermarks, cluttered, busy, dated technology imagery, circuit boards,
binary code, robotic faces, generic AI imagery, stock photo aesthetic, oversaturated""",
        "category": "hero",
        "variants": 3
    },

    "hero_skyline_dawn": {
        "prompt": """[STYLE: Architectural photography by Iwan Baan, golden hour majesty]
[MOOD: Ambitious, growth-oriented, metropolitan success]

Modern glass skyscraper district at dawn. Sun rising between towers creating dramatic god rays.
Reflective surfaces catching warm orange-gold light contrasting with cool blue shadows.
Low angle emphasizing height and aspiration. Morning mist adding atmospheric depth.

[TECHNICAL: Sony A7R V, 24mm tilt-shift, f/11, bracketed HDR merged naturally]
[COMPOSITION: Strong vertical leading lines, rule of thirds horizon, open sky for overlay]

Negative: people, cars, logos, dated architecture, industrial buildings, pollution,
overprocessed HDR, halos, chromatic aberration, lens flare artifacts""",
        "category": "hero",
        "variants": 2
    },

    # SECTION BACKGROUNDS
    "section_data_viz": {
        "prompt": """[STYLE: Information design aesthetic, Edward Tufte principles, Bloomberg terminal elegance]
[MOOD: Analytical precision, data-driven insight, professional intelligence]

Elegant 3D data visualization floating in dark space. Translucent holographic charts, graphs,
and flowing data streams in blue (#1E9FF2) and cyan (#5FDFDF) luminescence. Abstract representation
of business analytics - bar charts morphing into line graphs into scatter plots.
Subtle grid lines providing structure. Depth of field blur on distant elements.

[TECHNICAL: CGI render quality, subsurface scattering on translucent elements, volumetric lighting]
[COMPOSITION: Central focus with radial expansion, 60% dark space for content overlay]

Negative: specific numbers, readable text, pie charts, clipart style, flat design,
cartoon graphics, Excel screenshots, dated infographics, busy cluttered layout""",
        "category": "section",
        "variants": 2
    },

    "section_cloud_abstract": {
        "prompt": """[STYLE: Abstract art photography, Thomas Ruff influence, minimalist tech aesthetic]
[MOOD: Ethereal, scalable, infinite possibility]

Abstract cloudscape representing cloud computing infrastructure. Volumetric white and silver
cloud formations with subtle blue (#1E9FF2) internal luminescence. Suggestion of interconnected
nodes within cloud layers. Gradient from deep charcoal base to lighter atmospheric top.
Cinematic depth with layered cloud planes.

[TECHNICAL: Medium format aesthetic, controlled studio fog, backlit, f/5.6 shallow focus]
[COMPOSITION: Horizontal layers, bottom-heavy for text space above, subtle leading lines upward]

Negative: literal servers, data centers, cables, specific cloud provider logos, cartoon clouds,
fluffy white clouds, blue sky, weather photography, storm clouds, dark ominous mood""",
        "category": "section",
        "variants": 2
    },

    "section_ai_neural": {
        "prompt": """[STYLE: Scientific visualization, Nature journal cover aesthetic, cerebral elegance]
[MOOD: Intelligent, sophisticated, cutting-edge research]

Artistic interpretation of neural network architecture. Interconnected nodes with elegant
synaptic connections pulsing with cyan (#5FDFDF) energy. Organic yet structured layout
suggesting both biological and digital intelligence. Depth layers from macro to micro scale.
Warm accent highlights on active pathways against cool blue-charcoal background.

[TECHNICAL: Macro photography aesthetic with CGI precision, selective focus planes]
[COMPOSITION: Golden spiral flow, entry point upper left, expansion toward lower right]

Negative: human brain imagery, literal neurons, medical imagery, robotic faces,
terminator style AI, red glowing eyes, matrix code, generic neural network diagrams""",
        "category": "section",
        "variants": 2
    },

    # OFFICE/WORKSPACE SCENES
    "office_modern_meeting": {
        "prompt": """[STYLE: Architectural Digest interior photography, Herman Miller showroom quality]
[MOOD: Collaborative, innovative, premium workspace]

Empty modern conference room ready for a meeting. Floor-to-ceiling windows with city view
(blurred). Minimalist Scandinavian furniture - long oak table, ergonomic mesh chairs.
Warm afternoon light casting long shadows. Single plant adding organic touch.
Technology: slim display on wall (blank screen), subtle cable management.

[TECHNICAL: Leica Q3, 28mm, f/4, natural window light with fill, white balance 5500K]
[COMPOSITION: Two-point perspective, converging lines to window, negative space for overlay]

Negative: people, clutter, papers, coffee cups, brand logos, dated furniture,
fluorescent lighting, drop ceiling, cubicles, generic office, stock photo staging""",
        "category": "office",
        "variants": 2
    },

    "office_workspace_detail": {
        "prompt": """[STYLE: Product photography meets workspace lifestyle, Kinfolk magazine aesthetic]
[MOOD: Focused, creative, thoughtfully designed]

Close-up detail shot of premium workspace. Selective focus on: MacBook Pro (closed, logo subtle),
leather notebook, premium pen, ceramic coffee cup with latte art. Warm oak desk surface.
Morning light from left creating gentle shadows. Bokeh background suggesting creative studio.

[TECHNICAL: Sony 90mm macro, f/2.8, natural side light, white reflector fill]
[COMPOSITION: Diagonal arrangement, rule of thirds focus point, depth layering front to back]

Negative: messy desk, cables visible, brand logos prominent, artificial lighting,
cluttered background, dated technology, plastic materials, stock photo arrangement""",
        "category": "office",
        "variants": 2
    },

    # TECHNOLOGY ABSTRACT
    "tech_code_abstract": {
        "prompt": """[STYLE: Generative art, Casey Reas aesthetic, Processing/p5.js visualization]
[MOOD: Technical elegance, algorithmic beauty, developer sophistication]

Abstract visualization of code execution. Flowing lines of varying thickness representing
data streams and function calls. Blue (#1E9FF2) primary paths with cyan (#5FDFDF) branches.
Particle systems suggesting parallel processing. Dark charcoal (#3F4447) deep background.
Subtle noise texture adding organic quality to digital concept.

[TECHNICAL: High resolution vector-sharp edges, antialiased curves, subtle gradient fills]
[COMPOSITION: Flow from upper left to lower right, concentrated center with dispersing edges]

Negative: actual code text, terminal windows, matrix falling code, green on black,
hacker aesthetic, glitch effects, corrupted data visualization, busy cluttered patterns""",
        "category": "tech",
        "variants": 2
    },

    "tech_security_shield": {
        "prompt": """[STYLE: Premium iconography, SF Symbols quality, dimensional minimalism]
[MOOD: Protected, trustworthy, enterprise-grade security]

Abstract security visualization. Elegant translucent shield form with hexagonal pattern
suggesting blockchain/encryption. Subtle blue (#1E9FF2) inner glow. Floating in dark space
with faint particle field representing protected data. Clean geometric construction with
organic light behavior. Premium glass material aesthetic.

[TECHNICAL: 3D render, subsurface scattering, caustics, studio HDRI lighting]
[COMPOSITION: Centered hero object, ample negative space, slight upward camera angle]

Negative: padlock icons, key imagery, literal locks and chains, warning signs,
red danger colors, skull and crossbones, generic security clipart, flat icons""",
        "category": "tech",
        "variants": 2
    },

    # INVESTOR/GROWTH
    "growth_chart_abstract": {
        "prompt": """[STYLE: Financial Times infographic quality, data visualization art]
[MOOD: Upward trajectory, sustainable growth, investor confidence]

Abstract 3D representation of growth trajectory. Elegant ascending curve rendered as
luminescent ribbon in blue (#1E9FF2) against dark charcoal space. Subtle grid plane below
suggesting data foundation. Particle effects trailing the ascending line. Perspective from
below looking up at growth. Secondary cyan (#5FDFDF) accent lines showing supporting metrics.

[TECHNICAL: Cinema 4D render quality, global illumination, motion blur on particles]
[COMPOSITION: Strong diagonal from lower left to upper right, open space for metrics overlay]

Negative: literal dollar signs, money imagery, stock tickers, red/green trading colors,
downward trends, volatile zigzags, pie charts, dated infographic style, clipart""",
        "category": "investor",
        "variants": 2
    },

    # TEAM/COLLABORATION (without specific people)
    "collab_hands_abstract": {
        "prompt": """[STYLE: Editorial photography, Harvard Business Review cover aesthetic]
[MOOD: Partnership, unified vision, collective strength]

Abstract overhead view of diverse hands coming together over architectural blueprint/plans.
Selective focus on overlapping hands with blueprint soft. Warm skin tones contrasting with
blue (#1E9FF2) technical drawings. Wedding ring on one hand suggesting established professionals.
Natural daylight from above. Premium watch visible but not branded.

[TECHNICAL: Canon R5, 35mm, f/4, overhead rig, diffused natural light]
[COMPOSITION: Centered convergence point, radial hand arrangement, negative space in corners]

Negative: faces visible, identifiable individuals, branded items, casual clothing,
tattoos, jewelry focus, staged handshake, corporate cliche poses, stock photo feel""",
        "category": "collaboration",
        "variants": 2
    }
}


def get_fal_key():
    """Get FAL API key from 1Password"""
    result = subprocess.run(
        ["op", "item", "get", "FAL API Key", "--vault", "TrueNAS Infrastructure",
         "--reveal", "--fields", "credential"],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        raise RuntimeError(f"Failed to get FAL key: {result.stderr}")
    return result.stdout.strip()


def submit_generation(fal_key: str, prompt: str, num_images: int = 1) -> dict:
    """Submit image generation request to fal.ai queue"""
    headers = {
        "Authorization": f"Key {fal_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "prompt": prompt,
        "image_size": "1536x1024",  # Landscape format (permitted by API)
        "num_images": num_images,
        "output_format": "webp"
    }

    response = requests.post(API_ENDPOINT, headers=headers, json=payload, timeout=30)
    response.raise_for_status()
    return response.json()


def poll_for_completion(fal_key: str, request_id: str, max_wait: int = 300) -> dict:
    """Poll until request completes"""
    status_url = f"https://queue.fal.run/fal-ai/gpt-image-1.5/requests/{request_id}/status"
    result_url = f"https://queue.fal.run/fal-ai/gpt-image-1.5/requests/{request_id}"
    headers = {"Authorization": f"Key {fal_key}"}

    start_time = time.time()
    while time.time() - start_time < max_wait:
        status_resp = requests.get(status_url, headers=headers, timeout=10)
        status_data = status_resp.json()

        if status_data.get("status") == "COMPLETED":
            result_resp = requests.get(result_url, headers=headers, timeout=10)
            return result_resp.json()
        elif status_data.get("status") == "FAILED":
            raise RuntimeError(f"Generation failed: {status_data}")

        time.sleep(3)

    raise TimeoutError(f"Request {request_id} did not complete within {max_wait}s")


def download_image(url: str, output_path: Path) -> bool:
    """Download image from URL"""
    try:
        response = requests.get(url, timeout=60)
        response.raise_for_status()
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_bytes(response.content)
        return True
    except Exception as e:
        print(f"  ERROR downloading: {e}")
        return False


def main():
    print("=" * 60)
    print("WEBSITE ASSET GENERATION - Advanced Prompting")
    print("=" * 60)

    manifest = {
        "generated_at": datetime.now().isoformat(),
        "technique": "Advanced prompting with style anchoring, technical specs, compositional guidance",
        "assets": [],
        "stats": {"total": 0, "errors": 0}
    }

    print("\nLoading FAL API key...")
    fal_key = get_fal_key()
    print("  Key loaded")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    total_images = sum(p["variants"] for p in ASSET_PROMPTS.values())
    print(f"\nGenerating {total_images} images across {len(ASSET_PROMPTS)} asset types...\n")

    for asset_id, asset_config in ASSET_PROMPTS.items():
        print(f"Generating: {asset_id} ({asset_config['variants']} variants)...")

        category_dir = OUTPUT_DIR / asset_config["category"]
        category_dir.mkdir(parents=True, exist_ok=True)

        try:
            queue_resp = submit_generation(
                fal_key,
                asset_config["prompt"],
                num_images=asset_config["variants"]
            )
            request_id = queue_resp["request_id"]
            print(f"  Submitted: {request_id}")

            result = poll_for_completion(fal_key, request_id)

            for i, img_data in enumerate(result.get("images", [])):
                output_path = category_dir / f"{asset_id}_{i+1}.webp"
                if download_image(img_data["url"], output_path):
                    print(f"  Downloaded: {output_path.name}")
                    manifest["assets"].append({
                        "id": asset_id,
                        "category": asset_config["category"],
                        "variant": i + 1,
                        "local_path": str(output_path),
                        "remote_url": img_data["url"],
                        "prompt_excerpt": asset_config["prompt"][:150] + "..."
                    })
                    manifest["stats"]["total"] += 1

        except Exception as e:
            print(f"  ERROR: {e}")
            manifest["stats"]["errors"] += 1

    # Save manifest
    manifest_path = OUTPUT_DIR / "assets_manifest.json"
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)

    print("\n" + "=" * 60)
    print("GENERATION COMPLETE")
    print("=" * 60)
    print(f"Total assets: {manifest['stats']['total']}")
    print(f"Errors: {manifest['stats']['errors']}")
    print(f"Manifest: {manifest_path}")

    return manifest


if __name__ == "__main__":
    main()
