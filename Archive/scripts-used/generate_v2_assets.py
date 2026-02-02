#!/usr/bin/env python3
"""
ISN.BIZ V2 Asset Generation Pipeline
=====================================
Generates ALL new images for the ISN.BIZ website redesign using fal.ai GPT-Image-1.5.

Usage:
    # Activate venv first
    source venv_fal/bin/activate   # Linux/Mac
    venv_fal\\Scripts\\activate     # Windows

    # Run full pipeline (generate + convert + upload)
    python generate_v2_assets.py

    # Generate only (no S3 upload)
    python generate_v2_assets.py --no-upload

    # Resume from where you left off (skips existing files)
    python generate_v2_assets.py --resume

    # Generate a single category
    python generate_v2_assets.py --category logos

    # Dry run (print tasks without generating)
    python generate_v2_assets.py --dry-run
"""

import os
import sys
import json
import subprocess
import time
import base64
import io
import argparse
import traceback
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

OUTPUT_DIR = Path("/home/jdmal/workspace/ISNBIZ_Files/assets/premium_v2")
HEADSHOT_DIR = Path("/home/jdmal/workspace/ISNBIZ_Files/1")
S3_BUCKET = "isnbiz-assets-1769962280"
S3_PREFIX = "premium_v2"
S3_REGION = "us-west-2"

CREATE_MODEL = "fal-ai/gpt-image-1.5"
EDIT_MODEL = "fal-ai/gpt-image-1.5/edit"

# Pricing estimates (USD per image, low quality)
PRICE_1024x1024_LOW = 0.009
PRICE_OTHER_LOW = 0.013

# GPT-Image-1.5 only supports these native sizes.
# We generate at the closest native size then resize with Pillow.
NATIVE_SIZES = {
    "1024x1024": "1024x1024",
    "1536x1024": "1536x1024",
    "1024x1536": "1024x1536",
}

# Map desired output dimensions -> best native generation size
def best_native_size(width: int, height: int) -> str:
    """Pick the native API size closest to the desired aspect ratio."""
    ratio = width / height
    if ratio > 1.2:
        return "1536x1024"   # landscape
    elif ratio < 0.8:
        return "1024x1536"   # portrait
    else:
        return "1024x1024"   # square-ish


# ---------------------------------------------------------------------------
# Task definitions
# ---------------------------------------------------------------------------

@dataclass
class AssetTask:
    """One image generation task."""
    task_id: str           # e.g. "1.1_primary_logo"
    category: str          # e.g. "logos", "heroes", "sections", etc.
    filename: str          # output filename without extension
    prompt: str
    width: int
    height: int
    mode: str = "create"   # "create" or "edit"
    input_image: Optional[str] = None   # path for edit mode
    input_fidelity: Optional[str] = None
    quality: str = "low"
    output_format: str = "png"


