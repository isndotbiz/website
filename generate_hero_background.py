#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate Premium Hero Background for ISN.BIZ Website
Uses FAL API to create a stunning metallic technology background
"""

import os
import sys
import json
import time
import requests
from pathlib import Path
from io import BytesIO

# Fix Windows console encoding
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Check dependencies
try:
    import fal_client
    from PIL import Image
    from dotenv import load_dotenv
    import boto3
except ImportError as e:
    print("Missing dependencies. Install with:")
    print("pip install fal-client pillow python-dotenv boto3")
    sys.exit(1)

# Load environment variables
load_dotenv()

# Brand colors
BRAND_COLORS = {
    'blue': '#1E9FF2',
    'cyan': '#5FDFDF',
    'charcoal': '#3F4447'
}

# Output configuration
OUTPUT_DIR = Path(__file__).parent / 'assets' / 'backgrounds'
OUTPUT_FILE = 'hero-background-main.webp'
S3_BUCKET = 'isnbiz-assets-1769962280'
S3_KEY = 'premium_v3/backgrounds/hero-background-main.webp'
S3_REGION = 'us-east-1'

# Hero background prompt
HERO_PROMPT = f"""Premium abstract metallic technology surface background, elegant brushed metal texture with stunning blue {BRAND_COLORS['blue']} and vibrant cyan {BRAND_COLORS['cyan']} gradient lighting effects, sophisticated dark charcoal {BRAND_COLORS['charcoal']} base, modern enterprise professional aesthetic, cutting-edge technology patterns, sleek futuristic design, ultra-premium corporate look, 1920x1080 resolution, cinematic studio lighting, photorealistic render, ultra sharp and detailed, professional grade, trending on artstation, award-winning design"""

NEGATIVE_PROMPT = "amateur, low quality, cluttered, messy, busy, text, logos, watermarks, people, faces, cartoon, outdated, rusty, vintage, dull, flat, boring"


class HeroBackgroundGenerator:
    """Generate and upload hero background"""

    def __init__(self):
        self.fal_api_key = os.getenv('FAL_API_KEY')
        if not self.fal_api_key:
            raise ValueError("FAL_API_KEY not found in .env file")

        os.environ['FAL_KEY'] = self.fal_api_key

        # AWS credentials from environment
        self.aws_access_key = os.getenv('AWS_ACCESS_KEY_ID')
        self.aws_secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')

        if not self.aws_access_key or not self.aws_secret_key:
            print("WARNING: AWS credentials not found - will skip S3 upload")
            self.s3_enabled = False
        else:
            self.s3_enabled = True
            self.s3_client = boto3.client(
                's3',
                aws_access_key_id=self.aws_access_key,
                aws_secret_access_key=self.aws_secret_key,
                region_name=S3_REGION
            )

    def generate_image(self) -> bytes:
        """Generate hero background using FAL API"""

        print("\n" + "="*60)
        print("GENERATING HERO BACKGROUND")
        print("="*60)
        print(f"Model: fal-ai/flux-pro/v1.1")
        print(f"Resolution: 1920x1080")
        print(f"Brand Colors: Blue {BRAND_COLORS['blue']}, Cyan {BRAND_COLORS['cyan']}")
        print("="*60 + "\n")

        try:
            print("[*] Generating premium metallic technology background...")

            result = fal_client.subscribe(
                'fal-ai/flux-pro/v1.1',
                arguments={
                    "prompt": HERO_PROMPT,
                    "negative_prompt": NEGATIVE_PROMPT,
                    "image_size": {
                        "width": 1920,
                        "height": 1080
                    },
                    "num_inference_steps": 50,  # Higher quality
                    "guidance_scale": 7.5,       # Strong prompt adherence
                    "num_images": 1,
                    "enable_safety_checker": True,
                    "output_format": "png"
                }
            )

            # Download the generated image
            if result and 'images' in result and len(result['images']) > 0:
                image_url = result['images'][0]['url']
                print(f"[+] Image generated: {image_url}")

                print("[*] Downloading image...")
                response = requests.get(image_url)
                response.raise_for_status()

                print(f"[+] Downloaded {len(response.content) / 1024:.1f} KB")
                return response.content
            else:
                raise Exception("No image returned from API")

        except Exception as e:
            print(f"[!] Error generating image: {e}")
            raise

    def convert_to_webp(self, image_data: bytes) -> bytes:
        """Convert PNG to WebP format"""

        print("[*] Converting to WebP format...")

        try:
            # Open image
            img = Image.open(BytesIO(image_data))

            # Convert to WebP
            output = BytesIO()
            img.save(output, format='WEBP', quality=95, method=6)
            webp_data = output.getvalue()

            original_size = len(image_data) / 1024
            webp_size = len(webp_data) / 1024
            savings = ((original_size - webp_size) / original_size) * 100

            print(f"[+] Converted: {original_size:.1f}KB -> {webp_size:.1f}KB (saved {savings:.1f}%)")

            return webp_data

        except Exception as e:
            print(f"[!] Error converting to WebP: {e}")
            raise

    def save_locally(self, image_data: bytes) -> Path:
        """Save image locally"""

        print(f"[*] Saving to {OUTPUT_DIR / OUTPUT_FILE}...")

        try:
            # Create output directory
            OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

            # Save file
            output_path = OUTPUT_DIR / OUTPUT_FILE
            output_path.write_bytes(image_data)

            file_size = len(image_data) / 1024
            print(f"[+] Saved locally: {output_path} ({file_size:.1f} KB)")

            return output_path

        except Exception as e:
            print(f"[!] Error saving locally: {e}")
            raise

    def upload_to_s3(self, image_data: bytes) -> str:
        """Upload image to S3"""

        if not self.s3_enabled:
            print("[-] Skipping S3 upload (credentials not configured)")
            return ""

        print(f"[*] Uploading to S3: s3://{S3_BUCKET}/{S3_KEY}...")

        try:
            # Upload to S3
            self.s3_client.put_object(
                Bucket=S3_BUCKET,
                Key=S3_KEY,
                Body=image_data,
                ContentType='image/webp',
                CacheControl='public, max-age=31536000',  # 1 year cache
                ACL='public-read'
            )

            # Generate public URL
            s3_url = f"https://{S3_BUCKET}.s3.{S3_REGION}.amazonaws.com/{S3_KEY}"

            print(f"[+] Uploaded to S3")
            print(f"  URL: {s3_url}")

            return s3_url

        except Exception as e:
            print(f"[!] Error uploading to S3: {e}")
            raise

    def update_html(self, s3_url: str = None):
        """Update index.html with new background"""

        print("\n[*] Updating index.html...")

        try:
            html_path = Path(__file__).parent / 'index.html'

            if not html_path.exists():
                print("[!] index.html not found - skipping update")
                return

            # Read current HTML
            html_content = html_path.read_text(encoding='utf-8')

            # Determine URL to use
            if s3_url:
                background_url = s3_url
                print(f"  Using S3 URL: {s3_url}")
            else:
                background_url = f"assets/backgrounds/{OUTPUT_FILE}"
                print(f"  Using local path: {background_url}")

            # Find and replace hero background CSS
            # Look for .hero or .hero-background style
            import re

            # Pattern to find hero background
            pattern = r'(\.hero(?:-background)?\s*\{[^}]*?background(?:-image)?\s*:\s*)[^;]+(;)'

            # New background style
            new_bg = f'url("{background_url}")'

            # Replace
            updated_html = re.sub(
                pattern,
                r'\1' + new_bg + r'\2',
                html_content
            )

            # If no change, add style to hero section
            if updated_html == html_content:
                print("  No existing hero background found - adding inline style")

                # Add style to hero section
                updated_html = updated_html.replace(
                    '<section class="hero">',
                    f'<section class="hero" style="background-image: url(\'{background_url}\'); background-size: cover; background-position: center;">'
                )

            # Write updated HTML
            html_path.write_text(updated_html, encoding='utf-8')

            print("[+] index.html updated with new hero background")

        except Exception as e:
            print(f"[!] Error updating HTML: {e}")
            # Don't raise - HTML update is optional

    def generate(self):
        """Main generation workflow"""

        try:
            # Generate image
            image_data = self.generate_image()

            # Convert to WebP
            webp_data = self.convert_to_webp(image_data)

            # Save locally
            local_path = self.save_locally(webp_data)

            # Upload to S3
            s3_url = self.upload_to_s3(webp_data)

            # Update HTML
            self.update_html(s3_url if s3_url else None)

            # Summary
            print("\n" + "="*60)
            print("[SUCCESS] HERO BACKGROUND GENERATION COMPLETE")
            print("="*60)
            print(f"Local file: {local_path}")
            if s3_url:
                print(f"S3 URL: {s3_url}")
            print(f"File size: {len(webp_data) / 1024:.1f} KB")
            print("="*60 + "\n")

            print("Your new hero background is ready!")
            print("The first impression is everything - this will wow investors!")

        except Exception as e:
            print(f"\n[!] Generation failed: {e}")
            import traceback
            traceback.print_exc()
            sys.exit(1)


def main():
    """Main entry point"""

    try:
        generator = HeroBackgroundGenerator()
        generator.generate()

    except ValueError as e:
        print(f"\n[!] Configuration error: {e}")
        print("\nPlease ensure .env file contains:")
        print("  FAL_API_KEY=your-fal-api-key")
        print("  AWS_ACCESS_KEY_ID=your-aws-key (optional)")
        print("  AWS_SECRET_ACCESS_KEY=your-aws-secret (optional)")
        sys.exit(1)

    except KeyboardInterrupt:
        print("\n\n[!] Generation interrupted by user")
        sys.exit(1)


if __name__ == '__main__':
    main()
