# HROC Founder Photo Enhancement - Quick Start Guide

## TL;DR

Enhance HROC founder photos to professional corporate headshots using fal.ai:

```bash
# 1. Get API key from 1Password "FAL API Key"
export FAL_KEY="your-api-key-from-1password"

# 2. Run the enhancement script (recommended)
python3 /mnt/d/workspace/ISNBIZ_Files/scripts/enhance_founder_photos_base64.py

# 3. Check results
ls -lh /mnt/d/workspace/ISNBIZ_Files/assets/team/
```

## What This Does

Takes REAL founder photos from HROC and generates 3 professional variants per founder:

**Input**: Actual founder photos (Alicia, Bri, Jonathan, Lilly)
**Output**: 12 enhanced professional headshots (3 per founder)
**Model**: fal.ai GPT-Image 1.5 Edit API
**Cost**: ~$1.80 total (~$0.15 per image)
**Time**: ~5-10 minutes for all 12 images

## Source Photos Used

- **Alicia**: `/mnt/d/workspace/projects/HROC_Files/HROC_Website_New/images/founders/a/alicia_hero_real.webp`
- **Bri**: `/mnt/d/workspace/projects/HROC_Files/HROC_Website_New/images/founders/b/bri_varied_01.webp`
- **Jonathan**: `/mnt/d/workspace/projects/HROC_Files/HROC_Website_New/images/founders/j/jonathan_varied_02.webp`
- **Lilly**: `/mnt/d/workspace/projects/HROC_Files/HROC_Website_New/images/founders/l/lilly_varied_01.webp`

## Output Location

All enhanced photos saved to:
```
/mnt/d/workspace/ISNBIZ_Files/assets/team/
```

## Expected Results

### Alicia (3 variants)
- `alicia_enhanced_01.png` - Corporate executive style
- `alicia_enhanced_02.png` - Business casual style
- `alicia_enhanced_03.png` - Clean studio style

### Bri (3 variants)
- `bri_enhanced_01.png` - Corporate executive style
- `bri_enhanced_02.png` - Business casual style
- `bri_enhanced_03.png` - Clean studio style

### Jonathan (3 variants)
- `jonathan_enhanced_01.png` - Corporate executive style
- `jonathan_enhanced_02.png` - Business casual style
- `jonathan_enhanced_03.png` - Clean studio style

### Lilly (3 variants)
- `lilly_enhanced_01.png` - Corporate executive style
- `lilly_enhanced_02.png` - Business casual style
- `lilly_enhanced_03.png` - Clean studio style

## Alternative: Headshot Generator (Faster, Simpler)

If you want a simpler approach:

```bash
python3 /mnt/d/workspace/ISNBIZ_Files/scripts/enhance_founder_photos_headshot.py
```

This uses a specialized headshot model with preset backgrounds.

## Troubleshooting

### "FAL_KEY environment variable not set"
Get the API key from 1Password and export it:
```bash
export FAL_KEY="your-api-key"
```

### "401 Unauthorized"
The API key is invalid. Get the correct key from 1Password item "FAL API Key".

### Script fails or produces poor results
See the detailed troubleshooting in `FAL_AI_MODEL_COMPARISON.md`

## Next Steps After Generation

1. Review all 12 generated images
2. Select the best variant for each founder (or use all 3)
3. Use in HROC website team section
4. Use in marketing materials and presentations
5. Consider upscaling with Crystal Upscaler if higher resolution needed

## Key Features

✓ Uses REAL founder photos (not AI-generated faces)
✓ Maintains founder identity and appearance
✓ Professional corporate headshot quality
✓ Multiple style variants per founder
✓ High resolution PNG output
✓ Natural-looking enhancements
✓ Suitable for corporate website use

## Documentation

- `README_ENHANCEMENT.md` - Detailed setup and usage guide
- `FAL_AI_MODEL_COMPARISON.md` - Compare different models and approaches
- Scripts in `/mnt/d/workspace/ISNBIZ_Files/scripts/`:
  - `enhance_founder_photos_base64.py` (recommended)
  - `enhance_founder_photos_gpt15.py` (alternative)
  - `enhance_founder_photos_headshot.py` (specialized)

## Support

For issues or questions:
1. Check the detailed documentation in `README_ENHANCEMENT.md`
2. Review model comparison in `FAL_AI_MODEL_COMPARISON.md`
3. Check fal.ai documentation: https://docs.fal.ai

---

**Ready to go?** Just export your FAL_KEY and run the script!

```bash
export FAL_KEY="your-api-key-from-1password"
python3 /mnt/d/workspace/ISNBIZ_Files/scripts/enhance_founder_photos_base64.py
```
