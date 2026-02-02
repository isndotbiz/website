# Founder Photo Enhancement - START HERE

**Created:** 2026-02-02
**Status:** ✅ READY TO RUN
**Purpose:** Fix Lilly & Bri's neck proportions + Create 8 community outreach photos

---

## Quick Start (30 seconds)

```bash
cd /mnt/d/workspace/ISNBIZ_Files
./scripts/run_photo_enhancement.sh
```

That's it! Wait 10-15 minutes, then check the results in:
- `assets/founders/fixed_necks/` (2 images)
- `assets/founders/community/` (8 images)

---

## What You Get

### Task 1: Fixed Headshots (2 images)
- **Lilly** - Neck proportions improved (~15% shorter)
- **Bri** - Neck proportions improved (~15% shorter)
- Faces remain EXACTLY the same
- Professional corporate quality

### Task 2: Community Outreach Photos (8 images)
All 4 founders (Jonathan, Alicia, Bri, Lilly) in:
1. Community center volunteering
2. Teaching coding workshop
3. Speaking at tech event
4. Mentoring students
5. Community cleanup
6. Food bank volunteering
7. STEM outreach at school
8. Charity tech event

---

## Documentation Index

### Quick Reference (Start here if in a hurry)
- **QUICK_RUN_PHOTOS.txt** (4.8 KB)
  - Minimal instructions
  - One-page quick start
  - Common issues

### Visual Guide (For visual learners)
- **PHOTO_WORKFLOW_DIAGRAM.txt** (17 KB)
  - ASCII workflow diagram
  - Step-by-step visual
  - Timeline and costs

### Setup Summary (Current status)
- **SETUP_COMPLETE_SUMMARY.txt** (6.0 KB)
  - What's ready
  - How to run
  - Success metrics

### Executive Overview (For detailed planning)
- **PHOTO_TASKS_SUMMARY.md** (13 KB)
  - Complete task breakdown
  - Technical details
  - Quality assurance
  - Post-processing recommendations

### Complete Guide (Comprehensive documentation)
- **PHOTO_ENHANCEMENT_README.md** (7.1 KB)
  - Full step-by-step instructions
  - Troubleshooting guide
  - Advanced usage
  - Integration examples

---

## Technical Details

### Scripts
- **scripts/fix_necks_and_create_community_photos.py** (281 lines)
  - Main Python script
  - Handles both tasks
  - Progress reporting
  - Error handling

- **scripts/run_photo_enhancement.sh** (95 lines)
  - Bash automation
  - Environment setup
  - 1Password integration
  - Result reporting

### Technology
- **AI Provider:** fal.ai
- **Models:**
  - `fal-ai/gpt-image-1.5/edit` (Task 1 - neck fixes)
  - `fal-ai/gpt-image-1.5` (Task 2 - community photos)
- **Cost:** ~$1.00 - $1.50 total
- **Time:** 10-15 minutes

### Requirements
- Python 3.12+ with virtual environment
- fal-client and requests packages
- FAL API key (from 1Password)
- 1Password CLI (for automatic key retrieval)

---

## Common Workflows

### First Time Run
```bash
# 1. Set up environment (one-time)
python3 -m venv venv_fal
source venv_fal/bin/activate
pip install fal-client requests

# 2. Run the enhancement
./scripts/run_photo_enhancement.sh
```

### Subsequent Runs
```bash
# Just run the script (environment persists)
./scripts/run_photo_enhancement.sh
```

### Manual Run (if script fails)
```bash
source venv_fal/bin/activate
eval $(op signin)
export FAL_KEY=$(op read "op://Research/FAL API Key/credential")
python scripts/fix_necks_and_create_community_photos.py
```

---

## Troubleshooting

### Issue: "FAL_KEY environment variable not set"
**Solution:**
```bash
eval $(op signin)
export FAL_KEY=$(op read "op://Research/FAL API Key/credential")
```

### Issue: "Virtual environment not found"
**Solution:**
```bash
python3 -m venv venv_fal
source venv_fal/bin/activate
pip install fal-client requests
```

### Issue: "No module named 'fal_client'"
**Solution:**
```bash
source venv_fal/bin/activate
pip install fal-client requests
```

### Issue: "Cannot connect to 1Password app"
**Solution:**
- Make sure 1Password desktop app is running
- Sign in: `eval $(op signin)`
- Verify: `op item get "FAL API Key" --vault Research`

---

## Output Locations

### Fixed Necks
```
assets/founders/fixed_necks/
├── lilly_headshot_fixed.png
└── bri_headshot_fixed.png
```

### Community Photos
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

## Next Steps After Generation

1. **Review Images**
   ```bash
   cd assets/founders/fixed_necks && ls -lh
   cd ../community && ls -lh
   ```

