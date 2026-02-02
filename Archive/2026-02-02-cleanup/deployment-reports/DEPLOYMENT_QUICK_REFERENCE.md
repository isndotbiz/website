# ISN.BIZ Website - Deployment Quick Reference

## Current Status ✅ LIVE

**Website:** https://isn.biz
**Deployment Date:** February 2, 2026
**Location:** TrueNAS Kusanagi at `/mnt/tank/websites/kusanagi/isn.biz/public/`
**S3 Bucket:** `isnbiz-assets-1769962280` (us-east-1)

---

## Quick Links

### Production URLs
| Page | URL |
|------|-----|
| Homepage | https://isn.biz |
| About | https://isn.biz/about.html |
| Services | https://isn.biz/services.html |
| Portfolio | https://isn.biz/portfolio.html |
| Investors | https://isn.biz/investors.html |
| Contact | https://isn.biz/contact.html |
| Alicia (Founder) | https://isn.biz/alicia.html |
| Bri (Founder) | https://isn.biz/bri.html |
| Jonathan (Founder) | https://isn.biz/jonathan.html |
| Lilly (Founder) | https://isn.biz/lilly.html |

---

## What's Deployed

### Pages & Code
- ✅ 12 HTML pages (~530KB)
- ✅ 3 CSS files (~70KB, 404+ rules)
- ✅ 3 JavaScript files (~22.7KB)
- ✅ Responsive design (4 breakpoints)
- ✅ WCAG 2.1 AA accessibility

### Assets
- ✅ 150+ local images (WebP optimized)
- ✅ 57+ S3 images (live)
- ✅ 4 founder headshots
- ✅ 5 portfolio project images
- ✅ 3 service icons
- ✅ 7 logo variants
- ✅ 2 social sharing images (OG)
- ✅ 44+ generated tech/office images

### Infrastructure
- ✅ Let's Encrypt SSL/HTTPS
- ✅ Nginx web server
- ✅ Custom domain: isn.biz
- ✅ S3 CDN integration
- ✅ Automatic backups

---

## Asset Locations

### Local (Development)
```
D:\workspace\ISNBIZ_Files\
├── assets/
│   ├── founders/ (headshots, corporate, casual, group)
│   ├── generated/ (tech, office, icons)
│   ├── premium_v3/ (logos, portfolio, services, OG images)
│   └── projects/ (project showcase images)
```

### S3 (Production)
```
s3://isnbiz-assets-1769962280/
├── premium_v3/
│   ├── logos/ (favicon, navbar, hero, footer)
│   ├── og/ (social sharing)
│   ├── services/ (with responsive variants)
│   ├── portfolio/ (with responsive variants)
│   └── founders/ (with responsive variants)
├── assets/founders/ (original headshots)
└── generated/ (tech & office images)
```

---

## Deployed Images Summary

### By Category

| Category | Count | Status | S3 URL |
|----------|-------|--------|--------|
| Logos | 7 | ✅ Deployed | premium_v3/logos/ |
| Founder Profiles | 4 | ✅ Deployed | assets/founders/headshots_with_bg/ |
| Portfolio Projects | 5+ | ✅ Deployed | premium_v3/portfolio/ |
| Service Icons | 3+ | ✅ Deployed | premium_v3/services/ |
| Open Graph | 2 | ✅ Deployed | premium_v3/og/ |
| Generated Assets | 44+ | ✅ Deployed | generated/ |
| **TOTAL** | **57+** | **✅ All Live** | **Public Access** |

### Referenced in HTML

```html
<!-- Logos -->
<img src="https://isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com/premium_v3/logos/favicon.webp">
<img src="https://isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com/premium_v3/logos/navbar_logo.webp">

<!-- Founder Profiles -->
<img src="https://isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com/assets/founders/headshots_with_bg/alicia_headshot.webp">

<!-- Portfolio Projects -->
<img src="https://isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com/premium_v3/portfolio/opportunity_bot.webp">

<!-- Social Sharing -->
<meta property="og:image" content="https://isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com/premium_v3/og/og_default.webp">
```

---

## Testing Checklist

### Homepage
- [ ] Visit https://isn.biz
- [ ] Logo loads in navbar
- [ ] Hero section displays properly
- [ ] Company info visible
- [ ] Portfolio preview shows images
- [ ] All buttons clickable

### Founder Profiles
- [ ] Visit https://isn.biz/alicia.html
- [ ] Founder image loads from S3
- [ ] Bio text displays
- [ ] Links to other pages work

### Portfolio
- [ ] Visit https://isn.biz/portfolio.html
- [ ] All 5 project images load
- [ ] Descriptions display
- [ ] Project links functional

