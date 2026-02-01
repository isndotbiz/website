# AI Video Generation Prompts for isn.biz

## Runway Gen-3 Alpha Prompts for Background Videos

### Hero Background Video #1: AI Neural Network
**Duration**: 20 seconds
**Prompt**:
```
Abstract neural network visualization with glowing blue and cyan nodes
connected by flowing data streams, dark charcoal background with subtle
metallic texture, particles flowing through the network, smooth camera
zoom through the network, cinematic lighting with rim lights,
ultra-detailed 4K, professional corporate aesthetic
```

**Settings**:
- Resolution: 1920x1080 (1080p)
- Duration: 20 seconds
- Style: Corporate, Professional, High-tech
- Camera Movement: Slow zoom through
- Color Palette: #1E9FF2 (blue), #5FDFDF (cyan), #3F4447 (charcoal)

---

### Hero Background Video #2: Data Flow
**Duration**: 20 seconds
**Prompt**:
```
Flowing streams of binary code and data particles moving through a
3D grid space, cyan and blue color scheme with dark background,
geometric shapes and wireframe elements, smooth parallax camera
movement, glowing connections forming and dissolving, professional
technology visualization, seamless loop
```

**Settings**:
- Resolution: 1920x1080
- Duration: 20 seconds
- Loop: Yes (seamless)
- Camera: Smooth horizontal drift
- Mood: Futuristic, Clean, Professional

---

### Hero Background Video #3: AI Circuit Board
**Duration**: 20 seconds
**Prompt**:
```
Macro close-up of a futuristic circuit board with glowing blue and
cyan traces, electricity flowing through circuits, subtle camera pan
across the surface, metallic reflections, depth of field blur,
particles of light emanating from connections, dark industrial
background, cinematic quality, technology concept
```

**Settings**:
- Resolution: 1920x1080
- Duration: 20 seconds
- Camera: Slow pan right
- Depth: Shallow depth of field
- Lighting: Dramatic, focused

---

### Product Demo Background #1: Code Interface
**Duration**: 15 seconds
**Prompt**:
```
Split screen showing code being written on the left and 3D
visualizations appearing on the right, holographic interface
elements, futuristic HUD design, blue and cyan accent colors,
clean professional layout, smooth transitions between states,
AI assistant concept visualization
```

**Settings**:
- Resolution: 1920x1080
- Duration: 15 seconds
- Layout: Split screen or picture-in-picture
- Use: Product demonstration overlay

---

### Product Demo Background #2: Automation Flow
**Duration**: 15 seconds
**Prompt**:
```
Isometric view of automated workflow with robotic arms, data flowing
between different nodes, charts and graphs appearing dynamically,
cyan and blue color scheme, smooth camera rotation around the scene,
professional business intelligence dashboard aesthetic, clean
minimalist design
```

**Settings**:
- Resolution: 1920x1080
- Duration: 15 seconds
- View: Isometric 3D
- Movement: 360° rotation

---

## Pika Labs Alternative Prompts

### Abstract Tech Background
**Prompt**:
```
-camera rotate left -motion 3 -gs 8
Floating abstract geometric shapes in blue and cyan gradients,
metallic surfaces reflecting light, particles in motion, dark
background, professional corporate style, 4K quality
```

**Settings**:
- Motion Level: 3
- Guidance Scale: 8
- Camera: Rotate left
- Aspect Ratio: 16:9

---

## Synthesia Testimonial Avatar Setup

