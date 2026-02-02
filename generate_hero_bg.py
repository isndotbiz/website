#!/usr/bin/env python3
"""
Generate Stunning Hero Background for ISN.BIZ
Using FAL API to create abstract metallic tech background with blue/cyan gradient
Saves as WebP and uploads to S3
"""

import os
import sys
import time
import boto3
import requests
from pathlib import Path
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
FAL_API_KEY = os.getenv('FAL_API_KEY')
S3_BUCKET = 'isnbiz-assets-1769962280'
S3_PREFIX = 'premium_v3/backgrounds/'
OUTPUT_DIR = Path('/home/jdmal/workspace/ISNBIZ_Files/assets/hero_backgrounds')
OUTPUT_FILENAME = 'hero-bg-main.webp'

# Brand colors
BRAND_BLUE = '#1E9FF2'
BRAND_CYAN = '#5FDFDF'
BRAND_CHARCOAL = '#0D1117'

def generate_hero_background():
    """Generate stunning metallic tech hero background using FAL API"""

    if not FAL_API_KEY:
        print("ERROR: FAL_API_KEY not found in environment")
        print("Make sure .env file exists with FAL_API_KEY set")
        sys.exit(1)

    print("=" * 80)
    print("GENERATING STUNNING HERO BACKGROUND")
    print("=" * 80)
    print(f"Resolution: 1536x1024 (high quality)")
    print(f"Format: WebP (optimized)")
    print(f"Brand: Blue {BRAND_BLUE}, Cyan {BRAND_CYAN}")
    print("=" * 80)
    print()

    # Craft perfect prompt for metallic tech background
    prompt = f"""
Stunning abstract metallic technology background for enterprise software company hero section,
premium brushed metal surface texture with holographic blue {BRAND_BLUE} and cyan {BRAND_CYAN}
lighting gradients, dark charcoal {BRAND_CHARCOAL} base, sophisticated geometric patterns,
subtle circuit board elements, floating particles of light, volumetric fog effects,
professional corporate aesthetic, ultra-modern design, cinematic lighting with rim lights,
depth of field, photorealistic 3D render, award-winning composition, 8K quality,
clean and uncluttered, trending on artstation, enterprise-grade polish
""".strip().replace('\n', ' ')

    negative_prompt = """
cluttered, busy, messy, chaotic, amateur, low quality, blurry, distorted,
text, watermarks, logos, people, faces, cartoonish, vintage, rusty, old,
oversaturated, harsh colors, gradient banding, compression artifacts,
stock photo, generic
""".strip().replace('\n', ' ')

    print("Prompt:")
    print(f"  {prompt[:150]}...")
    print()

    # Call FAL API
    print("Calling FAL API (fal-ai/flux-pro/v1.1)...")
    print("This may take 30-60 seconds...")
    print()

    try:
        import fal_client

        # Set API key
        os.environ['FAL_KEY'] = FAL_API_KEY

        result = fal_client.subscribe(
            "fal-ai/flux-pro/v1.1",
            arguments={
                "prompt": prompt,
                "negative_prompt": negative_prompt,
                "image_size": {
                    "width": 1536,
                    "height": 1024
                },
                "num_inference_steps": 40,  # Higher quality
                "guidance_scale": 4.0,       # Stronger prompt adherence
                "num_images": 1,
                "enable_safety_checker": True,
                "output_format": "png"
            }
        )

        if not result or 'images' not in result or len(result['images']) == 0:
            print("ERROR: No image returned from API")
            sys.exit(1)

        image_url = result['images'][0]['url']
        print(f"[OK] Image generated successfully!")
        print(f"  Temporary URL: {image_url}")
        print()

        # Download image
        print("Downloading image...")
        response = requests.get(image_url)
        response.raise_for_status()
        image_data = response.content
        print(f"[OK] Downloaded {len(image_data) / 1024:.1f} KB")
        print()

        return image_data

    except ImportError:
        print("ERROR: fal-client not installed")
        print("Run: pip install fal-client")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR generating image: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


