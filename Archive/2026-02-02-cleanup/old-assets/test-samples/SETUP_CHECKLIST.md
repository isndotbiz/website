# fal.ai Model Testing - Setup Checklist

## Pre-Flight Checklist

Complete these steps before running tests:

### ✓ Step 1: Virtual Environment (DONE)
- [x] Virtual environment created at `/mnt/d/workspace/ISNBIZ_Files/venv_fal/`
- [x] Required packages installed: `fal-client`, `requests`

**Verify:**
```bash
source venv_fal/bin/activate
python -c "import fal_client; print('✓ fal-client installed')"
```

### ☐ Step 2: Get Real API Key (ACTION REQUIRED)

**Important:** The value `yfmv5bml45cw5jv5yf4dstk3py` is a **1Password item ID**, NOT your API key!

**Option A: From 1Password**
```
1. Open 1Password
2. Search: yfmv5bml45cw5jv5yf4dstk3py
3. Find field: "API Key" or "Secret"
4. Copy the ACTUAL key value
5. It should look like:
   - fal_xxxxxxxxxxxxxxxxxxxxxxxx
   - OR xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
   - OR long alphanumeric string (30+ chars)
```

**Option B: Generate New Key**
```
1. Visit: https://fal.ai/dashboard/keys
2. Sign in
3. Click "Create new API key"
4. Copy immediately (won't show again)
5. Save in 1Password
```

**Verify you have the right format:**
- [ ] Key is 30+ characters long
- [ ] Key is NOT "yfmv5bml45cw5jv5yf4dstk3py"
- [ ] Key looks like a random string, not readable text

### ☐ Step 3: Set Environment Variable

```bash
export FAL_KEY="your-actual-api-key-here"
```

**Verify:**
```bash
echo "First 10 chars: ${FAL_KEY:0:10}..."
echo "Key length: ${#FAL_KEY}"
```

**Expected:**
- Length should be 30+ characters
- First 10 chars should NOT be "yfmv5bml45"

### ✓ Step 4: Test Scripts Created (DONE)
- [x] `run_fal_tests.sh` - Main test runner
- [x] `quick_test_fal.py` - API verification
- [x] `test_fal_models_v2.py` - Full comparison

### ✓ Step 5: Documentation Created (DONE)
- [x] Quick start guide
- [x] Comprehensive guide
- [x] Setup instructions
- [x] Troubleshooting guide

## Running Tests

### Quick Verification Test (30 seconds)

**Purpose:** Confirm your API key works

```bash
cd /mnt/d/workspace/ISNBIZ_Files
source venv_fal/bin/activate
export FAL_KEY="your-actual-api-key"
./scripts/run_fal_tests.sh
# Choose option 1
```

**Success looks like:**
```
================================================================================
API KEY VERIFICATION: SUCCESS!
================================================================================

Test image saved to: assets/test-samples/api_test_success.png
Your API key is working correctly!
```

**Failure looks like:**
```
ERROR: Cannot access application... Authentication is required
```
→ You're using wrong key. Get the real one from 1Password.

### Full Model Comparison (2-5 minutes)

**Purpose:** Test all 4 models, generate comparison images

```bash
./scripts/run_fal_tests.sh
# Choose option 2
```

**What happens:**
1. Tests `nano-banana-pro` (2 images)
2. Tests `nano-banana-pro/edit` (1 image)
3. Tests `gpt-image-1.5/edit` (1 image)
4. Tests `flux-pro/kontext` (2 images)
5. Generates comparison report

**Output:**
```
assets/test-samples/
├── nano-banana-pro_abstract_tech_1.png
├── nano-banana-pro_ai_icon_1.png
├── nano-banana-pro-edit_enhancement_1.png
├── gpt-image-1.5-edit_style_1.png
├── flux-pro-kontext_background_1.png
├── flux-pro-kontext_lighting_1.png
└── model_comparison_report.md
```

