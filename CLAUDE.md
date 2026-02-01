# CLAUDE.md - ISN.BIZ Website

**Project:** ISN.BIZ Inc Investor-Ready Website
**Status:** Production Ready - READY FOR DEPLOYMENT
**Location:** `/mnt/d/workspace/ISNBIZ_Files/`

---

## Quick Overview

Professional investor-ready website for ISN.BIZ Inc (software company). Static HTML/CSS/JS site designed to attract funding and showcase AI/cloud software portfolio.

**Key Stats:**
- **30KB HTML** + **23KB CSS** + **687B JS** (ultra-lightweight)
- **Fully responsive** (mobile-first design)
- **SEO optimized** (semantic HTML, proper meta tags)
- **Fast load** (<3 seconds target)
- **Ready to deploy** (Netlify recommended)

---

## Website Structure

### Sections

1. **Navigation** - Fixed header with blur effect, mobile menu
2. **Hero** - Full-height entry with ISS logo, metallic background, key stats
3. **About** - Company overview, credentials (DUNS, UBI, EIN)
4. **Solutions** - 4 cards: AI Apps, Cloud, Enterprise Software, Data Analytics
5. **Portfolio Preview** - 3 case studies with metrics
6. **Investor Section** - Professional pitch, investment highlights, dual CTAs
7. **Contact** - Form + company info card
8. **Footer** - Credentials, links, copyright

### Brand Colors

```css
--color-blue: #1E9FF2      /* Primary brand - CTAs, accents */
--color-cyan: #5FDFDF      /* Secondary - highlights, gradients */
--color-charcoal: #3F4447  /* Dark text, backgrounds */
```

### Files

```
ISNBIZ_Files/
├── index.html              # Main page (30KB)
├── styles.css              # Stylesheet (23KB)
├── script.js               # Interactivity (687B)
├── logo-pallete/           # Brand assets
│   ├── ISS white long 500(1).png
│   ├── ISS2500.png
│   ├── metal 4 squared.jpg
│   ├── metal 5.jpg
│   └── pallete.png
└── docs/                   # Documentation (40 files)
```

---

## How to Deploy

### Option 1: Netlify (RECOMMENDED - Easiest)

**Why Netlify:**
- Drag-and-drop deployment
- Free SSL certificate (HTTPS)
- Built-in form handling
- CDN included
- Automatic Git deployments
- Custom domain easy

**Steps:**

```bash
# Method A: Netlify CLI
npm install -g netlify-cli
cd /mnt/d/workspace/ISNBIZ_Files
netlify deploy --prod

# Method B: Drag-and-drop
# 1. Go to https://app.netlify.com/
# 2. Drag ISNBIZ_Files folder to deploy
# 3. Configure custom domain (isn.biz)

# Method C: Git-based (auto-deploy)
cd /mnt/d/workspace/ISNBIZ_Files
git init
git add .
git commit -m "Initial investor website"
git remote add origin https://github.com/isn-biz/website.git
git push -u origin main
# Connect repo to Netlify for auto-deploy on push
```

**Documentation:** See `DEPLOY_TO_NETLIFY.md` for detailed guide

### Option 2: GitHub Pages

```bash
# 1. Create GitHub repo: isn-biz/website
# 2. Push code
git init
git add .
git commit -m "ISN.BIZ investor website"
git remote add origin https://github.com/isn-biz/website.git
git push -u origin main

# 3. Enable GitHub Pages in repo settings
# 4. Configure custom domain (isn.biz)
```

### Option 3: Traditional cPanel/FTP

```bash
# 1. Upload all files via FTP/SFTP
# 2. Configure SSL certificate (Let's Encrypt)
# 3. Point domain to server
# 4. Test
```

### Option 4: Kusanagi (Like HROC)

**Pros:** Match HROC infrastructure
**Cons:** More complex, requires server management

See `.serena/WEBSITES.md` for Kusanagi setup details

---

## Deployment Workflow

