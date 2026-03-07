# ISN.BIZ Website - Project Overview

**Last Updated:** 2026-02-25

## Purpose
Professional investor-ready website for ISN.BIZ Inc (software company). Multi-page static HTML/CSS/JS site designed to attract funding and showcase AI/cloud software portfolio.

## Project Status
**LIVE IN PRODUCTION** at https://isn.biz
- CI/CD: GitHub Actions auto-deploys to Netlify on push to main
- All Playwright tests pass (132 tests, `tests/site-audit.spec.js`)
- DNS: Cloudflare proxy (orange cloud) → Netlify
- TrueNAS no longer serves this site (Netlify only)

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

### Pages (20 total)
**Main pages:**
1. `index.html` - Homepage (hero, about, solutions, portfolio preview, investor section, team, contact)
2. `about.html` - Company details, trust badges (6), team grid (4 founders)
3. `services.html` - Solutions portfolio with visual grid
4. `portfolio.html` - 8 case studies (4x2), methodology, results
5. `investors.html` - Investment pitch, market opportunity, use of funds (6 items)
6. `contact.html` - Contact form (currently stub - shows alert())
7. `404.html` - Custom error page

**Founder bio pages:**
8. `jonathan.html` (CEO) | 9. `bri.html` (COO) | 10. `lilly.html` (CFO) | 11. `alicia.html` (CPO)

**Project pages (9 projects):**
12. `truenas.html` | 13. `videogen.html` | 14. `bin-intelligence.html` | 15. `spiritatlas.html` (Coming March 2026)
16. `comfyui.html` | 17. `gedcom.html` | 18. `llm-optimization.html` | 19. `opportunity-bot.html` | 20. `aurallm.html`

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
├── *.html                  # 20 HTML pages (see Pages section above)
├── styles.css              # Main stylesheet
├── script.js               # Main JavaScript (minimal, ~687B)
├── enhanced-animations.css # Animation styles
├── netlify.toml            # Netlify config + clean URL redirects for all 19 pages
├── playwright.config.js    # Playwright config (baseURL: https://isn.biz)
├── package.json            # Node deps (Playwright only)
├── .github/workflows/      # CI/CD (auto-deploy.yml: test → deploy)
├── tests/                  # Playwright test suite
│   └── site-audit.spec.js  # 132 tests covering all pages
├── scripts/                # Python asset generation scripts (fal.ai + S3)
├── venv_fal/               # Python venv for asset generation (gitignored)
├── assets/                 # Local asset copies (gitignored, 154MB - use S3 instead)
├── docs/                   # 40+ historical documentation files
├── .serena/                # Serena AI context (memories, project.yml)
└── .claude/                # Compound engineering plugin (agents, commands, skills)
```

## Company Information
- **DUNS:** 080513772 | **UBI:** 603-522-339 | **EIN:** 47-4530188
- **Founded:** July 8, 2015 | **Type:** Software development company
- **Founders:** Jonathan (CEO), Bri (COO), Lilly (CFO), Alicia (CPO)
- **Focus:** AI (Claude, GPT, Qwen), Cloud (AWS/Azure), Enterprise Software, Data Analytics

## Critical Design Rules

### Card Grid Symmetry (ENFORCED - CRITICAL)
- Cards MUST be 3xN or 4xN (acceptable: 3, 4, 6, 8, 9, 12)
- NEVER allow 1 or 2 orphaned/hanging cards in any grid section

### Image Policy for fal.ai Asset Generation
- Model: `fal-ai/gpt-image-1.5` (generation) or `fal-ai/gpt-image-1.5/edit` (editing)
- Quality: ALWAYS `"low"` (INVERTED setting - "low" = best quality, fastest, cheapest)
- NEVER use: high/medium quality, nano-banana-pro, flux-pro

### Clean URLs
- All pages use clean URLs (/about, /jonathan, /opportunity-bot, etc.)
- Redirects defined in `netlify.toml`

## Local Development Warning
- This Windows machine has Tailscale overriding `isn.biz` DNS → 100.65.249.20
- To test via Cloudflare: `curl --resolve "isn.biz:443:104.21.18.246" https://isn.biz`
- To test via Netlify directly: `curl --resolve "isn.biz:443:75.2.60.5" https://isn.biz`

## Related Projects
- **HROC Website** - Similar static site (reference for patterns)
- **Workspace** - D:\workspace\ (container for all projects)
