# CODEX CLI 5.2 HANDOFF DOCUMENT
## ISN.BIZ Website - Complete Context for Claude Sonnet 4.5 (1M Context)

**Generated:** 2026-02-04
**Purpose:** Enable Codex CLI 5.2 with xhigh reasoning to efficiently prompt Claude Sonnet 4.5 to complete the ISN.BIZ website with ALL assets, pages, and proper design

---

## CRITICAL FAL.AI CONFIGURATION - READ FIRST

### MANDATORY SETTINGS FOR ALL IMAGE GENERATION

```python
# ONLY USE THESE MODELS:
MODEL_CREATE = "fal-ai/gpt-image-1.5"      # For new image generation
MODEL_EDIT = "fal-ai/gpt-image-1.5/edit"   # For editing existing images

# ALWAYS SET QUALITY TO "low"
# NOTE: "low" is INVERTED - it's actually the BEST option
# - "low" = fast, cheap, high-quality (counter-intuitive naming)
# - "high" = slow, expensive, burns through credits
"quality": "low"  # or "image_quality": "low"
```

### WHY THIS MATTERS - PREVIOUS SESSION DISASTER

In a previous 9-hour session with 6 agents:
1. Claude used "high" quality mode on gpt-image-1.5
2. This burned through ALL fal.ai credits ($$$)
3. Claude was updating THE WRONG WEBSITE the whole time
4. Nearly lost all work due to this confusion
5. The theme and design are now correct - DO NOT LOSE IT

### CORRECT FAL.AI API CALLS

```python
# CORRECT - Image Generation
requests.post("https://fal.run/fal-ai/gpt-image-1.5",
    headers={"Authorization": f"Key {FAL_KEY}", "Content-Type": "application/json"},
    json={
        "prompt": "your prompt here",
        "image_size": "1024x1024",  # or "1536x1024" for landscape
        "quality": "low",           # ALWAYS LOW
        "num_images": 1
    }
)

# CORRECT - Image Editing
fal.submit("fal-ai/gpt-image-1.5/edit",
    arguments={
        "image_url": "https://...",
        "prompt": "edit instructions",
        "image_quality": "low"      # ALWAYS LOW
    }
)
```

### MODELS TO NEVER USE
- nano-banana-pro (expensive, unnecessary)
- flux-pro/kontext (expensive, unnecessary)
- Any model with quality="high" or quality="medium"

---

## PROJECT CURRENT STATE

### What's WORKING (Preserve This)

**Theme & Design:**
- Neo-Technical Brutalism design system
- Brand colors: Primary Blue `#1E9FF2`, Cyan `#5FDFDF`, Charcoal `#0D1117`
- Typography: Archivo Black (display), IBM Plex Sans (body), JetBrains Mono (code)
- All CSS in `styles.css` (43KB) and `enhanced-animations.css` (16KB)
- WCAG 2.1 AA accessibility compliant
- Mobile-first responsive design (4 breakpoints)

**Deployment:**
- Live at: https://isn.biz
- Server: TrueNAS at 100.83.75.4
- Path: /mnt/tank/websites/kusanagi/isn.biz/public/
- Web server: Nginx with Let's Encrypt SSL
- Pages served from TrueNAS, images from S3

**S3 CDN:**
- Bucket: `isnbiz-assets-1769962280`
- Region: `us-east-1`
- All images WebP format
- Base URL: `https://isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com/`

### What's MISSING (Needs to be Created)

1. **Portfolio still shows 8 old projects instead of 9 new ones**
   - portfolio.html has 8 projects listed
   - Should have 9 projects with their own detail pages
   - Need images for each project

2. **Founder pages exist but may lack proper images**
   - alicia.html, bri.html, jonathan.html, lilly.html exist
   - Need professional headshots and candid photos
   - Need images uploaded to S3 and referenced

3. **Project detail pages need images**
   - truenas.html, videogen.html, bin-intelligence.html, spiritatlas.html
   - comfyui.html, gedcom.html, llm-optimization.html, opportunity-bot.html
   - cli-tools.html (may be missing)
   - Need hero images and feature screenshots

4. **Card layouts need fixing**
   - Cards should ALWAYS be 3 or 4 per row
   - Everything must be centered
   - Symmetrical layouts throughout

---

## THE 9 PROJECTS (NEW)

Based on portfolio.html and project files, these are the 9 projects:

