# ISN.BIZ Website - Quick Testing Guide

**Purpose:** Verify all pages load correctly before deployment

---

## ✅ Quick Visual Test (2 Minutes)

### Step 1: Open Homepage
```
1. Double-click: index.html
2. Verify:
   - Logo appears (navbar)
   - Hero section with large ISN.BIZ logo
   - Blue/cyan color scheme
   - All sections visible (About, Solutions, Portfolio, Team, Investors, Contact)
   - Team section shows 4 founders with photos
```

### Step 2: Test Founder Pages (Click Each)
```
From homepage team section, click:
1. Jonathan → Should load jonathan.html with 6+ photos
2. Bri → Should load bri.html with corporate photos
3. Lilly → Should load lilly.html with corporate photos
4. Alicia → Should load alicia.html with corporate photos

Verify each page:
- Same navigation header
- Hero section with founder photo
- Biography sections with alternating text/image
- Same footer as homepage
```

### Step 3: Test Portfolio Pages
```
From homepage, click "View Full Portfolio" → portfolio.html
Verify:
- 8 project cards in grid layout
- Click any project card

Test these project pages:
1. Opportunity Bot
2. TrueNAS Infrastructure
3. BIN Intelligence
4. SpiritAtlas
5. VideoGen YouTube
6. ComfyUI Automation
7. GEDCOM Platform
8. LLM Optimization

Each should:
- Load with project hero
- Show detailed description
- Have technical stack section
- Link back to portfolio
```

### Step 4: Test Core Pages
```
From navigation, visit:
1. About → about.html
2. Services → services.html (if exists)
3. Investors → investors.html
4. Contact → contact.html

Verify:
- All pages use same design
- Navigation works
- Footer appears
```

### Step 5: Mobile Test
```
1. Resize browser to < 768px width
2. Verify:
   - Hamburger menu appears
   - Menu opens/closes on click
   - All content stacks vertically
   - Images scale properly
   - Text remains readable
```

---

## 🖼️ Image Loading Test (1 Minute)

### Check S3 Images Load
```
Open browser console (F12)
1. Go to Network tab
2. Filter by "Images"
3. Reload homepage
4. Verify all images show 200 status (not 404)
5. Look for any broken images (missing icon)

Key images to verify:
- Navbar logo
- Hero logo
- Founder headshots (4)
- Portfolio project images (6)
- Footer logo
```

### Expected S3 URLs
All should start with:
```
https://isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com/
```

Common paths:
- `premium_v3/logos/...`
- `assets/founders/headshots_with_bg/...`
- `premium_v3/portfolio/...`
- `premium_v3/projects/...`

---

## 🔗 Link Test (1 Minute)

### Navigation Links
From any page, click each nav link:
```
✓ Home → index.html
✓ About → about.html
✓ Services → services.html
✓ Portfolio → portfolio.html
✓ Team → index.html#team (scrolls to team section)
✓ Investors → investors.html
✓ Contact → contact.html
```

### Founder Links (From Homepage Team Section)
```
✓ Jonathan → jonathan.html
✓ Bri → bri.html
✓ Lilly → lilly.html
✓ Alicia → alicia.html
```

### Portfolio Links (From Homepage or Portfolio Page)
```
✓ Opportunity Bot → project-opportunity-bot.html
✓ Infrastructure → project-truenas-infrastructure.html
✓ BIN Intelligence → project-bin-intelligence.html
✓ SpiritAtlas → project-spiritatlas.html
✓ VideoGen → project-videogen-youtube.html
✓ ComfyUI → project-comfyui-automation.html
✓ GEDCOM → project-gedcom-platform.html
✓ LLM Optimization → project-llm-optimization.html
```

---

## 📱 Responsive Test (2 Minutes)

### Desktop (1920x1080)
```
✓ Navigation horizontal
✓ Grid layouts: 4 columns (solutions, portfolio)
✓ Hero full-width
✓ Founder grid: 2x2
✓ All images scale properly
```

