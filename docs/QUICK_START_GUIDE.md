# Quick Start Guide: Sliders & Galleries for isn.biz
## Get Up and Running in 5 Minutes

**Version:** 1.0
**Date:** February 1, 2026

---

## What's Already Implemented

Your isn.biz website now includes **4 production-ready slider components**:

1. **Portfolio Project Slider** - 3D coverflow effect
2. **Technology Stack Carousel** - Auto-rotating tech showcase
3. **Thumbnail Gallery** - Synchronized main + thumbnail navigation
4. **Features Grid** - Highlighting modern capabilities

---

## File Structure

```
/mnt/d/workspace/ISNBIZ_Files/
├── slider-gallery.html        # Demo page with all components
├── slider-styles.css          # Component styles
├── slider-init.js             # JavaScript initialization
├── styles.css                 # Main site styles (inherited)
└── docs/
    ├── SLIDER_GALLERY_RESEARCH_2026.md
    ├── ADVANCED_SLIDER_PATTERNS.md
    └── QUICK_START_GUIDE.md (this file)
```

---

## Quick Integration

### Step 1: Add to Any Page

**Include CSS (in `<head>`):**
```html
<!-- Swiper 11 CSS -->
<link rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css">

<!-- Custom Slider Styles -->
<link rel="stylesheet" href="slider-styles.css">
```

**Include JavaScript (before `</body>`):**
```html
<!-- Swiper 11 JS -->
<script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>

<!-- Slider Initialization -->
<script src="slider-init.js"></script>
```

---

### Step 2: Choose a Component

#### Option A: Portfolio Slider

**Copy this HTML:**
```html
<div class="swiper portfolio-swiper">
    <div class="swiper-wrapper">
        <!-- Slide 1 -->
        <div class="swiper-slide">
            <div class="slide-content">
                <div class="slide-background"
                     style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);">
                    <div class="slide-pattern"></div>
                </div>
                <div class="slide-info">
                    <span class="slide-number">01</span>
                    <h3 class="slide-title">Your Project Title</h3>
                    <p class="slide-description">Project description goes here.</p>
                    <div class="slide-tags">
                        <span class="tag">AI/ML</span>
                        <span class="tag">Python</span>
                    </div>
                    <a href="#" class="btn btn-primary">View Details</a>
                </div>
            </div>
        </div>

        <!-- Add more slides -->
    </div>

    <!-- Navigation -->
    <div class="swiper-button-prev"></div>
    <div class="swiper-button-next"></div>

    <!-- Pagination -->
    <div class="swiper-pagination"></div>
</div>
```

**Done!** The JavaScript in `slider-init.js` automatically initializes it.

---

#### Option B: Tech Carousel

**Copy this HTML:**
```html
<div class="swiper tech-swiper">
    <div class="swiper-wrapper">
        <div class="swiper-slide tech-slide">
            <div class="tech-item">
                <div class="tech-icon">🤖</div>
                <h4>AI/ML</h4>
                <p>Technology description</p>
            </div>
        </div>

        <!-- Add more tech items -->
    </div>
</div>
```

**Auto-plays and loops automatically!**

---

#### Option C: Thumbnail Gallery

**Copy this HTML:**
```html
<!-- Main Gallery -->
<div class="swiper gallery-main">
    <div class="swiper-wrapper">
        <div class="swiper-slide">
            <div class="gallery-image"
                 style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);">
                <h3>Image 1</h3>
            </div>
        </div>
        <!-- Add more slides -->
    </div>
    <div class="swiper-button-prev"></div>
    <div class="swiper-button-next"></div>
</div>

<!-- Thumbnail Gallery -->
<div class="swiper gallery-thumbs">
    <div class="swiper-wrapper">
        <div class="swiper-slide">
            <div class="thumb-image"
                 style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);"></div>
        </div>
        <!-- Add more thumbnails (must match main) -->
    </div>
</div>
```

**Thumbnails and main slider sync automatically!**

---

## Customization Guide

### Change Colors

All sliders use CSS variables from `styles.css`:

```css
:root {
    --color-primary: #1E9FF2;    /* Brand blue */
    --color-cyan: #5FDFDF;       /* Accent cyan */
    --color-white: #ffffff;
    --spacing-lg: 4rem;
}
```

**To customize:**
```css
/* In your custom CSS */
.portfolio-swiper .swiper-button-next {
    background: #YOUR_COLOR;
}
```

---

### Change Slide Dimensions

**Desktop:**
```css
.portfolio-swiper .swiper-slide {
    width: 700px;  /* Adjust width */
    height: 500px; /* Adjust height */
}
```

**Mobile:**
```css
@media (max-width: 768px) {
    .portfolio-swiper .swiper-slide {
        width: 100%;
        height: 550px;
    }
}
```

---

### Adjust Autoplay Speed

Edit `slider-init.js`:

```javascript
autoplay: {
    delay: 5000,  // 5 seconds (change this)
    pauseOnMouseEnter: true,
}
```

---

### Add More Slides

Just duplicate the slide HTML:

```html
<div class="swiper-slide">
    <!-- Your content -->
</div>
```

Swiper automatically picks up new slides!

---

## Live Demo

**View all components:**
Open `slider-gallery.html` in your browser.

