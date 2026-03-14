---
status: pending
priority: p2
issue_id: "007"
tags: [deployment, caching, netlify, security]
dependencies: []
---

# `immutable` cache directive on unhashed JS filename causes stale content after deploys

## Problem Statement

`netlify.toml` sets `Cache-Control: public, max-age=31536000, immutable` on all `/*.js` files. The slider data file is served at a stable filename (`/js/spiritatlas-slider-data.js`) with no content hash in the URL. `immutable` tells browsers and CDN edges to never revalidate. Users who cached the old 12-slide version of the file before this deploy may see stale slide data for up to a year.

## Findings

**File:** `netlify.toml:145–148`

```toml
[[headers]]
  for = "/*.js"
  [headers.values]
    Cache-Control = "public, max-age=31536000, immutable"
```

The `immutable` directive is designed for content-addressed filenames (e.g., `app.a3f8c2d.js`). When applied to mutable filenames, it makes it impossible for the browser to detect when the file changes without a hard refresh or cache clear.

This commit directly demonstrates the risk: `spiritatlas-slider-data.js` grew from 12 to 42 slides. Any user who visited the page before this deploy and has the file cached won't see the new slides until their 1-year cache expires.

## Proposed Solutions

### Option A — Add a query-string version to the script tags (Low friction, Recommended)
```html
<script src="js/spiritatlas-slider-data.js?v=20260307" defer></script>
<script src="js/hero-slider.js?v=20260307" defer></script>
```
Update `?v=` on every deploy that changes these files. Browsers treat the URL as distinct and re-fetch.
- Effort: Small per deploy (manual bump of version string in 2 HTML files)
- No build tooling required

### Option B — Lower `max-age` for JS files without content hash
```toml
Cache-Control = "public, max-age=86400"  # 1 day instead of 1 year
```
Remove `immutable` and reduce TTL. Less aggressive but still allows CDN caching.
- Effort: Small (1 line in netlify.toml)
- Drawback: Every visitor re-fetches JS daily even when unchanged

### Option C — Add a Netlify build step that appends a content hash to filenames
- Effort: Large (requires a build pipeline)
- Not warranted for this static site

## Acceptance Criteria

- [ ] Users who had the old 12-slide version cached will receive the new 42-slide version within a reasonable window
- [ ] Cache strategy is documented in netlify.toml comment

## Work Log

### 2026-03-07 — Code Review Finding

**By:** Claude Code (security-sentinel agent)
