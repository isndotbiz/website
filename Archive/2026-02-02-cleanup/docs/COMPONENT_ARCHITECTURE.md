# Component Architecture - isn.biz Video & Slider System

## System Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                     isn.biz Website Stack                        │
├─────────────────────────────────────────────────────────────────┤
│  Frontend Layer                                                  │
│  ├── HTML5 (Semantic, Accessible)                               │
│  ├── CSS3 (Custom Properties, Grid, Flexbox)                    │
│  └── JavaScript (ES6+, Async/Await)                             │
├─────────────────────────────────────────────────────────────────┤
│  Component Libraries (CDN)                                       │
│  ├── Swiper.js v11      → Carousels & Sliders                  │
│  ├── Plyr v3.7.8        → Video Player                          │
│  ├── AOS v2.3.1         → Scroll Animations                     │
│  ├── GSAP v3.12.5       → Advanced Animations                   │
│  ├── ScrollTrigger      → Scroll-based Triggers                 │
│  └── Lottie v5.12.2     → JSON Animations                       │
├─────────────────────────────────────────────────────────────────┤
│  Video Assets (AI-Generated)                                    │
│  ├── Runway Gen-3       → Hero Backgrounds                      │
│  ├── Synthesia          → Testimonial Avatars (Optional)        │
│  └── D-ID               → Avatar Videos (Optional)              │
├─────────────────────────────────────────────────────────────────┤
│  Performance Layer                                               │
│  ├── Lazy Loading       → Images & Videos                       │
│  ├── Intersection Observer → Scroll Triggers                    │
│  ├── Throttle/Debounce  → Event Optimization                    │
│  └── CDN Delivery       → Fast Asset Loading                    │
├─────────────────────────────────────────────────────────────────┤
│  Accessibility Layer (WCAG 2.2)                                 │
│  ├── ARIA Labels        → Screen Reader Support                 │
│  ├── Keyboard Nav       → Full Keyboard Control                 │
│  ├── Captions           → Video Accessibility                   │
│  ├── Focus Management   → Visual Focus Indicators               │
│  └── Reduced Motion     → Respects User Preferences             │
└─────────────────────────────────────────────────────────────────┘
```

---

## Component Hierarchy

```
Page Structure
│
├── 1. Hero Video Background (Full Viewport)
│   ├── Video Layer (Background)
│   │   ├── MP4 Source (Primary)
│   │   ├── WebM Source (Fallback)
│   │   └── Poster Image (Mobile/No-JS)
│   ├── Gradient Overlay
│   ├── Content Layer (Foreground)
│   │   ├── Logo
│   │   ├── Title & Subtitle
│   │   └── CTA Buttons
│   ├── Video Controls (Accessibility)
│   └── Scroll Indicator
│
├── 2. Animated Statistics Section
│   ├── Section Header
│   ├── Stats Grid (4 columns → responsive)
│   │   └── Stat Card × 4
│   │       ├── Icon (SVG)
│   │       ├── Number (Animated Counter)
│   │       ├── Suffix (+, %, etc.)
│   │       ├── Label
│   │       └── Description
│   └── Intersection Observer (Trigger)
│
├── 3. Testimonial Slider
│   ├── Section Header
│   ├── Swiper Container
│   │   ├── Swiper Wrapper
│   │   │   └── Testimonial Slide × N
│   │   │       ├── Quote Icon
│   │   │       ├── Testimonial Text
│   │   │       ├── Author Info
│   │   │       │   ├── Avatar Image
│   │   │       │   ├── Name
│   │   │       │   └── Role/Company
│   │   │       └── Star Rating
│   │   ├── Navigation (Prev/Next)
│   │   ├── Pagination (Bullets)
│   │   └── Autoplay Controls (Play/Pause)
│
├── 4. Portfolio Carousel
│   ├── Section Header
│   ├── Swiper Container
│   │   ├── Swiper Wrapper
│   │   │   └── Portfolio Slide × N
│   │   │       ├── Project Image (Lazy Load)
│   │   │       ├── Hover Overlay
│   │   │       ├── Project Content
│   │   │       │   ├── Number
│   │   │       │   ├── Title
│   │   │       │   ├── Description
│   │   │       │   ├── Tags
│   │   │       │   └── Metrics Grid
│   │   │       └── View Details Button
│   │   ├── Navigation (Prev/Next)
│   │   └── Pagination
│
├── 5. Video Showcase (Plyr)
│   ├── Section Header
│   ├── Video Player Wrapper
│   │   └── Plyr Video Element
│   │       ├── Video Sources (MP4, WebM)
│   │       ├── Captions Track (.vtt)
│   │       └── Poster Image
│   └── Video Description
│       ├── Title
│       ├── Description
│       ├── Feature List
│       └── CTA Button
│
├── 6. Parallax Section
│   ├── Parallax Layer (Background)
│   │   └── Animated Shapes × 3
│   ├── Parallax Content (Middle)
│   │   ├── Label
│   │   ├── Title
│   │   ├── Description
│   │   └── CTA Button
│   └── Parallax Layer (Foreground)
│       └── Animated Shapes × 2
│
└── 7. Loading Animation (Initial)
    ├── Loading Container
    │   ├── Lottie Animation (Primary)
    │   ├── Fallback Spinner (No Lottie)
    │   ├── Loading Text
    │   └── Progress Bar
    └── Auto-hide on Load Complete
