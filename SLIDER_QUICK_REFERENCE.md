# Slider Gallery - Quick Reference Guide

**Last Updated:** 2026-02-02

## Access the Slider

**Local File:** `D:\workspace\ISNBIZ_Files\slider-gallery.html`

**Live URL (when deployed):**
- Development: Open `slider-gallery.html` in browser
- Production: `https://isn.biz/slider-gallery.html`

## What's Included

### 1. Full-Screen Portfolio Slider (Component 1)
- **Type:** 3D Coverflow effect
- **Slides:** 8 professional tech-themed images
- **Features:** Auto-play, keyboard navigation, touch gestures
- **Images:** 1536x1024 WebP format from S3

**Slides:**
1. Modern Software Engineering
2. AI & Machine Learning
3. Enterprise Infrastructure
4. Cloud Solutions
5. Business Intelligence
6. Advanced AI Processing
7. Team Collaboration
8. Enterprise Security

### 2. Technology Stack Carousel (Component 2)
- **Type:** Auto-rotating infinite loop
- **Items:** 8 technology badges
- **Features:** Free scrolling, responsive breakpoints

### 3. Thumbnail Navigation Gallery (Component 3)
- **Type:** Synchronized main + thumbnail sliders
- **Images:** Same 8 slider images
- **Features:** Click thumbnails to navigate

## Image URLs

All images hosted on S3:
```
https://isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com/premium_v3/slider/slider_[1-8].webp
```

### Individual URLs
```
slider_1: Software engineering workspace
slider_2: AI neural networks
slider_3: Data center servers
slider_4: Cloud computing visualization
slider_5: Business analytics dashboard
slider_6: AI processing streams
slider_7: Team collaboration workspace
slider_8: Cybersecurity blockchain
```

## Customization Guide

### Change Slide Content

Edit `slider-gallery.html`, find the slide (lines 73-241):

```html
<div class="swiper-slide">
    <div class="slide-content">
        <div class="slide-background" style="background: url('IMAGE_URL') center/cover no-repeat;">
            <div class="slide-pattern"></div>
        </div>
        <div class="slide-info">
            <span class="slide-number">01</span>
            <h3 class="slide-title">Your Title</h3>
            <p class="slide-description">Your description...</p>
            <div class="slide-tags">
                <span class="tag">Tag 1</span>
                <span class="tag">Tag 2</span>
            </div>
            <div class="slide-metrics">
                <div class="metric">
                    <span class="metric-value">Value</span>
                    <span class="metric-label">Label</span>
                </div>
            </div>
            <a href="link.html" class="btn btn-primary"><span>Button Text</span></a>
        </div>
    </div>
</div>
```

### Adjust Slider Settings

Edit `slider-init.js` (or inline in slider-gallery.html):

```javascript
const portfolioSwiper = new Swiper('.portfolio-swiper', {
  effect: 'coverflow',           // Change effect: 'slide', 'fade', 'cube', 'flip'
  grabCursor: true,
  centeredSlides: true,
  slidesPerView: 'auto',
  coverflowEffect: {
    rotate: 50,                  // Adjust rotation (0-180)
    stretch: 0,                  // Stretch distance
    depth: 100,                  // Depth offset
    modifier: 1,                 // Effect multiplier
    slideShadows: true,          // Enable/disable shadows
  },
  autoplay: {
    delay: 5000,                 // 5 seconds between slides
    disableOnInteraction: false,
    pauseOnMouseEnter: true,
  },
  speed: 600,                    // Transition speed (ms)
  pagination: { clickable: true },
  navigation: true,
  keyboard: { enabled: true },
});
```

### Add More Slides

1. Generate new images using `generate_slider_images.py`
2. Upload to S3 using `upload_slider_to_s3.py`
3. Copy slide HTML template and paste after last slide
4. Update image URL, title, description, tags, metrics, and link

## Regenerating Images

### Step 1: Edit Prompts

Edit `generate_slider_images.py`, modify the `PROMPTS` array:

```python
PROMPTS = [
    {
        "filename": "slider_9.webp",
        "prompt": "Your detailed prompt here, professional tech theme, blue and cyan colors, 8k quality"
    },
    # Add more...
]
```

### Step 2: Generate

```bash
cd D:\workspace\ISNBIZ_Files
python generate_slider_images.py
```

### Step 3: Upload to S3

```bash
python upload_slider_to_s3.py
```

### Step 4: Update HTML

Copy the HTML snippets from the script output and paste into `slider-gallery.html`.

