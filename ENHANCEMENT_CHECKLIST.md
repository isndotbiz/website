# Photo Enhancement Checklist

## Pre-Flight Check

### 1. API Key Setup
- [ ] Go to https://fal.ai/
- [ ] Sign up/login
- [ ] Get API key from API Keys section
- [ ] Store in 1Password as "FAL API Key"
- [ ] Have key ready for script

### 2. Verify Source Photos
- [✓] Alicia's 3 photos (1.1-1.4 MB each)
- [✓] Bri's 3 photos (1.1 MB each)
- [✓] Jonathan's 3 photos (1.1-1.3 MB each)
- [✓] Lilly's 3 photos (1.0-1.2 MB each)

### 3. Dependencies
- [ ] Python 3 installed
- [ ] requests library (`pip install requests`)
- [ ] Internet connection active
- [ ] ~$6 credit on fal.ai account

## Running Enhancement

### Quick Start (Easiest)
```bash
/mnt/d/workspace/ISNBIZ_Files/scripts/run_photo_enhancement.sh
```

### Manual Start
```bash
export FAL_API_KEY='your-key-here'
python3 /mnt/d/workspace/ISNBIZ_Files/scripts/enhance_founder_photos.py
```

## What to Expect

### Timeline
- [ ] ~3-5 minutes per founder
- [ ] ~15-20 minutes total
- [ ] 24 photos generated

### Cost
- [ ] Portrait Enhance: $4.80 (12 images)
- [ ] FLUX Ultra: $0.72 (12 images)
- [ ] Total: ~$5.52

### Output
- [ ] 24 PNG files created
- [ ] Location: `/mnt/d/workspace/ISNBIZ_Files/assets/team/`
- [ ] High resolution (2K-4K)
- [ ] Professional quality

## After Enhancement

### Review
- [ ] Check all 24 photos
- [ ] Compare Portrait vs FLUX versions
- [ ] Select best for each founder
- [ ] Verify likeness maintained

### Usage
- [ ] Implement in HROC website
- [ ] Update marketing materials
- [ ] Use for presentations
- [ ] Share with team

### Archive
- [ ] Keep source photos
- [ ] Save enhanced versions
- [ ] Document which versions used where
- [ ] Note for future enhancements

## Files Reference

### Scripts
- `/mnt/d/workspace/ISNBIZ_Files/scripts/enhance_founder_photos.py`
- `/mnt/d/workspace/ISNBIZ_Files/scripts/run_photo_enhancement.sh`

### Documentation
- `/mnt/d/workspace/ISNBIZ_Files/FOUNDER_PHOTO_ENHANCEMENT_SUMMARY.md`
- `/mnt/d/workspace/ISNBIZ_Files/scripts/PHOTO_ENHANCEMENT_README.md`
- `/mnt/d/workspace/ISNBIZ_Files/scripts/SOURCE_PHOTOS_REFERENCE.md`

### Output
- `/mnt/d/workspace/ISNBIZ_Files/assets/team/*.png`

## Quality Check

For each founder, verify:
- [ ] 6 photos generated (3 portrait, 3 flux)
- [ ] Looks like the actual founder
- [ ] Professional quality
- [ ] Appropriate context/setting
- [ ] High resolution
- [ ] No artifacts or distortions

## Models Used

### Portrait Enhance
- [✓] Model: `fal-ai/image-apps-v2/portrait-enhance`
- [✓] Cost: $0.40/image
- [✓] Quality: 4K, 3:4 ratio
- [✓] Purpose: Clarity enhancement

### FLUX 1.1 Pro Ultra
- [✓] Model: `fal-ai/flux-pro/v1.1-ultra`
- [✓] Cost: $0.06/image
- [✓] Quality: 2K, photo realism
- [✓] Purpose: Professional styling

## Troubleshooting

Common issues:
- [ ] API key error → Set FAL_API_KEY
- [ ] Upload failed → Check connection
- [ ] Enhancement failed → Check API status
- [ ] File not found → Verify paths

## Success Criteria

- [✓] All source photos exist
- [ ] All 24 enhanced photos generated
- [ ] Each photo maintains founder likeness
- [ ] Professional quality achieved
- [ ] Ready for production use

## Next Steps

1. [ ] Get FAL API key
2. [ ] Run enhancement script
3. [ ] Review all 24 photos
4. [ ] Select best versions
5. [ ] Implement in website/materials
6. [ ] Archive for future use

---

**Ready to run!** All source photos verified and scripts ready.
