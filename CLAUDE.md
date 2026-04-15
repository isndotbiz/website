# ISN.BIZ Website

Live investor-ready website for ISN.BIZ Inc. LIVE at https://isn.biz.

## Stack / Architecture
- 20 static HTML pages + CSS/JS — no framework
- Hosting: Cloudflare Pages
- CDN/proxy: Cloudflare (SSL: Full)
- Images: Backblaze B2 via `b2cdn.isn.biz` + AWS S3 bucket `isnbiz-assets-1769962280` (legacy)
- CI/CD: GitHub Actions → Playwright tests → deploy on push to main

## Key Files
```
ISNBIZ_Files/
├── *.html              # 20 pages (7 main, 4 bios, 9 project pages)
├── styles.css          # CSS vars: --color-blue #1E9FF2, --color-cyan #5FDFDF, --color-charcoal #0D1117
├── tests/site-audit.spec.js  # Playwright suite (baseURL: https://isn.biz)
└── .github/workflows/auto-deploy.yml
```

## Dev Commands
```bash
python -m http.server 8000                           # local preview :8000
npx playwright test                                  # test against https://isn.biz
BASE_URL=http://localhost:8000 npx playwright test   # test locally
```

## Deploy
```bash
git push origin main   # triggers CI: tests → deploy
```

## Image Upload (Backblaze B2)
```bash
# URL pattern: https://b2cdn.isn.biz/file/isnbiz-cdn/assets/image.webp
```

## Conventions
- Cards MUST maintain 3xN or 4xN grid layout
- Design: Neo-Technical Brutalism (dark, technical)
- New pages: copy template → update all nav links → add redirect → add test
- Local `assets/` is gitignored (154MB) — use B2 CDN URLs only
- WebP format preferred for all images

## Open Tasks
- [ ] Contact form backend (wire up Cloudflare Worker or Formspree)
- [ ] Google Analytics 4 on all 20 pages
