# ISN.BIZ Design Reference Guide
## Complete Visual Design Specification

**Date:** 2026-02-02
**Design System:** Neo-Technical Brutalism
**Status:** ✅ Production (https://isn.biz)

---

## 🎨 Color Palette

### Primary Colors

```css
/* Brand Core */
--color-blue: #1E9FF2;      /* Primary brand - CTAs, links, accents */
--color-cyan: #5FDFDF;      /* Secondary - highlights, team section */
--color-charcoal: #0D1117;  /* Background - dark, professional */

/* Supporting Colors */
--color-blue-dark: #1578C2; /* Deep tech blue */
--color-accent: #FF2D55;    /* Electric pink - investor section */
--color-concrete: #1C1F26;  /* Section backgrounds */
--color-steel: #2A2F3A;     /* Card backgrounds */
--color-white: #F0F4F8;     /* Text, off-white */
```

### Color Usage Map

| Element | Color | Hex | Use Case |
|---------|-------|-----|----------|
| **Primary CTAs** | Blue | `#1E9FF2` | Investment buttons, main actions |
| **Links** | Blue | `#1E9FF2` | Navigation, footer links |
| **Borders** | Blue | `#1E9FF2` | Card borders, section dividers |
| **Accents** | Cyan | `#5FDFDF` | Team section, hover states |
| **Investor Section** | Pink | `#FF2D55` | Borders, labels, CTAs |
| **Body Text** | Off-white | `#F0F4F8` | All readable text |
| **Backgrounds** | Charcoal | `#0D1117` | Page background, cards |
| **Section Backgrounds** | Concrete | `#1C1F26` | Alternating sections |

### Color Combinations

**High Contrast (WCAG AAA):**
- White text (#F0F4F8) on Charcoal (#0D1117) = 14.8:1 ✅
- Blue (#1E9FF2) on Charcoal (#0D1117) = 7.7:1 ✅

**Medium Contrast (WCAG AA Large Text):**
- Blue (#1E9FF2) on White (#F0F4F8) = 3.8:1 ✅ (18pt+ only)

### Color Psychology

- **Blue (#1E9FF2)**: Trust, technology, professionalism
- **Cyan (#5FDFDF)**: Innovation, freshness, energy
- **Charcoal (#0D1117)**: Sophistication, power, authority
- **Pink (#FF2D55)**: Urgency, excitement, call-to-action

---

## 📝 Typography

### Font Stack

```css
/* Technical/Monospace */
--font-mono: 'JetBrains Mono', 'Courier New', monospace;

/* Display/Headlines */
--font-display: 'Archivo Black', impact, sans-serif;

/* Body/Readable */
--font-body: 'IBM Plex Sans', -apple-system, sans-serif;
```

### Font Usage

| Element | Font | Weight | Size | Transform | Usage |
|---------|------|--------|------|-----------|-------|
| **Hero Title** | Archivo Black | 900 | 3-8rem (clamp) | Uppercase | Main headline |
| **Section Titles** | Archivo Black | 900 | 2-4.5rem (clamp) | Uppercase | Section headers |
| **Card Titles** | Archivo Black | 900 | 1.5-2.5rem | Uppercase | Card headers |
| **Body Text** | IBM Plex Sans | 400 | 1.125rem | None | Paragraphs |
| **Lead Text** | IBM Plex Sans | 300 | 1.5rem | None | Intro paragraphs |
| **Labels** | JetBrains Mono | 700 | 1rem | Uppercase | Section labels |
| **Stats** | JetBrains Mono | 700 | 2.5rem | None | Numeric displays |
| **Nav Links** | JetBrains Mono | 700 | 1rem | Uppercase | Navigation |
| **Form Labels** | JetBrains Mono | 700 | 1rem | Uppercase | Form fields |

### Typography Scale

```css
/* Headings */
h1: clamp(3rem, 10vw, 8rem)     /* 48-128px */
h2: clamp(2rem, 6vw, 4.5rem)    /* 32-72px */
h3: clamp(1.5rem, 4vw, 2.5rem)  /* 24-40px */

/* Body */
p: 1.125rem                      /* 18px */
.lead: 1.5rem                    /* 24px */

/* UI Elements */
.section-label: 1rem             /* 16px */
.stat-number: 2.5rem             /* 40px */
.stat-label: 1rem                /* 16px */
.tag: 1rem                       /* 16px */
```

### Font Loading

```html
<!-- Preconnect for performance -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

<!-- Google Fonts -->
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Archivo+Black&family=IBM+Plex+Sans:wght@300;400;600;700&display=swap" rel="stylesheet">
```

---

## 📐 Spacing System

### Asymmetric Grid

```css
--space-xs: 0.5rem;   /* 8px */
--space-sm: 1rem;     /* 16px */
--space-md: 2rem;     /* 32px */
--space-lg: 4rem;     /* 64px */
--space-xl: 8rem;     /* 128px */
```

### Usage Examples

| Spacing | Value | Use Case |
|---------|-------|----------|
| **xs** | 8px | Icon gaps, tag spacing |
| **sm** | 16px | Card padding, form gaps |
| **md** | 32px | Section padding, grid gaps |
| **lg** | 64px | Between major sections |
| **xl** | 128px | Hero section padding |

### Container & Layout

```css
.container {
    max-width: 1400px;
    margin: 0 auto;
    padding: 0 var(--space-md); /* 32px horizontal */
}

.section {
    padding: var(--space-xl) 0;  /* 128px vertical */
}
```

---

## 🎭 Visual Effects

### Shadows

```css
/* Brutal Shadow (primary) */
--shadow-brutal: 8px 8px 0 rgba(30, 159, 242, 0.3);

/* Deep Shadow (cards) */
--shadow-deep: 0 20px 60px rgba(0, 0, 0, 0.5);
```

**Usage:**
- **Brutal Shadow**: Buttons, portfolio cards on hover
- **Deep Shadow**: Hero visual, elevated cards

### Grid Overlay

```css
body::before {
    background:
        linear-gradient(90deg, rgba(30, 159, 242, 0.15) 1px, transparent 1px),
        linear-gradient(0deg, rgba(30, 159, 242, 0.15) 1px, transparent 1px);
    background-size: 40px 40px;
    opacity: 0.4;
}
```

**Effect:** Technical blueprint aesthetic

### Noise Texture

```css
--noise: url("data:image/svg+xml,...");

body::after {
    background-image: var(--noise);
    mix-blend-mode: overlay;
    opacity: 0.3;
}
```

**Effect:** Subtle film grain texture

### Clip Paths (Angled Corners)

```css
/* Button - Left angle */
.btn-primary {
    clip-path: polygon(10% 0%, 100% 0%, 90% 100%, 0% 100%);
}

/* Button - Right angle */
.btn-secondary {
    clip-path: polygon(0% 0%, 90% 0%, 100% 100%, 10% 100%);
}

/* Icon - Angled */
.solution-icon {
    clip-path: polygon(15% 0%, 100% 0%, 85% 100%, 0% 100%);
}
```

---

## 🎬 Animations

### Hero Animations

```css
/* Logo Glitch-In */
@keyframes glitch-in {
    0% {
        opacity: 0;
        transform: translateY(-50px) scale(0.9);
        filter: blur(10px);
    }
    50% {
        transform: translateX(-5px);
    }
    100% {
        opacity: 1;
        transform: translateY(0) scale(1);
        filter: blur(0);
    }
}

/* Title Reveal */
@keyframes title-reveal {
    0% {
        opacity: 0;
        transform: translateY(30px);
        filter: blur(8px);
    }
    100% {
        opacity: 1;
        transform: translateY(0);
        filter: blur(0);
    }
}

/* Scanning Line */
@keyframes scan {
    0% { top: -10%; }
    100% { top: 110%; }
}
```

### Hover Effects

```css
/* Lift on Hover */
.lift-on-hover:hover {
    transform: translateY(-10px);
}

/* Brutal Shadow Shift */
.btn-primary:hover {
    transform: translate(4px, 4px);
    box-shadow: 4px 4px 0 rgba(30, 159, 242, 0.3);
}

/* Image Scale */
.portfolio-card:hover img {
    transform: scale(1.1);
    filter: grayscale(0%);
}
```

### Label Flicker

```css
@keyframes label-flicker {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.9; }
}

.section-label {
    animation: label-flicker 3s infinite;
}
```

---

## 🧩 Component Library

### 1. Buttons

**Primary Button**
```html
<a href="#" class="btn btn-primary"><span>Investment Opportunities</span></a>
```
- Background: `--color-blue` (#1E9FF2)
- Clip-path: Left angle
- Hover: Pink background slide-in, shadow shift

**Secondary Button**
```html
<a href="#" class="btn btn-secondary"><span>Schedule a Demo</span></a>
```
- Border: 3px solid `--color-blue`
- Background: Transparent
- Clip-path: Right angle
- Hover: Blue fill

**Outline Button**
```html
<a href="#" class="btn btn-outline"><span>View Full Portfolio</span></a>
```
- Border: 2px solid `--color-blue`
- Background: Transparent
- No clip-path
- Hover: Blue fill

### 2. Cards

**Solution Card**
```html
<div class="solution-card lift-on-hover">
    <div class="solution-icon glow">
        <svg>...</svg>
    </div>
    <h3>AI-Powered Applications</h3>
    <p>Description text...</p>
    <ul class="solution-features">
        <li>Feature 1</li>
        <li>Feature 2</li>
    </ul>
</div>
```
- Background: `--color-concrete`
- Border: 3px solid (transparent → blue on hover)
- Hover: Lift 10px, brutal shadow

**Portfolio Card**
```html
<div class="portfolio-card">
    <div class="portfolio-image">
        <img src="..." alt="..." loading="lazy">
    </div>
    <div class="portfolio-number">01</div>
    <h3>Project Title</h3>
    <p>Project description...</p>
    <div class="portfolio-tags">
        <span class="tag">Python</span>
        <span class="tag">Docker</span>
    </div>
</div>
```
- Background: `--color-charcoal`
- Border: 3px solid `--color-blue`
- Large number overlay (opacity 0.1)
- Image: Grayscale → color on hover

**Credential Card**
```html
<div class="credential-card">
    <h3>Company Information</h3>
    <ul class="credential-list">
        <li><strong>Founded:</strong> July 8, 2015</li>
        <li><strong>DUNS:</strong> 080513772</li>
    </ul>
</div>
```
- Background: `rgba(30, 159, 242, 0.05)`
- Border: 2px solid `--color-blue`
- Label: `//INFO` pseudo-element

### 3. Stats Display

**Hero Stats**
```html
<div class="hero-stats">
    <div class="stat">
        <div class="stat-number">11+</div>
        <div class="stat-label">Years Experience</div>
    </div>
</div>
```
- Background: `rgba(30, 159, 242, 0.05)`
- Border-left: 4px solid `--color-blue`
- Pseudo-element: `//` decorative marker

### 4. Section Label

```html
<span class="section-label">About iSN.BiZ</span>
```
- Font: JetBrains Mono
- Background: `rgba(30, 159, 242, 0.1)`
- Border: 2px solid `--color-blue`
- Animation: Label flicker (3s infinite)

### 5. Tags

```html
<div class="portfolio-tags">
    <span class="tag">Python</span>
    <span class="tag">Docker</span>
</div>
```
- Background: `--color-blue`
- Color: `--color-charcoal`
- Font: JetBrains Mono
- Size: 1rem (16px)

### 6. Form Elements

**Form Group**
```html
<div class="form-group">
    <label for="name">Full Name *</label>
    <input type="text" id="name" name="name" required>
</div>
```
- Background: `rgba(30, 159, 242, 0.05)`
- Border: 2px solid `rgba(30, 159, 242, 0.3)`
- Focus: Blue border, glow shadow
- Label: JetBrains Mono, uppercase

---

## 📱 Responsive Breakpoints

### Grid Systems

**4-Column Grid** (Solutions, Portfolio, Investors)
```css
.solutions-grid {
    grid-template-columns: repeat(4, 1fr);
}

@media (max-width: 992px) {
    grid-template-columns: repeat(2, 1fr);
}

@media (max-width: 768px) {
    grid-template-columns: 1fr;
}
```

**2-Column Grid** (Team, About)
```css
.team-grid {
    grid-template-columns: repeat(2, 1fr);
}

@media (max-width: 768px) {
    grid-template-columns: 1fr;
}
```

### Breakpoint Strategy

| Device | Width | Columns | Font Scale |
|--------|-------|---------|------------|
| Desktop | 1400px+ | 4 | 100% |
| Laptop | 992-1399px | 4 | 100% |
| Tablet | 768-991px | 2 | 95% |
| Mobile | 480-767px | 1 | 90% |
| Small | <480px | 1 | 85% |

---

## 🖼️ Image Guidelines

### Asset Types

**Logos:**
- Format: WebP
- Navbar: 50px height
- Hero: 500px max-width
- Footer: 200px max-width

**Backgrounds:**
- Format: WebP
- Resolution: 1920x1080 minimum
- Optimization: Gradient overlay

**Portfolio:**
- Format: WebP
- Dimensions: 800x600 (4:3 ratio)
- Effect: Grayscale 30% → 0% on hover

**Team Photos:**
- Format: WebP
- Dimensions: 400x400 (1:1 ratio)
- Background: Gradient (maintained in photo)

### S3 Asset Paths

```
https://isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com/
├── premium_v3/
│   ├── logos/
│   │   ├── navbar_logo.webp
│   │   ├── hero_logo.webp
│   │   ├── footer_logo.webp
│   │   ├── favicon.webp
│   │   └── apple_touch_icon.webp
│   ├── backgrounds/
│   │   └── hero-background-main.webp
│   ├── services/
│   │   └── ai_research.webp
│   ├── portfolio/
│   │   ├── opportunity_bot.webp
│   │   ├── infrastructure.webp
│   │   ├── credit_automation.webp
│   │   ├── rag_bi.webp
│   │   └── androidaps_health.webp
│   ├── sections/
│   │   └── investor_backdrop.webp
│   └── og/
│       └── og_default.webp
└── assets/
    └── founders/
        └── headshots_with_bg/
            ├── jonathan_headshot.webp
            ├── bri_headshot.webp
            ├── lilly_headshot.webp
            └── alicia_headshot.webp
```

---

## ♿ Accessibility (WCAG 2.1 AA)

### Compliance Checklist

✅ **Color Contrast**
- Body text: 14.8:1 (AAA)
- Links: 7.7:1 (AA)
- Large text: 3.8:1 (AA for 18pt+)

✅ **Font Sizes**
- Minimum: 16px (1rem)
- All text: 16px or larger
- No text below WCAG minimum

✅ **Keyboard Navigation**
- Skip link: `<a href="#about" class="skip-link">`
- Focus indicators: 3px solid blue outline
- Tab order: Logical, semantic

✅ **ARIA Labels**
- Nav toggle: `aria-label="Toggle navigation"`
- Nav toggle: `aria-expanded="false"`
- Nav menu: `id="primary-navigation"`

✅ **Links**
- Non-nav links: Underlined
- Color + underline distinction
- Hover states: Visible

✅ **Forms**
- Labels: Associated with inputs
- Focus states: Blue outline + glow
- Required: Indicated with *

✅ **Motion**
- Reduced motion: `@media (prefers-reduced-motion: reduce)`
- Animations: Optional, respects user preference

---

## 🎯 Design Principles

### 1. Technical Credibility
- **Monospace fonts** signal engineering expertise
- **Grid overlay** suggests precision and structure
- **Terminal aesthetics** convey technical depth

### 2. Investor Appeal
- **Dark theme** = sophistication and authority
- **Bold typography** = confidence and leadership
- **Structured layouts** = organized and professional

### 3. Performance
- **WebP images** = 30-50% smaller files
- **CSS-only effects** = no heavy JavaScript
- **S3/CDN** = fast global delivery
- **Minimal frameworks** = quick load times

### 4. Distinctive Identity
- **Neo-Technical Brutalism** = unique in industry
- **Angled clip-paths** = memorable brand signature
- **Technical overlays** = differentiated aesthetic

### 5. Accessibility First
- **WCAG 2.1 AA** = inclusive by design
- **Semantic HTML** = screen reader friendly
- **Keyboard support** = universally accessible

---

## 📦 Production Files

### Essential Files

```
D:\workspace\ISNBIZ_Files\
├── index.html                  # Main page (737 lines)
├── styles.css                  # Main stylesheet (1800 lines)
├── enhanced-animations.css     # Additional animations
├── enhanced-interactions.js    # JavaScript enhancements
└── logo-pallete/              # Local logo variants (backup)
```

### Deployed Version

**URL:** https://isn.biz
**Status:** ✅ Production
**CDN:** Amazon S3 + CloudFront
**SSL:** Active (HTTPS)

---

## 🚀 Usage Examples

### Adding a New Solution Card

```html
<div class="solution-card lift-on-hover grid-overlay">
    <div class="solution-icon glow">
        <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <!-- SVG icon path -->
        </svg>
    </div>
    <h3>New Solution Name</h3>
    <p>Solution description explaining the value proposition.</p>
    <ul class="solution-features">
        <li>Key Feature 1</li>
        <li>Key Feature 2</li>
        <li>Key Feature 3</li>
        <li>Key Feature 4</li>
    </ul>
</div>
```

### Adding a New Portfolio Item

```html
<div class="portfolio-card">
    <div class="portfolio-image">
        <img src="https://isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com/premium_v3/portfolio/new_project.webp"
             alt="Project description"
             loading="lazy">
    </div>
    <div class="portfolio-number">07</div>
    <h3>Project Title</h3>
    <p>Detailed project description with technical details and business impact.</p>
    <div class="portfolio-tags">
        <span class="tag">Tech 1</span>
        <span class="tag">Tech 2</span>
        <span class="tag">Tech 3</span>
    </div>
</div>
```

### Adding a New Team Member

```html
<div class="team-member">
    <div class="member-photo">
        <picture>
            <source srcset="https://isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com/assets/founders/headshots_with_bg/new_member.webp" type="image/webp">
            <img src="https://isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com/assets/founders/headshots_with_bg/new_member.webp"
                 alt="Member Name - Position"
                 loading="lazy"
                 width="400"
                 height="400">
        </picture>
    </div>
    <div class="member-info">
        <h3><a href="member-page.html">Member Name</a></h3>
        <p class="role">Position / Title</p>
        <p class="bio">Brief bio describing expertise and role.</p>
    </div>
</div>
```

---

## 🔍 Quick Reference

### Color Variables
```css
--color-blue: #1E9FF2
--color-cyan: #5FDFDF
--color-charcoal: #0D1117
--color-accent: #FF2D55
--color-white: #F0F4F8
```

### Font Variables
```css
--font-mono: 'JetBrains Mono'
--font-display: 'Archivo Black'
--font-body: 'IBM Plex Sans'
```

### Spacing Variables
```css
--space-xs: 0.5rem   /* 8px */
--space-sm: 1rem     /* 16px */
--space-md: 2rem     /* 32px */
--space-lg: 4rem     /* 64px */
--space-xl: 8rem     /* 128px */
```

### Shadow Variables
```css
--shadow-brutal: 8px 8px 0 rgba(30, 159, 242, 0.3)
--shadow-deep: 0 20px 60px rgba(0, 0, 0, 0.5)
```

---

**Last Updated:** 2026-02-02
**Design System:** Neo-Technical Brutalism
**Maintained by:** ISN.BIZ Design Team
**Version:** 1.0 (Production)
