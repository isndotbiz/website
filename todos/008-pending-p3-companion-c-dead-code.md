---
status: pending
priority: p3
issue_id: "008"
tags: [cleanup, javascript, hero-slider, dead-code]
dependencies: []
---

# `companionC` dead code — computed per slide, never rendered

## Problem Statement

`companionC` and its three derived variables are computed for every slide during `buildSlideMarkup` but are never referenced in the returned HTML template. Dead computation + misleading surface area for future developers.

## Findings

**File:** `js/hero-slider.js`

Line 22:
```js
const companionC = slidesConfig[(index + 3) % slidesConfig.length];
```

Lines 37–39:
```js
const companionCSrc = companionC?.src ? escapeHtml(companionC.src) : '';
const companionCAlt = escapeHtml(companionC?.alt || companionC?.title || 'SpiritAtlas companion screenshot');
const companionCTitle = escapeHtml(companionC?.title || 'Next spiritual screen');
```

None of `companionCSrc`, `companionCAlt`, or `companionCTitle` appear in the template string (lines 41–83). The phone-strip layout renders only `companionA` and `companionB`.

4 string allocations × 42 slides = 168 unnecessary string objects at initialization.

## Proposed Solutions

### Option A — Delete lines 22 and 37–39 (Recommended)
If a third companion card is planned, add it to the template at the same time. Do not leave unused computed variables.
- Effort: Small (delete 4 lines)

### Option B — Add a third companion card to the phone strip
If the design calls for three companion cards, implement lines 37–39 into the template and add a third `<figure class="slide-phone-card">` at line ~66.
- Effort: Small–Medium (implement + test the layout)

## Acceptance Criteria

- [ ] No unused variables in `buildSlideMarkup`
- [ ] Slider renders identically to before

## Work Log

### 2026-03-07 — Code Review Finding

**By:** Claude Code (performance-oracle + architecture-strategist agents)
