# ISN.BIZ Manual Deployment Guide

**Status:** Automated deployment can't connect to TrueNAS (network issue)
**Solution:** Deploy manually from TrueNAS server

---

## Option 1: Pull from GitHub on TrueNAS (RECOMMENDED)

```bash
# SSH to TrueNAS
ssh jdmal@10.0.0.89

# Navigate to website directory
cd /mnt/tank/websites/kusanagi/isn.biz/public

# Pull latest changes
git pull origin main

# Verify
ls -la

# Check what was updated
git log --oneline -7
```

**This will deploy:**
- 24 business visuals
- 9 project pages
- 4 founder pages
- Updated homepage
- All documentation

---

## Option 2: Direct Git Clone (If needed)

```bash
# SSH to TrueNAS
ssh jdmal@10.0.0.89

# Navigate to websites directory
cd /mnt/tank/websites/kusanagi/isn.biz/

# Backup current public directory
mv public public.backup.$(date +%Y%m%d)

# Clone fresh from GitHub
git clone https://github.com/isndotbiz/website.git public

# Set permissions
chown -R kusanagi:www-data public
chmod -R 755 public
```

---

## Verify Deployment

**After deploying, check:**

1. **Clear browser cache:** Ctrl+Shift+R or Cmd+Shift+R
2. **Visit:** https://isn.biz
3. **Check:**
   - Homepage loads with new layout
   - 9 project pages accessible
   - 4 founder pages working
   - Business visuals displaying
   - Mobile responsive

---

## What Got Deployed (7 Commits)

1. **ee847ae** - Business visuals documentation and preview page
2. **152ce4f** - Comprehensive progress report - 24 visuals + 13 pages
3. **68ef9d6** - Add 7 more business visuals (24 total!)
4. **c844e9e** - Visual work progress tracker
5. **9afed1a** - Add 9 business visuals generated with fal.ai/gpt-image-1.5
6. **4a16f26** - Comprehensive website update completion report
7. **f3efe0e** - Fix image paths in opportunity-bot.html

---

## Network Issue

Automated deployment from local machine failed to connect to 10.0.0.89.

**Possible causes:**
- Not on 10.0.0.0/24 network
- VPN not connected
- SSH key issues
- TrueNAS firewall

**Solution:** Deploy directly from TrueNAS server (see above)

---

## After Deployment

**Test these URLs:**
- https://isn.biz
- https://isn.biz/opportunity-bot.html
- https://isn.biz/truenas.html
- https://isn.biz/jonathan.html
- https://isn.biz/preview_business_visuals.html

---

**Everything's ready - just pull from GitHub!** 🚀
