# Codebase Structure

## Directory Tree

```
ISNBIZ_Files/
├── .git/                          # Git repository (separate from workspace)
├── .serena/                       # Serena AI context (project-specific)
│   ├── project.yml                # Serena configuration
│   └── .gitignore                 # Serena-specific gitignore
│
├── Main Website Files (Production)
│   ├── index.html                 # Homepage
│   ├── about.html                 # About page
│   ├── services.html              # Services/Solutions page
│   ├── portfolio.html             # Portfolio/Case studies page
│   ├── investors.html             # Investor information page
│   ├── contact.html               # Contact form page
│   ├── styles.css                 # Main stylesheet (23KB)
│   ├── script.js                  # Main JavaScript (687B)
│   ├── slider-styles.css          # Gallery/slider styles
│   ├── slider-init.js             # Gallery/slider initialization
│   └── .gitignore                 # Git ignore patterns
│
├── Brand Assets (Local - mostly deprecated, using S3)
│   ├── logo.png                   # ISN.BIZ logo
│   └── logo-pallete.zip           # Logo variants archive
│
├── Documentation (40+ files)
│   ├── README.md                  # Project overview
│   ├── CLAUDE.md                  # AI assistant context (PROJECT-SPECIFIC)
│   ├── START_HERE.md              # Getting started guide
│   ├── QUICK_START.md             # Quick start instructions
│   ├── GET_STARTED.md             # Detailed getting started
│   ├── PROJECT_SUMMARY.md         # Project summary
│   ├── PROJECT_STRUCTURE.md       # Project structure overview
│   │
│   ├── Deployment Guides
│   │   ├── DEPLOYMENT_CHECKLIST.md        # Pre-launch checklist
│   │   ├── DEPLOYMENT_INSTRUCTIONS.md     # General deployment
│   │   ├── DEPLOY_TO_NETLIFY.md           # Netlify-specific guide
│   │   ├── MANUAL_DEPLOYMENT_GUIDE.md     # Manual deployment steps
│   │   ├── NETLIFY_DEPLOYMENT_STEPS.md    # Step-by-step Netlify
│   │   ├── deploy-to-kusanagi.sh          # Kusanagi deployment script
│   │   ├── deploy-from-local.sh           # Local deployment script
│   │   └── quick_start.sh                 # Quick start automation
│   │
│   ├── Design & Brand Guides
│   │   ├── BRAND_ASSETS_GUIDE.md          # Brand usage guide
│   │   ├── VISUAL_PREVIEW_GUIDE.md        # Visual design preview
│   │   ├── WEBSITE_PREVIEW_GUIDE.md       # Website preview
│   │   ├── ASSET_CATALOG.md               # Complete asset listing
│   │   ├── ASSET_USAGE_GUIDE.md           # How to use assets
│   │   └── ASSET_GENERATION_QUICK_START.md # Asset creation guide
│   │
│   ├── Asset Generation & AI
│   │   ├── AI_ASSET_GENERATION_SUMMARY.md      # AI asset overview
│   │   ├── AI_IMAGE_SERVICES_RECOMMENDATIONS.md # AI service comparison
│   │   ├── COMPLETE_ASSET_GENERATION_PLAN.md   # Full asset strategy
│   │   ├── PREMIUM_ASSETS_INDEX.md             # Premium assets list
│   │   ├── PREMIUM_ASSETS_PROJECT_SUMMARY.md   # Premium project summary
│   │   ├── PREMIUM_ASSETS_README.md            # Premium assets guide
│   │   ├── PREMIUM_ASSET_LIBRARY_COMPLETE.md   # Complete library
│   │   ├── START_HERE_AI_ASSETS.md             # AI assets start
│   │   └── START_HERE_PREMIUM_ASSETS.md        # Premium assets start
│   │
│   ├── Page-Specific Documentation
│   │   ├── PORTFOLIO_PAGE_SUMMARY.md           # Portfolio page details
│   │   ├── PORTFOLIO_QUICK_START.md            # Portfolio quickstart
│   │   ├── PORTFOLIO_IMAGES_COMPLETE.md        # Portfolio image guide
│   │   ├── INVESTOR_PAGE_ANALYSIS_SUMMARY.md   # Investor page analysis
│   │   ├── INVESTOR_PAGE_BLUEPRINT.md          # Investor page design
│   │   └── INVESTOR_PAGE_QUICK_WINS.md         # Investor page improvements
│   │
│   ├── Quality & Verification
│   │   ├── WCAG_VALIDATION_FINAL.md            # Accessibility audit
│   │   ├── VERIFICATION_CHECKLIST.md           # Verification steps
│   │   ├── MONITORING_VERIFICATION_INDEX.md    # Monitoring guide
│   │   ├── TESTING_COMPLETE_SUMMARY.md         # Testing summary
│   │   ├── ENHANCEMENT_CHECKLIST.md            # Enhancement ideas
│   │   └── verify_setup.py                     # Setup verification script
│   │
│   ├── Photo Enhancement
│   │   ├── FOUNDER_PHOTO_ENHANCEMENT_SUMMARY.md # Photo enhancement results
│   │   ├── INDEX_FOUNDER_PHOTOS.md              # Founder photos index
│   │   └── README_FOUNDER_ENHANCEMENT.md        # Enhancement readme
│   │
│   ├── Status Reports
│   │   ├── DELIVERY_COMPLETE.txt                # Completion report
│   │   ├── FINAL_STATUS_2026-02-01.md           # Final status
│   │   ├── SESSION_STATUS_2026-02-01.md         # Session status
│   │   ├── system_status_report.md              # System status
│   │   ├── SYSTEM_STATUS_SUMMARY.txt            # Status summary
│   │   └── WORDPRESS_THEME_READY.md             # WP theme status
│   │
│   ├── Quick Reference
│   │   ├── QUICK_REFERENCE.md                   # Quick ref guide
│   │   ├── QUICK_START_GUIDE.md                 # Quick start guide
│   │   └── FAL_MODEL_TESTING_QUICKSTART.md      # FAL model testing
│   │
│   └── Miscellaneous
│       ├── COMPLETE_WEBSITE_SUMMARY.md          # Complete site summary
│       ├── b64data.txt                          # Base64 data
│       ├── s3_bucket_name.txt                   # S3 bucket reference
│       └── requirements_assets.txt              # Python requirements
│
├── Python Scripts (Asset Generation)
│   ├── scripts/                                 # Script directory
│   │   ├── README.md                            # Scripts readme
│   │   ├── USAGE_GUIDE.md                       # Usage instructions
│   │   ├── PROJECT_SUMMARY.md                   # Scripts summary
│   │   ├── QUICK_START.md                       # Quick start
│   │   ├── ASSET_GENERATION_QUICKSTART.md       # Asset gen quickstart
│   │   ├── ASSET_GENERATOR_README.md            # Asset generator guide
│   │   ├── PHOTO_ENHANCEMENT_README.md          # Photo enhancement guide
│   │   ├── FOUNDER_PHOTO_ENHANCEMENT_INSTRUCTIONS.md # Enhancement instructions
│   │   ├── SOURCE_PHOTOS_REFERENCE.md           # Source photos ref
│   │   │
│   │   ├── Asset Generation Scripts
│   │   │   ├── generate_isnbiz_assets.py        # ISN.BIZ asset generator
│   │   │   ├── generate_website_assets.py       # Website assets
│   │   │   ├── generate_ai_assets.py            # AI-powered generation
│   │   │   └── generate_assets.sh               # Shell script wrapper
│   │   │
│   │   ├── Photo Enhancement Scripts
│   │   │   ├── enhance_founder_photos.py        # Photo enhancement
│   │   │   ├── enhance_founder_photos_base64.py # Base64 version
│   │   │   ├── enhance_founder_photos_gpt15.py  # GPT-1.5 version
│   │   │   ├── enhance_founder_photos_headshot.py # Headshot version
│   │   │   └── run_photo_enhancement.sh         # Enhancement runner
│   │   │
│   │   ├── FAL Testing Scripts
│   │   │   ├── test_fal_models.py               # FAL model testing
│   │   │   ├── test_fal_models_v2.py            # FAL testing v2
│   │   │   ├── quick_test_fal.py                # Quick FAL test
│   │   │   └── run_fal_tests.sh                 # Test runner
│   │   │
│   │   ├── Setup Scripts
│   │   │   ├── setup_and_generate.sh            # Setup & generate
│   │   │   └── setup_and_run_generator.sh       # Setup & run
│   │   │
│   │   ├── Utility Files
│   │   │   ├── prompts_export.json              # AI prompts export
│   │   │   ├── prompt_viewer.html               # Prompt viewer
│   │   │   ├── requirements.txt                 # Python requirements
│   │   │   └── requirements-assets.txt          # Asset requirements
│   │   │
│   │   └── Quick Start Reference
│   │       ├── QUICK_START.txt                  # Quick start text
│   │       └── QUICK_START_REFERENCE.md         # Quick start ref
│   │
│   ├── Root-level Python Scripts
│   │   ├── generate_premium_assets.py           # Premium asset generator
│   │   ├── generate_and_upload_premium_assets.sh # Generate & upload
│   │   ├── upload_assets_to_s3.py               # S3 uploader
│   │   ├── verify_s3_urls.py                    # S3 URL verification
│   │   ├── update_html_with_s3.py               # HTML S3 updater
│   │   ├── verify_setup.py                      # Setup verifier
│   │   ├── generate_assets.py                   # Asset generator
│   │   ├── generate_v2_assets.py                # V2 asset generator
│   │   ├── generate_v3_assets.py                # V3 asset generator (latest)
│   │   ├── generate_hero_backgrounds.py         # Hero background gen
│   │   ├── generate_portfolio_images.py         # Portfolio image gen
│   │   ├── generate_images_sync.py              # Sync image generation
│   │   ├── generate_test_images.py              # Test image generation
│   │   ├── create_responsive_variants.py        # Responsive variants
│   │   ├── build_gen_script.py                  # Build generator
│   │   ├── write_gen.py                         # Write generator
│   │   ├── process_logos.py                     # Logo processor
│   │   └── process_logos_v3.py                  # Logo processor v3
│   │
│   └── requirements_assets.txt                  # Python dependencies
│
├── Python Virtual Environment
│   └── venv_fal/                                # Python 3.12 venv
│       ├── bin/                                 # Executables (python, pip)
│       ├── lib/                                 # Python libraries
│       ├── lib64/                               # 64-bit libraries
│       └── __pycache__/                         # Python cache
│
├── WordPress Theme (Optional)
│   ├── wp-theme-isnbiz-2026/                    # WordPress theme directory
│   │   ├── style.css                            # Theme stylesheet
│   │   ├── index.php                            # Main template
│   │   ├── functions.php                        # Theme functions
│   │   ├── header.php                           # Header template
│   │   ├── footer.php                           # Footer template
│   │   └── ... (other WP theme files)
│   │
│   └── wp-theme-isnbiz-2026.tar.gz              # Theme archive
│
├── Additional Directories
│   ├── assets/                                  # Local assets (if any)
│   ├── site-verification/                       # Site verification files
│   ├── 1/                                       # Unknown/temp directory
│   └── __pycache__/                             # Python cache (root level)
│
└── Git Configuration
    └── .gitignore                               # Git ignore patterns
```