### Mobile
- [ ] Test on phone (375px width)
- [ ] Navigation menu works
- [ ] Images responsive
- [ ] Text readable
- [ ] Forms functional

### Performance
- [ ] Lighthouse score 90+
- [ ] Images load from S3 CDN
- [ ] No 404 errors
- [ ] Page load <3 seconds

---

## Common Issues & Solutions

### Images Not Loading
1. Check browser console for 404 errors
2. Verify S3 bucket is public read
3. Check URL format: `https://isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com/...`
4. Clear browser cache and reload

### Slow Page Load
1. Check S3 access (should be instant)
2. Run Lighthouse audit for suggestions
3. Verify WebP format used (optimal compression)
4. Consider CloudFront CDN if issues persist

### Mobile Menu Not Working
1. Open browser console
2. Check for JavaScript errors
3. Verify script.js loads
4. Test on actual device (not just browser resize)

### Form Not Submitting
1. Check contact form backend (not yet configured)
2. Verify form HTML structure
3. Check for validation errors
4. Implement Formspree or Netlify Forms

---

## Maintenance Tasks

### Monthly
- [ ] Run Lighthouse audit (target 90+)
- [ ] Check SSL certificate (auto-renews)
- [ ] Review S3 bucket costs
- [ ] Verify all links work
- [ ] Test mobile responsiveness

### Quarterly
- [ ] Update content as needed
- [ ] Review analytics
- [ ] Optimize slow-loading images
- [ ] Update team bios if needed

### As Needed
- [ ] Update portfolio projects
- [ ] Add new images to S3
- [ ] Fix broken links
- [ ] Improve SEO meta tags

---

## Update Procedures

### Update Local Assets
```bash
cd D:\workspace\ISNBIZ_Files
# Edit or replace files in assets/
git add .
git commit -m "Update: asset changes"
git push
```

### Update HTML Content
```bash
cd D:\workspace\ISNBIZ_Files
# Edit index.html, about.html, etc.
# Test locally by opening in browser
git add .
git commit -m "Update: content changes"
git push
```

### Upload New Assets to S3
```bash
# From local machine
aws s3 sync assets/premium_v3/ \
  s3://isnbiz-assets-1769962280/premium_v3/ \
  --include "*.webp"
```

### Deploy to TrueNAS
```bash
# SSH to TrueNAS
ssh jdmal@10.0.0.89

# Copy files from git
cd /mnt/tank/websites/kusanagi/isn.biz/public/
git pull origin main
```

---

## Key Statistics

### Code Size
- HTML: ~530KB (12 pages)
- CSS: ~70KB (3 files, 404+ rules)
- JavaScript: ~22.7KB (3 files)
- **Total Code:** ~622.7KB

### Assets
- Total Images: 150+ local, 57+ on S3
- Formats: WebP (optimized), PNG (archive)
- Founder Photos: 36 images (4 founders × 9 variants)
- Portfolio Images: 8+ projects
- Generated: 44+ tech/office themed
- Storage: ~500MB locally, unlimited S3

### Performance
- Target Load Time: <3 seconds
- Image Format: WebP (30-40% smaller than PNG)
- Responsive: Mobile, Tablet, Desktop
- Accessibility: WCAG 2.1 AA
- SSL: Let's Encrypt (auto-renewed)

---

## Contact & Support

### For Issues
- Check this document first
- Review DEPLOYMENT_ASSET_AUDIT_2026_02_02.md for details
- Check website error logs on TrueNAS

### Credentials (in 1Password)
- AWS S3: "isnbiz-assets" vault
- TrueNAS SSH: "TrueNAS Infrastructure" vault
- Domain: Cloudflare DNS configuration

### Monitoring
- Website: https://isn.biz (live)
- S3 Bucket: AWS Console
- Logs: TrueNAS Nginx logs
- Performance: Lighthouse audits

---

## Brand Colors

```css
--color-blue: #1E9FF2       /* Primary - buttons, links */
--color-cyan: #5FDFDF       /* Secondary - accents */
--color-charcoal: #0D1117   /* Dark - backgrounds */
--color-gray-light: #E8EAF0 /* Light - borders */
```

## Typography

- **Headlines:** Archivo Black
- **Body:** IBM Plex Sans
- **Code:** JetBrains Mono

---

## Company Information (Deployed)

**ISN.BIZ Inc**
- DUNS: 080513772
- UBI: 603-522-339
- EIN: 47-4530188
- Founded: July 8, 2015
- Website: https://isn.biz
- Status: Active, Deployment Complete

---

**Last Updated:** 2026-02-02
**Status:** ✅ LIVE and VERIFIED
**Next Review:** 2026-02-09
