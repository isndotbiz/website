#!/usr/bin/env python3
"""
Community & Lifestyle Scene Generator
Founders in casual settings: yoga, coffee shop, gym, outreach
"""

import json
import subprocess
import time
import requests
from datetime import datetime
from pathlib import Path

OUTPUT_DIR = Path("D:/workspace/ISNBIZ_Files/generated_founders/community")
API_ENDPOINT = "https://queue.fal.run/fal-ai/gpt-image-1.5/edit"

# Founder headshots for identity reference
HEADSHOTS = {
    "jonathan": "https://isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com/assets/founders/headshots_with_bg/jonathan_headshot.webp",
    "alicia": "https://isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com/assets/founders/headshots_with_bg/alicia_headshot.webp",
    "bri": "https://isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com/assets/founders/headshots_with_bg/bri_headshot.webp",
    "lilly": "https://isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com/assets/founders/headshots_with_bg/lilly_headshot.webp"
}

# Scene configurations with advanced prompting
SCENES = [
    # ALL FOUR FOUNDERS - Community scenes
    {
        "id": "all_four_yoga",
        "name": "All Four - Yoga",
        "people": ["jonathan", "alicia", "bri", "lilly"],
        "prompt": """[IDENTITY PRESERVATION: CRITICAL]
Preserve each person's exact facial features, skin tone, bone structure, and identity with 100% accuracy.
The four people in the reference images must be recognizable as themselves.

[SCENE: Outdoor yoga class at sunrise]
Four friends doing yoga together in a beautiful park at golden hour. Casual athletic wear - yoga pants,
comfortable tops. Natural, relaxed poses on yoga mats. Dappled morning sunlight through trees.
Jonathan (man) in warrior pose, Alicia (woman, long dark hair), Bri (woman), and Lilly (woman) in
various yoga positions nearby. Genuine smiles, peaceful expressions. NOT looking at camera - focused
on their practice or each other.

[TECHNICAL: Canon R5, 35mm, f/2.8, golden hour backlight, documentary lifestyle photography]
[MOOD: Wellness, friendship, balance, community connection]

Negative: (((long necks))), bad proportions, looking at camera, gym interior, studio setting,
professional yoga instructor poses, stock photo staging, plastic skin, distorted faces,
merged bodies, extra limbs"""
    },
    {
        "id": "all_four_coffee",
        "name": "All Four - Coffee Shop",
        "people": ["jonathan", "alicia", "bri", "lilly"],
        "prompt": """[IDENTITY PRESERVATION: CRITICAL]
Preserve each person's exact facial features, skin tone, bone structure, and identity with 100% accuracy.

[SCENE: Cozy coffee shop hangout]
Four friends laughing together at a trendy coffee shop. Casual weekend clothing - jeans, sweaters,
comfortable layers. Seated around a rustic wooden table with lattes and pastries. Warm ambient
lighting, exposed brick background. Jonathan (man) telling a story, the three women (Alicia with
long dark hair, Bri, Lilly) genuinely engaged and laughing. Candid moment captured. NOT looking
at camera - natural conversation.

[TECHNICAL: Sony A7III, 50mm, f/1.8, warm indoor lighting, lifestyle editorial style]
[MOOD: Friendship, warmth, authentic connection, relaxed weekend vibes]

Negative: (((long necks))), bad proportions, looking at camera, posed group photo, stiff postures,
business attire, formal setting, plastic skin, distorted faces, cloned expressions"""
    },
    {
        "id": "all_four_gym",
        "name": "All Four - Gym",
        "people": ["jonathan", "alicia", "bri", "lilly"],
        "prompt": """[IDENTITY PRESERVATION: CRITICAL]
Preserve each person's exact facial features, skin tone, and identity with 100% accuracy.

[SCENE: Modern gym workout together]
Four friends working out together in a bright, modern fitness studio. Athletic wear - workout
clothes, sneakers. Mix of activities: Jonathan (man) at weights, Alicia (long dark hair) on
exercise bike, Bri with resistance bands, Lilly stretching. High ceilings, natural light from
large windows. Energetic but natural moment. Supporting each other's fitness journey. NOT
looking at camera - focused on workout.

[TECHNICAL: Wide angle 24mm, f/4, bright natural gym lighting, fitness lifestyle photography]
[MOOD: Health, motivation, team spirit, active lifestyle]

Negative: (((long necks))), bad proportions, looking at camera, bodybuilder poses, sweaty
close-ups, dark gym, plastic skin, distorted anatomy, merged limbs"""
    },
    {
        "id": "all_four_outreach",
        "name": "All Four - Community Outreach",
        "people": ["jonathan", "alicia", "bri", "lilly"],
        "prompt": """[IDENTITY PRESERVATION: CRITICAL]
Preserve each person's exact facial features, skin tone, and identity with 100% accuracy.

[SCENE: Homeless women's outreach event]
Four compassionate volunteers at a community outreach event for homeless women. Casual clothing
with volunteer badges. Setting up care packages, handing out supplies at a community center or
outdoor event. Jonathan (man) carrying boxes, Alicia (long dark hair), Bri, and Lilly warmly
engaging with community members (shown from behind or partially). Genuine compassion and
connection. NOT looking at camera - focused on helping.

[TECHNICAL: Documentary photography style, 35mm, f/2.8, natural outdoor/indoor light]
[MOOD: Compassion, service, community impact, genuine care, dignity]

Negative: (((long necks))), bad proportions, looking at camera, posed charity photo,
pity expressions, exploitation imagery, plastic skin, distorted faces"""
    },

    # JONATHAN + BRI
    {
        "id": "jonathan_bri_coffee",
        "name": "Jonathan & Bri - Coffee",
        "people": ["jonathan", "bri"],
        "prompt": """[IDENTITY PRESERVATION: CRITICAL]
Preserve Jonathan's and Bri's exact facial features, skin tone, and identity with 100% accuracy.

[SCENE: Coffee meeting]
Jonathan (man) and Bri (woman) having coffee at a sunny cafe patio. Casual smart clothing.
Engaged in friendly conversation over lattes. Natural morning light, urban backdrop softly
blurred. Warm, collegial dynamic. NOT looking at camera - talking to each other.

[TECHNICAL: 85mm portrait lens, f/2, natural side light, lifestyle editorial]
[MOOD: Friendship, collaboration, relaxed professionalism]

Negative: (((long necks))), bad proportions, looking at camera, romantic poses,
plastic skin, distorted features"""
    },
    {
        "id": "jonathan_bri_gym",
        "name": "Jonathan & Bri - Gym",
        "people": ["jonathan", "bri"],
        "prompt": """[IDENTITY PRESERVATION: CRITICAL]
Preserve Jonathan's and Bri's exact facial features and identity with 100% accuracy.

[SCENE: Gym workout partners]
Jonathan (man) and Bri (woman) working out together. Athletic wear. Jonathan spotting Bri
at weights, or both on adjacent cardio machines. Bright modern gym. Encouraging, supportive
dynamic. NOT looking at camera - focused on exercise.

[TECHNICAL: 35mm, f/2.8, bright gym lighting, fitness lifestyle]
[MOOD: Motivation, support, healthy lifestyle, teamwork]

Negative: (((long necks))), bad proportions, looking at camera, flexing poses,
plastic skin, distorted anatomy"""
    },

    # JONATHAN + LILLY
    {
        "id": "jonathan_lilly_yoga",
        "name": "Jonathan & Lilly - Yoga",
        "people": ["jonathan", "lilly"],
        "prompt": """[IDENTITY PRESERVATION: CRITICAL]
Preserve Jonathan's and Lilly's exact facial features and identity with 100% accuracy.

[SCENE: Partner yoga]
Jonathan (man) and Lilly (woman) doing partner yoga stretches in a peaceful outdoor setting.
Comfortable athletic wear. Morning light, grass or yoga studio. Helping each other with
stretches, natural and relaxed. NOT looking at camera - focused on practice.

[TECHNICAL: 50mm, f/2.8, soft natural light, wellness photography]
[MOOD: Balance, trust, wellness, mindfulness]

Negative: (((long necks))), bad proportions, looking at camera, contorted poses,
plastic skin, distorted features"""
    },
    {
        "id": "jonathan_lilly_outreach",
        "name": "Jonathan & Lilly - Outreach",
        "people": ["jonathan", "lilly"],
        "prompt": """[IDENTITY PRESERVATION: CRITICAL]
Preserve Jonathan's and Lilly's exact facial features and identity with 100% accuracy.

[SCENE: Community service]
Jonathan (man) and Lilly (woman) volunteering at a community event. Casual clothes with
volunteer vests. Organizing supplies, warmly greeting community members. Genuine care and
compassion visible. NOT looking at camera - engaged in service.

[TECHNICAL: Documentary style, 35mm, f/4, natural light]
[MOOD: Compassion, service, teamwork, community]

Negative: (((long necks))), bad proportions, looking at camera, staged charity,
plastic skin, distorted faces"""
    },

    # JONATHAN + ALICIA
    {
        "id": "jonathan_alicia_coffee",
        "name": "Jonathan & Alicia - Coffee",
        "people": ["jonathan", "alicia"],
        "prompt": """[IDENTITY PRESERVATION: CRITICAL]
Preserve Jonathan's and Alicia's exact facial features and identity with 100% accuracy.
Alicia has long dark hair.

[SCENE: Cafe conversation]
Jonathan (man) and Alicia (woman, long dark hair) at a cozy coffee shop. Casual weekend
attire. Deep in friendly conversation, genuine expressions. Warm lighting, books and
plants in background. NOT looking at camera - engaged with each other.

[TECHNICAL: 85mm, f/1.8, warm cafe lighting, lifestyle portrait]
[MOOD: Connection, friendship, intellectual engagement]

Negative: (((long necks))), bad proportions, looking at camera, romantic poses,
plastic skin, distorted features"""
    },
    {
        "id": "jonathan_alicia_gym",
        "name": "Jonathan & Alicia - Gym",
        "people": ["jonathan", "alicia"],
        "prompt": """[IDENTITY PRESERVATION: CRITICAL]
Preserve Jonathan's and Alicia's exact facial features and identity with 100% accuracy.
Alicia has long dark hair.

[SCENE: Fitness session]
Jonathan (man) and Alicia (woman, long dark hair) at a modern gym. Athletic wear.
Jonathan on treadmill, Alicia on adjacent elliptical, chatting while exercising.
Bright, energetic atmosphere. NOT looking at camera - mid-workout conversation.

[TECHNICAL: 35mm, f/4, bright natural gym light, lifestyle fitness]
[MOOD: Energy, health, friendship, motivation]

Negative: (((long necks))), bad proportions, looking at camera, posed,
plastic skin, distorted anatomy"""
    },

    # ALL THREE WOMEN
    {
        "id": "girls_yoga",
        "name": "Girls - Yoga Class",
        "people": ["alicia", "bri", "lilly"],
        "prompt": """[IDENTITY PRESERVATION: CRITICAL]
Preserve each woman's exact facial features, skin tone, and identity with 100% accuracy.
Alicia has long dark hair.

[SCENE: Women's yoga session]
Three women friends - Alicia (long dark hair), Bri, and Lilly - doing yoga together in
a bright, airy studio. Matching yoga outfits in soft colors. Synchronized peaceful poses
on mats. Natural light streaming through windows. Serene expressions. NOT looking at
camera - focused inward on practice.

[TECHNICAL: Wide 28mm, f/4, soft studio light, wellness editorial]
[MOOD: Sisterhood, peace, wellness, feminine strength]

Negative: (((long necks))), bad proportions, looking at camera, contorted poses,
plastic skin, distorted faces, merged bodies"""
    },
    {
        "id": "girls_coffee",
        "name": "Girls - Coffee Date",
        "people": ["alicia", "bri", "lilly"],
        "prompt": """[IDENTITY PRESERVATION: CRITICAL]
Preserve each woman's exact facial features and identity with 100% accuracy.
Alicia has long dark hair.

[SCENE: Girls' coffee date]
Three women friends - Alicia (long dark hair), Bri, and Lilly - at a trendy brunch spot.
Casual chic outfits. Sharing laughs over coffee and pastries at a marble table. Natural
daylight, Instagram-worthy cafe interior. Genuine friendship moment captured. NOT looking
at camera - mid-conversation laughter.

[TECHNICAL: 50mm, f/2, bright natural cafe light, lifestyle editorial]
[MOOD: Friendship, joy, connection, girl power]

Negative: (((long necks))), bad proportions, looking at camera, posed selfie,
plastic skin, distorted features, cloned expressions"""
    },
    {
        "id": "girls_gym",
        "name": "Girls - Gym Session",
        "people": ["alicia", "bri", "lilly"],
        "prompt": """[IDENTITY PRESERVATION: CRITICAL]
Preserve each woman's exact facial features and identity with 100% accuracy.
Alicia has long dark hair.

[SCENE: Women's gym workout]
Three women friends - Alicia (long dark hair), Bri, and Lilly - working out together.
Coordinated athletic wear. Group fitness class or weight area. High-fiving, encouraging
each other, energetic dynamic. Bright modern gym. NOT looking at camera - focused on
workout and each other.

[TECHNICAL: 35mm, f/2.8, bright gym lighting, fitness lifestyle]
[MOOD: Empowerment, support, strength, friendship goals]

Negative: (((long necks))), bad proportions, looking at camera, bodybuilder poses,
plastic skin, distorted anatomy, merged limbs"""
    },
    {
        "id": "girls_outreach",
        "name": "Girls - Outreach",
        "people": ["alicia", "bri", "lilly"],
        "prompt": """[IDENTITY PRESERVATION: CRITICAL]
Preserve each woman's exact facial features and identity with 100% accuracy.
Alicia has long dark hair.

[SCENE: Women helping women]
Three women - Alicia (long dark hair), Bri, and Lilly - at a women's shelter outreach.
Casual clothes with volunteer badges. Sorting donations, preparing care packages, warmly
connecting with shelter residents (shown respectfully, from behind). Meaningful service
moment. NOT looking at camera - engaged in helping.

[TECHNICAL: Documentary 35mm, f/4, warm indoor light, photojournalism style]
[MOOD: Compassion, sisterhood, service, empowerment, dignity]

Negative: (((long necks))), bad proportions, looking at camera, pity shots,
plastic skin, distorted faces, exploitation imagery"""
    }
]


