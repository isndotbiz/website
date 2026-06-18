# iSN.BiZ Website

Live, investor-facing website for ISNBIZ INCORPORATED (brand "iSN.BiZ").
Live at **https://isn.biz**.

## Stack

- Static HTML/CSS/JS — no framework, no build step
- One Cloudflare Pages Function (`functions/api/contact.js`) for the contact form
- Hosting: Cloudflare Pages (project `isnbiz-website`)
- CDN/proxy: Cloudflare in front of the origin
- Images: Backblaze B2 served via `b2c.isn.biz` (local `assets/` is gitignored — use CDN URLs)
- Analytics: Google Analytics 4 (`G-XTNRN7YP16`), included site-wide
- CI/CD: GitHub Actions → Playwright → `wrangler pages deploy` on push to `main`

## Pages

19 static HTML pages at the repo root plus `signals/index.html`:

- **Main:** `index.html`, `about.html`, `services.html`, `portfolio.html`, `investors.html`, `contact.html`
- **Products:** `spiritatlas.html`, `provenance.html`, `signals/index.html`, `phantom-browser.html`, `crucible.html`, `hermes-aingels.html`
- **Founders/bios:** `jonathan.html`, `bri.html`, `lilly.html`
- **Other:** `hroc-files.html`, `privacy.html`, `terms.html`, `404.html`

## Brand

CSS variables in `styles.css`:

- `--color-blue` `#1E9FF2` (primary)
- `--color-cyan` `#5FDFDF` (accent)
- `--color-charcoal` `#0D1117` (dark background)

Design language: dark, technical ("Neo-Technical Brutalism"). Cards keep 3xN / 4xN grid layouts.

## SEO / metadata

- OG, Twitter, and canonical tags on all pages
- JSON-LD structured data: Organization + WebSite (inline on `index.html`), Person (founder pages), BreadcrumbList + SoftwareApplication (product pages)
- Reference JSON-LD copies: `schema-organization.json`, `schema-website.json`, `schema-services.json`, `schema-team.json`, `schema-breadcrumb.json`
- `sitemap.xml` (18 URLs), `robots.txt`
- Response headers in `_headers` (X-Frame-Options, X-Content-Type-Options, Referrer-Policy, Permissions-Policy, long-lived cache for CSS/JS/WebP). No Content-Security-Policy header yet.

## Contact form backend

`functions/api/contact.js` — Cloudflare Pages Function on `POST /api/contact`. Sends submissions via the Resend HTTP API (raw SMTP is unavailable in the Workers runtime). Includes a honeypot field, server-side validation, and HTML escaping. If `RESEND_API_KEY` is unset it returns a clear "not configured" message rather than silently dropping mail.

Environment variables (set in the Cloudflare Pages dashboard → Settings → Environment variables):

| Var | Purpose | Default |
|-----|---------|---------|
| `RESEND_API_KEY` | Resend API key | (required for delivery) |
| `CONTACT_TO` | destination address | `jdm@isn.biz` |
| `CONTACT_FROM` | verified Resend sender | `iSN.BiZ Contact <contact@isn.biz>` |

`isn.biz` must be verified in Resend for the default `CONTACT_FROM` to deliver.

## Develop / test / deploy

```bash
# Local preview server (serves the static site on :8080, mirrors clean URLs)
node scripts/preview-server.js

# Run Playwright suite against the local preview
BASE_URL=http://localhost:8080 npx playwright test

# Run against production
BASE_URL=https://isn.biz npx playwright test

# Deploy: push to main triggers CI (tests → wrangler deploy)
git push origin main
```

Tests live in `tests/site-audit.spec.js` (page-load, nav/footer uniformity, section visibility, CDN image loads, word-count minimums, mobile checks — parameterized across all pages). `tests/visual-workflow.spec.js` covers the asset-generation tooling under `tools/`. Playwright `baseURL` defaults to `http://localhost:8080`; override with `BASE_URL`.

## CI deploy detail

`.github/workflows/auto-deploy.yml` copies only the static site files into a staging dir before `wrangler pages deploy` — the repo contains large sibling dirs (e.g. `hrocincorg/`) that exceed Cloudflare Pages' per-file limit, so a blanket deploy is not used. Staged: top-level `*.html`/`*.css`/`*.js`, `_headers`, `_redirects`, `robots.txt`, `sitemap.xml`, `schema-*.json`, `js/`, `signals/`, and `functions/`.

## Company

- ISNBIZ INCORPORATED ("iSN.BiZ")
- Founded: 2015-07-08
- DUNS 080513772 · UBI 603-522-339 · EIN 47-4530188
- https://isn.biz
