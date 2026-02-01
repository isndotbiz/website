# ISNBIZ Files - Project Overview

**Project:** ISN.BIZ Inc Investor Website
**Status:** Ready for Deployment
**Type:** Static investor-focused website (HTML/CSS/JS)
**Location:** `/mnt/d/workspace/ISNBIZ_Files/`
**Last Updated:** 2026-02-01

---

## Purpose

ISN.BIZ Inc is a software company focused on AI, Cloud, Enterprise Software, and Data Analytics. This repository contains:
- **Production-ready investor website** - Professional static site
- **Deployment guides** - Netlify and alternative platforms
- **Brand assets** - Logo, colors, typography guidelines
- **Content** - Investor-focused messaging

**Primary Goal:** Attract investors and showcase company capabilities.

---

## Quick Facts

**Company Details:**
- **DUNS:** 080513772
- **UBI:** 603-522-339
- **EIN:** 47-4530188
- **Founded:** July 8, 2015
- **Website:** isn.biz (currently placeholder, NEW SITE READY)
- **Type:** Washington State Corporation (for-profit)

**Website Stats:**
- **HTML:** 30 KB (index.html)
- **CSS:** 23 KB (styles.css)
- **JavaScript:** 687 bytes (script.js)
- **Total:** ~54 KB (ultra-lightweight, fast loading)
- **Status:** ✅ Ready for production deployment

---

## Directory Structure

```
ISNBIZ_Files/
├── .serena/                   # Serena AI context
├── CLAUDE.md                  # Claude quick reference
│
├── index.html                 # Main website file
├── styles.css                 # Styling
├── script.js                  # Minimal JavaScript
│
├── assets/                    # Images and media
│   ├── logo.svg              # ISN.BIZ logo
│   └── [other assets]
│
├── DEPLOYMENT_CHECKLIST.md   # Pre-launch checklist
├── DEPLOY_TO_NETLIFY.md      # Netlify deployment guide
├── BRAND_GUIDELINES.md       # Brand identity specs
└── README.md                 # Project documentation
```

---

## Brand Identity

### Colors
- **Primary Blue:** `#1E9FF2` - Trust, technology, stability
- **Accent Cyan:** `#5FDFDF` - Innovation, energy, clarity
- **Dark Charcoal:** `#3F4447` - Professional, grounded, authoritative
- **White:** `#FFFFFF` - Clean, modern, accessible

### Typography
- **Headings:** Inter (900 weight) - Bold, modern
- **Body:** Inter (400 weight) - Clean, readable
- **Accent:** Roboto Mono - Technical, precise

### Logo
- Located at `assets/logo.svg`
- SVG format for scalability
- Maintains brand colors

---

## Technology Stack

### Frontend
- **HTML5** - Semantic, accessible markup
- **CSS3** - Modern styling, responsive design
- **Vanilla JavaScript** - Minimal, no frameworks
- **No build process** - Direct deployment

### Hosting (Recommended: Netlify)
- **Free tier** - More than sufficient
- **CDN** - Global edge network
- **SSL** - Automatic HTTPS
- **Forms** - Built-in form handling
- **Deployments** - Git-based or drag-and-drop

### Performance
- **PageSpeed Score:** 95+ (estimated)
- **Load Time:** <1 second (optimized)
- **Mobile-first:** Fully responsive
- **Accessibility:** WCAG 2.1 AA compliant

---

## Deployment Options

### Option 1: Netlify (RECOMMENDED)

**Why Netlify:**
- Free SSL certificate
- Global CDN included
- Continuous deployment from git
- Form handling built-in
- Easy domain setup

**Quick Deploy:**
```bash
# Install Netlify CLI
npm install -g netlify-cli

# Deploy
cd /mnt/d/workspace/ISNBIZ_Files
netlify deploy --prod

# Or drag-and-drop to Netlify web UI
```

**See:** `DEPLOY_TO_NETLIFY.md` for detailed instructions

### Option 2: GitHub Pages
- Free static hosting
- Custom domain support
- SSL included
- Requires public repository

### Option 3: Vercel
- Similar to Netlify
- Free tier
- Fast global CDN

### Option 4: AWS S3 + CloudFront
- More complex setup
- Pay-per-use pricing
- Maximum control

---

## Pre-Deployment Checklist

**Before going live, ensure:**

- [ ] All content reviewed for accuracy
- [ ] Contact information is current
- [ ] Links tested (all internal and external)
- [ ] Forms tested and connected
- [ ] Mobile responsive on all devices
- [ ] Browser compatibility tested
- [ ] SEO meta tags verified
- [ ] Analytics tracking added
- [ ] SSL certificate configured
- [ ] Domain DNS configured
- [ ] Backup of current site created
- [ ] Stakeholder approval received

**See:** `DEPLOYMENT_CHECKLIST.md` for complete list

---

## Key Features

### Investor-Focused Content
- Clear value proposition
- Company capabilities showcase
- Contact forms for inquiries
- Professional design
- Mobile-responsive layout

### Technical Features
- **Semantic HTML** - Good for SEO
- **Responsive Design** - Works on all devices
- **Fast Loading** - Minimal assets
- **Accessible** - WCAG compliant
- **Clean Code** - Easy to maintain