def build_all_tasks() -> List[AssetTask]:
    """Build the complete list of generation tasks."""
    tasks: List[AssetTask] = []

    # ===================================================================
    # 1. LOGO SUITE (4 images)
    # ===================================================================
    tasks.append(AssetTask(
        task_id="1.1",
        category="logos",
        filename="primary_logo",
        width=2000, height=2000,
        prompt='Background/scene: Solid light background, neutral. Subject: New original logo for the company name "I S N . B I Z" (spell with spaces), with a geometric icon to the left and a clean wordmark to the right. Details: The icon should be abstract and tech-forward, using simple shapes, strong silhouette, and balanced negative space. Wordmark in modern sans-serif, uppercase, crisp kerning. Constraints: Flat design, minimal strokes, no gradients unless essential, centered composition, generous padding, no watermark, non-infringing. Intended use: Primary brand logo for a technology company website.',
    ))
    tasks.append(AssetTask(
        task_id="1.2",
        category="logos",
        filename="horizontal_wordmark",
        width=2600, height=800,
        prompt='Background/scene: Solid white background. Subject: Wordmark only for "I S N . B I Z" (spell with spaces), clean modern sans-serif. Details: Balanced spacing, crisp letterforms, high legibility at small sizes. Constraints: Flat design, no icon, no extra symbols, no watermark, centered. Intended use: Header logo for website navigation.',
    ))
    tasks.append(AssetTask(
        task_id="1.3",
        category="logos",
        filename="square_icon",
        width=2000, height=2000,
        prompt='Background/scene: Solid background. Subject: Abstract monogram icon based on letters "I S N" simplified into a geometric mark. Details: Bold, balanced negative space, strong silhouette, recognizable at 32px. Constraints: No text beyond the monogram, flat design, centered, no watermark. Intended use: App icon, favicon, social avatar.',
    ))
    tasks.append(AssetTask(
        task_id="1.4",
        category="logos",
        filename="favicon",
        width=2000, height=2000,
        prompt='Background/scene: Solid background. Subject: Minimalist geometric mark that feels like a tech compass or node cluster, no letters. Details: Ultra-simple shape, strong contrast, usable at 16px. Constraints: Flat design, no gradients, no watermark. Intended use: Favicon for browser tabs.',
    ))

    # ===================================================================
    # 2. HERO BACKGROUNDS (2 images, 1920x1080)
    # ===================================================================
    tasks.append(AssetTask(
        task_id="2.1",
        category="heroes",
        filename="hero_home",
        width=1920, height=1080,
        prompt='Background/scene: Dark charcoal tech environment with subtle depth-of-field, soft volumetric light. Subject: Abstract data streams and luminous nodes forming a gentle arc across the frame. Details: Blue/cyan accents (#1E9FF2, #5FDFDF), subtle grid and glassy reflections, premium enterprise feel. Constraints: No text, no logos, no people, no watermark. Leave negative space on left for headline. Intended use: Website hero background (16:9) for a technology company.',
    ))
    tasks.append(AssetTask(
        task_id="2.2",
        category="heroes",
        filename="hero_interior",
        width=1920, height=1080,
        prompt='Background/scene: Minimalist high-tech interior with glass panels and soft ambient light. Subject: Abstract light trails and faint circuitry patterns across a wide frame. Details: Cool blue/cyan highlights on charcoal, clean and cinematic. Constraints: No text, no logos, no people, no watermark. Leave negative space on right for headline. Intended use: Secondary hero background (16:9).',
    ))

    # ===================================================================
    # 3. SECTION BACKGROUNDS (2 images, 1920x1080)
    # ===================================================================
    tasks.append(AssetTask(
        task_id="3.1",
        category="sections",
        filename="investor_backdrop",
        width=1920, height=1080,
        prompt='Background/scene: Dark, refined financial-tech backdrop with subtle line graph silhouettes. Subject: Soft glowing lines and minimal geometric overlays. Details: Blue/cyan accents, restrained contrast, calm premium mood. Constraints: No readable chart numbers, no text, no logos, no watermark. Intended use: Investor page background banner (16:9).',
    ))
    tasks.append(AssetTask(
        task_id="3.2",
        category="sections",
        filename="cta_energy_burst",
        width=1920, height=1080,
        prompt='Background/scene: Abstract energy wave across a dark field. Subject: Flowing cyan/blue light ribbons with gentle particle glow. Details: Clean gradients, subtle motion feel, corporate premium. Constraints: No text, no logos, no watermark. Leave center negative space. Intended use: Call-to-action section background (16:9).',
    ))

    # ===================================================================
    # 4. SERVICES VISUALS (3 images, 1600x900)
    # ===================================================================
    tasks.append(AssetTask(
        task_id="4.1",
        category="services",
        filename="ai_research",
        width=1600, height=900,
        prompt='Background/scene: Clean enterprise dashboard environment on a dark canvas. Subject: Abstract AI research interface with cards, graphs, and network nodes (no readable text). Details: Blue/cyan highlights, soft shadows, realistic UI depth, glassy panels. Constraints: No readable text, no logos, no watermark. Intended use: Services section visual (16:9).',
    ))
    tasks.append(AssetTask(
        task_id="4.2",
        category="services",
        filename="enterprise_automation",
        width=1600, height=900,
        prompt='Background/scene: Modern ops dashboard with workflow lanes and status indicators. Subject: Automation timeline view with connected nodes and status badges (abstract labels only). Details: Subtle glow, blue/cyan accents, clean corporate UI. Constraints: No readable text, no logos, no watermark. Intended use: Services section visual (16:9).',
    ))
    tasks.append(AssetTask(
        task_id="4.3",
        category="services",
        filename="rag_and_search",
        width=1600, height=900,
        prompt='Background/scene: Knowledge graph interface over dark background. Subject: Search bar, node-link visualization, and analytics cards (abstract placeholders only). Details: Crisp UI, luminous nodes, blue/cyan accent lighting. Constraints: No readable text, no logos, no watermark. Intended use: Services section visual (16:9).',
    ))

    # ===================================================================
    # 5. PORTFOLIO VISUALS (6 images, 1600x900)
    # ===================================================================
    tasks.append(AssetTask(
        task_id="5.1",
        category="portfolio",
        filename="opportunity_bot",
        width=1600, height=900,
        prompt='Background/scene: Enterprise analytics dashboard on dark UI. Subject: Opportunity ranking list, scoring cards, and trend chart (abstract placeholders only). Details: Visuals suggest FICO-based personalization and automation intelligence. Blue/cyan accents. Constraints: No readable text, no logos, no watermark. Intended use: Portfolio project mockup (16:9).',
    ))
    tasks.append(AssetTask(
        task_id="5.2",
        category="portfolio",
        filename="credit_automation",
        width=1600, height=900,
        prompt='Background/scene: Fintech compliance dashboard. Subject: Automated report pipeline view, risk flags, and compliance checklist cards (abstract labels). Details: Clean corporate UI, subtle red/amber flags for contrast, but primarily brand blue/cyan. Constraints: No readable text, no logos, no watermark. Intended use: Portfolio project mockup (16:9).',
    ))
    tasks.append(AssetTask(
        task_id="5.3",
        category="portfolio",
        filename="hroc_website",
        width=1600, height=900,
        prompt='Background/scene: Bright, welcoming nonprofit website mockup on a laptop screen. Subject: Hero section with community imagery blocks, donation call-to-action area (no readable text). Details: Warm, inclusive feel with subtle blue/cyan accents; modern, responsive layout. Constraints: No readable text, no logos, no watermark. Intended use: Portfolio project mockup (16:9).',
    ))
    tasks.append(AssetTask(
        task_id="5.4",
        category="portfolio",
        filename="rag_bi",
        width=1600, height=900,
        prompt='Background/scene: High-end analytics platform dashboard. Subject: Search bar, knowledge graph, vector embeddings panel, KPI cards (abstract placeholders only). Details: Data-dense but clean; subtle glow and depth. Constraints: No readable text, no logos, no watermark. Intended use: Portfolio project mockup (16:9).',
    ))
    tasks.append(AssetTask(
        task_id="5.5",
        category="portfolio",
        filename="androidaps_health",
        width=1600, height=900,
        prompt='Background/scene: Photorealistic smartphone on desk, medical UI on screen. Subject: Vitals dashboard and appointments UI (abstract placeholders only). Details: Natural lighting, soft shadows, clean modern healthcare design, brand blue/cyan accents. Constraints: No readable text, no logos, no watermark. Intended use: Portfolio project mockup (16:9).',
    ))
    tasks.append(AssetTask(
        task_id="5.6",
        category="portfolio",
        filename="infrastructure",
        width=1600, height=900,
        prompt='Background/scene: Infrastructure monitoring UI with network topology. Subject: Server health cards, pipeline status, and node map (abstract placeholders only). Details: Dark UI, blue/cyan highlights, professional enterprise feel. Constraints: No readable text, no logos, no watermark. Intended use: Portfolio project mockup (16:9).',
    ))

    # ===================================================================
    # 6. GALLERY SLIDES (5 images, 1920x1080)
    # ===================================================================
    tasks.append(AssetTask(
        task_id="6.1",
        category="gallery",
        filename="slide_data_horizon",
        width=1920, height=1080,
        prompt='Background/scene: Abstract data horizon with glowing nodes and faint grid. Subject: Gentle arc of light forming a pathway across the frame. Details: Blue/cyan accents on charcoal, cinematic depth. Constraints: No text, no logos, no watermark. Intended use: Slider background (16:9).',
    ))
    tasks.append(AssetTask(
        task_id="6.2",
        category="gallery",
        filename="slide_circuit_macro",
        width=1920, height=1080,
        prompt='Background/scene: Minimalist circuit-board macro texture. Subject: Thin luminous traces and metallic surfaces. Details: Subtle cyan glow, shallow depth-of-field, realistic materials. Constraints: No text, no logos, no watermark. Intended use: Slider background (16:9).',
    ))
    tasks.append(AssetTask(
        task_id="6.3",
        category="gallery",
        filename="slide_glass_panels",
        width=1920, height=1080,
        prompt='Background/scene: Dark abstract geometry with layered glass panels. Subject: Floating translucent shapes with soft reflections. Details: Blue/cyan accents, premium corporate tone. Constraints: No text, no logos, no watermark. Intended use: Slider background (16:9).',
    ))
    tasks.append(AssetTask(
        task_id="6.4",
        category="gallery",
        filename="slide_city_network",
        width=1920, height=1080,
        prompt='Background/scene: Night city tech skyline in soft focus. Subject: Light trails forming a network web across the horizon. Details: Subtle cyan highlights, moody but clean. Constraints: No text, no logos, no watermark. Intended use: Slider background (16:9).',
    ))
    tasks.append(AssetTask(
        task_id="6.5",
        category="gallery",
        filename="slide_energy_bloom",
        width=1920, height=1080,
        prompt='Background/scene: Abstract gradient fog with soft particulate glow. Subject: Blue/cyan energy bloom in the center. Details: Minimal, airy, premium. Constraints: No text, no logos, no watermark. Intended use: Slider background (16:9).',
    ))

    # ===================================================================
    # 7. FOUNDER HEADSHOTS (4 edits, 1200x1200)
    # ===================================================================
    tasks.append(AssetTask(
        task_id="7.1",
        category="headshots",
        filename="jonathan",
        width=1200, height=1200,
        mode="edit",
        input_image=str(HEADSHOT_DIR / "j1.png"),
        input_fidelity="high",
        prompt='Background/scene: Replace background with soft neutral studio-like gradient (light gray), natural window lighting. Subject: Same person, same pose, same expression, same haircut and facial hair. Details: Subtle color correction, balanced contrast, natural skin texture. Clothing remains consistent. Constraints: Preserve identity and framing exactly. Change only lighting and background. No text or logos. Intended use: Founder headshot for company website.',
    ))
    tasks.append(AssetTask(
        task_id="7.2",
        category="headshots",
        filename="alicia",
        width=1200, height=1200,
        mode="edit",
        input_image=str(HEADSHOT_DIR / "a1.png"),
        input_fidelity="high",
        prompt='Background/scene: Soft warm-neutral background, gentle daylight. Subject: Same person, same pose, same expression, same hairstyle. Details: Natural skin texture, light color correction, professional polish. Constraints: Preserve identity and framing exactly. Change only lighting and background. No text or logos. Intended use: Founder headshot for company website.',
    ))
    tasks.append(AssetTask(
        task_id="7.3",
        category="headshots",
        filename="lilly",
        width=1200, height=1200,
        mode="edit",
        input_image=str(HEADSHOT_DIR / "l1.png"),
        input_fidelity="high",
        prompt='Background/scene: Neutral light background with subtle gradient, soft diffuse lighting. Subject: Same person, same pose, same expression, same hair. Details: Balanced contrast, natural skin texture, clean but not over-retouched. Constraints: Preserve identity and framing exactly. Change only lighting and background. No text or logos. Intended use: Founder headshot for company website.',
    ))
    tasks.append(AssetTask(
        task_id="7.4",
        category="headshots",
        filename="bri",
        width=1200, height=1200,
        mode="edit",
        input_image=str(HEADSHOT_DIR / "b1.png"),
        input_fidelity="high",
        prompt='Background/scene: Soft neutral background, gentle daylight. Subject: Same person, same pose, same expression, same hair and glasses. Details: Natural skin texture, subtle color correction, professional polish. Constraints: Preserve identity and framing exactly. Change only lighting and background. No text or logos. Intended use: Founder headshot for company website.',
    ))

    return tasks


