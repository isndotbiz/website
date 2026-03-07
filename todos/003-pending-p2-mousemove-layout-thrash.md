---
status: pending
priority: p2
issue_id: "003"
tags: [performance, javascript, animation, hero-slider]
dependencies: []
---

# Unthrottled `mousemove` forces `getBoundingClientRect()` reflow on every mouse event

## Problem Statement

The parallax effect on the hero slider calls `getBoundingClientRect()` on every `mousemove` event with no throttle or RAF gate. This forces a layout reflow 60–120 times per second and writes two CSS custom properties per event, which can trigger compositing passes. On a marketing/investor page this is unnecessary CPU cost — particularly on mobile or lower-powered devices.

## Findings

**File:** `js/hero-slider.js:281–288`

```js
slider.addEventListener('mousemove', (event) => {
    if (prefersReducedMotion) return;
    const rect = slider.getBoundingClientRect();  // forces reflow
    const x = ((event.clientX - rect.left) / rect.width) - 0.5;
    const y = ((event.clientY - rect.top) / rect.height) - 0.5;
    slider.style.setProperty('--sa-parallax-x', `${(x * 8).toFixed(2)}px`);
    slider.style.setProperty('--sa-parallax-y', `${(y * 6).toFixed(2)}px`);
});
```

- `getBoundingClientRect()` reads from the layout engine — can invalidate and re-trigger layout if any pending CSS change exists
- Fires 60–120× per second on modern displays with no frame gate
- No `requestAnimationFrame` wrapper, no debounce, no throttle

## Proposed Solutions

### Option A — Gate reads/writes inside a requestAnimationFrame (Recommended)
```js
let rafPending = false;
slider.addEventListener('mousemove', (event) => {
    if (prefersReducedMotion || rafPending) return;
    rafPending = true;
    requestAnimationFrame(() => {
        const rect = slider.getBoundingClientRect();
        const x = ((event.clientX - rect.left) / rect.width) - 0.5;
        const y = ((event.clientY - rect.top) / rect.height) - 0.5;
        slider.style.setProperty('--sa-parallax-x', `${(x * 8).toFixed(2)}px`);
        slider.style.setProperty('--sa-parallax-y', `${(y * 6).toFixed(2)}px`);
        rafPending = false;
    });
});
```
- Effort: Small (5 extra lines)
- Effect: Caps to 1 reflow per animation frame regardless of mouse speed

### Option B — Cache `getBoundingClientRect` on `mouseenter`, reuse in `mousemove`
```js
let cachedRect = null;
slider.addEventListener('mouseenter', () => { cachedRect = slider.getBoundingClientRect(); });
slider.addEventListener('mousemove', (event) => {
    if (prefersReducedMotion || !cachedRect) return;
    const x = ((event.clientX - cachedRect.left) / cachedRect.width) - 0.5;
    // ...
});
slider.addEventListener('mouseleave', () => { cachedRect = null; });
```
- Effort: Small (6 lines + modify existing handlers)
- Eliminates reflow from mousemove entirely; rect is stale if slider resizes mid-hover (acceptable edge case)

## Acceptance Criteria

- [ ] `getBoundingClientRect()` is no longer called synchronously on every `mousemove` event
- [ ] Parallax effect still functions visually
- [ ] `prefersReducedMotion` guard still applies

## Work Log

### 2026-03-07 — Code Review Finding

**By:** Claude Code (performance-oracle agent)
