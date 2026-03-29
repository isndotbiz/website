# CLAUDE.md - ISN.BIZ Website

## 1Password Connect — Credential Access
All credentials via 1Password Connect. No service accounts, no desktop auth, no plaintext .env secrets.
- `OP_CONNECT_HOST=http://100.67.89.29:8100`
- `OP_CONNECT_TOKEN` — set in global CLAUDE.md (inherited automatically)
- Vaults: `Research`, `TrueNAS Infrastructure`
- Usage: `op item get "Name" --vault "Research" --format json`

**Project:** ISN.BIZ Inc Investor-Ready Website
**Status:** LIVE IN PRODUCTION at https://isn.biz
**Last Updated:** 2026-02-25

---

## Architecture

```
Browser → Cloudflare (proxy ON, SSL: Full) → Netlify (HTML pages)
                                            → S3 CDN (all images/assets)
```

- **20 HTML pages** (7 main + 4 founder bios + 9 project pages)
- **Design system:** Neo-Technical Brutalism (dark, technical aesthetic)
- **Testing:** Playwright (`tests/site-audit.spec.js`) against https://isn.biz
- **CI/CD:** GitHub Actions (`.github/workflows/auto-deploy.yml`) — tests then deploys
- **Repo:** https://github.com/isndotbiz/website.git
- **Netlify site:** `isndotbiz.netlify.app` (site ID: `4d860499-0d6c-49cd-864f-69a0b7a2b3fe`)

---

## Website Pages

### Main Pages
| File | URL | Description |
|------|-----|-------------|
| `index.html` | `/` | Homepage: hero, about, solutions (4), portfolio preview (9), team (4), investors |
| `about.html` | `/about` | Company details, 6 trust badges, team grid (4 founders) |
| `services.html` | `/services` | Solutions portfolio with visual grid |
| `portfolio.html` | `/portfolio` | 8 case studies (4x2), methodology, results |
| `investors.html` | `/investors` | Investment pitch, market, use of funds (6 items) |
| `contact.html` | `/contact` | Contact form (currently stub — shows alert()) |
| `404.html` | (error) | Custom 404 error page |

### Founder Bio Pages
`jonathan.html` (CEO), `bri.html` (COO), `lilly.html` (CFO), `alicia.html` (CPO)

### Project Pages (9)
`truenas.html`, `videogen.html`, `bin-intelligence.html`, `spiritatlas.html` (Coming March 2026),
`comfyui.html`, `gedcom.html`, `llm-optimization.html`, `opportunity-bot.html`, `aurallm.html`

---

## Brand Colors (Neo-Technical Brutalism)

```css
--color-blue: #1E9FF2      /* Primary brand — CTAs, accents */
--color-cyan: #5FDFDF      /* Secondary — highlights, gradients */
--color-charcoal: #0D1117  /* Dark backgrounds */
--accent-pink: #FF2D55     /* Accent highlights */
```

---

## File Structure

```
ISNBIZ_Files/
├── *.html                              # 20 HTML pages
├── styles.css                          # Main stylesheet
├── script.js                           # Main JavaScript (minimal)
├── enhanced-animations.css             # Animation styles
├── netlify.toml                        # Netlify config + 19 clean URL redirects
├── playwright.config.js                # Test config (baseURL: https://isn.biz)
├── package.json                        # Node deps (Playwright only)
├── .github/workflows/auto-deploy.yml   # CI/CD: test → deploy on push to main
├── tests/site-audit.spec.js            # Playwright test suite
├── scripts/                            # Python asset generation scripts (fal.ai)
├── assets/                             # Local asset copies (gitignored, 154MB — use S3)
├── logo.png                            # ISN.BIZ logo
└── docs/                               # 40+ historical documentation files
```

---

## Deployment

### Standard (CI/CD)

```bash
git add <specific files>
git commit -m "fix: description"
git push origin main
# GitHub Actions: runs Playwright tests → deploys to Netlify if tests pass
```

### Emergency Manual Deploy