## Key File Purposes

### Production Website Files
- **index.html** (30KB) - Homepage, main entry point
- **about.html** - Company information, history, credentials
- **services.html** - Solutions portfolio (AI, Cloud, Enterprise, Data)
- **portfolio.html** - Case studies, project showcase
- **investors.html** - Investment opportunities, pitch
- **contact.html** - Contact form, company info
- **styles.css** (23KB) - Main stylesheet, Neo-Technical Brutalism design
- **script.js** (687B) - Minimal JS for interactivity

### Asset Strategy
- **S3 Primary:** All production assets on S3 (isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com)
- **Local Minimal:** Only essential local files, most assets reference S3 URLs
- **WebP Format:** All images optimized as WebP

### Python Tooling
- **Purpose:** Asset generation, S3 uploads, image processing
- **Not Required:** For website deployment (static HTML/CSS/JS)
- **venv_fal:** Python 3.12 virtual environment
- **Dependencies:** requests, Pillow, boto3

### Documentation Organization
- **40+ markdown files** - Comprehensive guides for all aspects
- **Deployment guides** - Multiple deployment options covered
- **Asset guides** - Complete asset management documentation
- **Quality guides** - WCAG compliance, testing, verification

### Ignore Patterns (.gitignore)
```gitignore
# Python
venv_fal/
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
*.egg-info/

# Environment
.env
.env.local
*.local

# OS
.DS_Store
Thumbs.db
desktop.ini

# Editors
.vscode/
.idea/
*.swp
*.swo
*~

# Temporary
*.tmp
*.bak
*.log
temp/
tmp/

# Build
dist/
build/
*.zip (except specific archives)

# Assets (local, using S3)
logo-pallete/ (if not needed)
```

