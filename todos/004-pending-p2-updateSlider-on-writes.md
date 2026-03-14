---
status: pending
priority: p2
issue_id: "004"
tags: [performance, javascript, hero-slider, dom]
dependencies: []
---

# `updateSlider` does O(n) DOM writes across all slides on every transition

## Problem Statement

Every slide transition iterates all 42 slides and all 42 dots, making 84 synchronous DOM writes per transition. The correct pattern is to track the previously active index and toggle only the 2 elements that change (deactivate old, activate new) — 4 DOM writes regardless of slide count.

At 12 slides this was 24 DOM writes per transition. At 42 slides it is 84. Scaling to 60+ slides (signalled as likely in the data file comment) worsens this linearly.

## Findings

**File:** `js/hero-slider.js:171–182`

```js
slides.forEach((slide, slideIndex) => {
    const isActive = slideIndex === normalizedIndex;
    slide.classList.toggle('active', isActive);
    slide.setAttribute('aria-selected', String(isActive));
    slide.setAttribute('tabindex', isActive ? '0' : '-1');
});

dots.forEach((dot, dotIndex) => {
    const isActive = dotIndex === normalizedIndex;
    dot.classList.toggle('active', isActive);
    dot.setAttribute('aria-current', String(isActive));
});
```

Each `setAttribute` and `classList.toggle` can trigger a style recalculation. Writing all 42 at once is 21x more DOM writes than necessary.

## Proposed Solutions

### Option A — Track previous index, toggle only changed elements (Recommended)
```js
let prevIndex = 0; // add to initHeroSlider scope

const updateSlider = (index) => {
    const normalizedIndex = ((index % totalSlides) + totalSlides) % totalSlides;

    // Deactivate previous
    slides[prevIndex].classList.remove('active');
    slides[prevIndex].setAttribute('aria-selected', 'false');
    slides[prevIndex].setAttribute('tabindex', '-1');
    dots[prevIndex].classList.remove('active');
    dots[prevIndex].setAttribute('aria-current', 'false');

    // Activate new
    slides[normalizedIndex].classList.add('active');
    slides[normalizedIndex].setAttribute('aria-selected', 'true');
    slides[normalizedIndex].setAttribute('tabindex', '0');
    dots[normalizedIndex].classList.add('active');
    dots[normalizedIndex].setAttribute('aria-current', 'true');

    prevIndex = normalizedIndex;
    // ... rest of function unchanged
};
```
- Effort: Small (refactor ~15 lines)
- Impact: Reduces DOM writes from O(n) to O(1) per transition

## Acceptance Criteria

- [ ] `updateSlider` no longer iterates all slides/dots on each call
- [ ] Active/inactive states are visually identical to before
- [ ] ARIA attributes (`aria-selected`, `aria-current`, `tabindex`) are correctly toggled

## Work Log

### 2026-03-07 — Code Review Finding

**By:** Claude Code (performance-oracle agent)