### 1. TrueNAS Infrastructure Platform
- **File:** truenas.html, project-truenas-infrastructure.html
- **Description:** Production-grade on-premise AI/ML infrastructure, 50+ containers, 247GB RAM
- **Image needed:** Hero showing server rack/infrastructure visualization
- **S3 path:** premium_v3/projects/truenas_infrastructure.webp

### 2. VideoGen YouTube Pipeline
- **File:** videogen.html, project-videogen-youtube.html
- **Description:** AI content production pipeline, $12B creator economy, 10x content velocity
- **Image needed:** Video production/editing interface
- **S3 path:** premium_v3/projects/videogen_youtube.webp

### 3. BIN Intelligence Platform
- **File:** bin-intelligence.html, project-bin-intelligence.html
- **Description:** Payment fraud intelligence, BIN enrichment, $32B security market
- **Image needed:** Payment/fraud analytics dashboard
- **S3 path:** premium_v3/projects/bin_intelligence.webp

### 4. SpiritAtlas Mobile App
- **File:** spiritatlas.html, project-spiritatlas.html
- **Description:** Privacy-first spiritual wellness app, consent-gated AI
- **Image needed:** Mobile app interface
- **S3 path:** assets/projects/spiritatlas_1.webp

### 5. ComfyUI Automation
- **File:** comfyui.html, project-comfyui-automation.html
- **Description:** Generative AI production pipeline, LoRA management, batch orchestration
- **Image needed:** ComfyUI workflow interface
- **S3 path:** premium_v3/projects/comfyui_automation.webp

### 6. GEDCOM Processing Engine
- **File:** gedcom.html, project-gedcom-platform.html
- **Description:** Enterprise genealogy data processing, zero-data-loss
- **Image needed:** Family tree/genealogy visualization
- **S3 path:** premium_v3/projects/gedcom_processing.webp

### 7. LLM Optimization Framework
- **File:** llm-optimization.html, project-llm-optimization.html
- **Description:** AI safety & evaluation, enterprise AI governance
- **Image needed:** AI evaluation dashboard
- **S3 path:** premium_v3/projects/llm_optimization.webp

### 8. Opportunity Bot (Market Intelligence)
- **File:** opportunity-bot.html, project-opportunity-bot.html
- **Description:** Autonomous opportunity discovery, proprietary scoring
- **Image needed:** Market intelligence dashboard
- **S3 path:** premium_v3/projects/opportunity_bot.webp

### 9. CLI Tools Suite (MISSING?)
- **File:** cli-tools.html (needs creation if missing)
- **Description:** Developer productivity tools, terminal automation
- **Image needed:** Terminal/CLI interface
- **S3 path:** premium_v3/projects/cli_tools.webp

---

## THE 4 FOUNDERS

### 1. Alicia
- **File:** alicia.html
- **Role:** VP & Chief Program Officer
- **Page exists:** Yes
- **Needs:** Professional headshot, candid photos
- **S3 path:** assets/founders/headshots_with_bg/alicia_headshot.webp

### 2. Bri
- **File:** bri.html
- **Role:** (Check page for role)
- **Page exists:** Yes
- **Needs:** Professional headshot, candid photos
- **S3 path:** assets/founders/headshots_with_bg/bri_headshot.webp

### 3. Jonathan
- **File:** jonathan.html
- **Role:** Chairman and CEO
- **Page exists:** Yes
- **Needs:** Professional headshot, candid photos
- **S3 path:** assets/founders/headshots_with_bg/jonathan_headshot.webp

### 4. Lilly
- **File:** lilly.html
- **Role:** (Check page for role)
- **Page exists:** Yes
- **Needs:** Professional headshot, candid photos
- **S3 path:** assets/founders/headshots_with_bg/lilly_headshot.webp

---

## DESIGN REQUIREMENTS

### Card Grid Layouts - CRITICAL

```css
/* Portfolio cards - ALWAYS 4 per row on desktop */
.portfolio-grid-4col {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 2rem;
}

/* Services/Solutions - ALWAYS 3 or 4 per row */
.solutions-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 2rem;
    max-width: 1200px;
    margin: 0 auto;
}

/* Team grid - 4 founders = 4 per row or 2x2 */
.team-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 2rem;
}

/* Responsive breakpoints */
@media (max-width: 1200px) { grid-template-columns: repeat(3, 1fr); }
@media (max-width: 992px) { grid-template-columns: repeat(2, 1fr); }
@media (max-width: 576px) { grid-template-columns: 1fr; }
```

### Centering - CRITICAL

