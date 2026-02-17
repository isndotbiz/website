# ISNBIZ_Files Codex Handoff Script
# Generates comprehensive handoff documentation for ISN Business Intelligence website

param(
    [string]$OutputDir = "D:\workspace\ISNBIZ_Files\codex_handoff",
    [switch]$IncludeAssets = $false
)

Write-Host "ISNBIZ_Files Codex Handoff Generator" -ForegroundColor Cyan
Write-Host "====================================" -ForegroundColor Cyan
Write-Host ""

$projectRoot = "D:\workspace\ISNBIZ_Files"
$timestamp = Get-Date -Format "yyyy-MM-dd_HHmmss"
$handoffDir = "$OutputDir\$timestamp"

# Create handoff directory
New-Item -ItemType Directory -Path $handoffDir -Force | Out-Null
Write-Host "✓ Created handoff directory: $handoffDir" -ForegroundColor Green

# 1. Project Structure Documentation
Write-Host "`nGenerating project structure..." -ForegroundColor Cyan
$structure = @"
# ISNBIZ_Files Project Structure
**Generated:** $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")
**Location:** $projectRoot

## Directory Overview

``````
ISNBIZ_Files/
├── *.html                    # Individual service/product pages
├── index.html                # Main homepage
├── 404.html                  # Error page
├── assets/                   # Static assets
│   ├── css/                  # Stylesheets
│   ├── js/                   # JavaScript files
│   └── images/               # Image assets
├── spiritatlas_screenshots/  # SpiritAtlas app screenshots (NEW)
│   ├── *.png (10 files)      # Mobile app screenshots
│   ├── SCREENSHOT_DESCRIPTIONS.md
│   ├── slider_config.json
│   └── README.md
├── backups/                  # Backup files
├── .netlify/                 # Netlify deployment config
├── .git/                     # Git repository
└── Archive-*.tar.gz          # Historical archives
``````

## Key Files

### HTML Pages
"@

# List all HTML files
Get-ChildItem -Path $projectRoot -Filter "*.html" | ForEach-Object {
    $structure += "`n- **$($_.Name)** - $(
        switch -Wildcard ($_.Name) {
            'index.html' { 'Homepage' }
            '404.html' { 'Error page' }
            'about.html' { 'About ISN Business Intelligence' }
            'aurallm.html' { 'AuraLLM AI Service' }
            'bin-intelligence.html' { 'Business Intelligence & Networking' }
            'alicia.html' { 'Alicia AI Assistant' }
            'bri.html' { 'BRI Platform' }
            default { $_.BaseName -replace '-', ' ' }
        }
    )"
}

$structure | Out-File -FilePath "$handoffDir\01_PROJECT_STRUCTURE.md" -Encoding UTF8
Write-Host "✓ Generated 01_PROJECT_STRUCTURE.md" -ForegroundColor Green

# 2. Git History and Recent Changes
Write-Host "`nExtracting Git history..." -ForegroundColor Cyan
try {
    Push-Location $projectRoot
    $gitLog = & git log --oneline --graph --decorate -20 2>&1
    $gitStatus = & git status 2>&1
    $gitBranch = & git branch -a 2>&1
    Pop-Location

    $gitDoc = @"
# Git Repository Information
**Generated:** $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")

## Current Status

``````
$gitStatus
``````

## Branches

``````
$gitBranch
``````

## Recent Commits (Last 20)

``````
$gitLog
``````

## Key Commits to Review

1. Latest commit - Check for recent changes
2. Archive commits - Look for backup/archive operations
3. Feature additions - New pages or services added

"@

    $gitDoc | Out-File -FilePath "$handoffDir\02_GIT_HISTORY.md" -Encoding UTF8
    Write-Host "✓ Generated 02_GIT_HISTORY.md" -ForegroundColor Green
} catch {
    Write-Host "⚠ Git not initialized or accessible" -ForegroundColor Yellow
}

# 3. Asset Inventory
Write-Host "`nInventorying assets..." -ForegroundColor Cyan
$assetDoc = @"
# Asset Inventory
**Generated:** $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")

## Screenshots (SpiritAtlas)

### App Screenshots (10 files)
"@

if (Test-Path "$projectRoot\spiritatlas_screenshots") {
    Get-ChildItem -Path "$projectRoot\spiritatlas_screenshots" -Filter "*.png" | ForEach-Object {
        $size = [math]::Round($_.Length / 1KB, 2)
        $assetDoc += "`n- **$($_.Name)** - ${size} KB"
    }
}

