---
status: pending
priority: p2
issue_id: "006"
tags: [ux, javascript, hero-slider, accessibility]
dependencies: []
---

# Autoplay permanently killed after any prev/next click; Play button becomes non-functional

## Problem Statement

After a user clicks the prev or next navigation button, `userInteracted` is set to `true` and autoplay is permanently disabled — even if the user then clicks the "Play" button. The `userInteracted` flag is checked inside `restartAutoPlay` and causes it to return early, meaning the Play button has no effect after any nav click. The progress bar also sits at 0% indefinitely.

## Findings

**File:** `js/hero-slider.js`

Lines 201–204 (prev/next click handlers):
```js
userInteracted = true;         // permanently kills autoplay
updateSlider(currentIndex - 1);
restartAutoPlay();             // returns immediately due to userInteracted check
```

Lines 155–166 (`restartAutoPlay`):
```js
const restartAutoPlay = () => {
    clearAutoPlay();
    if (isPaused || userInteracted || totalSlides < 2) return;  // ← early return
    // ...
};
```

Lines 200–211 (toggle button correctly manages `isPaused`):
```js
isPaused = !isPaused;
userInteracted = isPaused;   // sets userInteracted = false when unpausing
```

But after a nav click, `userInteracted` is `true` and `isPaused` is still `false`. Clicking Play sets `isPaused = false` but does NOT reset `userInteracted`, so `restartAutoPlay` still returns early. The Play button appears to toggle its label but does nothing.

## Proposed Solutions

### Option A — Remove `userInteracted` from `restartAutoPlay` guard; use only `isPaused` (Recommended)
```js
const restartAutoPlay = () => {
    clearAutoPlay();
    if (isPaused || totalSlides < 2) return;  // remove userInteracted check
    // ...
};
```
Nav clicks reset the timer for the next slide and autoplay continues. Permanent pause is still possible via the Pause/Play toggle which manages `isPaused`.
- Effort: Small (1 line change)
- Aligns with standard carousel UX: user interaction resets timer, doesn't kill it

### Option B — Reset `userInteracted` to `false` in the Play toggle handler
Keep the guard as-is, but add `userInteracted = false` when the user clicks Play.
- Effort: Small (1 line)
- Preserves current "nav kills autoplay" behavior but makes Play actually work

## Acceptance Criteria

- [ ] Clicking prev/next restarts the autoplay timer (does not permanently kill it)
- [ ] Clicking "Pause" stops autoplay; clicking "Play" resumes it
- [ ] Progress bar animates correctly after both nav clicks and Play clicks

## Work Log

### 2026-03-07 — Code Review Finding

**By:** Claude Code (architecture-strategist agent)
