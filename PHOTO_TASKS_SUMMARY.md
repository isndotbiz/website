# Founder Photo Enhancement Tasks - Summary

## Status: Ready to Run

All scripts and documentation have been created. Ready to execute when FAL API key is available.

---

## Task 1: Fix Neck Proportions

### Objective
Make Lilly and Bri's necks slightly shorter (~15% reduction) while keeping faces EXACTLY the same.

### Method
- Uses `fal.ai/gpt-image-1.5/edit` for precision editing
- Surgical editing with high fidelity to original faces
- Professional corporate headshot quality

### Input Files
```
assets/founders/headshots_no_bg/
├── lilly_headshot_no_bg.png  → Fix
└── bri_headshot_no_bg.png    → Fix
```

### Output Files
```
assets/founders/fixed_necks/
├── lilly_headshot_fixed.png  ← New
└── bri_headshot_fixed.png    ← New
```

### Expected Results
- Lilly: More balanced neck-to-head ratio
- Bri: More balanced neck-to-head ratio
- Faces remain identical (same eyes, nose, mouth, hair, expression)
- Professional quality maintained
- Same background and lighting

---

## Task 2: Create Community Outreach Photos

### Objective
Generate 8 team photos showing all 4 founders in community engagement scenarios.

### Method
- Uses `fal.ai/gpt-image-1.5` for text-to-image generation
- Detailed prompts describing each founder
- Professional documentary-style photography
- 16:9 aspect ratio

### Founders Included (All 4)
1. **Jonathan** (40s, professional man with beard and business attire)
2. **Alicia** (30s, professional woman with dark straight hair)
3. **Bri** (30s, professional woman with dark wavy hair)
4. **Lilly** (30s, professional woman with brown wavy hair)

### 8 Scenarios

#### 1. Community Center Volunteering
**Description:** Volunteering at busy community center, helping diverse people with computers
**Use Case:** Shows tech expertise helping community
**Output:** `community_01_tech_founders_volunteering.png`

#### 2. Coding Workshop
**Description:** Teaching coding workshop to enthusiastic diverse students in classroom
**Use Case:** Education outreach, STEM advocacy
**Output:** `community_02_teaching_coding_workshop.png`

#### 3. Tech Event Speaking
**Description:** Speaking at community tech event, engaging with diverse audience
**Use Case:** Thought leadership, community engagement
**Output:** `community_03_speaking_at_community_tech.png`

#### 4. Student Mentoring
**Description:** Mentoring young diverse students with laptops in modern learning space
**Use Case:** Youth development, future tech leaders
**Output:** `community_04_professional_mentors_guiding.png`

#### 5. Community Cleanup
**Description:** Participating in community cleanup day, wearing casual volunteer shirts
**Use Case:** Environmental responsibility, hands-on involvement
**Output:** `community_05_tech_team_participating_in.png`

#### 6. Food Bank Volunteering
**Description:** Volunteering at food bank, organizing donations and helping community members
**Use Case:** Social responsibility, helping those in need
**Output:** `community_06_founders_volunteering_at_fo.png`

#### 7. STEM Outreach
**Description:** Leading STEM outreach at elementary school, excited children learning
**Use Case:** Early education, inspiring young minds
**Output:** `community_07_technology_professionals_l.png`

#### 8. Charity Tech Event
**Description:** Charity tech event demonstrating technology to diverse community members
**Use Case:** Combining tech and charity, making tech accessible
**Output:** `community_08_charity_tech_event_with_fo.png`

### Output Location
```
assets/founders/community/
├── community_01_tech_founders_volunteering.png
├── community_02_teaching_coding_workshop.png
├── community_03_speaking_at_community_tech.png
├── community_04_professional_mentors_guiding.png
├── community_05_tech_team_participating_in.png
├── community_06_founders_volunteering_at_fo.png
├── community_07_technology_professionals_l.png
└── community_08_charity_tech_event_with_fo.png
```

---

## How to Run

### Quick Start (Recommended)
```bash
cd /mnt/d/workspace/ISNBIZ_Files
./scripts/run_photo_enhancement.sh
```

The script will:
1. Activate virtual environment
2. Get FAL API key from 1Password
3. Run the enhancement script
4. Show progress for all 10 images

### Manual Method
```bash
cd /mnt/d/workspace/ISNBIZ_Files
source venv_fal/bin/activate
eval $(op signin)
export FAL_KEY=$(op read "op://Research/FAL API Key/credential")
python scripts/fix_necks_and_create_community_photos.py
```

