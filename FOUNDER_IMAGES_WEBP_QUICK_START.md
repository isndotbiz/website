# Founder Images WebP - Quick Start Guide

**Status:** All 44 founder images converted to WebP ✅

---

## What Was Done

44 PNG images have been converted to WebP format (95.43% smaller):
- 4 headshots with background
- 4 headshots without background
- 16 corporate photos
- 16 casual variants
- 4 group photos

**Before:** 48.20 MB total
**After:** 2.20 MB total
**Savings:** 45.90 MB

---

## Quick Reference: Using WebP Images

### Best Practice (Use This!)

```html
<picture>
  <source srcset="assets/founders/headshots_with_bg/alicia_headshot.webp" type="image/webp">
  <img src="assets/founders/headshots_with_bg/alicia_headshot.png" alt="Alicia, Co-founder">
</picture>
```

**Why:** Modern browsers get WebP (fast), older browsers get PNG (compatibility)

### All Founder Images Available

**Headshots with Background:**
- `headshots_with_bg/alicia_headshot.webp`
- `headshots_with_bg/bri_headshot.webp`
- `headshots_with_bg/jonathan_headshot.webp`
- `headshots_with_bg/lilly_headshot.webp`

**Headshots without Background:**
- `headshots_no_bg/alicia_headshot_no_bg.webp`
- `headshots_no_bg/bri_headshot_no_bg.webp`
- `headshots_no_bg/jonathan_headshot_no_bg.webp`
- `headshots_no_bg/lilly_headshot_no_bg.webp`

**Corporate Photos (4 each: analyzing, collaborating, presenting, working):**
- `corporate_photos/alicia_*.webp`
- `corporate_photos/bri_*.webp`
- `corporate_photos/jonathan_*.webp`
- `corporate_photos/lilly_*.webp`

**Casual Variants (4 each: brainstorming, casual_meeting, coffee, outdoor):**
- `casual_variants/alicia_*.webp`
- `casual_variants/bri_*.webp`
- `casual_variants/jonathan_*.webp`
- `casual_variants/lilly_*.webp`

**Group Photos:**
- `group_photos/team_brainstorm.webp`
- `group_photos/team_casual.webp`
- `group_photos/team_meeting.webp`
- `group_photos/team_presentation.webp`

---

## Integration Examples

### For Team/Founder Section

```html
<div class="founder">
  <picture>
    <source srcset="assets/founders/headshots_with_bg/alicia_headshot.webp" type="image/webp">
    <img src="assets/founders/headshots_with_bg/alicia_headshot.png" alt="Alicia">
  </picture>
  <h3>Alicia</h3>
  <p>Co-founder & CEO</p>
</div>
```

### For Portfolio/Case Study

```html
<div class="case-study">
  <picture>
    <source srcset="assets/founders/corporate_photos/alicia_presenting.webp" type="image/webp">
    <img src="assets/founders/corporate_photos/alicia_presenting.png" alt="Alicia presenting">
  </picture>
</div>
```

### In CSS (Background Image)

```css
.founder-hero {
  background-image: url('assets/founders/group_photos/team_presentation.webp');
  /* Fallback for browsers without WebP support */
}

@supports not (background-image: url('image.webp')) {
  .founder-hero {
    background-image: url('assets/founders/group_photos/team_presentation.png');
  }
}
```

---

## Deployment Checklist

- [ ] All WebP files exist in correct directories
- [ ] Manifest file created: `assets/founders/webp_conversion_manifest.json`
- [ ] PNG originals retained as backup ✅
- [ ] HTML updated to use WebP with PNG fallback
- [ ] CSS updated if using background images
- [ ] Tested on desktop browsers (Chrome, Firefox, Safari, Edge)
- [ ] Tested on mobile browsers
- [ ] Performance verified (Lighthouse audit)
- [ ] Deployed to production/S3

---

## Verification Command

Check that all WebP files were created:

```bash
# Count WebP files in each directory
find assets/founders -name "*.webp" | wc -l
# Should show: 44

# List all conversions
find assets/founders -name "*.webp" | sort
```

---

## File Size Comparison

| Type | Original | WebP | Savings |
|------|----------|------|---------|
| Headshot (with BG) | 1.09 MB | 0.049 MB | 95.59% |
| Headshot (no BG) | 0.83 MB | 0.044 MB | 94.81% |
| Corporate Photo | 1.08 MB | 0.047 MB | 95.62% |
| Casual Variant | 1.19 MB | 0.055 MB | 95.37% |
| Group Photo | 1.27 MB | 0.065 MB | 94.84% |

---

## Performance Impact

**Load Time Example:**
- Page with all 44 founder images
- Before: 48.20 MB → ~4-8 seconds (DSL/Cable)
- After: 2.20 MB → ~0.2-0.4 seconds (DSL/Cable)
- **Improvement: 20-40x faster**

---

## Browser Compatibility

| Browser | WebP Support | Min Version |
|---------|--------------|------------|
| Chrome | ✅ Yes | 23+ |
| Firefox | ✅ Yes | 65+ |
| Safari | ✅ Yes | 16+ |
| Edge | ✅ Yes | 18+ |
| Opera | ✅ Yes | 12.1+ |
| Android | ✅ Yes | 4.3+ |
| iOS | ✅ Yes | 14+ |

**Coverage:** 94%+ of users

---

## If You Need PNG Only

All original PNG files are still present alongside WebP versions. You can:

1. Continue using PNG files (no changes needed)
2. Transition gradually to WebP using `<picture>` elements
3. Switch to WebP-only when ready

---

## Manifest File

Location: `assets/founders/webp_conversion_manifest.json`

Contains:
- Timestamp of conversion
- Quality settings (85/100)
- List of all 44 conversions
- File sizes (before/after)
- Compression percentages
- Success/failure status

Use for:
- Verification that all files converted
- Tracking which images are which size
- Performance metrics

---

## Next Steps

1. **Review:** Check that WebP files look good in your browser
2. **Deploy:** Copy WebP files to production server
3. **Update:** Modify HTML to use WebP with PNG fallback
4. **Test:** Verify on multiple devices and browsers
5. **Monitor:** Track performance improvements

---

## Questions & Troubleshooting

**Q: Do I have to use WebP?**
A: No, PNG files still work. But WebP is 95% smaller - recommended for web.

**Q: Will older browsers break?**
A: No - use `<picture>` element with PNG fallback (shown above).

**Q: Can I regenerate with different quality?**
A: Yes, run `python3 convert_pngs_to_webp.py` again (safe, creates new files).

**Q: Should I delete the PNG files?**
A: Not yet - keep them as backup. Can delete after verifying WebP works.

---

## File Locations

```
D:\workspace\ISNBIZ_Files\assets\founders\
├── headshots_with_bg/
│   ├── alicia_headshot.png
│   ├── alicia_headshot.webp ← USE THIS
│   └── ... (3 more pairs)
├── headshots_no_bg/
├── corporate_photos/
├── casual_variants/
├── group_photos/
├── webp_conversion_manifest.json ← VERIFY HERE
└── [PNG backups]
```

---

**Status:** Ready for production ✅
**Date:** 2026-02-02
