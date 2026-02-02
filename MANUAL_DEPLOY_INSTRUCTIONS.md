# Manual Deployment Instructions

Since automated deployment can't reach TrueNAS from this environment, follow these steps to deploy manually.

## ✅ What's Already Done

- [x] All images uploaded to S3 (126 images, 9.47MB)
- [x] HTML files updated to use S3 URLs
- [x] Deployment package created (107KB)
- [x] All pages tested and ready

## 🚀 Deploy in 3 Steps

### Step 1: Open Terminal on Your Local Machine

Make sure you're on the 10.0.0.0/24 network or connected via VPN.

### Step 2: Copy Files to TrueNAS

```bash
cd /mnt/d/workspace/ISNBIZ_Files

# Option A: Using SCP (if SSH keys are set up)
scp /tmp/isn-biz-truenas.tar.gz jdmal@10.0.0.89:/tmp/

# Option B: Using rsync
rsync -avz /tmp/isn-biz-truenas.tar.gz jdmal@10.0.0.89:/tmp/
```

If prompted for password, use the TrueNAS password from 1Password:
```bash
op read "op://TrueNAS Infrastructure/localhost/password"
```

### Step 3: SSH to TrueNAS and Deploy

```bash
# SSH to TrueNAS
ssh jdmal@10.0.0.89

# Backup existing site (if any)
sudo mkdir -p /mnt/tank/backups/websites/isn.biz_$(date +%Y%m%d_%H%M%S)
sudo cp -r /mnt/tank/websites/kusanagi/isn.biz/public/* \
    /mnt/tank/backups/websites/isn.biz_$(date +%Y%m%d_%H%M%S)/ 2>/dev/null || echo "No existing site"

# Create/clear site directory
sudo mkdir -p /mnt/tank/websites/kusanagi/isn.biz/public
sudo rm -rf /mnt/tank/websites/kusanagi/isn.biz/public/*

# Extract deployment package
cd /mnt/tank/websites/kusanagi/isn.biz/public
sudo tar xzf /tmp/isn-biz-truenas.tar.gz

# Set permissions
sudo chown -R www-data:www-data /mnt/tank/websites/kusanagi/isn.biz/public
sudo chmod -R 755 /mnt/tank/websites/kusanagi/isn.biz/public
sudo find /mnt/tank/websites/kusanagi/isn.biz/public -type f -exec chmod 644 {} \;

# Verify
ls -lh /mnt/tank/websites/kusanagi/isn.biz/public
echo "Total files: $(find /mnt/tank/websites/kusanagi/isn.biz/public -type f | wc -l)"

# Restart nginx
sudo systemctl restart nginx

# Clean up
rm /tmp/isn-biz-truenas.tar.gz
```

### Step 4: Configure SSL (if not done)

```bash
# Still SSH'd into TrueNAS
sudo certbot --nginx -d isn.biz -d www.isn.biz

# Or using Kusanagi
sudo kusanagi ssl isn.biz

# Verify
sudo certbot certificates
curl -I https://isn.biz
```

### Step 5: Test the Site

**From command line:**
```bash
curl -I https://isn.biz
curl -I https://www.isn.biz
```

**In browser:**
1. Open https://isn.biz
2. Verify all images load from S3
3. Test all founder pages (alicia.html, bri.html, jonathan.html, lilly.html)
4. Test all 8 project pages
5. Check on mobile device

### Step 6: Verify Subdomains (Important!)

Test each subdomain to ensure they weren't affected:
```bash
# Example (replace with your actual subdomains)
curl -I https://portainer.isn.biz
curl -I https://grafana.isn.biz
# etc...
```

---

## 🔧 Alternative: Quick Copy Method

If the tar.gz approach doesn't work, copy files directly:

```bash
# From your local machine
cd /mnt/d/workspace/ISNBIZ_Files

# Copy all HTML/CSS/JS to TrueNAS
scp *.html *.css *.js jdmal@10.0.0.89:/tmp/isn-site/

# Then SSH and move to web root
ssh jdmal@10.0.0.89
sudo mkdir -p /mnt/tank/websites/kusanagi/isn.biz/public
sudo mv /tmp/isn-site/* /mnt/tank/websites/kusanagi/isn.biz/public/
sudo chown -R www-data:www-data /mnt/tank/websites/kusanagi/isn.biz/public
sudo systemctl restart nginx
```

---

## 📋 Verification Checklist

After deployment, verify:

- [ ] Site loads: https://isn.biz
- [ ] SSL certificate valid (green padlock)
- [ ] All founder images load from S3
- [ ] All project images load from S3
- [ ] Founder pages work (4 pages)
- [ ] Project pages work (8 pages)
- [ ] Mobile responsive
- [ ] No console errors
- [ ] All subdomains still work

---

## 🛟 If Something Goes Wrong

**Rollback:**
```bash
ssh jdmal@10.0.0.89
sudo cp -r /mnt/tank/backups/websites/isn.biz_[timestamp]/* \
    /mnt/tank/websites/kusanagi/isn.biz/public/
sudo systemctl reload nginx
```

**Check nginx logs:**
```bash
sudo tail -f /var/log/nginx/error.log
sudo tail -f /var/log/nginx/access.log
```

---

## 🎯 What's Deployed

**TrueNAS (107KB):**
- 33 HTML files
- 3 CSS files
- 2 JS files

**S3 CDN (9.47MB):**
- 44 founder images
- 36 project images
- 46+ other images
- All optimized WebP format

**Total site load:** ~10MB (served globally from S3 CDN)

---

Ready to deploy! Run the commands above when you're on the TrueNAS network.