## Important Paths

### For Reading/Editing Code
```
HTML:  D:\workspace\ISNBIZ_Files\*.html
CSS:   D:\workspace\ISNBIZ_Files\styles.css
JS:    D:\workspace\ISNBIZ_Files\script.js
```

### For Documentation
```
Main:  D:\workspace\ISNBIZ_Files\README.md
AI:    D:\workspace\ISNBIZ_Files\CLAUDE.md
Guide: D:\workspace\ISNBIZ_Files\GET_STARTED.md
```

### For Deployment
```
Deploy:  D:\workspace\ISNBIZ_Files\DEPLOY_TO_NETLIFY.md
Check:   D:\workspace\ISNBIZ_Files\DEPLOYMENT_CHECKLIST.md
Script:  D:\workspace\ISNBIZ_Files\deploy-to-kusanagi.sh
```

### For Assets (S3)
```
S3 Base: https://isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com/premium_v3/
Logos:   /logos/
OG:      /og/
```

## Navigation Tips

### Find specific documentation:
```bash
# Quick starts
GET_STARTED.md, QUICK_START.md, START_HERE.md

# Deployment
DEPLOY_TO_NETLIFY.md, DEPLOYMENT_CHECKLIST.md

# Assets
BRAND_ASSETS_GUIDE.md, ASSET_CATALOG.md

# Status
FINAL_STATUS_2026-02-01.md, DELIVERY_COMPLETE.txt
```