---

## Files Created

### Main Script
- **`scripts/fix_necks_and_create_community_photos.py`**
  - 270 lines of Python
  - Uses fal.ai API
  - Handles both tasks
  - Includes progress reporting
  - Rate limiting between requests

### Runner Script
- **`scripts/run_photo_enhancement.sh`**
  - Bash automation script
  - Sets up environment
  - Gets API key from 1Password
  - Runs Python script
  - Reports results

### Documentation
- **`PHOTO_ENHANCEMENT_README.md`**
  - Complete usage guide
  - Step-by-step instructions
  - Troubleshooting
  - Cost estimates
  - Advanced usage

- **`PHOTO_TASKS_SUMMARY.md`** (this file)
  - Executive summary
  - Task breakdown
  - Expected results

---

## Technical Details

### Models Used

**Task 1 (Neck Fixes):**
- Model: `fal-ai/gpt-image-1.5/edit`
- Type: Image-to-image editing
- Input: Existing founder photos
- Guidance Scale: 7.5 (subtle)
- Inference Steps: 50 (high quality)

**Task 2 (Community Photos):**
- Model: `fal-ai/gpt-image-1.5`
- Type: Text-to-image generation
- Input: Detailed text prompts
- Aspect Ratio: 16:9 (landscape)
- Guidance Scale: 7.5 (balanced)
- Inference Steps: 50 (high quality)

### Processing Flow

```
Start
  │
  ├─→ Task 1: Fix Necks (2 images)
  │     │
  │     ├─→ Load lilly_headshot_no_bg.png
  │     ├─→ Encode to base64
  │     ├─→ Submit to gpt-image-1.5/edit
  │     ├─→ Wait for result
  │     ├─→ Download image
  │     ├─→ Save to fixed_necks/lilly_headshot_fixed.png
  │     │
  │     ├─→ Load bri_headshot_no_bg.png
  │     ├─→ Encode to base64
  │     ├─→ Submit to gpt-image-1.5/edit
  │     ├─→ Wait for result
  │     ├─→ Download image
  │     └─→ Save to fixed_necks/bri_headshot_fixed.png
  │
  └─→ Task 2: Community Photos (8 images)
        │
        ├─→ For each scenario (1-8):
        │     │
        │     ├─→ Build detailed prompt
        │     ├─→ Submit to gpt-image-1.5
        │     ├─→ Wait for result
        │     ├─→ Download image
        │     ├─→ Save to community/community_XX_*.png
        │     └─→ Rate limit (2 second pause)
        │
        └─→ Print final summary
```

### Rate Limiting
- 2 second pause between requests
- 5 second pause halfway through community photos
- Prevents API rate limit errors
- Total runtime: ~5-10 minutes

---

## Cost Estimate

### fal.ai Pricing (Approximate)
- GPT-Image-1.5: ~$0.05 - $0.10 per image
- GPT-Image-1.5/edit: ~$0.05 - $0.10 per edit

### Total Cost
- Task 1: 2 edits × $0.10 = $0.20
- Task 2: 8 images × $0.10 = $0.80
- **Total: ~$1.00 - $1.50**

(Check fal.ai for current pricing)

---

## Expected Timeline

### First-Time Setup (5 minutes)
1. Create virtual environment (1 min)
2. Install dependencies (2 min)
3. Get API key from 1Password (1 min)
4. Test API connection (1 min)

### Actual Processing (5-10 minutes)
1. Task 1 - Fix necks (2-3 min)
   - 2 images × 1-1.5 min each
2. Task 2 - Community photos (3-7 min)
   - 8 images × 0.5-1 min each

### Total: ~10-15 minutes (including setup)

---

## Quality Assurance

### Manual Review Required
After generation, check each image for:

#### Task 1 (Neck Fixes)
- [ ] Face is EXACTLY the same (eyes, nose, mouth)
- [ ] Hair style and color unchanged
- [ ] Neck is proportionally shorter
- [ ] Natural transition from neck to shoulders
- [ ] No artifacts or distortions
- [ ] Professional quality maintained

#### Task 2 (Community Photos)
- [ ] All 4 founders visible (or appropriate group)
- [ ] Diverse community members present
- [ ] Appropriate setting for scenario
- [ ] Natural, authentic poses
- [ ] Professional photography quality
- [ ] Proper lighting and composition
- [ ] No text artifacts or watermarks

