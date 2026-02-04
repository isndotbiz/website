#!/usr/bin/env python3
"""
Founder Image Generator using fal.ai GPT Image 1.5 Edit
Generates portraits, casual scenes, and group scenes with identity preservation.
"""

import json
import os
import subprocess
import time
import requests
from datetime import datetime
from pathlib import Path

# Configuration
OUTPUT_DIR = Path("D:/workspace/ISNBIZ_Files/generated_founders")
MANIFEST_FILE = OUTPUT_DIR / "manifest.json"
API_ENDPOINT = "https://queue.fal.run/fal-ai/gpt-image-1.5/edit"

# Founders data
FOUNDERS = {
    "jonathan": {
        "name": "Jonathan",
        "role": "Chairman",
        "headshot": "https://isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com/assets/founders/headshots_with_bg/jonathan_headshot.webp"
    },
    "alicia": {
        "name": "Alicia",
        "role": "Co-founder",
        "headshot": "https://isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com/assets/founders/headshots_with_bg/alicia_headshot.webp"
    },
    "bri": {
        "name": "Bri",
        "role": "COO",
        "headshot": "https://isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com/assets/founders/headshots_with_bg/bri_headshot.webp",
        "needs_proportion_fix": True
    },
    "lilly": {
        "name": "Lilly",
        "role": "CFO",
        "headshot": "https://isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com/assets/founders/headshots_with_bg/lilly_headshot.webp",
        "needs_proportion_fix": True
    }
}

# Prompt templates
PORTRAIT_TEMPLATE = """Preserve this person's exact facial features, skin tone, bone structure, eye color, expression, and identity with 100% accuracy. Do not alter their face, hairstyle, or any identifying characteristics.
Professional executive portrait in modern office environment. Subject has natural, relaxed posture - NOT looking directly at camera, natural 3/4 profile gaze toward something off-frame. Confident, approachable expression.
Soft studio lighting with subtle window light, shallow depth of field, natural skin texture with visible pores, subtle film grain, 85mm portrait lens aesthetic, neutral warm tones.
Negative: (((long neck))), ((bad proportions)), plastic skin, airbrushed, perfect skin, looking at camera, direct eye contact, posed, stiff, deformed, cartoonish, watermark"""

CASUAL_TEMPLATE = """This is {name}. Preserve their exact facial features, identity, skin tone, and all distinguishing characteristics with absolute fidelity. Face must remain 100% unchanged.
{name} in a bright, modern co-working space wearing smart casual attire (fitted sweater/blazer). Engaged in {activity}, natural mid-action moment. NOT looking at camera - focused on their work or colleague off-frame.
Natural daylight from large windows, documentary photography style, authentic candid moment, realistic skin texture, 35mm lens perspective, warm contemporary interior.
Negative: (((long neck))), bad anatomy, plastic skin, posed, looking at camera, stiff posture, airbrushed, deformed hands, extra fingers"""

GROUP_TEMPLATE = """This image features four business executives in a collaborative moment. Each person's exact facial features, identity, and distinguishing characteristics must be preserved with 100% accuracy.
The four founders gathered around a modern conference table during a strategy session: Jonathan (man, chairman), Alicia (woman, long dark hair), Bri (woman, COO), Lilly (woman, CFO). Natural interaction - people interacting with each other, not camera. Documentary business photography style, candid moment captured.
Negative: (((long necks))), bad proportions, cloned faces, looking at camera, posed group photo, plastic skin, stiff postures, deformed hands, fused faces"""

PROPORTION_FIX_TEMPLATE = """EDIT ONLY THE MASKED AREA. Do not change the face, facial features, hair, or expression in any way.
Adjust neck to natural human proportions - anatomically correct shorter length. Shoulders properly proportioned relative to head. Seamless blending with unmasked areas, matching skin tone, lighting, and texture exactly.
Negative: long neck, giraffe neck, bad anatomy, visible seams, mismatched lighting, changed face"""

# Casual activities for variety
CASUAL_ACTIVITIES = [
    "reviewing a presentation on a laptop",
    "discussing ideas with a colleague",
    "writing notes on a whiteboard"
]

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

