# ISN.BIZ Founder Photos - Generation Guide

**Purpose:** Professional candid founder photos for ISN.BIZ website
**Location:** `D:\workspace\ISNBIZ_Files\assets\founders\`
**API:** FAL.ai (FLUX Pro & GPT-Image 1.5 Edit)
**Format:** WebP (optimized for web)

---

## Founders

### 1. Bri - Secretary/COO
**Description:** Professional woman, brunette hair, mid-30s, confident executive presence

**Photos:**
- `bri_office_work.webp` - Working at desk reviewing documents
- `bri_presentation.webp` - Giving presentation to team
- `bri_team_meeting.webp` - Collaborating in team meeting
- `bri_strategic_planning.webp` - Reviewing strategic plans

### 2. Lilly - Treasurer/CFO
**Description:** Professional woman, blonde hair, early-40s, financial executive demeanor

**Photos:**
- `lilly_office_work.webp` - Analyzing financial reports
- `lilly_presentation.webp` - Presenting financial data to board
- `lilly_team_meeting.webp` - Financial planning meeting
- `lilly_strategic_planning.webp` - Reviewing quarterly reports

### 3. Jonathan - Chairman/CEO
**Description:** Professional man, short dark hair, mid-40s, executive leadership presence

**Photos:**
- `jonathan_office_work.webp` - Working at executive desk with monitors
- `jonathan_presentation.webp` - Presenting company vision to investors
- `jonathan_team_meeting.webp` - Leading executive team meeting
- `jonathan_strategic_planning.webp` - Reviewing strategic roadmap

### 4. Alicia - VP/CPO
**Description:** Professional woman, dark hair, late-30s, product leadership presence

**Photos:**
- `alicia_office_work.webp` - Reviewing product designs
- `alicia_presentation.webp` - Presenting product roadmap
- `alicia_team_meeting.webp` - Product planning meeting
- `alicia_strategic_planning.webp` - Analyzing user feedback and metrics

---

## Photo Specifications

**Key Requirements:**
- ✅ **NOT looking at camera** - All photos are candid-style, NOT portraits
- ✅ **Professional settings** - Office work, presentations, meetings, planning
- ✅ **Business attire** - Professional or business casual
- ✅ **Natural lighting** - Realistic office environments
- ✅ **High quality** - 1024×1536 resolution (portrait), 4K quality
- ✅ **Authentic moments** - Real work scenarios, not posed

**Format:**
- **Resolution:** 1024×1536 (portrait orientation)
- **File format:** WebP (optimized for web performance)
- **Quality:** 90% WebP compression
- **Size:** ~60-90 KB per image

---

## Generation Scripts

### Method 1: Edit API (Slower, More Consistent)

**Script:** `scripts/generate_founder_photos_candid.py`

**How it works:**
1. Generates base photo for each founder using FLUX Pro
2. Uses GPT-Image 1.5 Edit API to create scenario variations
3. Maintains consistent appearance across all photos
4. Converts to WebP automatically

**Usage:**
```bash
cd D:\workspace\ISNBIZ_Files
python scripts/generate_founder_photos_candid.py
```

**Time:** ~2 minutes per photo (~40 minutes total for 20 photos)

### Method 2: Text-to-Image (Faster, Standalone)

**Script:** `scripts/generate_founders_text_to_image.py`

**How it works:**
1. Generates each photo directly with FLUX Pro
2. No base photo needed - each is standalone
3. Faster generation (~30-60 seconds per photo)
4. May have slight appearance variations

**Usage:**
```bash
cd D:\workspace\ISNBIZ_Files
python scripts/generate_founders_text_to_image.py
```

**Time:** ~1 minute per photo (~16 minutes total for 16 photos)

### Continue From Where You Left Off

**Script:** `scripts/continue_founder_photos.py`

**How it works:**
- Checks what photos already exist
- Only generates missing ones
- Uses existing base photos

**Usage:**
```bash
cd D:\workspace\ISNBIZ_Files
python scripts/continue_founder_photos.py
```

---

## FAL API Configuration

**API Key Location:**
- **1Password:** "FAL API Key" in "True" vault
- **Retrieval:** `op item get "FAL API Key" --vault "True" --reveal --fields label=credential`
- **Environment variable:** `FAL_KEY`

**API Endpoints Used:**
- `fal-ai/flux-pro/v1.1` - Text-to-image generation
- `fal-ai/gpt-image-1.5/edit` - Image editing/variations

**Rate Limiting:**
- 3-second pause between API calls
- Prevents rate limit errors
- Allows queue processing time

---

## Usage on Website

### HTML Implementation

```html
<!-- Founder profile -->
<div class="founder-card">
  <img src="assets/founders/bri_office_work.webp"
       alt="Bri - Secretary/COO working in office"
       loading="lazy"
       width="1024"
       height="1536">
  <h3>Bri</h3>
  <p class="role">Secretary / COO</p>
</div>
```

### Multiple Photos (Carousel/Gallery)

```html
<!-- Photo carousel for single founder -->
<div class="founder-gallery" data-founder="bri">
  <img src="assets/founders/bri_office_work.webp" alt="Bri at work">
  <img src="assets/founders/bri_presentation.webp" alt="Bri presenting">
  <img src="assets/founders/bri_team_meeting.webp" alt="Bri in meeting">
  <img src="assets/founders/bri_strategic_planning.webp" alt="Bri planning">