# ---------------------------------------------------------------------------
# Credential retrieval
# ---------------------------------------------------------------------------

def get_fal_api_key() -> str:
    """Retrieve fal.ai API key from 1Password CLI."""
    print("[SETUP] Retrieving fal.ai API key from 1Password...")
    try:
        result = subprocess.run(
            ["op", "read", "op://Research/FAL API Key/credential"],
            capture_output=True, text=True, timeout=30,
        )
        if result.returncode != 0:
            print(f"[ERROR] 1Password CLI failed (exit {result.returncode}): {result.stderr.strip()}")
            # Fall back to environment variable
            key = os.environ.get("FAL_KEY", "")
            if key:
                print("[SETUP] Using FAL_KEY from environment variable instead.")
                return key
            print("[ERROR] No FAL_KEY environment variable set either.")
            print("[HINT]  Run: eval $(op signin)  then retry, or set FAL_KEY manually.")
            sys.exit(1)
        key = result.stdout.strip()
        if not key:
            print("[ERROR] 1Password returned empty key.")
            sys.exit(1)
        print("[SETUP] API key retrieved successfully.")
        return key
    except FileNotFoundError:
        print("[ERROR] 1Password CLI (op) not found on PATH.")
        key = os.environ.get("FAL_KEY", "")
        if key:
            print("[SETUP] Using FAL_KEY from environment variable instead.")
            return key
        print("[ERROR] No FAL_KEY environment variable set either.")
        sys.exit(1)
    except subprocess.TimeoutExpired:
        print("[ERROR] 1Password CLI timed out. You may need to: eval $(op signin)")
        sys.exit(1)


