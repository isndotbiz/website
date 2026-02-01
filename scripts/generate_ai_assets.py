#!/usr/bin/env python3
"""
AI Asset Generation Script for ISN.BIZ Website
Generates professional visual assets using Flux 2 API via fal.ai

Requirements:
    pip install fal-client pillow requests python-dotenv

Usage:
    1. Set FAL_KEY environment variable or create .env file
    2. Run: python generate_ai_assets.py
    3. Assets will be saved to /mnt/d/workspace/ISNBIZ_Files/assets/images/
"""

import os
import sys
import json
import time
from pathlib import Path
from typing import Dict, List, Optional
import requests

try:
    import fal_client
    from PIL import Image
    from io import BytesIO
except ImportError:
    print("Missing dependencies. Install with:")
    print("pip install fal-client pillow requests python-dotenv")
    sys.exit(1)

# Brand colors
BRAND_COLORS = {
    'blue': '#1E9FF2',
    'cyan': '#5FDFDF',
    'charcoal': '#3F4447'
}

# Base directory for assets
BASE_DIR = Path('/mnt/d/workspace/ISNBIZ_Files/assets/images')

# Asset specifications
ASSETS = {
    'hero_backgrounds': {
        'output_dir': BASE_DIR / 'hero',
        'specs': {
            'resolution': '2560x1440',
            'format': 'png'
        },
        'prompts': [
            {
                'name': 'hero-bg-network',
                'prompt': f"Ultra-modern abstract digital network background, flowing data streams and glowing nodes, color palette of bright blue {BRAND_COLORS['blue']} and cyan {BRAND_COLORS['cyan']} on dark charcoal {BRAND_COLORS['charcoal']} background, futuristic technology aesthetic, clean professional design, high resolution 2560x1440, cinematic lighting, depth of field, photorealistic render, trending on artstation",
                'negative': "cluttered, busy, text, logos, people, faces, amateur, low quality"
            },
            {
                'name': 'hero-bg-geometric',
                'prompt': f"Minimalist geometric abstract background, floating 3D shapes and polygons, gradient from bright blue {BRAND_COLORS['blue']} to cyan {BRAND_COLORS['cyan']}, dark charcoal {BRAND_COLORS['charcoal']} accents, modern tech aesthetic, clean composition, professional corporate design, 2560x1440 resolution, studio lighting, sharp focus, ultra detailed",
                'negative': "cluttered, messy, chaotic, text, watermarks, low resolution"
            },
            {
                'name': 'hero-bg-data-viz',
                'prompt': f"Sleek data visualization abstract background, glowing charts and graphs elements, circuit board patterns, color scheme of electric blue {BRAND_COLORS['blue']} and vibrant cyan {BRAND_COLORS['cyan']} on charcoal {BRAND_COLORS['charcoal']} base, futuristic dashboard aesthetic, professional tech design, 2560x1440 high resolution, cinematic composition, photorealistic 3D render",
                'negative': "messy, cluttered, amateur, cartoonish, low quality, text"
            },
            {
                'name': 'hero-bg-metallic',
                'prompt': f"Premium metallic technology background, brushed metal texture with blue {BRAND_COLORS['blue']} and cyan {BRAND_COLORS['cyan']} lighting effects, dark charcoal {BRAND_COLORS['charcoal']} base, abstract tech patterns, sophisticated modern design, enterprise-grade aesthetic, 2560x1440 resolution, professional studio lighting, ultra sharp, photorealistic",
                'negative': "rusty, old, vintage, cluttered, low quality, amateur"
            },
            {
                'name': 'hero-bg-particles',
                'prompt': f"Dynamic particle flow abstract background, glowing particles in motion, energy streams in bright blue {BRAND_COLORS['blue']} and cyan {BRAND_COLORS['cyan']} colors, dark charcoal {BRAND_COLORS['charcoal']} background, cutting-edge technology aesthetic, clean modern composition, 2560x1440 high resolution, volumetric lighting, photorealistic render, professional grade",
                'negative': "static, boring, cluttered, messy, text, low resolution"
            }
        ]
    },
    'portfolio_mockups': {
        'output_dir': BASE_DIR / 'portfolio',
        'specs': {
            'resolution': '1920x1080',
            'format': 'png'
        },
        'prompts': [
            {
                'name': 'portfolio-opportunity-bot-dashboard',
                'prompt': f"Modern AI chatbot dashboard interface mockup, dark theme UI with blue {BRAND_COLORS['blue']} and cyan {BRAND_COLORS['cyan']} accent colors, conversation threads, analytics graphs, clean professional design, realistic software interface, high detail, flat design with depth, 1920x1080 resolution, professional UI/UX design",
                'negative': "cluttered, amateur, outdated, low quality, blurry"
            },
            {
                'name': 'portfolio-opportunity-bot-chat',
                'prompt': f"Sleek AI chat interface mockup, modern messaging UI with blue {BRAND_COLORS['blue']} and cyan {BRAND_COLORS['cyan']} highlights, chatbot conversation bubbles, typing indicators, dark charcoal {BRAND_COLORS['charcoal']} background, professional SaaS design, clean layout, 1920x1080 resolution, high fidelity mockup, modern UI design",
                'negative': "messy, cluttered, old-fashioned, low quality, amateur"
            },
            {
                'name': 'portfolio-spiritatlas-profile',
                'prompt': f"Premium mobile app interface mockup on iPhone 15 Pro, spiritual wellness app, profile screen with meditation stats, blue {BRAND_COLORS['blue']} and cyan {BRAND_COLORS['cyan']} color scheme, modern iOS design, clean minimalist UI, realistic phone mockup, professional app design, 1600x1200 resolution, studio lighting on device",
                'negative': "cluttered, amateur, outdated phone, low quality, messy",
                'resolution': '1600x1200'
            },
            {
                'name': 'portfolio-spiritatlas-meditation',
                'prompt': f"Beautiful mobile meditation app interface on modern smartphone, guided meditation screen with wave animations, calming blue {BRAND_COLORS['blue']} gradients, cyan {BRAND_COLORS['cyan']} accents, peaceful design aesthetic, professional UI/UX, realistic phone mockup, 1600x1200 resolution, premium app design",
                'negative': "cluttered, chaotic, amateur, low quality, unrealistic",
                'resolution': '1600x1200'
            },
            {
                'name': 'portfolio-analytics-dashboard',
                'prompt': f"Professional analytics dashboard interface, modern data visualization, charts and graphs in blue {BRAND_COLORS['blue']} and cyan {BRAND_COLORS['cyan']} colors, dark theme with charcoal {BRAND_COLORS['charcoal']} background, clean layout, enterprise-grade UI design, 1920x1080 resolution, high detail, realistic software interface, professional design",
                'negative': "cluttered, messy, amateur, outdated, low quality"
            },
            {
                'name': 'portfolio-cloud-architecture',
                'prompt': f"Modern cloud architecture diagram visualization, AWS/Azure infrastructure, isometric 3D elements, blue {BRAND_COLORS['blue']} and cyan {BRAND_COLORS['cyan']} color scheme, clean professional infographic style, dark charcoal {BRAND_COLORS['charcoal']} background, technical but accessible, 1920x1080 resolution, high quality illustration",
                'negative': "cluttered, messy, confusing, amateur, low quality"
            },
            {
                'name': 'portfolio-ecommerce-platform',
                'prompt': f"Sleek e-commerce platform dashboard mockup, modern admin interface, product management screen, sales analytics, blue {BRAND_COLORS['blue']} and cyan {BRAND_COLORS['cyan']} accents, professional SaaS design, clean layout, realistic UI, 1920x1080 resolution, high fidelity mockup, enterprise-grade design",
                'negative': "cluttered, outdated, amateur, messy, low quality"
            },
            {
                'name': 'portfolio-api-docs',
                'prompt': f"Modern API documentation portal interface, developer-focused design, code snippets with syntax highlighting, blue {BRAND_COLORS['blue']} and cyan {BRAND_COLORS['cyan']} theme, dark mode interface, professional tech documentation layout, 1920x1080 resolution, clean typography, high quality UI design",
                'negative': "cluttered, confusing, amateur, outdated, low quality"
            }
        ]
    },
    'service_icons': {
        'output_dir': BASE_DIR / 'icons',
        'specs': {
            'resolution': '512x512',
            'format': 'png'
        },
        'prompts': [
            {
                'name': 'icon-custom-dev',
                'prompt': f"Modern icon for custom software development, code brackets and gear symbol, bright blue {BRAND_COLORS['blue']} and cyan {BRAND_COLORS['cyan']} gradient, flat design with subtle depth, clean professional style, 512x512 resolution, transparent background, crisp edges, vector-style illustration",
                'negative': "3D, realistic, cluttered, messy, low quality, blurry"
            },
            {
                'name': 'icon-ai-ml',
                'prompt': f"Sleek AI and machine learning icon, neural network nodes connected, blue {BRAND_COLORS['blue']} to cyan {BRAND_COLORS['cyan']} gradient, modern flat design, professional tech icon style, 512x512 resolution, transparent background, clean geometric shapes, high quality vector-style",
                'negative': "3D, photorealistic, cluttered, amateur, low quality"
            },
            {
                'name': 'icon-cloud-architecture',
                'prompt': f"Modern cloud computing icon, stylized cloud with server nodes, bright blue {BRAND_COLORS['blue']} and cyan {BRAND_COLORS['cyan']} colors, flat design with depth, professional tech icon, 512x512 resolution, transparent background, clean minimalist style, crisp vector illustration",
                'negative': "realistic, 3D, cluttered, outdated, low quality"
            },
            {
                'name': 'icon-data-engineering',
                'prompt': f"Professional data engineering icon, database cylinders with data flow arrows, blue {BRAND_COLORS['blue']} and cyan {BRAND_COLORS['cyan']} gradient, modern flat icon design, clean tech aesthetic, 512x512 resolution, transparent background, geometric precision, high quality vector-style",
                'negative': "3D, photorealistic, messy, amateur, low quality"
            },
            {
                'name': 'icon-security',
                'prompt': f"Modern cybersecurity icon, shield with lock and circuit elements, bright blue {BRAND_COLORS['blue']} to cyan {BRAND_COLORS['cyan']} gradient, flat design with subtle depth, professional security icon style, 512x512 resolution, transparent background, clean geometric design, vector illustration quality",
                'negative': "3D, realistic, cluttered, outdated, low quality"
            },
            {
                'name': 'icon-mobile-dev',
                'prompt': f"Sleek mobile development icon, smartphone with code elements, blue {BRAND_COLORS['blue']} and cyan {BRAND_COLORS['cyan']} colors, modern flat icon design, professional tech style, 512x512 resolution, transparent background, clean minimalist aesthetic, crisp vector-style illustration",
                'negative': "3D, photorealistic, messy, amateur, low quality, blurry"
            }
        ]
    },
    'section_dividers': {
        'output_dir': BASE_DIR / 'backgrounds',
        'specs': {
            'resolution': '1920x400',
            'format': 'png'
        },
        'prompts': [
            {
                'name': 'divider-gradient-wave',
                'prompt': f"Subtle abstract wave gradient background, smooth flowing curves, blue {BRAND_COLORS['blue']} to cyan {BRAND_COLORS['cyan']} to charcoal {BRAND_COLORS['charcoal']} gradient, minimal professional design, 1920x400 banner resolution, clean modern aesthetic, high quality render",
                'negative': "busy, cluttered, distracting, harsh, low quality"
            },
            {
                'name': 'divider-metallic-lines',
                'prompt': f"Sleek metallic horizontal lines pattern, subtle tech aesthetic, blue {BRAND_COLORS['blue']} and cyan {BRAND_COLORS['cyan']} highlights on charcoal {BRAND_COLORS['charcoal']} base, minimal professional background, 1920x400 resolution, clean modern design, high quality",
                'negative': "cluttered, messy, distracting, amateur, low quality"
            },
            {
                'name': 'divider-particle-scatter',
                'prompt': f"Minimal particle scatter background, subtle glowing dots, blue {BRAND_COLORS['blue']} and cyan {BRAND_COLORS['cyan']} particles on dark charcoal {BRAND_COLORS['charcoal']}, professional tech aesthetic, non-distracting, 1920x400 banner, clean modern design, high quality render",
                'negative': "busy, cluttered, chaotic, harsh, low quality"
            },
            {
                'name': 'divider-circuit-pattern',
                'prompt': f"Subtle circuit board pattern background, minimal tech lines, blue {BRAND_COLORS['blue']} and cyan {BRAND_COLORS['cyan']} accents on charcoal {BRAND_COLORS['charcoal']}, professional subtle design, 1920x400 resolution, clean modern aesthetic, non-distracting, high quality",
                'negative': "cluttered, busy, messy, harsh, low quality"
            }
        ]
    }
}