</div>
```

### CSS Optimization

```css
.founder-card img {
  width: 100%;
  height: auto;
  object-fit: cover;
  border-radius: 8px;
}

/* Lazy loading placeholder */
.founder-card img[loading="lazy"] {
  background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
  background-size: 200% 100%;
  animation: loading 1.5s infinite;
}

@keyframes loading {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}
```

---

## Regenerating Photos

### Regenerate Single Founder

Edit the script to only include one founder:

```python
# In generate_founders_text_to_image.py
# Comment out founders you don't want to regenerate

FOUNDER_SCENARIOS = {
    "bri": [...],  # Keep this
    # "lilly": [...],  # Comment out
    # "jonathan": [...],  # Comment out
    # "alicia": [...],  # Comment out
}
```

### Regenerate Single Scenario

Delete the specific WebP file and run the script again:

```bash
rm D:\workspace\ISNBIZ_Files\assets\founders\bri_office_work.webp
python scripts/generate_founders_text_to_image.py
```

### Change Appearance

Edit the prompts in the script to modify appearance:

```python
"prompt": "Professional woman in mid-30s, brunette hair, glasses, ..."
```

---

## Troubleshooting

### "API Rate Limit" Error
- **Solution:** Increase sleep time between calls (currently 2-3 seconds)
- Edit: `time.sleep(5)` for more conservative rate limiting

### "Unicode Encoding" Error
- **Solution:** Already fixed - uses ASCII characters `[OK]` and `[X]` instead of Unicode checkmarks
- If issue persists, set `PYTHONIOENCODING=utf-8` environment variable

### Photos Look Different
- **Edit API** maintains consistency better (use Method 1)
- **Text-to-image** is faster but may have variations (Method 2)
- For consistency, use same base photo with Edit API

### WebP Conversion Failed
- **Solution:** Ensure Pillow is installed: `pip install Pillow`
- Check PNG exists before conversion
- Verify sufficient disk space

### "No Base Photo" Error
- **Solution:** Run full generation script first to create base photos
- Or run text-to-image version which doesn't need base photos

---

## File Structure

```
ISNBIZ_Files/
├── assets/
│   └── founders/
│       ├── bri_base.webp
│       ├── bri_office_work.webp
│       ├── bri_presentation.webp
│       ├── bri_team_meeting.webp
│       ├── bri_strategic_planning.webp
│       ├── lilly_base.webp
│       ├── lilly_office_work.webp
│       ├── lilly_presentation.webp
│       ├── lilly_team_meeting.webp
│       ├── lilly_strategic_planning.webp
│       ├── jonathan_base.webp
│       ├── jonathan_office_work.webp
│       ├── jonathan_presentation.webp
│       ├── jonathan_team_meeting.webp
│       ├── jonathan_strategic_planning.webp
│       ├── alicia_base.webp
│       ├── alicia_office_work.webp
│       ├── alicia_presentation.webp
│       ├── alicia_team_meeting.webp
│       └── alicia_strategic_planning.webp
├── scripts/
│   ├── generate_founder_photos_candid.py
│   ├── generate_founders_text_to_image.py
│   └── continue_founder_photos.py
└── FOUNDER_PHOTOS_README.md  # This file
```

**Total files:** 20 photos (4 base + 16 scenarios)

---

## Cost Estimation

**FAL.ai Pricing (approximate):**
- FLUX Pro: ~$0.04 per image
- GPT-Image 1.5 Edit: ~$0.02 per image

**Method 1 (Edit API):**
- 4 base photos × $0.04 = $0.16
- 16 edits × $0.02 = $0.32
- **Total: ~$0.48**

**Method 2 (Text-to-Image):**
- 16 photos × $0.04 = $0.64
- **Total: ~$0.64**

---

## Best Practices

1. **Always backup** generated photos before regenerating
2. **Use lazy loading** on website to improve performance
3. **Optimize images** - WebP at 90% quality is sweet spot
4. **Test on mobile** - Ensure photos look good on small screens
5. **Alt text** - Always include descriptive alt text for accessibility
6. **Aspect ratio** - Portrait (1024×1536) works best for founder cards
7. **Consistency** - Use same method for all founders to maintain visual consistency

---

## Next Steps

### For Website Integration:

1. **Choose photos** - Select best scenario for each founder
2. **Add to website** - Update HTML with photo paths
3. **Test loading** - Verify lazy loading works
4. **Mobile test** - Check appearance on mobile devices
5. **Optimize** - Adjust quality if file sizes too large

### For Future Updates:

1. **Additional scenarios** - Add more professional situations
2. **Seasonal updates** - Generate holiday/themed versions
3. **Team photos** - Generate group shots of founders together
4. **Action shots** - More dynamic scenarios (speaking events, etc.)

---

**Last Updated:** 2026-02-02
**Maintained by:** jdmal + Claude AI
**Status:** ✅ 4 founders × 4 scenarios each = 16 professional photos

**API Key:** 1Password "True" vault → "FAL API Key"
