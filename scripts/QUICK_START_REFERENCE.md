# Quick Start Reference - Website Asset Generator

## 🚀 3-Step Generation

### Step 1: Get API Key
```bash
# Open 1Password and search for "fal"
# Copy the API key
```

### Step 2: Set Environment Variable
```bash
export FAL_KEY='your-fal-api-key-from-1password'
```

### Step 3: Run Generator
```bash
cd /mnt/d/workspace/ISNBIZ_Files/scripts
./setup_and_generate.sh
```

## 📊 What You'll Get

| Asset Type | Count | Resolution | Time | Cost |
|------------|-------|------------|------|------|
| Hero Backgrounds | 5 | 2560×1440 | 2-3 min | $0.25-0.50 |
| Portfolio Mockups | 10 | 1920×1080 | 3-4 min | $0.30-0.60 |
| Service Icons | 6 | 1024×1024 | 2 min | $0.15-0.30 |
| Team Visuals | 4 | 1920×1080 | 2 min | $0.20-0.40 |
| Video Assets | 2-3 | 1080p | 6-10 min | $1.40-2.10 |
| **TOTAL** | **27** | **Various** | **15-20 min** | **$2.30-3.90** |

## 🎨 Latest 2026 Models Used

- **FLUX.2 Max** - Best quality (hero backgrounds, team visuals)
- **FLUX1.1 Pro Ultra** - 2K resolution, 6x faster (portfolio mockups)
- **FLUX.2 Pro** - Production-optimized (service icons)
- **Kling 2.6 Pro** - Latest video with native audio

## 📁 Output Location

```
/mnt/d/workspace/ISNBIZ_Files/assets/generated/
├── hero/          ← 5 backgrounds (2560×1440)
├── portfolio/     ← 10 mockups (1920×1080)
├── icons/         ← 6 icons (1024×1024)
├── team/          ← 4 visuals (1920×1080)
├── video/         ← 2-3 videos (1080p, 10s)
└── manifest.json  ← Generation metadata
```

## 🎯 Brand Colors (Auto-Applied)

- **Blue**: `#1E9FF2` - Primary
- **Cyan**: `#5FDFDF` - Accent
- **Charcoal**: `#3F4447` - Dark/Text

## 📖 Documentation

- **Full Guide**: `/scripts/USAGE_GUIDE.md`
- **Project Summary**: `/scripts/PROJECT_SUMMARY.md`
- **Asset Docs**: `/assets/generated/README.md`

## 🔧 Manual Execution

```bash
# Install dependencies
pip install -r requirements.txt

# Set API key
export FAL_KEY='your-api-key'

# Run directly
python3 generate_website_assets.py
```

## ⚡ Quick Customization

### Change Quality
Edit `generate_website_assets.py`:
```python
# Higher quality (slower)
num_inference_steps=40
guidance_scale=4.0
```

### Skip Videos (Faster)
Comment out in `main()`:
```python
# video_files = generate_video_assets(generator, OUTPUT_DIR)
```

## 🆘 Troubleshooting

| Issue | Solution |
|-------|----------|
| API key error | `export FAL_KEY='your-key'` |
| Rate limiting | Increase `time.sleep(5)` in script |
| Out of credits | Check fal.ai account balance |
| Generation fails | Try different model or simplify prompt |

## 📞 Need Help?

1. Check `USAGE_GUIDE.md` for detailed instructions
2. Review fal.ai documentation: https://fal.ai/
3. Verify API key in 1Password

---

**Ready to generate professional website assets in 15-20 minutes!**