## Styling Customization

### Colors

Edit `slider-styles.css`:

```css
:root {
    --slider-primary: #1E9FF2;    /* Brand blue */
    --slider-secondary: #5FDFDF;  /* Cyan accent */
    --slider-dark: #3F4447;       /* Charcoal */
}
```

### Animations

Adjust transition speeds in `slider-init.js`:

```javascript
speed: 600,              // Transition duration
autoplay: { delay: 5000 } // Auto-play delay
```

## Responsive Breakpoints

Current breakpoints (in `slider-init.js`):

```javascript
breakpoints: {
    640: { slidesPerView: 3 },   // Mobile
    768: { slidesPerView: 4 },   // Tablet
    1024: { slidesPerView: 5 },  // Desktop
}
```

## Browser Support

✅ **Fully Supported:**
- Chrome/Edge (all versions)
- Firefox 65+
- Safari 14+
- Opera 35+

⚠️ **Limited Support:**
- IE11 (WebP not supported, consider JPEG fallback)

## Performance

### Current Performance
- **Image Total:** ~2.6 MB for all 8 images
- **Average Size:** ~325 KB per image
- **Format:** WebP (50-70% smaller than JPEG)
- **CDN:** S3 with 1-year cache
- **Load Time:** <3 seconds on average connection

### Optimization Tips
1. Images already optimized (WebP format)
2. CDN caching enabled (1 year)
3. Lazy loading can be added for off-screen slides
4. Consider responsive images for mobile (smaller versions)

## Testing Checklist

Before deploying:

- [ ] Open `slider-gallery.html` in browser
- [ ] Test all 8 slides load correctly
- [ ] Verify auto-play works
- [ ] Test keyboard navigation (arrow keys)
- [ ] Test mouse/touch gestures (swipe)
- [ ] Check mobile responsiveness
- [ ] Verify all links work
- [ ] Test on multiple browsers
- [ ] Check console for errors
- [ ] Verify S3 images load

## Common Issues

### Images Not Loading
**Problem:** 404 errors on image URLs
**Solution:**
- Verify S3 bucket policy allows public read
- Check image URLs are correct
- Run `python upload_slider_to_s3.py` again

### Slider Not Auto-Playing
**Problem:** Slider doesn't advance automatically
**Solution:**
- Check `autoplay` setting in slider-init.js
- Verify JavaScript loaded without errors
- Check browser console for errors

### Slider Navigation Not Working
**Problem:** Can't click through slides
**Solution:**
- Verify Swiper JS library loaded (check <head>)
- Check slider-init.js is loaded
- Inspect browser console for errors

### Images Load Slowly
**Problem:** Long initial load time
**Solution:**
- Images already optimized (WebP)
- Consider CloudFront CDN for faster delivery
- Implement lazy loading for off-screen slides
- Create smaller mobile versions

## Deployment

### To Netlify
```bash
cd D:\workspace\ISNBIZ_Files
netlify deploy --prod
```

### Manual FTP/SFTP
Upload these files:
- slider-gallery.html
- slider-styles.css
- slider-init.js
- (Images already on S3)

## Maintenance

### Monthly Tasks
- Check S3 usage and costs
- Verify all images load correctly
- Test on new browser versions
- Review slider performance metrics

### Yearly Tasks
- Refresh images with updated designs
- Update content/descriptions
- Review slider library for updates
- Optimize for new web standards

## Resources

### Documentation
- **Swiper JS Docs:** https://swiperjs.com/
- **WebP Guide:** https://developers.google.com/speed/webp
- **AWS S3 Docs:** https://docs.aws.amazon.com/s3/

### Support Files
- `SLIDER_UPDATE_SUMMARY.md` - Complete implementation details
- `generate_slider_images.py` - Image generation script
- `upload_slider_to_s3.py` - S3 upload automation

## Quick Commands

```bash
# Navigate to project
cd D:\workspace\ISNBIZ_Files

# Generate new images
python generate_slider_images.py

# Upload to S3
python upload_slider_to_s3.py

# Open in browser (Windows)
start slider-gallery.html

# Deploy to Netlify
netlify deploy --prod
```

## Support

For issues or questions:
1. Check this guide first
2. Review `SLIDER_UPDATE_SUMMARY.md` for technical details
3. Inspect browser console for JavaScript errors
4. Verify S3 images are accessible
5. Check Swiper JS documentation

---

**Version:** 1.0
**Last Updated:** 2026-02-02
**Maintained by:** jdmal + Claude AI