def get_fal_key():
    result = subprocess.run(
        ["op", "item", "get", "FAL API Key", "--vault", "TrueNAS Infrastructure",
         "--reveal", "--fields", "credential"],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        raise RuntimeError(f"Failed to get FAL key: {result.stderr}")
    return result.stdout.strip()


def submit_generation(fal_key: str, prompt: str, image_urls: list, num_images: int = 2) -> dict:
    headers = {
        "Authorization": f"Key {fal_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "prompt": prompt,
        "image_urls": image_urls,
        "input_fidelity": "high",
        "quality": "low",
        "image_size": "1536x1024",
        "output_format": "webp",
        "num_images": num_images
    }
    response = requests.post(API_ENDPOINT, headers=headers, json=payload, timeout=30)
    response.raise_for_status()
    return response.json()


def poll_for_completion(fal_key: str, request_id: str, max_wait: int = 300) -> dict:
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

    raise TimeoutError(f"Request {request_id} did not complete")


def download_image(url: str, output_path: Path) -> bool:
    try:
        response = requests.get(url, timeout=60)
        response.raise_for_status()
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_bytes(response.content)
        return True
    except Exception as e:
        print(f"  ERROR: {e}")
        return False


def main():
    print("=" * 60)
    print("COMMUNITY LIFESTYLE SCENES - Identity Preserved")
    print("=" * 60)

    manifest = {
        "generated_at": datetime.now().isoformat(),
        "scenes": [],
        "stats": {"total": 0, "errors": 0}
    }

    print("\nLoading FAL API key...")
    fal_key = get_fal_key()
    print("  Key loaded")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print(f"\nGenerating {len(SCENES)} scene types (2 variants each)...\n")

    for scene in SCENES:
        print(f"Generating: {scene['name']}...")

        # Get headshots for people in this scene
        image_urls = [HEADSHOTS[p] for p in scene["people"]]

        try:
            queue_resp = submit_generation(fal_key, scene["prompt"], image_urls, num_images=2)
            request_id = queue_resp["request_id"]
            print(f"  Submitted: {request_id}")

            result = poll_for_completion(fal_key, request_id)

            for i, img_data in enumerate(result.get("images", [])):
                output_path = OUTPUT_DIR / f"{scene['id']}_{i+1}.webp"
                if download_image(img_data["url"], output_path):
                    print(f"  Downloaded: {output_path.name}")
                    manifest["scenes"].append({
                        "id": scene["id"],
                        "name": scene["name"],
                        "people": scene["people"],
                        "variant": i + 1,
                        "local_path": str(output_path),
                        "remote_url": img_data["url"]
                    })
                    manifest["stats"]["total"] += 1

        except Exception as e:
            print(f"  ERROR: {e}")
            manifest["stats"]["errors"] += 1

    # Save manifest
    manifest_path = OUTPUT_DIR / "community_manifest.json"
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)

    print("\n" + "=" * 60)
    print("GENERATION COMPLETE")
    print("=" * 60)
    print(f"Total scenes: {manifest['stats']['total']}")
    print(f"Errors: {manifest['stats']['errors']}")
    print(f"Manifest: {manifest_path}")

    return manifest


if __name__ == "__main__":
    main()
