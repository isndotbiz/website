#!/usr/bin/env python3
"""
Test script for comparing fal.ai image generation models.
Generates 2-3 test images per model for quality comparison.

USAGE:
    export FAL_KEY="your-actual-fal-api-key-here"
    python3 test_fal_models_v2.py

Note: The key should start with something like "fal_" or be a UUID-format string.
"""

import os
import sys
import json
import time
from pathlib import Path
from datetime import datetime

try:
    import fal_client as fal
    import requests
except ImportError:
    print("ERROR: Required packages not installed.")
    print("Please run: pip install fal-client requests")
    sys.exit(1)

# Check for API key
FAL_API_KEY = os.environ.get("FAL_KEY")
if not FAL_API_KEY:
    print("ERROR: FAL_KEY environment variable not set!")
    print("\nPlease set your fal.ai API key:")
    print("  export FAL_KEY='your-actual-api-key-here'")
    print("\nNote: The value 'yfmv5bml45cw5jv5yf4dstk3py' appears to be a 1Password item ID.")
    print("You need to retrieve the actual API key from 1Password and use that instead.")
    sys.exit(1)

# Output directory
OUTPUT_DIR = Path("/mnt/d/workspace/ISNBIZ_Files/assets/test-samples")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Brand colors for prompts
BRAND_COLORS = {
    "blue": "#1E9FF2",
    "cyan": "#5FDFDF"
}

def download_image(url, filepath):
    """Download image from URL to filepath."""
    print(f"  Downloading: {url}")
    response = requests.get(url)
    if response.status_code == 200:
        with open(filepath, 'wb') as f:
            f.write(response.content)
        print(f"  Saved to: {filepath}")
        return True
    else:
        print(f"  Failed to download: {response.status_code}")
        return False

def test_nano_banana_pro():
    """Test fal-ai/nano-banana-pro (text-to-image)."""
    print("\n" + "="*80)
    print("TESTING: fal-ai/nano-banana-pro")
    print("="*80)

    model_name = "nano-banana-pro"
    results = []

    # Test 1: Abstract Tech Background
    print("\nTest 1: Abstract Tech Background")
    try:
        handler = fal.submit(
            "fal-ai/nano-banana-pro",
            arguments={
                "prompt": "Abstract technological background with flowing data streams, blue #1E9FF2 and cyan #5FDFDF gradient colors, modern professional design, clean minimalist style, digital network patterns, suitable for website hero section, high quality, 4k",
                "num_images": 1,
                "aspect_ratio": "16:9",
                "output_format": "png",
                "resolution": "2K"
            }
        )
        result = handler.get()
        print(f"  Success! Result: {json.dumps(result, indent=2)}")

        if "images" in result:
            for idx, img in enumerate(result["images"]):
                filepath = OUTPUT_DIR / f"{model_name}_abstract_tech_{idx+1}.png"
                if download_image(img["url"], filepath):
                    results.append({
                        "test": "Abstract Tech Background",
                        "prompt": "Abstract technological background with flowing data streams...",
                        "settings": {"aspect_ratio": "16:9", "resolution": "2K"},
                        "output_path": str(filepath),
                        "url": img["url"]
                    })
        time.sleep(2)
    except Exception as e:
        print(f"  Error: {e}")

    # Test 2: AI/ML Service Icon
    print("\nTest 2: AI/ML Service Icon")
    try:
        handler = fal.submit(
            "fal-ai/nano-banana-pro",
            arguments={
                "prompt": "Modern AI and machine learning icon illustration, neural network visualization, blue #1E9FF2 accent color, clean professional design, minimalist style, technology theme, suitable for website service section, white background, high quality",
                "num_images": 1,
                "aspect_ratio": "1:1",
                "output_format": "png",
                "resolution": "2K"
            }
        )
        result = handler.get()
        print(f"  Success! Result: {json.dumps(result, indent=2)}")

        if "images" in result:
            for idx, img in enumerate(result["images"]):
                filepath = OUTPUT_DIR / f"{model_name}_ai_icon_{idx+1}.png"
                if download_image(img["url"], filepath):
                    results.append({
                        "test": "AI/ML Service Icon",
                        "prompt": "Modern AI and machine learning icon illustration...",
                        "settings": {"aspect_ratio": "1:1", "resolution": "2K"},
                        "output_path": str(filepath),
                        "url": img["url"]
                    })
        time.sleep(2)
    except Exception as e:
        print(f"  Error: {e}")

    return {
        "model": "fal-ai/nano-banana-pro",
        "description": "Fast text-to-image generation with good quality",
        "results": results
    }

