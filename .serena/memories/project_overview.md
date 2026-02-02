# ISN.BIZ Website - Project Overview

## Purpose
Professional investor-ready website for ISN.BIZ Inc (software company). Static multi-page website designed to attract funding and showcase AI/cloud software portfolio.

## Project Status
**Production Ready** - Awaiting deployment to Netlify or Kusanagi

## Tech Stack

### Frontend
- **HTML5** - Semantic, accessible markup (WCAG 2.1 AA compliant)
- **CSS3** - Modern, mobile-first styling with custom properties
- **Vanilla JavaScript** - Minimal JS for form handling and smooth scrolling
- **No frameworks** - Intentionally framework-free for speed

### Design System
- **Neo-Technical Brutalism** - Distinctive design approach
- **Brand Colors:**
  - Primary Blue: `#1E9FF2`
  - Secondary Cyan: `#5FDFDF`
  - Charcoal: `#0D1117`
  - Accent Pink: `#FF2D55`
- **Typography:**
  - Mono: JetBrains Mono
  - Display: Archivo Black
  - Body: IBM Plex Sans

### Asset Management
- **S3 Storage:** isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com
- All images served from S3 (logos, backgrounds, OG images)
- WebP format for optimal performance

### Python Tooling (Optional)
- **Python 3.12** with venv at `venv_fal/`
- **Dependencies:** `requirements_assets.txt`
  - requests >= 2.31.0
  - Pillow >= 10.0.0
  - boto3 >= 1.28.0
- **Purpose:** Asset generation and S3 uploads (not needed for website itself)

## Website Structure

### Pages (Multi-page site)
1. **index.html** - Homepage with hero, about, and overview
2. **about.html** - Company details and history
3. **services.html** - Solutions portfolio
4. **portfolio.html** - Case studies and projects
5. **investors.html** - Investment opportunities
6. **contact.html** - Contact form

### Key Sections on Homepage
- Navigation (fixed header with mobile menu)
- Hero (full-height with logo, stats, CTAs)
- About (company overview, credentials)
- Solutions (4 cards: AI, Cloud, Enterprise, Data)
- Portfolio Preview (3 case studies)
- Investor Section (pitch, investment highlights)
- Contact (form + company info)
- Footer (credentials, links, copyright)

## File Structure
```
ISNBIZ_Files/
├── index.html              # Main homepage
├── about.html              # About page
├── services.html           # Services page
├── portfolio.html          # Portfolio page
├── investors.html          # Investors page
├── contact.html            # Contact page
├── styles.css              # Main stylesheet
├── script.js               # JavaScript functionality
├── slider-styles.css       # Gallery/slider styles
├── slider-init.js          # Gallery/slider initialization
├── .gitignore              # Git ignore patterns
├── README.md               # Project documentation
├── CLAUDE.md               # AI assistant context
├── docs/                   # 40+ documentation files
├── scripts/                # Python asset generation scripts
├── assets/                 # Local assets (if any)
├── venv_fal/               # Python virtual environment
├── wp-theme-isnbiz-2026/   # WordPress theme version
└── deploy-*.sh             # Deployment scripts
```

## Key Features
- **WCAG 2.1 AA Compliant** - Accessibility audited
- **Mobile-First** - Responsive design, touch-friendly
- **SEO Optimized** - Semantic HTML, proper meta tags
- **Fast Loading** - Ultra-lightweight (30KB HTML + 23KB CSS + 687B JS)
- **Investor-Focused** - Clear CTAs, professional design
- **Trust Signals** - DUNS, UBI, EIN displayed

## Company Information
- **DUNS:** 080513772
- **UBI:** 603-522-339
- **EIN:** 47-4530188
- **Founded:** July 8, 2015
- **Type:** Software development company
- **Focus:** AI, Cloud, Enterprise Software, Data Analytics

## Development Environment
- **Platform:** Windows (WSL2 compatible)
- **Location:** D:\workspace\ISNBIZ_Files
- **Git:** Yes, separate git repo for this project
- **Serena:** Active (.serena/ directory present)

## Related Projects
- **HROC Website** - Similar static site (reference for patterns)
- **Opportunity Bot** - AI research tool (separate project)
- **Workspace** - D:\workspace\ (container for all projects)