def get_aws_credentials() -> Dict[str, str]:
    """Retrieve AWS credentials from 1Password CLI for S3 upload."""
    print("[SETUP] Retrieving AWS credentials from 1Password...")
    creds = {}
    try:
        for field_name, env_key in [
            ("access key id", "AWS_ACCESS_KEY_ID"),
            ("secret access key", "AWS_SECRET_ACCESS_KEY"),
        ]:
            result = subprocess.run(
                ["op", "read", f"op://Research/AWS ISN.BIZ S3/{field_name}"],
                capture_output=True, text=True, timeout=30,
            )
            if result.returncode != 0:
                # Try alternate vault/item names
                result = subprocess.run(
                    ["op", "read", f"op://TrueNAS Infrastructure/AWS S3 ISN.BIZ/{field_name}"],
                    capture_output=True, text=True, timeout=30,
                )
            if result.returncode == 0 and result.stdout.strip():
                creds[env_key] = result.stdout.strip()

        # Fall back to environment
        if "AWS_ACCESS_KEY_ID" not in creds:
            if os.environ.get("AWS_ACCESS_KEY_ID"):
                creds["AWS_ACCESS_KEY_ID"] = os.environ["AWS_ACCESS_KEY_ID"]
                creds["AWS_SECRET_ACCESS_KEY"] = os.environ.get("AWS_SECRET_ACCESS_KEY", "")
                print("[SETUP] Using AWS credentials from environment variables.")
            else:
                print("[WARN]  Could not retrieve AWS credentials. S3 upload will be skipped.")
                return {}

        print("[SETUP] AWS credentials retrieved successfully.")
        return creds
    except Exception as e:
        print(f"[WARN]  Could not retrieve AWS credentials: {e}")
        print("[WARN]  S3 upload will be skipped. Set AWS_ACCESS_KEY_ID / AWS_SECRET_ACCESS_KEY manually.")
        return {}


