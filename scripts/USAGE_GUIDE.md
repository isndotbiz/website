# Website Asset Generator - Complete Usage Guide

## Overview

This tool generates professional, award-worthy website assets using **fal.ai's latest 2026 AI models**. It creates hero backgrounds, portfolio mockups, service icons, team visuals, and video assets optimized for modern web design.

## 🚀 Quick Start

### 1. Get Your API Key

1. Open **1Password**
2. Search for **"fal"**
3. Copy the API key

### 2. Set Environment Variable

```bash
export FAL_KEY='your-fal-api-key-here'
```

**For persistent setup**, add to your shell profile:

```bash
# Add to ~/.bashrc or ~/.zshrc
echo 'export FAL_KEY="your-fal-api-key-here"' >> ~/.bashrc
source ~/.bashrc
```

### 3. Install Dependencies

```bash
cd /mnt/d/workspace/ISNBIZ_Files/scripts
pip install -r requirements.txt
```

### 4. Generate Assets

**Option A: Using the setup script (recommended)**
```bash
./setup_and_generate.sh
```

**Option B: Direct Python execution**
```bash
python3 generate_website_assets.py
```

## 📊 What Gets Generated

### Hero Backgrounds (5 variations)
- **Resolution**: 2560×1440 (QHD)
- **Model**: FLUX.2 Max
- **Time**: ~2-3 minutes
- **Use**: Header sections, landing pages

### Portfolio Mockups (10 images)
- **Resolution**: 1920×1080 (Full HD)
- **Model**: FLUX1.1 Pro Ultra (2K, 6x faster)
- **Time**: ~3-4 minutes
- **Use**: Portfolio galleries, case studies

Types:
1. AI chatbot interface
2. Analytics dashboard
3. Mobile app screens
4. Code editor
5. Data visualization
6. Cloud architecture
7. CRM interface
8. Security dashboard
9. ML training interface
10. API documentation

### Service Icons (6 custom)
- **Resolution**: 1024×1024
- **Model**: FLUX.2 Pro
- **Time**: ~2 minutes
- **Use**: Service cards, feature lists

Icons:
1. AI/ML Development
2. Cloud Architecture
3. Mobile Development
4. Data Engineering
5. Security & Compliance
6. Custom Development

### Team Visuals (4 images)
- **Resolution**: 1920×1080
- **Model**: FLUX.2 Max
- **Time**: ~2 minutes
- **Use**: About page, team section

### Video Assets (2-3 videos)
- **Resolution**: 1920×1080 (1080p)
- **Duration**: 10 seconds each
- **Model**: Kling 2.6 Pro (exclusive on fal.ai)
- **Time**: ~6-10 minutes
- **Use**: Hero backgrounds, product demos

## 🎨 Customization

### Modifying Prompts

Edit `generate_website_assets.py` and customize the prompt arrays:

```python
hero_prompts = [
    "Your custom prompt here with brand colors...",
    # Add more prompts
]
```

### Adjusting Quality Settings

Higher quality (slower, more expensive):
```python
result = generator.generate_image(
    prompt=prompt,
    model="flux2_max",
    num_inference_steps=40,  # Increase from 28
    guidance_scale=4.0        # Increase from 3.5
)
```

Faster generation (lower quality):
```python
result = generator.generate_image(
    prompt=prompt,
    model="flux2_pro",
    num_inference_steps=15,  # Decrease from 28
    guidance_scale=3.0
)
```

### Changing Resolutions

```python
# Ultra-wide hero
result = generator.generate_image(
    width=3440,
    height=1440
)

# 4K resolution
result = generator.generate_image(
    width=3840,
    height=2160
)

# Square for social media
result = generator.generate_image(
    width=1200,
    height=1200
)
```

## 🔧 Advanced Configuration

### Using Different Models

#### For Images:

**FLUX.2 Max** - Best overall quality
```python
model="flux2_max"
```

**FLUX.2 Pro** - Production-optimized, faster
```python
model="flux2_pro"
```

**FLUX1.1 Pro Ultra** - 2K resolution, 6x faster
```python
model="flux11_ultra"
```

#### For Videos:

**Kling 2.6 Pro** - Latest, with optional audio
```python
model="kling_video"
duration=10  # 5 or 10 seconds
```

