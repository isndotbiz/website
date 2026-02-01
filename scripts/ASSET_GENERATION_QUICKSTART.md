# AI Asset Generation - Quick Start Guide

## Overview
Generate professional AI-created visual assets for the isn.biz website using the Flux 2 API.

---

## Prerequisites

### 1. Get API Key

Sign up for a fal.ai account and get your API key:
- Visit: https://fal.ai/
- Create account
- Get API key from dashboard
- Cost: ~$2.10 for all 23 assets

### 2. Install Dependencies

```bash
cd /mnt/d/workspace/ISNBIZ_Files/scripts
pip install -r requirements-assets.txt
```

---

## Quick Start

### Option 1: Generate All Assets (Recommended)

```bash
# Set your API key
export FAL_KEY='your-fal-ai-api-key-here'

# Generate all assets
python generate_ai_assets.py
```

This will generate:
- 5 Hero backgrounds
- 8 Portfolio mockups
- 6 Service icons
- 4 Section dividers

**Total: 23 high-quality images**

### Option 2: Test First (Recommended for First Run)

```bash
# Test with just one asset per category
python generate_ai_assets.py --test
```

This generates only 4 images (one from each category) to verify everything works.

### Option 3: Generate Specific Categories

```bash
# Generate only hero backgrounds
python generate_ai_assets.py --categories hero_backgrounds

# Generate multiple categories
python generate_ai_assets.py --categories hero_backgrounds service_icons

# Available categories:
# - hero_backgrounds
# - portfolio_mockups
# - service_icons
# - section_dividers
```

---

## Command Options

```bash
# Show help
python generate_ai_assets.py --help

# Pass API key via argument (instead of environment variable)
python generate_ai_assets.py --api-key YOUR_KEY

# Overwrite existing files (default: skip existing)
python generate_ai_assets.py --overwrite

# Test mode (one asset per category)
python generate_ai_assets.py --test
```

---

## Expected Output

### Directory Structure
```
/mnt/d/workspace/ISNBIZ_Files/assets/images/
├── hero/
│   ├── hero-bg-network.png
│   ├── hero-bg-geometric.png
│   ├── hero-bg-data-viz.png
│   ├── hero-bg-metallic.png
│   └── hero-bg-particles.png
├── portfolio/
│   ├── portfolio-opportunity-bot-dashboard.png
│   ├── portfolio-opportunity-bot-chat.png
│   ├── portfolio-spiritatlas-profile.png
│   ├── portfolio-spiritatlas-meditation.png
│   ├── portfolio-analytics-dashboard.png
│   ├── portfolio-cloud-architecture.png
│   ├── portfolio-ecommerce-platform.png
│   └── portfolio-api-docs.png
├── icons/
│   ├── icon-custom-dev.png
│   ├── icon-ai-ml.png
│   ├── icon-cloud-architecture.png
│   ├── icon-data-engineering.png
│   ├── icon-security.png
│   └── icon-mobile-dev.png
└── backgrounds/
    ├── divider-gradient-wave.png
    ├── divider-metallic-lines.png
    ├── divider-particle-scatter.png
    └── divider-circuit-pattern.png
```

### Generation Time
- Each image: ~10-20 seconds
- Total time: ~8-10 minutes for all assets
- Rate limiting: 2 seconds between requests

### Cost Estimate
- Hero backgrounds (5): $0.50
- Portfolio mockups (8): $0.80
- Service icons (6): $0.48
- Section dividers (4): $0.32
- **Total: ~$2.10**

---

## Troubleshooting

### API Key Error
```
❌ Error: FAL_KEY not found in environment variables
```
**Solution**: Set your API key
```bash
export FAL_KEY='your-api-key'
```

### Missing Dependencies
```
Missing dependencies. Install with:
pip install fal-client pillow requests python-dotenv
```
**Solution**: Install requirements
```bash
pip install -r requirements-assets.txt
```

### Generation Failed
```
❌ Error generating image: [error message]
```
**Common causes**:
- Invalid API key
- Insufficient credits
- Network issues
- API rate limiting

**Solution**: Check API key, account credits, and try again

### Low Quality Results
If generated images don't meet quality expectations:

1. **Adjust prompts** in `generate_ai_assets.py`
2. **Regenerate specific assets**:
   ```bash
   # Delete the low-quality image
   rm /mnt/d/workspace/ISNBIZ_Files/assets/images/hero/hero-bg-network.png

   # Regenerate
   python generate_ai_assets.py --categories hero_backgrounds
   ```

---

## Manual Generation (Alternative)

If you prefer manual control or don't want to use the script:

### 1. Use fal.ai Playground
- Visit: https://fal.ai/models/fal-ai/flux-pro
- Copy prompts from `/mnt/d/workspace/ISNBIZ_Files/docs/AI_ASSET_GENERATION_GUIDE.md`
- Generate and download manually

### 2. Use Other Services
- **Midjourney**: Via Discord bot (requires subscription)
- **DALL-E 3**: Via OpenAI API
- **Stable Diffusion**: Self-hosted or via Replicate