$assetDoc += @"

### Documentation
- SCREENSHOT_DESCRIPTIONS.md - Full descriptions and website copy
- slider_config.json - Structured data for slider integration
- README.md - Quick reference guide

## CSS Files
"@

if (Test-Path "$projectRoot\assets\css") {
    Get-ChildItem -Path "$projectRoot\assets\css" -Filter "*.css" | ForEach-Object {
        $size = [math]::Round($_.Length / 1KB, 2)
        $assetDoc += "`n- **$($_.Name)** - ${size} KB"
    }
}

$assetDoc += "`n`n## JavaScript Files`n"

if (Test-Path "$projectRoot\assets\js") {
    Get-ChildItem -Path "$projectRoot\assets\js" -Filter "*.js" | ForEach-Object {
        $size = [math]::Round($_.Length / 1KB, 2)
        $assetDoc += "`n- **$($_.Name)** - ${size} KB"
    }
}

$assetDoc | Out-File -FilePath "$handoffDir\03_ASSET_INVENTORY.md" -Encoding UTF8
Write-Host "✓ Generated 03_ASSET_INVENTORY.md" -ForegroundColor Green

# 4. Deployment Configuration
Write-Host "`nDocumenting deployment config..." -ForegroundColor Cyan
$deployDoc = @"
# Deployment Configuration
**Generated:** $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")

## Netlify Configuration

### Directory Structure
``````
.netlify/
$(if (Test-Path "$projectRoot\.netlify") { (Get-ChildItem -Path "$projectRoot\.netlify" -Recurse | Out-String) } else { "No .netlify directory found" })
``````

### .netlifyignore
"@

if (Test-Path "$projectRoot\.netlifyignore") {
    $deployDoc += "`n``````"
    $deployDoc += "`n$(Get-Content "$projectRoot\.netlifyignore" -Raw)"
    $deployDoc += "`n``````"
}

$deployDoc += @"

## Deployment Checklist

- [ ] Verify all HTML pages are accessible
- [ ] Check asset paths (CSS, JS, images)
- [ ] Test 404 page
- [ ] Validate SpiritAtlas screenshot slider
- [ ] Check mobile responsiveness
- [ ] Test form submissions (if any)
- [ ] Verify SSL/HTTPS
- [ ] Check custom domain configuration
- [ ] Test all navigation links
- [ ] Validate meta tags and SEO

## Recommended Netlify Settings

``````toml
[build]
  publish = "."
  command = ""  # Static site, no build command

[[redirects]]
  from = "/*"
  to = "/404.html"
  status = 404

