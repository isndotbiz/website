---
status: pending
priority: p3
issue_id: "009"
tags: [content, xss, spiritatlas-slider, javascript]
dependencies: []
---

# Pre-HTML-encoded `&amp;` in slide title double-encodes through `escapeHtml()`

## Problem Statement

`spiritatlas-slider-data.js` line 33 uses `&amp;` in a slide title. When `escapeHtml()` processes it, the `&` in `&amp;` is re-encoded to `&amp;amp;`, so the browser renders `Soul Profiles &amp; Compatibility Sanctum` instead of `Soul Profiles & Compatibility Sanctum`.

## Findings

**File:** `js/spiritatlas-slider-data.js:33`

```js
title: 'Soul Profiles &amp; Compatibility Sanctum',
```

`escapeHtml()` converts `&` → `&amp;`, so the output becomes `Soul Profiles &amp;amp; Compatibility Sanctum`.

The fix is to use the raw character in the data file. The data file is a JS source file, not HTML — raw `&` is correct here and `escapeHtml()` will correctly encode it for HTML output.

## Proposed Solutions

### Option A — Use raw `&` in the data file (Recommended)
```js
title: 'Soul Profiles & Compatibility Sanctum',
```
- Effort: 1 character change

## Acceptance Criteria

- [ ] Slide title renders as `Soul Profiles & Compatibility Sanctum` in the browser
- [ ] No other slide titles in the data file use pre-encoded HTML entities

## Work Log

### 2026-03-07 — Code Review Finding

**By:** Claude Code (security-sentinel agent)
