# fal.ai Model Testing - Quick Start

## TL;DR - Get Started in 3 Steps

```bash
# 1. Get your ACTUAL API key (not the 1Password item ID!)
#    Open 1Password → "FAL API Key" → Copy the actual key value
export FAL_KEY="your-real-api-key-from-1password"

# 2. Run the test script
./scripts/run_fal_tests.sh

# 3. Choose option 1 for quick test, option 2 for full comparison
```

## Important: About Your API Key

**The value `yfmv5bml45cw5jv5yf4dstk3py` is NOT your API key!**

This is a **1Password item ID**. You need to open the actual 1Password entry and copy the real API key.

### How to Get Your Real API Key

**Option 1: From 1Password**
1. Open 1Password
2. Search for item ID: `yfmv5bml45cw5jv5yf4dstk3py`
3. Find the field labeled "API Key" or "Secret"
4. Copy that value (should be much longer, looks like `fal_xxxxx...` or a UUID)

**Option 2: Generate New Key**
1. Go to https://fal.ai/
2. Sign in
3. Dashboard → Settings → API Keys
4. Create new key
5. Copy and save securely

## What This Does

Tests 4 different fal.ai models with your brand colors (#1E9FF2, #5FDFDF):

1. **nano-banana-pro** - Fast text-to-image
2. **nano-banana-pro/edit** - Image editing
3. **gpt-image-1.5/edit** - Advanced AI editing
4. **flux-pro/kontext** - Context-aware editing

## Output

- **Test images:** `assets/test-samples/*.png`
- **Comparison report:** `assets/test-samples/model_comparison_report.md`

## Use Cases Tested

✓ Abstract tech backgrounds (16:9, for hero sections)
✓ AI/ML service icons (1:1, professional illustrations)
✓ Image enhancements (lighting, effects)
✓ Background transformations
✓ Professional color grading

## After Testing

Review the generated images and report to decide:
- Which model for hero images?
- Which model for icons?
- Which model for photo editing?
- Cost vs quality tradeoffs

## Need Help?

See full documentation: `docs/FAL_MODEL_COMPARISON_GUIDE.md`

## Files Created

```
/mnt/d/workspace/ISNBIZ_Files/
├── scripts/
│   ├── run_fal_tests.sh          # Main test runner (use this!)
│   ├── quick_test_fal.py         # API verification
│   └── test_fal_models_v2.py     # Full comparison suite
├── assets/test-samples/
│   ├── README.md                  # Detailed setup guide
│   └── (generated images here)
├── docs/
│   └── FAL_MODEL_COMPARISON_GUIDE.md  # Complete documentation
└── FAL_MODEL_TESTING_QUICKSTART.md    # This file
```

---

**Ready?** Run `./scripts/run_fal_tests.sh` to begin!