[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "DENY"
    X-XSS-Protection = "1; mode=block"
    X-Content-Type-Options = "nosniff"
    Referrer-Policy = "strict-origin-when-cross-origin"

[[headers]]
  for = "/assets/*"
  [headers.values]
    Cache-Control = "public, max-age=31536000, immutable"
``````

"@

$deployDoc | Out-File -FilePath "$handoffDir\04_DEPLOYMENT.md" -Encoding UTF8
Write-Host "✓ Generated 04_DEPLOYMENT.md" -ForegroundColor Green

# 5. Services & Products Documentation
Write-Host "`nExtracting services/products..." -ForegroundColor Cyan
$servicesDoc = @"
# Services & Products
**Generated:** $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")

## ISN Business Intelligence Offerings

### Core Services
"@

# Parse HTML files for service info
$htmlFiles = Get-ChildItem -Path $projectRoot -Filter "*.html" | Where-Object { $_.Name -ne 'index.html' -and $_.Name -ne '404.html' }

foreach ($file in $htmlFiles) {
    $servicesDoc += "`n`n### $($file.BaseName -replace '-', ' ')"
    $servicesDoc += "`n**File:** $($file.Name)"
    $servicesDoc += "`n**URL:** /$($file.Name)"

    # Try to extract title and description from HTML
    try {
        $content = Get-Content $file.FullName -Raw
        if ($content -match '<title>(.*?)</title>') {
            $servicesDoc += "`n**Title:** $($Matches[1])"
        }
        if ($content -match '<meta name="description" content="(.*?)"') {
            $servicesDoc += "`n**Description:** $($Matches[1])"
        }
    } catch {
        Write-Host "  ⚠ Could not parse $($file.Name)" -ForegroundColor Yellow
    }
}

$servicesDoc | Out-File -FilePath "$handoffDir\05_SERVICES.md" -Encoding UTF8
Write-Host "✓ Generated 05_SERVICES.md" -ForegroundColor Green

# 6. Maintenance Guide
Write-Host "`nGenerating maintenance guide..." -ForegroundColor Cyan
$maintenanceDoc = @"
# Maintenance Guide
**Generated:** $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")

## Regular Tasks

### Weekly
- [ ] Check for broken links
- [ ] Review analytics (if configured)
- [ ] Update SpiritAtlas screenshots (if app updated)
- [ ] Backup website files

### Monthly
- [ ] Review and update service descriptions
- [ ] Check for outdated content
- [ ] Update copyright year (if applicable)
- [ ] Review SEO performance
- [ ] Test all forms and interactive elements

### Quarterly
- [ ] Full content audit
- [ ] Performance optimization
- [ ] Security updates
- [ ] Competitor analysis
- [ ] Archive old backups

## Common Updates

### Adding a New Service Page

1. Create new HTML file: ``service-name.html``
2. Use existing template from another service page
3. Update navigation in all pages
4. Add to sitemap (if exists)
5. Test locally before deploying
6. Deploy via Netlify

### Updating SpiritAtlas Screenshots

1. Navigate to: ``spiritatlas_screenshots/``
2. Replace PNG files (maintain naming: 01-10)
3. Update ``SCREENSHOT_DESCRIPTIONS.md`` if needed
4. Update ``slider_config.json`` with new captions
5. Test slider functionality
6. Deploy

### CSS/JS Changes

1. Edit files in ``assets/css/`` or ``assets/js/``
2. Test locally in multiple browsers
3. Check mobile responsiveness
4. Clear Netlify cache after deployment
5. Verify changes in production

## Backup Procedure

``````powershell
# Create timestamped archive
`$timestamp = Get-Date -Format "yyyy-MM-dd_HHmmss"
`$archiveName = "ISNBIZ_Backup_`$timestamp.tar.gz"
tar -czf `$archiveName .

# Move to backups directory
Move-Item `$archiveName backups/

# Clean up old backups (keep last 5)
Get-ChildItem backups/ -Filter "*.tar.gz" |
    Sort-Object LastWriteTime -Descending |
    Select-Object -Skip 5 |
    Remove-Item
``````

## Troubleshooting

### Site Not Updating After Deploy
1. Check Netlify deploy log for errors
2. Clear Netlify cache
3. Force rebuild: ``Deploys → Trigger deploy → Clear cache and deploy site``
4. Check ``.netlifyignore`` - ensure files aren't ignored

### Broken Images
1. Check file paths are relative (``./assets/images/`` or ``assets/images/``)
2. Verify image files exist in repository
3. Check file extensions match (case-sensitive on Linux servers)
4. Test image URLs directly in browser

### Slider Not Working
1. Check ``slider_config.json`` is valid JSON
2. Verify screenshot files exist in ``spiritatlas_screenshots/``
3. Check JavaScript console for errors
4. Test Swiper.js CDN link is accessible
5. Verify initialization code is correct

## Contact Information

**Developer:** [Your Name/Company]
**Repository:** D:\workspace\ISNBIZ_Files
**Deployment:** Netlify
**Domain:** [Your Domain]

"@

$maintenanceDoc | Out-File -FilePath "$handoffDir\06_MAINTENANCE.md" -Encoding UTF8
Write-Host "✓ Generated 06_MAINTENANCE.md" -ForegroundColor Green

# 7. Create Master Index
Write-Host "`nGenerating master index..." -ForegroundColor Cyan
$indexDoc = @"
# ISNBIZ_Files Codex Handoff
**Generated:** $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")
**Project:** ISN Business Intelligence Website
**Location:** D:\workspace\ISNBIZ_Files

---

## Quick Overview

ISN Business Intelligence (ISNBIZ) is a professional services website showcasing AI solutions, business intelligence tools, and consulting services. The site is a static HTML/CSS/JS website deployed on Netlify.

### Key Components

- **Website:** Static HTML pages for each service
- **Assets:** CSS, JavaScript, images
- **SpiritAtlas Integration:** Mobile app screenshots and slider (added 2026-02-11)
- **Deployment:** Netlify (continuous deployment)
- **Version Control:** Git

---

## Documentation Files

1. **01_PROJECT_STRUCTURE.md** - Directory layout and file organization
2. **02_GIT_HISTORY.md** - Git repository information and recent commits
3. **03_ASSET_INVENTORY.md** - Complete list of assets (images, CSS, JS)
4. **04_DEPLOYMENT.md** - Netlify configuration and deployment checklist
5. **05_SERVICES.md** - List of all services/products pages
6. **06_MAINTENANCE.md** - Regular maintenance tasks and troubleshooting

---

## Quick Start for New Developer

### 1. Clone Repository
``````bash
cd D:/workspace
# Repository already exists at D:/workspace/ISNBIZ_Files
``````

### 2. Local Development
``````bash
# Serve locally (use any simple HTTP server)
python -m http.server 8000
# OR
npx serve .
# OR
php -S localhost:8000
``````

### 3. Make Changes
- Edit HTML files in root directory
- Update CSS in ``assets/css/``
- Update JS in ``assets/js/``
- Add images to ``assets/images/``

### 4. Deploy
``````bash
git add .
git commit -m "Description of changes"
git push origin main
# Netlify auto-deploys on push
``````

---

## Recent Updates (2026-02-11)

### SpiritAtlas Screenshots Added
- 10 high-quality mobile app screenshots
- Comprehensive documentation (SCREENSHOT_DESCRIPTIONS.md)
- Slider integration guide (slider_config.json)
- Ready for website slider implementation

**Location:** ``spiritatlas_screenshots/``
**Files:**
- 01_home_screen.png → 10_adama_profile.png
- SCREENSHOT_DESCRIPTIONS.md (full website copy)
- slider_config.json (structured data)
- README.md (quick reference)

---

## Technical Stack

- **Frontend:** HTML5, CSS3, JavaScript (ES6+)
- **Deployment:** Netlify
- **Version Control:** Git
- **Build:** None (static site)
- **Dependencies:** None (vanilla JS, no npm/node)

---

## Important Notes

1. **Static Site:** No build process, all files deployed as-is
2. **Netlify Auto-Deploy:** Pushes to main branch automatically deploy
3. **Asset Paths:** Use relative paths for portability
4. **Browser Support:** Modern browsers (ES6+)
5. **Mobile-First:** Responsive design tested on mobile devices

---

## Contact & Support

**Project Owner:** ISN Business Intelligence
**Repository:** D:\workspace\ISNBIZ_Files
**Generated By:** Codex Handoff Script
**Last Updated:** $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")

For questions or issues, refer to 06_MAINTENANCE.md for troubleshooting guide.

---

**Next Steps:**

1. Review all 6 documentation files
2. Verify deployment configuration (04_DEPLOYMENT.md)
3. Test SpiritAtlas slider integration
4. Set up regular backups (06_MAINTENANCE.md)
5. Update contact information in this index

---

**Handoff Complete!** 🎉
All documentation generated in: $handoffDir
"@

$indexDoc | Out-File -FilePath "$handoffDir\00_INDEX.md" -Encoding UTF8
Write-Host "✓ Generated 00_INDEX.md" -ForegroundColor Green

# Optional: Copy assets if requested
if ($IncludeAssets) {
    Write-Host "`nCopying assets..." -ForegroundColor Cyan
    $assetsDir = "$handoffDir\assets_backup"
    New-Item -ItemType Directory -Path $assetsDir -Force | Out-Null

    Copy-Item -Path "$projectRoot\assets" -Destination $assetsDir -Recurse -Force
    Copy-Item -Path "$projectRoot\spiritatlas_screenshots" -Destination $assetsDir -Recurse -Force

    Write-Host "✓ Assets copied to $assetsDir" -ForegroundColor Green
}

# Summary
Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "Codex Handoff Complete!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Documentation generated in:" -ForegroundColor White
Write-Host "  $handoffDir" -ForegroundColor Yellow
Write-Host ""
Write-Host "Files created:" -ForegroundColor White
Write-Host "  00_INDEX.md - Master overview" -ForegroundColor Yellow
Write-Host "  01_PROJECT_STRUCTURE.md" -ForegroundColor Yellow
Write-Host "  02_GIT_HISTORY.md" -ForegroundColor Yellow
Write-Host "  03_ASSET_INVENTORY.md" -ForegroundColor Yellow
Write-Host "  04_DEPLOYMENT.md" -ForegroundColor Yellow
Write-Host "  05_SERVICES.md" -ForegroundColor Yellow
Write-Host "  06_MAINTENANCE.md" -ForegroundColor Yellow
Write-Host ""
Write-Host "Start with: 00_INDEX.md" -ForegroundColor Cyan
Write-Host ""