## Verification Steps

After running tests, verify:

### Check 1: Images Generated
```bash
ls -lh assets/test-samples/*.png
```

**Expected:** 6-8 PNG files

### Check 2: Report Created
```bash
cat assets/test-samples/model_comparison_report.md
```

**Expected:** Markdown report with all test results

### Check 3: Visual Quality
```bash
# Open images to review quality
open assets/test-samples/*.png  # Mac
xdg-open assets/test-samples/*.png  # Linux
explorer assets/test-samples  # Windows
```

**Look for:**
- ✓ Brand colors present (#1E9FF2, #5FDFDF)
- ✓ Professional appearance
- ✓ Clear, high resolution
- ✓ Matches prompt description

## Troubleshooting

### Problem: "FAL_KEY environment variable not set"

**Solution:**
```bash
export FAL_KEY="your-actual-api-key"
```

### Problem: "Cannot access application... Authentication is required"

**Root Cause:** Wrong API key (likely using 1Password item ID)

**Solution:**
1. Open 1Password entry
2. Find ACTUAL API key field
3. Copy that value
4. Use it instead

### Problem: "Module not found: fal_client"

**Solution:**
```bash
source venv_fal/bin/activate
pip install fal-client requests
```

### Problem: Tests run but no images generated

**Causes:**
- Network issues
- API rate limits
- Account credit issues

**Solution:**
1. Check internet connection
2. Check fal.ai account status
3. Verify API key has proper permissions
4. Check account credits/billing

### Problem: Images generated but low quality

**Solution:**
- Review prompts in `test_fal_models_v2.py`
- Adjust resolution settings (1K → 2K → 4K)
- Try different models
- Refine prompt wording

## Next Steps

After successful testing:

1. **Review Images**
   - Open all generated images
   - Compare quality across models
   - Note which ones best match your needs

2. **Read Report**
   - Open `model_comparison_report.md`
   - Review settings used for each
   - Check recommendations

3. **Make Decisions**
   - Which model for hero images?
   - Which model for icons?
   - Which model for photo editing?
   - Cost vs quality tradeoffs?

4. **Document Choices**
   - Note which model works best for each use case
   - Save successful prompts
   - Plan production image generation

5. **Production Run**
   - Use selected model(s)
   - Generate final website assets
   - Implement in website

## Quick Reference

**Test scripts location:**
```
/mnt/d/workspace/ISNBIZ_Files/scripts/
├── run_fal_tests.sh          ← START HERE
├── quick_test_fal.py         ← API verification
└── test_fal_models_v2.py     ← Full comparison
```

**Output location:**
```
/mnt/d/workspace/ISNBIZ_Files/assets/test-samples/
├── (test images here)
└── model_comparison_report.md
```

**Documentation:**
```
/mnt/d/workspace/ISNBIZ_Files/
├── FAL_MODEL_TESTING_QUICKSTART.md  ← TL;DR guide
├── TESTING_COMPLETE_SUMMARY.md      ← Complete overview
└── docs/FAL_MODEL_COMPARISON_GUIDE.md  ← Detailed guide
```

## Common Commands

**Activate environment:**
```bash
source venv_fal/bin/activate
```

**Set API key:**
```bash
export FAL_KEY="your-actual-api-key"
```

**Run quick test:**
```bash
./scripts/run_fal_tests.sh  # Choose 1
```

**Run full comparison:**
```bash
./scripts/run_fal_tests.sh  # Choose 2
```

**View results:**
```bash
cat assets/test-samples/model_comparison_report.md
ls -lh assets/test-samples/*.png
```

---

## Ready to Start?

- [ ] Got actual API key from 1Password (NOT the item ID)
- [ ] Set environment variable: `export FAL_KEY="..."`
- [ ] Verified key is set: `echo ${FAL_KEY:0:10}...`
- [ ] Run: `./scripts/run_fal_tests.sh`

**Go!**
