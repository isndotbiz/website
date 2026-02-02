# ISN.BIZ Deployment Guide

Complete guide for deploying the ISN.BIZ investor website to TrueNAS Kusanagi with S3-hosted images.

## Overview

**Architecture:**
- **HTML/CSS/JS** → Deployed to TrueNAS Kusanagi (`/mnt/tank/websites/kusanagi/isn.biz`)
- **All Images** → Hosted on S3 (`isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com`)
- **SSL** → Let's Encrypt via Certbot or Kusanagi
- **DNS** → Cloudflare

**Why this architecture?**
- Minimal files on TrueNAS (only ~50 HTML/CSS/JS files, < 5MB)
- Images served from S3 CDN (fast, scalable, 173MB of optimized WebP images)
- Easy to update - just deploy HTML files, images stay on S3
- Preserves TrueNAS subdomain configurations

---

## Prerequisites

1. **AWS Credentials** configured (for S3 upload)
   ```bash
   aws configure
   # Or set env vars: AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
   ```

2. **1Password CLI** authenticated
   ```bash
   eval $(op signin)
   ```

3. **Network Access** to TrueNAS (10.0.0.89)
   - Must be on 10.0.0.0/24 network or VPN

4. **Python 3.11+** with pip

---

## Quick Start (Automated)

The easiest way to deploy everything:

```bash
cd /mnt/d/workspace/ISNBIZ_Files
./deploy_complete.sh
```

This script will:
1. Optimize and upload all images to S3
2. Update HTML files to reference S3 URLs
3. Deploy HTML/CSS/JS to TrueNAS
4. Guide you through SSL and DNS setup

---

## Manual Deployment (Step by Step)

### Step 1: Upload Images to S3

```bash
# Install dependencies
pip install boto3 pillow

# Upload images (this will optimize and convert to WebP)
python3 upload_images_to_s3.py
```

**What this does:**
- Finds all images in `assets/` directory
- Converts to WebP format (quality=85)
- Optimizes for web delivery
- Uploads to S3 with public-read ACL
- Creates `s3_url_mapping.json` mapping file

**Expected output:**
```
📊 Statistics:
  Total files:        44+ images
  Uploaded:           44+
  Original size:      ~200 MB
  Optimized size:     ~100 MB
  Total savings:      ~50%
```

### Step 2: Update HTML Files

```bash
python3 update_html_to_s3_urls.py
```

**What this does:**
- Reads `s3_url_mapping.json`
- Updates all `*.html` files to use S3 URLs
- Creates `.backup` files of originals
- Replaces local paths like `assets/founders/...` with `https://isnbiz-assets...`

**Important:** This modifies your HTML files! Backups are created automatically.

### Step 3: Deploy to TrueNAS

```bash
./deploy_to_truenas.sh
```

**What this does:**
1. Authenticates with 1Password
2. Tests TrueNAS connection
3. Backs up existing site (if any)
4. Creates tarball of HTML/CSS/JS (NO images)
5. Transfers to TrueNAS
6. Extracts to `/mnt/tank/websites/kusanagi/isn.biz`
7. Sets proper permissions (www-data:www-data)

**Expected package size:** ~2-5 MB (vs 173MB if images were included)

### Step 4: Configure SSL

**SSH to TrueNAS:**
```bash
ssh jdmal@10.0.0.89
```

**Option A: Certbot (Recommended)**
```bash
sudo certbot --nginx -d isn.biz -d www.isn.biz

# Follow prompts:
# - Enter email for renewal notifications
# - Agree to Terms of Service
# - Choose whether to redirect HTTP to HTTPS (recommended: yes)
```

**Option B: ACME.sh**
```bash
sudo acme.sh --issue -d isn.biz -d www.isn.biz --nginx
sudo acme.sh --install-cert -d isn.biz \
    --cert-file /etc/ssl/certs/isn.biz.crt \
    --key-file /etc/ssl/private/isn.biz.key \
    --fullchain-file /etc/ssl/certs/isn.biz.fullchain.crt \
    --reloadcmd "systemctl reload nginx"
```

**Option C: Kusanagi SSL Tool**
```bash
sudo kusanagi ssl isn.biz
```

**Verify SSL:**
```bash
sudo certbot certificates  # Check expiry and details
curl -I https://isn.biz    # Should return 200 OK with HTTPS
```

### Step 5: Configure Cloudflare DNS

**Log into Cloudflare:**
1. Go to https://dash.cloudflare.com
2. Select `isn.biz` domain

**DNS Records:**
```
Type   Name         Content              Proxy  TTL
A      isn.biz      [Your Public IP]     ON     Auto
A      www          [Your Public IP]     ON     Auto
```

**Important:** If TrueNAS is behind NAT/router:
- Use your public/external IP in DNS
- Or use Cloudflare Tunnel
- Existing subdomains should NOT be affected

**SSL/TLS Settings:**
- **Encryption mode:** Full (strict)
- **Always Use HTTPS:** ON
- **Automatic HTTPS Rewrites:** ON
- **Minimum TLS Version:** 1.2

**Verify DNS propagation:**
```bash
dig isn.biz +short           # Should show your IP
dig www.isn.biz +short       # Should show your IP
nslookup isn.biz 1.1.1.1    # Check Cloudflare's resolver
```

### Step 6: Verify Deployment

**Test from command line:**
```bash
# Check HTTP redirect
curl -I http://isn.biz
# Should redirect to https://

# Check HTTPS
curl -I https://isn.biz
# Should return 200 OK

# Check www subdomain
curl -I https://www.isn.biz
# Should work too
```

