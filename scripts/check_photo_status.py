#!/usr/bin/env python3
"""
Check status of founder photo generation
"""

from pathlib import Path

OUTPUT_DIR = Path("/home/jdmal/workspace/ISNBIZ_Files/assets/founders")

EXPECTED_PHOTOS = {
    "bri": ["office_work", "presentation", "team_meeting", "strategic_planning"],
    "lilly": ["office_work", "presentation", "team_meeting", "strategic_planning"],
    "jonathan": ["office_work", "presentation", "team_meeting", "strategic_planning"],
    "alicia": ["office_work", "presentation", "team_meeting", "strategic_planning"]
}

def main():
    print("\n" + "="*70)
    print("ISN.BIZ FOUNDER PHOTOS - STATUS CHECK")
    print("="*70 + "\n")

    total_expected = 0
    total_complete = 0

    for founder, scenarios in EXPECTED_PHOTOS.items():
        print(f"{founder.upper()}:")

        complete = 0
        for scenario in scenarios:
            filename = f"{founder}_{scenario}.webp"
            filepath = OUTPUT_DIR / filename

            if filepath.exists():
                size_kb = filepath.stat().st_size / 1024
                print(f"  [OK] {scenario:20s} ({size_kb:6.1f} KB)")
                complete += 1
                total_complete += 1
            else:
                print(f"  [ ] {scenario:20s} (missing)")

            total_expected += 1

        print(f"  Status: {complete}/{len(scenarios)} complete\n")

    print("="*70)
    print(f"OVERALL: {total_complete}/{total_expected} photos complete")
    print(f"Progress: {total_complete/total_expected*100:.1f}%")
    print("="*70 + "\n")

if __name__ == "__main__":
    main()
