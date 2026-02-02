# Video & Slider Components Guide for isn.biz

## Research Summary - Modern Web Component Best Practices (2026)

### Hero Background Videos

#### Best Practices
- **Duration**: 15-30 seconds maximum to prevent user fatigue
- **Resolution**: 720p (1280×720) for most sites, 1080p if file size permits
- **Frame Rate**: 24-30 fps for optimal performance
- **Bitrate**: 1,000-2,500 kbps using variable bitrate (VBR)
- **Autoplay**: Always muted, hidden controls
- **Mobile**: Display static images or CSS animations instead
- **Accessibility**: Provide captions, pause controls, and static alternatives
- **Performance**: Use lazy loading, test page without video fallback

**Sources:**
- [Web Design Trends 2026 - Ginger IT Solutions](https://www.gingeritsolutions.com/blog/web-design-trends-2026/)
- [Autoplaying Hero Background Videos - Harvard Design System](https://designsystem.harvardsites.harvard.edu/news/2025/02/autoplaying-hero-background-videos-digital-design)
- [Optimize Silent Background Video - Design TLC](https://designtlc.com/how-to-optimize-a-silent-background-video-for-your-websites-hero-area/)

---

### Swiper.js (Modern Carousel Library)

#### Why Swiper.js?
- Most popular mobile-friendly slider (2026 standard)
- Hardware-accelerated transitions
- Touch-enabled interactions
- Framework agnostic (React, Vue, vanilla JS)
- WCAG 2.2 compliant with proper implementation

#### Key Features
- Autoplay with pause/play controls (accessibility required)
- Custom pagination and navigation
- Progress bar synchronization
- Responsive breakpoints
- Lazy loading images
- Loop and autoplay

#### Implementation Requirements
- Keep default Swiper classes intact
- Add pause/play controls for WCAG compliance
- Implement dynamic announcements for screen readers
- Use custom classes alongside default classes

**Sources:**
- [Swiper Official Site](https://swiperjs.com/)
- [Accessible Swiper Carousel - Graceful Web Studio](https://www.gracefulwebstudio.com/blog-articles/accessible-swiper-js-carousel-autoplay-a11y)
- [3-Step Slider Creation with Swiper - Bits Kingdom](https://bitskingdom.com/blog/create-sliders-in-3-steps-with-swiper-js/)

---

### GSAP & ScrollTrigger (Advanced Animations)

#### Capabilities
- Industry standard for scroll-driven animations (2026)
- Parallax effects with multiple speed layers
- Pinned horizontal scroll sections
- Smooth scroll integration (Lenis)
- Framework agnostic

#### Best Practices
- Use `scrub: 1` for fluid parallax tied to scrollbar
- Animate `transform` instead of `top/left` for performance
- Use `will-change` CSS property on animated elements
- Easing: `power2.out` or `none` for scroll-linked effects
- Pin sections with `pin: true` for storytelling

#### Modern Techniques (2026)
- Horizontal scroll on vertical scroll
- Multi-layer parallax depth
- React + GSAP + Lenis integration
- ScrollTrigger with Intersection Observer

**Sources:**
- [GSAP ScrollTrigger Official Docs](https://gsap.com/docs/v3/Plugins/ScrollTrigger/)
- [45 GSAP ScrollTrigger Examples - Free Frontend](https://freefrontend.com/scroll-trigger-js/)
- [Animate Like a Pro with GSAP - ICreator Studio](https://icreatorstudio.com/blog/gsap-scroll-animation-website-tutorial)

---

### AOS (Animate On Scroll)

#### Overview
- Lightweight CSS-driven animation library
- Detects element position, adds animation classes
- Simple data attributes for configuration
- Clean separation of logic and animation

#### Available Animations
- **Fade**: fade, fade-up, fade-down, fade-left, fade-right
- **Fade Diagonal**: fade-up-right, fade-up-left, fade-down-right, fade-down-left
- **Flip**: flip-up, flip-left, flip-right, flip-down
- **Slide**: slide-up, slide-down, slide-left, slide-right
- **Zoom**: zoom-in, zoom-out

#### Best Practices
- Set `data-aos-once="true"` to animate only once
- Use specific `transition-property` for performance
- Configure `data-aos-duration` (300-3000ms)
- Set `data-aos-offset` for trigger point
- Use `data-aos-easing` for animation curves
- Responsive animations with breakpoint conditions

**Sources:**
- [AOS Official Site](https://michalsnik.github.io/aos/)
- [AOS GitHub Repository](https://github.com/michalsnik/aos)
- [Create Ultimate UX with AOS - DEV Community](https://dev.to/ruppysuppy/create-the-ultimate-user-experience-with-aos-animate-on-scroll-39jp)

---

### Animated Counter Statistics

#### Implementation Approach
- Use Intersection Observer API for trigger
- Unobserve after animation to prevent duplicates
- Threshold: 0.3-0.7 (element visibility percentage)
- Legacy browser fallback support

#### Best Practices
- **Performance**: Intersection Observer + CSS most performant
- **Complex Animations**: Use GSAP for advanced counter effects
- **Root Margin**: Add margin around viewport trigger
- **Once Option**: Animate only on first scroll
- **Accessibility**: Ensure final value is always visible

**Sources:**
- [Animated Counter with Intersection Observer - getButterfly](https://getbutterfly.com/animated-javascript-counter-up-with-the-intersection-observer-api/)
- [Scroll-triggered Counter Plugin](https://www.cssscript.com/scroll-triggered-counter/)
- [Intersection Observer vs GSAP - CL Creative](https://www.clcreative.co/blog/should-you-use-the-intersection-observer-api-or-gsap-for-scroll-animations)

---

### Video Players: Video.js vs Plyr

#### Video.js
- **Launched**: 2010
- **Usage**: 450,000+ websites
- **Strengths**: Extensive plugins, HLS/DASH support, live streaming UI
- **Customization**: Custom skins, controls, plugins
- **Trade-off**: Many plugins outdated or unmaintained

#### Plyr
- **Type**: Lightweight, modern HTML5/YouTube/Vimeo player
- **Strengths**: Simple API, responsive, accessible, lightweight
- **Customization**: CSS/JS customizable, keyboard navigation, screen reader support
- **Trade-off**: No plugin system for extensions

#### Recommendation for isn.biz
**Plyr** - Better for simple, professional video showcases with modern UI and accessibility

**Sources:**
- [Video.js vs Plyr Comparison - Slashdot](https://slashdot.org/software/comparison/Plyr-vs-Video.js/)
- [Ultimate HTML5 Video Player Showdown - Cloudinary](https://cloudinary.com/blog/html5_video_player)

---

### AI-Generated Video Options

#### Runway Gen-3 Alpha
- **Launch**: June 2024
- **Capabilities**: Text-to-video, image-to-video
- **Video Length**: 10-11 seconds per clip
- **Quality**: Cinematic visuals, sharp details, fluid movement
- **Business Use**: Background videos, motion previews, concept art animation
- **Advanced Features**: Background removal, video extension, lip sync, motion brush
- **Custom Models**: Collaborate for brand-specific styles

#### Other AI Video Tools (2026)
- **Pika Labs**: Similar text-to-video capabilities
- **Synthesia**: Talking head/avatar videos for explainer content
- **D-ID**: AI avatar videos for presentations

#### Recommended Use for isn.biz
1. **Hero Background**: Generate abstract tech/AI-themed motion graphics
2. **Product Demos**: Animate concept designs or interface mockups
3. **Testimonials**: Create avatar-based testimonials (Synthesia/D-ID)

**Sources:**
- [Runway Gen-3 Alpha Launch - Runway Research](https://runwayml.com/research/introducing-gen-3-alpha)
- [Runway AI Review 2026 - Cybernews](https://cybernews.com/ai-tools/runway-ai-review/)
- [Runway AI Video Generator Features](https://runwayml.com/product)

---

## Component Implementation Strategy for isn.biz

### 1. Hero Video Background
- Generate 20-second abstract AI/tech loop with Runway Gen-3
- Optimize to 720p, H.264, 1500 kbps
- Implement with Plyr for controls
- Static gradient fallback for mobile
- Lazy load after initial page load

### 2. Testimonial Slider
- Swiper.js with autoplay
- Accessibility: pause/play controls
- 3-5 client testimonials with photos
- Progress bar pagination
- Loop and responsive design

### 3. Portfolio Carousel
- Swiper.js with thumbnail navigation
- Lazy loading images
- Custom prev/next arrows
- Modal lightbox for detail view
- Mobile swipe gestures

### 4. Animated Statistics
- Intersection Observer trigger
- Count-up animation on scroll
- GSAP for smooth easing
- Threshold: 0.5 (50% visible)
- Animate once only

### 5. Parallax Scroll Effects
- GSAP ScrollTrigger
- Multi-layer background elements
- Pin hero section on scroll
- Smooth scroll with Lenis
- Mobile-optimized (reduced motion)

### 6. Loading Animations
- Lottie JSON animations for loader
- AOS for section reveals
- Skeleton screens for content
- Progressive image loading

---

## Technology Stack Recommendations

### Core Libraries
1. **Swiper.js** (v11+) - Carousels and sliders
2. **GSAP** (v3+) with ScrollTrigger - Advanced animations
3. **AOS** (v2.3+) - Simple scroll animations
4. **Plyr** (v3.7+) - Video player
5. **Lottie Web** - JSON animations

### Optional Enhancements
- **Lenis** - Smooth scroll
- **CountUp.js** - Animated counters
- **GLightbox** - Lightbox modal

### AI Video Generation
- **Runway Gen-3 Alpha** - Hero backgrounds, product demos
- **Synthesia/D-ID** - Testimonial avatars (optional)

---

## Performance Checklist

- [ ] Videos: 720p, VBR 1000-2500 kbps, 15-30 sec max
- [ ] Lazy load all media assets
- [ ] Mobile: static images instead of video
- [ ] Intersection Observer for scroll triggers
- [ ] Animate `transform` not `top/left`
- [ ] Use `will-change` CSS property
- [ ] Implement skeleton screens
- [ ] Test without JavaScript fallback
- [ ] WCAG 2.2 pause controls for autoplay
- [ ] Prefers-reduced-motion media query

---

## Next Steps

1. Review component designs below
2. Generate AI video assets with Runway Gen-3
3. Implement components in test environment
4. Accessibility audit (WCAG 2.2)
5. Performance testing (Lighthouse)
6. Mobile responsiveness testing
7. Deploy to production

---

*Last Updated: February 2026*
*Research compiled for isn.biz website enhancement project*