```bash
npm install -g netlify-cli
netlify deploy --prod --dir=. \
  --auth=$NETLIFY_AUTH_TOKEN \
  --site=4d860499-0d6c-49cd-864f-69a0b7a2b3fe
```

### Verify Live Site

```bash
curl -I https://isn.biz

# Tailscale DNS bypass (if needed):
curl --resolve "isn.biz:443:104.21.18.246" -I https://isn.biz  # via Cloudflare
curl --resolve "isn.biz:443:75.2.60.5" -I https://isn.biz       # via Netlify
```

---

## S3 Asset Management

All production images served from S3 CDN (not local files):
- **S3 Bucket:** `isnbiz-assets-1769962280` (us-east-1)
- **URL pattern:** `https://isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com/assets/...`
- **Format:** WebP preferred
- Local `assets/` folder is gitignored — do NOT commit it

```bash
aws s3 cp my-image.webp s3://isnbiz-assets-1769962280/assets/ --acl public-read
# Reference: <img src="https://isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com/assets/my-image.webp">
```

---

## Open Tasks

**Critical:**
- [ ] Contact form backend (currently shows `alert()` — needs Netlify Forms or Formspree)

**High Priority:**
- [ ] Google Analytics 4 (add GA4 ID to all 20 pages)
- [ ] reCAPTCHA on contact form
- [ ] Alicia headshot regeneration (chin dimple AI artifact)

**Medium:**
- [ ] SpiritAtlas launch (update "Coming March 2026" badge)
- [ ] Privacy policy + Terms of service pages

---

## How to Update

### Change Content
Edit the relevant `.html` file directly. Cards MUST maintain 3xN or 4xN grid layout.

### Change Colors
Edit CSS custom properties at top of `styles.css`.

### Add a New Page
1. Copy an existing similar page as template
2. Update navigation links on ALL pages
3. Add clean URL redirect to `netlify.toml`
4. Add test coverage in `tests/site-audit.spec.js`
5. Commit and push — CI/CD handles deploy

---

## Form Backend Options

### Formspree (Easiest)
```html
<form action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
```
Free tier: 50 submissions/month, no backend code needed.

### Netlify Forms
```html
<form name="contact" method="POST" data-netlify="true" netlify-honeypot="bot-field">
  <input type="hidden" name="form-name" value="contact" />
```
Included with Netlify hosting, built-in spam protection.

---

## Common Update Patterns

### Update Stats (index.html ~45-57)
```html
<div class="stat">
    <span class="stat-number">NEW_VALUE</span>
    <span class="stat-label">Label</span>
</div>
```

### Add Portfolio Item (index.html ~207-235)
```html
<div class="portfolio-item">
    <span class="portfolio-tag">Industry Tag</span>
    <h3>Project Title</h3>
    <p>Description...</p>
    <div class="portfolio-tech"><span>Tech 1</span></div>
    <div class="portfolio-metric"><strong>Metric:</strong> Result</div>
</div>
```

### Add Analytics (before `</head>`)
```html
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

---

## Company Information

- **DUNS:** 080513772
- **UBI:** 603-522-339
- **EIN:** 47-4530188
- **Founded:** July 8, 2015
- **Type:** Software development company
- **Focus:** AI-Powered Apps, Cloud Solutions, Enterprise Software, Data Analytics

**Live:** https://isn.biz | **Netlify:** https://isndotbiz.netlify.app

---

## Troubleshooting

- **Form not submitting** — Check form backend config, verify action URL, check browser console
- **Images not loading** — All images on S3 CDN; check URL, verify `--acl public-read` on upload
- **Mobile menu broken** — Ensure `script.js` loads, check console for JS errors
- **Netlify deploy failed** — Check build logs, verify all files committed, no files >100MB

---

## Local Development

```bash
python -m http.server 8000    # Preview at http://localhost:8000
npx playwright test            # Run tests against https://isn.biz
BASE_URL=http://localhost:8000 npx playwright test  # Test locally
```

---

**Maintained by:** jdmal + Claude AI
**Next priority:** Contact form backend + Google Analytics 4
