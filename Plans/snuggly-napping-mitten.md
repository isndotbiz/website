# HROC Website Redesign: "Electric Tide" Dark → "Warm Earth" Light

## Context

The HROC (Healing Roots Outreach Collective) website currently uses a dark cyberpunk "Electric Tide" theme — neon cyan/mint on pitch-black backgrounds. This is tonally wrong for a harm reduction nonprofit serving Indigenous communities. Jonathan wants a lighter theme with softer fonts, incorporating award-winning web design techniques from 2023-2026.

The HTML structure, grid layouts, responsive breakpoints, and animation system are all excellent and stay untouched. **The entire transformation is a visual-layer swap** — CSS custom properties, ~10 hardcoded color overrides, a font change, and minor JS/HTML enhancements.

---

## Files Modified

| File | Change Scope |
|------|-------------|
| `HROC_Website_New/styles.css` | `:root` token swap + ~10 hardcoded color overrides + new CSS blocks |
| `HROC_Website_New/script.js` | Add scroll-aware header (~15 lines) |
| `HROC_Website_New/index.html` | Font URL, LCP preload, image attrs, cache bust |
| `HROC_Website_New/bri.html` | Font URL, image attrs, cache bust |
| `HROC_Website_New/lilly.html` | Font URL, image attrs, cache bust |
| `HROC_Website_New/jonathan.html` | Font URL, image attrs, cache bust |
| `HROC_Website_New/documents.html` | Font URL, cache bust |

---

## Step 1 — CSS Token Swap (`:root` variables)

Replace all `:root` color/shadow/glow variables. The variable NAMES stay the same so every downstream reference works automatically.

### New Palette: "Warm Earth"

| Token | Old (Electric Tide) | New (Warm Earth) |
|-------|-------------------|-----------------|
| `--bg-deep` | `#0A0E14` | `#FAFAF8` (warm off-white) |
| `--bg-surface` | `#111820` | `#F4F1EB` (parchment) |
| `--bg-elevated` | `#182028` | `#EDE9E0` (deeper warm) |
| `--bg-card` | `#1C2530` | `#FFFFFF` (white cards) |
| `--bg-glass` | `rgba(24,32,40,0.78)` | `rgba(255,255,255,0.82)` |
| `--cyan` | `#00E8FF` | `#2D6A4F` (forest green) |
| `--cyan-bright` | `#44F0FF` | `#1B4332` (deep forest) |
| `--cyan-dim` | `#00B8CC` | `#52796F` (sage) |
| `--mint` | `#00F7B5` | `#D4845A` (terracotta) |
| `--mint-bright` | `#33FFD0` | `#BF6A44` (deep terracotta) |
| `--mint-dim` | `#00C48E` | `#C8956C` (warm amber) |
| `--crisis` | `#FF3B5C` | `#C0392B` (warm red, still urgent) |
| `--crisis-bright` | `#FF5C7A` | `#E74C3C` |
| `--text-primary` | `#E8F4F8` | `#1C1510` (near-black warm) |
| `--text-secondary` | `#8BA4B0` | `#5C4A3A` (warm brown) |
| `--text-muted` | `#709098` | `#8A7060` (taupe) |
| `--line` | `rgba(0,232,255,0.08)` | `rgba(44,82,52,0.10)` |
| `--line-strong` | `rgba(0,232,255,0.16)` | `rgba(44,82,52,0.18)` |
| Shadows | `rgba(0,0,0,0.4-0.5)` | `rgba(28,21,16,0.08-0.12)` (soft warm) |
| Glows | neon `rgba(0,232,255,...)` | muted `rgba(45,106,79,...)` |

### Font variable change
- `--font-body`: `"DM Sans"` → `"Inter"` (softer, variable, award-standard)
- `--font-display`: `"Fraunces"` stays (already trendy for editorial/nonprofit)

---

## Step 2 — Hardcoded Color Overrides (~10 spots)

These reference raw rgba values, not tokens:

