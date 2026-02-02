# Where to Find Things - Post-Cleanup Guide

**Updated:** 2026-02-02
**Purpose:** Quick lookup for archived files after cleanup

---

## Looking for Something?

### "Where are the deployment status reports?"
→ `Archive/2026-02-02-cleanup/deployment-reports/`

Files include:
- SSL_SUCCESS_REPORT.md
- SSL_VERIFICATION_REPORT.md
- SITE_VERIFICATION_REPORT.md
- MONITORING_STATUS_SUMMARY.txt
- DEPLOYMENT_ASSET_AUDIT_2026_02_02.md
- TASK_COMPLETION_SUMMARY.txt
- WEBP_CONVERSION_COMPLETION_REPORT.md

### "Where are the old quick start guides?"
→ `Archive/2026-02-02-cleanup/documentation-old/`

Files include:
- QUICK_START_GUIDE.md
- QUICK_START.md
- START_HERE.md
- MANUAL_DEPLOYMENT_GUIDE.md
- NETLIFY_DEPLOYMENT_STEPS.md

### "Where are the screenshot comparisons?"
→ `Archive/2026-02-02-cleanup/comparison-files/`

Directories:
- screenshots/ - Site screenshots
- screenshots_comparison/ - Before/after
- truenas-current/ - TrueNAS deployment

### "Where are the test/preview files?"
→ `Archive/2026-02-02-cleanup/test-files/`

Files include:
- preview_founder_images.html
- preview_hero_bg.html
- preview_project_images.html
- slider-gallery.html
- enhanced-animations.css (experimental)
- enhanced-interactions.js (experimental)

### "Where are the individual project pages?"
→ `Archive/2026-02-02-cleanup/project-pages/`

Files include:
- project-opportunity-bot.html
- project-spiritatlas.html
- project-truenas-infrastructure.html
- project-bin-intelligence.html
- project-comfyui-automation.html
- And 6 more...

### "Where are the asset generation docs?"
→ `Archive/2026-02-02-cleanup/documentation-old/`

Files include:
- PREMIUM_ASSET_LIBRARY_COMPLETE.md
- PREMIUM_ASSETS_INDEX.md
- START_HERE_AI_ASSETS.md
- PROJECT_ICONS_COMPLETE.md
- PORTFOLIO_IMAGES_COMPLETE.md

### "Where are the founder photo docs?"
→ `Archive/2026-02-02-cleanup/documentation-old/`

Files include:
- FOUNDER_PHOTO_ENHANCEMENT_SUMMARY.md
- README_FOUNDER_ENHANCEMENT.md

### "Where are the investor page planning docs?"
→ `Archive/2026-02-02-cleanup/documentation-old/`

Files include:
- INVESTOR_PAGE_BLUEPRINT.md (86KB - comprehensive)
- INVESTOR_PAGE_ANALYSIS_SUMMARY.md
- INVESTOR_PAGE_QUICK_WINS.md

### "Where are the portfolio planning docs?"
→ `Archive/2026-02-02-cleanup/documentation-old/`

Files include:
- PORTFOLIO_PAGE_SUMMARY.md
- PORTFOLIO_QUICK_START.md

### "Where are the session status reports?"
→ `Archive/2026-02-02-cleanup/deployment-reports/`

Files include:
- FINAL_STATUS_2026-02-01.md
- SESSION_STATUS_2026-02-01.md
- TASK_5_COMPLETE.md

### "Where are the slider/carousel docs?"
→ `Archive/2026-02-02-cleanup/documentation-old/`

Files include:
- SLIDER_DELIVERABLES.md
- SLIDER_QUICK_REFERENCE.md
- SLIDER_UPDATE_SUMMARY.md

---

## Current Production Files (Root Directory)

### Main Pages
- **index.html** - Homepage
- **about.html** - About ISN.BIZ
- **services.html** - Services offered
- **portfolio.html** - Portfolio showcase
- **portfolio-grid.html** - Portfolio grid view
- **investors.html** - Investor information
- **contact.html** - Contact form

### Team Pages
- **alicia.html** - Alicia's profile
- **bri.html** - Bri's profile
- **jonathan.html** - Jonathan's profile
- **lilly.html** - Lilly's profile

### Core Assets
- **styles.css** - Main stylesheet (43KB)
- **script.js** - JavaScript functionality (687B)
- **logo.png** - Company logo (11KB)

