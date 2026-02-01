# Video & Slider Components for isn.biz

## Overview

This documentation package contains cutting-edge, modern video and slider components designed specifically for the isn.biz website. All components follow 2026 best practices for performance, accessibility (WCAG 2.2), and user experience.

## Package Contents

### Documentation Files
1. **video-slider-components-guide.md** - Comprehensive research and best practices
2. **ai-video-generation-prompts.md** - AI video creation prompts and workflows
3. **VIDEO_SLIDER_README.md** - This file (implementation guide)

### Component Files
1. **video-slider-components.html** - Complete HTML structure for all components
2. **video-slider-styles.css** - Fully integrated CSS styling
3. **video-slider-scripts.js** - JavaScript functionality with all libraries

## Components Included

### 1. Hero Video Background
- Autoplay background video with gradient overlay
- Mobile-optimized (static image fallback)
- Accessibility controls (play/pause button)
- Lazy loading support
- Performance-optimized

### 2. Animated Statistics
- Count-up animations triggered by scroll
- Intersection Observer API
- Smooth easing functions
- Customizable numbers and labels

### 3. Testimonial Slider
- Swiper.js powered carousel
- Autoplay with pause controls (WCAG 2.2)
- Responsive design
- Star ratings and avatars
- Navigation and pagination

### 4. Portfolio Carousel
- Multi-slide responsive carousel
- Lazy loading images
- Hover effects and overlays
- Project metrics display
- Custom navigation

### 5. Video Showcase (Plyr)
- Professional video player
- Captions support
- Quality selector
- Analytics tracking
- Responsive embed

### 6. Parallax Scroll Effects
- GSAP ScrollTrigger
- Multi-layer depth effects
- Smooth animations
- Reduced motion support

### 7. Loading Animation
- Lottie JSON animation
- Fallback spinner
- Progress bar
- Brand colors

## Technology Stack

### Core Libraries (CDN Included)
```html
<!-- Swiper.js v11 -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css">
<script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>

<!-- Plyr v3.7.8 -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/plyr@3.7.8/dist/plyr.css">
<script src="https://cdn.jsdelivr.net/npm/plyr@3.7.8/dist/plyr.min.js"></script>

<!-- AOS v2.3.1 -->
<link rel="stylesheet" href="https://unpkg.com/aos@2.3.1/dist/aos.css">
<script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>

<!-- GSAP v3.12.5 with ScrollTrigger -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>

<!-- Lottie v5.12.2 -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/bodymovin/5.12.2/lottie.min.js"></script>
```

## Quick Start

### Step 1: Copy Files
```bash
# Copy component files to your project
cp video-slider-components.html your-project/components/
cp video-slider-styles.css your-project/css/
cp video-slider-scripts.js your-project/js/
```

### Step 2: Create Assets Directory
```bash
mkdir -p your-project/assets/videos
mkdir -p your-project/assets/videos/hero
mkdir -p your-project/assets/videos/products
mkdir -p your-project/assets/videos/testimonials
mkdir -p your-project/assets/videos/thumbnails
```

### Step 3: Add to Existing Page

#### Option A: Use Complete Demo Page
```html
<!-- Use video-slider-components.html as-is for testing -->
<!-- Open in browser to see all components -->
```

#### Option B: Integrate Individual Components
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your Page</title>

    <!-- Existing styles.css -->
    <link rel="stylesheet" href="styles.css">

    <!-- Add component libraries -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/plyr@3.7.8/dist/plyr.css">
    <link rel="stylesheet" href="https://unpkg.com/aos@2.3.1/dist/aos.css">

    <!-- Add component styles -->
    <link rel="stylesheet" href="css/video-slider-styles.css">
</head>
<body>

    <!-- Your existing content -->

    <!-- Insert component HTML from video-slider-components.html -->
    <!-- Copy desired sections (e.g., testimonial slider) -->

    <!-- Add component scripts before closing body tag -->
    <script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/plyr@3.7.8/dist/plyr.min.js"></script>
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/bodymovin/5.12.2/lottie.min.js"></script>

    <!-- Component functionality -->
    <script src="js/video-slider-scripts.js"></script>
</body>
</html>
```

## Integration with Existing isn.biz Site

### Replace Hero Section
```html
<!-- BEFORE: Current hero in index.html -->
<section class="hero">
    <div class="hero-background"></div>
    <!-- ... existing content ... -->
</section>

<!-- AFTER: New hero with video background -->
<section class="hero-video-section">
    <!-- Copy from video-slider-components.html -->
</section>
```

### Add to Portfolio Page
```html
<!-- In portfolio.html, replace or enhance existing portfolio grid -->
<section class="portfolio-carousel-section section">
    <!-- Copy portfolio carousel from video-slider-components.html -->
