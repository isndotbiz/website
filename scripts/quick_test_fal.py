#!/usr/bin/env python3
"""
Quick test script to verify fal.ai API key is working correctly.
This generates a single test image to confirm authentication.
"""

import os
import sys
from pathlib import Path

try:
    import fal_client as fal
    import requests
except ImportError:
    print("ERROR: Required packages not installed.")
    print("\nInstall them with:")
    print("  source venv_fal/bin/activate")
    print("  pip install fal-client requests")
    sys.exit(1)

# Check API key
FAL_API_KEY = os.environ.get("FAL_KEY")
if not FAL_API_KEY:
    print("="*80)
    print("ERROR: FAL_KEY environment variable not set!")
    print("="*80)
    print("\nThe value 'yfmv5bml45cw5jv5yf4dstk3py' is a 1Password item ID, not the API key.")
    print("\nTo get your actual API key:")
    print("  1. Open 1Password")
    print("  2. Find the 'FAL API Key' entry")
    print("  3. Copy the actual API key value (not the item ID)")
    print("  4. Set it as an environment variable:")
    print("\n     export FAL_KEY='your-actual-api-key-here'")
    print("\nThen run this script again.")
    print("="*80)
    sys.exit(1)

OUTPUT_DIR = Path("/mnt/d/workspace/ISNBIZ_Files/assets/test-samples")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def main():
    print("="*80)
    print("FAL.AI API KEY VERIFICATION TEST")
    print("="*80)
    print(f"\nAPI Key detected (first 10 chars): {FAL_API_KEY[:10]}...")
    print(f"Key length: {len(FAL_API_KEY)} characters")
    print(f"Output directory: {OUTPUT_DIR}")
    print("\nAttempting to generate a test image...")
    print("-"*80)

    try:
        # Simple test with nano-banana-pro (fastest model)
        handler = fal.submit(
            "fal-ai/nano-banana-pro",
            arguments={
                "prompt": "A simple test image: a blue geometric shape on white background",
                "num_images": 1,
                "aspect_ratio": "1:1",
                "output_format": "png",
                "resolution": "1K"
            }
        )

        print("Request submitted successfully! Waiting for result...")
        result = handler.get()

        if "images" in result and len(result["images"]) > 0:
            image_url = result["images"][0]["url"]
            output_file = OUTPUT_DIR / "api_test_success.png"

            print(f"\nSuccess! Image generated: {image_url}")
            print(f"Downloading to: {output_file}")

            response = requests.get(image_url)
            if response.status_code == 200:
                with open(output_file, 'wb') as f:
                    f.write(response.content)

                print("\n" + "="*80)
                print("API KEY VERIFICATION: SUCCESS!")
                print("="*80)
                print(f"\nTest image saved to: {output_file}")
                print("\nYour API key is working correctly!")
                print("You can now run the full test suite:")
                print("  python scripts/test_fal_models_v2.py")
                print("="*80)
                return 0
            else:
                print(f"\nWarning: Could not download image (status {response.status_code})")
                print("But the API call succeeded, so your key is valid!")
                return 0
        else:
            print("\nWarning: Unexpected response format")
            print(f"Response: {result}")
            return 1

    except Exception as e:
        print("\n" + "="*80)
        print("API KEY VERIFICATION: FAILED!")
        print("="*80)
        print(f"\nError: {str(e)}")
        print("\nPossible reasons:")
        print("  1. The API key is incorrect")
        print("  2. You're using the 1Password item ID instead of the actual key")
        print("  3. The API key has expired or been revoked")
        print("  4. Network connectivity issues")
        print("\nPlease verify your API key and try again.")
        print("="*80)
        return 1

if __name__ == "__main__":
    sys.exit(main())
