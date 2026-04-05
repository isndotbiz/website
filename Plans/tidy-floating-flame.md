# Plan: Migrate ISN.BIZ Assets to Backblaze B2 + WebP + Spirit Atlas Image Update

## Context

ISN.BIZ is currently deployed on **Cloudflare Pages** (project `isnbiz-website`, domains: `isn.biz`, `www.isn.biz`). Assets are on **Cloudflare R2** via `cdn.isn.biz`. Jonathan wants to:
1. Move all assets to **Backblaze B2** (already authorized, CLI ready)
2. Convert all PNG/JPG assets to **WebP** for smaller payloads
3. Update **Spirit Atlas page images** from the latest Spirit-Atlas repo images
4. Deploy the updated site to **CF Pages** (already set up, just needs fresh deploy)

## Current State

| Item | Current | Target |
|------|---------|--------|
| Hosting | CF Pages (last deploy 5 days ago) | CF Pages (fresh deploy) |
| Assets | R2 via `cdn.isn.biz` | B2 public bucket via Cloudflare CDN |
| Image format | 13 PNG + 36 WebP in HTML, 333 PNG + 71 MP4 in JS | All WebP (videos stay MP4) |
| Spirit Atlas | Generated art from Flux LoRAs | Real app images from Spirit-Atlas/images |
| B2 auth | CLI authorized, 3 private buckets | New public bucket `isnbiz-assets` |

## Asset Inventory

**HTML refs (49 unique URLs):**
- 36 WebP (logos, portraits, founders, project action shots) — already optimal
- 9 PNG hero images (`assets/generated/truenas_flux/*/hero.png`) — convert to WebP
- 4 PNG Spirit Atlas inline images — convert to WebP

**JS refs (404 files in `spiritatlas-final-media.generated.js`):**
- 333 PNG images — convert to WebP
- 71 MP4 videos — keep as MP4

**Total: ~453 files to upload to B2** (~1.9GB as PNG/MP4, expected ~800MB after WebP conversion)

## Steps

### Step 1: Create B2 Public Bucket
- Create bucket `isnbiz-cdn` with `allPublic` visibility
- B2 public URL pattern: `https://f004.backblazeb2.com/file/isnbiz-cdn/...`
- Set up Cloudflare CDN: CNAME `b2cdn.isn.biz` → B2 friendly URL for clean paths

### Step 2: Convert All PNG Assets to WebP Locally
- Convert 9 hero PNGs → WebP using `cwebp` (quality 85, available at `/opt/local/bin/cwebp`)
- Convert 333 Spirit Atlas image PNGs → WebP
- Convert 4 Spirit Atlas inline images → WebP
- Keep 71 MP4 videos as-is
- Keep 36 existing WebP assets as-is (download from R2, re-upload to B2)

### Step 3: Upload All Assets to B2
- Upload converted WebP + existing WebP + MP4 to B2 bucket
- Use `b2 upload-file` or `b2 sync` for bulk upload
- Maintain same path structure (just swap `.png` → `.webp` where converted)

### Step 4: Update Spirit Atlas Page Images
- Replace the 4 inline Spirit Atlas images in `spiritatlas.html` with latest from `Spirit-Atlas/images/`
- Update `spiritatlas-final-media.generated.js` to regenerate from latest Spirit-Atlas/images source
- Convert all to WebP before upload

### Step 5: Update All HTML/JS CDN References
- Replace `https://cdn.isn.biz/` → new B2 CDN base URL in all HTML files
- Replace `.png` → `.webp` for converted images in HTML and JS
- Update og:image URLs to WebP versions

### Step 6: Create CF Pages `_redirects` File
- CF Pages uses `_redirects` instead of `netlify.toml`
- Convert all 19 Netlify redirects to CF Pages format
- Add security headers via `_headers` file

### Step 7: Deploy to CF Pages
- `wrangler pages deploy . --project-name isnbiz-website --branch main`
- Verify live site

### Step 8: Verify
- Check all og:image tags point to B2 CDN WebP URLs
- Spot-check 10 random Spirit Atlas media wall images
- Verify clean URLs work (e.g., `/about` → `about.html`)
- Verify security headers present

## Key Files to Modify

| File | Changes |
|------|---------|
| `*.html` (12 project pages) | CDN URL base + .png→.webp |
| `index.html` | CDN URL base + .png→.webp |
| `portfolio.html` | CDN URL base + .png→.webp |
| `services.html` | CDN URL base + .png→.webp |
| `spiritatlas.html` | CDN URL base + inline images from Spirit-Atlas |
| `js/spiritatlas-final-media.generated.js` | Regenerate with B2 CDN + .webp |
| `js/spiritatlas-media-wall.js` | No change (format-agnostic) |
| `_redirects` | **NEW** — CF Pages clean URL redirects |
| `_headers` | **NEW** — CF Pages security/cache headers |
| `.gitignore` | Remove netlify.toml reference if needed |

## B2 CDN URL Strategy

**Option A**: Direct B2 URL — `https://f004.backblazeb2.com/file/isnbiz-cdn/path/to/file.webp`
**Option B**: Cloudflare CNAME — `https://b2cdn.isn.biz/path/to/file.webp` (CNAME → B2 friendly URL)

**Recommend Option B** — cleaner URLs, Cloudflare cache in front, consistent with existing `cdn.isn.biz` pattern.

## Verification

1. `grep -rn 'og:image' *.html` — all point to B2 CDN WebP
2. `grep -c 'cdn.isn.biz' *.html js/*.js` — should be 0 (migrated to B2)
3. `curl -I https://b2cdn.isn.biz/assets/generated/truenas_flux/opportunity-bot/hero.webp` — 200
4. Spot-check Spirit Atlas media wall — 10 random images return 200
5. `curl -I https://isn.biz/about` — 200, correct headers
6. `wrangler pages deployment list --project-name isnbiz-website` — fresh deployment visible