### Tablet (768x1024)
```
✓ Navigation horizontal (or starts collapsing)
✓ Grid layouts: 2 columns
✓ Founder grid: 2x2 or 1x4
✓ Text remains readable
```

### Mobile (375x667)
```
✓ Hamburger menu appears
✓ Menu opens/closes
✓ Grid layouts: 1 column
✓ Founder grid: 1x4
✓ Buttons stack vertically
✓ No horizontal scrolling
✓ Font size ≥ 16px
```

---

## ⚡ Performance Test (1 Minute)

### Page Load Speed
```
1. Open homepage in incognito mode
2. Open DevTools (F12) → Network tab
3. Disable cache
4. Reload page
5. Check "Load" time at bottom

Expected results:
✓ Load time: < 3 seconds
✓ DOMContentLoaded: < 1.5 seconds
✓ All resources loaded
✓ No 404 errors
✓ Total size: < 5MB (with images)
```

---

## 🎨 Design Consistency Test (1 Minute)

### Colors (Check Multiple Pages)
```
✓ Primary blue: #1E9FF2
✓ Secondary cyan: #5FDFDF
✓ Background charcoal: #0D1117
✓ Accent pink: #FF2D55 (investor section)
```

### Typography
```
✓ Headers: Archivo Black (bold, uppercase)
✓ Labels: JetBrains Mono (technical style)
✓ Body: IBM Plex Sans (readable)
```

### Layout
```
✓ Navigation: Fixed header with blur
✓ Grid overlay on body (technical feel)
✓ Brutal button styles (clipped corners)
✓ Consistent spacing
✓ Same footer on all pages
```

---

## ✅ Quick Checklist

Run through this in **5 minutes** before deployment:

### Homepage
- [ ] Loads without errors
- [ ] Hero section displays
- [ ] Navigation works
- [ ] Team section shows 4 founders
- [ ] Portfolio shows 6 projects
- [ ] All images load
- [ ] Footer displays

### Founder Pages (Pick 2)
- [ ] jonathan.html loads with photos
- [ ] bri.html loads with photos
- [ ] Navigation works
- [ ] Images load from S3

### Project Pages (Pick 2)
- [ ] project-opportunity-bot.html loads
- [ ] project-truenas-infrastructure.html loads
- [ ] Hero sections display
- [ ] Tech stacks visible
- [ ] Images load

### Mobile
- [ ] Hamburger menu works
- [ ] All content accessible
- [ ] No horizontal scroll
- [ ] Text readable

### Links
- [ ] Nav links work
- [ ] Founder links work
- [ ] Portfolio links work
- [ ] Footer links work

---

## 🐛 Common Issues & Fixes

### Issue: Images Don't Load
**Symptoms:** Broken image icons, missing logos
**Fix:** Check S3 URLs use forward slashes `/` not backslashes `\`
```
CORRECT: https://isnbiz-assets...com/premium_v3/logos/logo.webp
WRONG:   https://isnbiz-assets...com\premium_v3\logos\logo.webp
```

### Issue: Navigation Doesn't Work
**Symptoms:** Clicking nav items does nothing
**Fix:** Verify JavaScript is enabled, check browser console for errors

### Issue: Mobile Menu Stuck Open
**Symptoms:** Hamburger menu won't close
**Fix:** Check JavaScript loaded, verify nav-toggle script present

### Issue: Styles Not Applied
**Symptoms:** Plain HTML, no colors
**Fix:** Verify `<link rel="stylesheet" href="styles.css">` in `<head>`

### Issue: Pages Not Found (404)
**Symptoms:** Clicking links shows "Page Not Found"
**Fix:** Ensure all HTML files are in same directory as index.html

---

## 🚀 Ready for Deployment?

If all tests pass:
1. ✅ All pages load
2. ✅ All images display
3. ✅ All links work
4. ✅ Mobile responsive
5. ✅ No console errors

**YOU'RE READY TO DEPLOY!**

See `DEPLOY_TO_NETLIFY.md` for deployment instructions.

---

**Testing Time:** 5-10 minutes total
**Last Updated:** 2026-02-02