**Test in browser:**
1. Open https://isn.biz
2. Verify:
   - ✅ Secure (HTTPS with valid cert)
   - ✅ Main page loads
   - ✅ Founder images load (from S3)
   - ✅ Founder pages work (alicia.html, bri.html, jonathan.html, lilly.html)
   - ✅ All 8 project pages work
   - ✅ Portfolio page shows all projects
   - ✅ All images display correctly (check Network tab - should load from S3)

**Check browser console:**
- No 404 errors for images
- No mixed content warnings (HTTP resources on HTTPS page)
- All S3 URLs should load successfully

### Step 7: Verify Subdomains (Critical!)

**Test each existing subdomain:**
```bash
# List your subdomains (example):
curl -I https://portainer.isn.biz
curl -I https://grafana.isn.biz
curl -I https://[service].isn.biz
```

If any subdomain is broken:
1. Check nginx configuration: `/etc/nginx/sites-available/`
2. Ensure virtual host configs weren't overwritten
3. Reload nginx: `sudo systemctl reload nginx`

---

## Troubleshooting

### Images not loading

**Symptom:** Broken image icons, 404 errors

**Check:**
```bash
# Verify S3 URLs in HTML
grep "isnbiz-assets" index.html | head -5

# Test S3 URL directly
curl -I https://isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com/assets/founders/headshots_with_bg/jonathan_headshot.webp
```

**Fix:** Re-run `update_html_to_s3_urls.py`

### SSL certificate issues

**Symptom:** Browser shows "Not Secure" or certificate errors

**Check:**
```bash
sudo certbot certificates
sudo nginx -t  # Test nginx config
sudo systemctl status nginx
```

**Fix:**
```bash
sudo certbot renew --dry-run  # Test renewal
sudo certbot --nginx -d isn.biz -d www.isn.biz  # Re-run setup
```

### Cloudflare mixed content warnings

**Symptom:** Some resources blocked due to HTTP on HTTPS page

**Fix:**
1. Cloudflare → SSL/TLS → Edge Certificates → Always Use HTTPS: ON
2. Check HTML for any `http://` URLs, should all be `https://`

### Subdomain broken after deployment

**Symptom:** Existing subdomains return 404 or redirect incorrectly

**Check nginx configs:**
```bash
sudo ls -la /etc/nginx/sites-available/
sudo cat /etc/nginx/sites-available/[subdomain-config]
```

**Fix:**
1. Ensure each subdomain has its own virtual host config
2. Main site (`isn.biz`) should not have catch-all that breaks other subdomains
3. Reload nginx: `sudo systemctl reload nginx`

---

## Rollback Procedures

### Restore HTML files from backup

```bash
# On local machine
cd /mnt/d/workspace/ISNBIZ_Files
for f in *.html.backup; do
    mv "$f" "${f%.backup}"
done
```

### Restore TrueNAS site from backup

```bash
# SSH to TrueNAS
ssh jdmal@10.0.0.89

# Find backup
ls -la /mnt/tank/backups/websites/

# Restore (replace TIMESTAMP with actual backup timestamp)
sudo cp -r /mnt/tank/backups/websites/isn.biz_TIMESTAMP/* /mnt/tank/websites/kusanagi/isn.biz/

# Reload nginx
sudo systemctl reload nginx
```

---

## Maintenance

### Update site content

**To update HTML/CSS/JS only:**
```bash
# Edit files locally
# Then re-run deployment
./deploy_to_truenas.sh
```

**To add new images:**
```bash
# Add images to assets/ directory
# Convert to WebP and upload to S3
python3 upload_images_to_s3.py

# Update HTML to reference new S3 URLs
python3 update_html_to_s3_urls.py

# Deploy updated HTML
./deploy_to_truenas.sh
```

### SSL certificate renewal

Certbot auto-renews via cron. To manually renew:
```bash
ssh jdmal@10.0.0.89
sudo certbot renew
sudo systemctl reload nginx
```

### Monitor site performance

```bash
# Check site response time
time curl -I https://isn.biz

# Check S3 image load times
time curl -I https://isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com/assets/founders/headshots_with_bg/jonathan_headshot.webp
```

---

## File Structure

**On TrueNAS (`/mnt/tank/websites/kusanagi/isn.biz/`):**
```
├── index.html
├── about.html
├── portfolio.html
├── investors.html
├── contact.html
├── alicia.html
├── bri.html
├── jonathan.html
├── lilly.html
├── project-*.html (8 files)
├── styles.css
├── script.js
├── enhanced-animations.css
└── enhanced-interactions.js
```

**On S3 (`s3://isnbiz-assets-1769962280/assets/`):**
```
assets/
├── founders/
│   ├── headshots_with_bg/ (4 WebP images)
│   ├── headshots_no_bg/ (4 WebP images)
│   ├── corporate_photos/ (16 WebP images)
│   ├── casual_variants/ (16 WebP images)
│   └── group_photos/ (4 WebP images)
├── projects/ (36+ WebP images)
├── backgrounds/ (WebP images)
└── hero_backgrounds/ (WebP images)
```

---

## Security Checklist

- [x] HTTPS enabled with valid SSL certificate
- [x] HTTP redirects to HTTPS
- [x] Cloudflare SSL mode set to "Full (strict)"
- [x] S3 bucket has public-read on images only (not upload/delete)
- [x] TrueNAS site directory owned by www-data
- [x] Nginx running as www-data (non-root)
- [x] Subdomain configurations preserved
- [x] No sensitive files in web root

---

## Support and References

**Certbot Documentation:**
- https://certbot.eff.org/instructions

**Cloudflare SSL:**
- https://developers.cloudflare.com/ssl/

**AWS S3:**
- https://docs.aws.amazon.com/s3/

**Kusanagi:**
- https://en.kusanagi.tokyo/

---

**Last Updated:** 2026-02-02
**Author:** ISN.BIZ Development Team + Claude AI
**Version:** 1.0
