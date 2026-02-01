# HROC Founder Photo Enhancement - Project Structure

## Directory Organization

```
/mnt/d/workspace/
│
├── projects/HROC_Files/HROC_Website_New/images/founders/
│   ├── a/                          # Alicia's photos
│   │   ├── alicia_hero_real.webp       (1.4M) ← SOURCE
│   │   ├── alicia_office_real.webp     (1.1M) ← SOURCE
│   │   └── alicia_whiteboard_real.webp (1.1M) ← SOURCE
│   │
│   ├── b/                          # Bri's photos
│   │   ├── bri_varied_01.webp          (1.1M) ← SOURCE
│   │   ├── bri_varied_02.webp          (1.1M) ← SOURCE
│   │   └── bri_varied_03.webp          (1.1M) ← SOURCE
│   │
│   ├── j/                          # Jonathan's photos
│   │   ├── jonathan_varied_01.webp     (1.1M) ← SOURCE
│   │   ├── jonathan_varied_02.webp     (1.3M) ← SOURCE
│   │   └── jonathan_varied_03.webp     (1.1M) ← SOURCE
│   │
│   └── l/                          # Lilly's photos
│       ├── lilly_varied_01.webp        (1.1M) ← SOURCE
│       ├── lilly_varied_02.webp        (1.0M) ← SOURCE
│       └── lilly_varied_03.webp        (1.2M) ← SOURCE
│
└── ISNBIZ_Files/
    │
    ├── QUICK_START.md                  # ONE-COMMAND QUICK START
    ├── ENHANCEMENT_CHECKLIST.md        # Pre-flight checklist
    ├── FOUNDER_PHOTO_ENHANCEMENT_SUMMARY.md  # Complete guide
    ├── PROJECT_STRUCTURE.md            # This file
    │
    ├── scripts/
    │   ├── run_photo_enhancement.sh    # ← RUN THIS! (user-friendly)
    │   ├── enhance_founder_photos.py   # Main enhancement script
    │   ├── PHOTO_ENHANCEMENT_README.md # Technical documentation
    │   └── SOURCE_PHOTOS_REFERENCE.md  # Photo mapping reference
    │
    └── assets/
        └── team/                       # OUTPUT DIRECTORY
            ├── alicia_enhanced_portrait_01.png  ← Generated
            ├── alicia_enhanced_portrait_02.png
            ├── alicia_enhanced_portrait_03.png
            ├── alicia_enhanced_flux_01.png
            ├── alicia_enhanced_flux_02.png
            ├── alicia_enhanced_flux_03.png
            ├── bri_enhanced_portrait_01.png
            ├── bri_enhanced_portrait_02.png
            ├── bri_enhanced_portrait_03.png
            ├── bri_enhanced_flux_01.png
            ├── bri_enhanced_flux_02.png
            ├── bri_enhanced_flux_03.png
            ├── jonathan_enhanced_portrait_01.png
            ├── jonathan_enhanced_portrait_02.png
            ├── jonathan_enhanced_portrait_03.png
            ├── jonathan_enhanced_flux_01.png
            ├── jonathan_enhanced_flux_02.png
            ├── jonathan_enhanced_flux_03.png
            ├── lilly_enhanced_portrait_01.png
            ├── lilly_enhanced_portrait_02.png
            ├── lilly_enhanced_portrait_03.png
            ├── lilly_enhanced_flux_01.png
            ├── lilly_enhanced_flux_02.png
            └── lilly_enhanced_flux_03.png
```

## File Count Summary

### Source Photos
- **12 total** (3 per founder)
- All verified and exist
- High resolution (1.0-1.4 MB each)

### Generated Photos
- **24 total** (6 per founder)
- 12 Portrait Enhanced versions
- 12 FLUX Ultra versions
- High resolution (2K-4K PNG)

### Documentation Files
- **6 total**
  - 1 Quick start guide
  - 1 Checklist
  - 1 Complete summary
  - 1 Project structure (this file)
  - 2 Technical references

### Script Files
- **2 total**
  - 1 User-friendly launcher
  - 1 Main Python script

## Quick Navigation

### To Run Enhancement
```bash
/mnt/d/workspace/ISNBIZ_Files/scripts/run_photo_enhancement.sh
```

### To View Output
```bash
ls -lh /mnt/d/workspace/ISNBIZ_Files/assets/team/
```

### To Read Documentation
```bash
# Quick start
cat /mnt/d/workspace/ISNBIZ_Files/QUICK_START.md

# Complete guide
cat /mnt/d/workspace/ISNBIZ_Files/FOUNDER_PHOTO_ENHANCEMENT_SUMMARY.md

# Checklist
cat /mnt/d/workspace/ISNBIZ_Files/ENHANCEMENT_CHECKLIST.md
```

## File Purposes

### User-Facing Files
- **QUICK_START.md** - Fastest way to get started
- **ENHANCEMENT_CHECKLIST.md** - Step-by-step verification
- **run_photo_enhancement.sh** - Interactive launcher

### Technical Files
- **enhance_founder_photos.py** - Main processing logic
- **PHOTO_ENHANCEMENT_README.md** - API documentation
- **SOURCE_PHOTOS_REFERENCE.md** - Photo mappings

### Reference Files
- **FOUNDER_PHOTO_ENHANCEMENT_SUMMARY.md** - Complete reference
- **PROJECT_STRUCTURE.md** - This organizational guide

## Enhancement Flow

```
SOURCE PHOTOS (12)
    ↓
[Upload to fal.ai]
    ↓
[Portrait Enhance API] → 12 portrait_*.png
    ↓
[FLUX 1.1 Pro Ultra] → 12 flux_*.png
    ↓
OUTPUT DIRECTORY (24 enhanced photos)
```

## Models Used

1. **Portrait Enhance**
   - API: `fal-ai/image-apps-v2/portrait-enhance`
   - Cost: $0.40/image × 12 = $4.80

2. **FLUX 1.1 Pro Ultra**
   - API: `fal-ai/flux-pro/v1.1-ultra`
   - Cost: $0.06/image × 12 = $0.72

**Total Cost: ~$5.52**

## Professional Contexts

Each founder gets 3 different professional enhancements:

- **Alicia:** Headshot, Office, Presentation
- **Bri:** Headshot, Business Casual, Leadership
- **Jonathan:** Headshot, Tech Leader, Executive
- **Lilly:** Headshot, Office Professional, Wellness Leader

## Success Metrics

- ✓ All source photos verified (12/12)
- ✓ Scripts created and executable (2/2)
- ✓ Documentation complete (6/6)
- ✓ Output directory ready
- ⏳ Enhancement pending (run script)
- ⏳ Review and selection (after enhancement)

---

**Status:** Ready to run enhancement!
**Next Step:** Execute `/mnt/d/workspace/ISNBIZ_Files/scripts/run_photo_enhancement.sh`
