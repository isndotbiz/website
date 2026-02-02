# Deployment Guide

## Overview

The ISN.BIZ website is a static site that can be deployed to various hosting platforms. This guide covers the recommended deployment methods.

## Recommended: Netlify Deployment

### Why Netlify?
- **Easiest deployment** - Drag-and-drop or Git-based
- **Free SSL** - HTTPS included automatically
- **CDN included** - Global distribution for fast loading
- **Form handling** - Built-in form backend (no server needed)
- **Auto-deploy** - Push to Git = automatic deployment
- **Custom domains** - Easy DNS configuration

### Method 1: Git-Based Auto-Deploy (Recommended)

**One-time setup:**
```bash
# 1. Create GitHub repository
# Visit https://github.com/new
# Name: isnbiz-website (or your preferred name)

# 2. Connect local repo to GitHub
cd /mnt/d/workspace/ISNBIZ_Files  # or D:\workspace\ISNBIZ_Files
git remote add origin https://github.com/YOUR_USERNAME/isnbiz-website.git
git push -u origin main

# 3. Connect Netlify to GitHub
# Visit https://app.netlify.com/
# Click "Add new site" > "Import an existing project"
# Choose "GitHub" and select your repository
# Build settings:
#   - Build command: (leave empty for static site)
#   - Publish directory: . (root)
# Click "Deploy site"
```

**Daily workflow (after setup):**
```bash
# Make changes to your code
# Test locally: start index.html

# Commit and push
git add .
git commit -m "feat: Update homepage content"
git push origin main

# Netlify will automatically deploy (takes 30-60 seconds)
# Visit your site: https://YOUR_SITE_NAME.netlify.app
```

### Method 2: Netlify CLI

**One-time setup:**
```bash
# Install Netlify CLI
npm install -g netlify-cli

# Login to Netlify
netlify login
# This will open browser for authentication
```

**Deploy:**
```bash
cd /mnt/d/workspace/ISNBIZ_Files

# Deploy to production
netlify deploy --prod

# Follow prompts:
# - Create new site or link existing
# - Set publish directory: . (current directory)
# - Confirm deployment

# You'll get a URL like: https://YOUR_SITE_NAME.netlify.app
```

**Preview deploy (test before production):**
```bash
netlify deploy  # Without --prod flag
# Creates preview URL for testing
```

### Method 3: Netlify Drag-and-Drop

**Steps:**
1. Visit https://app.netlify.com/
2. Sign in or create account
3. Drag the `ISNBIZ_Files` folder to the drop zone
4. Wait for deployment (30-60 seconds)
5. Site is live at: https://YOUR_SITE_NAME.netlify.app

**Limitations:**
- No auto-deploy (must manually upload for each change)
- Suitable for quick tests or one-time deployments

### Custom Domain Configuration (Netlify)

**After deployment:**
```bash
# 1. In Netlify dashboard, go to "Domain settings"
# 2. Click "Add custom domain"
# 3. Enter: isn.biz
# 4. Netlify will provide DNS records
# 5. Update your domain registrar DNS settings:
#    - Add CNAME record: www → YOUR_SITE_NAME.netlify.app
#    - Add A record: @ → 75.2.60.5 (Netlify's IP)
# 6. Wait for DNS propagation (up to 48 hours)
# 7. SSL will be automatically provisioned
```

### Netlify Form Setup

**Current state:** Form shows JavaScript alert (placeholder)

**To enable Netlify Forms:**
```html
<!-- Update contact.html form tag -->
<form id="contactForm" 
      name="contact" 
      method="POST" 
      data-netlify="true" 
      netlify-honeypot="bot-field">
    
    <!-- Add hidden input -->
    <input type="hidden" name="form-name" value="contact" />
    
    <!-- Add honeypot (spam protection) -->
    <div style="display: none;">
        <label>Don't fill this out: <input name="bot-field" /></label>
    </div>
    
    <!-- Rest of form fields... -->
</form>
```

**After enabling:**
- Submissions visible in Netlify dashboard
- Email notifications configurable
- No backend code needed

## Alternative: Kusanagi Deployment

### Why Kusanagi?
- **Match HROC infrastructure** - Similar to HROC website setup
- **Full control** - Self-hosted on your server
- **WordPress compatible** - Can run WP theme if needed

### Kusanagi Prerequisites
- Kusanagi server configured (10.0.0.X on your network)
- SSH access configured
- Web directory path known

### Deploy to Kusanagi

**Using deployment script:**
```bash
# Script is provided: deploy-to-kusanagi.sh
bash deploy-to-kusanagi.sh
```