```

---

## Data Flow

```
User Interaction → Event Handler → Component Logic → Animation/Update
     │                  │                 │                  │
     │                  │                 │                  │
     v                  v                 v                  v
┌─────────┐      ┌──────────┐     ┌───────────┐     ┌──────────┐
│ Click   │─────→│ Button   │────→│ Swiper    │────→│ Slide    │
│ Scroll  │      │ Listener │     │ API       │     │ Change   │
│ Hover   │      │          │     │           │     │          │
└─────────┘      └──────────┘     └───────────┘     └──────────┘
                                          │
                                          v
                                  ┌───────────────┐
                                  │ Analytics     │
                                  │ Tracking      │
                                  │ (Google GA4)  │
                                  └───────────────┘
```

---

## Scroll Trigger Flow

```
Page Scroll
    │
    v
┌────────────────────────────────────┐
│  Intersection Observer API         │
│  (Detects element visibility)      │
└────────────────────────────────────┘
    │
    v
┌────────────────────────────────────┐
│  Is Element 50% Visible?           │
└────────────────────────────────────┘
    │
    ├── Yes ──→ Trigger Animation
    │           │
    │           v
    │       ┌──────────────────────┐
    │       │  AOS: Fade/Slide In  │
    │       │  GSAP: Count Up      │
    │       │  Custom: Video Play  │
    │       └──────────────────────┘
    │           │
    │           v
    │       Unobserve Element
    │       (Prevent Re-trigger)
    │
    └── No ──→ Continue Monitoring
```

---

## Video Loading Strategy

```
Page Load
    │
    v
┌────────────────────────────────────┐
│  Device Detection                  │
└────────────────────────────────────┘
    │
    ├── Desktop (> 768px)
    │   │
    │   v
    │   ┌──────────────────────────┐
    │   │  Load Video Element      │
    │   │  Set poster attribute    │
    │   │  Preload: metadata only  │
    │   └──────────────────────────┘
    │   │
    │   v
    │   ┌──────────────────────────┐
    │   │  User Scrolls Near Video │
    │   │  (Intersection Observer) │
    │   └──────────────────────────┘
    │   │
    │   v
    │   ┌──────────────────────────┐
    │   │  Load Full Video         │
    │   │  Autoplay (if allowed)   │
    │   └──────────────────────────┘
    │
    └── Mobile (≤ 768px)
        │
        v
        ┌──────────────────────────┐
        │  Show Poster Image Only  │
        │  (No video element)      │
        │  Save Bandwidth          │
        └──────────────────────────┘
```

---

## Swiper.js Integration Pattern

```javascript
// Initialization Flow
Document Ready
    │
    v
