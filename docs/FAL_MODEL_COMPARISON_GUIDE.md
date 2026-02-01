# fal.ai Model Comparison Guide

## Overview

This guide walks you through testing and comparing 4 different fal.ai image generation models to determine which ones work best for your ISNBIZ website and marketing materials.

## Models to Test

1. **fal-ai/nano-banana-pro** - Fast text-to-image generation
2. **fal-ai/nano-banana-pro/edit** - Image editing and enhancement
3. **fal-ai/gpt-image-1.5/edit** - Advanced AI-powered image editing
4. **fal-ai/flux-pro/kontext** - Context-aware image editing with subject preservation

## Prerequisites

### 1. Get Your Actual fal.ai API Key

**Important:** The value `yfmv5bml45cw5jv5yf4dstk3py` is a **1Password item ID**, not your actual API key.

**To retrieve your actual API key:**

#### Option A: From 1Password
1. Open 1Password desktop app or browser extension
2. Search for "FAL API Key" (item ID: yfmv5bml45cw5jv5yf4dstk3py)
3. Look for a field labeled "API Key", "Secret Key", or similar
4. Copy the **full key value** (not the item reference)
5. Real API keys typically look like:
   - `fal_xxxxxxxxxxxxxxxxxxxxxxxxxxxx` (starts with "fal_")
   - `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx` (UUID format)
   - Or a long random alphanumeric string