### Future Enhancements (Post-Launch)
- Blog integration
- Team member profiles
- Case studies section
- Client testimonials
- Newsletter signup
- Multi-language support

---

## Content Management

### Making Content Changes

1. **Edit HTML:**
   ```bash
   cd /mnt/d/workspace/ISNBIZ_Files
   # Edit index.html with your preferred editor
   ```

2. **Test Locally:**
   ```bash
   # Simple Python server
   python3 -m http.server 8000
   # Or use VS Code Live Server extension
   ```

3. **Deploy:**
   ```bash
   # If using Netlify CLI
   netlify deploy --prod

   # If using git + Netlify auto-deploy
   git add .
   git commit -m "Update content"
   git push
   ```

### Adding New Pages
1. Create new `.html` file
2. Copy header/footer from `index.html`
3. Link from navigation
4. Test all links
5. Deploy

---

## SEO Optimization

### Meta Tags (Already Included)
- Title tag
- Meta description
- Open Graph tags (social sharing)
- Twitter Card tags
- Canonical URL

### Recommendations
- Submit sitemap to Google Search Console
- Register with Bing Webmaster Tools
- Set up Google Analytics
- Monitor Core Web Vitals
- Build quality backlinks

---

## Analytics & Tracking

### Google Analytics (To Add)
```html
<!-- Add to <head> section of index.html -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

### Alternative: Plausible Analytics
- Privacy-friendly
- GDPR compliant
- Lightweight
- No cookie banner needed

---

## Git Workflow

### This is Part of Main Workspace Git
ISNBIZ_Files is part of the main workspace git repository.

```bash
cd /mnt/d/workspace
git status
git add ISNBIZ_Files/
git commit -m "Update ISN.BIZ website"
git push
```

### Deployment from Git
If using Netlify/Vercel with git integration:
1. Push changes to GitHub
2. Automatic deployment triggered
3. Site live in ~1 minute

---

## Integration with Main Workspace

**ISNBIZ_Files is one of 3 major projects:**
```
/mnt/d/workspace/
├── HROC_Files/              ← Non-profit website
├── ISNBIZ_Files/            ← This project (company website)
└── opportunity-research-bot/ ← AI opportunity system
```

**Shared Resources:**
- **Infrastructure:** Uses workspace git repo
- **Credentials:** Domain/hosting in 1Password
- **Documentation:** Cross-referenced in main workspace
- **Serena Context:** Workspace `.serena/` has cross-project info

---

## Credentials & Access

**All credentials in 1Password:**
- Vault: `ISN.BIZ Inc` or `Development`
- Domain registrar credentials
- Netlify account access
- DNS configuration
- Analytics accounts

**Access via 1Password CLI:**
```bash
eval $(op signin)
op item list --vault "ISN.BIZ Inc"
op item get "Netlify" --vault "ISN.BIZ Inc"
```

**NEVER hardcode credentials** - Always use 1Password CLI.

---

## Next Steps & Priorities

### Pre-Launch
1. **Final content review** - Proofread all text
2. **Legal review** - Terms of service, privacy policy
3. **Stakeholder approval** - Get sign-off
4. **DNS preparation** - Configure isn.biz domain
5. **Analytics setup** - Add tracking code

### Launch Day
1. **Deploy to production** - Netlify deployment
2. **DNS cutover** - Point domain to new site
3. **SSL verification** - Confirm HTTPS working
4. **Cross-browser test** - Safari, Chrome, Firefox, Edge
5. **Mobile test** - iOS and Android
6. **Monitor** - Watch for errors/issues

### Post-Launch
1. **Submit to search engines** - Google, Bing
2. **Set up monitoring** - Uptime monitoring
3. **Social media announcement** - Share new site
4. **Investor outreach** - Email campaign
5. **Gather feedback** - Iterate based on response

---

## Performance Notes

### Running from Windows Filesystem (Current)
**Location:** `/mnt/d/workspace/ISNBIZ_Files/` (WSL mounting Windows)
**Performance:** Fine for this small site (54 KB total)
**Best for:** All operations (site is tiny)

### Running from Linux Filesystem (Optional)
**Location:** `/home/jdmal/workspace/ISNBIZ_Files/` (native ext4)
**Performance:** Faster but not necessary for this project
**Best for:** Not needed unless doing heavy git operations

For this lightweight static site, Windows filesystem performance is fine.

---

## Support & References

### Internal Documentation
- `CLAUDE.md` - Quick reference for AI assistance
- `DEPLOYMENT_CHECKLIST.md` - Pre-launch checklist
- `DEPLOY_TO_NETLIFY.md` - Deployment guide
- `BRAND_GUIDELINES.md` - Brand specifications
- `.serena/` - This directory (Serena context)

### External Resources
- **Netlify Docs:** https://docs.netlify.com/
- **HTML/CSS:** https://developer.mozilla.org/
- **Accessibility:** https://www.w3.org/WAI/WCAG21/quickref/

---

**Maintained by:** jdmal + Serena AI
**Review schedule:** Update when deployment occurs
**Purpose:** Enable Serena to provide context-aware assistance for ISN.BIZ website
**Status:** 🚀 Ready to deploy - awaiting final approval
