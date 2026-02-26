# ISN.BIZ Website State - 2026-02-04

## Quick Reference (Updated 2026-02-25)
- **Live:** https://isn.biz
- **Netlify:** https://isndotbiz.netlify.app (Site ID: 4d860499-0d6c-49cd-864f-69a0b7a2b3fe)
- **S3:** `isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com`
- **Repo:** https://github.com/isndotbiz/website.git
- **Cloudflare Zone:** `a2efe184e74443f824ef58f1c862eb5a`

## Architecture (as of 2026-02-24)
```
Browser → Cloudflare (proxy ON, SSL: Full) → Netlify (HTML)
                                           → S3 (all images)
```
- DNS: Cloudflare proxy ENABLED (orange cloud) → IPs 104.21.18.246, 172.67.183.245
- SSL: Cloudflare Universal SSL (fixed 2026-02-24, was DNS-only with no cert)
- Last CI deploy: Feb 25 2026 (deploy ID: 699ec426a23b8757455fce0c, commit 80ea051)
- TrueNAS no longer serves this site
- GitHub Actions secrets: NETLIFY_AUTH_TOKEN + NETLIFY_SITE_ID set ✓

## CI/CD Status (2026-02-25)
- GitHub Actions: fully working, all 132 tests pass ✓
- Netlify deploy: triggered by push to main, tests-then-deploy ✓
- All HTML pages use clean URLs (/about, /jonathan, /opportunity-bot, etc.)
- netlify.toml has redirects for all 19 pages (main + team + projects)
- tests/website-fixes-verification.spec.js DELETED (was using localhost:8000)

## Local DNS Warning
- This Windows machine has Tailscale overriding `isn.biz` DNS → 100.65.249.20
- Use `--resolve "isn.biz:443:104.21.18.246"` to test via Cloudflare
- Or `--resolve "isn.biz:443:75.2.60.5"` to test via Netlify directly

## Symmetry Rules (CRITICAL)
- Cards MUST be 3×n or 4×n (3,4,6,8,9,12)
- NEVER 1-2 hanging cards
- All 19 sections now compliant

## Image Policy (CRITICAL)
- Model: `fal-ai/gpt-image-1.5` or `/edit`
- Quality: ALWAYS `"low"` (inverted - low=best)
- NEVER: high/medium quality, nano-banana-pro, flux-pro

## 9 Projects (Updated 2026-02-06)
1. TrueNAS Infrastructure
2. VideoGen YouTube
3. BIN Intelligence
4. SpiritAtlas
5. ComfyUI Automation
6. GEDCOM Processing
7. LLM Optimization
8. Opportunity Bot
9. AuraLLM (~2025) — replaced CLI Tools on 2026-02-06

CLI Tools removed: internal standards, not a product.
AuraLLM page: aurallm.html, images on S3 at assets/projects/aurallm_*.webp

## 4 Founders
Jonathan (CEO), Bri (COO), Lilly (CFO), Alicia (CPO)

## Recent Updates (2026-02-06)
- ✓ Homepage: SpiritAtlas slider with "Coming March 2026"
- ✓ About page: 3-column grid + 6th trust badge (Open Source Contributor)
- ✓ Repo: Removed cli-tools.html, publish/ folder
- ✓ Git: Added playwright-report/, test-results/ to .gitignore
- ✓ 404 error page created
- ✓ DEPLOYMENT_GAPS.md: Complete external dependency checklist
- ✓ Branch: audit-cleanup-2026-02-06 pushed to GitHub

## Known Issues
- Alicia headshot: CENTER CHIN DIMPLE (AI artifact)
- assets/ folder (154MB, 197 files) - all on S3, local copies in .gitignore, safe to delete
- Local Tailscale DNS overrides isn.biz → use --resolve to bypass

## Recommended Hosting
Cloudflare Pages (prod) + TrueNAS (dev) + Cloudflare CDN for S3