# ---------------------------------------------------------------------------
# Image generation
# ---------------------------------------------------------------------------

def generate_create_image(task: AssetTask) -> Dict[str, Any]:
    """Generate an image using the text-to-image (create) endpoint."""
    import fal_client

    native_size = best_native_size(task.width, task.height)

    arguments = {
        "prompt": task.prompt,
        "image_size": native_size,
        "quality": task.quality,
        "num_images": 1,
        "output_format": task.output_format,
    }

    result = fal_client.subscribe(
        CREATE_MODEL,
        arguments=arguments,
        with_logs=False,
    )
    return result


def generate_edit_image(task: AssetTask) -> Dict[str, Any]:
    """Generate an image using the image-to-image (edit) endpoint."""
    import fal_client

    # Upload the input image to fal CDN first so the API can access it
    input_path = Path(task.input_image)
    if not input_path.exists():
        raise FileNotFoundError(f"Input image not found: {input_path}")

    print(f"         Uploading input image: {input_path.name} ...")
    image_url = fal_client.upload_file(input_path)
    print(f"         Uploaded to: {image_url[:80]}...")

    native_size = best_native_size(task.width, task.height)

    arguments = {
        "prompt": task.prompt,
        "image_urls": [image_url],
        "image_size": native_size,
        "quality": task.quality,
        "num_images": 1,
        "output_format": task.output_format,
    }
    if task.input_fidelity:
        arguments["input_fidelity"] = task.input_fidelity

    result = fal_client.subscribe(
        EDIT_MODEL,
        arguments=arguments,
        with_logs=False,
    )
    return result


def download_image(url: str) -> bytes:
    """Download image bytes from a URL."""
    import requests
    resp = requests.get(url, timeout=120)
    resp.raise_for_status()
    return resp.content


