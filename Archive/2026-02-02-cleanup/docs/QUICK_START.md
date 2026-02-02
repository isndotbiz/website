# Quick Start Guide - Video & Slider Components

## 5-Minute Integration

### Step 1: Add CDN Links (Copy to `<head>`)
```html
<!-- Swiper CSS -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css">

<!-- Plyr CSS -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/plyr@3.7.8/dist/plyr.css">

<!-- AOS CSS -->
<link rel="stylesheet" href="https://unpkg.com/aos@2.3.1/dist/aos.css">

<!-- Component Styles -->
<link rel="stylesheet" href="docs/video-slider-styles.css">
```

### Step 2: Add Scripts (Before `</body>`)
```html
<!-- Libraries -->
<script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/plyr@3.7.8/dist/plyr.min.js"></script>
<script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>

<!-- Component Scripts -->
<script src="docs/video-slider-scripts.js"></script>
```

### Step 3: Insert Component HTML
Copy desired component section from `video-slider-components.html` into your page.

---

## Component Quick Copy

### 1. Testimonial Slider (Most Popular)
**Where**: After services section
**Copy**: Lines 202-434 from `video-slider-components.html`
**Customization**: Update testimonial text, names, photos

### 2. Animated Stats
**Where**: In hero or after about section
**Copy**: Lines 130-200 from `video-slider-components.html`
**Customization**: Change `data-count` values

### 3. Portfolio Carousel
**Where**: Replace existing portfolio grid
**Copy**: Lines 436-580 from `video-slider-components.html`
**Customization**: Update images, project details

### 4. Hero Video Background
**Where**: Replace current hero section
**Copy**: Lines 25-128 from `video-slider-components.html`
**Customization**: Add your video file path

---

## Customization Cheat Sheet

### Change Colors
```css
/* Add to your styles.css */
:root {
    --color-primary: #1E9FF2;
    --color-secondary: #5FDFDF;
    --color-dark: #3F4447;
}
```

### Change Animation Speed
```javascript
// Slower animations
AOS.init({ duration: 1500 });

// Faster slider
autoplay: { delay: 3000 }
```

### Update Statistics
```html
<!-- Count to different number -->
<div class="stat-number" data-count="500">0</div>
<div class="stat-suffix">+</div>
<div class="stat-label">Your Label</div>
```

### Add New Testimonial
```html
<!-- Copy this block inside swiper-wrapper -->
<div class="swiper-slide">
    <div class="testimonial-card">
        <div class="testimonial-quote"><!-- SVG --></div>
        <p class="testimonial-text">Your testimonial...</p>
        <div class="testimonial-author">
            <div class="author-avatar">
                <img src="avatar.jpg" alt="Name">
            </div>
            <div class="author-info">
                <div class="author-name">Name</div>
                <div class="author-role">Title, Company</div>
            </div>
        </div>
        <div class="testimonial-rating">
            <span class="star">★</span><!-- x5 -->
        </div>
    </div>
</div>
```

---

## Video Setup (2 Steps)

### Option A: Use Placeholder (Testing)
```html
<!-- Replace video src with online video -->
<source src="https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4">
```

### Option B: Generate with AI
1. Go to https://runwayml.com
2. Use prompt from `ai-video-generation-prompts.md`
3. Download MP4
4. Optimize with FFmpeg (see README)
5. Upload to `/assets/videos/hero/`

---

## Common Issues & Fixes

### Slider Not Working?
✅ Check Swiper CSS is loaded
✅ Verify HTML structure has correct classes
✅ Open browser console for errors

### Video Won't Autoplay?
✅ Add `muted` attribute
✅ Add `playsinline` for iOS
✅ Check browser console for errors

### Animations Not Smooth?
✅ Add `will-change: transform` to CSS
✅ Reduce motion complexity
✅ Test on actual mobile device

---

## Performance Tips

1. **Optimize Videos**: Keep under 5MB
2. **Lazy Load Images**: Already implemented
3. **Mobile**: Videos hidden on small screens
4. **CDN**: Use for production assets

---

## Test Before Launch

```bash
# Performance
✅ Lighthouse score > 90
✅ Page load < 3 seconds
✅ Mobile friendly test

# Accessibility
✅ WAVE test (0 errors)
✅ Keyboard navigation works
✅ Screen reader compatible

# Cross-Browser
✅ Chrome, Firefox, Safari, Edge
✅ iOS Safari, Android Chrome
```

---

## File Structure
```
isn.biz/
├── index.html                    # Add CDN links here
├── styles.css                    # Your existing styles
├── docs/
│   ├── video-slider-components.html    # Component HTML
│   ├── video-slider-styles.css         # Component CSS
│   ├── video-slider-scripts.js         # Component JS
│   └── VIDEO_SLIDER_README.md          # Full docs
└── assets/
    └── videos/
        ├── hero/
        │   ├── hero-background.mp4
        │   └── hero-background.webm
        └── thumbnails/
            └── hero-poster.jpg
```

---

## Next Steps

1. ✅ Review component demo: Open `video-slider-components.html`
2. ✅ Pick components you want
3. ✅ Copy HTML to your page
4. ✅ Add CDN links
5. ✅ Customize content
6. ✅ Generate/add videos
7. ✅ Test and deploy

---

## Need Help?

📖 **Full Documentation**: `VIDEO_SLIDER_README.md`
🎨 **Customization Guide**: `video-slider-components-guide.md`
🎬 **Video Prompts**: `ai-video-generation-prompts.md`

📧 **Contact**: info@isn.biz

---

**Version**: 1.0.0 | **Updated**: February 2026 | **© iSN.BiZ Inc**