### Pre-Launch Checklist

**CRITICAL (Must Complete Before Launch):**
- [ ] Update contact email (currently placeholder)
- [ ] Add real company metrics in hero stats
- [ ] Replace portfolio examples with actual projects
- [ ] Set up form backend (Formspree, Netlify Forms, or custom)
- [ ] Configure SSL certificate (HTTPS)
- [ ] Test on multiple devices (mobile, tablet, desktop)
- [ ] Test on multiple browsers (Chrome, Firefox, Safari, Edge)

**IMPORTANT (Week 1):**
- [ ] Add Google Analytics 4 tracking
- [ ] Set up Google Search Console
- [ ] Configure form spam protection (CAPTCHA)
- [ ] Optimize images (WebP format, compression)
- [ ] Update LinkedIn with new URL
- [ ] Update CrunchBase profile
- [ ] Update AngelList/Wellfound

**ENHANCED (Weeks 2-4):**
- [ ] Create privacy policy page
- [ ] Create terms of service page
- [ ] Add team photos and bios
- [ ] Create downloadable pitch deck PDF
- [ ] Add client logos (with permission)
- [ ] Implement schema markup (JSON-LD)
- [ ] Set up email newsletter signup
- [ ] Create blog section

**Full checklist:** See `DEPLOYMENT_CHECKLIST.md`

### GitHub Workflow

```bash
# Setup (one-time)
cd /mnt/d/workspace/ISNBIZ_Files
git init
git add .
git commit -m "Initial investor-ready website"
git remote add origin https://github.com/isn-biz/website.git
git push -u origin main

# Daily workflow
git add .
git commit -m "Update: description of changes"
git push

# Netlify will auto-deploy on push to main
```

---

## How to Update

### Change Content

**Edit `index.html`:**

```bash
# Hero stats (lines ~45-57)
<div class="stat">
    <span class="stat-number">11+</span>
    <span class="stat-label">Years</span>
</div>

# Company info (lines ~89-115)
<h2>About ISN.BIZ Inc</h2>
<p>Your description here...</p>

# Solutions (lines ~130-195)
<div class="solution-card">
    <h3>AI-Powered Applications</h3>
    <p>Description...</p>
</div>

# Portfolio items (lines ~207-235)
<div class="portfolio-item">
    <h3>Project Title</h3>
    <p>Description...</p>
</div>

# Contact info (line ~480)
<p><strong>Email:</strong> contact@isn.biz</p>
```

### Change Colors

**Edit `styles.css` (lines 1-25):**

```css
:root {
    --color-blue: #1E9FF2;      /* Change primary color */
    --color-cyan: #5FDFDF;      /* Change secondary */
    --color-charcoal: #3F4447;  /* Change dark color */
}
```

### Add New Section

1. Copy existing section structure from `index.html`
2. Maintain consistent class naming
3. Update navigation menu
4. Test responsiveness
5. Git commit and push

### Update Logo

1. Replace files in `logo-pallete/`
2. Update references in `index.html`:
   ```html
   <img src="logo-pallete/ISS white long 500(1).png" alt="ISN.BIZ Logo">
   ```
3. Optimize image (compress, WebP)
4. Test on different backgrounds

---

## S3 Asset Management

### Current: Local Assets

All images in `logo-pallete/` directory, served directly with HTML.

### Future: S3 + CloudFront CDN

**Benefits:**
- Fast global delivery
- Reduced server load
- Scalable storage
- Cost-effective

**Setup:**

```bash
# Upload to S3
aws s3 cp logo-pallete/ISS2500.png s3://isn-biz-assets/images/

# Configure CloudFront distribution
# Point to S3 bucket
# Enable HTTPS
# Set caching headers

# Update HTML
<img src="https://cdn.isn.biz/images/ISS2500.png" alt="ISN.BIZ Logo">
```

**See:** `/mnt/d/workspace/.serena/WEBSITES.md` for S3 setup details

---

## Form Backend Setup

### Current State