**Hunyuan Video 1.5** - Alternative, high quality
```python
model="hunyuan_video"
duration=5  # Max 5 seconds
```

### Video with Audio

For product demos or presentations:
```python
result = generator.generate_video(
    prompt=prompt,
    model="kling_video",
    duration=10,
    generate_audio=True  # Costs 2x
)
```

### Aspect Ratios

```python
# For videos
aspect_ratio="16:9"   # Landscape (default)
aspect_ratio="9:16"   # Portrait (mobile/social)
aspect_ratio="1:1"    # Square (social media)
```

## 💰 Cost Estimation

### Image Generation

| Model | Resolution | Cost per Image | Notes |
|-------|-----------|----------------|-------|
| FLUX.2 Max | 2560×1440 | ~$0.05-0.10 | Best quality |
| FLUX.2 Pro | 1920×1080 | ~$0.03 | Production-ready |
| FLUX1.1 Ultra | 1920×1080 | ~$0.03-0.06 | 2K, 6x faster |

### Video Generation

| Model | Duration | Cost per Video | Notes |
|-------|----------|----------------|-------|
| Kling 2.6 Pro | 10s | ~$0.70 (no audio) | Latest model |
| Kling 2.6 Pro | 10s | ~$1.40 (with audio) | 2x cost for audio |
| Hunyuan 1.5 | 5s | ~$0.38 | Alternative |

### Full Generation Run

**Total estimated cost**: $2.30 - $3.90
- 5 Hero backgrounds: $0.25-0.50
- 10 Portfolio mockups: $0.30-0.60
- 6 Service icons: $0.15-0.30
- 4 Team visuals: $0.20-0.40
- 2-3 Videos: $1.40-2.10

## 🐛 Troubleshooting

### API Key Issues

**Error**: "FAL_KEY environment variable not set"

**Solution**:
```bash
export FAL_KEY='your-api-key-from-1password'
```

### Rate Limiting

If you get rate limit errors, increase delays:

```python
time.sleep(5)  # Increase from 2 seconds
```

### Generation Failures

**Error**: "No image in response"

**Solutions**:
1. Check your API key is valid
2. Verify you have sufficient credits
3. Try a different model
4. Simplify the prompt

### Memory Issues

If running on limited memory:

```python
# Generate in smaller batches
# Comment out some generation functions
# hero_files = generate_hero_backgrounds(generator, OUTPUT_DIR)
# portfolio_files = generate_portfolio_mockups(generator, OUTPUT_DIR)
```

### Slow Generation

Video generation is intentionally slow (3-5 minutes per video). To speed up:

1. Reduce video count
2. Use shorter duration (5s instead of 10s)
3. Skip video generation entirely:

```python
# Comment out in main():
# video_files = generate_video_assets(generator, OUTPUT_DIR)
```

## 📁 Output Structure

```
/mnt/d/workspace/ISNBIZ_Files/assets/generated/
├── hero/
│   ├── hero_background_1.png
│   ├── hero_background_2.png
│   ├── hero_background_3.png
│   ├── hero_background_4.png
│   └── hero_background_5.png
├── portfolio/
│   ├── portfolio_mockup_1.png
│   ├── portfolio_mockup_2.png
│   └── ... (10 total)
├── icons/
│   ├── service_icon_1.png
│   ├── service_icon_2.png
│   └── ... (6 total)
├── team/
│   ├── team_visual_1.png
│   ├── team_visual_2.png
│   ├── team_visual_3.png
│   └── team_visual_4.png
├── video/
│   ├── hero_video_1.mp4
│   └── hero_video_2.mp4
├── manifest.json
└── README.md
```

## 🌐 Using Assets in Website

### HTML Examples

#### Hero with Static Background
```html
<section class="hero" style="background-image: url('assets/generated/hero/hero_background_1.png');">
    <div class="hero-content">
        <h1>Welcome to ISNBIZ</h1>
        <p>Professional AI & Cloud Solutions</p>
    </div>
</section>
```

#### Hero with Video Background
```html
<section class="hero">
    <video autoplay muted loop playsinline class="hero-video">
        <source src="assets/generated/video/hero_video_1.mp4" type="video/mp4">
    </video>
    <div class="hero-content">
        <h1>Innovation Powered by AI</h1>
    </div>
</section>
```

