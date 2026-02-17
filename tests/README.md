# Website Fixes - Playwright Test Suite

## Overview

This test suite verifies all fixes made to the ISN.BIZ website:

1. **Team Name Corrections** - All founder names show correctly
2. **Services Page Images** - All images load without 403 errors
3. **Hero Slider Auto-Advance** - Slider automatically cycles through slides
4. **Founder Page Images** - No duplicate images on any founder page
5. **Visual Regression** - Screenshot comparison for key pages

## Quick Start

### Install Dependencies

```bash
npm install --save-dev @playwright/test
npx playwright install
```

### Run Tests

```bash
# Run all tests
npx playwright test

# Run specific test file
npx playwright test website-fixes-verification.spec.js

# Run tests in headed mode (see browser)
npx playwright test --headed

# Run tests in debug mode
npx playwright test --debug

# Generate HTML report
npx playwright show-report
```

### Run Tests with Local Server

The tests will automatically start a local Python HTTP server on port 8000. If you prefer to use your own server:

```bash
# Terminal 1: Start your server
python -m http.server 8000

# Terminal 2: Run tests
BASE_URL=http://localhost:8000 npx playwright test
```

## Test Structure

### Team Name Corrections
- ✅ Verifies navigation dropdown shows correct names
- ✅ Verifies team section shows correct names
- ✅ Verifies Schema.org JSON-LD has correct founder name

### Services Page Images
- ✅ All 3 visual proof images load successfully (no 403 errors)
- ✅ Images have proper alt text
- ✅ No broken image paths

### Hero Slider
- ✅ Auto-advances after 7 seconds
- ✅ Pauses on hover
- ✅ Shows pause/play button
- ✅ Progress bar updates during auto-advance
- ✅ Keyboard navigation works (arrow keys)

### Founder Pages
- ✅ Jonathan's page has no duplicate images
- ✅ All founder pages load without image errors
- ✅ Each founder has unique portrait image

### Visual Regression
- Screenshots captured for all key pages
- Can be used for before/after comparison
- Stored in `tests/screenshots/`

## Expected Results

All tests should **PASS** after fixes are applied:

```
✓ Team Name Corrections (4 tests)
✓ Services Page Images (2 tests)
✓ Hero Slider Auto-Advance (4 tests)
✓ Founder Page Images (3 tests)
✓ Visual Regression - Screenshots (4 tests)
✓ Accessibility Checks (2 tests)

Total: 19 tests passed
```

## Screenshots

Generated screenshots:
- `homepage-fixed.png` - Full homepage
- `team-section-fixed.png` - Team section with correct names
- `services-page-fixed.png` - Services page with working images
- `services-page-images-fixed.png` - Close-up of service visual grid
- `jonathan-page-fixed.png` - Jonathan's page (no duplicates)
- `lilly-page-fixed.png` - Lilly's page
- `bri-page-fixed.png` - Bri's page
- `alicia-page-fixed.png` - Alicia's page

## Troubleshooting

### Tests Fail with "Connection Refused"
- Make sure the web server is running on port 8000
- Check if another service is using port 8000
- Try a different port: `BASE_URL=http://localhost:3000 npx playwright test`

### Image Load Tests Fail
- Check internet connection (S3 bucket images require network access)
- Verify S3 bucket permissions haven't changed
- Check if CloudFront/CDN is working

### Slider Tests Fail
- Increase timeout values if on slow connection
- Check browser console for JavaScript errors
- Verify `hero-slider.js` loaded correctly

## CI/CD Integration

### GitHub Actions Example

```yaml
name: Playwright Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: 18
      - name: Install dependencies
        run: npm ci
      - name: Install Playwright Browsers
        run: npx playwright install --with-deps
      - name: Run Playwright tests
        run: npx playwright test
      - uses: actions/upload-artifact@v3
        if: always()
        with:
          name: playwright-report
          path: playwright-report/
          retention-days: 30
```

## Manual Verification Checklist

Even with automated tests, verify manually:

- [ ] Navigate to isn.biz and check team dropdown shows: Mallinger, Fedas, Bear, Haas
- [ ] Visit services.html and confirm all 3 images load (no broken icons)
- [ ] Watch homepage slider for 10 seconds - should auto-advance
- [ ] Visit jonathan.html - scroll through page, no repeated images
- [ ] Visit lilly.html, bri.html, alicia.html - all images load

## Future Enhancements

Potential additions to test suite:
- Performance testing (Lighthouse integration)
- Mobile responsiveness tests
- Cross-browser visual comparison
- Link checker (all links work)
- SEO meta tag validation
- Form submission testing
