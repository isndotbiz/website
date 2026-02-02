# ISN.BIZ WordPress Deployment Instructions

**Status:** Ready to deploy
**Target:** Kusanagi on TrueNAS (10.0.0.89)
**Theme:** ISN.BIZ 2026 v3.0.0

---

## Quick Start (Easiest Method)

**From your local machine (WSL or Git Bash):**

```bash
cd /d/workspace/ISNBIZ_Files  # or /mnt/d/workspace/ISNBIZ_Files in WSL
bash deploy-from-local.sh
```

This script will:
1. Transfer the theme to TrueNAS
2. Set up WordPress on Kusanagi
3. Deploy and activate the theme
4. Create all pages and menus

**Done in 5-10 minutes!** 🚀

---

## Manual Deployment (Alternative)

If you prefer to run commands manually:

### Step 1: Transfer Theme to TrueNAS

```bash
scp wp-theme-isnbiz-2026.tar.gz jdmal@10.0.0.89:/tmp/
scp deploy-to-kusanagi.sh jdmal@10.0.0.89:/tmp/
```

### Step 2: SSH to TrueNAS

```bash
ssh jdmal@10.0.0.89
```

### Step 3: Run Deployment Script

```bash
chmod +x /tmp/deploy-to-kusanagi.sh
bash /tmp/deploy-to-kusanagi.sh
```

Follow the prompts to complete setup.

---

## What Gets Created

### Kusanagi Site
- **Domain:** isn.biz
- **PHP Version:** 8.2
- **Database:** isnbiz_wp
- **SSL:** Let's Encrypt (auto-configured)

### WordPress Installation
- **Site Title:** iSN.BiZ Inc
- **Admin URL:** https://isn.biz/wp-admin
- **Credentials:** Generated during setup (save them!)

### WordPress Pages
- Home (set as front page)
- About (Template: About)
- Services (Template: Services)
- Portfolio (Template: Portfolio)
- Investors (Template: Investors)
- Contact (Template: Contact)

### WordPress Settings
- **Permalinks:** Post name (/%postname%/)
- **Timezone:** America/Los_Angeles
- **Menu:** Primary Menu (auto-created with all pages)
- **Theme:** ISN.BIZ 2026 (activated)

---

## Post-Deployment Checklist

### 1. Login to WordPress Admin
```
URL: https://isn.biz/wp-admin
Username: [generated during setup]
Password: [generated during setup]
```

### 2. Assign Page Templates
Some pages need specific templates:
- Go to Pages → All Pages
- Edit each page:
  - **Portfolio** → Template: Portfolio
  - **About** → Template: About
  - **Services** → Template: Services
  - **Investors** → Template: Investors
  - **Contact** → Template: Contact

### 3. Verify Pages Display Correctly
Visit each page and verify content appears:
- https://isn.biz/ (homepage)
- https://isn.biz/about/
- https://isn.biz/services/
- https://isn.biz/portfolio/
- https://isn.biz/investors/
- https://isn.biz/contact/

### 4. Test Functionality
- ✅ All images load from S3
- ✅ Navigation menu works
- ✅ Portfolio shows all 9 projects
- ✅ Mobile responsiveness
- ✅ Accessibility (WCAG 2.1 AA)

### 5. Configure DNS
Point isn.biz domain to TrueNAS:
```
A Record: isn.biz → [TrueNAS IP]
```

### 6. Optional: Install Plugins
Recommended WordPress plugins:
- **Wordfence Security** (security)
- **WP Super Cache** (performance)
- **Contact Form 7** (forms, if needed)
- **Yoast SEO** (SEO optimization)

---

## Troubleshooting

### "Cannot connect to TrueNAS"
```bash
# Add SSH key manually:
ssh-copy-id -i ~/.ssh/truenas_jdmal jdmal@10.0.0.89
```

### "Theme package not found"
```bash
# Verify theme exists:
ls -lh D:/workspace/ISNBIZ_Files/wp-theme-isnbiz-2026.tar.gz
```

### "Kusanagi command not found"
Kusanagi is not installed on TrueNAS. Install it first:
```bash
curl -sS https://kusanagi.tokyo/get | sudo bash
```

### "SSL certificate failed"
Ensure:
- Domain DNS points to TrueNAS
- Port 80 and 443 are open
- Email is valid

---

## Files Included

**Deployment Scripts:**
- `deploy-from-local.sh` - Run from your local machine (easiest)
- `deploy-to-kusanagi.sh` - Run on TrueNAS server (manual)

**Theme Package:**
- `wp-theme-isnbiz-2026.tar.gz` (70KB) - Complete WordPress theme

**Theme Files:**
- `wp-theme-isnbiz-2026/` - Uncompressed theme directory
- All PHP templates, CSS, JS, and documentation

---

## Support

**Documentation:**
- Theme README: `wp-theme-isnbiz-2026/README.md`
- Installation Guide: `wp-theme-isnbiz-2026/INSTALLATION_GUIDE.md`
- WordPress Theme Ready: `WORDPRESS_THEME_READY.md`

**Kusanagi Documentation:**
- https://kusanagi.tokyo/en/document/

**WordPress Documentation:**
- https://wordpress.org/support/

---

## Next Steps After Deployment

1. **Content Review** - Review all pages for accuracy
2. **SEO Setup** - Configure meta descriptions, keywords
3. **Analytics** - Add Google Analytics 4
4. **Testing** - Test on multiple devices and browsers
5. **Launch** - Update DNS and announce!

---

**Created:** 2026-02-01
**Version:** 3.0.0
**Status:** Production Ready