**URL:** `file:///mnt/d/workspace/ISNBIZ_Files/slider-gallery.html`

---

## Common Customizations

### 1. Disable Autoplay

```javascript
// In slider-init.js, comment out:
autoplay: {
    delay: 5000,
},
```

---

### 2. Change Transition Speed

```javascript
speed: 600,  // Milliseconds (change this)
```

---

### 3. Show More Slides on Desktop

```javascript
// For tech carousel
breakpoints: {
    1024: { slidesPerView: 6 },  // Show 6 instead of 5
}
```

---

### 4. Add Lazy Loading to Images

**HTML:**
```html
<img data-src="large-image.jpg" class="swiper-lazy" alt="Description">
<div class="swiper-lazy-preloader"></div>
```

**JavaScript (already enabled in gallery):**
```javascript
lazy: {
    loadPrevNext: true,
}
```

---

## Accessibility Features

✅ **Already Included:**
- Keyboard navigation (arrow keys)
- ARIA labels for screen readers
- Focus indicators
- Reduced motion support
- Semantic HTML

**Test keyboard nav:**
1. Click on slider
2. Press `←` or `→` to navigate
3. Press `Tab` to focus buttons

---

## Performance Tips

### 1. Use WebP Images

```html
<picture>
    <source data-srcset="image.webp" type="image/webp">
    <img data-src="image.jpg" class="swiper-lazy" alt="Fallback">
</picture>
```

### 2. Optimize Image Sizes

- Desktop: max 1920px width
- Mobile: max 800px width
- Compress with [TinyPNG](https://tinypng.com)

### 3. Lazy Load Off-Screen Sliders

Uncomment in `slider-init.js`:

```javascript
// Lines 272-295
const sliderObserver = new IntersectionObserver(...);
```

---

## Troubleshooting

### Slider Not Showing

**Check:**
1. ✅ Swiper CSS included
2. ✅ Swiper JS included
3. ✅ `slider-init.js` included
4. ✅ HTML structure matches examples

**Console errors?**
Press `F12` > Console tab to see errors.

---

### Navigation Buttons Not Working

**Ensure:**
```html
<div class="swiper-button-prev"></div>
<div class="swiper-button-next"></div>
```

Are **inside** the `.swiper` container.

---

### Images Not Loading

**Check:**
- Image paths are correct
- For lazy loading: use `data-src` not `src`
- Include `swiper-lazy-preloader` div

---

## Next Steps

### Add to Existing Pages

**Portfolio Page (`portfolio.html`):**
```html
<!-- Replace static grid with portfolio slider -->
<section id="projects" class="section">
    <div class="container">
        <h2>Our Projects</h2>

        <!-- Insert portfolio slider here -->
        <div class="swiper portfolio-swiper">
            ...
        </div>
    </div>
</section>
```

**Home Page (`index.html`):**
```html
<!-- Add tech carousel to "Solutions" section -->
<section id="solutions" class="section">
    <div class="container">
        <h2>Our Technology Stack</h2>

        <!-- Insert tech carousel here -->
        <div class="swiper tech-swiper">
            ...
        </div>
    </div>
</section>
```

---

## Resources

### Documentation
- **Full Research:** `docs/SLIDER_GALLERY_RESEARCH_2026.md`
- **Advanced Patterns:** `docs/ADVANCED_SLIDER_PATTERNS.md`
- **Swiper Docs:** [swiperjs.com](https://swiperjs.com/)

### Demo
- **Live Components:** `slider-gallery.html`

### Support
- **Email:** info@isn.biz
- **Swiper Community:** [GitHub Issues](https://github.com/nolimits4web/swiper/issues)

---

## Quick Reference

### Essential Classes

| Class | Purpose |
|-------|---------|
| `.swiper` | Main container |
| `.swiper-wrapper` | Slides wrapper |
| `.swiper-slide` | Individual slide |
| `.swiper-button-prev` | Previous button |
| `.swiper-button-next` | Next button |
| `.swiper-pagination` | Pagination dots |

### Breakpoints

| Screen | Width | Slides/View |
|--------|-------|-------------|
| Mobile | < 640px | 2 |
| Tablet | 640-1024px | 3-4 |
| Desktop | > 1024px | 5-6 |

### Timing

| Action | Default Speed |
|--------|---------------|
| Slide transition | 600ms |
| Autoplay delay | 5000ms |
| Hover pause | Yes |

---

## Checklist: Before Going Live

- [ ] Test on Chrome, Firefox, Safari, Edge
- [ ] Test on iOS and Android mobile
- [ ] Verify keyboard navigation works
- [ ] Check ARIA labels with screen reader
- [ ] Optimize all images (WebP + compression)
- [ ] Enable lazy loading for images
- [ ] Test with slow 3G connection
- [ ] Verify reduced motion support
- [ ] Add analytics tracking
- [ ] Run Lighthouse performance audit

---

**You're Ready to Go!**

If you need advanced features like video sliders, parallax effects, or custom transitions, check out `docs/ADVANCED_SLIDER_PATTERNS.md`.

For any questions, refer to the comprehensive research in `docs/SLIDER_GALLERY_RESEARCH_2026.md`.

---

**Happy Sliding! 🎉**

*Prepared by iSN.BiZ Inc Development Team*
*Last Updated: February 1, 2026*