1. **`body::before` atmosphere gradients** — swap cyan/mint rgba to forest green/terracotta
2. **`.topline` header bg** (line ~205) — `rgba(10,14,20,0.92)` → `rgba(250,250,248,0.92)`
3. **Mobile nav bg** (line ~1247) — same dark→light swap
4. **`.eyebrow::before` dot glow** — cyan ring → forest green ring
5. **`.button-ghost:hover` bg** — cyan tint → forest green tint
6. **`.service-card::after` orb** — mint neon → terracotta glow
7. **`.page-hero-portrait::before` glow** — cyan → forest green
8. **Hero h1 mobile override** (line ~1260) — `-webkit-text-fill-color: var(--text-primary)` already uses token, fine
9. **Image filters** — add `sepia(0.08)` for warm cast on all images (interim until new photos)
10. **Crisis strip `.crisis-strip` border** — update rgba to match new crisis red

---

## Step 3 — New CSS Additions (Award-Winning Touches)

Add before the responsive section:

1. **Scroll-aware header classes** — `.topline.is-hidden { transform: translateY(-100%); }`
2. **Nav link sliding underline** — `::after` pseudo-element with `scaleX()` transition
3. **Global `:focus-visible`** — `2px solid var(--cyan)` outline with offset
4. **Card hover enhancement** — already exists via tokens, just verify shadows look right on light bg

---

## Step 4 — script.js: Scroll-Aware Header

Add ~15 lines after IntersectionObserver setup:
- Track `window.scrollY` direction
- Toggle `.is-hidden` on `.topline`
- 80px threshold before hiding activates
- `{ passive: true }` for performance

**Note:** This hides the crisis strip too when scrolling down. The phone number is also in contact section and footer. Flag if this is a concern.

---

## Step 5 — HTML Updates (All 5 Files)

1. **Google Fonts URL** — Replace DM Sans with Inter variable:
   ```
   Inter:wght@300..700&family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600;9..144,700&display=swap
   ```

2. **LCP preload** (index.html only) — `<link rel="preload">` for hero image

3. **Image attributes** — `loading="lazy" decoding="async"` on below-fold images, `width`/`height` where possible

4. **Cache bust** — `?v=20260329-ember` → `?v=20260408-earth` in all 5 files

---

## Step 6 — Image Warm-Up (Interim)

Add `sepia(0.08)` to the existing image filter rule to warm all community photos until new images are generated. New image generation is a separate follow-up task.

---

## What Does NOT Change

- HTML structure, class names, semantic markup
- Grid layouts, spacing scale, responsive breakpoints (1040px, 760px)
- Crisis strip stays red (safety element)
- IntersectionObserver animation system
- Document search, mailto form handler
- Netlify config, deployment pipeline
- `prefers-reduced-motion` support

---

## Verification

1. `python -m http.server 8000` in `HROC_Website_New/` — visual check all 5 pages
2. Verify light theme renders: off-white bg, forest green accents, terracotta secondary
3. Verify Inter font loads (check Network tab for `fonts.googleapis.com`)
4. Verify scroll-aware header hides/shows on scroll
5. Verify mobile menu still works (760px breakpoint)
6. Verify crisis strip stays visible at page top, red and urgent
7. Verify document search still filters
8. Verify reduced motion preference respected
9. Git push → Netlify auto-deploy → check https://hrocinc.org live

---

## Downsides / Risks

- **Image mismatch:** Current AI-generated photos were shot with cool/dark tone. The `sepia(0.08)` filter is a stopgap — new warmer photos should be generated
- **Crisis strip on light:** Red on warm off-white has slightly less contrast than red on black. Still WCAG AA compliant (C0392B on FAFAF8 = 5.2:1 ratio)
- **Font weight shift:** Inter renders slightly thinner than DM Sans at same weight. May need weight bumps on some elements after visual QA
- **Cache risk:** Users with cached CSS may see dark theme until cache expires or version param propagates