Create Swiper Instance
    │
    ├── Configuration Object
    │   ├── Slides per view (responsive)
    │   ├── Space between slides
    │   ├── Loop mode
    │   ├── Autoplay settings
    │   ├── Pagination config
    │   ├── Navigation config
    │   └── Accessibility (a11y)
    │
    v
Swiper API Available
    │
    ├── .slideNext() ─→ Manual navigation
    ├── .slidePrev()
    ├── .autoplay.start() ─→ Control autoplay
    ├── .autoplay.stop()
    └── .on('slideChange') ─→ Event listeners
```

---

## Animation Timeline (GSAP)

```
Scroll Position: 0px (Top of Page)
    │
    v  [Hero Section]
    │  ├── Video opacity: 1
    │  └── Overlay opacity: 0.95
    │
    v  Scroll: 0-800px
    │  ├── Video scales up
    │  └── Overlay darkens
    │
    v  [Stats Section Enters Viewport]
    │  ├── Trigger: top 70%
    │  └── Action: Fade in + Count up
    │
    v  [Parallax Section]
    │  ├── Background: moves slow (0.5x)
    │  ├── Content: normal speed (1x)
    │  └── Foreground: moves fast (1.5x)
    │
    v  Scroll: Bottom of Page
        └── All animations complete
```

---

## State Management

```javascript
// Component States
const state = {
    // Video
    heroVideo: {
        isPlaying: true,
        volume: 0, // Always muted for autoplay
        currentTime: 0
    },

    // Sliders
    testimonialSlider: {
        activeIndex: 0,
        autoplayEnabled: true,
        totalSlides: 4
    },

    portfolioCarousel: {
        activeIndex: 0,
        autoplayEnabled: true,
        totalSlides: 4
    },

    // Animations
    stats: {
        animated: false, // Prevent re-animation
        values: {
            stat1: { current: 0, target: 95 },
            stat2: { current: 0, target: 1500 },
            stat3: { current: 0, target: 700 },
            stat4: { current: 0, target: 100 }
        }
    },

    // Loading
    pageLoad: {
        progress: 0,
        complete: false,
        loadingScreenVisible: true
    }
};
```

---

## Performance Optimization Layers

```
┌────────────────────────────────────────────────────┐
│  Layer 1: Asset Optimization                       │
│  ├── Video: H.264, 1500 kbps max                   │
│  ├── Images: WebP with JPG fallback               │
│  ├── Fonts: Subset, woff2 format                  │
│  └── Scripts: Minified, bundled                   │
├────────────────────────────────────────────────────┤
│  Layer 2: Loading Strategy                        │
│  ├── Critical CSS: Inlined                        │
│  ├── Scripts: Deferred or async                   │
│  ├── Images: Lazy loaded (below fold)             │
│  └── Videos: Intersection Observer trigger        │
├────────────────────────────────────────────────────┤
│  Layer 3: Runtime Optimization                    │
│  ├── Throttle: Scroll events (250ms)              │
│  ├── Debounce: Resize events (250ms)              │
│  ├── Passive Listeners: Touch/scroll              │
│  └── RequestAnimationFrame: Smooth animations     │
├────────────────────────────────────────────────────┤
│  Layer 4: Browser Optimization                    │
│  ├── will-change: transform (animated elements)   │
│  ├── transform: translate3d (GPU acceleration)    │
│  ├── contain: layout/paint (isolation)            │
│  └── content-visibility: auto (render on demand)  │
└────────────────────────────────────────────────────┘
```

---

## Accessibility Tree

```
Page Landmarks
│
├── <header role="banner">
│   └── Navigation
│
├── <main role="main" id="main-content">
│   │
│   ├── <section aria-labelledby="hero-title">
│   │   ├── <h1 id="hero-title">
│   │   └── <button aria-label="Play/Pause video">
│   │
│   ├── <section aria-labelledby="stats-title">
│   │   └── Stats (aria-live="polite" on count)
│   │
│   ├── <section aria-labelledby="testimonials-title">
│   │   └── Slider (role="region" aria-roledescription="carousel")
│   │       ├── <button aria-label="Previous testimonial">
│   │       ├── <button aria-label="Next testimonial">
│   │       └── <button aria-label="Pause/Play slider">
│   │
│   └── <section aria-labelledby="portfolio-title">
│       └── Carousel (keyboard navigable)
│
└── <footer role="contentinfo">
    └── Footer content