```css
/* All sections must be centered */
.container {
    max-width: 1400px;
    margin: 0 auto;
    padding: 0 2rem;
}

.section-header.centered {
    text-align: center;
    margin: 0 auto;
}

/* Card grids must be centered within container */
.portfolio-grid-4col,
.solutions-grid,
.team-grid {
    justify-content: center;
    margin: 0 auto;
}
```

### Symmetry Rules

1. If 9 projects: Display as 3 rows of 3, OR 2 rows of 4 + 1 row centered
2. If 4 founders: Display as 1 row of 4, OR 2 rows of 2
3. If 8 items: Display as 2 rows of 4
4. Never leave odd items hanging to one side
5. Last row with fewer items should be centered

---

## FILE STRUCTURE

```
ISNBIZ_Files/
├── HTML Pages (on TrueNAS)
│   ├── index.html          # Homepage
│   ├── about.html          # About page
│   ├── services.html       # Solutions/services
│   ├── portfolio.html      # Portfolio grid (needs 9 projects)
│   ├── investors.html      # Investor info
│   ├── contact.html        # Contact form
│   ├── alicia.html         # Founder page
│   ├── bri.html            # Founder page
│   ├── jonathan.html       # Founder page
│   ├── lilly.html          # Founder page
│   ├── truenas.html        # Project detail
│   ├── videogen.html       # Project detail
│   ├── bin-intelligence.html
│   ├── spiritatlas.html
│   ├── comfyui.html
│   ├── gedcom.html
│   ├── llm-optimization.html
│   ├── opportunity-bot.html
│   └── cli-tools.html      # May need creation
│
├── CSS (on TrueNAS)
│   ├── styles.css          # Main styles (43KB)
│   └── enhanced-animations.css # Animations
│
├── JS (on TrueNAS)
│   ├── script.js           # Main JS
│   └── enhanced-interactions.js
│
└── Images (on S3 - NOT on TrueNAS)
    └── All via: https://isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com/
```

---

## S3 ASSET STRUCTURE

```
isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com/
├── premium_v3/
│   ├── logos/
│   │   ├── navbar_logo.webp
│   │   ├── hero_logo.webp
│   │   ├── footer_logo.webp
│   │   ├── favicon.webp
│   │   └── apple_touch_icon.webp
│   ├── og/
│   │   └── og_default.webp
│   ├── projects/                    # PROJECT IMAGES GO HERE
│   │   ├── truenas_infrastructure.webp
│   │   ├── videogen_youtube.webp
│   │   ├── bin_intelligence.webp
│   │   ├── comfyui_automation.webp
│   │   ├── gedcom_processing.webp
│   │   ├── llm_optimization.webp
│   │   ├── opportunity_bot.webp
│   │   └── cli_tools.webp          # NEEDS CREATION
│   ├── portfolio/
│   │   └── (responsive variants)
│   └── services/
│       └── (service images)
├── assets/
│   ├── founders/
│   │   └── headshots_with_bg/      # FOUNDER HEADSHOTS GO HERE
│   │       ├── alicia_headshot.webp
│   │       ├── bri_headshot.webp
│   │       ├── jonathan_headshot.webp
│   │       └── lilly_headshot.webp
│   └── projects/
│       └── spiritatlas_1.webp
└── generated/                       # AI-generated images
    ├── hero_*.webp
    ├── tech_*.webp
    ├── project_*.webp
    └── (45+ images cataloged in s3_urls.json)
```

---

## EXACT TASK LIST FOR COMPLETION

### Phase 1: Verify Current State
1. Check which project images exist on S3
2. Check which founder images exist on S3
3. Verify portfolio.html has correct 9-project grid
4. Verify all founder pages link correctly

### Phase 2: Generate Missing Images (USE gpt-image-1.5 quality=low)
1. Generate any missing project hero images
2. Generate any missing founder headshots
3. Generate founder candid/action photos
4. Convert all to WebP format

### Phase 3: Upload to S3
1. Upload images to correct S3 paths
2. Verify public access enabled
3. Test URLs are accessible

### Phase 4: Update HTML
1. Update portfolio.html with all 9 projects in 3x3 or 4+4+1 grid
2. Update founder pages with S3 image URLs
3. Update project detail pages with S3 image URLs
4. Ensure all grids are 3 or 4 per row
5. Ensure all content is centered