### Regeneration
If any image doesn't meet quality standards:

```bash
# Edit the script to focus on one image
python scripts/fix_necks_and_create_community_photos.py

# Or manually run specific functions:
# fix_neck("lilly", Path("assets/founders/headshots_no_bg/lilly_headshot_no_bg.png"))
# create_community_photo(3, "Your custom scenario")
```

---

## Use Cases for Generated Images

### Website
- Fixed headshots: Team page, about page
- Community photos: Values section, culture page, social responsibility

### Marketing
- Social media posts (LinkedIn, Twitter, Instagram)
- Email newsletters
- Company announcements
- Press releases

### Investor Materials
- Pitch deck (shows team values)
- Company overview
- ESG (Environmental, Social, Governance) reporting
- Annual reports

### Recruiting
- Careers page
- LinkedIn company page
- Job postings
- Company culture showcase

---

## Post-Processing Recommendations

### 1. Convert to WebP (Better Compression)
```bash
cd /mnt/d/workspace/ISNBIZ_Files

# Convert fixed necks
for img in assets/founders/fixed_necks/*.png; do
    cwebp -q 90 "$img" -o "${img%.png}.webp"
done

# Convert community photos
for img in assets/founders/community/*.png; do
    cwebp -q 85 "$img" -o "${img%.png}.webp"
done
```

### 2. Create Thumbnails (Faster Loading)
```bash
# Using ImageMagick
for img in assets/founders/community/*.png; do
    convert "$img" -resize 400x225 "${img%.png}_thumb.png"
done
```

### 3. Add to Git
```bash
git add assets/founders/fixed_necks/
git add assets/founders/community/
git commit -m "Add enhanced founder photos and community outreach images

- Fixed neck proportions for Lilly and Bri using fal.ai
- Generated 8 community engagement scenarios
- All images professional quality, ready for website"
git push
```

---

## Next Steps

1. **Run the script** (when ready):
   ```bash
   ./scripts/run_photo_enhancement.sh
   ```

2. **Review all generated images**:
   - Check quality
   - Verify accuracy
   - Select favorites

3. **Update website HTML**:
   - Use fixed headshots on team page
   - Add community photos to about/values section

4. **Social media**:
   - Share community photos
   - Show company values
   - Engage with community

5. **Investor deck**:
   - Add to team slide
   - Create values/culture slide
   - Show social responsibility

---

## Maintenance

### Regenerating Images
If you need to regenerate:

1. Delete old images:
   ```bash
   rm -rf assets/founders/fixed_necks/*
   rm -rf assets/founders/community/*
   ```

2. Edit prompts in script if needed

3. Re-run script:
   ```bash
   ./scripts/run_photo_enhancement.sh
   ```

### Updating Scenarios
Edit the `scenarios` list in `scripts/fix_necks_and_create_community_photos.py`:

```python
scenarios = [
    "Your new scenario 1",
    "Your new scenario 2",
    # ... up to 8 scenarios
]
```

### Adding More Founders
Edit the `people_desc` in the script:

```python
people_desc = """Five diverse tech founders:
- Jonathan (40s, professional man with beard)
- Alicia (30s, dark straight hair)
- Bri (30s, dark wavy hair)
- Lilly (30s, brown wavy hair)
- NewPerson (description)"""
```

---

## Support

### Troubleshooting
See **PHOTO_ENHANCEMENT_README.md** for detailed troubleshooting.

### Common Issues
1. API key not set → Check 1Password
2. Virtual environment missing → Create with `python3 -m venv venv_fal`
3. Dependencies missing → Run `pip install fal-client requests`
4. Images look wrong → Adjust guidance_scale or prompts

### Getting Help
- Check script comments
- Review fal.ai documentation: https://fal.ai/models
- Check API status: https://status.fal.ai/

---

**Created:** 2026-02-02
**Purpose:** Enhance ISN.BIZ founder photos for investor-ready website
**Status:** Ready to execute
**Estimated Time:** 10-15 minutes
**Estimated Cost:** $1.00 - $1.50

---

## Summary

Two comprehensive tasks to enhance ISN.BIZ founder photos:

1. **Fix Necks** - Improve Lilly and Bri's headshot proportions
2. **Community Photos** - Generate 8 professional team engagement photos

All scripts, documentation, and automation are ready. Just run:

```bash
./scripts/run_photo_enhancement.sh
```

Then review the 10 generated images and use them across the website, marketing, and investor materials.