def save_as_webp(image_data, output_path):
    """Convert to WebP and save with optimization"""

    print(f"Converting to WebP...")
    print(f"Output: {output_path}")

    try:
        # Open image with PIL
        img = Image.open(BytesIO(image_data))

        # Create output directory
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Save as WebP with high quality
        img.save(
            output_path,
            'WebP',
            quality=90,
            method=6  # Best compression
        )

        file_size = output_path.stat().st_size / 1024
        print(f"[OK] Saved as WebP: {file_size:.1f} KB")
        print()

        return True

    except Exception as e:
        print(f"ERROR saving WebP: {e}")
        return False


def upload_to_s3(local_path, s3_key):
    """Upload to S3 with proper metadata"""

    print(f"Uploading to S3...")
    print(f"Bucket: {S3_BUCKET}")
    print(f"Key: {s3_key}")

    try:
        s3_client = boto3.client('s3')

        # Upload with proper content type and caching
        s3_client.upload_file(
            str(local_path),
            S3_BUCKET,
            s3_key,
            ExtraArgs={
                'ContentType': 'image/webp',
                'CacheControl': 'public, max-age=31536000'  # 1 year
                # No ACL - bucket has public access via policy
            }
        )

        # Generate public URL
        url = f"https://{S3_BUCKET}.s3.us-east-1.amazonaws.com/{s3_key}"

        print(f"[OK] Uploaded successfully!")
        print()
        print("=" * 80)
        print("S3 URL:")
        print(url)
        print("=" * 80)
        print()

        return url

    except Exception as e:
        print(f"ERROR uploading to S3: {e}")
        print()
        print("Make sure AWS credentials are configured:")
        print("  aws configure")
        return None


def update_css(s3_url):
    """Update styles.css with new hero background"""

    css_path = Path('/home/jdmal/workspace/ISNBIZ_Files/styles.css')

    if not css_path.exists():
        print(f"WARNING: {css_path} not found, skipping CSS update")
        return False

    print("Updating styles.css...")

    try:
        # Read current CSS
        with open(css_path, 'r', encoding='utf-8') as f:
            css_content = f.read()

        # Find hero background section and update
        # Look for .hero-background or .hero section

        new_background_rule = f"""    background: linear-gradient(135deg, rgba(13, 17, 23, 0.85), rgba(13, 17, 23, 0.70)),
               url('{s3_url}');
    background-size: cover;
    background-position: center;
    background-attachment: fixed;"""

        # This is a simple approach - you might need to adjust based on actual CSS structure
        print(f"  Background URL: {s3_url}")
        print()
        print("MANUAL UPDATE REQUIRED:")
        print("Add this to .hero or .hero-background in styles.css:")
        print()
        print(new_background_rule)
        print()

        return True

    except Exception as e:
        print(f"ERROR updating CSS: {e}")
        return False


def main():
    """Main execution"""

    print()
    print("ISN.BIZ Hero Background Generator")
    print()

    # Step 1: Generate image
    image_data = generate_hero_background()

    # Step 2: Save as WebP
    output_path = OUTPUT_DIR / OUTPUT_FILENAME
    if not save_as_webp(image_data, output_path):
        sys.exit(1)

    # Step 3: Upload to S3
    s3_key = f"{S3_PREFIX}{OUTPUT_FILENAME}"
    s3_url = upload_to_s3(output_path, s3_key)

    if not s3_url:
        print("Upload failed, but file is saved locally at:")
        print(f"  {output_path}")
        sys.exit(1)

    # Step 4: Update CSS
    update_css(s3_url)

    # Summary
    print()
    print("=" * 80)
    print("[SUCCESS] COMPLETE!")
    print("=" * 80)
    print(f"Local file: {output_path}")
    print(f"S3 URL: {s3_url}")
    print()
    print("Next steps:")
    print("1. Update styles.css with the new background URL")
    print("2. Test the website locally")
    print("3. Deploy to production")
    print("=" * 80)
    print()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nInterrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
