#!/usr/bin/env python3
"""Create responsive variants of portfolio images"""

from PIL import Image
from pathlib import Path

INPUT_DIR = Path("D:/workspace/ISNBIZ_Files/assets/premium_v3/portfolio")

# Images to process
IMAGES = [
    "cli_template.webp",
    "comfyui_wan.webp",
    "gedcom_processing.webp"
]

# Responsive sizes
SIZES = {
    "desktop": (1536, 1024),  # Original size
    "tablet": (1024, 683),    # 2/3 scale
    "mobile": (800, 533)      # ~1/2 scale
}

print("Creating responsive variants...\n")

for filename in IMAGES:
    source = INPUT_DIR / filename

    if not source.exists():
        print(f"ERROR: {filename} not found")
        continue

    print(f"Processing: {filename}")

    # Load original
    img = Image.open(source)
    print(f"  Original: {img.size[0]}x{img.size[1]} ({source.stat().st_size / 1024:.1f} KB)")

    for variant, size in SIZES.items():
        # Create filename
        base = filename.replace('.webp', '')
        output = INPUT_DIR / f"{base}_{variant}.webp"

        # Resize
        resized = img.resize(size, Image.Resampling.LANCZOS)

        # Save with optimization
        resized.save(output, 'WEBP', quality=85, method=6)

        size_kb = output.stat().st_size / 1024
        print(f"    {variant}: {size[0]}x{size[1]} ({size_kb:.1f} KB) -> {output.name}")

    print()

print("Complete!")
print("\nAll variants ready for S3 upload.")