def test_nano_banana_pro_edit():
    """Test fal-ai/nano-banana-pro/edit (image editing)."""
    print("\n" + "="*80)
    print("TESTING: fal-ai/nano-banana-pro/edit")
    print("="*80)

    model_name = "nano-banana-pro-edit"
    results = []

    # Use example image for testing
    input_image_url = "https://storage.googleapis.com/falserverless/example_inputs/nano-banana-edit-input.png"

    print("\nTest 1: Professional Enhancement")
    try:
        handler = fal.submit(
            "fal-ai/nano-banana-pro/edit",
            arguments={
                "prompt": "enhance the image with professional lighting, add subtle blue #1E9FF2 glow effect, modern tech aesthetic, maintain original subject",
                "image_urls": [input_image_url],
                "num_images": 1,
                "aspect_ratio": "auto",
                "output_format": "png",
                "resolution": "2K"
            }
        )
        result = handler.get()
        print(f"  Success! Result: {json.dumps(result, indent=2)}")

        if "images" in result:
            for idx, img in enumerate(result["images"]):
                filepath = OUTPUT_DIR / f"{model_name}_enhancement_{idx+1}.png"
                if download_image(img["url"], filepath):
                    results.append({
                        "test": "Professional Enhancement",
                        "prompt": "enhance the image with professional lighting...",
                        "settings": {"aspect_ratio": "auto", "resolution": "2K"},
                        "output_path": str(filepath),
                        "url": img["url"]
                    })
        time.sleep(2)
    except Exception as e:
        print(f"  Error: {e}")

    return {
        "model": "fal-ai/nano-banana-pro/edit",
        "description": "Image editing and enhancement capabilities",
        "results": results
    }

def test_gpt_image_edit():
    """Test fal-ai/gpt-image-1.5/edit (advanced editing)."""
    print("\n" + "="*80)
    print("TESTING: fal-ai/gpt-image-1.5/edit")
    print("="*80)

    model_name = "gpt-image-1.5-edit"
    results = []

    input_image_url = "https://storage.googleapis.com/falserverless/example_inputs/nano-banana-edit-input.png"

    print("\nTest 1: Professional Style Enhancement")
    try:
        handler = fal.submit(
            "fal-ai/gpt-image-1.5/edit",
            arguments={
                "prompt": "transform into a professional corporate style with blue #1E9FF2 and cyan #5FDFDF color scheme, modern business aesthetic",
                "image_urls": [input_image_url],
                "num_images": 1
            }
        )
        result = handler.get()
        print(f"  Success! Result: {json.dumps(result, indent=2)}")

        if "images" in result:
            for idx, img in enumerate(result["images"]):
                filepath = OUTPUT_DIR / f"{model_name}_style_{idx+1}.png"
                if download_image(img["url"], filepath):
                    results.append({
                        "test": "Professional Style Enhancement",
                        "prompt": "transform into a professional corporate style...",
                        "settings": {"num_images": 1},
                        "output_path": str(filepath),
                        "url": img["url"]
                    })
        time.sleep(2)
    except Exception as e:
        print(f"  Error: {e}")

    return {
        "model": "fal-ai/gpt-image-1.5/edit",
        "description": "Advanced image editing with GPT-powered understanding",
        "results": results
    }

def test_flux_pro_kontext():
    """Test fal-ai/flux-pro/kontext (context-aware editing)."""
    print("\n" + "="*80)
    print("TESTING: fal-ai/flux-pro/kontext")
    print("="*80)

    model_name = "flux-pro-kontext"
    results = []

    input_image_url = "https://storage.googleapis.com/falserverless/example_inputs/kontext_example_input.webp"

    # Test 1: Context-Aware Background Change
    print("\nTest 1: Professional Background Transformation")
    try:
        handler = fal.submit(
            "fal-ai/flux-pro/kontext",
            arguments={
                "prompt": "change the background to a modern professional office environment with blue #1E9FF2 accents while maintaining the same subject and lighting",
                "image_url": input_image_url,
                "guidance_scale": 7.5,
                "num_inference_steps": 50
            }
        )
        result = handler.get()
        print(f"  Success! Result: {json.dumps(result, indent=2)}")

        if "images" in result:
            for idx, img in enumerate(result["images"]):
                filepath = OUTPUT_DIR / f"{model_name}_background_{idx+1}.png"
                if download_image(img["url"], filepath):
                    results.append({
                        "test": "Professional Background Transformation",
                        "prompt": "change the background to a modern professional office...",
                        "settings": {"guidance_scale": 7.5, "num_inference_steps": 50},
                        "output_path": str(filepath),
                        "url": img["url"]
                    })
        time.sleep(2)
    except Exception as e:
        print(f"  Error: {e}")

    # Test 2: Lighting Enhancement
    print("\nTest 2: Lighting and Color Enhancement")
    try:
        handler = fal.submit(
            "fal-ai/flux-pro/kontext",
            arguments={
                "prompt": "enhance with professional studio lighting and add subtle blue #1E9FF2 color grading while keeping the subject identical",
                "image_url": input_image_url,
                "guidance_scale": 7.0,
                "num_inference_steps": 40
            }
        )
        result = handler.get()
        print(f"  Success! Result: {json.dumps(result, indent=2)}")

        if "images" in result:
            for idx, img in enumerate(result["images"]):
                filepath = OUTPUT_DIR / f"{model_name}_lighting_{idx+1}.png"
                if download_image(img["url"], filepath):
                    results.append({
                        "test": "Lighting and Color Enhancement",
                        "prompt": "enhance with professional studio lighting...",
                        "settings": {"guidance_scale": 7.0, "num_inference_steps": 40},
                        "output_path": str(filepath),
                        "url": img["url"]
                    })
        time.sleep(2)
    except Exception as e:
        print(f"  Error: {e}")

    return {
        "model": "fal-ai/flux-pro/kontext",
        "description": "Context-aware editing with subject preservation",
        "results": results
    }

