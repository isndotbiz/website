# HROC Founder Photo Enhancement - Complete Setup

## Overview
Professional enhancement of ACTUAL HROC founder photos using fal.ai's top portrait models.

**CRITICAL:** Uses REAL founder photos - not AI-generated people!

## Quick Start

### Option 1: Automated Run (Recommended)
```bash
/mnt/d/workspace/ISNBIZ_Files/scripts/run_photo_enhancement.sh
```

### Option 2: Manual Run
```bash
export FAL_API_KEY='your-api-key-here'
python3 /mnt/d/workspace/ISNBIZ_Files/scripts/enhance_founder_photos.py
```

## What Gets Enhanced

### 12 Source Photos (3 per founder)
- **Alicia:** High-quality real photos from recent update
- **Bri:** Professional varied shots
- **Jonathan:** Professional varied shots
- **Lilly:** Professional varied shots

### 24 Enhanced Outputs (6 per founder)
Each source photo gets TWO professional enhancements:
1. **Portrait Enhance** - Clarity and detail enhancement
2. **FLUX Ultra** - Professional styling and context

## Models Used

### 1. Portrait Enhance ($0.40/image)
- **API:** `fal-ai/image-apps-v2/portrait-enhance`
- **Quality:** 4K resolution, 3:4 aspect ratio
- **Purpose:** Enhanced clarity while maintaining original look
- **Best for:** Clean, professional enhancement

### 2. FLUX 1.1 Pro Ultra ($0.06/image)
- **API:** `fal-ai/flux-pro/v1.1-ultra`
- **Quality:** 2K resolution, professional photo realism
- **Purpose:** Professional context and styling
- **Best for:** Corporate/executive photography look

### Why These Models?
Based on 2026 research, these are the TOP fal.ai models for professional portraits:
- FLUX 1.1 Pro Ultra: Best photo realism, professional grade
- Portrait Enhance: Specialized portrait refinement
- Both maintain source image likeness (not generative)

## Cost Breakdown
- Portrait Enhance: 12 images × $0.40 = $4.80
- FLUX Ultra: 12 images × $0.06 = $0.72
- **Total: ~$5.52**

## Source Photos Verified

### Alicia Santiago (3 photos, ~1.1-1.4 MB each)
```
✓ /founders/a/alicia_hero_real.webp (1.4M)
✓ /founders/a/alicia_office_real.webp (1.1M)
✓ /founders/a/alicia_whiteboard_real.webp (1.1M)
```

### Bri [Last Name] (3 photos, ~1.1 MB each)
```
✓ /founders/b/bri_varied_01.webp (1.1M)
✓ /founders/b/bri_varied_02.webp (1.1M)
✓ /founders/b/bri_varied_03.webp (1.1M)
```

### Jonathan [Last Name] (3 photos, ~1.1-1.3 MB each)
```
✓ /founders/j/jonathan_varied_01.webp (1.1M)
✓ /founders/j/jonathan_varied_02.webp (1.3M)
✓ /founders/j/jonathan_varied_03.webp (1.1M)
```

### Lilly [Last Name] (3 photos, ~1.0-1.2 MB each)
```
✓ /founders/l/lilly_varied_01.webp (1.1M)
✓ /founders/l/lilly_varied_02.webp (1.0M)
✓ /founders/l/lilly_varied_03.webp (1.2M)
```

## Output Structure

### Directory
```
/mnt/d/workspace/ISNBIZ_Files/assets/team/
```

### Files (24 total)
```
alicia_enhanced_portrait_01.png
alicia_enhanced_portrait_02.png
alicia_enhanced_portrait_03.png
alicia_enhanced_flux_01.png
alicia_enhanced_flux_02.png
alicia_enhanced_flux_03.png

bri_enhanced_portrait_01.png
bri_enhanced_portrait_02.png
bri_enhanced_portrait_03.png
bri_enhanced_flux_01.png
bri_enhanced_flux_02.png
bri_enhanced_flux_03.png

jonathan_enhanced_portrait_01.png
jonathan_enhanced_portrait_02.png
jonathan_enhanced_portrait_03.png
jonathan_enhanced_flux_01.png
jonathan_enhanced_flux_02.png
jonathan_enhanced_flux_03.png

lilly_enhanced_portrait_01.png
lilly_enhanced_portrait_02.png
lilly_enhanced_portrait_03.png
lilly_enhanced_flux_01.png
lilly_enhanced_flux_02.png
lilly_enhanced_flux_03.png
```

## Professional Contexts

Each photo is enhanced with specific professional styling:

