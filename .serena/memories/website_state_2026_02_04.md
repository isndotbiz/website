# ISN.BIZ Website State - 2026-02-04

## Quick Reference (Updated 2026-02-24)
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
- Last CLI deploy: Feb 17 2026 (deploy ID: 69948971795b231edff10983)
- TrueNAS no longer serves this site

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
- Playwright tests fail against live site (not yet deployed with latest changes)

## Recommended Hosting
Cloudflare Pages (prod) + TrueNAS (dev) + Cloudflare CDN for S3