### Find specific functionality:
```bash
# Form handling: script.js (lines 1-17)
# Navigation: index.html (lines 28-47), script.js (smooth scrolling)
# Styles: styles.css (organized by section)
# Colors: styles.css (lines 18-29, :root variables)
```

## Project Context Files

### For Claude/Serena
- **CLAUDE.md** - Project-specific context (THIS PROJECT ONLY)
- **.serena/** - Serena AI context directory (THIS PROJECT ONLY)
- **Workspace CLAUDE.md** - /mnt/d/workspace/CLAUDE.md (WORKSPACE-LEVEL)

**Important:** This project's CLAUDE.md is separate from workspace CLAUDE.md.

## Build/Compile Process

**There is NO build process!**

This is a static site:
- No compilation needed
- No bundling required
- No transpiling necessary
- Direct deployment of source files

Just upload HTML/CSS/JS files to hosting platform.

## Dependencies

### Production (None!)
- **No NPM packages**
- **No JavaScript frameworks**
- **No CSS preprocessors**
- **No build tools**

### Development (Optional)
- **Python 3.12** - Asset generation only
- **boto3** - S3 uploads
- **Pillow** - Image processing
- **requests** - HTTP requests

## Related Projects

- **HROC Website** - Similar static site at /mnt/d/workspace/HROC_Files
- **Opportunity Bot** - Separate project at /mnt/d/workspace/opportunity-research-bot
- **Workspace** - Container directory at /mnt/d/workspace

Each project has its own git repo and .serena context.
