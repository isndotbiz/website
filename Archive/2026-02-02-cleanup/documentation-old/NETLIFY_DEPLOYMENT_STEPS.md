# Deploy isn.biz to Netlify - Quick Guide

## 🚀 DEPLOY IN 2 MINUTES:

### **Step 1: Go to Netlify**
Visit: **https://app.netlify.com/**
- Sign in (or create free account)

### **Step 2: Import from GitHub**
1. Click **"Add new site"**
2. Select **"Import an existing project"**
3. Choose **"Deploy with GitHub"**
4. Authorize Netlify to access your GitHub
5. Select repository: **`isndotbiz/website`**

### **Step 3: Configure Build Settings**
**Leave everything as default:**
- Branch: `main`
- Build command: (leave empty - static HTML)
- Publish directory: `/` (root)
- Click **"Deploy site"**

### **Step 4: Wait 30 Seconds**
Netlify will:
- Clone your repo
- Deploy all files
- Generate SSL certificate
- Give you live URL

**You'll get:** `https://random-name-123.netlify.app`

### **Step 5: Add Custom Domain**
1. Go to **Site settings** → **Domain management**
2. Click **"Add custom domain"**
3. Enter: **`isn.biz`**
4. Click **"Verify"**

### **Step 6: Configure DNS**

**At your domain registrar** (where you bought isn.biz):

**Option A: Use Netlify DNS (Recommended)**
- Point nameservers to Netlify
- Netlify handles everything automatically

**Option B: Keep Your DNS**
Add these records:
```
Type    Name    Value
A       @       75.2.60.5
CNAME   www     your-site-name.netlify.app
```

### **Step 7: SSL Auto-Configured**
Netlify automatically provides free SSL certificate.
Your site will be at: **https://isn.biz**

---

## ✅ THAT'S IT - DEPLOYED!

**Your 7-page professional website is now LIVE!**

**Pages available:**
- https://isn.biz/
- https://isn.biz/about.html
- https://isn.biz/portfolio.html
- https://isn.biz/services.html
- https://isn.biz/investors.html
- https://isn.biz/contact.html

---

## 🔄 AUTOMATIC UPDATES:

Every time you `git push` to GitHub:
- Netlify auto-detects the change
- Automatically redeploys
- Live in ~30 seconds

**Update workflow:**
```bash
cd /mnt/d/workspace/ISNBIZ_Files
# Make changes to any .html file
git add .
git commit -m "Update content"
git push
# Netlify auto-deploys!
```

---

## 💡 NETLIFY FEATURES (FREE):

✅ **Free SSL** - HTTPS automatically
✅ **Global CDN** - Fast worldwide
✅ **Form Handling** - Contact form works automatically!
✅ **Deploy Previews** - Test before going live
✅ **Instant Rollbacks** - One-click undo
✅ **Custom Domain** - isn.biz support
✅ **Analytics** - Built-in (optional paid tier)

---

## 📱 FORMS (BONUS):

Your contact form will work automatically with Netlify!

**Just add `netlify` attribute:**
```html
<form netlify>
  <!-- Your existing form fields -->
</form>
```

Form submissions appear in Netlify dashboard - no backend needed!

---

## 🎯 NEXT STEPS AFTER DEPLOYMENT:

1. **Verify site loads:** https://your-site.netlify.app
2. **Test all pages** - Click through navigation
3. **Test contact form** - Submit a test
4. **Configure custom domain** - Add isn.biz
5. **Update DNS** - Point to Netlify
6. **Wait for SSL** - ~5-15 minutes
7. **Go live!** - https://isn.biz

---

**Total deployment time: ~2 minutes**
**Your website will be LIVE!** 🎉