class AssetGenerator:
    """Generate AI assets using Flux 2 via fal.ai"""

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv('FAL_KEY')
        if not self.api_key:
            raise ValueError("FAL_KEY not found in environment variables")

        os.environ['FAL_KEY'] = self.api_key
        self.stats = {
            'generated': 0,
            'failed': 0,
            'skipped': 0
        }

    def parse_resolution(self, resolution: str) -> Dict[str, int]:
        """Parse resolution string to width/height dict"""
        width, height = map(int, resolution.split('x'))
        return {'width': width, 'height': height}

    def generate_image(
        self,
        prompt: str,
        negative_prompt: str,
        resolution: str = '1024x1024',
        model: str = 'fal-ai/flux-pro/v1.1'
    ) -> Optional[bytes]:
        """Generate image using Flux 2 API"""

        try:
            size = self.parse_resolution(resolution)

            print(f"  Generating with {model}...")
            print(f"  Resolution: {resolution}")

            result = fal_client.subscribe(
                model,
                arguments={
                    "prompt": prompt,
                    "negative_prompt": negative_prompt,
                    "image_size": {
                        "width": size['width'],
                        "height": size['height']
                    },
                    "num_inference_steps": 28,
                    "guidance_scale": 3.5,
                    "num_images": 1,
                    "enable_safety_checker": True,
                    "output_format": "png"
                }
            )

            # Download the generated image
            if result and 'images' in result and len(result['images']) > 0:
                image_url = result['images'][0]['url']
                response = requests.get(image_url)
                response.raise_for_status()
                return response.content
            else:
                print("  ⚠ No image returned from API")
                return None

        except Exception as e:
            print(f"  ❌ Error generating image: {e}")
            return None

    def save_image(self, image_data: bytes, output_path: Path) -> bool:
        """Save image data to file"""
        try:
            output_path.parent.mkdir(parents=True, exist_ok=True)

            # Open and save with PIL for consistency
            img = Image.open(BytesIO(image_data))
            img.save(output_path, 'PNG', optimize=True)

            file_size = output_path.stat().st_size / 1024  # KB
            print(f"  ✓ Saved: {output_path.name} ({file_size:.1f} KB)")
            return True

        except Exception as e:
            print(f"  ❌ Error saving image: {e}")
            return False

    def generate_asset_category(
        self,
        category_name: str,
        category_data: Dict,
        skip_existing: bool = True
    ):
        """Generate all assets in a category"""

        print(f"\n{'='*60}")
        print(f"Generating: {category_name.upper().replace('_', ' ')}")
        print(f"{'='*60}")

        output_dir = category_data['output_dir']
        default_resolution = category_data['specs']['resolution']
        prompts = category_data['prompts']

        print(f"Output directory: {output_dir}")
        print(f"Assets to generate: {len(prompts)}")

        for i, asset_spec in enumerate(prompts, 1):
            name = asset_spec['name']
            output_path = output_dir / f"{name}.png"

            print(f"\n[{i}/{len(prompts)}] {name}")

            # Check if already exists
            if skip_existing and output_path.exists():
                print(f"  ⊘ Skipping (already exists)")
                self.stats['skipped'] += 1
                continue

            # Get resolution (use custom if specified)
            resolution = asset_spec.get('resolution', default_resolution)

            # Generate image
            image_data = self.generate_image(
                prompt=asset_spec['prompt'],
                negative_prompt=asset_spec['negative'],
                resolution=resolution
            )

            if image_data:
                if self.save_image(image_data, output_path):
                    self.stats['generated'] += 1
                else:
                    self.stats['failed'] += 1
            else:
                self.stats['failed'] += 1

            # Rate limiting - be nice to the API
            time.sleep(2)

    def generate_all_assets(self, skip_existing: bool = True, categories: Optional[List[str]] = None):
        """Generate all assets or specific categories"""

        print("\n" + "="*60)
        print("ISN.BIZ AI ASSET GENERATOR")
        print("="*60)
        print(f"Brand Colors: Blue {BRAND_COLORS['blue']}, Cyan {BRAND_COLORS['cyan']}, Charcoal {BRAND_COLORS['charcoal']}")
        print(f"Output base: {BASE_DIR}")
        print("="*60)

        # Filter categories if specified
        categories_to_generate = ASSETS
        if categories:
            categories_to_generate = {k: v for k, v in ASSETS.items() if k in categories}

        # Generate each category
        for category_name, category_data in categories_to_generate.items():
            self.generate_asset_category(category_name, category_data, skip_existing)

        # Print summary
        self.print_summary()

    def print_summary(self):
        """Print generation summary"""
        print("\n" + "="*60)
        print("GENERATION SUMMARY")
        print("="*60)
        print(f"✓ Generated: {self.stats['generated']}")
        print(f"⊘ Skipped: {self.stats['skipped']}")
        print(f"❌ Failed: {self.stats['failed']}")
        print(f"Total: {sum(self.stats.values())}")
        print("="*60)


