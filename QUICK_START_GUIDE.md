# Quick Start Guide - ISN.biz Homepage

## Immediate Next Steps

### 1. Preview the Website Locally
**Right now, you can view your new homepage:**

**Option A: Simple Double-Click**
1. Navigate to `/mnt/d/workspace/ISNBIZ_Files/`
2. Double-click `index.html`
3. It will open in your default browser

**Option B: Using a Local Server (Recommended)**
```bash
# Navigate to the directory
cd /mnt/d/workspace/ISNBIZ_Files/

# Python 3
python -m http.server 8000

# Then open browser to: http://localhost:8000
```

### 2. Customize Your Content (Priority)

#### A. Update Contact Email
**File:** `index.html`
**Line:** ~480

Change from placeholder:
```html
<p><a href="mailto:info@isn.biz">info@isn.biz</a></p>
```

To your actual email:
```html
<p><a href="mailto:youremail@isn.biz">youremail@isn.biz</a></p>
```

#### B. Add Real Metrics
**File:** `index.html`
**Lines:** ~45-57 (Hero Stats)

Update with your actual numbers:
```html
<div class="stat">
    <div class="stat-number">$2.5M</div>
    <div class="stat-label">Annual Revenue</div>
</div>
```

**Lines:** ~248-310 (Investor Section)
- Add specific ARR/MRR numbers
- Update customer counts
- Include retention rates
- Add growth percentages

#### C. Update Portfolio Examples
**File:** `index.html`
**Lines:** ~207-235

Replace generic examples with your actual projects:
- Client names (with permission)
- Real results and metrics
- Actual technologies used
- Specific industries served

### 3. Set Up Form Submission (Critical!)

Currently, the contact form shows a JavaScript alert. You need a real backend.

**Option A: Formspree (Easiest - Free tier available)**
1. Go to https://formspree.io
2. Create account and get form endpoint
3. Update form in `index.html` (line ~439):

```html
<form class="contact-form"
      action="https://formspree.io/f/YOUR_FORM_ID"
      method="POST">
```

4. Remove the JavaScript form handler at bottom of file

**Option B: Netlify Forms (If hosting on Netlify)**
Add to form tag:
```html
<form class="contact-form"
      name="contact"
      method="POST"
      data-netlify="true">
```

**Option C: Custom Backend**
Build your own API endpoint and update the JavaScript fetch in the form handler.

### 4. Deploy to Production

#### Recommended Hosting Options:

**A. Netlify (Recommended for Static Sites)**
1. Create account at https://netlify.com
2. Drag and drop the entire `ISNBIZ_Files` folder
3. Configure custom domain (isn.biz)
4. SSL is automatic
5. Forms work automatically (add data-netlify="true")

**B. Vercel**
1. Create account at https://vercel.com
2. Import project from Git or upload folder
3. Configure domain
4. SSL is automatic

**C. Traditional Web Hosting (cPanel, etc.)**
1. Upload all files via FTP/SFTP
2. Maintain folder structure
3. Configure SSL certificate
4. Point domain to hosting

**D. GitHub Pages (Free)**
1. Create GitHub repository
2. Push files to repository
3. Enable GitHub Pages in settings
4. Configure custom domain

### 5. Add Analytics (Do This Day 1)

#### Google Analytics 4
1. Create account at https://analytics.google.com
2. Get your Measurement ID
3. Add to `index.html` before `</head>`:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

#### Track Investor Actions
Add event tracking for:
- Pitch deck download button clicks
- Investor inquiry form submissions
- Data room access requests
- Demo request clicks

Example:
```javascript
document.querySelector('.investor-cta-button').addEventListener('click', () => {
    gtag('event', 'investor_inquiry', {
        'event_category': 'engagement',
        'event_label': 'pitch_deck_request'
    });
});
```

### 6. SEO Essentials (Week 1)

#### A. Google Search Console
1. Go to https://search.google.com/search-console
2. Add your property (isn.biz)
3. Verify ownership
4. Submit sitemap (create sitemap.xml)

#### B. Create Sitemap
Create `sitemap.xml` in root directory:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://isn.biz/</loc>
    <lastmod>2026-02-01</lastmod>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://isn.biz/#about</loc>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://isn.biz/#investors</loc>
    <priority>0.9</priority>
  </url>