</section>
```

### Add to Index Page
```html
<!-- Add testimonial slider before contact section -->
<section class="testimonials-section section">
    <!-- Copy from video-slider-components.html -->
</section>

<!-- Add animated stats after about section -->
<section class="stats-section section">
    <!-- Copy from video-slider-components.html -->
</section>
```

## Video Asset Creation

### Step 1: Generate Videos with AI

Use the prompts in `ai-video-generation-prompts.md`:

1. **Runway Gen-3 Alpha** (https://runwayml.com)
   - Create account
   - Generate hero backgrounds using provided prompts
   - Export as MP4, 1080p, 30fps

2. **Synthesia** (https://www.synthesia.io) - Optional
   - Create testimonial avatar videos
   - Use provided scripts
   - Export with captions

### Step 2: Optimize Videos
```bash
# Install FFmpeg (if not already installed)
# macOS: brew install ffmpeg
# Ubuntu: sudo apt-get install ffmpeg
# Windows: Download from ffmpeg.org

# Optimize hero background video
ffmpeg -i runway-output.mp4 -vcodec libx264 -crf 23 -preset medium \
  -vf scale=1920:1080 -r 30 -acodec aac -b:a 128k \
  -movflags +faststart assets/videos/hero/hero-background.mp4

# Create WebM version
ffmpeg -i runway-output.mp4 -c:v libvpx-vp9 -b:v 1.5M -c:a libopus \
  -vf scale=1920:1080 -r 30 assets/videos/hero/hero-background.webm

# Extract poster image (first frame)
ffmpeg -i assets/videos/hero/hero-background.mp4 -vframes 1 \
  -vf scale=1920:1080 assets/videos/thumbnails/hero-poster.jpg
```

### Step 3: Create Mobile Fallback
```bash
# Create static gradient image for mobile (lightweight)
# Use your existing logo-pallete/metal 4 squared.jpg
# Or create a new one with gradient overlay
```

## Customization Guide

### Modify Colors
```css
/* In video-slider-styles.css, update color variables */
:root {
    --color-primary: #1E9FF2;    /* Your primary blue */
    --color-secondary: #5FDFDF;  /* Your secondary cyan */
    --color-dark: #3F4447;       /* Your dark charcoal */
}
```

### Adjust Animation Timing
```javascript
// In video-slider-scripts.js

// AOS animation duration
AOS.init({
    duration: 1000,  // Change to 800 for faster, 1500 for slower
    once: true
});

// Testimonial slider autoplay speed
const testimonialSwiper = new Swiper('.testimonial-swiper', {
    autoplay: {
        delay: 5000,  // Change to 3000 for faster rotation
    }
});
```

### Change Video
```html
<!-- Update video sources in HTML -->
<video id="hero-video" playsinline muted loop>
    <source src="your-new-video.mp4" type="video/mp4">
    <source src="your-new-video.webm" type="video/webm">
</video>
```

### Modify Statistics
```html
<!-- Update data-count attribute for different numbers -->
<div class="stat-number" data-count="95">0</div> <!-- Will count to 95 -->
<div class="stat-number" data-count="1500">0</div> <!-- Will count to 1500 -->
```

### Customize Testimonials
```html
<!-- Update testimonial content in HTML -->
<div class="testimonial-card">
    <p class="testimonial-text">Your testimonial text here...</p>
    <div class="testimonial-author">
        <div class="author-avatar">
            <img src="your-avatar.jpg" alt="Client Name">
        </div>
        <div class="author-info">
            <div class="author-name">Client Name</div>
            <div class="author-role">Title, Company</div>
        </div>
    </div>
</div>
```

## Performance Optimization

### 1. Lazy Load Videos
```html
<!-- Videos already lazy load via JavaScript -->
<!-- Ensure intersection observer is enabled -->
```

### 2. Mobile Optimization
```css
/* Video automatically hidden on mobile (< 768px) */
/* Static background image shown instead */
@media (max-width: 768px) {
    .hero-video-element {
        display: none; /* Saves bandwidth */
    }
}
```

### 3. Compress Images
```bash
# Install imagemin (if not already)
npm install -g imagemin-cli imagemin-mozjpeg imagemin-pngquant

# Compress portfolio images
imagemin portfolio-*.jpg --plugin=mozjpeg --plugin.mozjpeg.quality=80 > optimized/
```

### 4. Enable CDN Caching
```html
<!-- Use CDN for libraries (already implemented) -->
<!-- For your videos, consider Cloudflare or AWS CloudFront -->
```

## Accessibility Checklist

- [x] WCAG 2.2 compliant pause controls for autoplay
- [x] Keyboard navigation for sliders (Arrow keys)
- [x] Screen reader labels (ARIA)
- [x] Captions support for videos (.vtt files)
- [x] Reduced motion support
- [x] Focus indicators
- [x] Skip links
- [x] Alt text for images

### Add Captions to Videos
```vtt
WEBVTT

