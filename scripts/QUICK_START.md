# Quick Start Guide - fal.ai Asset Generator

## 🚀 Get Started in 3 Steps

### Step 1: Get Your API Key

```bash
# Open 1Password and search for "fal"
# Copy the API key
```

### Step 2: Set Environment Variable

```bash
export FAL_KEY="your-api-key-from-1password"
```

### Step 3: Run the Generator

```bash
cd /mnt/d/workspace/ISNBIZ_Files/scripts
./setup_and_run_generator.sh
```

That's it! Your assets will be generated in `/mnt/d/workspace/ISNBIZ_Files/assets/generated/`

---

## 🎯 What You'll Get

```
27 Professional Assets:
  ✓ 5 Hero Backgrounds (2560x1440)
  ✓ 10 Portfolio Mockups (1920x1440)
  ✓ 6 Service Icons (1024x1024)
  ✓ 4 Team Visuals (2560x1440)
  ✓ 2 Video Assets (1080p, 8s)
```

---

## 💰 Cost & Time

- **Cost**: ~$5-6 USD
- **Time**: 10-20 minutes
- **Quality**: Professional, award-worthy

---

## 🎨 Your Brand Colors

All assets automatically use:
- **Blue**: #1E9FF2
- **Cyan**: #5FDFDF
- **Charcoal**: #3F4447

---

## 📋 Models Used

- **FLUX.2 Pro**: Best image quality (2026)
- **Veo 3**: Google's latest video AI

---

## 🔍 Preview Results

After generation, check:
```bash
ls -lh /mnt/d/workspace/ISNBIZ_Files/assets/generated/
```

View manifest:
```bash
cat /mnt/d/workspace/ISNBIZ_Files/assets/generated/manifest.json
```

---

## 🛠️ Troubleshooting

**API key not working?**
```bash
echo $FAL_KEY  # Should show your key
```

**Python not found?**
```bash
python3 --version  # Need 3.8+
```

**Missing dependencies?**
```bash
pip install requests
```

---

## 📞 Need Help?

See full documentation: `ASSET_GENERATOR_README.md`
