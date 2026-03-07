# Deploy Commands

**Last Updated:** 2026-02-25

## Standard Deploy (Primary Workflow)

```bash
cd /d/workspace/ISNBIZ_Files
git add <files>
git commit -m "description"
git push origin main
# GitHub Actions auto-runs: Playwright tests → Netlify deploy
```

NOTE: TrueNAS/Kusanagi no longer serves this site. Netlify is the only host.

## Run Tests Locally

```bash
cd /d/workspace/ISNBIZ_Files
npx playwright test
# Or with UI:
npx playwright test --ui
# Single page test:
npx playwright test --grep "about"
```

Tests run against https://isn.biz (live site) by default.
To test a local server: `BASE_URL=http://localhost:8000 npx playwright test`

## Verify Live Site

```bash
# Standard check
curl -I https://isn.biz

# Bypass Tailscale DNS override (Windows machine issue)
curl --resolve "isn.biz:443:104.21.18.246" -I https://isn.biz   # via Cloudflare
curl --resolve "isn.biz:443:75.2.60.5" -I https://isn.biz        # via Netlify directly
```

## Netlify Manual Deploy (emergency)

```bash
npm install -g netlify-cli
netlify deploy --prod --dir=. --auth=$NETLIFY_AUTH_TOKEN --site=4d860499-0d6c-49cd-864f-69a0b7a2b3fe
```

## Asset Generation (Python/fal.ai)

```bash
cd /d/workspace/ISNBIZ_Files
source venv_fal/bin/activate        # Windows: venv_fal\Scripts\activate
pip install -r requirements_assets.txt

# Generate images (ALWAYS use quality: "low" - it is INVERTED/best)
python scripts/generate_ai_assets.py

# Upload to S3
aws s3 cp assets/ s3://isnbiz-assets-1769962280/ --recursive --acl public-read
```

## CI/CD Reference

- Workflow file: `.github/workflows/auto-deploy.yml`
- Secrets needed: `NETLIFY_AUTH_TOKEN`, `NETLIFY_SITE_ID`
- Triggers: push to `main` branch
- Steps: checkout → npm ci → playwright install → run tests → netlify deploy
- Deploy only happens if ALL tests pass