def main():
    """Main entry point"""
    import argparse

    parser = argparse.ArgumentParser(description='Generate AI assets for ISN.BIZ website')
    parser.add_argument('--api-key', help='fal.ai API key (or set FAL_KEY env var)')
    parser.add_argument('--categories', nargs='+',
                       choices=['hero_backgrounds', 'portfolio_mockups', 'service_icons', 'section_dividers'],
                       help='Specific categories to generate (default: all)')
    parser.add_argument('--overwrite', action='store_true',
                       help='Overwrite existing files (default: skip)')
    parser.add_argument('--test', action='store_true',
                       help='Test mode - generate only first asset of each category')

    args = parser.parse_args()

    try:
        generator = AssetGenerator(api_key=args.api_key)

        if args.test:
            print("\n🧪 TEST MODE - Generating first asset from each category\n")
            # Modify ASSETS to only include first prompt
            for category in ASSETS.values():
                category['prompts'] = [category['prompts'][0]]

        generator.generate_all_assets(
            skip_existing=not args.overwrite,
            categories=args.categories
        )

    except ValueError as e:
        print(f"\n❌ Error: {e}")
        print("\nPlease set your fal.ai API key:")
        print("  export FAL_KEY='your-api-key'")
        print("Or pass via --api-key argument")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n⚠ Generation interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