def submit_generation(fal_key: str, prompt: str, image_urls: list, num_images: int = 3) -> dict:
    """Submit image generation request to fal.ai queue"""
    headers = {
        "Authorization": f"Key {fal_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "prompt": prompt,
        "image_urls": image_urls,
        "input_fidelity": "high",  # Critical for identity preservation
        "quality": "low",  # Cost guardrail
        "image_size": "1024x1024",
        "output_format": "webp",
        "num_images": num_images
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

        time.sleep(2)

    raise TimeoutError(f"Request {request_id} did not complete within {max_wait}s")

def download_image(url: str, output_path: Path) -> bool:
    """Download image from URL"""
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_bytes(response.content)
        return True
    except Exception as e:
        print(f"  ERROR downloading {url}: {e}")
        return False

def qc_check(image_path: Path, category: str) -> dict:
    """Basic QC check - returns pass/fail with notes"""
    # In production, this would use image analysis
    # For now, record as pending manual review
    return {
        "path": str(image_path),
        "category": category,
        "status": "pending_review",
        "checks": {
            "identity_match": "pending",
            "proportions": "pending",
            "lighting": "pending",
            "realism": "pending",
            "not_looking_at_camera": "pending",
            "no_artifacts": "pending"
        }
    }

def generate_portraits(fal_key: str, manifest: dict):
    """Generate 3 portrait variations per founder"""
    print("\n=== Phase 2: Generating Portraits ===")

    for founder_id, founder in FOUNDERS.items():
        print(f"\nGenerating portraits for {founder['name']}...")

        prompt = PORTRAIT_TEMPLATE
        image_urls = [founder["headshot"]]

        try:
            # Submit request
            queue_resp = submit_generation(fal_key, prompt, image_urls, num_images=3)
            request_id = queue_resp["request_id"]
            print(f"  Submitted: {request_id}")

            # Wait for completion
            result = poll_for_completion(fal_key, request_id)

            # Download images
            for i, img_data in enumerate(result.get("images", [])):
                output_path = OUTPUT_DIR / "portraits" / f"{founder_id}_portrait_{i+1}.webp"
                if download_image(img_data["url"], output_path):
                    print(f"  Downloaded: {output_path.name}")

                    manifest["images"].append({
                        "type": "portrait",
                        "founder": founder_id,
                        "variant": i + 1,
                        "source_url": founder["headshot"],
                        "output_url": img_data["url"],
                        "local_path": str(output_path),
                        "prompt": prompt[:200] + "...",
                        "qc": qc_check(output_path, "portrait")
                    })

            manifest["stats"]["portraits_generated"] += len(result.get("images", []))

        except Exception as e:
            print(f"  ERROR: {e}")
            manifest["errors"].append({
                "phase": "portrait",
                "founder": founder_id,
                "error": str(e)
            })

def generate_casual_scenes(fal_key: str, manifest: dict):
    """Generate 3 casual scene variations per founder"""
    print("\n=== Phase 3: Generating Casual Scenes ===")

    for founder_id, founder in FOUNDERS.items():
        print(f"\nGenerating casual scenes for {founder['name']}...")

        for i, activity in enumerate(CASUAL_ACTIVITIES):
            prompt = CASUAL_TEMPLATE.format(name=founder["name"], activity=activity)
            image_urls = [founder["headshot"]]

            try:
                queue_resp = submit_generation(fal_key, prompt, image_urls, num_images=1)
                request_id = queue_resp["request_id"]
                print(f"  Submitted scene {i+1}: {request_id}")

                result = poll_for_completion(fal_key, request_id)

                for j, img_data in enumerate(result.get("images", [])):
                    output_path = OUTPUT_DIR / "casual" / f"{founder_id}_casual_{i+1}.webp"
                    if download_image(img_data["url"], output_path):
                        print(f"  Downloaded: {output_path.name}")

                        manifest["images"].append({
                            "type": "casual",
                            "founder": founder_id,
                            "variant": i + 1,
                            "activity": activity,
                            "source_url": founder["headshot"],
                            "output_url": img_data["url"],
                            "local_path": str(output_path),
                            "prompt": prompt[:200] + "...",
                            "qc": qc_check(output_path, "casual")
                        })

                manifest["stats"]["casual_generated"] += len(result.get("images", []))

            except Exception as e:
                print(f"  ERROR scene {i+1}: {e}")
                manifest["errors"].append({
                    "phase": "casual",
                    "founder": founder_id,
                    "scene": i + 1,
                    "error": str(e)
                })

def generate_group_scenes(fal_key: str, manifest: dict):
    """Generate 3 group scene variations"""
    print("\n=== Phase 4: Generating Group Scenes ===")

    # Use all four headshots as reference
    all_headshots = [f["headshot"] for f in FOUNDERS.values()]

    for i in range(3):
        print(f"\nGenerating group scene {i+1}/3...")

        try:
            queue_resp = submit_generation(fal_key, GROUP_TEMPLATE, all_headshots, num_images=1)
            request_id = queue_resp["request_id"]
            print(f"  Submitted: {request_id}")

            result = poll_for_completion(fal_key, request_id)

            for j, img_data in enumerate(result.get("images", [])):
                output_path = OUTPUT_DIR / "group" / f"founders_group_{i+1}.webp"
                if download_image(img_data["url"], output_path):
                    print(f"  Downloaded: {output_path.name}")

                    manifest["images"].append({
                        "type": "group",
                        "variant": i + 1,
                        "source_urls": all_headshots,
                        "output_url": img_data["url"],
                        "local_path": str(output_path),
                        "prompt": GROUP_TEMPLATE[:200] + "...",
                        "qc": qc_check(output_path, "group")
                    })

            manifest["stats"]["group_generated"] += len(result.get("images", []))

        except Exception as e:
            print(f"  ERROR: {e}")
            manifest["errors"].append({
                "phase": "group",
                "scene": i + 1,
                "error": str(e)
            })

def generate_proportion_fixes(fal_key: str, manifest: dict):
    """Generate proportion fixes for Lilly and Bri"""
    print("\n=== Phase 1: Proportion Fixes (Lilly, Bri) ===")
    print("Note: GPT Image 1.5 Edit uses prompt-based editing without explicit masks")

    for founder_id in ["lilly", "bri"]:
        founder = FOUNDERS[founder_id]
        print(f"\nGenerating proportion fixes for {founder['name']}...")

        try:
            queue_resp = submit_generation(fal_key, PROPORTION_FIX_TEMPLATE,
                                          [founder["headshot"]], num_images=3)
            request_id = queue_resp["request_id"]
            print(f"  Submitted: {request_id}")

            result = poll_for_completion(fal_key, request_id)

            for i, img_data in enumerate(result.get("images", [])):
                output_path = OUTPUT_DIR / "proportion_fixes" / f"{founder_id}_fixed_{i+1}.webp"
                if download_image(img_data["url"], output_path):
                    print(f"  Downloaded: {output_path.name}")

                    manifest["images"].append({
                        "type": "proportion_fix",
                        "founder": founder_id,
                        "variant": i + 1,
                        "source_url": founder["headshot"],
                        "output_url": img_data["url"],
                        "local_path": str(output_path),
                        "prompt": PROPORTION_FIX_TEMPLATE[:200] + "...",
                        "qc": qc_check(output_path, "proportion_fix")
                    })

            manifest["stats"]["proportion_fixes_generated"] += len(result.get("images", []))

        except Exception as e:
            print(f"  ERROR: {e}")
            manifest["errors"].append({
                "phase": "proportion_fix",
                "founder": founder_id,
                "error": str(e)
            })

def main():
    print("=" * 60)
    print("FOUNDER IMAGE GENERATION - GPT Image 1.5 Edit via fal.ai")
    print("=" * 60)

    # Initialize manifest
    manifest = {
        "generated_at": datetime.now().isoformat(),
        "api_settings": {
            "endpoint": API_ENDPOINT,
            "input_fidelity": "high",
            "quality": "low",
            "image_size": "1024x1024",
            "output_format": "webp"
        },
        "founders": FOUNDERS,
        "stats": {
            "proportion_fixes_generated": 0,
            "portraits_generated": 0,
            "casual_generated": 0,
            "group_generated": 0,
            "total_images": 0,
            "errors": 0
        },
        "images": [],
        "errors": []
    }

    # Get API key
    print("\nLoading FAL API key from 1Password...")
    fal_key = get_fal_key()
    print("  Key loaded successfully")

    # Create output directories
    for subdir in ["proportion_fixes", "portraits", "casual", "group"]:
        (OUTPUT_DIR / subdir).mkdir(parents=True, exist_ok=True)

    # Run generation phases
    generate_proportion_fixes(fal_key, manifest)
    generate_portraits(fal_key, manifest)
    generate_casual_scenes(fal_key, manifest)
    generate_group_scenes(fal_key, manifest)

    # Update final stats
    manifest["stats"]["total_images"] = (
        manifest["stats"]["proportion_fixes_generated"] +
        manifest["stats"]["portraits_generated"] +
        manifest["stats"]["casual_generated"] +
        manifest["stats"]["group_generated"]
    )
    manifest["stats"]["errors"] = len(manifest["errors"])

    # Save manifest
    with open(MANIFEST_FILE, "w") as f:
        json.dump(manifest, f, indent=2)
    print(f"\n\nManifest saved to: {MANIFEST_FILE}")

    # Summary
    print("\n" + "=" * 60)
    print("GENERATION COMPLETE")
    print("=" * 60)
    print(f"Proportion fixes: {manifest['stats']['proportion_fixes_generated']}")
    print(f"Portraits: {manifest['stats']['portraits_generated']}")
    print(f"Casual scenes: {manifest['stats']['casual_generated']}")
    print(f"Group scenes: {manifest['stats']['group_generated']}")
    print(f"Total images: {manifest['stats']['total_images']}")
    print(f"Errors: {manifest['stats']['errors']}")

    if manifest["errors"]:
        print("\nErrors encountered:")
        for err in manifest["errors"]:
            print(f"  - {err}")

    return manifest

if __name__ == "__main__":
    main()