---

## Post-Processing (Optional)

### Optimize Images
```bash
# Install optimization tools
sudo apt-get install imagemagick webp

# Optimize PNGs (reduce file size)
cd /mnt/d/workspace/ISNBIZ_Files/assets/images
find . -name "*.png" -exec optipng -o7 {} \;

# Convert to WebP (modern format, better compression)
find . -name "*.png" -exec sh -c 'cwebp -q 85 "$1" -o "${1%.png}.webp"' _ {} \;
```

### Create Responsive Versions
```bash
# Create @2x versions for retina displays
cd /mnt/d/workspace/ISNBIZ_Files/assets/images/icons
for file in *.png; do
    convert "$file" -resize 1024x1024 "${file%.png}@2x.png"
done
```

---

## Integration with Website

After generating assets, update the HTML to use them:

### Hero Backgrounds
```html
<!-- In index.html -->
<section class="hero" style="background-image: url('assets/images/hero/hero-bg-network.png')">
```

### Portfolio Mockups
```html
<!-- In portfolio.html -->
<img src="assets/images/portfolio/portfolio-opportunity-bot-dashboard.png"
     alt="Opportunity Bot Dashboard">
```

### Service Icons
```html
<!-- In services.html -->
<img src="assets/images/icons/icon-custom-dev.png"
     alt="Custom Development Icon"
     class="service-icon">
```

### Section Dividers
```css
/* In styles.css */
.section-divider {
    background-image: url('assets/images/backgrounds/divider-gradient-wave.png');
    background-size: cover;
    height: 400px;
}
```

---

## Quality Checklist

After generation, verify:
- [ ] All 23 assets generated successfully
- [ ] Brand colors are accurate (#1E9FF2, #5FDFDF, #3F4447)
- [ ] Images are high resolution and sharp
- [ ] No unwanted text or watermarks
- [ ] Professional, modern aesthetic
- [ ] Consistent style across categories
- [ ] File sizes are reasonable (< 500KB for backgrounds)
- [ ] Images display correctly in browsers

---

## Next Steps

1. **Generate assets**: Run the script
2. **Review quality**: Check all generated images
3. **Optimize**: Convert to WebP, create responsive versions
4. **Integrate**: Update HTML/CSS to use new assets
5. **Test**: Preview website with new assets
6. **Deploy**: Push to production

---

## Support & Resources

### Documentation
- Full Guide: `/mnt/d/workspace/ISNBIZ_Files/docs/AI_ASSET_GENERATION_GUIDE.md`
- Generation Script: `/mnt/d/workspace/ISNBIZ_Files/scripts/generate_ai_assets.py`

### API Documentation
- fal.ai Docs: https://fal.ai/docs
- Flux 2 Guide: https://wavespeed.ai/blog/posts/flux-2-complete-guide-2026/
- API Examples: https://medium.com/@davidlfliang/guide-api-image-generation-2026-nano-banana-imagen-flux-gpt-image-0bff59e9d163

### Need Help?
- Check script output for error messages
- Review the troubleshooting section above
- Consult the detailed guide for prompt customization
- Contact fal.ai support for API issues

---

## Example Session

```bash
# Navigate to scripts directory
cd /mnt/d/workspace/ISNBIZ_Files/scripts

# Set API key
export FAL_KEY='fal_xxxxxxxxxxxxx'

# Test first (recommended)
python generate_ai_assets.py --test

# Output:
# 🧪 TEST MODE - Generating first asset from each category
#
# ============================================================
# ISN.BIZ AI ASSET GENERATOR
# ============================================================
# Brand Colors: Blue #1E9FF2, Cyan #5FDFDF, Charcoal #3F4447
# Output base: /mnt/d/workspace/ISNBIZ_Files/assets/images
# ============================================================
#
# ============================================================
# Generating: HERO BACKGROUNDS
# ============================================================
# Output directory: /mnt/d/workspace/ISNBIZ_Files/assets/images/hero
# Assets to generate: 1
#
# [1/1] hero-bg-network
#   Generating with fal-ai/flux-pro/v1.1...
#   Resolution: 2560x1440
#   ✓ Saved: hero-bg-network.png (423.5 KB)
#
# ... (continues for each category)
#
# ============================================================
# GENERATION SUMMARY
# ============================================================
# ✓ Generated: 4
# ⊘ Skipped: 0
# ❌ Failed: 0
# Total: 4
# ============================================================

# If test looks good, generate all assets
python generate_ai_assets.py

# Check results
ls -lh /mnt/d/workspace/ISNBIZ_Files/assets/images/hero/
ls -lh /mnt/d/workspace/ISNBIZ_Files/assets/images/portfolio/
ls -lh /mnt/d/workspace/ISNBIZ_Files/assets/images/icons/
ls -lh /mnt/d/workspace/ISNBIZ_Files/assets/images/backgrounds/
```

---

**Ready to create stunning AI-generated assets for your isn.biz website!**
