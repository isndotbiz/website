# Professional Website Assets - Generated with fal.ai (2026 Models)

## Overview

This directory contains professional website assets generated using the **latest 2026 AI models** from fal.ai:

### Models Used

#### Image Generation
- **FLUX.2 [max]** - State-of-the-art image generation with exceptional realism, precision, and consistency
- **FLUX.2 [pro]** - Studio-grade images with zero-configuration, production-optimized pipeline
- **FLUX1.1 [pro] ultra** - 2K resolution with improved photo realism, 6x faster than previous versions

#### Video Generation
- **Kling 2.6 Pro** - Latest video generation with native audio support (exclusive on fal.ai)
- **Hunyuan Video 1.5** - Alternative high-quality text-to-video generation

## Brand Colors

All assets are generated using the following brand color palette:

- **Blue**: `#1E9FF2` - Primary brand color
- **Cyan**: `#5FDFDF` - Accent and highlight color
- **Charcoal**: `#3F4447` - Dark backgrounds and text

## Asset Categories

### 1. Hero Backgrounds (`/hero/`)
**Count**: 5 variations
**Resolution**: 2560×1440 (QHD)
**Model**: FLUX.2 Max
**Format**: PNG

Professional hero section backgrounds featuring:
- Abstract tech/AI themes
- Neural network patterns
- Futuristic holographic interfaces
- Data visualization concepts
- Modern geometric designs

### 2. Portfolio Mockups (`/portfolio/`)
**Count**: 10+ images
**Resolution**: 1920×1080 (Full HD)
**Model**: FLUX1.1 Pro Ultra
**Format**: PNG

High-fidelity UI/UX mockups including:
- AI chatbot interfaces
- Analytics dashboards
- Mobile app screens
- Code editor screenshots
- Data visualization platforms
- SaaS application interfaces
- Cloud architecture diagrams
- Security monitoring dashboards
- ML training interfaces
- API documentation portals

### 3. Service Icons (`/icons/`)
**Count**: 6 custom icons
**Resolution**: 1024×1024
**Model**: FLUX.2 Pro
**Format**: PNG

Minimalist service icons for:
1. AI/ML development
2. Cloud architecture
3. Mobile development
4. Data engineering
5. Security & compliance
6. Custom development

### 4. Team/About Visuals (`/team/`)
**Count**: 4 images
**Resolution**: 1920×1080
**Model**: FLUX.2 Max
**Format**: PNG

Professional imagery featuring:
- Abstract collaboration concepts
- Technology innovation themes
- Modern office environments
- Team networking visualizations

### 5. Video Assets (`/video/`)
**Count**: 2-3 videos
**Duration**: 10 seconds each
**Resolution**: 1080p
**Model**: Kling 2.6 Pro
**Format**: MP4

Looping hero background videos:
- Abstract tech particle animations
- Neural network visualizations
- Futuristic data center walkthroughs
- Professional motion graphics

## Setup & Generation

### Prerequisites

1. **Python 3.8+** installed
2. **fal.ai API Key** - Get from 1Password (search for "fal")

### Installation

```bash
# Install required dependencies
pip install requests

# Set your API key
export FAL_KEY="your-fal-api-key-here"
```

### Generate Assets

```bash
# Navigate to scripts directory
cd /mnt/d/workspace/ISNBIZ_Files/scripts

# Run the generator
python3 generate_website_assets.py
```

The script will:
1. Generate 5 hero backgrounds (~2-3 minutes)
2. Generate 10 portfolio mockups (~3-4 minutes)
3. Generate 6 service icons (~2 minutes)
4. Generate 4 team visuals (~2 minutes)
5. Generate 2-3 video assets (~6-10 minutes)

**Total estimated time**: 15-20 minutes

### Output

All assets will be saved to:
```
/mnt/d/workspace/ISNBIZ_Files/assets/generated/
├── hero/
│   ├── hero_background_1.png
│   ├── hero_background_2.png
│   └── ...
├── portfolio/
│   ├── portfolio_mockup_1.png
│   ├── portfolio_mockup_2.png
│   └── ...
├── icons/
│   ├── service_icon_1.png
│   ├── service_icon_2.png
│   └── ...
├── team/
│   ├── team_visual_1.png
│   ├── team_visual_2.png
│   └── ...
├── video/
│   ├── hero_video_1.mp4
│   └── hero_video_2.mp4
└── manifest.json
```

## Manifest File

The `manifest.json` file contains:
- Generation timestamp
- Total asset count
- Models used
- Brand colors
- Complete file listing

## Usage in Website

### Hero Sections

```html
<!-- Static background -->
<div class="hero" style="background-image: url('assets/generated/hero/hero_background_1.png');">
  <!-- Hero content -->
</div>

<!-- Video background -->
<div class="hero">
  <video autoplay muted loop playsinline>
    <source src="assets/generated/video/hero_video_1.mp4" type="video/mp4">
  </video>
  <!-- Hero content -->
</div>
```

### Portfolio Grid

```html
<div class="portfolio-grid">
  <img src="assets/generated/portfolio/portfolio_mockup_1.png" alt="AI Chatbot Interface">
  <img src="assets/generated/portfolio/portfolio_mockup_2.png" alt="Analytics Dashboard">
  <!-- More portfolio items -->
</div>
```

### Service Icons

```html
<div class="services">
  <div class="service-card">
    <img src="assets/generated/icons/service_icon_1.png" alt="AI/ML Development">
    <h3>AI/ML Development</h3>
  </div>
  <!-- More services -->
</div>
```

## Model Information

### FLUX.2 [max]
- **Provider**: Black Forest Labs via fal.ai
- **Strengths**: Exceptional realism, precision, consistency
- **Best for**: Hero backgrounds, photorealistic visuals
- **Pricing**: ~$0.05-0.10 per generation

### FLUX1.1 [pro] ultra
- **Provider**: Black Forest Labs via fal.ai
- **Strengths**: 2K resolution, 6x faster generation
- **Best for**: Detailed mockups, UI screenshots
- **Pricing**: ~$0.03-0.06 per generation

### FLUX.2 [pro]
- **Provider**: Black Forest Labs via fal.ai
- **Strengths**: Studio-grade quality, production-optimized
- **Best for**: Icons, clean graphics
- **Pricing**: ~$0.03 per generation

### Kling 2.6 Pro
- **Provider**: Kuaishou via fal.ai
- **Strengths**: Latest video model with native audio
- **Best for**: Hero background videos, animations
- **Pricing**: ~$0.07/second (without audio)

## Resources

- [fal.ai Documentation](https://fal.ai/)
- [FLUX.2 Models](https://fal.ai/flux-2)
- [Kling Video API](https://fal.ai/models/fal-ai/kling-video/v2.6/pro/text-to-video)
- [Hunyuan Video](https://fal.ai/models/fal-ai/hunyuan-video-v1.5/text-to-video)

## License

Generated assets are for use in the ISNBIZ professional website. Commercial use rights are included via fal.ai's API license.

---

**Generated**: 2026-02-01
**Models**: Latest 2026 releases from fal.ai
**Quality**: Award-worthy, professional grade
