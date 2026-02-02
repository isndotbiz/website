#!/usr/bin/env python3
"""
Continue generating founder photos - only generates missing ones
"""

import os
import sys
from pathlib import Path

# Add the parent directory to path to import from the main script
sys.path.insert(0, str(Path(__file__).parent))

from generate_founder_photos_candid import (
    FOUNDER_CONFIG, OUTPUT_DIR, generate_scenario_photo, convert_to_webp
)
import time


def main():
    """Continue generation for missing photos"""
    print("\n" + "="*70)
    print("CONTINUING ISN.BIZ FOUNDER PHOTO GENERATION")
    print("Only generating missing scenarios")
    print("="*70)

    # Ensure output directory exists
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Statistics
    total_generated = 0
    total_skipped = 0
    total_failed = 0
    total_time = 0.0

    # Process each founder
    for founder_key, config in FOUNDER_CONFIG.items():
        print(f"\n{'#'*70}")
        print(f"# FOUNDER: {config['name']} - {config['role']}")
        print(f"{'#'*70}")

        # Check for base photo
        base_webp_path = OUTPUT_DIR / f"{founder_key}_base.webp"
        base_png_path = OUTPUT_DIR / f"{founder_key}_base.png"

        if base_webp_path.exists():
            base_image_path = base_webp_path
        elif base_png_path.exists():
            base_image_path = base_png_path
        else:
            print(f"[X] No base photo found for {config['name']}, skipping")
            total_failed += len(config['scenarios'])
            continue

        print(f"[OK] Using base photo: {base_image_path.name}")

        # Generate missing scenario photos
        for idx, scenario in enumerate(config['scenarios'], 1):
            situation = scenario['situation']
            output_path = OUTPUT_DIR / f"{founder_key}_{situation}.webp"

            # Skip if already exists
            if output_path.exists():
                print(f"\n[SKIP] Scenario {idx}/4: {situation} (already exists)")
                total_skipped += 1
                continue

            print(f"\n--- Generating Scenario {idx}/4: {situation} ---")

            start_time = time.time()
            success = generate_scenario_photo(base_image_path, founder_key, scenario, idx)
            elapsed = time.time() - start_time

            if success:
                total_generated += 1
                total_time += elapsed
                print(f"[OK] Success! ({elapsed:.1f}s)")
            else:
                total_failed += 1
                print(f"[X] Failed ({elapsed:.1f}s)")

            # Rate limiting
            if idx < len(config['scenarios']):
                time.sleep(3)

    # Final summary
    print("\n" + "="*70)
    print("GENERATION SUMMARY")
    print("="*70)

    total_expected = sum(len(config['scenarios']) for config in FOUNDER_CONFIG.values())

    print(f"\n[OK] Successfully generated: {total_generated}/{total_expected}")
    print(f"[SKIP] Already existed: {total_skipped}/{total_expected}")
    print(f"[X] Failed: {total_failed}/{total_expected}")
    print(f"\nTotal processing time: {total_time:.1f}s")

    if total_generated > 0:
        print(f"Average per image: {total_time/total_generated:.1f}s")

    print(f"\nOutput directory: {OUTPUT_DIR}")
    print(f"\nAll files:")
    for file in sorted(OUTPUT_DIR.glob("*.webp")):
        file_size = file.stat().st_size / (1024 * 1024)  # MB
        print(f"  - {file.name} ({file_size:.2f} MB)")

    print("\n" + "="*70)
    print("DONE!")
    print("="*70)

    return total_failed == 0


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