</urlset>
```

#### C. Create robots.txt
Create `robots.txt` in root directory:
```
User-agent: *
Allow: /
Sitemap: https://isn.biz/sitemap.xml
```

### 7. External Profiles (Week 1-2)

Update these platforms to link to your new site:

1. **CrunchBase**
   - Update company profile
   - Add website link
   - Update description
   - Add funding information

2. **LinkedIn Company Page**
   - Update company description
   - Add website
   - Post about new site
   - Link from founder profiles

3. **AngelList/Wellfound**
   - Create or update profile
   - Link to website
   - Add pitch deck link
   - Update company metrics

### 8. Create Additional Pages (Priority Order)

#### Week 2: Privacy & Legal
- `privacy.html` - Privacy Policy (required)
- `terms.html` - Terms of Service (required)

#### Week 3: Team Page
- `team.html` - Executive bios with photos
- Professional headshots
- Detailed backgrounds
- LinkedIn links

#### Week 4: Investor Materials
- `investors.html` - Detailed investor relations page
- Pitch deck PDF (password-protected or gated)
- Financial highlights
- Data room access form

#### Month 2: Content Pages
- `solutions.html` - Detailed solutions pages
- `portfolio.html` - Full case studies
- `blog.html` - Thought leadership (SEO)
- `press.html` - Media and press coverage

### 9. Security Checklist

Before going live:
- [ ] SSL certificate installed (HTTPS)
- [ ] Form has CAPTCHA or honeypot (prevent spam)
- [ ] No sensitive data in HTML comments
- [ ] All external links have rel="noopener"
- [ ] Security headers configured
- [ ] Regular backups scheduled

### 10. Testing Checklist

Before announcing:
- [ ] Test on Chrome (desktop & mobile)
- [ ] Test on Safari (desktop & mobile)
- [ ] Test on Firefox
- [ ] Test on Edge
- [ ] Test all forms submit correctly
- [ ] Test all links work
- [ ] Test video embeds (when added)
- [ ] Check mobile navigation
- [ ] Test page load speed (< 3 seconds)
- [ ] Run accessibility checker
- [ ] Proofread all content

## Launch Day Checklist

### Morning of Launch:
1. [ ] Final content review
2. [ ] All forms tested
3. [ ] Analytics verified working
4. [ ] SSL certificate active
5. [ ] Mobile display perfect
6. [ ] All CTAs working

### Launch Announcements:
1. [ ] LinkedIn post (personal & company)
2. [ ] Email to existing contacts
3. [ ] Update email signatures
4. [ ] Update business cards
5. [ ] Press release (if appropriate)

### Post-Launch (First 24 Hours):
1. [ ] Monitor analytics
2. [ ] Check form submissions
3. [ ] Monitor error logs
4. [ ] Watch for broken links
5. [ ] Respond to inquiries quickly

## Quick Wins (Do These First)

### Priority 1 (Today):
1. Preview the site locally
2. Update contact email
3. Add your real company metrics
4. Test all navigation

### Priority 2 (This Week):
1. Set up form backend
2. Deploy to hosting
3. Configure SSL
4. Add Google Analytics
5. Update LinkedIn with link

### Priority 3 (Week 2):
1. Create privacy policy
2. Set up Google Search Console
3. Update external profiles
4. Add team photos/bios
5. Create pitch deck download

## Common Issues & Solutions

### Issue: Images Not Loading
**Solution:** Check file paths in HTML match folder structure
```html
<!-- Should be -->
<img src="logo-pallete/ISS2500.png">
<!-- Not -->
<img src="/logo-pallete/ISS2500.png">
```

### Issue: Fonts Not Loading
**Solution:** Google Fonts requires internet connection. For offline, download fonts locally.

### Issue: Form Not Submitting
**Solution:** Set up backend (Formspree/Netlify) or build custom API

### Issue: Mobile Menu Not Opening
**Solution:** Check JavaScript is enabled, clear browser cache

### Issue: Slow Loading
**Solution:**
1. Compress images (use TinyPNG.com)
2. Enable caching on server
3. Use CDN for assets
4. Minify CSS/JS

## Support Resources

### For Development:
- **HTML/CSS Questions:** https://stackoverflow.com
- **Hosting Help:** Your hosting provider's support
- **Domain Questions:** Your domain registrar

### For Content:
- **Stock Photos:** Unsplash, Pexels (free)
- **Icons:** Font Awesome, Heroicons
- **Colors:** Coolors.co (palette generator)

### For SEO:
- **Google Search Console:** https://search.google.com/search-console
- **Page Speed Insights:** https://pagespeed.web.dev
- **Schema Markup:** https://schema.org

### For Analytics:
- **Google Analytics:** https://analytics.google.com
- **Hotjar (Heatmaps):** https://www.hotjar.com

## Need Help?

If you need assistance with:
1. **Customization** - Refer to README.md customization guide
2. **Technical Issues** - Check browser console for errors
3. **Content Strategy** - Reference ISN-BIZ-FUNDING-READY-WEBSITE-REQUIREMENTS.md
4. **Deployment** - Follow hosting provider documentation

## Measuring Success

### Week 1 Metrics:
- Page views
- Bounce rate (target: < 50%)
- Average session duration (target: 2+ minutes)
- Form submissions

### Month 1 Goals:
- 100+ unique visitors
- 10+ investor inquiries
- 5+ demo requests
- Ranking on page 1 for "iSN.BiZ"

### Quarter 1 Objectives:
- 500+ unique visitors
- 25+ qualified investor leads
- 3+ investor meetings scheduled
- Top 3 ranking for company name + key terms

## Final Notes

**This website is investor-ready but living.** You should:
- Update metrics monthly
- Add case studies as you complete projects
- Post blog content regularly (SEO)
- Keep portfolio current
- Refresh design annually

**Remember:** Your deck gets you the meeting, but your website gets you the check. Keep it current, professional, and focused on investor priorities.

---

**Built:** February 1, 2026
**Version:** 1.0
**Status:** Ready for production deployment

Good luck with your fundraising! 🚀