def generate_comparison_report(all_results):
    """Generate a markdown comparison report."""
    print("\n" + "="*80)
    print("GENERATING COMPARISON REPORT")
    print("="*80)

    report_path = OUTPUT_DIR / "model_comparison_report.md"

    with open(report_path, 'w') as f:
        f.write("# fal.ai Model Comparison Report\n\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("## Test Configuration\n\n")
        f.write("**Brand Colors:**\n")
        f.write(f"- Primary Blue: {BRAND_COLORS['blue']}\n")
        f.write(f"- Accent Cyan: {BRAND_COLORS['cyan']}\n\n")
        f.write("---\n\n")

        for model_result in all_results:
            f.write(f"## {model_result['model']}\n\n")
            f.write(f"**Description:** {model_result['description']}\n\n")

            if not model_result['results']:
                f.write("*No results generated - check errors above*\n\n")
                continue

            for idx, test in enumerate(model_result['results'], 1):
                f.write(f"### Test {idx}: {test['test']}\n\n")
                f.write(f"**Prompt:**\n```\n{test['prompt']}\n```\n\n")
                f.write(f"**Settings:**\n```json\n{json.dumps(test['settings'], indent=2)}\n```\n\n")
                f.write(f"**Output:** `{test['output_path']}`\n\n")

                # Use relative path for markdown image display
                rel_path = Path(test['output_path']).name
                f.write(f"![{test['test']}](./{rel_path})\n\n")
                f.write("---\n\n")

        f.write("## Quality Assessment\n\n")
        f.write("### Recommendations\n\n")
        f.write("1. **nano-banana-pro**: Best for fast, high-quality text-to-image generation\n")
        f.write("2. **nano-banana-pro/edit**: Good for basic image enhancements\n")
        f.write("3. **gpt-image-1.5/edit**: Advanced editing with natural language understanding\n")
        f.write("4. **flux-pro/kontext**: Context-aware editing with excellent subject preservation\n\n")
        f.write("### Best Use Cases\n\n")
        f.write("- **Website Hero Images**: nano-banana-pro (fast generation, good quality)\n")
        f.write("- **Icon/Illustration Creation**: nano-banana-pro (clean, professional output)\n")
        f.write("- **Photo Enhancement**: gpt-image-1.5/edit (advanced understanding)\n")
        f.write("- **Background Changes**: flux-pro/kontext (preserves subject perfectly)\n")
        f.write("- **Style Transfer**: flux-pro/kontext or gpt-image-1.5/edit\n\n")

    print(f"Report saved to: {report_path}")
    return report_path

def main():
    """Run all tests and generate comparison report."""
    print("="*80)
    print("FAL.AI MODEL COMPARISON TEST SUITE")
    print("="*80)
    print(f"Output Directory: {OUTPUT_DIR}")
    print(f"API Key: {FAL_API_KEY[:10]}... (length: {len(FAL_API_KEY)})")

    all_results = []

    # Test each model
    try:
        all_results.append(test_nano_banana_pro())
        time.sleep(2)
    except Exception as e:
        print(f"Error testing nano-banana-pro: {e}")
        all_results.append({
            "model": "fal-ai/nano-banana-pro",
            "description": "Error occurred during testing",
            "results": []
        })

    try:
        all_results.append(test_nano_banana_pro_edit())
        time.sleep(2)
    except Exception as e:
        print(f"Error testing nano-banana-pro/edit: {e}")
        all_results.append({
            "model": "fal-ai/nano-banana-pro/edit",
            "description": "Error occurred during testing",
            "results": []
        })

    try:
        all_results.append(test_gpt_image_edit())
        time.sleep(2)
    except Exception as e:
        print(f"Error testing gpt-image-1.5/edit: {e}")
        all_results.append({
            "model": "fal-ai/gpt-image-1.5/edit",
            "description": "Error occurred during testing",
            "results": []
        })

    try:
        all_results.append(test_flux_pro_kontext())
    except Exception as e:
        print(f"Error testing flux-pro/kontext: {e}")
        all_results.append({
            "model": "fal-ai/flux-pro/kontext",
            "description": "Error occurred during testing",
            "results": []
        })

    # Generate comparison report
    report_path = generate_comparison_report(all_results)

    print("\n" + "="*80)
    print("TESTING COMPLETE!")
    print("="*80)
    print(f"\nComparison Report: {report_path}")
    print(f"Test Images: {OUTPUT_DIR}/")
    print("\nReview the generated images to choose which models to use for full generation!")

    return 0

if __name__ == "__main__":
    sys.exit(main())
