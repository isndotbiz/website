# HROC Founder Photo Enhancement

## Overview
This script enhances ACTUAL founder photos from HROC using fal.ai's professional portrait enhancement APIs.

**CRITICAL:** This uses REAL founder photos - not AI-generated people!

## Source Photos
- **Alicia:** `/mnt/d/workspace/projects/HROC_Files/HROC_Website_New/images/founders/a/alicia_*_real.webp`
- **Bri:** `/mnt/d/workspace/projects/HROC_Files/HROC_Website_New/images/founders/b/bri_varied_*.webp`
- **Jonathan:** `/mnt/d/workspace/projects/HROC_Files/HROC_Website_New/images/founders/j/jonathan_varied_*.webp`
- **Lilly:** `/mnt/d/workspace/projects/HROC_Files/HROC_Website_New/images/founders/l/lilly_varied_*.webp`

## Enhancement Methods

### 1. Portrait Enhance ($0.40/image)
- **Model:** `fal-ai/image-apps-v2/portrait-enhance`
- **Purpose:** Enhance clarity and detail of portraits
- **Output:** 3:4 aspect ratio, 4K quality
- **Best for:** Clean enhancement while maintaining original look

### 2. FLUX 1.1 Pro Ultra ($0.06/image)
- **Model:** `fal-ai/flux-pro/v1.1-ultra`
- **Purpose:** Image-to-image enhancement with professional styling
- **Output:** 2K resolution, professional photo realism
- **Best for:** Adding professional context and polish

## Setup

### 1. Get FAL API Key
1. Go to https://fal.ai/
2. Sign up/login
3. Go to API Keys section
4. Create new API key
5. Store in 1Password as "FAL API Key"

### 2. Set Environment Variable
```bash
export FAL_API_KEY='your-fal-api-key-here'
```

### 3. Install Dependencies
```bash
pip install requests
```

## Usage

### Run Enhancement Script
```bash
python3 /mnt/d/workspace/ISNBIZ_Files/scripts/enhance_founder_photos.py
```

### What It Does
For each founder (Alicia, Bri, Jonathan, Lilly):
1. Takes 3 source photos
2. Creates 2 enhanced versions per photo:
   - Portrait Enhanced version
   - FLUX Ultra professional version
3. Total: 24 enhanced images (6 per founder)

### Output Location
```
/mnt/d/workspace/ISNBIZ_Files/assets/team/
```

### Output Files
- `{founder}_enhanced_portrait_{01-03}.png` - Portrait Enhance versions
- `{founder}_enhanced_flux_{01-03}.png` - FLUX Ultra versions

## Professional Contexts

Each photo is enhanced with specific professional context:

### Alicia
1. Professional headshot
2. Office setting
3. Presentation

### Bri
1. Professional headshot
2. Business casual
3. Leadership

### Jonathan
1. Professional headshot
2. Tech leader
3. Executive

### Lilly
1. Professional headshot
2. Office professional
3. Wellness leader

## Cost Estimate
- Portrait Enhance: 12 images × $0.40 = $4.80
- FLUX Ultra: 12 images × $0.06 = $0.72
- **Total: ~$5.52**

## Quality Settings
- **Portrait Enhance:** 3:4 aspect ratio for professional portraits
- **FLUX Ultra:** 
  - image_prompt_strength: 0.75 (strong source influence)
  - output_format: PNG (high quality)
  - safety_tolerance: 5 (professional content)

## Important Notes
1. **Uses REAL photos** - Not AI-generated faces
2. **Maintains likeness** - Enhances the actual founders
3. **Professional quality** - Suitable for website, marketing materials
4. **High resolution** - Ready for print and digital use
5. **Rate limited** - 2-second delay between API calls

## Research Sources
Based on 2026 research, the best fal.ai models for professional portraits are:
- **FLUX 1.1 Pro Ultra** - Best photo realism (up to 2K)
- **Portrait Enhance** - Specialized portrait enhancement
- **FLUX.2 [max]** - State-of-the-art (alternate option)

## Troubleshooting

### API Key Error
```
ERROR: FAL_API_KEY environment variable not set
```
**Solution:** Set the environment variable with your API key

### Upload Failed
**Solution:** Check internet connection and API key validity

### Enhancement Failed
**Solution:** Check fal.ai API status and rate limits

### File Not Found
**Solution:** Verify source photo paths exist

## Next Steps
1. Review enhanced photos
2. Select best versions for each founder
3. Use in HROC website and marketing materials
4. Keep originals for future re-enhancement if needed

## API Documentation
- Portrait Enhance: https://fal.ai/models/fal-ai/image-apps-v2/portrait-enhance
- FLUX 1.1 Pro Ultra: https://fal.ai/models/fal-ai/flux-pro/v1.1-ultra
- File Upload: https://fal.ai/docs/model-api/file-upload
