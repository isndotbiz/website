---
status: pending
priority: p2
issue_id: "001"
tags: [security, xss, hero-slider, javascript]
dependencies: []
---

# Unescaped `slide.loading` field in innerHTML write

## Problem Statement

`js/hero-slider.js` applies `escapeHtml()` to every slide data field before inserting into DOM via `innerHTML` — except `slide.loading`. This field is written directly into an HTML attribute without sanitization, creating a latent XSS injection path if any future slide record sets `loading` to a malicious string.

## Findings

**File:** `js/hero-slider.js`

Line 24 computes the loading value:
```js
const loading = slide.loading || (index === 0 ? 'eager' : 'lazy');
```

Lines 46 and 52 insert it directly:
```js
loading="${loading}"
```

Every other dynamic field (`title`, `caption`, `alt`, `src`, `wideSrc`, `placeholder`, `id`, companions) is routed through `escapeHtml()`. `loading` is the sole exception.

**Current risk:** The data file only sets `loading: 'eager'` on slide 1 (line 11 of `spiritatlas-slider-data.js`). All other slides omit the field, falling back to the hardcoded safe string `'lazy'`. No active exploit exists today.

**Latent risk:** A future slide record with `loading: 'lazy" onerror="alert(1)'` would execute arbitrary JS.

## Proposed Solutions

### Option A — Apply escapeHtml to the computed loading value (Recommended)
```js
const loading = escapeHtml(slide.loading || (index === 0 ? 'eager' : 'lazy'));
```
- Effort: Small (1 line)
- Risk: Zero — `escapeHtml` is already defined and tested in scope

### Option B — Allowlist the loading attribute value
```js
const rawLoading = slide.loading || (index === 0 ? 'eager' : 'lazy');
const loading = ['eager', 'lazy', 'auto'].includes(rawLoading) ? rawLoading : 'lazy';
```
- Effort: Small (3 lines)
- Risk: Zero — validates against the HTML spec values for `loading`

## Acceptance Criteria

- [ ] `slide.loading` is escaped or allowlisted before `innerHTML` insertion
- [ ] All other slide fields continue to use `escapeHtml()`

## Work Log

### 2026-03-07 — Code Review Finding

**By:** Claude Code (security-sentinel agent)

**Actions:**
- Identified gap during security audit of commit 1484a3e
- Confirmed all other fields use escapeHtml(); `loading` is the sole exception
- Verified current data file poses no active exploit risk

**Learnings:**
- The escaping pattern is consistently applied everywhere else; this is an oversight rather than a design decision
