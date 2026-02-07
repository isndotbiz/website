# Deployment Gaps & External Dependencies

## Status: Ready for Deployment (with external TODOs)

This document lists items that require external access, credentials, or third-party services to complete.

---

## A. Analytics & Tracking

### Google Analytics 4 (GA4)
**Status:** TODO - Requires GA4 account setup
**Priority:** High
**Effort:** 15 minutes

**Steps:**
1. Create GA4 property at https://analytics.google.com/
2. Get Measurement ID (format: G-XXXXXXXXXX)
3. Add to `index.html` and all pages before `</head>`:

```html
<!-- Google Analytics 4 -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

**Files to update:** All 19 HTML pages
**Command:** Use find/replace in IDE or run script

---

## B. Form Backend

### Contact Form Processing
**Status:** STUB - Currently shows alert(), needs backend
**Priority:** Critical
**Effort:** 30 minutes

**Options:**

#### Option 1: Netlify Forms (Recommended if deploying to Netlify)
```html
<form name="contact" method="POST" data-netlify="true" netlify-honeypot="bot-field">
  <input type="hidden" name="form-name" value="contact" />
  <!-- existing form fields -->
</form>
```
- **Pros:** Built-in, free tier 100 submissions/month, spam protection
- **Cons:** Netlify-specific

#### Option 2: Formspree
```html
<form action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
  <!-- existing form fields -->
</form>
```
- **Pros:** Simple, works anywhere, free tier 50 submissions/month
- **Setup:** Sign up at https://formspree.io/
- **Cons:** 3rd party dependency

#### Option 3: Custom Backend
- **Pros:** Full control, no limits
- **Cons:** Requires server, more complex
- **Tech:** Node.js/Express, Python/Flask, or PHP
- **Files:** See `deploy/form-backend-example.js` (TODO: create)

**Current file:** `index.html:942-956` (Form submission handler)
**Action:** Replace alert() with chosen solution

---

## C. Error Pages

### 404 Page
**Status:** MISSING
**Priority:** Medium
**Effort:** 20 minutes

**Files needed:**
- `404.html` - Custom error page
- `.htaccess` (Apache) or `_redirects` (Netlify) for routing

**Template:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 - Page Not Found | ISN.BIZ Inc</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Nav from index.html -->
    <section class="hero" style="min-height: 60vh;">
        <div class="container">
            <h1>404 - Page Not Found</h1>
            <p>The page you're looking for doesn't exist.</p>
            <a href="index.html" class="btn btn-primary">Return Home</a>
        </div>
    </section>
    <!-- Footer from index.html -->
</body>
</html>
```

**Netlify config** (`_redirects`):
```
/*    /404.html    404
```

---

## D. Security Headers

### HTTP Security Headers
**Status:** TODO - Requires server/CDN configuration
**Priority:** High
**Effort:** 15 minutes

**Recommended headers:**
```
X-Frame-Options: DENY
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: geolocation=(), microphone=(), camera=()
Content-Security-Policy: default-src 'self' https://isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com https://fonts.googleapis.com https://fonts.gstatic.com; script-src 'self' 'unsafe-inline' https://www.googletagmanager.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; img-src 'self' data: https://isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com;
```

**Implementation:**

#### Netlify (`netlify.toml`):
```toml
[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "DENY"
    X-Content-Type-Options = "nosniff"
    X-XSS-Protection = "1; mode=block"
    Referrer-Policy = "strict-origin-when-cross-origin"
```

#### Apache (`.htaccess`):
```apache
<IfModule mod_headers.c>
  Header set X-Frame-Options "DENY"
  Header set X-Content-Type-Options "nosniff"
  Header set X-XSS-Protection "1; mode=block"
  Header set Referrer-Policy "strict-origin-when-cross-origin"
</IfModule>
```

#### TrueNAS/Kusanagi:
See `/mnt/tank/websites/kusanagi/isn.biz/nginx.conf` - add to server block

---

## E. Spam Protection

### reCAPTCHA v3 (for contact form)
**Status:** TODO - Requires Google reCAPTCHA keys
**Priority:** Medium
**Effort:** 20 minutes

**Steps:**
1. Get keys at https://www.google.com/recaptcha/admin/
2. Add to contact form:

```html
<script src="https://www.google.com/recaptcha/api.js?render=YOUR_SITE_KEY"></script>
<script>
  contactForm.addEventListener('submit', (e) => {
    e.preventDefault();
    grecaptcha.ready(function() {
      grecaptcha.execute('YOUR_SITE_KEY', {action: 'submit'}).then(function(token) {
        // Add token to form data
        // Submit to backend
      });
    });
  });
</script>
```

---

## F. Monitoring & Logging

### Error Logging
**Status:** TODO - Choose service
**Priority:** Low
**Effort:** 30 minutes

**Options:**
- **Sentry.io** - Frontend error tracking (free tier available)
- **LogRocket** - Session replay + error tracking
- **Google Cloud Logging** - If using GCP

