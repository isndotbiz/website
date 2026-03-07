---
status: pending
priority: p2
issue_id: "005"
tags: [maintainability, javascript, spiritatlas-slider, simplicity]
dependencies: []
---

# CDN base URL repeated 84 times in slider data file

## Problem Statement

Every `src` and `wideSrc` field in `js/spiritatlas-slider-data.js` hardcodes the full 77-character S3 CDN prefix:
`https://isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com/assets/`

This prefix appears 84 times across the 444-line file. If the bucket name or region ever changes, 84 strings must be updated manually. A single `const CDN` constant at the top of the file makes it a single edit point.

## Findings

**File:** `js/spiritatlas-slider-data.js` — lines 7–443, all `src` and `wideSrc` fields

Example:
```js
src: 'https://isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com/assets/projects/spiritatlas/app/20260213_090332/01_01_home-dashboard.webp',
wideSrc: 'https://isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com/assets/projects/spiritatlas/composites/20260213_wide_v1/01_wide-composite.webp',
```

Additional repetition: the `app/20260213_090332/` folder prefix for the 12 app screenshots is written out 12 times in `src` and another 12 times in `wideSrc`, each time with the full base URL. These are 100% mechanical patterns.

**Estimated reduction:** ~130–160 lines (30–36% of the file) with a CDN constant + named gradient constants.

## Proposed Solutions

### Option A — Extract CDN constant + keep per-slide template literals (Recommended, minimal change)
```js
const CDN = 'https://isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com/assets/';

window.spiritAtlasSliderData = [
    {
        id: 'home-dashboard',
        // ...
        src: `${CDN}projects/spiritatlas/app/20260213_090332/01_01_home-dashboard.webp`,
        wideSrc: `${CDN}projects/spiritatlas/composites/20260213_wide_v1/01_wide-composite.webp`,
    },
    // ...
];
```
- Effort: Medium (find-replace + convert strings to template literals)
- Saves ~60 lines of horizontal noise; zero behavior change
- Single update point for future bucket/region changes

### Option B — CDN constant + APP_FOLDER constant + named gradient constants
```js
const CDN = 'https://isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com/assets/';
const APP_FOLDER = `${CDN}projects/spiritatlas/app/20260213_090332/`;
const COMP_FOLDER = `${CDN}projects/spiritatlas/composites/20260213_wide_v1/`;
const GRAD_DEEP_SPACE = 'linear-gradient(135deg, #0e1b30 0%, #1f4f8f 50%, #6b20a5 100%)';
```
- Effort: Medium-Large (more constants, more refactoring)
- Saves ~160 lines; all future app screenshot batches use `APP_FOLDER` update point

## Acceptance Criteria

- [ ] CDN base URL appears exactly once in the file
- [ ] All 42 `src`/`wideSrc` values correctly resolve to the same S3 URLs as before
- [ ] File passes a simple URL equality test (load in browser, verify image sources unchanged)

## Work Log

### 2026-03-07 — Code Review Finding

**By:** Claude Code (code-simplicity-reviewer agent)
