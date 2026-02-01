#!/usr/bin/env python3
"""
Professional Website Asset Generator using fal.ai's LATEST 2026 Models
======================================================================

Generates hero backgrounds, portfolio mockups, service icons, team visuals, and video assets

LATEST MODELS USED (2026):
- FLUX.2 [max] - State-of-the-art image generation with exceptional realism
- FLUX.2 [pro] - Studio-grade images, zero-config, production-optimized
- FLUX1.1 [pro] ultra - 2K resolution with improved photo realism (6x faster)
- Kling 2.6 Pro - Latest video with native audio generation
- Hunyuan Video 1.5 - Alternative video generation with high visual quality

Brand Colors:
- Blue: #1E9FF2
- Cyan: #5FDFDF
- Charcoal: #3F4447
"""

import os
import json
import requests
import time
from pathlib import Path
from typing import Dict, List, Optional
import subprocess

# Configuration
FAL_API_KEY = os.getenv("FAL_KEY")  # Get from environment or 1Password
if not FAL_API_KEY:
    print("WARNING: FAL_KEY not found in environment variables")
    print("Please set FAL_KEY or retrieve it from 1Password (search for 'fal')")
    exit(1)

BASE_URL = "https://fal.run"
OUTPUT_DIR = Path("/mnt/d/workspace/ISNBIZ_Files/assets/generated")

# Brand colors
BRAND_COLORS = {
    "blue": "#1E9FF2",
    "cyan": "#5FDFDF",
    "charcoal": "#3F4447"
}

