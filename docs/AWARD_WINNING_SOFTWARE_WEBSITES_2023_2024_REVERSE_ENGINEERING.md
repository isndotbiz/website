# Award-Winning Software Company Websites 2023-2024: Deep Reverse Engineering

**Created:** February 2026
**Purpose:** Reverse engineer proven, award-winning software company website designs from 2023-2024 to extract specific patterns, code, and techniques for isn.biz

## Table of Contents
1. [Award Winners Overview](#award-winners-overview)
2. [Typography Systems](#typography-systems)
3. [Color Psychology & Schemes](#color-psychology--schemes)
4. [Layout Grids & Spacing](#layout-grids--spacing)
5. [Animation Libraries & Timing](#animation-libraries--timing)
6. [Component Patterns](#component-patterns)
7. [Content Strategy](#content-strategy)
8. [Code Examples](#code-examples)
9. [Implementation Guide](#implementation-guide)

---

## Award Winners Overview

### Awwwards 2023-2024

**Site of the Year 2023: Lusion v3**
- **Category:** Digital Agency/Portfolio
- **Recognition:** Site of the Year, Developer Site of the Year, Site of the Month
- **Tech Stack:** Angular, Three.js, TypeScript
- **What Made It Win:** Seamless blend of clean interface with over-the-top animations, compelling interaction techniques, walking the line between current design trends and creative innovation
- **Scores:** Design 8.26/10, Usability 7.95/10, Creativity 8.65/10, Content 8.26/10
- **Source:** [Awwwards - Lusion v3](https://www.awwwards.com/sites/lusion-v3)

**Key Insight:** You don't need crazy fonts or vibrant colors to stand out—sophisticated animations with minimalist aesthetics create memorable experiences.

### CSS Design Awards 2023-2024

**2023 Winners:**
1. **Lusion v3** by Lusion (9.27/10)
2. **Unseen Studio®** (9.20/10) - Best UI Site
3. **MOTION.ED** by Zajno (9.07/10) - Best Innovation Site
4. **MSI - Egg Hunt** by Merci-Michel (9.04/10) - Best UX Site
5. **THE ROGER** by North Kingdom (9.01/10)

**Source:** [CSS Design Awards 2023 Winners](https://www.cssdesignawards.com/blog/2023-website-of-the-year-winners/394/)

### Webby Awards 2023-2024

**2024 Technology/Software Winners:**
- **ChatGPT by OpenAI** - Breakout of the Year Award (2023)
- **OURA** - Connected Products & Wearables, App Features
- **PhotoRoom** - Product & Services, AI Apps and Experiences
- **Notion, Shopify, Spotify** - Various categories including Best User Experience
- **Vercel** - SaaS Awards 2023 Winner (Loyalty and Retention Category)

**Shopify Winter '24 Edition** won for turning mundane release notes into creative editorial content with narrative-driven digital catalog design.

**Sources:**
- [28th Annual Webby Award Winners](https://www.webbyawards.com/press/press-releases/28th-annual-webby-award-winners-announced/)
- [Shopify on Balancing Function and Form](https://www.webbyawards.com/winner-stories-shopify-editions/)

### Best B2B SaaS Websites 2023-2024

Top consistently-ranked B2B SaaS websites across multiple design award lists:

1. **Stripe** - "Masterclass in focus," minimalist yet authoritative
2. **Linear** - "Less is more," precisely calibrated typography and spacing
3. **Vercel** - Professional and polished minimalist aesthetic
4. **Notion** - Narrative-driven, user-friendly design
5. **Slack, HubSpot, Webflow, Dropbox** - Industry leaders in design

**Source:** [Best B2B SaaS Websites 2023-2024](https://azurodigital.com/saas-website-examples/)

---

## Typography Systems

### The Inter Font Dominance

**Winner Pattern:** Inter is the most popular font across award-winning software websites in 2023-2024, used by Linear, Vercel, Notion, and many others.

**Why Inter Works:**
- Designed specifically for screens with exceptional readability
- Variable font with weights from 100-900
- Open-source and free
- Optimized for on-screen use
- Geometric precision that pairs well with modern UIs

### Typography Hierarchy - Lusion v3

**Font:** Inter Tight
**Weight System:**
- Light (300)
- Normal (400)
- Medium (500)
- Bold (600)
- Extra Bold (700)
- Black (800)

**Fluid Typography Implementation:**
```css
/* Lusion v3's approach to responsive typography */
font-size: clamp(1rem, 2.5vw, 2rem);
/* Scales from 16px minimum to 32px maximum based on viewport */
```

### Award-Winning Font Pairings

**1. Inter + Fira Code**
- **Use Case:** Tech companies, developer tools
- **Psychology:** Clean minimalism with technical credibility
- **Example:** Used in coding-focused SaaS platforms

**2. Inter + Manrope**
- **Use Case:** Modern corporate websites, tech startups
- **Psychology:** Geometric precision meets readability
- **Visual Effect:** Balanced and professional

**3. Inter + Krub**
- **Use Case:** Tech websites needing visual interest
- **Psychology:** Contemporary lines with distinctive character
- **Example:** Screen-optimized with clarity

**4. Inter + IBM Plex Mono**
- **Use Case:** Developer-focused products
- **Psychology:** Professional sans-serif meets monospace precision

**Sources:**
- [Inter Font Combinations - Typewolf](https://www.typewolf.com/inter)
- [5 Fonts to Pair with Inter](https://jenwagner.co/5-fonts-to-pair-with-inter/)

### Fluid Typography Best Practices

**The clamp() Function:**
```css
/* Basic syntax */
font-size: clamp(minimum, preferred, maximum);

/* Accessibility-focused example */
html {
  font-size: clamp(1em, 17px + 0.24vw, 1.125em);
}

/* Complete typography styling */
.hero h1 {
  font-size: clamp(40px, 8vw + 1rem, 100px);
  letter-spacing: clamp(2px, 10vw + 1rem, 10px);
  line-height: clamp(0, 10vw + 1rem, 60px);
}
```

**Why This Works:**
- Eliminates breakpoint jumps
- Scales smoothly across all viewport sizes
- Reduces media query code
- Maintains readability at all sizes

**Accessibility Note:** Always combine `vw` with `rem` units so text scales with browser zoom:
```css
/* Good - scales with zoom */
font-size: clamp(1rem, 1rem + 2vw, 3rem);

/* Bad - doesn't scale with zoom */
font-size: clamp(16px, 2vw, 48px);
```

**Sources:**
- [CSS Fluid Typography Using clamp()](https://dev.to/devyoma/css-fluid-typography-a-guide-to-using-clamp-for-scalable-text-293o)
- [Modern Fluid Typography - Smashing Magazine](https://www.smashingmagazine.com/2022/01/modern-fluid-typography-css-clamp/)

### Typography Scale Example

**Lusion v3 Typography Scale:**
```css
/* Title hierarchy */
--title-8: clamp(3rem, 5vw, 6rem);      /* 48px - 96px */
--title-7: clamp(2.5rem, 4vw, 5rem);     /* 40px - 80px */
--title-6: clamp(2rem, 3.5vw, 4rem);     /* 32px - 64px */
--title-5: clamp(1.75rem, 3vw, 3.5rem);  /* 28px - 56px */
--title-4: clamp(1.5rem, 2.5vw, 3rem);   /* 24px - 48px */
--title-3: clamp(1.25rem, 2vw, 2.5rem);  /* 20px - 40px */
--title-2: clamp(1.125rem, 1.75vw, 2rem);/* 18px - 32px */
--title-1: clamp(1rem, 1.5vw, 1.75rem);  /* 16px - 28px */

/* Text hierarchy */
--text-large: clamp(1.125rem, 1.25vw, 1.5rem);  /* 18px - 24px */
--text-base: clamp(1rem, 1vw, 1.25rem);         /* 16px - 20px */
--text-small: clamp(0.875rem, 0.9vw, 1rem);     /* 14px - 16px */
--text-mini: clamp(0.75rem, 0.85vw, 0.875rem);  /* 12px - 14px */
```

**Linear Typography Approach:**
```css
/* Linear's balanced text wrapping */
h1, h2, h3 {
  text-wrap: balance; /* New CSS feature for optimal line breaks */
}

/* Consistent letter spacing tied to scale */
--letter-spacing-tight: -0.02em;
--letter-spacing-normal: 0;
--letter-spacing-wide: 0.05em;
```

---

## Color Psychology & Schemes

### Award-Winning Color Patterns

**Analysis of 50+ award-winning websites from 2023-2024:**

**Source:** [50 Gorgeous Color Schemes From Award-Winning Websites](https://visme.co/blog/website-color-schemes/)

### Color Scheme Categories

**1. Dark & Vibrant**
- **Pattern:** Dark smoky black (#0A0A0A) + Electric blue (#0066FF)
- **Psychology:** Sophisticated, modern, tech-forward
- **Used By:** Developer tools, SaaS platforms
- **Example:**
```css
:root {
  --background: #0A0A0A;
  --primary: #0066FF;
  --text: #FFFFFF;
  --text-secondary: rgba(255, 255, 255, 0.7);
}
```

**2. Minimalist Bright**
- **Pattern:** White (#FFFFFF) + Vivid accents (Yellow #FFEB3B, Blue #2196F3, Pink #E91E63)
- **Psychology:** Clean, energetic, approachable
- **Used By:** Creative agencies, modern SaaS
- **Example:**
```css
:root {
  --background: #FFFFFF;
  --accent-yellow: #FFEB3B;
  --accent-blue: #2196F3;
  --accent-pink: #E91E63;
  --text: #1A1A1A;
}
```

**3. Corporate Blue + Green**
- **Pattern:** Royal blue (#1E40AF) + Eco green (#10B981) + Gold accents (#F59E0B)
- **Psychology:** Trustworthy, professional, growth-oriented
- **Used By:** Financial tech, enterprise software
- **Example:**
```css
:root {
  --primary-blue: #1E40AF;
  --eco-green: #10B981;
  --gold-accent: #F59E0B;
  --background: #F9FAFB;
}
```

**4. Bold Contrasts**
- **Pattern:** Deep navy (#0F172A) + Vivid cyan (#06B6D4) + White
- **Psychology:** Professional yet dynamic
- **Used By:** Tech companies, AI platforms
- **Example:**
```css
:root {
  --background: #0F172A;
  --primary-cyan: #06B6D4;
  --highlight: #FFFFFF;
  --text: #E2E8F0;
}
```

### Specific Award-Winner Color Schemes

**Lusion v3:**
```css
:root {
  --primary-dark: #222222;
  --accent-orange: #FA5D29;
  --accent-blue: #49B3FC;
  --accent-green: #AAEEC4;
  --accent-purple: #502BD8;
  --text-primary: #FFFFFF;
  --text-secondary: rgba(255, 255, 255, 0.8);
}
```

**Stripe (Inferred from analysis):**
```css
:root {
  --background: #FFFFFF;
  --primary: #635BFF;        /* Stripe purple */
  --gradient-start: #8B5CF6;
  --gradient-end: #635BFF;
  --text-primary: #0A2540;   /* Deep navy */
  --text-secondary: #425466;
  --border: #E6E6E6;
}
```

**Linear (Inferred from analysis):**
```css
:root[data-theme="dark"] {
  --color-text-primary: #FFFFFF;
  --color-text-secondary: rgba(255, 255, 255, 0.9);
  --color-text-tertiary: rgba(255, 255, 255, 0.7);
  --color-text-quaternary: rgba(255, 255, 255, 0.5);
  --red: #FF5555;
  --orange: #FF8E53;
  --green: #00D4AA;
}
```

**Vercel:**
```css
:root {
  --background-light: #FFFFFF;
  --background-dark: #000000;
  --foreground-light: #000000;
  --foreground-dark: #FFFFFF;
  --accent: #0070F3;        /* Vercel blue */
  --border: #EAEAEA;
  --code-bg: #F4F4F4;
}
```

### Modern Gradient Backgrounds (2023-2024 Trends)

**Trend:** Multicolored gradients with vibrant palettes, irregular shapes with blur and distortion effects.

**Implementation Examples:**

**1. Subtle Tech Gradient:**
```css
.hero-background {
  background: linear-gradient(
    135deg,
    rgba(99, 91, 255, 0.1) 0%,
    rgba(139, 92, 246, 0.05) 50%,
    rgba(6, 182, 212, 0.1) 100%
  );
}
```

**2. Vibrant Accent Gradient:**
```css
.accent-section {
  background: linear-gradient(
    90deg,
    rgba(42, 123, 155, 1) 0%,
    rgba(87, 199, 133, 1) 50%,
    rgba(237, 221, 83, 1) 100%
  );
}
```

**3. Mesh Gradient (Trending in 2023-2024):**
```css
.mesh-gradient {
  background: radial-gradient(at 40% 20%, hsla(28,100%,74%,1) 0px, transparent 50%),
              radial-gradient(at 80% 0%, hsla(189,100%,56%,1) 0px, transparent 50%),
              radial-gradient(at 0% 50%, hsla(355,100%,93%,1) 0px, transparent 50%),
              radial-gradient(at 80% 50%, hsla(340,100%,76%,1) 0px, transparent 50%),
              radial-gradient(at 0% 100%, hsla(22,100%,77%,1) 0px, transparent 50%),
              radial-gradient(at 80% 100%, hsla(242,100%,70%,1) 0px, transparent 50%),
              radial-gradient(at 0% 0%, hsla(343,100%,76%,1) 0px, transparent 50%);
}
```

**4. Gradient Text Effect (Linear's Approach):**
```css
.gradient-text {
  background: linear-gradient(
    to right,
    var(--color-text-primary),
    transparent 80%
  );
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
```

**Resources:**
- [CSS Gradient Generator](https://cssgradient.io/)
- [WebGradients - 180 Free Gradients](https://webgradients.com/)
- [Awwwards - Trendy Gradients](https://www.awwwards.com/gradients-in-web-design-elements.html)

---

## Layout Grids & Spacing

### The 4px/8px Grid System Evolution

**Historical Context:** The 8px grid was standard, but 2023-2024 saw a shift to **4px baseline with 8pt linear scale**.

**Why 4px Won:**
- More flexible for mobile screens
- Better for content-dense layouts
- 8pt increments too large for small UI elements
- Still maintains divisibility (4/2=2)

**Sources:**
- [Basics: Grid Systems and the 4px Grid](https://blog.designary.com/p/layout-basics-grid-systems-and-the-4px-grid)
- [Spacing Best Practices - 8pt Grid System](https://cieden.com/book/sub-atomic/spacing/spacing-best-practices)

### Hybrid Spacing System (Winner Pattern)

**Best Practice from Award-Winning Sites:**
```css
:root {
  /* 4px baseline for fine-tuning */
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-5: 20px;
  --space-6: 24px;
  --space-8: 32px;
  --space-10: 40px;
  --space-12: 48px;
  --space-16: 64px;
  --space-20: 80px;
  --space-24: 96px;
  --space-32: 128px;
  --space-40: 160px;
  --space-48: 192px;

  /* Line heights always divisible by 4 */
  --leading-none: 1;
  --leading-tight: 1.25;   /* 20px for 16px font */
  --leading-normal: 1.5;   /* 24px for 16px font */
  --leading-relaxed: 1.75; /* 28px for 16px font */
  --leading-loose: 2;      /* 32px for 16px font */
}
```

### Internal ≤ External Rule

**Critical Design Principle:** Internal spacing of elements should never exceed spacing between elements.

**Example:**
```css
.card {
  padding: var(--space-6);        /* Internal: 24px */
  margin-bottom: var(--space-8);  /* External: 32px ✓ */
  /* If margin-bottom were 16px, it would violate the rule */
}

.button {
  padding: var(--space-3) var(--space-6);  /* Internal: 12px 24px */
  margin-right: var(--space-4);             /* External: 16px ✓ */
}
```

### Lusion v3 Grid System

**Responsive Grid Architecture:**
```css
/* Primary content grid */
.grid-primary {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: clamp(20px, 5vw, 100px);
}

/* Collections grid for larger cards */
.grid-collections {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(440px, 1fr));
  gap: clamp(24px, 4vw, 80px);
}

/* Modern container queries for component-level responsiveness */
@container (min-width: 400px) {
  .card {
    grid-template-columns: 1fr 2fr;
  }
}
```

### CSS Grid Patterns from Award Winners

**1. Auto-Fill Responsive Grid:**
```css
.grid-responsive {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(min(100%, 300px), 1fr));
  gap: var(--space-8);
}
```

**2. Asymmetric Layout (Stripe Pattern):**
```css
.grid-asymmetric {
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: var(--space-12);
}

@media (max-width: 768px) {
  .grid-asymmetric {
    grid-template-columns: 1fr;
  }
}
```

**3. Bento Box Layout (Trending in 2023-2024):**
```css
.bento-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-template-rows: repeat(3, 200px);
  gap: var(--space-4);
}

.bento-item-large {
  grid-column: span 2;
  grid-row: span 2;
}

.bento-item-wide {
  grid-column: span 2;
}

.bento-item-tall {
  grid-row: span 2;
}
```

### Flexbox for Component Layouts

**Linear's Flex Component Approach:**
```css
.flex {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
}

.flex-col {
  flex-direction: column;
}

.flex-between {
  justify-content: space-between;
}

.flex-start {
  align-items: flex-start;
}
```

### Maximum Width Containers

**Award-Winning Width Patterns:**
```css
:root {
  --container-xs: 640px;
  --container-sm: 768px;
  --container-md: 1024px;
  --container-lg: 1280px;
  --container-xl: 1440px;
  --container-2xl: 1600px;
}

.container {
  width: 100%;
  max-width: var(--container-xl);
  margin-left: auto;
  margin-right: auto;
  padding-left: var(--space-6);
  padding-right: var(--space-6);
}

@media (min-width: 640px) {
  .container {
    padding-left: var(--space-8);
    padding-right: var(--space-8);
  }
}
```

---

## Animation Libraries & Timing

### GSAP: The Industry Standard

**Winner Pattern:** GSAP (GreenSock Animation Platform) dominates award-winning websites in 2023-2024.

**Why GSAP Wins:**
- **Performance:** Optimized for maximum runtime performance
- **Compatibility:** Works seamlessly across all browsers
- **Power:** Handles thousands of simultaneous animations
- **Size:** Core library only ~23KB gzipped
- **Free:** Completely free since Webflow acquisition in 2024

**Sources:**
- [GSAP Official](https://gsap.com/)
- [45 GSAP ScrollTrigger Examples](https://freefrontend.com/scroll-trigger-js/)

### GSAP ScrollTrigger Code Examples

**Basic ScrollTrigger Setup:**
```javascript
gsap.registerPlugin(ScrollTrigger);

// Pin section while scrolling
gsap.to(".panel", {
  scrollTrigger: {
    trigger: ".panel",
    pin: true,
    start: "top top",
    end: "+=500",
    scrub: 1,
    markers: false
  },
  rotation: 360,
  ease: "none"
});
```

**Smooth Scrubbing Animation:**
```javascript
// Scrub links animation to scrollbar position
gsap.to(".element", {
  scrollTrigger: {
    trigger: ".element",
    start: "top center",
    end: "bottom center",
    scrub: 2, // Smooth scrubbing effect (2 seconds delay)
  },
  x: 400,
  opacity: 1,
  ease: "power2.inOut"
});
```

**Parallax Effect with ScrollTrigger:**
```javascript
// Different elements scroll at different speeds
gsap.to(".parallax-slow", {
  y: (i, target) => -ScrollTrigger.maxScroll(window) * target.dataset.speed,
  ease: "none",
  scrollTrigger: {
    start: 0,
    end: "max",
    invalidateOnRefresh: true,
    scrub: 0
  }
});
```

**ScrollSmoother for Buttery Smooth Scrolling:**
```javascript
gsap.registerPlugin(ScrollSmoother);

// Create smooth scrolling instance
ScrollSmoother.create({
  wrapper: "#smooth-wrapper",
  content: "#smooth-content",
  smooth: 1.5,    // Smoothness amount (0-3)
  effects: true,  // Enable data-speed and data-lag attributes
  smoothTouch: 0.1 // Mobile smoothness
});
```

**Award-Winning Parallax HTML Structure:**
```html
<div id="smooth-wrapper">
  <div id="smooth-content">
    <!-- Elements with data-speed for parallax -->
    <div class="element" data-speed="0.5">
      <!-- Scrolls at half speed -->
    </div>
    <div class="element" data-speed="1.5">
      <!-- Scrolls at 1.5x speed -->
    </div>
  </div>
</div>
```

### Framer Motion for React

**When to Use:** React/Next.js applications (like Vercel's site)

**Size:** ~32KB gzipped
**Strengths:** Declarative animations, layout animations, gesture support

**Basic Framer Motion Example:**
```jsx
import { motion } from 'framer-motion';

export default function Hero() {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.6, ease: "easeOut" }}
    >
      <h1>Your Headline</h1>
    </motion.div>
  );
}
```

**Scroll-Triggered Animation:**
```jsx
import { motion, useScroll, useTransform } from 'framer-motion';

export default function ParallaxSection() {
  const { scrollYProgress } = useScroll();
  const y = useTransform(scrollYProgress, [0, 1], ['0%', '50%']);

  return (
    <motion.div style={{ y }}>
      <h2>Parallax Content</h2>
    </motion.div>
  );
}
```

**Stagger Children Animation (Common in Award Winners):**
```jsx
const container = {
  hidden: { opacity: 0 },
  show: {
    opacity: 1,
    transition: {
      staggerChildren: 0.1
    }
  }
};

const item = {
  hidden: { opacity: 0, y: 20 },
  show: { opacity: 1, y: 0 }
};

export default function StaggerList() {
  return (
    <motion.ul variants={container} initial="hidden" animate="show">
      <motion.li variants={item}>Item 1</motion.li>
      <motion.li variants={item}>Item 2</motion.li>
      <motion.li variants={item}>Item 3</motion.li>
    </motion.ul>
  );
}
```

### Animation Timing from Lusion v3

**Easing Functions:**
```css
:root {
  --ease-in-out: cubic-bezier(0.42, 0, 0.58, 1);
  --ease-out: cubic-bezier(0, 0, 0.58, 1);
  --ease-in: cubic-bezier(0.42, 0, 1, 1);
  --ease-smooth: cubic-bezier(0.4, 0, 0.2, 1);
}
```

**Transition Durations:**
```css
:root {
  --duration-instant: 0.15s;
  --duration-fast: 0.3s;      /* UI interactions */
  --duration-normal: 0.6s;    /* Complex animations */
  --duration-slow: 1s;        /* Page transitions */
}
```

**Specific Animation Examples:**

**1. Progress Pulse (Notification Highlight):**
```css
@keyframes aniCountPulse {
  0% {
    transform: scale(1);
    opacity: 1;
  }
  50% {
    transform: scale(1.1);
    opacity: 0.8;
  }
  100% {
    transform: scale(1);
    opacity: 1;
  }
}

.notification-badge {
  animation: aniCountPulse 2s ease-in-out infinite;
}
```

**2. Dropdown Reveal:**
```css
@keyframes aniDropdownHideShow {
  0% {
    visibility: hidden;
    max-height: 0;
    opacity: 0;
  }
  1% {
    visibility: visible;
  }
  100% {
    max-height: 500px;
    opacity: 1;
  }
}

.dropdown {
  animation: aniDropdownHideShow 0.3s ease-out forwards;
}
```

**3. Loading Spinner:**
```css
@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.spinner {
  animation: spin 0.6s linear infinite;
}
```

**4. Button Loading Animation:**
```css
@keyframes buttonLoadMore {
  0%, 100% {
    clip-path: inset(0 0 0 0);
  }
  25% {
    clip-path: inset(0 0 100% 0);
  }
  50% {
    clip-path: inset(0 100% 0 0);
  }
  75% {
    clip-path: inset(100% 0 0 0);
  }
}

.btn-load-more {
  position: relative;
}

.btn-load-more::after {
  content: '';
  position: absolute;
  inset: 0;
  border: 2px solid currentColor;
  animation: buttonLoadMore 2s ease-in-out infinite;
}
```

### Micro-Interactions from Award Winners

**Hover States (0.3s transitions):**
```css
.card {
  transition: transform 0.3s var(--ease-out),
              box-shadow 0.3s var(--ease-out);
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.15);
}
```

**Focus States:**
```css
.input:focus {
  outline: 2px solid var(--primary);
  outline-offset: 2px;
  transition: outline-offset 0.2s var(--ease-out);
}
```

**Modal Overlays (Subtle Depth):**
```css
.modal-backdrop {
  background: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(8px);
  transition: opacity 0.3s var(--ease-out);
}

.modal-content {
  transform: scale(0.95);
  opacity: 0;
  transition: all 0.3s var(--ease-out);
}

.modal.open .modal-content {
  transform: scale(1);
  opacity: 1;
}
```

### Award-Winning Smooth Scroll Implementation

**Lenis Smooth Scroll (Popular in 2023-2024):**
```javascript
import Lenis from '@studio-freight/lenis';

const lenis = new Lenis({
  duration: 1.2,
  easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
  direction: 'vertical',
  smooth: true,
  smoothTouch: false,
  touchMultiplier: 2
});

function raf(time) {
  lenis.raf(time);
  requestAnimationFrame(raf);
}

requestAnimationFrame(raf);
```

**Combine with GSAP:**
```javascript
lenis.on('scroll', ScrollTrigger.update);

gsap.ticker.add((time) => {
  lenis.raf(time * 1000);
});

gsap.ticker.lagSmoothing(0);
```

---

## Component Patterns

### Hero Section Patterns (B2B SaaS)

**Award-Winning Formula (2023-2024):**

**Source:** [22 Best B2B Hero Sections](https://saaswebsites.com/22-best-b2b-hero-sections-on-saas-homepage/)

**Four Essential Elements:**
1. **Headline** - Takes <3 seconds to understand
2. **Subheadline** - Adds context
3. **Visual** - Product screenshot or demonstration
4. **CTA** - Primary + secondary options

**HTML Structure:**
```html
<section class="hero">
  <div class="container">
    <div class="hero-content">
      <!-- Headline with gradient effect -->
      <h1 class="hero-headline">
        Financial infrastructure to
        <span class="gradient-text">grow your revenue</span>
      </h1>

      <!-- Subheadline for context -->
      <p class="hero-subheadline">
        Join millions of businesses using Stripe to accept
        payments and manage their revenue operations.
      </p>

      <!-- CTA Group -->
      <div class="hero-cta">
        <button class="btn-primary">Start now →</button>
        <button class="btn-secondary">Contact sales</button>
      </div>

      <!-- Trust indicators -->
      <div class="hero-social-proof">
        <p class="text-small">Trusted by 50+ of the Fortune 100</p>
        <div class="logo-cloud">
          <!-- Customer logos -->
        </div>
      </div>
    </div>

    <!-- Visual element -->
    <div class="hero-visual">
      <img src="product-screenshot.png" alt="Product interface" />
    </div>
  </div>
</section>
```

**CSS for Hero:**
```css
.hero {
  min-height: 90vh;
  display: flex;
  align-items: center;
  padding: var(--space-20) 0;
}

.hero-headline {
  font-size: clamp(2.5rem, 5vw, 4rem);
  font-weight: 700;
  line-height: 1.1;
  letter-spacing: -0.02em;
  margin-bottom: var(--space-6);
}

.gradient-text {
  background: linear-gradient(135deg, #635BFF 0%, #8B5CF6 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero-subheadline {
  font-size: clamp(1.125rem, 2vw, 1.5rem);
  color: var(--text-secondary);
  max-width: 600px;
  margin-bottom: var(--space-8);
  line-height: 1.6;
}

.hero-cta {
  display: flex;
  gap: var(--space-4);
  flex-wrap: wrap;
  margin-bottom: var(--space-12);
}

.hero-visual {
  position: relative;
  animation: floatIn 1s ease-out;
}

@keyframes floatIn {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```

### CTA Button Patterns

**Primary CTA (High Contrast):**
```css
.btn-primary {
  background: var(--primary);
  color: #FFFFFF;
  padding: var(--space-4) var(--space-8);
  border-radius: 8px;
  font-weight: 600;
  font-size: 1rem;
  border: none;
  cursor: pointer;
  transition: all 0.3s var(--ease-out);
  position: relative;
  overflow: hidden;
}

.btn-primary::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    135deg,
    rgba(255, 255, 255, 0.2),
    rgba(255, 255, 255, 0)
  );
  transform: translateX(-100%);
  transition: transform 0.6s ease;
}

.btn-primary:hover::before {
  transform: translateX(100%);
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 16px rgba(99, 91, 255, 0.4);
}
```

**Secondary CTA (Subtle):**
```css
.btn-secondary {
  background: transparent;
  color: var(--text-primary);
  padding: var(--space-4) var(--space-8);
  border-radius: 8px;
  font-weight: 600;
  font-size: 1rem;
  border: 2px solid var(--border);
  cursor: pointer;
  transition: all 0.3s var(--ease-out);
}

.btn-secondary:hover {
  border-color: var(--primary);
  color: var(--primary);
  background: rgba(99, 91, 255, 0.05);
}
```

### Card Components

**Lusion v3 Card Pattern:**
```html
<article class="card">
  <div class="card-image">
    <img src="thumbnail.jpg" alt="Card image" />
    <div class="card-badge">Featured</div>
  </div>
  <div class="card-content">
    <h3 class="card-title">Card Title</h3>
    <p class="card-description">Brief description of the content...</p>
    <div class="card-meta">
      <span class="card-date">Jan 15, 2024</span>
      <span class="card-category">Design</span>
    </div>
  </div>
</article>
```

```css
.card {
  background: var(--background-secondary);
  border-radius: 12px;
  overflow: hidden;
  transition: all 0.3s var(--ease-out);
  cursor: pointer;
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
}

.card-image {
  position: relative;
  aspect-ratio: 16 / 9;
  overflow: hidden;
}

.card-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.6s var(--ease-out);
}

.card:hover .card-image img {
  transform: scale(1.05);
}

.card-badge {
  position: absolute;
  top: var(--space-4);
  right: var(--space-4);
  background: var(--accent-orange);
  color: white;
  padding: var(--space-2) var(--space-4);
  border-radius: 6px;
  font-size: 0.875rem;
  font-weight: 600;
}

.card-content {
  padding: var(--space-6);
}

.card-title {
  font-size: 1.25rem;
  font-weight: 700;
  margin-bottom: var(--space-3);
  line-height: 1.3;
}

.card-description {
  color: var(--text-secondary);
  line-height: 1.6;
  margin-bottom: var(--space-4);
}

.card-meta {
  display: flex;
  gap: var(--space-4);
  font-size: 0.875rem;
  color: var(--text-tertiary);
}
```

### Feature Section (Bento Grid Pattern)

**Trending Pattern in 2023-2024:**
```html
<section class="features">
  <div class="container">
    <h2 class="section-title">Everything you need</h2>

    <div class="bento-grid">
      <div class="feature-card feature-large">
        <h3>Lightning Fast</h3>
        <p>Built for performance from the ground up</p>
        <div class="feature-visual">
          <!-- SVG or image -->
        </div>
      </div>

      <div class="feature-card feature-wide">
        <h3>Secure by Default</h3>
        <p>Enterprise-grade security</p>
      </div>

      <div class="feature-card">
        <h3>Global Scale</h3>
        <p>Deploy worldwide</p>
      </div>

      <div class="feature-card feature-tall">
        <h3>Real-time Analytics</h3>
        <p>Track everything that matters</p>
      </div>
    </div>
  </div>
</section>
```

```css
.bento-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: var(--space-4);
  margin-top: var(--space-12);
}

@media (min-width: 1024px) {
  .bento-grid {
    grid-template-columns: repeat(4, 1fr);
    grid-template-rows: repeat(3, 200px);
  }

  .feature-large {
    grid-column: span 2;
    grid-row: span 2;
  }

  .feature-wide {
    grid-column: span 2;
  }

  .feature-tall {
    grid-row: span 2;
  }
}

.feature-card {
  background: linear-gradient(
    135deg,
    rgba(255, 255, 255, 0.1) 0%,
    rgba(255, 255, 255, 0.05) 100%
  );
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: var(--space-8);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  transition: all 0.3s var(--ease-out);
}

.feature-card:hover {
  border-color: var(--primary);
  transform: translateY(-4px);
  box-shadow: 0 12px 32px rgba(99, 91, 255, 0.2);
}
```

### Navigation Patterns

**Minimalist Header (Linear/Vercel Pattern):**
```html
<header class="header">
  <div class="container">
    <nav class="nav">
      <div class="nav-logo">
        <a href="/">
          <img src="logo.svg" alt="Company" />
        </a>
      </div>

      <div class="nav-links">
        <a href="#features">Features</a>
        <a href="#pricing">Pricing</a>
        <a href="#docs">Docs</a>
      </div>

      <div class="nav-cta">
        <button class="btn-secondary">Sign in</button>
        <button class="btn-primary">Get started</button>
      </div>

      <button class="nav-toggle" aria-label="Menu">
        <span></span>
        <span></span>
        <span></span>
      </button>
    </nav>
  </div>
</header>
```

```css
.header {
  position: sticky;
  top: 0;
  background: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--border);
  z-index: 100;
  transition: all 0.3s var(--ease-out);
}

.header.scrolled {
  background: rgba(255, 255, 255, 0.95);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

.nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 64px;
}

.nav-links {
  display: flex;
  gap: var(--space-8);
}

.nav-links a {
  color: var(--text-primary);
  text-decoration: none;
  font-weight: 500;
  font-size: 0.9375rem;
  transition: color 0.2s ease;
  position: relative;
}

.nav-links a::after {
  content: '';
  position: absolute;
  bottom: -4px;
  left: 0;
  width: 0;
  height: 2px;
  background: var(--primary);
  transition: width 0.3s var(--ease-out);
}

.nav-links a:hover {
  color: var(--primary);
}

.nav-links a:hover::after {
  width: 100%;
}

.nav-cta {
  display: flex;
  gap: var(--space-4);
}

/* Mobile menu toggle */
.nav-toggle {
  display: none;
  flex-direction: column;
  gap: 4px;
  background: none;
  border: none;
  cursor: pointer;
}

.nav-toggle span {
  width: 24px;
  height: 2px;
  background: var(--text-primary);
  transition: all 0.3s ease;
}

@media (max-width: 768px) {
  .nav-links,
  .nav-cta {
    display: none;
  }

  .nav-toggle {
    display: flex;
  }
}
```

### Form Components

**Modern Input Fields:**
```css
.input-group {
  position: relative;
  margin-bottom: var(--space-6);
}

.input-label {
  display: block;
  font-size: 0.875rem;
  font-weight: 600;
  margin-bottom: var(--space-2);
  color: var(--text-primary);
}

.input-field {
  width: 100%;
  padding: var(--space-4);
  border: 2px solid var(--border);
  border-radius: 8px;
  font-size: 1rem;
  background: var(--background);
  color: var(--text-primary);
  transition: all 0.3s var(--ease-out);
}

.input-field:focus {
  outline: none;
  border-color: var(--primary);
  box-shadow: 0 0 0 4px rgba(99, 91, 255, 0.1);
}

.input-field::placeholder {
  color: var(--text-quaternary);
}

/* Floating label effect */
.input-floating {
  position: relative;
}

.input-floating .input-label {
  position: absolute;
  top: 50%;
  left: var(--space-4);
  transform: translateY(-50%);
  transition: all 0.3s var(--ease-out);
  pointer-events: none;
}

.input-floating .input-field:focus + .input-label,
.input-floating .input-field:not(:placeholder-shown) + .input-label {
  top: 0;
  font-size: 0.75rem;
  background: var(--background);
  padding: 0 var(--space-2);
}
```

---

## Content Strategy

### Value Proposition Frameworks

**Award-Winning Pattern Analysis:**

**Source:** [How to Build Effective B2B SaaS Website Design](https://duck.design/b2b-saas-website-design/)

### 1. Feature → Benefit Translation

**Bad (Feature-focused):**
> "Our platform uses AI-powered algorithms with 99.9% uptime"

**Good (Benefit-focused):**
> "Focus on growth while we handle the infrastructure. Never worry about downtime again."

**Stripe's Approach:**
- **Headline:** "Financial infrastructure to grow your revenue"
- **Benefit-first:** Focuses on outcome (growth) not technology
- **Clear value:** Immediately understand what you get

### 2. Three-Second Rule

**Your headline must answer:**
1. What does this do?
2. Who is it for?
3. Why should I care?

**Examples from Award Winners:**

**Linear:**
> "The issue tracking tool you'll enjoy using"
- **What:** Issue tracking
- **Who:** Teams (implied)
- **Why:** Enjoyable to use (addresses pain point)

**Vercel:**
> "Develop. Preview. Ship. For the best frontend teams"
- **What:** Development platform
- **Who:** Frontend teams
- **Why:** Best teams use it (social proof + aspiration)

**Notion:**
> "One workspace. Every team."
- **What:** Workspace
- **Who:** Teams
- **Why:** Consolidation (solves tool sprawl)

### 3. Content Hierarchy Formula

**Award-Winning Page Structure:**

```
1. Hero Section
   ├─ Headline (What + Why)
   ├─ Subheadline (How + For Whom)
   ├─ Primary CTA (Action-oriented)
   ├─ Secondary CTA (Low-commitment)
   └─ Social Proof (Logos or stat)

2. Problem Statement
   ├─ Acknowledge pain points
   └─ Show you understand their world

3. Solution Overview
   ├─ How it works (3-5 steps max)
   └─ Visual demonstration

4. Feature Showcase
   ├─ Benefits-first approach
   ├─ Visual + text pairing
   └─ Proof points for each claim

5. Social Proof
   ├─ Customer logos
   ├─ Testimonials with photos
   ├─ Case studies
   └─ Stats/metrics

6. Final CTA
   ├─ Restate value
   └─ Remove friction
```

### 4. Copywriting Patterns

**Action-Oriented CTAs from Award Winners:**

**Weak CTAs:**
- Submit
- Learn More
- Click Here

**Strong CTAs (Award-Winning):**
- "Start building for free" (Vercel)
- "Get started" (Linear)
- "Start now →" (Stripe)
- "Try for free" (Notion)
- "See how it works" (Show, don't tell)

**Pattern:** Verb + Outcome or Verb + No-Risk

### 5. Scannable Content Structure

**Visual Hierarchy Techniques:**

```html
<section class="content-section">
  <!-- Overline for context -->
  <span class="overline">For Engineering Teams</span>

  <!-- Main headline -->
  <h2 class="section-headline">
    Build faster with better tools
  </h2>

  <!-- Supporting description -->
  <p class="section-description">
    Everything your team needs to ship quality software,
    faster than ever before.
  </p>

  <!-- Scannable feature list -->
  <ul class="feature-list">
    <li>
      <strong>Real-time collaboration</strong> —
      Work together without stepping on toes
    </li>
    <li>
      <strong>Automated workflows</strong> —
      Save hours every week
    </li>
    <li>
      <strong>Deep integrations</strong> —
      Connect your entire stack
    </li>
  </ul>
</section>
```

**CSS for Scannable Content:**
```css
.overline {
  display: inline-block;
  font-size: 0.875rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--primary);
  margin-bottom: var(--space-4);
}

.section-headline {
  font-size: clamp(2rem, 4vw, 3rem);
  font-weight: 700;
  line-height: 1.2;
  margin-bottom: var(--space-4);
}

.section-description {
  font-size: 1.125rem;
  line-height: 1.7;
  color: var(--text-secondary);
  max-width: 65ch; /* Optimal reading width */
  margin-bottom: var(--space-8);
}

.feature-list {
  list-style: none;
  padding: 0;
}

.feature-list li {
  padding-left: var(--space-8);
  margin-bottom: var(--space-4);
  position: relative;
  line-height: 1.6;
}

.feature-list li::before {
  content: '✓';
  position: absolute;
  left: 0;
  color: var(--primary);
  font-weight: bold;
}

.feature-list strong {
  color: var(--text-primary);
}
```

### 6. Social Proof Techniques

**Stripe's Approach:**
```html
<div class="social-proof">
  <p class="proof-stat">
    <strong>135+</strong> currencies supported
  </p>
  <p class="proof-stat">
    <strong>$1.4T</strong> processed annually
  </p>
  <p class="proof-stat">
    <strong>99.999%</strong> historical uptime
  </p>
</div>

<div class="customer-logos">
  <p class="logos-intro">Trusted by 50+ of the Fortune 100</p>
  <div class="logos-grid">
    <img src="amazon.svg" alt="Amazon" />
    <img src="shopify.svg" alt="Shopify" />
    <img src="figma.svg" alt="Figma" />
    <!-- etc -->
  </div>
</div>
```

**Testimonial Pattern:**
```html
<blockquote class="testimonial">
  <div class="testimonial-content">
    <p class="testimonial-quote">
      "Linear helped us ship 3x faster. The interface is so
      intuitive that onboarding new engineers takes minutes,
      not days."
    </p>
  </div>
  <footer class="testimonial-author">
    <img
      src="headshot.jpg"
      alt="Sarah Chen"
      class="author-photo"
    />
    <div class="author-info">
      <cite class="author-name">Sarah Chen</cite>
      <p class="author-title">VP Engineering, Acme Corp</p>
    </div>
  </footer>
</blockquote>
```

```css
.testimonial {
  background: var(--background-secondary);
  border-left: 4px solid var(--primary);
  padding: var(--space-8);
  border-radius: 12px;
  margin: 0;
}

.testimonial-quote {
  font-size: 1.25rem;
  line-height: 1.6;
  color: var(--text-primary);
  margin-bottom: var(--space-6);
  font-style: italic;
}

.testimonial-author {
  display: flex;
  align-items: center;
  gap: var(--space-4);
}

.author-photo {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  object-fit: cover;
}

.author-name {
  font-weight: 600;
  font-style: normal;
  display: block;
}

.author-title {
  font-size: 0.875rem;
  color: var(--text-secondary);
  margin-top: var(--space-1);
}
```

### 7. Writing for Developers (Tech SaaS Pattern)

**Vercel's Developer-First Content:**

```html
<section class="code-showcase">
  <div class="content-side">
    <h2>Deploy in seconds</h2>
    <p>
      Push to Git and watch your site go live.
      Zero configuration required.
    </p>

    <ul class="check-list">
      <li>Automatic HTTPS</li>
      <li>Global CDN</li>
      <li>Instant rollbacks</li>
    </ul>
  </div>

  <div class="code-side">
    <pre><code class="language-bash">$ git push origin main

Deploying to production...
✓ Build completed in 23s
✓ Deployed to https://your-site.vercel.app

Preview: https://git-abc123.vercel.app</code></pre>
  </div>
</section>
```

**Key Patterns:**
- Show, don't just tell
- Use real code examples
- Monospace fonts for code blocks
- Syntax highlighting
- Terminal-like aesthetics

---

## Code Examples

### Complete Award-Winning Page Template

**HTML Structure:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Award-Winning SaaS Template</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <!-- Header with sticky navigation -->
  <header class="header" id="header">
    <div class="container">
      <nav class="nav">
        <div class="nav-logo">
          <a href="/">
            <svg width="32" height="32" viewBox="0 0 32 32">
              <!-- Your logo SVG -->
            </svg>
          </a>
        </div>

        <div class="nav-links">
          <a href="#features">Features</a>
          <a href="#pricing">Pricing</a>
          <a href="#docs">Docs</a>
        </div>

        <div class="nav-cta">
          <button class="btn-secondary">Sign in</button>
          <button class="btn-primary">Get started</button>
        </div>
      </nav>
    </div>
  </header>

  <!-- Hero Section -->
  <section class="hero">
    <div class="container">
      <div class="hero-content">
        <span class="overline">For Modern Teams</span>

        <h1 class="hero-headline">
          Build products that
          <span class="gradient-text">customers love</span>
        </h1>

        <p class="hero-subheadline">
          The all-in-one platform that helps you ship faster,
          collaborate better, and scale without limits.
        </p>

        <div class="hero-cta">
          <button class="btn-primary btn-large">
            Start building for free →
          </button>
          <button class="btn-secondary btn-large">
            See how it works
          </button>
        </div>

        <div class="hero-social-proof">
          <div class="stats">
            <div class="stat">
              <strong>10K+</strong>
              <span>Teams</span>
            </div>
            <div class="stat">
              <strong>99.99%</strong>
              <span>Uptime</span>
            </div>
            <div class="stat">
              <strong>24/7</strong>
              <span>Support</span>
            </div>
          </div>
        </div>
      </div>

      <div class="hero-visual">
        <div class="hero-image-wrapper">
          <img
            src="product-screenshot.png"
            alt="Product interface"
            class="hero-image"
          />
          <div class="hero-gradient-bg"></div>
        </div>
      </div>
    </div>
  </section>

  <!-- Features Section with Bento Grid -->
  <section class="features">
    <div class="container">
      <div class="section-header">
        <span class="overline">Features</span>
        <h2 class="section-headline">Everything you need</h2>
        <p class="section-description">
          Powerful features that help you work smarter, not harder.
        </p>
      </div>

      <div class="bento-grid">
        <div class="feature-card feature-large">
          <div class="feature-icon">⚡</div>
          <h3>Lightning Fast</h3>
          <p>Built for performance from the ground up</p>
          <div class="feature-visual">
            <!-- SVG or animated element -->
          </div>
        </div>

        <div class="feature-card feature-wide">
          <div class="feature-icon">🔒</div>
          <h3>Secure by Default</h3>
          <p>Enterprise-grade security built in</p>
        </div>

        <div class="feature-card">
          <div class="feature-icon">🌍</div>
          <h3>Global Scale</h3>
          <p>Deploy worldwide in seconds</p>
        </div>

        <div class="feature-card feature-tall">
          <div class="feature-icon">📊</div>
          <h3>Real-time Analytics</h3>
          <p>Track everything that matters</p>
        </div>

        <div class="feature-card">
          <div class="feature-icon">🔄</div>
          <h3>Auto Updates</h3>
          <p>Always on the latest version</p>
        </div>

        <div class="feature-card">
          <div class="feature-icon">🎨</div>
          <h3>Customizable</h3>
          <p>Make it yours with themes</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Social Proof Section -->
  <section class="social-proof">
    <div class="container">
      <p class="proof-intro">Trusted by leading companies</p>
      <div class="logo-cloud">
        <!-- Company logos -->
      </div>

      <div class="testimonials">
        <blockquote class="testimonial">
          <p class="testimonial-quote">
            "This tool completely transformed how our team works.
            We ship 3x faster now."
          </p>
          <footer class="testimonial-author">
            <img src="avatar1.jpg" alt="Sarah Chen" class="author-photo" />
            <div class="author-info">
              <cite class="author-name">Sarah Chen</cite>
              <p class="author-title">VP Engineering, Acme Corp</p>
            </div>
          </footer>
        </blockquote>
      </div>
    </div>
  </section>

  <!-- Final CTA -->
  <section class="cta-final">
    <div class="container">
      <div class="cta-content">
        <h2>Ready to get started?</h2>
        <p>Join thousands of teams building better products.</p>
        <button class="btn-primary btn-large">
          Start building for free →
        </button>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <svg width="32" height="32" viewBox="0 0 32 32">
            <!-- Logo -->
          </svg>
          <p>Building the future of work.</p>
        </div>

        <div class="footer-links">
          <h4>Product</h4>
          <a href="#features">Features</a>
          <a href="#pricing">Pricing</a>
          <a href="#changelog">Changelog</a>
        </div>

        <div class="footer-links">
          <h4>Company</h4>
          <a href="#about">About</a>
          <a href="#blog">Blog</a>
          <a href="#careers">Careers</a>
        </div>

        <div class="footer-links">
          <h4>Resources</h4>
          <a href="#docs">Documentation</a>
          <a href="#support">Support</a>
          <a href="#status">Status</a>
        </div>
      </div>

      <div class="footer-bottom">
        <p>&copy; 2024 Your Company. All rights reserved.</p>
      </div>
    </div>
  </footer>

  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
  <script src="script.js"></script>
</body>
</html>
```

### Complete CSS (styles.css)

```css
/* ===================================
   CSS CUSTOM PROPERTIES (DESIGN TOKENS)
   =================================== */

:root {
  /* Colors */
  --primary: #635BFF;
  --primary-hover: #5047E5;
  --background: #FFFFFF;
  --background-secondary: #F9FAFB;
  --text-primary: #0A2540;
  --text-secondary: #425466;
  --text-tertiary: #6B7280;
  --text-quaternary: #9CA3AF;
  --border: #E6E6E6;
  --border-hover: #D1D5DB;

  /* Spacing (4px baseline) */
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-5: 20px;
  --space-6: 24px;
  --space-8: 32px;
  --space-10: 40px;
  --space-12: 48px;
  --space-16: 64px;
  --space-20: 80px;
  --space-24: 96px;

  /* Container widths */
  --container-sm: 640px;
  --container-md: 768px;
  --container-lg: 1024px;
  --container-xl: 1280px;
  --container-2xl: 1536px;

  /* Typography */
  --font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;

  /* Timing */
  --duration-instant: 0.15s;
  --duration-fast: 0.3s;
  --duration-normal: 0.6s;
  --duration-slow: 1s;

  /* Easing */
  --ease-in-out: cubic-bezier(0.42, 0, 0.58, 1);
  --ease-out: cubic-bezier(0, 0, 0.58, 1);
  --ease-smooth: cubic-bezier(0.4, 0, 0.2, 1);

  /* Shadows */
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.07);
  --shadow-lg: 0 12px 24px rgba(0, 0, 0, 0.1);
  --shadow-xl: 0 24px 48px rgba(0, 0, 0, 0.15);
}

/* Dark mode */
@media (prefers-color-scheme: dark) {
  :root {
    --background: #0A0A0A;
    --background-secondary: #1A1A1A;
    --text-primary: #FFFFFF;
    --text-secondary: rgba(255, 255, 255, 0.8);
    --text-tertiary: rgba(255, 255, 255, 0.6);
    --text-quaternary: rgba(255, 255, 255, 0.4);
    --border: #2A2A2A;
    --border-hover: #3A3A3A;
  }
}

/* ===================================
   RESET & BASE STYLES
   =================================== */

*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  font-size: 16px;
  scroll-behavior: smooth;
}

body {
  font-family: var(--font-family);
  line-height: 1.6;
  color: var(--text-primary);
  background: var(--background);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

img {
  max-width: 100%;
  height: auto;
  display: block;
}

/* ===================================
   TYPOGRAPHY
   =================================== */

h1, h2, h3, h4, h5, h6 {
  font-weight: 700;
  line-height: 1.2;
  text-wrap: balance;
  letter-spacing: -0.02em;
}

a {
  color: var(--primary);
  text-decoration: none;
  transition: color var(--duration-fast) var(--ease-out);
}

a:hover {
  color: var(--primary-hover);
}

/* ===================================
   LAYOUT CONTAINERS
   =================================== */

.container {
  width: 100%;
  max-width: var(--container-xl);
  margin-left: auto;
  margin-right: auto;
  padding-left: var(--space-6);
  padding-right: var(--space-6);
}

@media (min-width: 640px) {
  .container {
    padding-left: var(--space-8);
    padding-right: var(--space-8);
  }
}

/* ===================================
   HEADER & NAVIGATION
   =================================== */

.header {
  position: sticky;
  top: 0;
  background: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--border);
  z-index: 100;
  transition: all var(--duration-fast) var(--ease-out);
}

.header.scrolled {
  background: rgba(255, 255, 255, 0.95);
  box-shadow: var(--shadow-sm);
}

.nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 64px;
}

.nav-logo svg {
  display: block;
}

.nav-links {
  display: flex;
  gap: var(--space-8);
}

.nav-links a {
  color: var(--text-primary);
  font-weight: 500;
  font-size: 0.9375rem;
  position: relative;
}

.nav-links a::after {
  content: '';
  position: absolute;
  bottom: -4px;
  left: 0;
  width: 0;
  height: 2px;
  background: var(--primary);
  transition: width var(--duration-fast) var(--ease-out);
}

.nav-links a:hover::after {
  width: 100%;
}

.nav-cta {
  display: flex;
  gap: var(--space-4);
}

/* ===================================
   BUTTONS
   =================================== */

.btn-primary {
  background: var(--primary);
  color: #FFFFFF;
  padding: var(--space-4) var(--space-8);
  border-radius: 8px;
  font-weight: 600;
  font-size: 1rem;
  border: none;
  cursor: pointer;
  transition: all var(--duration-fast) var(--ease-out);
  position: relative;
  overflow: hidden;
}

.btn-primary::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    135deg,
    rgba(255, 255, 255, 0.2),
    rgba(255, 255, 255, 0)
  );
  transform: translateX(-100%);
  transition: transform var(--duration-normal) ease;
}

.btn-primary:hover::before {
  transform: translateX(100%);
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 16px rgba(99, 91, 255, 0.4);
}

.btn-primary:active {
  transform: translateY(0);
}

.btn-secondary {
  background: transparent;
  color: var(--text-primary);
  padding: var(--space-4) var(--space-8);
  border-radius: 8px;
  font-weight: 600;
  font-size: 1rem;
  border: 2px solid var(--border);
  cursor: pointer;
  transition: all var(--duration-fast) var(--ease-out);
}

.btn-secondary:hover {
  border-color: var(--primary);
  color: var(--primary);
  background: rgba(99, 91, 255, 0.05);
}

.btn-large {
  padding: var(--space-5) var(--space-12);
  font-size: 1.125rem;
}

/* ===================================
   HERO SECTION
   =================================== */

.hero {
  min-height: 90vh;
  display: flex;
  align-items: center;
  padding: var(--space-20) 0;
  position: relative;
  overflow: hidden;
}

.hero .container {
  display: grid;
  grid-template-columns: 1fr;
  gap: var(--space-12);
  align-items: center;
}

@media (min-width: 1024px) {
  .hero .container {
    grid-template-columns: 1fr 1fr;
    gap: var(--space-16);
  }
}

.hero-content {
  z-index: 2;
}

.overline {
  display: inline-block;
  font-size: 0.875rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--primary);
  margin-bottom: var(--space-4);
}

.hero-headline {
  font-size: clamp(2.5rem, 5vw, 4rem);
  font-weight: 700;
  line-height: 1.1;
  letter-spacing: -0.02em;
  margin-bottom: var(--space-6);
}

.gradient-text {
  background: linear-gradient(135deg, #635BFF 0%, #8B5CF6 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero-subheadline {
  font-size: clamp(1.125rem, 2vw, 1.5rem);
  color: var(--text-secondary);
  max-width: 600px;
  margin-bottom: var(--space-8);
  line-height: 1.6;
}

.hero-cta {
  display: flex;
  gap: var(--space-4);
  flex-wrap: wrap;
  margin-bottom: var(--space-12);
}

.hero-social-proof .stats {
  display: flex;
  gap: var(--space-8);
  flex-wrap: wrap;
}

.stat {
  display: flex;
  flex-direction: column;
}

.stat strong {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--text-primary);
}

.stat span {
  font-size: 0.875rem;
  color: var(--text-tertiary);
}

.hero-visual {
  position: relative;
  animation: floatIn var(--duration-slow) var(--ease-out);
}

.hero-image-wrapper {
  position: relative;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: var(--shadow-xl);
}

.hero-image {
  width: 100%;
  height: auto;
  display: block;
}

.hero-gradient-bg {
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: radial-gradient(
    circle,
    rgba(99, 91, 255, 0.1) 0%,
    transparent 70%
  );
  z-index: -1;
  animation: rotate 20s linear infinite;
}

@keyframes floatIn {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes rotate {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

/* ===================================
   FEATURES SECTION
   =================================== */

.features {
  padding: var(--space-24) 0;
  background: var(--background-secondary);
}

.section-header {
  text-align: center;
  max-width: 800px;
  margin: 0 auto var(--space-16);
}

.section-headline {
  font-size: clamp(2rem, 4vw, 3rem);
  margin-bottom: var(--space-4);
}

.section-description {
  font-size: 1.125rem;
  line-height: 1.7;
  color: var(--text-secondary);
  max-width: 65ch;
  margin: 0 auto;
}

.bento-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: var(--space-4);
  margin-top: var(--space-12);
}

@media (min-width: 1024px) {
  .bento-grid {
    grid-template-columns: repeat(4, 1fr);
    grid-template-rows: repeat(3, 200px);
  }

  .feature-large {
    grid-column: span 2;
    grid-row: span 2;
  }

  .feature-wide {
    grid-column: span 2;
  }

  .feature-tall {
    grid-row: span 2;
  }
}

.feature-card {
  background: linear-gradient(
    135deg,
    rgba(255, 255, 255, 0.1) 0%,
    rgba(255, 255, 255, 0.05) 100%
  );
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: var(--space-8);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  transition: all var(--duration-fast) var(--ease-out);
  cursor: pointer;
}

.feature-card:hover {
  border-color: var(--primary);
  transform: translateY(-4px);
  box-shadow: 0 12px 32px rgba(99, 91, 255, 0.2);
}

.feature-icon {
  font-size: 2rem;
  margin-bottom: var(--space-4);
}

.feature-card h3 {
  font-size: 1.25rem;
  margin-bottom: var(--space-2);
}

.feature-card p {
  color: var(--text-secondary);
  line-height: 1.6;
}

/* ===================================
   SOCIAL PROOF SECTION
   =================================== */

.social-proof {
  padding: var(--space-24) 0;
}

.proof-intro {
  text-align: center;
  font-size: 0.875rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--text-tertiary);
  margin-bottom: var(--space-8);
}

.logo-cloud {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
  gap: var(--space-8);
  margin-bottom: var(--space-16);
}

.testimonials {
  max-width: 800px;
  margin: 0 auto;
}

.testimonial {
  background: var(--background-secondary);
  border-left: 4px solid var(--primary);
  padding: var(--space-8);
  border-radius: 12px;
  margin: 0;
}

.testimonial-quote {
  font-size: 1.25rem;
  line-height: 1.6;
  color: var(--text-primary);
  margin-bottom: var(--space-6);
  font-style: italic;
}

.testimonial-author {
  display: flex;
  align-items: center;
  gap: var(--space-4);
}

.author-photo {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  object-fit: cover;
}

.author-name {
  font-weight: 600;
  font-style: normal;
  display: block;
}

.author-title {
  font-size: 0.875rem;
  color: var(--text-secondary);
  margin-top: var(--space-1);
}

/* ===================================
   FINAL CTA SECTION
   =================================== */

.cta-final {
  padding: var(--space-24) 0;
  background: linear-gradient(
    135deg,
    rgba(99, 91, 255, 0.1) 0%,
    rgba(139, 92, 246, 0.05) 100%
  );
}

.cta-content {
  text-align: center;
  max-width: 600px;
  margin: 0 auto;
}

.cta-content h2 {
  font-size: clamp(2rem, 4vw, 3rem);
  margin-bottom: var(--space-4);
}

.cta-content p {
  font-size: 1.25rem;
  color: var(--text-secondary);
  margin-bottom: var(--space-8);
}

/* ===================================
   FOOTER
   =================================== */

.footer {
  padding: var(--space-16) 0 var(--space-8);
  background: var(--background-secondary);
  border-top: 1px solid var(--border);
}

.footer-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: var(--space-12);
  margin-bottom: var(--space-8);
}

.footer-brand p {
  margin-top: var(--space-4);
  color: var(--text-secondary);
  max-width: 30ch;
}

.footer-links {
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
}

.footer-links h4 {
  font-size: 0.875rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  margin-bottom: var(--space-2);
}

.footer-links a {
  color: var(--text-secondary);
  font-size: 0.9375rem;
}

.footer-links a:hover {
  color: var(--primary);
}

.footer-bottom {
  text-align: center;
  padding-top: var(--space-8);
  border-top: 1px solid var(--border);
}

.footer-bottom p {
  color: var(--text-tertiary);
  font-size: 0.875rem;
}

/* ===================================
   UTILITIES
   =================================== */

.text-center {
  text-align: center;
}

.mt-4 { margin-top: var(--space-4); }
.mt-8 { margin-top: var(--space-8); }
.mb-4 { margin-bottom: var(--space-4); }
.mb-8 { margin-bottom: var(--space-8); }
```

### Complete JavaScript (script.js)

```javascript
// ===================================
// GSAP SCROLL ANIMATIONS
// ===================================

gsap.registerPlugin(ScrollTrigger);

// Animate hero content on load
gsap.from('.hero-content > *', {
  duration: 0.8,
  y: 30,
  opacity: 0,
  stagger: 0.15,
  ease: 'power3.out'
});

// Parallax effect on hero image
gsap.to('.hero-visual', {
  scrollTrigger: {
    trigger: '.hero',
    start: 'top top',
    end: 'bottom top',
    scrub: 1
  },
  y: 100,
  opacity: 0.5
});

// Animate feature cards on scroll
gsap.utils.toArray('.feature-card').forEach((card, i) => {
  gsap.from(card, {
    scrollTrigger: {
      trigger: card,
      start: 'top 80%',
      end: 'top 50%',
      scrub: 1
    },
    y: 50,
    opacity: 0,
    duration: 0.6,
    delay: i * 0.1
  });
});

// Testimonial reveal
gsap.from('.testimonial', {
  scrollTrigger: {
    trigger: '.testimonial',
    start: 'top 80%',
    toggleActions: 'play none none reverse'
  },
  x: -50,
  opacity: 0,
  duration: 0.8,
  ease: 'power3.out'
});

// ===================================
// HEADER SCROLL EFFECT
// ===================================

const header = document.getElementById('header');
let lastScroll = 0;

window.addEventListener('scroll', () => {
  const currentScroll = window.pageYOffset;

  if (currentScroll > 100) {
    header.classList.add('scrolled');
  } else {
    header.classList.remove('scrolled');
  }

  lastScroll = currentScroll;
});

// ===================================
// SMOOTH SCROLL FOR ANCHOR LINKS
// ===================================

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));

    if (target) {
      const headerHeight = header.offsetHeight;
      const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - headerHeight;

      window.scrollTo({
        top: targetPosition,
        behavior: 'smooth'
      });
    }
  });
});

// ===================================
// INTERSECTION OBSERVER FOR LAZY LOADING
// ===================================

const imageObserver = new IntersectionObserver((entries, observer) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const img = entry.target;
      img.src = img.dataset.src;
      img.classList.add('loaded');
      observer.unobserve(img);
    }
  });
}, {
  rootMargin: '50px'
});

document.querySelectorAll('img[data-src]').forEach(img => {
  imageObserver.observe(img);
});

// ===================================
// FEATURE CARD HOVER TILT EFFECT
// ===================================

document.querySelectorAll('.feature-card').forEach(card => {
  card.addEventListener('mousemove', (e) => {
    const rect = card.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;

    const centerX = rect.width / 2;
    const centerY = rect.height / 2;

    const rotateX = (y - centerY) / 10;
    const rotateY = (centerX - x) / 10;

    card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-4px)`;
  });

  card.addEventListener('mouseleave', () => {
    card.style.transform = '';
  });
});

// ===================================
// STATS COUNTER ANIMATION
// ===================================

function animateCounter(element, target, duration = 2000) {
  const start = 0;
  const increment = target / (duration / 16);
  let current = start;

  const timer = setInterval(() => {
    current += increment;
    if (current >= target) {
      element.textContent = target;
      clearInterval(timer);
    } else {
      element.textContent = Math.floor(current);
    }
  }, 16);
}

// Trigger counter animation on scroll
const statsObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const stat = entry.target;
      const targetValue = parseInt(stat.dataset.target);
      animateCounter(stat, targetValue);
      statsObserver.unobserve(stat);
    }
  });
}, { threshold: 0.5 });

document.querySelectorAll('.stat strong').forEach(stat => {
  statsObserver.observe(stat);
});
```

---

## Implementation Guide

### Step 1: Foundation Setup

**1.1 Choose Your Tech Stack:**

**Option A: Static Site (Fastest)**
- HTML + CSS + Vanilla JS
- GSAP for animations
- Perfect for landing pages

**Option B: React/Next.js (Modern)**
- Next.js 14+ with App Router
- Framer Motion for animations
- Tailwind CSS (optional)
- Best for isn.biz (developer-friendly)

**Option C: Existing Framework**
- Integrate patterns into current stack
- Use CSS variables for consistency

**1.2 Install Dependencies:**

```bash
# For Next.js setup
npx create-next-app@latest isn-biz --typescript --tailwind --app
cd isn-biz

# Install animation libraries
npm install gsap framer-motion

# Install fonts
npm install @next/font
```

**1.3 Set Up Design Tokens:**

Create `/styles/tokens.css`:
```css
/* Copy the CSS custom properties section from above */
```

### Step 2: Typography Implementation

**2.1 Load Inter Font:**

In Next.js `app/layout.tsx`:
```tsx
import { Inter } from 'next/font/google';

const inter = Inter({
  subsets: ['latin'],
  variable: '--font-inter',
  display: 'swap',
});

export default function RootLayout({ children }) {
  return (
    <html lang="en" className={inter.variable}>
      <body>{children}</body>
    </html>
  );
}
```

**2.2 Create Typography Components:**

`/components/Typography.tsx`:
```tsx
import React from 'react';

export const Headline = ({ children, className = '' }) => (
  <h1 className={`hero-headline ${className}`}>
    {children}
  </h1>
);

export const Subheadline = ({ children, className = '' }) => (
  <p className={`hero-subheadline ${className}`}>
    {children}
  </p>
);

export const GradientText = ({ children }) => (
  <span className="gradient-text">{children}</span>
);
```

### Step 3: Color System Setup

**3.1 Create Theme Context (for dark/light mode):**

```tsx
'use client';

import { createContext, useContext, useEffect, useState } from 'react';

const ThemeContext = createContext({
  theme: 'light',
  toggleTheme: () => {},
});

export function ThemeProvider({ children }) {
  const [theme, setTheme] = useState('light');

  useEffect(() => {
    const stored = localStorage.getItem('theme');
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    setTheme(stored || (prefersDark ? 'dark' : 'light'));
  }, []);

  const toggleTheme = () => {
    const newTheme = theme === 'light' ? 'dark' : 'light';
    setTheme(newTheme);
    localStorage.setItem('theme', newTheme);
    document.documentElement.setAttribute('data-theme', newTheme);
  };

  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  );
}

export const useTheme = () => useContext(ThemeContext);
```

### Step 4: Component Library Creation

**4.1 Button Components:**

`/components/Button.tsx`:
```tsx
import React from 'react';

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'secondary';
  size?: 'normal' | 'large';
  children: React.ReactNode;
}

export const Button: React.FC<ButtonProps> = ({
  variant = 'primary',
  size = 'normal',
  children,
  className = '',
  ...props
}) => {
  const baseClass = `btn-${variant} ${size === 'large' ? 'btn-large' : ''}`;

  return (
    <button className={`${baseClass} ${className}`} {...props}>
      {children}
    </button>
  );
};
```

**4.2 Card Component:**

`/components/Card.tsx`:
```tsx
import React from 'react';

interface CardProps {
  image?: string;
  badge?: string;
  title: string;
  description: string;
  meta?: { date?: string; category?: string };
}

export const Card: React.FC<CardProps> = ({
  image,
  badge,
  title,
  description,
  meta
}) => {
  return (
    <article className="card">
      {image && (
        <div className="card-image">
          <img src={image} alt={title} />
          {badge && <div className="card-badge">{badge}</div>}
        </div>
      )}
      <div className="card-content">
        <h3 className="card-title">{title}</h3>
        <p className="card-description">{description}</p>
        {meta && (
          <div className="card-meta">
            {meta.date && <span className="card-date">{meta.date}</span>}
            {meta.category && <span className="card-category">{meta.category}</span>}
          </div>
        )}
      </div>
    </article>
  );
};
```

### Step 5: Animation Setup

**5.1 GSAP Configuration:**

`/lib/gsap.ts`:
```typescript
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

if (typeof window !== 'undefined') {
  gsap.registerPlugin(ScrollTrigger);
}

export { gsap, ScrollTrigger };
```

**5.2 Framer Motion Variants:**

`/lib/motion-variants.ts`:
```typescript
export const fadeInUp = {
  hidden: { opacity: 0, y: 20 },
  visible: {
    opacity: 1,
    y: 0,
    transition: {
      duration: 0.6,
      ease: [0.4, 0, 0.2, 1]
    }
  }
};

export const staggerContainer = {
  hidden: { opacity: 0 },
  visible: {
    opacity: 1,
    transition: {
      staggerChildren: 0.1
    }
  }
};

export const scaleIn = {
  hidden: { scale: 0.95, opacity: 0 },
  visible: {
    scale: 1,
    opacity: 1,
    transition: {
      duration: 0.4,
      ease: [0.4, 0, 0.2, 1]
    }
  }
};
```

### Step 6: Page Assembly

**6.1 Create Hero Section:**

`/components/sections/Hero.tsx`:
```tsx
'use client';

import { motion } from 'framer-motion';
import { Button } from '@/components/Button';
import { GradientText } from '@/components/Typography';
import { fadeInUp, staggerContainer } from '@/lib/motion-variants';

export const Hero = () => {
  return (
    <section className="hero">
      <div className="container">
        <motion.div
          className="hero-content"
          variants={staggerContainer}
          initial="hidden"
          animate="visible"
        >
          <motion.span className="overline" variants={fadeInUp}>
            For Modern Teams
          </motion.span>

          <motion.h1 className="hero-headline" variants={fadeInUp}>
            Build products that{' '}
            <GradientText>customers love</GradientText>
          </motion.h1>

          <motion.p className="hero-subheadline" variants={fadeInUp}>
            The all-in-one platform that helps you ship faster,
            collaborate better, and scale without limits.
          </motion.p>

          <motion.div className="hero-cta" variants={fadeInUp}>
            <Button variant="primary" size="large">
              Start building for free →
            </Button>
            <Button variant="secondary" size="large">
              See how it works
            </Button>
          </motion.div>

          <motion.div className="hero-social-proof" variants={fadeInUp}>
            <div className="stats">
              <div className="stat">
                <strong>10K+</strong>
                <span>Teams</span>
              </div>
              <div className="stat">
                <strong>99.99%</strong>
                <span>Uptime</span>
              </div>
              <div className="stat">
                <strong>24/7</strong>
                <span>Support</span>
              </div>
            </div>
          </motion.div>
        </motion.div>

        <motion.div
          className="hero-visual"
          initial={{ opacity: 0, x: 20 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.8, delay: 0.3 }}
        >
          <div className="hero-image-wrapper">
            <img
              src="/product-screenshot.png"
              alt="Product interface"
              className="hero-image"
            />
            <div className="hero-gradient-bg" />
          </div>
        </motion.div>
      </div>
    </section>
  );
};
```

### Step 7: Performance Optimization

**7.1 Image Optimization:**

Use Next.js Image component:
```tsx
import Image from 'next/image';

<Image
  src="/product-screenshot.png"
  alt="Product interface"
  width={1200}
  height={800}
  priority
  quality={90}
/>
```

**7.2 Lazy Load Animations:**

```tsx
'use client';

import { useEffect, useRef } from 'react';
import { gsap } from '@/lib/gsap';

export const LazySection = ({ children }) => {
  const sectionRef = useRef(null);

  useEffect(() => {
    const element = sectionRef.current;

    gsap.from(element, {
      scrollTrigger: {
        trigger: element,
        start: 'top 80%',
        toggleActions: 'play none none reverse'
      },
      y: 50,
      opacity: 0,
      duration: 0.8
    });
  }, []);

  return <div ref={sectionRef}>{children}</div>;
};
```

### Step 8: Testing & Refinement

**8.1 Performance Checklist:**
- [ ] Lighthouse score >90 for all metrics
- [ ] Images optimized (WebP format)
- [ ] Animations run at 60fps
- [ ] CSS bundle <50KB gzipped
- [ ] JS bundle <200KB gzipped
- [ ] Time to Interactive <3s

**8.2 Accessibility Checklist:**
- [ ] All images have alt text
- [ ] Color contrast ratio >4.5:1
- [ ] Keyboard navigation works
- [ ] Screen reader tested
- [ ] Focus states visible
- [ ] ARIA labels where needed

**8.3 Cross-Browser Testing:**
- [ ] Chrome/Edge (latest)
- [ ] Firefox (latest)
- [ ] Safari (latest)
- [ ] Mobile Safari (iOS)
- [ ] Chrome Mobile (Android)

---

## Key Takeaways for isn.biz

### 1. **Typography Wins**
- Use Inter font (industry standard for SaaS)
- Implement fluid typography with `clamp()`
- Maintain clear hierarchy
- Use text-wrap: balance for headlines

### 2. **Minimalist Color Schemes**
- Start with monochromatic base
- Add 1-2 accent colors maximum
- Use gradients sparingly but effectively
- Dark mode is expected in 2024

### 3. **Performance Matters**
- GSAP is the gold standard for animations
- ScrollTrigger for scroll-based effects
- Keep animations purposeful, not decorative
- 60fps or nothing

### 4. **Grid System**
- 4px baseline for flexibility
- 8px linear scale for major spacing
- CSS Grid for layouts
- Flexbox for components

### 5. **Content First**
- Benefits over features
- Three-second rule for headlines
- Show, don't just tell
- Social proof everywhere

### 6. **Component Patterns**
- Hero: Headline + Sub + Visual + CTA
- Features: Bento grid layout
- Cards: Image + Content + Meta
- CTAs: Primary + Secondary options

### 7. **Modern Techniques**
- Container queries
- CSS custom properties
- Backdrop filters
- View transitions (coming)

---

## Sources & References

### Award Organizations
- [Awwwards](https://www.awwwards.com/)
- [CSS Design Awards](https://www.cssdesignawards.com/)
- [The Webby Awards](https://www.webbyawards.com/)
- [FWA - Favourite Website Awards](https://thefwa.com/)

### Design Inspiration
- [50 Gorgeous Color Schemes](https://visme.co/blog/website-color-schemes/)
- [29 Beautiful Color Schemes](https://digitalsynopsis.com/design/website-color-schemes-palettes-combinations/)
- [Best B2B SaaS Websites](https://azurodigital.com/saas-website-examples/)
- [22 Best B2B Hero Sections](https://saaswebsites.com/22-best-b2b-hero-sections-on-saas-homepage/)

### Technical Resources
- [GSAP Official](https://gsap.com/)
- [Framer Motion](https://www.framer.com/motion/)
- [CSS Gradient Generator](https://cssgradient.io/)
- [Modern Fluid Typography](https://www.smashingmagazine.com/2022/01/modern-fluid-typography-css-clamp/)
- [4px Grid System](https://blog.designary.com/p/layout-basics-grid-systems-and-the-4px-grid)

### Specific Site Analysis
- [Linear](https://linear.app)
- [Stripe](https://stripe.com)
- [Vercel](https://vercel.com)
- [Notion](https://notion.so)
- [Lusion v3](https://www.awwwards.com/sites/lusion-v3)

---

## Next Steps for isn.biz

1. **Audit Current Site**
   - Measure against these patterns
   - Identify quick wins
   - Plan phased rollout

2. **Implement Foundation**
   - Design tokens (colors, spacing, typography)
   - Component library
   - Animation system

3. **Build Pages**
   - Start with homepage hero
   - Add feature sections
   - Implement social proof

4. **Optimize & Test**
   - Performance testing
   - Accessibility audit
   - User testing

5. **Iterate & Improve**
   - A/B test CTAs
   - Monitor analytics
   - Gather feedback

---

**Document Version:** 1.0
**Last Updated:** February 2026
**Next Review:** Quarterly (May 2026)