### Avatar Style
**Type**: Professional Business Person
**Background**: Blurred office environment or solid color (#f8f9fa)
**Clothing**: Business casual
**Age Range**: 35-50 years old
**Expression**: Confident, friendly, professional

### Testimonial Script #1 - Financial Services
**Avatar**: Professional woman, business attire
**Duration**: 30 seconds
**Script**:
```
Hi, I'm Sarah Chen, CTO at TechVenture Capital. Working with iSN.BiZ
has been transformative for our operations. Their AI-powered automation
reduced our manual processing time by 95%, allowing our team to focus
on strategic initiatives rather than repetitive tasks. The ROI was
immediate and the ongoing support has been exceptional. I highly
recommend their solutions.
```

### Testimonial Script #2 - Enterprise Cloud
**Avatar**: Professional man, business suit
**Duration**: 30 seconds
**Script**:
```
I'm David Thompson, CEO of Enterprise Cloud Services. The iSN.BiZ team's
expertise in self-hosted AI infrastructure saved us over $18,000 annually
in cloud costs while giving us complete control over our data. Their
deep understanding of both AI technology and security requirements makes
them our go-to technology partner. Outstanding work.
```

### Testimonial Script #3 - Healthcare Tech
**Avatar**: Professional woman, medical/tech hybrid attire
**Duration**: 30 seconds
**Script**:
```
Jennifer Park here, Director of Innovation at HealthTech Solutions.
The RAG system implemented by iSN.BiZ revolutionized how we access our
knowledge base. What used to take hours of manual searching now happens
in seconds with incredible accuracy. Their attention to HIPAA compliance
and data security gave us complete confidence in the solution.
```

---

## D-ID Avatar Video Setup

### Avatar Configuration
**Platform**: D-ID Studio
**Avatar Type**: Real person photo-based
**Voice**: Professional, clear, enthusiastic
**Language**: English (US)
**Background**: Branded or neutral corporate

### Use Cases for D-ID
1. **Investor Pitch Introduction** (60 seconds)
2. **Product Feature Explanations** (30 seconds each)
3. **Company Mission Statement** (45 seconds)
4. **Technology Explainer Videos** (90 seconds)

---

## Video Optimization Guidelines

### Pre-Production
- Resolution: Create at 1080p minimum
- Frame Rate: 30 fps for web
- Color Space: sRGB
- Format: MP4 (H.264)

### Encoding Settings (FFmpeg)
```bash
# Convert to web-optimized MP4
ffmpeg -i input.mp4 -vcodec libx264 -crf 23 -preset medium \
  -vf scale=1920:1080 -r 30 -acodec aac -b:a 128k \
  -movflags +faststart output.mp4

# Create WebM version for modern browsers
ffmpeg -i input.mp4 -c:v libvpx-vp9 -b:v 1.5M -c:a libopus \
  -vf scale=1920:1080 -r 30 output.webm

# Create mobile-optimized version (720p)
ffmpeg -i input.mp4 -vcodec libx264 -crf 28 -preset medium \
  -vf scale=1280:720 -r 30 -acodec aac -b:a 96k \
  -movflags +faststart output-mobile.mp4
```

### Post-Production
1. **Trim to exact duration** (15-30 seconds)
2. **Ensure seamless loop** (match first and last frames)
3. **Add fade in/out** (1-2 seconds)
4. **Color grade** to match brand colors
5. **Test on multiple devices**

---

## Video File Structure

```
/assets/
  /videos/
    /hero/
      hero-background.mp4         # Desktop 1080p (1500 kbps)
      hero-background.webm        # Desktop WebM
      hero-background-mobile.jpg  # Mobile fallback image
    /products/
      product-demo.mp4            # Demo video 1080p
      product-demo.webm           # Demo WebM
      captions-en.vtt             # English captions
    /testimonials/
      testimonial-1.mp4           # Avatar video 1
      testimonial-2.mp4           # Avatar video 2
      testimonial-3.mp4           # Avatar video 3
    /thumbnails/
      hero-poster.jpg             # Hero video poster
      demo-poster.jpg             # Demo video poster
```

---

## Brand Guidelines for Video

### Color Palette
- Primary Blue: `#1E9FF2`
- Secondary Cyan: `#5FDFDF`
- Dark Charcoal: `#3F4447`
- Light Background: `#f8f9fa`

### Typography (Text Overlays)
- Primary Font: Space Grotesk (Bold 700)
- Secondary Font: Inter (Regular 400, Medium 600)
- Minimum Size: 24px for readability

### Motion Guidelines
- **Camera Movement**: Slow, smooth, cinematic
- **Transitions**: Fade, dissolve (avoid jarring cuts)
- **Speed**: 0.5x to 1x speed (never fast/chaotic)
- **Easing**: Ease-in-out for professional feel

### Audio (if applicable)
- **Background Music**: Subtle, corporate, inspirational
- **Volume**: -20dB to -15dB (background only)
- **Voiceover**: Clear, professional, enthusiastic but measured
- **Sound Effects**: Minimal, high-quality only

---

## Video Testing Checklist

### Technical
- [ ] Plays on Chrome, Firefox, Safari, Edge
- [ ] Mobile playback (iOS Safari, Android Chrome)
- [ ] File size under 5MB for 20-second clip
- [ ] Seamless loop (no visible jump)
- [ ] Autoplay works when muted
- [ ] Poster image displays before load
- [ ] Accessibility: captions available

### Performance
- [ ] Lazy loading implemented
- [ ] Preload metadata only (not full video)
- [ ] Mobile shows static image (no video load)
- [ ] Video pauses when tab inactive
- [ ] Intersection Observer triggers correctly

### Accessibility
- [ ] Captions/subtitles available (.vtt file)
- [ ] Play/pause controls visible and keyboard accessible
- [ ] Reduced motion preference respected
- [ ] Static fallback for no-video scenarios
- [ ] ARIA labels on video controls

---

## Budget Estimates (2026 Pricing)

### Runway Gen-3 Alpha
- **20-second video**: ~$1.50 - $3.00 per generation
- **Estimated iterations**: 3-5 attempts
- **Total per video**: $5 - $15

### Synthesia
- **Personal Plan**: $30/month (10 videos/month)
- **Business Plan**: $90/month (30 videos/month)
- **Per testimonial**: ~$3 - $10 depending on plan

### D-ID
- **Trial**: 20 credits free (1 video = 1 credit)
- **Lite Plan**: $5.9/month (10 videos)
- **Pro Plan**: $29/month (60 videos)

### Total Project Estimate
- **3 Hero backgrounds** (Runway): $15 - $45
- **2 Product demos** (Runway): $10 - $30
- **4 Testimonials** (Synthesia): $12 - $40
- **Total**: $37 - $115 for complete video library

---

## Timeline

### Week 1: Pre-Production
- Finalize prompts and storyboards
- Create style guide and brand assets
- Set up accounts (Runway, Synthesia, D-ID)

### Week 2: Generation
- Generate hero backgrounds (test multiple prompts)
- Create product demo videos
- Record/generate testimonial avatars

### Week 3: Post-Production
- Edit and optimize all videos
- Create captions and accessibility files
- Generate mobile fallback images
- Encode multiple formats (MP4, WebM)

### Week 4: Integration & Testing
- Implement in HTML/CSS/JS
- Test across devices and browsers
- Accessibility audit
- Performance optimization
- Deploy to production

---

*Last Updated: February 2026*
*Generated for isn.biz video component implementation*