### Documentation (Root)
- **CLAUDE.md** - Claude AI context (primary reference)
- **README.md** - Project overview
- **DEPLOY_TO_NETLIFY.md** - Deployment guide
- **DEPLOYMENT_CHECKLIST.md** - Pre-launch checklist

### Deployment
- **DEPLOY_NOW.sh** - Automated deployment script

### Configuration
- **package.json** - NPM configuration
- **package-lock.json** - NPM dependencies
- **.env** - Environment variables
- **.gitignore** - Git ignore rules

---

## Directory Reference

### assets/
**Location:** Root
**Size:** 185MB
**Contents:** Images, icons, backgrounds, generated assets

**Key subdirectories:**
- backgrounds/ - Hero backgrounds
- founders/ - Team photos
- generated/ - AI-generated assets
- premium_v3/ - Premium asset library
- projects/ - Project images

### docs/
**Location:** Root
**Size:** 1.2MB
**Contents:** Current documentation

**Check for:**
- Design guides
- Asset catalogs
- Technical specifications
- Deployment guides

### scripts/
**Location:** Root
**Size:** 386KB
**Contents:** Build and deployment scripts

**Key files:**
- Photo generation scripts
- Asset upload scripts
- Deployment automation

### Archive/
**Location:** Root
**Size:** 108MB
**Contents:** Historical files organized by date

**Subdirectories:**
- 2026-02-02-cleanup/ - This cleanup
- scripts-used/ - Old scripts
- temp-files/ - Temporary files

---

## Search Commands

### Find Any Archived File
```bash
cd /d/workspace/ISNBIZ_Files/Archive/2026-02-02-cleanup
find . -name "FILENAME" -type f
```

### Search by Keyword
```bash
cd /d/workspace/ISNBIZ_Files/Archive/2026-02-02-cleanup
grep -r "KEYWORD" --include="*.md"
```

### List All Markdown Files
```bash
cd /d/workspace/ISNBIZ_Files/Archive/2026-02-02-cleanup
find . -name "*.md" -type f
```

### List Files by Size
```bash
cd /d/workspace/ISNBIZ_Files/Archive/2026-02-02-cleanup
find . -type f -exec ls -lh {} \; | sort -k5 -hr | head -20
```

---

## Restoration Quick Commands

### Restore a Single File
```bash
cp Archive/2026-02-02-cleanup/path/to/file ./
```

### Restore a Category
```bash
cp -r Archive/2026-02-02-cleanup/deployment-reports/* ./docs/
```

### Restore for Reference (Don't Copy)
```bash
# Just read from archive
cat Archive/2026-02-02-cleanup/documentation-old/QUICK_START_GUIDE.md
```

---

## Most Commonly Needed Archived Files

### Deployment Reference
1. **SSL_SUCCESS_REPORT.md** - SSL certificate setup
2. **DEPLOYMENT_ASSET_AUDIT_2026_02_02.md** - Asset inventory
3. **SITE_VERIFICATION_REPORT.md** - Site verification

### Development Reference
1. **INVESTOR_PAGE_BLUEPRINT.md** - Investor page design (86KB)
2. **PREMIUM_ASSETS_INDEX.md** - Asset catalog
3. **PROJECT_SUMMARY.md** - Project overview

### Quick Guides
1. **QUICK_START_GUIDE.md** - Getting started
2. **MANUAL_DEPLOYMENT_GUIDE.md** - Manual deploy steps
3. **QUICK_REFERENCE.md** - Quick reference

---

## Archive Policy

### Keep For
- **1 year minimum** - All archived files
- **Indefinitely** - Deployment reports, major milestones
- **Review annually** - Test files, experiments

### Can Delete After Review
- Duplicate documentation
- Temporary test files
- Expired session reports
- Obsolete comparisons

### Never Delete
- Deployment success reports
- SSL certificates documentation
- Production configuration backups

---

## Tips

### Before Restoring
1. Check if information is in current docs first
2. CLAUDE.md is the primary reference
3. README.md has essential info
4. docs/ has current documentation

### When Searching Archives
1. Use meaningful keywords
2. Check multiple locations
3. Read file timestamps
4. Compare with current files

### If You Can't Find It
1. Check CLEANUP_REPORT.md for full file list
2. Search by file type (.md, .html, .json)
3. Check git history: `git log --all --full-history -- "**/FILENAME"`
4. Ask Claude to search archive

---

**Last Updated:** 2026-02-02
**Created by:** Claude AI
**Maintained by:** jdmal + Claude AI

**Quick Access:** See CLEANUP_REPORT.md for complete details
