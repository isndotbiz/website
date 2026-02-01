# Founder Photo Enhancement System

Complete automated system for enhancing HROC founder photos using fal.ai's Portrait Enhance API.

## Quick Start

```bash
# 1. Get API key from 1Password: "FAL API Key"
export FAL_KEY="your-fal-api-key"

# 2. Run the script
cd /mnt/d/workspace/ISNBIZ_Files/scripts
python3 enhance_founder_photos.py
```

## What This Does

Creates **12 professional enhanced portraits** (3 per founder):
- Alicia (using high-quality *_real.webp photos)
- Bri
- Jonathan
- Lilly

**CRITICAL:** Uses ACTUAL founder photos from HROC, NOT AI-generated random people!

## Files in This Directory

```
/mnt/d/workspace/ISNBIZ_Files/scripts/
│
├── enhance_founder_photos.py                      # Main enhancement script
├── FOUNDER_PHOTO_ENHANCEMENT_INSTRUCTIONS.md      # Complete documentation
├── QUICK_START.txt                                # 3-step quick reference
├── PROJECT_SUMMARY.md                             # Technical overview
└── README.md                                      # This file
```

## Model Research Results

After researching fal.ai's 2026 model catalog, we chose:

**fal-ai/image-apps-v2/portrait-enhance**

Why? It's purpose-built for portrait enhancement, preserves identity, and delivers professional quality while maintaining the actual person's appearance.

Models we considered but rejected:
- FLUX1.1 Pro Ultra - Better for text-to-image generation
- GPT Image 1.5 - May alter appearance too much
- Face Enhancement - Portrait Enhance is newer/better

## Cost & Time

- **Cost:** $4.80 total ($0.40 per image × 12 images)
- **Time:** ~4 minutes total processing

## Output

Enhanced photos saved to:
```
/mnt/d/workspace/ISNBIZ_Files/assets/team/
├── alicia_enhanced_01.webp
├── alicia_enhanced_02.webp
├── alicia_enhanced_03.webp
├── bri_enhanced_01.webp
├── bri_enhanced_02.webp
├── bri_enhanced_03.webp
├── jonathan_enhanced_01.webp
├── jonathan_enhanced_02.webp
├── jonathan_enhanced_03.webp
├── lilly_enhanced_01.webp
├── lilly_enhanced_02.webp
└── lilly_enhanced_03.webp
```

## Documentation

- **Quick Start:** `QUICK_START.txt` - 3 steps to run
- **Full Guide:** `FOUNDER_PHOTO_ENHANCEMENT_INSTRUCTIONS.md` - Complete documentation
- **Project Summary:** `PROJECT_SUMMARY.md` - Technical details and rationale

## Source Photos

Located in: `/mnt/d/workspace/projects/HROC_Files/HROC_Website_New/images/founders/`

All 12 source photos verified and ready:
- 6 Alicia photos (using *_real.webp high-quality versions)
- 8 Bri photos available (using 3 best professional shots)
- 8 Jonathan photos available (using 3 varied shots)
- 8 Lilly photos available (using 3 varied shots)

## Requirements

- Python 3.12+ (installed)
- fal-client library (installed)
- requests library (installed)
- FAL_KEY environment variable (get from 1Password)

## References

- [fal.ai Portrait Enhance](https://fal.ai/models/fal-ai/image-apps-v2/portrait-enhance)
- [fal.ai Model Explorer](https://fal.ai/explore/models)
- [fal-client Documentation](https://github.com/fal-ai/fal)

---

**Status:** Ready to Run
**Created:** 2026-02-01