```

---

## Dependency Graph

```
Core Dependencies (Must Load First)
    │
    ├── styles.css (Base Styles)
    ├── video-slider-styles.css (Component Styles)
    │
    v
Library Dependencies (CDN, Parallel Load)
    │
    ├── Swiper.js ──┐
    ├── Plyr ───────┼── Load in Parallel
    ├── AOS ────────┤
    ├── GSAP ───────┤
    └── Lottie ─────┘
    │
    v
Component Scripts (After Libraries)
    │
    └── video-slider-scripts.js
        │
        ├── Initialize AOS
        ├── Initialize Swiper instances
        ├── Initialize Plyr
        ├── Set up GSAP ScrollTrigger
        ├── Set up Intersection Observers
        └── Set up Event Listeners
```

---

## Browser Compatibility Matrix

```
Feature                 Chrome  Firefox  Safari  Edge    iOS     Android
─────────────────────────────────────────────────────────────────────────
Video Autoplay (muted)   ✅      ✅       ✅      ✅      ✅      ✅
Intersection Observer    ✅      ✅       ✅      ✅      ✅      ✅
CSS Grid                 ✅      ✅       ✅      ✅      ✅      ✅
CSS Custom Properties    ✅      ✅       ✅      ✅      ✅      ✅
Arrow Functions (ES6)    ✅      ✅       ✅      ✅      ✅      ✅
Promises/Async           ✅      ✅       ✅      ✅      ✅      ✅
WebP Images              ✅      ✅       ✅      ✅      ✅      ✅
WebM Video               ✅      ✅       ❌      ✅      ❌      ✅
Plyr Controls            ✅      ✅       ✅      ✅      ✅      ✅
Swiper Touch Events      ✅      ✅       ✅      ✅      ✅      ✅
GSAP Animations          ✅      ✅       ✅      ✅      ✅      ✅

Minimum Supported Versions:
Chrome 90+ | Firefox 88+ | Safari 14+ | Edge 90+ | iOS 14+ | Android 90+
```

---

## Deployment Architecture

```
Development                Production
────────────────          ────────────────

Local Files    ─────────→  CDN (Cloudflare/AWS)
│                          │
├── HTML                   ├── HTML (Minified)
├── CSS                    ├── CSS (Minified, Gzipped)
├── JavaScript             ├── JS (Minified, Gzipped)
└── Assets                 └── Assets (Optimized)
    ├── Videos                 ├── Videos (CDN)
    │   ├── MP4                │   ├── MP4 (Transcoded)
    │   └── WebM               │   └── WebM (Transcoded)
    └── Images                 └── Images (CDN)
        ├── JPG                    ├── WebP (Primary)
        └── PNG                    └── JPG (Fallback)

External CDNs:
├── Swiper CDN
├── Plyr CDN
├── AOS CDN
├── GSAP CDN
└── Lottie CDN
```

---

## File Size Budget

```
Component               Target Size    Maximum Size
─────────────────────────────────────────────────────
HTML                    < 50 KB        75 KB
Component CSS           < 30 KB        50 KB
Component JS            < 40 KB        60 KB
Hero Video (20s)        < 5 MB         8 MB
Product Demo (30s)      < 8 MB         12 MB
Testimonial Avatar      < 3 MB         5 MB
Portfolio Images        < 200 KB each  300 KB
─────────────────────────────────────────────────────
Total Initial Load      < 150 KB       200 KB
Total with Video        < 5.5 MB       8.5 MB
```

---

**Last Updated**: February 2026
**Architecture Version**: 1.0.0
**Created by**: iSN.BiZ Inc Development Team
