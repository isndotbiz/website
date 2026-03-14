---
status: pending
priority: p3
issue_id: "010"
tags: [cleanup, html, alicia, jonathan]
dependencies: []
---

# Double blank lines in alicia.html and jonathan.html after bio-row removal

## Problem Statement

After removing the last 2 bio-row sections from both pages, a double blank line remains inside `.founder-bio > .container` before the closing `</div>`. Cosmetic only, no rendering effect, but it's a remnant of the removal.

## Findings

**`alicia.html` lines 561–562:** Double blank line after the closing `</div>` of bio-row 2 ("The Solution Architect") before the container's closing `</div>`.

**`jonathan.html` lines 577–578:** Same pattern — double blank line after bio-row 2 ("Portfolio Coherence and Platform Depth") before the container's closing `</div>`.

## Proposed Solutions

### Option A — Remove one blank line from each file (Recommended)
Change double blank to single blank in both files.
- Effort: 2 line deletions

## Acceptance Criteria

- [ ] Single blank line between last bio-row closing tag and container closing div in `alicia.html`
- [ ] Same in `jonathan.html`

## Work Log

### 2026-03-07 — Code Review Finding

**By:** Claude Code (code-simplicity-reviewer agent)