**Example (Sentry):**
```html
<script src="https://browser.sentry-cdn.com/7.x.x/bundle.min.js"></script>
<script>
  Sentry.init({
    dsn: "YOUR_DSN_HERE",
    integrations: [new Sentry.BrowserTracing()],
    tracesSampleRate: 0.1,
  });
</script>
```

---

## G. Content Protection

### Investor Material Protection
**Status:** TODO - Design approach
**Priority:** Low
**Effort:** Variable

**Options:**

#### Option 1: Password Protection (Simple)
- Use Netlify password protection
- Or basic auth on server

#### Option 2: Gated Content (Medium)
- Require email signup for pitch deck
- Use Mailchimp/ConvertKit for email capture
- Serve PDF via signed URL

#### Option 3: NDA Required (Complex)
- DocuSign integration
- Custom auth system
- Store signed NDAs

**Recommended:** Start with Option 1, upgrade as needed

---

## H. External Profile Updates

### Professional Profiles
**Status:** Manual task - Cannot be automated
**Priority:** Medium
**Effort:** 60 minutes total

**Checklist:**

- [ ] **LinkedIn Company Page**
  - Update: https://linkedin.com/company/isn-biz-inc/
  - Add new website URL: https://isn.biz
  - Update description with new copy from About page
  - Add SpiritAtlas to products/services

- [ ] **CrunchBase**
  - Update: https://www.crunchbase.com/organization/isn-biz-inc
  - Add new URL, update description
  - Add recent projects

- [ ] **Wellfound (AngelList)**
  - Update: https://wellfound.com/company/isn-biz-inc
  - Add new URL, team photos
  - Update funding status

- [ ] **Google My Business**
  - Verify ownership if not done
  - Update website URL
  - Add recent photos

---

## I. Deployment Platforms

### Netlify Deployment
**Status:** READY - Just needs credentials
**Priority:** Critical
**Effort:** 10 minutes

**Steps:**
1. Log in to Netlify: https://app.netlify.com/
2. New site from Git → Connect to GitHub repo
3. Build settings: NONE (static site)
4. Domain: Point isn.biz to Netlify nameservers
5. SSL: Auto-configured

**Automation:**
```bash
# One-time setup
npm install -g netlify-cli
netlify login
netlify init

# Deploy
netlify deploy --prod
```

### TrueNAS Sync
**Status:** READY - Just needs credentials
**Priority:** Medium (dev environment)
**Effort:** 5 minutes

**Current:** Server at 100.83.75.4
**Path:** `/mnt/tank/websites/kusanagi/isn.biz/public/`

**Sync command:**
```bash
rsync -avz --delete \
  --exclude '.git' \
  --exclude 'node_modules' \
  --exclude '.serena' \
  ./ root@100.83.75.4:/mnt/tank/websites/kusanagi/isn.biz/public/
```

**Note:** Ask user for SSH key/password for TrueNAS access

---

## J. Performance Optimization

### Image Optimization
**Status:** COMPLETE (S3 + WebP)
**Priority:** Done
**Effort:** 0 minutes

All images already on S3 in WebP format. ✓

### Lazy Loading
**Status:** COMPLETE
**Priority:** Done
**Effort:** 0 minutes

All images have `loading="lazy"` except above-the-fold. ✓

### CDN for S3
**Status:** TODO - Optional improvement
**Priority:** Low
**Effort:** 20 minutes

**Options:**
- Cloudflare R2 + CDN (free tier available)
- AWS CloudFront (pay-per-use)
- Current S3 direct is acceptable for now

---

## Quick Start Deploy Checklist

### Minimum for Launch:
1. [ ] Get Netlify credentials
2. [ ] Deploy to Netlify
3. [ ] Point isn.biz domain
4. [ ] Set up GA4 (get ID)
5. [ ] Configure form backend (Netlify Forms recommended)
6. [ ] Add security headers via netlify.toml
7. [ ] Create 404.html page

### Week 1 Post-Launch:
8. [ ] Add reCAPTCHA to contact form
9. [ ] Set up error logging (Sentry)
10. [ ] Update LinkedIn, CrunchBase, Wellfound
11. [ ] Test on multiple devices/browsers

### Future Enhancements:
12. [ ] CloudFront CDN for S3
13. [ ] Investor material protection
14. [ ] A/B testing (Google Optimize)
15. [ ] Blog/news section

---

## Credentials Needed

**To proceed with full deployment, need:**

1. **Netlify account** - email/password or GitHub OAuth
2. **Google Analytics** - GA4 Measurement ID
3. **TrueNAS** - SSH key or root password for 100.83.75.4
4. **Domain DNS** - Access to isn.biz registrar (to point nameservers)
5. **(Optional) Google reCAPTCHA** - Site key + secret key
6. **(Optional) Sentry** - DSN for error tracking

**Store in:** 1Password CLI (already set up per CLAUDE.md)

---

## Summary

**Ready to deploy:** ✓ Static site is production-ready
**Blocking items:** Netlify credentials, GA4 ID, form backend choice
**Non-blocking:** reCAPTCHA, error logging, profile updates, CDN

**Next step:** Provide Netlify credentials to deploy, or run:
```bash
netlify deploy --prod
```

**Estimated time to full production:** 90 minutes with all credentials available