2. **Update Website**
   - Edit HTML to reference new images
   - Replace old headshots with fixed versions
   - Add community photos to about/values sections

3. **Convert to WebP** (optional, better compression)
   ```bash
   for img in assets/founders/fixed_necks/*.png; do
       cwebp -q 90 "$img" -o "${img%.png}.webp"
   done

   for img in assets/founders/community/*.png; do
       cwebp -q 85 "$img" -o "${img%.png}.webp"
   done
   ```

4. **Commit to Git**
   ```bash
   git add assets/founders/
   git commit -m "Add enhanced founder photos and community outreach images"
   git push
   ```

---

## Use Cases

### Website
- **Team page:** Fixed headshots
- **About page:** Community photos
- **Values section:** Community engagement
- **Culture page:** Team in action

### Marketing
- **LinkedIn posts:** Community involvement
- **Twitter:** Company values
- **Instagram:** Behind the scenes
- **Email newsletters:** Team updates

### Investor Materials
- **Pitch deck:** Team + values slide
- **Company overview:** Social responsibility
- **ESG reporting:** Community impact
- **Annual reports:** Team culture

### Recruiting
- **Careers page:** Company culture
- **LinkedIn company page:** Team environment
- **Job postings:** Work environment
- **Recruiting emails:** Why join us

---

## File Summary

### Created Today (2026-02-02)
| File | Size | Purpose |
|------|------|---------|
| **START_HERE_PHOTOS.md** | - | This file - master index |
| **PHOTO_ENHANCEMENT_README.md** | 7.1 KB | Complete guide |
| **PHOTO_TASKS_SUMMARY.md** | 13 KB | Executive overview |
| **PHOTO_WORKFLOW_DIAGRAM.txt** | 17 KB | Visual workflow |
| **QUICK_RUN_PHOTOS.txt** | 4.8 KB | Quick reference |
| **SETUP_COMPLETE_SUMMARY.txt** | 6.0 KB | Setup status |
| **scripts/fix_necks_and_create_community_photos.py** | 281 lines | Main script |
| **scripts/run_photo_enhancement.sh** | 95 lines | Runner script |

**Total Documentation:** ~50 KB
**Total Code:** 376 lines

---

## Support

### Internal Documentation
All documentation is self-contained in this directory:
- Start with **QUICK_RUN_PHOTOS.txt** for immediate use
- Read **PHOTO_ENHANCEMENT_README.md** for complete guide
- Check **PHOTO_WORKFLOW_DIAGRAM.txt** for visual understanding

### External Resources
- fal.ai Models: https://fal.ai/models
- fal.ai Status: https://status.fal.ai/
- GPT-Image-1.5: https://fal.ai/models/fal-ai/gpt-image-1.5

### Credentials
- Location: 1Password "Research" vault
- Item: "FAL API Key"
- CLI: `op read "op://Research/FAL API Key/credential"`

---

## Success Checklist

After running, verify:
- [ ] 2 fixed headshots in `assets/founders/fixed_necks/`
- [ ] 8 community photos in `assets/founders/community/`
- [ ] All images are high quality PNG files
- [ ] Faces in fixed headshots look identical to originals
- [ ] Neck proportions are improved
- [ ] Community photos show all 4 founders
- [ ] No artifacts or distortions
- [ ] Total cost under $2
- [ ] Total time under 15 minutes

If all checked, **SUCCESS!** 🎉

---

## Quick Commands Reference

```bash
# Run everything
./scripts/run_photo_enhancement.sh

# Check status
ls -lh assets/founders/fixed_necks/
ls -lh assets/founders/community/

# View documentation
cat QUICK_RUN_PHOTOS.txt
cat PHOTO_ENHANCEMENT_README.md

# Sign into 1Password
eval $(op signin)

# Get API key manually
export FAL_KEY=$(op read "op://Research/FAL API Key/credential")

# Activate virtual environment
source venv_fal/bin/activate

# Install dependencies
pip install fal-client requests

# Convert to WebP
for img in assets/founders/fixed_necks/*.png; do
    cwebp -q 90 "$img" -o "${img%.png}.webp"
done
```

---

## Ready to Run!

Everything is set up and ready to execute.

**To begin:**
```bash
./scripts/run_photo_enhancement.sh
```

**Questions?** Check the documentation:
- Quick start: `QUICK_RUN_PHOTOS.txt`
- Full guide: `PHOTO_ENHANCEMENT_README.md`
- Workflow: `PHOTO_WORKFLOW_DIAGRAM.txt`

**Good luck!** 🚀

---

*Documentation created: 2026-02-02*
*Author: Claude + jdmal*
*Project: ISN.BIZ Investor Website*