def resize_and_save(image_bytes: bytes, output_path: Path, target_w: int, target_h: int):
    """Resize image to target dimensions and save as PNG, then also save a WebP copy."""
    from PIL import Image as PILImage

    img = PILImage.open(io.BytesIO(image_bytes))

    # Resize if dimensions differ
    if img.width != target_w or img.height != target_h:
        img = img.resize((target_w, target_h), PILImage.LANCZOS)

    # Save PNG
    png_path = output_path.with_suffix(".png")
    img.save(str(png_path), "PNG")

    # Save WebP
    webp_path = output_path.with_suffix(".webp")
    # Convert RGBA to RGB for WebP if needed (WebP supports RGBA but smaller with RGB)
    if img.mode == "RGBA":
        # Keep RGBA for logos that might need transparency
        img.save(str(webp_path), "WEBP", quality=90, method=6)
    else:
        img.save(str(webp_path), "WEBP", quality=90, method=6)

    file_size_png = png_path.stat().st_size
    file_size_webp = webp_path.stat().st_size
    print(f"         Saved: {png_path.name} ({file_size_png:,} bytes)")
    print(f"         Saved: {webp_path.name} ({file_size_webp:,} bytes)")

    return {
        "png": str(png_path),
        "webp": str(webp_path),
        "width": target_w,
        "height": target_h,
        "png_size": file_size_png,
        "webp_size": file_size_webp,
    }


# ---------------------------------------------------------------------------
# S3 upload
# ---------------------------------------------------------------------------

def upload_to_s3(local_path: str, s3_key: str, content_type: str = "image/png") -> Optional[str]:
    """Upload a file to S3 and return the public URL."""
    try:
        import boto3
        s3 = boto3.client("s3", region_name=S3_REGION)
        s3.upload_file(
            local_path, S3_BUCKET, s3_key,
            ExtraArgs={"ContentType": content_type},
        )
        url = f"https://{S3_BUCKET}.s3.{S3_REGION}.amazonaws.com/{s3_key}"
        return url
    except Exception as e:
        print(f"         [S3 ERROR] {e}")
        return None


def upload_all_to_s3(manifest: Dict[str, Any]) -> Dict[str, Any]:
    """Upload all generated assets to S3."""
    print("\n" + "=" * 80)
    print("UPLOADING TO S3")
    print("=" * 80)

    uploaded = 0
    failed = 0

    for entry in manifest.get("assets", []):
        for fmt in ["png", "webp"]:
            local_path = entry.get(fmt)
            if not local_path or not Path(local_path).exists():
                continue

            ext = fmt
            ct = f"image/{fmt}"
            s3_key = f"{S3_PREFIX}/{entry['category']}/{entry['filename']}.{ext}"

            print(f"  Uploading {s3_key} ...")
            url = upload_to_s3(local_path, s3_key, ct)
            if url:
                entry[f"s3_url_{fmt}"] = url
                uploaded += 1
                print(f"    -> {url}")
            else:
                failed += 1

    print(f"\n  Uploaded: {uploaded}  |  Failed: {failed}")
    manifest["s3_uploaded"] = uploaded
    manifest["s3_failed"] = failed
    return manifest


# ---------------------------------------------------------------------------
# Cost estimation
# ---------------------------------------------------------------------------

def estimate_cost(tasks: List[AssetTask]) -> float:
    """Estimate total cost for all tasks at low quality."""
    total = 0.0
    for t in tasks:
        native = best_native_size(t.width, t.height)
        if native == "1024x1024":
            total += PRICE_1024x1024_LOW
        else:
            total += PRICE_OTHER_LOW
    return total


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------