### Alicia
1. Professional headshot (corporate portrait)
2. Office setting (modern workspace)
3. Presentation (leadership presence)

### Bri
1. Professional headshot (executive portrait)
2. Business casual (approachable professional)
3. Leadership (inspirational leader)

### Jonathan
1. Professional headshot (executive portrait)
2. Tech leader (technology executive)
3. Executive (senior C-suite)

### Lilly
1. Professional headshot (executive portrait)
2. Office professional (contemporary workspace)
3. Wellness leader (balanced leadership)

## Getting Your API Key

1. Go to **https://fal.ai/**
2. Sign up or log in
3. Navigate to **API Keys** section
4. Create a new API key or copy existing
5. Store in **1Password** as "FAL API Key"
6. Use when running the script

## Files Created

### Main Script
```
/mnt/d/workspace/ISNBIZ_Files/scripts/enhance_founder_photos.py
```
- Full enhancement logic
- Both Portrait Enhance and FLUX Ultra
- Error handling and progress tracking

### Launcher Script
```
/mnt/d/workspace/ISNBIZ_Files/scripts/run_photo_enhancement.sh
```
- Interactive API key prompt
- Dependency checking
- User-friendly interface

### Documentation
```
/mnt/d/workspace/ISNBIZ_Files/scripts/PHOTO_ENHANCEMENT_README.md
/mnt/d/workspace/ISNBIZ_Files/scripts/SOURCE_PHOTOS_REFERENCE.md
/mnt/d/workspace/ISNBIZ_Files/FOUNDER_PHOTO_ENHANCEMENT_SUMMARY.md (this file)
```

## Technical Details

### Enhancement Process
1. Upload source photo to fal.ai storage
2. Run Portrait Enhance (4K quality)
3. Run FLUX Ultra with professional prompt
4. Download and save both versions
5. Rate-limited (2 sec between calls)

### Quality Settings
- **Portrait Enhance:** 3:4 ratio, 4K output
- **FLUX Ultra:** 0.75 image strength, PNG format, 2K resolution
- **Both:** High fidelity, professional color grading

### Professional Prompts
Each FLUX enhancement uses context-specific prompts:
- Professional corporate headshot
- Executive portrait
- High-end business photography
- Studio/office lighting
- Confident professional presence

## Research Sources

Based on comprehensive 2026 research:

### Top Models for Professional Portraits
1. **FLUX 1.1 Pro Ultra** - Best photo realism, professional grade
2. **Portrait Enhance** - Specialized portrait refinement
3. **FLUX.2 [max]** - State-of-the-art (alternative)

### Key Findings
- FLUX creates "incredibly realistic and professional headshots"
- Portrait Enhance "preserves composition, lighting, and fine-grained detail"
- Image-to-image maintains source likeness (unlike text-to-image)

### Documentation
- [fal.ai Portrait Enhance](https://fal.ai/models/fal-ai/image-apps-v2/portrait-enhance)
- [fal.ai FLUX 1.1 Pro Ultra](https://fal.ai/models/fal-ai/flux-pro/v1.1-ultra)
- [FLUX AI Headshot Tutorial](https://firstmovers.ai/flux-ai-image-generator/)
- [LinkedIn Headshots with FLUX](https://dev.to/derekdillman/creating-the-perfect-linkedin-headshot-using-ai-with-flux-lora-and-falai-1lc1)

## Important Notes

### About the Photos
- **REAL PEOPLE** - Actual HROC founders
- **MAINTAINS LIKENESS** - Enhances, doesn't transform
- **HIGH QUALITY** - Professional, print-ready
- **VERSATILE** - Website, marketing, presentations

### Processing Time
- ~3-5 minutes per founder
- ~15-20 minutes total
- Rate-limited for API stability

### Next Steps After Enhancement
1. Review all 24 enhanced photos
2. Select best versions for each use case
3. Implement in HROC website
4. Use in marketing materials
5. Keep originals for future re-enhancement

## Troubleshooting

### "FAL_API_KEY not set"
Set the environment variable with your API key

### "Upload failed"
Check internet connection and API key validity

### "Enhancement failed"
Check fal.ai API status and rate limits

### "File not found"
Verify source photo paths exist (all verified above)

## Support

For issues or questions:
1. Check documentation files
2. Verify API key is valid
3. Check fal.ai status page
4. Review error messages in script output

---

**Created:** 2026-02-01
**Purpose:** Professional enhancement of ACTUAL HROC founder photos
**Method:** fal.ai Portrait Enhance + FLUX 1.1 Pro Ultra
**Output:** 24 high-quality professional photos ready for use
