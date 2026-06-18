# STATE — iSN.BiZ Website

Resume doc for the next session. Live at https://isn.biz (Cloudflare Pages, project `isnbiz-website`).

## Where we are

- **Branch:** `autopilot/quality-pass` (working branch; not yet merged to main)
- **main HEAD:** `3f1fd7e` — contact Function returns 200 `{ok:false}` on handled errors (CF masks 5xx), env-driven recipient

### Deployed on main (recent quality pass)
- Brand casing normalized to **iSN.BiZ**
- OG / Twitter / canonical tags on all pages
- JSON-LD: Organization + WebSite (inline on index), Person (founder pages), BreadcrumbList + SoftwareApplication (product pages)
- GA4 `G-XTNRN7YP16` site-wide
- Marketing claims softened to verifiable framing
- Contact form backend: `functions/api/contact.js` (Resend via Pages Function)

## Open items

- **Resend domain verification.** Contact form delivers, but `isn.biz` is not yet verified in Resend, so mail currently lands at the owner Gmail rather than `jdm@isn.biz`. Needs a full-access Resend API key to verify the `isn.biz` domain, then set `CONTACT_TO=jdm@isn.biz` / `CONTACT_FROM` on a verified sender. Env vars (`RESEND_API_KEY`, `CONTACT_TO`, `CONTACT_FROM`) live in the Cloudflare Pages dashboard → Settings → Environment variables.
- **CSP header absent.** `_headers` has X-Frame-Options, X-Content-Type-Options, Referrer-Policy, Permissions-Policy, and cache headers — but no Content-Security-Policy yet.
- **CI flakiness.** Playwright runs have shown intermittent flakiness around the Spirit Atlas page; watch the GitHub Actions run on push.
- **From CLAUDE.md open tasks:** GA4 is done; contact backend is wired (pending Resend verification above).

## Run / test / deploy

```bash
node scripts/preview-server.js                          # local preview on :8080
BASE_URL=http://localhost:8080 npx playwright test       # test against local
BASE_URL=https://isn.biz npx playwright test             # test against prod
git push origin main                                     # CI: tests -> wrangler deploy
```

- Tests: `tests/site-audit.spec.js` (parameterized across all pages; ~111 runtime tests from 11 test blocks). `tests/visual-workflow.spec.js` covers `tools/` asset tooling.
- Playwright `baseURL` defaults to `http://localhost:8080`; override with `BASE_URL`.
- CI (`.github/workflows/auto-deploy.yml`) stages only static site files (large sibling dirs like `hrocincorg/` exceed CF per-file limits), then `wrangler pages deploy`.

## Pages (19 root + signals/)

Main: index, about, services, portfolio, investors, contact.
Products: spiritatlas, provenance, signals/, phantom-browser, crucible, hermes-aingels.
Founders: jonathan, bri, lilly. Other: hroc-files, privacy, terms, 404.

## Read first next session

- `README.md` — current stack/deploy/test reference
- `functions/api/contact.js` — contact backend + env var contract
- `.github/workflows/auto-deploy.yml` — deploy staging logic
- `CLAUDE.md` — owner-managed project rules