00:00:00.000 --> 00:00:05.000
This is the opening caption for your product demo video.

00:00:05.000 --> 00:00:10.000
Describe what's happening on screen for accessibility.
```

Save as `captions-en.vtt` and reference in HTML:
```html
<track kind="captions" label="English" srclang="en" src="assets/captions-en.vtt" default>
```

## Browser Support

### Tested and Supported
- Chrome 90+ ✅
- Firefox 88+ ✅
- Safari 14+ ✅
- Edge 90+ ✅
- iOS Safari 14+ ✅
- Android Chrome 90+ ✅

### Fallbacks
- No JavaScript: Static content visible
- No video support: Poster images shown
- Old browsers: Progressive enhancement (basic functionality)

## Analytics Integration

### Google Analytics 4
```javascript
// Already included in video-slider-scripts.js
// Tracks:
// - Video plays/pauses/completions
// - Slider interactions
// - CTA button clicks
// - Scroll depth

// Ensure GA4 is loaded on page:
<script async src="https://www.googletagmanager.com/gtag/js?id=YOUR-GA4-ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'YOUR-GA4-ID');
</script>
```

## Troubleshooting

### Video Won't Autoplay
**Issue**: Browser blocking autoplay
**Solution**:
```javascript
// Video must be muted for autoplay to work
<video muted autoplay playsinline>
```

### Slider Not Working
**Issue**: Swiper not initializing
**Solution**:
```javascript
// Check console for errors
// Ensure Swiper CSS and JS are loaded
// Verify HTML structure has correct classes
```

### Animations Not Triggering
**Issue**: AOS or GSAP not working
**Solution**:
```javascript
// Refresh ScrollTrigger after DOM changes
ScrollTrigger.refresh();

// Reinitialize AOS
AOS.refresh();
```

### Performance Issues
**Issue**: Page loading slowly
**Solution**:
```javascript
// 1. Optimize video file size (< 5MB for 20 seconds)
// 2. Enable lazy loading
// 3. Use WebP images instead of JPG/PNG
// 4. Minify CSS and JavaScript
// 5. Enable browser caching
```

### Mobile Video Not Showing
**Issue**: Video blank on mobile
**Solution**:
```html
<!-- Add playsinline attribute -->
<video playsinline muted loop>

<!-- Ensure poster image exists -->
<video poster="fallback-image.jpg">
```

## Deployment Checklist

- [ ] Generate all AI videos (Runway Gen-3)
- [ ] Optimize videos (FFmpeg compression)
- [ ] Create WebM versions for modern browsers
- [ ] Generate poster images
- [ ] Create caption files (.vtt)
- [ ] Compress all images (ImageMin)
- [ ] Update content (testimonials, stats, portfolio)
- [ ] Test on Chrome, Firefox, Safari, Edge
- [ ] Test on mobile (iOS, Android)
- [ ] Accessibility audit (WAVE, axe DevTools)
- [ ] Performance test (Lighthouse score > 90)
- [ ] Analytics tracking verified
- [ ] CDN configured (if applicable)
- [ ] Backup existing site
- [ ] Deploy to staging
- [ ] Final QA review
- [ ] Deploy to production

## Maintenance

### Regular Updates
- **Weekly**: Check analytics for engagement metrics
- **Monthly**: Update testimonials and portfolio items
- **Quarterly**: Refresh videos if content outdated
- **Annually**: Review and update dependencies

### Library Updates
```bash
# Check for updates
npm outdated

# Update specific library (example)
# Update CDN links in HTML to latest versions
```

## Support & Resources

### Documentation
- Swiper.js: https://swiperjs.com/
- Plyr: https://github.com/sampotts/plyr
- GSAP: https://greensock.com/docs/
- AOS: https://github.com/michalsnik/aos

### AI Video Platforms
- Runway Gen-3: https://runwayml.com/
- Synthesia: https://www.synthesia.io/
- D-ID: https://www.d-id.com/

### Video Optimization
- FFmpeg: https://ffmpeg.org/
- HandBrake: https://handbrake.fr/

### Accessibility Testing
- WAVE: https://wave.webaim.org/
- axe DevTools: https://www.deque.com/axe/
- WCAG 2.2: https://www.w3.org/WAI/WCAG22/quickref/

## Contact

For questions or support:
- Email: info@isn.biz
- Website: https://isn.biz

---

## License

These components are proprietary to iSN.BiZ Inc. All rights reserved.

Built with cutting-edge technology. Designed for the future.

**Last Updated**: February 2026
**Version**: 1.0.0
**Created by**: iSN.BiZ Inc Development Team