**Manual deployment:**
```bash
# 1. Get SSH credentials from 1Password
eval $(op signin)
SSH_KEY=$(op read "op://TrueNAS Infrastructure/Kusanagi SSH/private key")

# 2. Upload files via rsync
rsync -avz \
  --exclude 'venv_fal' \
  --exclude '.git' \
  --exclude 'docs' \
  --exclude 'scripts' \
  -e "ssh -i <(echo \"$SSH_KEY\")" \
  ./ user@kusanagi-server:/path/to/webroot/isn.biz/

# 3. Set permissions on server
ssh -i <(echo "$SSH_KEY") user@kusanagi-server \
  "cd /path/to/webroot/isn.biz && chown -R nginx:nginx . && chmod -R 755 ."

# 4. Test: Visit http://kusanagi-server/isn.biz or http://isn.biz
```

**Configuration:**
- Update `deploy-to-kusanagi.sh` with correct paths and credentials
- Configure SSL certificate (Let's Encrypt)
- Set up DNS to point to Kusanagi server

## Alternative: GitHub Pages

### Why GitHub Pages?
- **Free hosting** - For public repositories
- **GitHub integration** - Built into GitHub
- **Simple setup** - Enable in repo settings

### Limitations
- Less feature-rich than Netlify
- No built-in form handling
- Slower deployment than Netlify

### Deploy to GitHub Pages

```bash
# 1. Push code to GitHub
git remote add origin https://github.com/YOUR_USERNAME/isnbiz-website.git
git push -u origin main

# 2. Enable GitHub Pages
# Go to repo settings > Pages
# Source: Deploy from branch
# Branch: main
# Folder: / (root)
# Save

# 3. Wait 1-2 minutes
# Site will be live at: https://YOUR_USERNAME.github.io/isnbiz-website/

# 4. Custom domain (optional)
# In Pages settings, add custom domain: isn.biz
# Update DNS at domain registrar:
#   CNAME: www → YOUR_USERNAME.github.io
#   A records: @ → GitHub Pages IPs
```

## Alternative: Traditional Web Hosting (cPanel/FTP)

### Steps:
```bash
# 1. Get hosting credentials from provider
# 2. Connect via FTP client (FileZilla, WinSCP, etc.)
#    - Host: ftp.isn.biz (or provided FTP server)
#    - Username: your_username
#    - Password: your_password
#    - Port: 21 (FTP) or 22 (SFTP)

# 3. Upload files
#    - Upload all files from ISNBIZ_Files/
#    - Exclude: venv_fal/, .git/, docs/, scripts/
#    - Root files: index.html, about.html, etc.

# 4. Set permissions (if needed)
#    - Files: 644
#    - Directories: 755

# 5. Configure SSL
#    - Use cPanel to enable Let's Encrypt SSL
#    - Or upload SSL certificate if provided

# 6. Test site
#    - Visit https://isn.biz
```

## Pre-Deployment Checklist

**CRITICAL (Must Complete):**
- [ ] Update contact email (remove placeholder)
- [ ] Add real company metrics in hero stats
- [ ] Replace portfolio examples with actual projects
- [ ] Set up form backend (Netlify Forms, Formspree, or custom)
- [ ] Configure SSL certificate (HTTPS)
- [ ] Test on multiple devices and browsers

**IMPORTANT:**
- [ ] Add Google Analytics tracking
- [ ] Set up Google Search Console
- [ ] Configure form spam protection
- [ ] Optimize images (WebP, compression)
- [ ] Test all pages and links
- [ ] Verify S3 assets load correctly
- [ ] Update meta descriptions
- [ ] Add favicon

**ENHANCED (Post-Launch):**
- [ ] Create privacy policy page
- [ ] Create terms of service page
- [ ] Add team photos and bios
- [ ] Update LinkedIn with new URL
- [ ] Update CrunchBase profile
- [ ] Update AngelList/Wellfound

**Full checklist:** See `DEPLOYMENT_CHECKLIST.md` in project root

## Post-Deployment Verification

### Immediate Checks (within 5 minutes)
```bash
- [ ] Visit live URL and verify homepage loads
- [ ] Test navigation (all menu links work)
- [ ] Test all pages load (about, services, portfolio, investors, contact)
- [ ] Check mobile version (use Chrome DevTools device toolbar)
- [ ] Verify images load (check S3 URLs)
- [ ] Check browser console for errors (F12)
- [ ] Test form submission
- [ ] Verify HTTPS/SSL certificate
```

### Within 24 Hours
```bash
- [ ] Test on real mobile devices (iOS, Android)
- [ ] Test in multiple browsers (Chrome, Firefox, Edge, Safari)
- [ ] Run Lighthouse audit (aim for 90+ all categories)
- [ ] Check Google Search Console for indexing
- [ ] Verify DNS propagation (if using custom domain)
- [ ] Test from different locations/networks
- [ ] Monitor form submissions (if using Netlify Forms)
```

### Within 1 Week
```bash
- [ ] Check Google Analytics for traffic
- [ ] Monitor server/CDN performance
- [ ] Review any user feedback
- [ ] Check for broken links (dead link checker)
- [ ] Verify email notifications working
- [ ] Test backup/restore process
```

## Monitoring and Maintenance

### Netlify Dashboard
- **Analytics:** Track visitors, bandwidth usage
- **Forms:** View form submissions
- **Deploy log:** Check deployment history
- **Functions:** (if using serverless functions)

### Google Analytics 4
```html
<!-- Add to <head> section of all pages -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

### Google Search Console
1. Visit https://search.google.com/search-console
2. Add property: isn.biz
3. Verify ownership (HTML file or DNS record)
4. Submit sitemap.xml (if created)
5. Monitor indexing and search performance

### Uptime Monitoring (Optional)
- **UptimeRobot** (free): https://uptimerobot.com/
- **Pingdom** (free tier): https://www.pingdom.com/
- **StatusCake** (free tier): https://www.statuscake.com/

## Rollback Procedure

### If deployment fails or issues found:

**Netlify:**
```bash
# Option 1: Rollback in dashboard
# Go to Deploys > Click on previous successful deploy > Publish deploy

# Option 2: Rollback via CLI
netlify rollback

# Option 3: Git revert and redeploy
git revert HEAD
git push origin main
```

**Kusanagi/Traditional:**
```bash
# Restore from backup
# (Ensure you have backups before deploying!)
```

## Troubleshooting

### "Site not loading"
```bash
# Check:
1. DNS propagation (use https://dnschecker.org/)
2. Deployment status (Netlify dashboard or logs)
3. SSL certificate (should auto-provision)
4. Firewall rules (if self-hosted)
```

### "Images not showing"
```bash
# Check:
1. S3 URLs are correct and accessible
2. S3 bucket permissions (public read)
3. CORS settings on S3 bucket
4. Browser console for 404 errors
```

### "Form not working"
```bash
# Check:
1. Netlify form is properly configured (data-netlify="true")
2. Hidden form-name input is present
3. JavaScript isn't interfering (check console)
4. Check Netlify dashboard for submissions
```

### "SSL certificate error"
```bash
# Netlify: Should auto-provision, wait 10 minutes
# If still failing:
1. Check DNS is pointing to Netlify
2. Try manual SSL provision in Netlify dashboard
3. Contact Netlify support
```

## Deployment Comparison

| Feature | Netlify | Kusanagi | GitHub Pages | Traditional |
|---------|---------|----------|--------------|-------------|
| **Ease of Setup** | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Auto-Deploy** | ✅ Yes | ❌ No | ✅ Yes | ❌ No |
| **Free SSL** | ✅ Yes | ⚙️ Manual | ✅ Yes | ⚙️ Manual |
| **Form Handling** | ✅ Built-in | ⚙️ Custom | ❌ No | ⚙️ Custom |
| **CDN** | ✅ Yes | ❌ No | ✅ Yes | Depends |
| **Cost** | Free | Server cost | Free | $5-20/mo |
| **Custom Domain** | ✅ Easy | ✅ Easy | ✅ Easy | ✅ Easy |
| **Control** | Medium | Full | Low | Full |

**Recommendation:** **Netlify** for ease of use and features. Use Kusanagi only if you need full control or want to match HROC infrastructure.

## Support Resources

### Netlify
- **Docs:** https://docs.netlify.com/
- **Community:** https://answers.netlify.com/
- **Support:** support@netlify.com

### Kusanagi
- **Docs:** See `/mnt/d/workspace/.serena/WEBSITES.md`
- **HROC Reference:** `/mnt/d/workspace/HROC_Files/CLAUDE.md`

### DNS/Domain
- **DNS Checker:** https://dnschecker.org/
- **SSL Checker:** https://www.sslshopper.com/ssl-checker.html

## Next Steps After Deployment

1. **Monitor:** Check analytics and uptime
2. **Iterate:** Based on user feedback and data
3. **Optimize:** Improve performance, SEO
4. **Maintain:** Regular updates, security patches
5. **Scale:** Add features as needed (blog, case studies, etc.)

---

**Ready to deploy?** Start with Netlify Method 1 (Git-based) for the smoothest experience.