class FalAIGenerator:
    """Generate professional website assets using fal.ai's latest 2026 models"""

    # Latest 2026 Model Endpoints
    MODELS = {
        "flux2_max": "fal-ai/flux-2-max",              # Best: exceptional realism & precision
        "flux2_pro": "fal-ai/flux-2-pro",              # Studio-grade, production-optimized
        "flux11_ultra": "fal-ai/flux-pro/v1.1-ultra",  # 2K resolution, 6x faster
        "kling_video": "fal-ai/kling-video/v2.6/pro/text-to-video",  # Latest video w/ audio
        "hunyuan_video": "fal-ai/hunyuan-video-v1.5/text-to-video",  # Alternative video
    }

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Key {api_key}",
            "Content-Type": "application/json"
        }
        self.base_url = "https://fal.run"

    def generate_image(
        self,
        prompt: str,
        output_path: Path,
        model: str = "flux2_max",
        width: int = 2560,
        height: int = 1440,
        num_inference_steps: int = 28,
        guidance_scale: float = 3.5
    ) -> Optional[str]:
        """
        Generate image using latest fal.ai models

        Args:
            prompt: Text description of desired image
            output_path: Where to save the generated image
            model: Model to use (flux2_max, flux2_pro, flux11_ultra)
            width: Image width in pixels
            height: Image height in pixels
            num_inference_steps: Quality/speed tradeoff (higher = better quality)
            guidance_scale: How closely to follow prompt (3-4 recommended)

        Returns:
            Path to generated image or None if failed
        """
        endpoint = f"{self.base_url}/{self.MODELS[model]}"

        # Build payload based on model
        if model == "flux11_ultra":
            payload = {
                "prompt": prompt,
                "image_size": {"width": width, "height": height},
                "num_inference_steps": num_inference_steps,
                "guidance_scale": guidance_scale,
                "output_format": "png",
                "raw": False
            }
        else:  # flux2_max, flux2_pro
            payload = {
                "prompt": prompt,
                "image_size": {"width": width, "height": height},
                "num_inference_steps": num_inference_steps,
                "guidance_scale": guidance_scale,
                "output_format": "png",
                "safety_tolerance": "2"
            }

        print(f"\n🎨 Generating with {model}: {output_path.name}")
        print(f"📝 Prompt: {prompt[:100]}...")

        try:
            response = requests.post(endpoint, headers=self.headers, json=payload)
            response.raise_for_status()

            result = response.json()

            # Download the generated image
            image_url = None
            if "images" in result and len(result["images"]) > 0:
                image_url = result["images"][0]["url"]
            elif "image" in result:
                image_url = result["image"]["url"]

            if image_url:
                img_response = requests.get(image_url)
                img_response.raise_for_status()

                output_path.parent.mkdir(parents=True, exist_ok=True)
                with open(output_path, 'wb') as f:
                    f.write(img_response.content)

                print(f"✅ Saved: {output_path}")
                return str(output_path)
            else:
                print(f"❌ No image in response")
                print(f"Response: {json.dumps(result, indent=2)}")
                return None

        except requests.exceptions.RequestException as e:
            print(f"❌ Error generating image: {e}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"Response: {e.response.text}")
            return None

    def generate_video(
        self,
        prompt: str,
        output_path: Path,
        model: str = "kling_video",
        duration: int = 10,
        aspect_ratio: str = "16:9",
        generate_audio: bool = False
    ) -> Optional[str]:
        """
        Generate video using latest 2026 video models

        Args:
            prompt: Text description of desired video
            output_path: Where to save the generated video
            model: Model to use (kling_video, hunyuan_video)
            duration: Video length in seconds (5 or 10 for Kling, 5s for Hunyuan)
            aspect_ratio: "16:9", "9:16", or "1:1"
            generate_audio: Whether to generate audio (Kling 2.6 only)

        Returns:
            Path to generated video or None if failed
        """
        endpoint = f"{self.base_url}/{self.MODELS[model]}"

        # Build payload based on model
        if model == "kling_video":
            payload = {
                "prompt": prompt,
                "duration": duration,  # 5 or 10 seconds
                "aspect_ratio": aspect_ratio,
                "audio": generate_audio,  # Native audio in Kling 2.6
                "negative_prompt": "low quality, blurry, distorted, pixelated"
            }
        else:  # hunyuan_video
            payload = {
                "prompt": prompt,
                "duration": min(duration, 5),  # Hunyuan max 5s
                "video_size": aspect_ratio,
                "num_inference_steps": 50
            }

        print(f"\n🎬 Generating video with {model}: {output_path.name}")
        print(f"📝 Prompt: {prompt[:100]}...")
        print(f"⏱️  This may take 3-5 minutes...")

        try:
            response = requests.post(endpoint, headers=self.headers, json=payload)
            response.raise_for_status()

            result = response.json()

            # Handle async video generation - may need to poll for completion
            video_url = None
            if "video" in result:
                if isinstance(result["video"], dict):
                    video_url = result["video"]["url"]
                else:
                    video_url = result["video"]

            if video_url:
                print(f"📥 Downloading video...")
                video_response = requests.get(video_url)
                video_response.raise_for_status()

                output_path.parent.mkdir(parents=True, exist_ok=True)
                with open(output_path, 'wb') as f:
                    f.write(video_response.content)

                print(f"✅ Saved video: {output_path}")
                return str(output_path)
            else:
                print(f"❌ No video in response")
                print(f"Response: {json.dumps(result, indent=2)}")
                return None

        except requests.exceptions.RequestException as e:
            print(f"❌ Error generating video: {e}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"Response: {e.response.text}")
            return None


def generate_hero_backgrounds(generator: FalAIGenerator, output_dir: Path) -> List[str]:
    """Generate 5 hero background variations"""

    hero_prompts = [
        f"Abstract technological background with neural network patterns, flowing data streams, and geometric shapes. "
        f"Color palette: electric blue {BRAND_COLORS['blue']}, cyan {BRAND_COLORS['cyan']}, dark charcoal {BRAND_COLORS['charcoal']}. "
        f"Professional, modern, high-tech aesthetic. Subtle gradient. Award-winning design. 8K resolution.",

        f"Futuristic AI-powered dashboard interface floating in 3D space with holographic elements. "
        f"Brand colors: {BRAND_COLORS['blue']}, {BRAND_COLORS['cyan']}, {BRAND_COLORS['charcoal']}. "
        f"Clean, minimalist, professional. Depth of field. Cinematic lighting. Ultra high quality.",

        f"Abstract particle system forming AI and cloud computing symbols in space. "
        f"Vibrant blue {BRAND_COLORS['blue']} and cyan {BRAND_COLORS['cyan']} particles against dark {BRAND_COLORS['charcoal']} background. "
        f"Dynamic, elegant, professional. Motion blur effect. Premium quality. Photorealistic.",

        f"Sleek modern technology workspace with multiple holographic screens displaying code and data visualizations. "
        f"Color scheme: {BRAND_COLORS['blue']}, {BRAND_COLORS['cyan']}, {BRAND_COLORS['charcoal']}. "
        f"Professional office environment. Soft lighting. Contemporary design. High-end render.",

        f"Abstract geometric mesh network representing cloud infrastructure and AI connections. "
        f"Brand palette: bright blue {BRAND_COLORS['blue']}, turquoise {BRAND_COLORS['cyan']}, charcoal {BRAND_COLORS['charcoal']}. "
        f"Sophisticated, modern, clean. Gradient overlays. Studio quality. Award-worthy composition."
    ]

    generated_files = []
    hero_dir = output_dir / "hero"

    for i, prompt in enumerate(hero_prompts, 1):
        output_path = hero_dir / f"hero_background_{i}.png"
        result = generator.generate_image(
            prompt=prompt,
            output_path=output_path,
            model="flux2_max",  # Best quality for hero images
            width=2560,
            height=1440,
            num_inference_steps=28,
            guidance_scale=3.5
        )
        if result:
            generated_files.append(result)
        time.sleep(2)  # Rate limiting

    return generated_files


def generate_portfolio_mockups(generator: FalAIGenerator, output_dir: Path) -> List[str]:
    """Generate 8+ portfolio project mockups"""

    portfolio_prompts = [
        f"Modern AI chatbot interface mockup with conversational UI, message bubbles, and smart suggestions. "
        f"Clean design with {BRAND_COLORS['blue']} accents and {BRAND_COLORS['charcoal']} text. "
        f"Professional SaaS application design. High-fidelity mockup. Dribbble quality.",

        f"Sophisticated AI analytics dashboard with data visualizations, charts, graphs, and KPI widgets. "
        f"Color scheme: {BRAND_COLORS['blue']}, {BRAND_COLORS['cyan']}, white, {BRAND_COLORS['charcoal']}. "
        f"Modern UI/UX design. Clean layout. Professional quality. Behance featured.",

        f"Mobile app screenshots showing opportunity tracking and AI-powered business insights. "
        f"iOS design with {BRAND_COLORS['blue']} primary color and {BRAND_COLORS['cyan']} highlights. "
        f"Multiple screens in phone mockups. Professional app design. App Store quality.",

        f"VS Code-style code editor interface with syntax highlighting, showing Python AI/ML code. "
        f"Dark theme with {BRAND_COLORS['cyan']} and {BRAND_COLORS['blue']} syntax colors. "
        f"Professional developer tool design. Clean, readable. High-quality mockup.",

        f"Real-time data visualization dashboard with live charts, metrics, and monitoring panels. "
        f"Brand colors: {BRAND_COLORS['blue']}, {BRAND_COLORS['cyan']}, dark mode {BRAND_COLORS['charcoal']}. "
        f"Enterprise-grade UI design. Professional quality. Award-winning interface.",

        f"Cloud architecture diagram visualization with nodes, connections, and infrastructure components. "
        f"Technical illustration with {BRAND_COLORS['blue']} primary and {BRAND_COLORS['cyan']} secondary colors. "
        f"Professional technical documentation style. Clean, clear, educational.",

        f"Modern CRM interface mockup with contact management, pipeline view, and automation features. "
        f"Professional SaaS design with {BRAND_COLORS['blue']} branding. "
        f"Clean, intuitive UI. High-fidelity design. Portfolio quality.",

        f"AI-powered security dashboard showing threat detection, compliance metrics, and security analytics. "
        f"Dark theme with {BRAND_COLORS['cyan']} alerts and {BRAND_COLORS['blue']} accents. "
        f"Professional cybersecurity interface. Enterprise quality. Modern design.",

        f"Machine learning model training interface with progress indicators, accuracy graphs, and hyperparameters. "
        f"Technical UI with {BRAND_COLORS['blue']} and {BRAND_COLORS['cyan']} data visualizations. "
        f"Professional ML platform design. Clean, functional. High-quality mockup.",

        f"API documentation portal with code examples, endpoint listings, and interactive testing interface. "
        f"Developer-focused design with {BRAND_COLORS['blue']} branding and {BRAND_COLORS['charcoal']} code blocks. "
        f"Professional developer portal. Clean typography. Award-worthy design."
    ]

    generated_files = []
    portfolio_dir = output_dir / "portfolio"

    for i, prompt in enumerate(portfolio_prompts, 1):
        output_path = portfolio_dir / f"portfolio_mockup_{i}.png"
        result = generator.generate_image(
            prompt=prompt,
            output_path=output_path,
            model="flux11_ultra",  # 2K resolution for detailed mockups
            width=1920,
            height=1080,
            num_inference_steps=28,
            guidance_scale=3.5
        )
        if result:
            generated_files.append(result)
        time.sleep(2)

    return generated_files


def generate_service_icons(generator: FalAIGenerator, output_dir: Path) -> List[str]:
    """Generate 6 custom service icons"""

    icon_prompts = [
        f"Minimalist AI/ML icon featuring neural network nodes and connections. "
        f"Simple, modern design in {BRAND_COLORS['blue']} and {BRAND_COLORS['cyan']}. "
        f"Flat design, professional, clean lines. Icon design. White background.",

        f"Modern cloud architecture icon with server and network symbols. "
        f"Minimalist style, {BRAND_COLORS['blue']} primary color, {BRAND_COLORS['cyan']} accents. "
        f"Professional tech icon. Clean, simple. White background. Vector-style.",

        f"Sleek mobile development icon showing smartphone with app interface elements. "
        f"Modern minimal design in {BRAND_COLORS['blue']} and {BRAND_COLORS['cyan']}. "
        f"Professional icon design. Flat style. White background. Clean lines.",

        f"Data engineering icon with database, pipeline, and data flow symbols. "
        f"Minimalist technical icon in {BRAND_COLORS['blue']} and {BRAND_COLORS['cyan']}. "
        f"Professional design. Clean geometry. White background. Modern style.",

        f"Security and compliance icon featuring shield with checkmark and lock elements. "
        f"Simple, professional design in {BRAND_COLORS['blue']} and {BRAND_COLORS['cyan']}. "
        f"Minimalist icon. Clean shapes. White background. Trust-inspiring.",

        f"Custom development icon with code brackets and customization symbols. "
        f"Modern minimal style, {BRAND_COLORS['blue']} and {BRAND_COLORS['cyan']} colors. "
        f"Professional tech icon. Clean design. White background. Developer-focused."
    ]

    generated_files = []
    icons_dir = output_dir / "icons"

    for i, prompt in enumerate(icon_prompts, 1):
        output_path = icons_dir / f"service_icon_{i}.png"
        result = generator.generate_image(
            prompt=prompt,
            output_path=output_path,
            model="flux2_pro",  # Clean, professional icons
            width=1024,
            height=1024,
            num_inference_steps=20,
            guidance_scale=3.0
        )
        if result:
            generated_files.append(result)
        time.sleep(2)

    return generated_files


def generate_team_visuals(generator: FalAIGenerator, output_dir: Path) -> List[str]:
    """Generate team/about section visuals"""

    team_prompts = [
        f"Abstract representation of diverse team collaboration with interconnected human silhouettes and technology elements. "
        f"Professional, modern style with {BRAND_COLORS['blue']}, {BRAND_COLORS['cyan']}, {BRAND_COLORS['charcoal']} colors. "
        f"Corporate imagery. Clean, inspiring. Award-winning design.",

        f"Modern innovation and technology theme with abstract shapes, light beams, and digital elements. "
        f"Professional business aesthetic. Brand colors: {BRAND_COLORS['blue']}, {BRAND_COLORS['cyan']}, {BRAND_COLORS['charcoal']}. "
        f"Sophisticated, forward-thinking. High-quality render.",

        f"Contemporary professional office environment with modern technology, clean workspace, natural lighting. "
        f"Subtle {BRAND_COLORS['blue']} and {BRAND_COLORS['cyan']} accent colors. "
        f"Professional corporate photography style. Bright, open, innovative atmosphere.",

        f"Abstract teamwork and connection concept with geometric shapes forming network patterns. "
        f"Modern design with {BRAND_COLORS['blue']}, {BRAND_COLORS['cyan']}, {BRAND_COLORS['charcoal']} palette. "
        f"Professional, inspiring. Clean composition. Award-worthy."
    ]

    generated_files = []
    team_dir = output_dir / "team"

    for i, prompt in enumerate(team_prompts, 1):
        output_path = team_dir / f"team_visual_{i}.png"
        result = generator.generate_image(
            prompt=prompt,
            output_path=output_path,
            model="flux2_max",  # Photorealistic quality for team visuals
            width=1920,
            height=1080,
            num_inference_steps=28,
            guidance_scale=3.5
        )
        if result:
            generated_files.append(result)
        time.sleep(2)

    return generated_files


def generate_video_assets(generator: FalAIGenerator, output_dir: Path) -> List[str]:
    """Generate video assets for hero sections"""

    video_prompts = [
        f"Smooth looping animation of abstract technology particles flowing and forming AI neural network patterns. "
        f"Color palette: electric blue {BRAND_COLORS['blue']}, cyan {BRAND_COLORS['cyan']}, dark {BRAND_COLORS['charcoal']}. "
        f"Professional, elegant motion. Seamless loop. Cinematic quality. 4K resolution.",

        f"Elegant camera movement through a futuristic data center with holographic displays and flowing data streams. "
        f"Brand colors: {BRAND_COLORS['blue']}, {BRAND_COLORS['cyan']}, {BRAND_COLORS['charcoal']}. "
        f"Professional corporate video. Smooth motion. High-end production quality. Loopable."
    ]

    generated_files = []
    video_dir = output_dir / "video"

    for i, prompt in enumerate(video_prompts, 1):
        output_path = video_dir / f"hero_video_{i}.mp4"
        result = generator.generate_video(
            prompt=prompt,
            output_path=output_path,
            model="kling_video",  # Latest Kling 2.6 Pro
            duration=10,  # 10 seconds for hero loops
            aspect_ratio="16:9",
            generate_audio=False  # Background videos don't need audio
        )
        if result:
            generated_files.append(result)
        time.sleep(5)  # Longer delay for video generation

    return generated_files


def main():
    """Main execution function"""

    print("=" * 80)
    print("Professional Website Asset Generator")
    print("Using fal.ai's Latest 2026 Models")
    print("=" * 80)
    print(f"\nBrand Colors:")
    print(f"  Blue: {BRAND_COLORS['blue']}")
    print(f"  Cyan: {BRAND_COLORS['cyan']}")
    print(f"  Charcoal: {BRAND_COLORS['charcoal']}")
    print(f"\nOutput Directory: {OUTPUT_DIR}")
    print("=" * 80)

    # Initialize generator
    generator = FalAIGenerator(FAL_API_KEY)

    all_generated = []

    # Generate each category
    print("\n📸 Generating Hero Backgrounds (5 variations)...")
    hero_files = generate_hero_backgrounds(generator, OUTPUT_DIR)
    all_generated.extend(hero_files)
    print(f"✓ Generated {len(hero_files)} hero backgrounds\n")

    print("📸 Generating Portfolio Mockups (10 images)...")
    portfolio_files = generate_portfolio_mockups(generator, OUTPUT_DIR)
    all_generated.extend(portfolio_files)
    print(f"✓ Generated {len(portfolio_files)} portfolio mockups\n")

    print("📸 Generating Service Icons (6 custom icons)...")
    icon_files = generate_service_icons(generator, OUTPUT_DIR)
    all_generated.extend(icon_files)
    print(f"✓ Generated {len(icon_files)} service icons\n")

    print("📸 Generating Team/About Visuals (4 images)...")
    team_files = generate_team_visuals(generator, OUTPUT_DIR)
    all_generated.extend(team_files)
    print(f"✓ Generated {len(team_files)} team visuals\n")

    print("🎬 Generating Video Assets (2 videos - this will take longer)...")
    video_files = generate_video_assets(generator, OUTPUT_DIR)
    all_generated.extend(video_files)
    print(f"✓ Generated {len(video_files)} video assets\n")

    # Summary
    print("=" * 80)
    print("GENERATION COMPLETE")
    print("=" * 80)
    print(f"\nTotal assets generated: {len(all_generated)}")
    print(f"\nAssets saved to: {OUTPUT_DIR}")
    print("\nBreakdown:")
    print(f"  - Hero Backgrounds: {len(hero_files)}")
    print(f"  - Portfolio Mockups: {len(portfolio_files)}")
    print(f"  - Service Icons: {len(icon_files)}")
    print(f"  - Team Visuals: {len(team_files)}")
    print(f"  - Video Assets: {len(video_files)}")

    # Save manifest
    manifest = {
        "generated_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "total_assets": len(all_generated),
        "models_used": {
            "images": ["FLUX.2 Max", "FLUX.2 Pro", "FLUX1.1 Pro Ultra"],
            "videos": ["Kling 2.6 Pro", "Hunyuan Video 1.5"],
            "description": "Latest 2026 models from fal.ai"
        },
        "brand_colors": BRAND_COLORS,
        "files": {
            "hero_backgrounds": hero_files,
            "portfolio_mockups": portfolio_files,
            "service_icons": icon_files,
            "team_visuals": team_files,
            "video_assets": video_files
        }
    }

    manifest_path = OUTPUT_DIR / "manifest.json"
    with open(manifest_path, 'w') as f:
        json.dump(manifest, f, indent=2)

    print(f"\n✓ Manifest saved to: {manifest_path}")
    print("\n" + "=" * 80)
    print("Ready to use in your professional website!")
    print("=" * 80)


if __name__ == "__main__":
    main()