def run_pipeline(
    tasks: List[AssetTask],
    resume: bool = False,
    do_upload: bool = True,
    dry_run: bool = False,
):
    """Execute the full generation pipeline."""
    total = len(tasks)
    est_cost = estimate_cost(tasks)

    print("=" * 80)
    print("ISN.BIZ V2 ASSET GENERATION PIPELINE")
    print("=" * 80)
    print(f"  Total tasks:      {total}")
    print(f"  Output directory:  {OUTPUT_DIR}")
    print(f"  Estimated cost:    ${est_cost:.3f} (low quality)")
    print(f"  Resume mode:       {'ON' if resume else 'OFF'}")
    print(f"  S3 upload:         {'ON' if do_upload else 'OFF'}")
    print(f"  Dry run:           {'YES' if dry_run else 'NO'}")
    print("=" * 80)

    if dry_run:
        print("\n[DRY RUN] Listing all tasks:\n")
        for i, t in enumerate(tasks, 1):
            native = best_native_size(t.width, t.height)
            price = PRICE_1024x1024_LOW if native == "1024x1024" else PRICE_OTHER_LOW
            print(f"  [{i:2d}/{total}] {t.task_id:5s} | {t.category:10s} | {t.filename:25s} | "
                  f"{t.width}x{t.height} -> {native} | {t.mode:6s} | ~${price:.3f}")
        print(f"\n  Total estimated cost: ${est_cost:.3f}")
        return

    # Ensure output directory exists
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Load existing manifest for resume
    manifest_path = OUTPUT_DIR / "manifest.json"
    manifest: Dict[str, Any] = {
        "generated_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "model_create": CREATE_MODEL,
        "model_edit": EDIT_MODEL,
        "quality": "low",
        "total_tasks": total,
        "estimated_cost_usd": est_cost,
        "assets": [],
    }

    completed_filenames = set()
    if resume and manifest_path.exists():
        try:
            with open(manifest_path, "r") as f:
                old_manifest = json.load(f)
            for entry in old_manifest.get("assets", []):
                if entry.get("status") == "success":
                    completed_filenames.add(entry["filename"])
                    manifest["assets"].append(entry)
            print(f"\n[RESUME] Found {len(completed_filenames)} previously completed assets.")
        except Exception as e:
            print(f"[RESUME] Could not load manifest: {e}. Starting fresh.")

    succeeded = len(completed_filenames)
    failed = 0
    skipped = 0
    cost_running = 0.0
    start_time = time.time()

    for idx, task in enumerate(tasks, 1):
        # Skip already completed in resume mode
        if task.filename in completed_filenames:
            skipped += 1
            print(f"\n[{idx:2d}/{total}] SKIP (already done): {task.task_id} {task.filename}")
            continue

        native = best_native_size(task.width, task.height)
        price = PRICE_1024x1024_LOW if native == "1024x1024" else PRICE_OTHER_LOW

        print(f"\n{'─' * 80}")
        print(f"[{idx:2d}/{total}] {task.task_id} | {task.category}/{task.filename}")
        print(f"         Mode: {task.mode} | Target: {task.width}x{task.height} | "
              f"Native: {native} | ~${price:.3f}")
        print(f"         Prompt: {task.prompt[:100]}...")

        # Create category subdirectory
        cat_dir = OUTPUT_DIR / task.category
        cat_dir.mkdir(parents=True, exist_ok=True)
        output_path = cat_dir / task.filename

        entry = {
            "task_id": task.task_id,
            "category": task.category,
            "filename": task.filename,
            "mode": task.mode,
            "width": task.width,
            "height": task.height,
            "native_size": native,
            "prompt": task.prompt,
            "estimated_cost_usd": price,
            "status": "pending",
        }

        # Attempt generation with one retry
        for attempt in range(1, 3):
            try:
                print(f"         Generating (attempt {attempt}/2)...")
                gen_start = time.time()

                if task.mode == "edit":
                    result = generate_edit_image(task)
                else:
                    result = generate_create_image(task)

                gen_elapsed = time.time() - gen_start
                print(f"         Generation took {gen_elapsed:.1f}s")

                # Extract image URL from result
                images = result.get("images", [])
                if not images:
                    raise ValueError(f"No images in API response: {json.dumps(result)[:200]}")

                image_url = images[0].get("url")
                if not image_url:
                    raise ValueError(f"No URL in image result: {json.dumps(images[0])[:200]}")

                print(f"         Downloading from: {image_url[:80]}...")
                image_bytes = download_image(image_url)
                print(f"         Downloaded {len(image_bytes):,} bytes")

                # Resize and save
                file_info = resize_and_save(image_bytes, output_path, task.width, task.height)
                entry.update(file_info)
                entry["status"] = "success"
                entry["generation_time_s"] = round(gen_elapsed, 1)
                entry["fal_image_url"] = image_url
                cost_running += price
                succeeded += 1
                break  # Success, no retry needed

            except Exception as e:
                print(f"         [ERROR] Attempt {attempt}: {e}")
                if attempt < 2:
                    print(f"         Retrying in 5 seconds...")
                    time.sleep(5)
                else:
                    entry["status"] = "failed"
                    entry["error"] = str(e)
                    entry["traceback"] = traceback.format_exc()
                    failed += 1
                    print(f"         FAILED after 2 attempts.")

        manifest["assets"].append(entry)

        # Save manifest after each task (for resume capability)
        manifest["succeeded"] = succeeded
        manifest["failed"] = failed
        manifest["skipped"] = skipped
        manifest["cost_running_usd"] = round(cost_running, 4)
        manifest["elapsed_s"] = round(time.time() - start_time, 1)
        with open(manifest_path, "w") as f:
            json.dump(manifest, f, indent=2)

        # Brief pause between requests to be respectful to the API
        time.sleep(1)

    # Final summary
    elapsed = time.time() - start_time
    manifest["total_elapsed_s"] = round(elapsed, 1)
    manifest["final_succeeded"] = succeeded
    manifest["final_failed"] = failed
    manifest["final_skipped"] = skipped
    manifest["final_cost_usd"] = round(cost_running, 4)

    print("\n" + "=" * 80)
    print("GENERATION COMPLETE")
    print("=" * 80)
    print(f"  Succeeded:  {succeeded}/{total}")
    print(f"  Failed:     {failed}/{total}")
    print(f"  Skipped:    {skipped}/{total}")
    print(f"  Est. cost:  ${cost_running:.4f}")
    print(f"  Elapsed:    {elapsed:.1f}s ({elapsed/60:.1f}m)")
    print(f"  Output:     {OUTPUT_DIR}")
    print("=" * 80)

    # S3 Upload
    if do_upload and succeeded > 0:
        aws_creds = get_aws_credentials()
        if aws_creds:
            os.environ.update(aws_creds)
            manifest = upload_all_to_s3(manifest)
        else:
            print("\n[SKIP] S3 upload skipped (no AWS credentials).")
            print("       To upload later, set AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY,")
            print("       then run: python generate_v2_assets.py --upload-only")

    # Write final manifest
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)
    print(f"\nManifest saved: {manifest_path}")

    # Print S3 URL summary if available
    s3_entries = [a for a in manifest["assets"] if a.get("s3_url_webp")]
    if s3_entries:
        print("\n" + "=" * 80)
        print("S3 URLs (WebP)")
        print("=" * 80)
        for a in s3_entries:
            print(f"  {a['category']:10s}/{a['filename']:25s} -> {a['s3_url_webp']}")