JavaScript alert (placeholder):
```javascript
alert('Thank you! We will contact you soon.');
```

### Option 1: Formspree (Easiest)

```html
<form action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
  <!-- Existing form fields -->
</form>
```

- Free tier: 50 submissions/month
- Get YOUR_FORM_ID at: https://formspree.io/
- No backend code needed

### Option 2: Netlify Forms (If using Netlify)

```html
<form name="contact" method="POST" data-netlify="true" netlify-honeypot="bot-field">
  <input type="hidden" name="form-name" value="contact" />
  <!-- Existing form fields -->
</form>
```

- Included with Netlify hosting
- Built-in spam protection
- Email notifications

### Option 3: Custom Backend

```javascript
// Python Flask example
@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    # Send email, store in database, etc.
    return jsonify({'success': True})
```

---

## Important Commands

### Local Preview

```bash
cd /mnt/d/workspace/ISNBIZ_Files

# Open in browser
# Windows: start index.html
# Linux: xdg-open index.html
# Or just double-click index.html
```

### Deploy to Netlify

```bash
netlify deploy --prod
```

### Git Workflow

```bash
cd /mnt/d/workspace/ISNBIZ_Files

git status                     # Check changes
git add .                      # Stage changes
git commit -m "Description"    # Commit
git push                       # Push (auto-deploys on Netlify)
```

### Image Optimization

```bash
# Convert to WebP (better compression)
for img in logo-pallete/*.{jpg,png}; do
  cwebp -q 85 "$img" -o "${img%.*}.webp"
done

# Use in HTML with fallback
<picture>
  <source srcset="logo-pallete/ISS2500.webp" type="image/webp">
  <img src="logo-pallete/ISS2500.png" alt="ISN.BIZ Logo">
</picture>
```

### Performance Check

```bash
# Lighthouse audit (Chrome DevTools)
# Or use online tool: web.dev/measure/

# Check load time
curl -w "@curl-format.txt" -o /dev/null -s https://isn.biz
```

---

## Key Decisions Made

### Why Static HTML/CSS/JS?
- **Fast load times** - No framework overhead
- **SEO friendly** - Search engines love clean HTML
- **Easy to deploy** - Works anywhere
- **Low maintenance** - No backend dependencies
- **Cost effective** - Can host for free

### Why Netlify?
- **Easiest deployment** - Drag-and-drop or Git
- **Free SSL** - HTTPS included
- **CDN included** - Global distribution
- **Form handling** - No backend needed
- **Auto-deploy** - Push to Git = deploy

### Why Investor-Focused?
- **Clear CTAs** - Schedule Meeting, Request Pitch Deck
- **Professional design** - Dark investor section
- **Trust signals** - DUNS, UBI, EIN displayed
- **Measurable results** - Portfolio metrics shown
- **Mobile-first** - 70%+ investors on mobile

### Design Choices
- **Metallic backgrounds** - Professional, tech-forward
- **Blue/cyan colors** - Trust, technology, innovation
- **Minimal JavaScript** - Fast, accessible
- **Responsive design** - Works on all devices

---

## Where to Find Things

### Documentation

**Quick Starts:**
- `GET_STARTED.md` - Getting started guide
- `QUICK_START_GUIDE.md` - Launch instructions
- `DEPLOYMENT_CHECKLIST.md` - Pre-launch tasks

**Design Guides:**
- `BRAND_ASSETS_GUIDE.md` - Logo usage, colors
- `VISUAL_PREVIEW_GUIDE.md` - Design preview
- `ASSET_CATALOG.md` - All available assets
- `ASSET_USAGE_GUIDE.md` - How to use assets

**Deployment:**
- `DEPLOY_TO_NETLIFY.md` - Netlify deployment
- `MANUAL_DEPLOYMENT_GUIDE.md` - Manual deployment
- `DEPLOYMENT_CHECKLIST.md` - Pre-launch checklist