#### Option B: Generate a New Key from fal.ai
1. Visit https://fal.ai/
2. Sign in to your account
3. Go to **Dashboard** → **Settings** → **API Keys**
4. Click **"Create new API key"**
5. Copy the generated key immediately (it won't be shown again)
6. Save it securely in 1Password

### 2. Set Up Python Environment

```bash
# Navigate to workspace
cd /mnt/d/workspace/ISNBIZ_Files

# Activate virtual environment (already created)
source venv_fal/bin/activate

# Verify packages are installed
pip list | grep fal
```

You should see:
- `fal-client`
- `requests`

## Step-by-Step Testing Process

### Step 1: Set Your API Key

```bash
# Replace YOUR_ACTUAL_API_KEY with the real key from 1Password or fal.ai
export FAL_KEY="YOUR_ACTUAL_API_KEY"

# Verify it's set (will show first 10 characters)
echo ${FAL_KEY:0:10}...
```

### Step 2: Quick API Verification Test

Before running the full test suite, verify your API key works:

```bash
python scripts/quick_test_fal.py
```

**Expected output if successful:**
```
==============================================================================
API KEY VERIFICATION: SUCCESS!
==============================================================================

Test image saved to: /mnt/d/workspace/ISNBIZ_Files/assets/test-samples/api_test_success.png

Your API key is working correctly!
```

**If it fails:**
- Double-check you copied the actual API key, not the 1Password item ID
- Verify the key hasn't expired
- Check for typos or extra spaces

### Step 3: Run Full Model Comparison

Once the quick test succeeds, run the comprehensive comparison:

```bash
python scripts/test_fal_models_v2.py
```

This will:
1. Test each of the 4 models
2. Generate 2-3 sample images per model
3. Save all images to `assets/test-samples/`
4. Create a detailed comparison report

**Expected runtime:** 2-5 minutes (depends on API response times)

### Step 4: Review Results

Open the comparison report:

```bash
# View the markdown report
cat assets/test-samples/model_comparison_report.md

# Or open in your preferred markdown viewer
```

Check the generated images in:
```
/mnt/d/workspace/ISNBIZ_Files/assets/test-samples/
```

## Understanding the Results

### Image Files

Each image follows this naming convention:
```
{model-name}_{test-type}_{number}.png
```

Examples:
- `nano-banana-pro_abstract_tech_1.png` - Abstract tech background
- `nano-banana-pro_ai_icon_1.png` - AI/ML service icon
- `flux-pro-kontext_background_1.png` - Background transformation test
- `flux-pro-kontext_lighting_1.png` - Lighting enhancement test

### Comparison Report

The report includes for each model:
- **Description** - What the model does best
- **Test prompts** - Exact prompts used
- **Settings** - Parameters and configuration
- **Output images** - Visual results with embedded images
- **Recommendations** - Suggested use cases

## Brand Color Integration

All test prompts incorporate ISNBIZ brand colors:
- **Primary Blue:** `#1E9FF2`
- **Accent Cyan:** `#5FDFDF`

This ensures the test images reflect your actual branding needs.

## Test Scenarios

### Test 1: Abstract Tech Background (nano-banana-pro)
**Purpose:** Hero section backgrounds for website
**Settings:**
- Aspect ratio: 16:9 (standard web)
- Resolution: 2K (high quality)
- Style: Modern, professional, minimalist

### Test 2: Service Icon/Illustration (nano-banana-pro)
**Purpose:** Icons for service sections, features, capabilities
**Settings:**
- Aspect ratio: 1:1 (square icons)
- Resolution: 2K
- Style: Clean, professional, tech-focused

### Test 3: Professional Enhancement (nano-banana-pro/edit)
**Purpose:** Enhance existing images with better lighting and effects
**Settings:**
- Resolution: 2K
- Edit type: Enhancement (non-destructive)

### Test 4: Style Transfer (gpt-image-1.5/edit)
**Purpose:** Transform images to match corporate style guide
**Settings:**
- Advanced AI understanding
- Natural language edit instructions

### Test 5: Background Transformation (flux-pro/kontext)
**Purpose:** Change backgrounds while preserving subjects
**Settings:**
- Guidance scale: 7.5 (strong prompt adherence)
- Inference steps: 50 (high quality)

### Test 6: Lighting Enhancement (flux-pro/kontext)
**Purpose:** Professional lighting and color grading
**Settings:**
- Guidance scale: 7.0
- Inference steps: 40

## Making Your Decision

After reviewing all results, evaluate each model based on:

### Quality Metrics
- ✓ **Visual quality** - Clarity, detail, professional appearance
- ✓ **Brand alignment** - Does it match ISNBIZ aesthetic?
- ✓ **Color accuracy** - Are brand colors rendered correctly?
- ✓ **Prompt adherence** - Does output match the request?

### Practical Considerations
- ✓ **Generation speed** - How fast does it produce results?
- ✓ **Cost per image** - Check fal.ai pricing for each model
- ✓ **Use case fit** - Which model works best for your specific needs?
- ✓ **Consistency** - Do multiple generations maintain quality?

## Recommended Workflow

Based on typical use cases:

### For Website Hero Images
**Best choice:** `fal-ai/nano-banana-pro`
- Fast generation
- High quality
- Good for abstract backgrounds
- Cost-effective

### For Service Icons/Illustrations
**Best choice:** `fal-ai/nano-banana-pro`
- Clean, professional output
- Suitable for minimalist designs
- Consistent style

### For Photo Enhancements
**Best choice:** `fal-ai/gpt-image-1.5/edit` or `fal-ai/flux-pro/kontext`
- Advanced editing capabilities
- Natural language understanding
- Professional-grade results

### For Background Replacements
**Best choice:** `fal-ai/flux-pro/kontext`
- Excellent subject preservation
- Context-aware editing
- Realistic composition

## Next Steps

After selecting your preferred model(s):

1. **Document your choice** - Note which model(s) work best for which purposes
2. **Create production prompts** - Refine prompts based on test results
3. **Generate final assets** - Produce your actual website images
4. **Cost analysis** - Calculate total cost based on number of images needed
5. **Quality control** - Review all generated images before publishing

## Troubleshooting

### "Cannot access application... Authentication is required"
- You're using the 1Password item ID instead of the actual API key
- Get the real key from 1Password or generate a new one from fal.ai

### "FAL_KEY environment variable not set"
```bash
export FAL_KEY="your-actual-api-key-here"
```

### Images look wrong or low quality
- Adjust prompt wording
- Try different resolution settings (1K vs 2K vs 4K)
- Test different aspect ratios
- Modify guidance_scale for editing models

### Generation takes too long
- nano-banana-pro is fastest (use for bulk generation)
- flux-pro/kontext is slower but higher quality
- Balance speed vs quality based on your needs

### API rate limits
- Add `time.sleep(2)` between requests (already in script)
- Check your fal.ai account for rate limit details
- Upgrade plan if needed for higher throughput

## Cost Optimization Tips

1. **Use nano-banana-pro for bulk generation** - Most cost-effective
2. **Reserve premium models for hero images** - Use flux-pro/kontext selectively
3. **Generate at appropriate resolution** - Don't use 4K if 2K suffices
4. **Batch your requests** - Plan all images before generating
5. **Reuse successful prompts** - Document what works to avoid regeneration

## Resources

- **fal.ai Documentation:** https://fal.ai/docs
- **Model Pricing:** https://fal.ai/pricing
- **API Reference:** https://fal.ai/docs/api-reference
- **Community Examples:** https://fal.ai/explore

## Support

If you encounter issues:
1. Check the troubleshooting section above
2. Review fal.ai documentation
3. Verify API key is valid and active
4. Check account credits/billing status
5. Contact fal.ai support if technical issues persist

---

**Last Updated:** 2026-02-01
