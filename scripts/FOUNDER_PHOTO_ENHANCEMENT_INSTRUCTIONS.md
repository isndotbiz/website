# HROC Founder Photo Enhancement Guide

## Overview
This script uses fal.ai's Portrait Enhance API to create professional, enhanced versions of the ACTUAL HROC founder photos.

## What This Does
- Takes REAL founder photos from HROC (not AI-generated random people)
- Enhances them using fal.ai Portrait Enhance model
- Creates 3 professional variants per founder (12 total images)
- Maintains realistic appearance while improving quality

## Source Photos

### Alicia (Real Photos - High Quality)
- `alicia_hero_real.webp` - Professional hero shot
- `alicia_office_real.webp` - Office setting
- `alicia_community_real.webp` - Community engagement

### Bri
- `bri_professional_01_2.webp` - Professional photo 1
- `bri_professional_08_2.webp` - Professional photo 2
- `bri_varied_01.webp` - Varied setting

### Jonathan
- `jonathan_varied_01.webp` - Professional variant 1
- `jonathan_varied_02.webp` - Professional variant 2
- `jonathan_varied_03.webp` - Professional variant 3

### Lilly
- `lilly_varied_01.webp` - Professional variant 1
- `lilly_varied_02.webp` - Professional variant 2
- `lilly_varied_03.webp` - Professional variant 3

## fal.ai Model Research

### Best Model for Professional Portraits: Portrait Enhance
After researching fal.ai's model catalog, the **Portrait Enhance** model is ideal because:

1. **Purpose-Built**: Specifically designed for portrait enhancement
2. **Preserves Identity**: Enhances clarity and detail while keeping the same person
3. **Professional Quality**: Improves lighting, sharpness, and overall presentation
4. **Cost-Effective**: $0.40 per image (vs $0.06-$4+ for other models)
5. **Fast**: Quick processing times (~10s per image)

### Alternative Models Considered
- **FLUX1.1 Pro Ultra**: Better for text-to-image generation, not portrait enhancement
- **GPT Image 1.5**: More for creative editing, may alter appearance too much
- **Face Enhancement**: Similar but Portrait Enhance is newer/better

## Setup Instructions

### 1. Get API Key from 1Password
```bash
# Find "FAL API Key" in 1Password
# Copy the key value
```

### 2. Set Environment Variable
```bash
export FAL_KEY="your-fal-api-key-from-1password"
```

### 3. Install Dependencies (if needed)
```bash
pip install fal-client requests
```

### 4. Run the Script
```bash
cd /mnt/d/workspace/ISNBIZ_Files/scripts
python3 enhance_founder_photos.py
```

## Output

### Location
All enhanced photos will be saved to:
```
/mnt/d/workspace/ISNBIZ_Files/assets/team/
```

### File Naming
- `alicia_enhanced_01.webp` through `alicia_enhanced_03.webp`
- `bri_enhanced_01.webp` through `bri_enhanced_03.webp`
- `jonathan_enhanced_01.webp` through `jonathan_enhanced_03.webp`
- `lilly_enhanced_01.webp` through `lilly_enhanced_03.webp`

### Total Output
- 12 high-quality professional portraits
- Enhanced clarity and detail
- Maintained realistic appearance
- Same actual founders, just professionally enhanced

## Expected Cost
- 12 images × $0.40 = **$4.80 total**

## Expected Time
- ~10 seconds per image
- ~2 minutes total processing time
- Plus 2-second pauses between API calls = ~4 minutes total

## API Model Used

**fal-ai/image-apps-v2/portrait-enhance**
- Endpoint: `https://fal.run/fal-ai/image-apps-v2/portrait-enhance`
- Method: POST with image_url and aspect_ratio parameters
- Output: Enhanced portrait with improved clarity and detail
- Aspect Ratio: 1:1 (professional headshot format)

## Success Criteria
- All 12 images successfully enhanced
- Output files saved to assets/team/ directory
- Photos look like the actual founders (not random AI people)
- Professional quality suitable for website/marketing

## Troubleshooting

### If API Key Error
```bash
# Make sure you've exported the key:
export FAL_KEY="your-key-here"

# Verify it's set:
echo $FAL_KEY
```

### If File Not Found
- Check that source photos exist in HROC directory
- Verify paths in the script match actual file locations

### If Enhancement Fails
- Check internet connection
- Verify API key is valid and has credits
- Check fal.ai service status

## References
- [fal.ai Portrait Enhance](https://fal.ai/models/fal-ai/image-apps-v2/portrait-enhance)
- [fal.ai Model Explorer](https://fal.ai/explore/models)
- [fal-client Python Library](https://github.com/fal-ai/fal)

---

**IMPORTANT**: This uses REAL founder photos from HROC, not AI-generated random people. The enhancement process improves quality while maintaining the actual founder's appearance.