def upload_only():
    """Upload already-generated assets to S3 (no generation)."""
    manifest_path = OUTPUT_DIR / "manifest.json"
    if not manifest_path.exists():
        print("[ERROR] No manifest.json found. Generate assets first.")
        sys.exit(1)

    with open(manifest_path, "r") as f:
        manifest = json.load(f)

    aws_creds = get_aws_credentials()
    if not aws_creds:
        print("[ERROR] No AWS credentials available.")
        sys.exit(1)
    os.environ.update(aws_creds)

    manifest = upload_all_to_s3(manifest)

    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)
    print(f"\nManifest updated: {manifest_path}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="ISN.BIZ V2 Asset Generation Pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python generate_v2_assets.py                  # Full pipeline
  python generate_v2_assets.py --no-upload      # Generate only
  python generate_v2_assets.py --resume         # Resume interrupted run
  python generate_v2_assets.py --dry-run        # Preview tasks
  python generate_v2_assets.py --category logos  # Single category
  python generate_v2_assets.py --upload-only    # Upload existing assets
        """,
    )
    parser.add_argument("--no-upload", action="store_true",
                        help="Skip S3 upload after generation")
    parser.add_argument("--upload-only", action="store_true",
                        help="Only upload existing assets to S3 (no generation)")
    parser.add_argument("--resume", action="store_true",
                        help="Resume from previous run, skipping completed tasks")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print task list without generating anything")
    parser.add_argument("--category", type=str, default=None,
                        choices=["logos", "heroes", "sections", "services",
                                 "portfolio", "gallery", "headshots"],
                        help="Generate only a specific category")

    args = parser.parse_args()

    # Handle upload-only mode
    if args.upload_only:
        upload_only()
        return

    # Build tasks
    all_tasks = build_all_tasks()

    # Filter by category if specified
    if args.category:
        all_tasks = [t for t in all_tasks if t.category == args.category]
        if not all_tasks:
            print(f"[ERROR] No tasks found for category '{args.category}'.")
            sys.exit(1)

    # Dry run doesn't need credentials
    if args.dry_run:
        run_pipeline(all_tasks, dry_run=True)
        return

    # Get API key and set it
    fal_key = get_fal_api_key()
    os.environ["FAL_KEY"] = fal_key

    # Verify fal_client can import
    try:
        import fal_client  # noqa: F401
    except ImportError:
        print("[ERROR] fal_client not installed. Activate the venv first:")
        print("        source venv_fal/bin/activate")
        sys.exit(1)

    # Verify Pillow is available
    try:
        from PIL import Image as PILImage  # noqa: F401
    except ImportError:
        print("[ERROR] Pillow not installed. Install with: pip install Pillow")
        sys.exit(1)

    # Run the pipeline
    run_pipeline(
        all_tasks,
        resume=args.resume,
        do_upload=not args.no_upload,
        dry_run=False,
    )


if __name__ == "__main__":
    main()