#### Portfolio Grid
```html
<div class="portfolio-grid">
    <div class="portfolio-item">
        <img src="assets/generated/portfolio/portfolio_mockup_1.png" alt="AI Chatbot">
        <h3>Opportunity Research Bot</h3>
    </div>
    <div class="portfolio-item">
        <img src="assets/generated/portfolio/portfolio_mockup_2.png" alt="Analytics Dashboard">
        <h3>Business Intelligence Platform</h3>
    </div>
</div>
```

#### Service Cards
```html
<div class="services">
    <div class="service-card">
        <img src="assets/generated/icons/service_icon_1.png" alt="AI/ML">
        <h3>AI/ML Development</h3>
        <p>Custom machine learning solutions</p>
    </div>
</div>
```

### CSS Examples

```css
/* Hero with background */
.hero {
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    height: 100vh;
    position: relative;
}

/* Video background */
.hero-video {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    z-index: -1;
}

/* Portfolio grid */
.portfolio-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
    gap: 2rem;
}

.portfolio-item img {
    width: 100%;
    height: auto;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

/* Service icons */
.service-card img {
    width: 80px;
    height: 80px;
    margin-bottom: 1rem;
}
```

## 📚 Resources

### fal.ai Documentation
- [Main Site](https://fal.ai/)
- [FLUX.2 Models](https://fal.ai/flux-2)
- [FLUX.2 Max](https://fal.ai/models/fal-ai/flux-2-max)
- [FLUX.2 Pro](https://fal.ai/models/fal-ai/flux-2-pro)
- [FLUX1.1 Pro Ultra](https://fal.ai/models/fal-ai/flux-pro/v1.1-ultra)
- [Kling 2.6 Pro](https://fal.ai/models/fal-ai/kling-video/v2.6/pro/text-to-video)
- [Hunyuan Video 1.5](https://fal.ai/models/fal-ai/hunyuan-video-v1.5/text-to-video)

### Model Information
- [Black Forest Labs (FLUX creators)](https://blackforestlabs.ai/)
- [Kling AI by Kuaishou](https://klingai.com/)
- [Hunyuan Video by Tencent](https://github.com/Tencent/HunyuanVideo)

## 🔄 Re-generation

To regenerate specific categories only:

```python
# Edit main() function in generate_website_assets.py
def main():
    generator = FalAIGenerator(FAL_API_KEY)

    # Comment out categories you don't want to regenerate
    hero_files = generate_hero_backgrounds(generator, OUTPUT_DIR)
    # portfolio_files = generate_portfolio_mockups(generator, OUTPUT_DIR)
    # icon_files = generate_service_icons(generator, OUTPUT_DIR)
    # team_files = generate_team_visuals(generator, OUTPUT_DIR)
    # video_files = generate_video_assets(generator, OUTPUT_DIR)
```

## 🎯 Best Practices

### Prompts
- Be specific with descriptions
- Include brand colors explicitly
- Mention desired style (modern, minimalist, professional)
- Add quality keywords (award-winning, high-quality, professional)

### Quality vs. Speed
- Use FLUX.2 Max for hero/key visuals
- Use FLUX.2 Pro for icons and faster generation
- Use FLUX1.1 Ultra for mockups needing 2K resolution

### File Management
- Check manifest.json after generation
- Review all assets before integrating
- Keep originals, create optimized versions for web

### Web Optimization
After generation, optimize for web:
```bash
# Install imagemagick
sudo apt-get install imagemagick

# Optimize PNGs
for file in hero/*.png; do
    convert "$file" -quality 85 -strip "optimized_$file"
done

# Compress videos
ffmpeg -i video/hero_video_1.mp4 -vcodec libx264 -crf 23 optimized_video.mp4
```

## 💡 Tips & Tricks

1. **Batch Generation**: Run overnight for large asset sets
2. **A/B Testing**: Generate multiple variations, pick the best
3. **Consistent Style**: Use same model for related assets
4. **Version Control**: Save prompts used for each asset
5. **Backup**: Keep generated assets in version control

## 🆘 Support

For issues or questions:
1. Check this guide first
2. Review fal.ai documentation
3. Check API status at status.fal.ai
4. Verify API key and credits

---

**Last Updated**: 2026-02-01
**Models**: Latest 2026 releases from fal.ai
**Script Version**: 2.0
