# ISN.BIZ Website

Live investor-ready website for ISN.BIZ Inc. LIVE at https://isn.biz.

## Stack / Architecture
- 20 static HTML pages + CSS/JS — no framework
- Hosting: Netlify (`isndotbiz.netlify.app`, site ID: `4d860499-0d6c-49cd-864f-69a0b7a2b3fe`)
- CDN/proxy: Cloudflare (SSL: Full) in front of Netlify
- Images: AWS S3 bucket `isnbiz-assets-1769962280` (us-east-1) — **migration to Backblaze B2 planned**
- CI/CD: GitHub Actions → Playwright tests → Netlify deploy on push to main

## Key Files
```
ISNBIZ_Files/
├── *.html              # 20 pages (7 main, 4 bios, 9 project pages)
├── styles.css          # CSS vars: --color-blue #1E9FF2, --color-cyan #5FDFDF, --color-charcoal #0D1117
├── netlify.toml        # 19 clean URL redirects
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
git push origin main   # triggers CI: tests → Netlify deploy
# Emergency manual:
netlify deploy --prod --dir=. --auth=$NETLIFY_AUTH_TOKEN --site=4d860499-0d6c-49cd-864f-69a0b7a2b3fe
```

## Image Upload (current S3)
```bash
aws s3 cp image.webp s3://isnbiz-assets-1769962280/assets/ --acl public-read
# URL: https://isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com/assets/image.webp
```

## Conventions
- Cards MUST maintain 3xN or 4xN grid layout
- Design: Neo-Technical Brutalism (dark, technical)
- New pages: copy template → update all nav links → add netlify.toml redirect → add test
- Local `assets/` is gitignored (154MB) — use S3 URLs only
- WebP format preferred for all images

## Open Tasks
- [ ] Contact form backend (currently `alert()` — use Netlify Forms or Formspree)
- [ ] Google Analytics 4 on all 20 pages
- [ ] Update SpiritAtlas "Coming March 2026" badge
