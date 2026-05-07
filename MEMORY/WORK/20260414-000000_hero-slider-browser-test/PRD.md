---
task: Test hero slider navigation and visual state
slug: 20260414-000000_hero-slider-browser-test
effort: standard
phase: complete
progress: 8/8
mode: interactive
started: 2026-04-14T00:00:00Z
updated: 2026-04-14T00:00:01Z
---

## Context

Browser automation test of the ISN.BIZ hero slider at localhost:8000. Task requires navigating to the page, scrolling to the hero slider, screenshotting initial state, advancing slides via right arrow (2x), jumping via dot click (to slide 5), and reporting on transition quality, 3-phone layout persistence, caption updates, active dot correctness, and any visual glitches or broken images.

### Risks
- Slider section may not be visible without scroll
- Arrow/dot element refs may not be obvious in accessibility tree
- Local server must be running on port 8000
- Dot numbering may be 0-indexed vs 1-indexed

## Criteria

- [x] ISC-1: Screenshot of initial slider state captured and saved
- [x] ISC-2: Right arrow click advances from slide 1 to slide 2
- [x] ISC-3: Screenshot of slide 2 captured and saved
- [x] ISC-4: Right arrow click advances from slide 2 to slide 3
- [x] ISC-5: Screenshot of slide 3 captured and saved
- [x] ISC-6: 5th dot click jumps to slide 5
- [x] ISC-7: Screenshot of slide 5 captured and saved
- [x] ISC-8: Report on transitions, 3-phone layout, captions, dots, glitches produced

## Decisions

## Verification