**Assets:**
- `COMPLETE_ASSET_GENERATION_PLAN.md` - Asset strategy
- `ASSET_GENERATION_QUICK_START.md` - Quick asset guide
- `AI_ASSET_GENERATION_SUMMARY.md` - AI-generated assets

**Summaries:**
- `COMPLETE_WEBSITE_SUMMARY.md` - Full site overview
- `DELIVERY_COMPLETE.txt` - Completion report

### File Locations

- **HTML:** `index.html` (main page)
- **CSS:** `styles.css` (all styling)
- **JavaScript:** `script.js` (interactivity)
- **Images:** `logo-pallete/` (brand assets)
- **Docs:** `docs/` (40 documentation files)

---

## Company Information

### ISN.BIZ Inc

**Legal:**
- **DUNS:** 080513772
- **UBI:** 603-522-339
- **EIN:** 47-4530188
- **Founded:** July 8, 2015
- **Type:** Software development company

**Focus:**
- AI-Powered Applications (Claude, GPT, Qwen)
- Cloud Solutions (AWS, Azure, scalable)
- Enterprise Software (custom business apps)
- Data Analytics (RAG, vector databases)

**Website:**
- **Current:** isn.biz (placeholder)
- **New:** Production-ready, awaiting deployment

---

## Troubleshooting

### "Form not submitting"
- Check form backend is configured (Formspree/Netlify/custom)
- Test with browser console open for errors
- Verify action URL is correct

### "Images not loading"
- Check file paths are correct (case-sensitive on Linux)
- Verify images exist in `logo-pallete/`
- Check browser console for 404 errors

### "Mobile menu not working"
- Ensure `script.js` is loading
- Check browser console for JavaScript errors
- Test on actual mobile device, not just resize

### "Site looks different on mobile"
- Test on actual devices, not just browser resize
- Check CSS media queries (480px, 768px, 992px, 1200px)
- Use Chrome DevTools device emulation

### "Netlify deploy failed"
- Check build logs in Netlify dashboard
- Verify all files are committed to Git
- Ensure no large files (>100MB) in repo

---

## Related Documentation

**Workspace:**
- `/mnt/d/workspace/CLAUDE.md` - Workspace overview
- `/mnt/d/workspace/.serena/WEBSITES.md` - Website deployment details
- `/mnt/d/workspace/.serena/PROJECT_OVERVIEW.md` - Complete project context

**Infrastructure:**
- `/mnt/d/workspace/.serena/INFRASTRUCTURE.md` - Server options (Kusanagi)

**HROC Website (Reference):**
- `/mnt/d/workspace/HROC_Files/CLAUDE.md` - Similar project
- `/mnt/d/workspace/.serena/WEBSITES.md` - Shared infrastructure

---

## Common Tasks for Claude

### Update Company Stats

Edit `index.html` lines ~45-57:
```html
<div class="stat">
    <span class="stat-number">NEW_VALUE</span>
    <span class="stat-label">Label</span>
</div>
```

### Add Portfolio Item

Copy existing structure in `index.html` lines ~207-235:
```html
<div class="portfolio-item">
    <span class="portfolio-tag">Industry Tag</span>
    <h3>Project Title</h3>
    <p>Description of project and results...</p>
    <div class="portfolio-tech">
        <span>Tech 1</span>
        <span>Tech 2</span>
    </div>
    <div class="portfolio-metric">
        <strong>Metric:</strong> Result
    </div>
</div>
```

### Update Contact Information

Edit `index.html` line ~480:
```html
<p><strong>Email:</strong> new-email@isn.biz</p>
<p><strong>Phone:</strong> (XXX) XXX-XXXX</p>
```

### Add Analytics

Add before `</head>` in `index.html`:
```html
<!-- Google Analytics 4 -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

---

**Last Updated:** 2026-02-01
**Maintained by:** jdmal + Claude AI
**Status:** Production ready, awaiting deployment

**Next Step:** Deploy to Netlify → See `DEPLOY_TO_NETLIFY.md`
