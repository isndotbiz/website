---
status: pending
priority: p2
issue_id: "002"
tags: [performance, html, scripts, loading]
dependencies: []
---

# Scripts loaded without `defer` — sequential fetch waterfall

## Problem Statement

The three `<script>` tags at the bottom of `spiritatlas.html` and `index.html` have no `defer` attribute. Without `defer`, the browser fetches and executes them sequentially: `script.js` completes before `spiritatlas-slider-data.js` begins, and that must complete before `hero-slider.js` begins. Adding `defer` allows the browser to fetch all three in parallel and execute them in document order after HTML parsing — eliminating the sequential fetch penalty.

Additionally, the required load order (data file before engine) is undocumented. If a developer adds `async` during a future optimization pass, the slider silently breaks because `async` ignores document order.

## Findings

**Files:**
- `spiritatlas.html:862–864`
- `index.html:974–975`

```html
<!-- Current (spiritatlas.html lines 862–864) -->
<script src="script.js"></script>
<script src="js/spiritatlas-slider-data.js"></script>
<script src="js/hero-slider.js"></script>
```

Scripts are already at page bottom (correct), so this doesn't block initial HTML parse. But without `defer`, the browser still downloads + executes them in series once it reaches those tags. The data file at 444 lines is the middle step of a 3-step waterfall.

**Confirmed:** Both `spiritatlas.html` and `index.html` include both the data file and engine file in the correct order.

## Proposed Solutions

### Option A — Add `defer` to all three tags + add a load-order comment (Recommended)
```html
<!-- data file must precede engine; do not reorder or use async -->
<script src="script.js" defer></script>
<script src="js/spiritatlas-slider-data.js" defer></script>
<script src="js/hero-slider.js" defer></script>
```
- Effort: Small (4 lines per page, 2 pages)
- Risk: Low — `defer` preserves document order, so the data-before-engine contract is maintained

### Option B — Use ES modules with static import
Convert to `type="module"`, have `hero-slider.js` explicitly `import` the data. Removes implicit global contract entirely.
- Effort: Medium (refactor both files)
- Risk: Low technically, higher churn

## Acceptance Criteria

- [ ] `defer` added to script tags in `spiritatlas.html` lines 862–864
- [ ] `defer` added to script tags in `index.html` lines 974–975
- [ ] Comment above each pair documents the required load order
- [ ] Verify slider still initializes correctly after change

## Work Log

### 2026-03-07 — Code Review Finding

**By:** Claude Code (performance-oracle + architecture-strategist agents)

**Actions:**
- Identified sequential script fetch waterfall during performance audit
- Confirmed `index.html` includes both script files (architecture agent initially flagged as missing — false positive)
- Identified undocumented `async`-unsafe dependency between data and engine files
