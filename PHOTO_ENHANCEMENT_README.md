# Founder Photo Enhancement with fal.ai

## Overview

This script performs two tasks using fal.ai's GPT-Image-1.5 model:

### Task 1: Fix Neck Proportions
- Edits Lilly and Bri's photos to make necks slightly shorter
- Keeps faces EXACTLY the same
- Uses `gpt-image-1.5/edit` for precision editing
- Output: `assets/founders/fixed_necks/`

### Task 2: Create Community Outreach Photos
- Generates 8 team photos showing all 4 founders
- Scenarios include:
  1. Volunteering at community center
  2. Teaching coding workshop
  3. Speaking at tech event
  4. Mentoring students
  5. Community cleanup
  6. Food bank volunteering
  7. STEM outreach at school
  8. Charity tech event
- Output: `assets/founders/community/`

## Requirements

1. **1Password CLI** - To get FAL API key
2. **Python 3.12+** - For running the script
3. **Virtual environment** - `venv_fal` with fal-client installed
4. **FAL API key** - Stored in 1Password "Research" vault

## Quick Start

```bash
# Option 1: Run with automated setup (RECOMMENDED)
./scripts/run_photo_enhancement.sh

# Option 2: Manual setup
source venv_fal/bin/activate
eval $(op signin)
export FAL_KEY=$(op read "op://Research/FAL API Key/credential")
python scripts/fix_necks_and_create_community_photos.py
```

## Step-by-Step Instructions

### 1. Set up virtual environment (first time only)

```bash
cd /mnt/d/workspace/ISNBIZ_Files

# Create virtual environment
python3 -m venv venv_fal

# Activate it
source venv_fal/bin/activate

# Install dependencies
pip install fal-client requests
```

### 2. Get FAL API key from 1Password

```bash
# Sign into 1Password (if not already)
eval $(op signin)

# Get the API key
export FAL_KEY=$(op read "op://Research/FAL API Key/credential")

# Verify it's set
echo "API Key length: ${#FAL_KEY} characters"
```

### 3. Run the enhancement script

```bash
# Make sure you're in the virtual environment
source venv_fal/bin/activate

# Run the script
python scripts/fix_necks_and_create_community_photos.py
```

## What the Script Does

### Phase 1: Neck Fixes (2 images)
1. Loads Lilly's headshot from `assets/founders/headshots_no_bg/lilly_headshot_no_bg.png`
2. Uses `gpt-image-1.5/edit` to reduce neck length by ~15%
3. Saves to `assets/founders/fixed_necks/lilly_headshot_fixed.png`
4. Repeats for Bri

**Prompt used:**
> Subtle neck adjustment: Make the neck slightly shorter (reduce by ~15%) while keeping the face,
> hair, expression, and all other features EXACTLY identical. The neck should appear more proportionate
> to the head. Professional corporate headshot. Photorealistic.

### Phase 2: Community Photos (8 images)
1. Generates each scenario using `gpt-image-1.5`
2. Includes detailed descriptions of all 4 founders
3. Saves to `assets/founders/community/community_01_*.png` through `community_08_*.png`

**Sample prompt:**
> Four diverse tech founders volunteering at busy community center, helping diverse people with computers.
> Jonathan (40s, professional man with beard), Alicia (30s, dark straight hair),
> Bri (30s, dark wavy hair), Lilly (30s, brown wavy hair).
> Professional photography, bright natural lighting, photorealistic, Canon EOS R5 quality.

## Output Files

### Fixed Necks (2 files)
```
assets/founders/fixed_necks/
├── lilly_headshot_fixed.png
└── bri_headshot_fixed.png
```

### Community Photos (8 files)
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

## Costs

- **Model:** `fal-ai/gpt-image-1.5` and `gpt-image-1.5/edit`
- **Images:** 10 total (2 edits + 8 generations)
- **Estimated cost:** ~$0.50 - $1.50 (check fal.ai pricing)

## Troubleshooting

### "FAL_KEY environment variable not set"
```bash
eval $(op signin)
export FAL_KEY=$(op read "op://Research/FAL API Key/credential")
```

### "Virtual environment not found"
```bash
python3 -m venv venv_fal
source venv_fal/bin/activate
pip install fal-client requests
```

### "No module named 'fal_client'"
```bash
source venv_fal/bin/activate
pip install fal-client requests
```

### "Cannot connect to 1Password app"
- Make sure 1Password is running
- Sign in: `eval $(op signin)`
- Check the item exists: `op item get "FAL API Key" --vault Research`

### Images look wrong
- Check the prompts in the script
- Adjust `guidance_scale` (lower = more creative, higher = more literal)
- Adjust `num_inference_steps` (more = higher quality, slower)

## Using the Results

### For Website
```html
<!-- Use fixed headshots -->
<img src="assets/founders/fixed_necks/lilly_headshot_fixed.png" alt="Lilly - CTO">
<img src="assets/founders/fixed_necks/bri_headshot_fixed.png" alt="Bri - COO">

<!-- Use community photos in team/about sections -->
<img src="assets/founders/community/community_01_tech_founders_volunteering.png"
     alt="ISN.BIZ team volunteering">
```

### For Social Media
- Use community photos to show company values
- Great for LinkedIn, Twitter, Instagram
- Shows authentic community engagement

### For Investor Deck
- Community photos demonstrate social responsibility
- Shows team culture and values
- Professional yet approachable

## Advanced Usage

### Edit the Script

The script is well-commented and easy to modify:

```python
# Change neck reduction amount (line ~75)
"reduce by ~15%"  # Change to ~10% or ~20%

# Change community scenarios (line ~245)
scenarios = [
    "Your custom scenario here",
    # ...
]

# Adjust image quality (line ~110)
"guidance_scale": 7.5,  # Lower = more creative
"num_inference_steps": 50  # Higher = better quality
```

### Generate Individual Photos

```python
from scripts.fix_necks_and_create_community_photos import fix_neck, create_community_photo

# Fix one person's neck
fix_neck("lilly", Path("assets/founders/lilly_base.webp"))

# Create one community photo
create_community_photo(1, "Your scenario description")
```

## Files Created

- `scripts/fix_necks_and_create_community_photos.py` - Main enhancement script
- `scripts/run_photo_enhancement.sh` - Automated runner with 1Password integration
- `PHOTO_ENHANCEMENT_README.md` - This file

## Next Steps

After running the enhancement:

1. Review all generated images in:
   - `assets/founders/fixed_necks/`
   - `assets/founders/community/`

2. Compare with originals to ensure quality

3. Update website HTML to use new images

4. Consider converting to WebP for better compression:
   ```bash
   for img in assets/founders/fixed_necks/*.png; do
       cwebp -q 90 "$img" -o "${img%.png}.webp"
   done
   ```

5. Update CLAUDE.md if needed

---

**Created:** 2026-02-02
**Author:** Claude + jdmal
**Purpose:** Generate professional founder photos for ISN.BIZ website