### Phase 5: Deploy to TrueNAS
1. Copy updated HTML/CSS/JS to TrueNAS
2. Do NOT copy images (they're on S3)
3. Reload Nginx
4. Test live site

---

## DEPLOYMENT COMMANDS

```bash
# SSH to TrueNAS
ssh jdmal@100.83.75.4

# Copy files to TrueNAS (from local)
scp index.html portfolio.html styles.css \
    jdmal@100.83.75.4:/mnt/tank/websites/kusanagi/isn.biz/public/

# Or use rsync
rsync -avz --exclude='*.py' --exclude='venv_fal' --exclude='.git' \
    --exclude='assets' --exclude='Archive' --exclude='scripts' \
    ./*.html ./*.css ./*.js \
    jdmal@100.83.75.4:/mnt/tank/websites/kusanagi/isn.biz/public/

# Reload Nginx
ssh jdmal@100.83.75.4 "sudo service nginx reload"

# Verify
curl -I https://isn.biz
```

---

## IMAGE GENERATION PROMPTS

### For Project Images (1536x1024 landscape)

```python
PROMPTS = {
    "truenas": "Professional enterprise server room visualization, blue #1E9FF2 accent lighting, rack-mounted servers with glowing indicators, modern data center aesthetic, clean tech photography style, 4K quality",

    "videogen": "AI video production interface, modern editing timeline, multiple video streams, blue #1E9FF2 UI elements, professional content creation dashboard, clean dark theme",

    "bin_intelligence": "Financial fraud detection dashboard, payment card analytics, real-time data visualization, blue #1E9FF2 and cyan #5FDFDF charts, enterprise security interface",

    "spiritatlas": "Elegant mobile app interface, spiritual wellness design, soft gradients, mindfulness UI, premium mobile mockup, peaceful aesthetic with blue accents",

    "comfyui": "Node-based AI workflow interface, ComfyUI style node graph, image generation pipeline, dark theme with blue #1E9FF2 connection lines",

    "gedcom": "Family tree visualization, genealogy network graph, professional data processing interface, blue connections on dark background",

    "llm_optimization": "AI model evaluation dashboard, benchmark metrics display, LLM performance graphs, enterprise AI governance interface, blue #1E9FF2 theme",

    "opportunity_bot": "Market intelligence dashboard, opportunity discovery interface, scoring metrics, automated research visualization, blue and cyan data charts",

    "cli_tools": "Modern terminal interface, command line productivity tools, syntax highlighted code, dark theme with blue #1E9FF2 accents"
}
```

### For Founder Headshots (1024x1024 square)

```python
# Use gpt-image-1.5/edit with source photos
FOUNDER_PROMPTS = {
    "headshot": "Professional corporate headshot, soft studio lighting, neutral gradient background, executive portrait style, high quality, sharp focus on face",

    "candid": "Natural candid photo in modern office environment, professional but approachable, warm lighting, authentic expression"
}
```

---

## VERIFICATION CHECKLIST

After completion, verify:

- [ ] All 9 projects displayed on portfolio.html
- [ ] Portfolio grid is 3x3 or properly centered
- [ ] All 4 founder pages have images
- [ ] Founder team section shows 4 in a row (or 2x2)
- [ ] All project detail pages have hero images
- [ ] All images load from S3 (check Network tab)
- [ ] No broken image links (check console)
- [ ] Cards are symmetrical and centered
- [ ] Mobile responsive works
- [ ] Live site at https://isn.biz reflects changes

---

## IMPORTANT WARNINGS

1. **DO NOT use quality="high"** on fal.ai - it burns credits
2. **DO NOT upload images to TrueNAS** - they go on S3 only
3. **DO NOT modify the theme/CSS** unless fixing grid layouts
4. **DO NOT delete existing working pages** - only update/add
5. **ALWAYS test locally before deploying** to TrueNAS
6. **ALWAYS backup current state** before making changes

---

## CONTACT & SUPPORT

- **TrueNAS Server:** 100.83.75.4
- **S3 Bucket:** isnbiz-assets-1769962280
- **Live Site:** https://isn.biz
- **FAL API:** Credentials in 1Password

---

## SUMMARY FOR CODEX CLI 5.2

**Primary Objective:** Complete the ISN.BIZ website by:
1. Adding images for all 9 projects (using gpt-image-1.5 quality=low)
2. Adding proper founder photos to all 4 founder pages
3. Ensuring all card grids are 3 or 4 per row and centered
4. Deploying HTML to TrueNAS, images to S3

**Key Constraints:**
- ONLY use gpt-image-1.5 and gpt-image-1.5/edit
- ALWAYS set quality="low" (it's inverted - low is best)
- Pages on TrueNAS, images on S3
- Preserve the existing theme/design
- Make everything symmetrical and centered

**End State:**
- 9 projects with images in centered grid
- 4 founders with professional photos
- All images served from S3 CDN
- Live at https://isn.biz
