# Professional Website Asset Generator - fal.ai

Generate award-winning website assets using the latest 2026 AI models from fal.ai.

## 🚀 Latest Models Used (2026)

### FLUX.2 Pro - Image Generation
- **State-of-the-art** text-to-image model from Black Forest Labs
- **Best image quality** on the market (January 2026)
- Zero-config operation - no inference steps or guidance scales
- Supports resolutions up to 4MP
- Precise color control using HEX codes
- **Cost**: $0.03/megapixel
- [Model Documentation](https://fal.ai/models/fal-ai/flux-2-pro)

**Why FLUX.2 Pro?**
- Highest quality professional imagery
- Superior prompt adherence
- Exceptional detail and realism
- Studio-grade output quality

### Veo 3 - Video Generation
- **Google's most advanced** video generation model
- Realistic motion and cinematic quality
- Supports 720p/1080p resolution
- 4s, 6s, or 8s duration options
- Optional audio generation
- **Cost**: $0.20/second (no audio), $0.40/second (with audio)
- [Model Documentation](https://fal.ai/models/fal-ai/veo3/api)

**Why Veo 3?**
- Industry-leading video quality
- Smooth, realistic motion
- Perfect for hero section backgrounds
- Professional cinematic output

### Alternative Models Available

If you need different capabilities, fal.ai also offers:

- **FLUX.2 Dev Turbo**: Ultra-fast generation (6.6s for 1024x1024) at $0.008/image
- **FLUX 1.1 Pro**: Highest Elo score, fastest in class
- **Sora 2**: OpenAI's latest video generation
- **Kling 2.5 Turbo Pro**: Exceptional motion fluidity
- **LTX 2.0**: Advanced image-to-video

## 📦 What Gets Generated

### 1. Hero Backgrounds (5 variations)
- **Resolution**: 2560x1440 (landscape_16_9)
- **Format**: PNG
- **Themes**:
  - Abstract neural networks
  - Futuristic AI dashboards
  - Particle systems
  - Modern workspaces
  - Geometric mesh networks
- All using your brand colors

### 2. Portfolio Mockups (10 images)
- **Resolution**: 1920x1440 (landscape_4_3)
- **Format**: PNG
- **Types**:
  - AI chatbot interfaces
  - Analytics dashboards
  - Mobile app screenshots
  - Code editor mockups
  - Data visualizations
  - Cloud architecture diagrams
  - CRM interfaces
  - Security dashboards
  - ML training interfaces
  - API documentation portals

### 3. Service Icons (6 custom icons)
- **Resolution**: 1024x1024 (square_hd)
- **Format**: PNG
- **Icons**:
  - AI/ML
  - Cloud Architecture
  - Mobile Development
  - Data Engineering
  - Security/Compliance
  - Custom Development
- Minimalist, professional, brand-aligned

### 4. Team/About Visuals (4 images)
- **Resolution**: 2560x1440 (landscape_16_9)
- **Format**: PNG
- **Themes**:
  - Team collaboration
  - Innovation & technology
  - Professional office environments
  - Teamwork concepts

### 5. Video Assets (2 videos)
- **Resolution**: 1920x1080 (1080p)
- **Duration**: 8 seconds (loopable)
- **Format**: MP4
- **Content**:
  - Flowing tech particles
  - Futuristic data center flythrough
- No audio (perfect for background videos)

## 🎨 Brand Colors

All assets are generated using your brand color palette:

```
Blue:     #1E9FF2  (Primary - Electric Blue)
Cyan:     #5FDFDF  (Secondary - Bright Cyan)
Charcoal: #3F4447  (Accent - Dark Charcoal)
```

## ⚙️ Setup & Installation

### Prerequisites

1. **Python 3.8+**
2. **fal.ai API Key** - Get from 1Password (search for "fal")
3. **requests** package (auto-installed by setup script)

### Quick Start

```bash
# Option 1: Run setup script (recommended)
cd /mnt/d/workspace/ISNBIZ_Files/scripts
./setup_and_run_generator.sh

# Option 2: Manual setup
export FAL_KEY="your-api-key-here"
python3 generate_website_assets.py
```

The setup script will:
- Check for API key
- Install dependencies
- Create output directories
- Run the generator

## 📁 Output Structure

Generated assets are saved to:

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
│   ├── ... (10 total)
│   └── portfolio_mockup_10.png
├── icons/
│   ├── service_icon_1.png (AI/ML)
│   ├── service_icon_2.png (Cloud)
│   ├── service_icon_3.png (Mobile)
│   ├── service_icon_4.png (Data)
│   ├── service_icon_5.png (Security)
│   └── service_icon_6.png (Custom)
├── team/
│   ├── team_visual_1.png
│   ├── team_visual_2.png
│   ├── team_visual_3.png
│   └── team_visual_4.png
├── video/
│   ├── hero_video_1.mp4
│   └── hero_video_2.mp4
└── manifest.json (metadata about all generated assets)
```

## 💰 Cost Estimate

Based on fal.ai pricing (January 2026):

| Asset Type | Count | Resolution | Cost per Item | Total |
|------------|-------|------------|---------------|-------|
| Hero Backgrounds | 5 | 2560x1440 | ~$0.11 | $0.55 |
| Portfolio Mockups | 10 | 1920x1440 | ~$0.08 | $0.80 |
| Service Icons | 6 | 1024x1024 | ~$0.03 | $0.18 |
| Team Visuals | 4 | 2560x1440 | ~$0.11 | $0.44 |
| Video Assets | 2 | 1080p, 8s | $1.60 | $3.20 |

**Total Estimated Cost: $5-6 USD**

*Actual costs may vary based on fal.ai's current pricing and any account credits.*

## ⏱️ Generation Time

- **Images**: ~5-10 seconds per image
- **Videos**: ~2-5 minutes per video
- **Total Time**: 10-20 minutes for all assets

## 🔧 Customization

### Modify Prompts

Edit the prompt lists in `generate_website_assets.py`:
- `hero_prompts` - Hero backgrounds
- `portfolio_prompts` - Portfolio mockups
- `icon_prompts` - Service icons
- `team_prompts` - Team visuals
- `video_prompts` - Video assets

### Change Image Sizes

Available sizes for FLUX.2 Pro:
- `landscape_16_9` - 2560x1440
- `landscape_4_3` - 1920x1440
- `square_hd` - 1024x1024
- `square` - 512x512
- `portrait_4_3` - 1440x1920
- `portrait_16_9` - 1440x2560

### Adjust Video Parameters

For Veo 3 videos:
- **Duration**: "4s", "6s", "8s"
- **Resolution**: "720p", "1080p"
- **Aspect Ratio**: "16:9", "9:16"
- **Audio**: `True` or `False`

## 📊 Output Manifest

After generation, a `manifest.json` file is created with:

```json
{
  "generated_at": "2026-02-01 12:00:00",
  "total_assets": 27,
  "models_used": ["FLUX.2 Pro", "Veo 3"],
  "brand_colors": {
    "blue": "#1E9FF2",
    "cyan": "#5FDFDF",
    "charcoal": "#3F4447"
  },
  "files": {
    "hero_backgrounds": [...],
    "portfolio_mockups": [...],
    "service_icons": [...],
    "team_visuals": [...],
    "video_assets": [...]
  }
}
```

## 🚨 Troubleshooting

### API Key Issues

```bash
# Check if key is set
echo $FAL_KEY

# Set manually if needed
export FAL_KEY="your-key-here"
```

### Rate Limiting

The script includes 2-5 second delays between requests. If you hit rate limits:
- Increase delays in the code
- Run in smaller batches
- Check your fal.ai account limits

### Failed Generations

If some assets fail to generate:
- Check the error messages
- Verify API key is valid
- Check fal.ai service status
- Review prompt for policy violations
- Adjust safety_tolerance if needed

### Dependencies

```bash
# Install required packages
pip install requests

# Or use a virtual environment
python3 -m venv venv
source venv/bin/activate
pip install requests
```

## 📚 Resources

- [fal.ai Documentation](https://docs.fal.ai/)
- [FLUX.2 Pro Model Page](https://fal.ai/models/fal-ai/flux-2-pro)
- [Veo 3 Model Page](https://fal.ai/models/fal-ai/veo3)
- [fal.ai Blog](https://blog.fal.ai/)
- [Model Explorer](https://fal.ai/explore/models)

## 🎯 Next Steps

After generation:

1. **Review Assets**: Check all generated files
2. **Select Favorites**: Choose the best versions
3. **Optimize**: Compress images/videos if needed
4. **Integrate**: Add to your website
5. **Iterate**: Regenerate any assets you want to improve

## 💡 Tips for Best Results

1. **Be Specific**: Detailed prompts = better results
2. **Brand Consistency**: Use exact HEX codes in prompts
3. **Test Variations**: Generate multiple versions
4. **Professional Language**: Use industry terms
5. **Quality Keywords**: "award-winning", "professional", "high-quality"
6. **Resolution Matters**: Choose appropriate sizes for use case

## 📝 License & Usage

Generated assets are yours to use commercially. Check fal.ai's terms of service for specific usage rights.

---

**Generated with**: FLUX.2 Pro & Veo 3 (Latest 2026 Models)
**Platform**: fal.ai
**Quality**: Professional, Award-Worthy
**Ready**: For Production Use
