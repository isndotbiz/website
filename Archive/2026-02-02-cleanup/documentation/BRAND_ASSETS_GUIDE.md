# iSN.BiZ Inc - Brand Assets Guide
**Created:** 2026-02-01
**Location:** /mnt/d/workspace/ISNBIZ_Files/

---

## 🎨 Color Palette

**Primary Colors:**
```css
--primary-blue: #1E9FF2;        /* Bright blue - primary brand color */
--accent-cyan: #5FDFDF;         /* Cyan/turquoise - accents, highlights */
--dark-charcoal: #3F4447;       /* Dark gray - text, primary dark */
--dark-slate: #4A545C;          /* Secondary dark - backgrounds */
--light-gray: #D3D3D3;          /* Light backgrounds, subtle elements */
```

**Usage Guidelines:**
- **Headers/CTAs:** Primary Blue (#1E9FF2)
- **Links/Accents:** Accent Cyan (#5FDFDF)
- **Body Text:** Dark Charcoal (#3F4447)
- **Backgrounds:** Light Gray for light sections, Dark Slate for dark sections
- **Contrast:** Ensure accessibility (WCAG AA minimum)

**Color Relationships:**
- Professional tech aesthetic
- Modern, clean, trustworthy
- Blue = Innovation, reliability
- Cyan = Technology, forward-thinking
- Gray tones = Professionalism, stability

---

## 📐 Logo Assets

### Primary Logo
**File:** `logo-pallete/ISS.jpg`
- **Size:** 4096 x 3112 px (1.1MB)
- **Format:** JPEG
- **Use:** High-resolution, print, large web displays
- **Aspect Ratio:** ~1.3:1

### Horizontal Logos (White)
**File:** `logo-pallete/ISS white long.jpg`
- **Size:** 4000 x 1350 px (152KB)
- **Format:** JPEG
- **Use:** Website headers, dark backgrounds
- **Aspect Ratio:** ~3:1 (wide)

**File:** `logo-pallete/ISS white long cut.jpg`
- **Size:** 2420 x 960 px (139KB)
- **Format:** JPEG
- **Use:** Compact headers
- **Aspect Ratio:** 2.5:1

**File:** `logo-pallete/ISS white long 500(1).png`
- **Size:** 500 x 169 px (19KB)
- **Format:** PNG with transparency
- **Use:** Small headers, favicons, responsive mobile

### Standard Sizes (PNG with transparency)
**ISS2500.png:** 500 x 225 px (62KB) - Large web display
**ISS2300.png:** 300 x 135 px (35KB) - Medium web display
**ISS300.png:** 300 x 131 px (41KB) - Small web display

### Square Logo Variants
**9.png / 9(1).png:** 200 x 200 px (11-12KB)
- **Use:** Social media, favicon bases, square placements

---

## 🖼️ Background Textures

### Metallic Backgrounds
Premium metallic textures for hero sections or feature backgrounds:

**metal 5.jpg:** 1.2MB - High quality metallic texture
**metal 4 squared.jpg:** 956KB - Squared metallic pattern
**metal 3 squared.jpg:** 464KB - Lighter metallic pattern

**Usage:** Hero sections, premium feature showcases, depth/texture

---

## 🎯 Brand Personality

Based on color palette and logo design:
- **Modern** - Clean lines, contemporary colors
- **Tech-focused** - Blue/cyan palette, digital aesthetic
- **Professional** - Gray tones, structured layout
- **Trustworthy** - Stable color choices, clear hierarchy
- **Innovative** - Bright accents, forward-looking

---

## 🌐 Website Implementation

### Color Usage Recommendations

**Homepage Hero:**
- Background: Dark Slate (#4A545C) or metallic texture
- Text: White or Light Gray
- CTA Buttons: Primary Blue (#1E9FF2) with white text
- Accents: Accent Cyan (#5FDFDF)

**Body Sections (Alternating):**
- Light sections: Light Gray (#D3D3D3) background, Dark Charcoal text
- Dark sections: Dark Slate (#4A545C) background, white text
- Borders/dividers: Dark Charcoal or Primary Blue

**Navigation:**
- Background: Dark Charcoal (#3F4447)
- Links: White default, Accent Cyan on hover
- Active: Primary Blue (#1E9FF2)

**Call-to-Action Buttons:**
- Primary CTA: Primary Blue (#1E9FF2) background, white text
- Secondary CTA: Accent Cyan (#5FDFDF) background, Dark Charcoal text
- Outline CTA: Transparent background, Primary Blue border

---

## 📱 Responsive Logo Usage

**Desktop (>1200px):**
- Use: ISS2500.png or ISS white long.jpg
- Height: 80-120px

**Tablet (768-1200px):**
- Use: ISS2300.png or ISS300.png
- Height: 60-80px

**Mobile (<768px):**
- Use: ISS300.png or square logo (9.png)
- Height: 40-60px

---

## 🔗 File References for Developers

```html
<!-- Header Logo (light background) -->
<img src="logo-pallete/ISS2500.png" alt="iSN.BiZ Inc" height="100">

<!-- Header Logo (dark background) -->
<img src="logo-pallete/ISS white long 500(1).png" alt="iSN.BiZ Inc" height="100">

<!-- Favicon -->
<link rel="icon" href="logo-pallete/9.png" type="image/png">

<!-- Hero Section Background -->
<div style="background: linear-gradient(135deg, #4A545C 0%, #3F4447 100%);">

<!-- Or with texture -->
<div style="background-image: url('logo-pallete/metal 5.jpg'); background-size: cover;">
```

```css
/* CSS Variables */
:root {
  --brand-primary-blue: #1E9FF2;
  --brand-accent-cyan: #5FDFDF;
  --brand-dark-charcoal: #3F4447;
  --brand-dark-slate: #4A545C;
  --brand-light-gray: #D3D3D3;
  --brand-white: #FFFFFF;
}

/* Button Styles */
.btn-primary {
  background-color: var(--brand-primary-blue);
  color: var(--brand-white);
  border: none;
}

.btn-primary:hover {
  background-color: var(--brand-accent-cyan);
  color: var(--brand-dark-charcoal);
}
```

---

## 📁 Asset Organization

**Current Structure:**
```
ISNBIZ_Files/
└── logo-pallete/
    ├── pallete.png          (Color reference)
    ├── ISS.jpg              (Main logo - high res)
    ├── ISS white long.jpg   (Horizontal white)
    ├── ISS2500.png          (Large web)
    ├── ISS2300.png          (Medium web)
    ├── ISS300.png           (Small web)
    ├── 9.png                (Square logo)
    ├── metal*.jpg           (Background textures)
    └── ...
```

**Recommended for Production:**
```
ISNBIZ_Files/
├── assets/
│   ├── images/
│   │   ├── logos/
│   │   │   ├── logo-main.png (ISS2500.png)
│   │   │   ├── logo-white-horizontal.png
│   │   │   ├── logo-square.png
│   │   │   └── favicon.png
│   │   ├── backgrounds/
│   │   │   ├── metallic-texture.jpg
│   │   │   └── hero-gradient.png
│   │   └── screenshots/ (portfolio/projects)
│   └── css/
│       └── brand-colors.css
├── index.html
├── about.html
├── portfolio.html
└── ...
```

---

## 🎨 Design Principles

**Typography Pairing:**
- **Headers:** Modern sans-serif (Inter, Poppins, or Montserrat)
- **Body:** Clean readable sans-serif (Open Sans, Roboto)
- **Code/Technical:** Monospace (Fira Code, JetBrains Mono)

**Spacing:**
- Generous whitespace
- 8px grid system (8, 16, 24, 32, 48, 64, 96, 128)
- Consistent padding/margins

**Visual Style:**
- Clean lines
- Subtle shadows (0 2px 8px rgba(0,0,0,0.1))
- Rounded corners (4-8px for cards, 24px for buttons)
- Smooth transitions (0.3s ease)

---

## 🚀 S3 Upload Plan

When ready for production:

```bash
# Upload brand assets to S3
aws s3 sync /mnt/d/workspace/ISNBIZ_Files/logo-pallete/ \
  s3://isn-biz-assets-2026/brand/ \
  --exclude "*.psd" --exclude "*.ai" \
  --acl public-read

# Set cache headers
aws s3 cp s3://isn-biz-assets-2026/brand/ s3://isn-biz-assets-2026/brand/ \
  --recursive \
  --metadata-directive REPLACE \
  --cache-control "max-age=31536000, public"
```

**CDN URL Pattern:**
```
https://isn-biz-assets-2026.s3.us-east-1.amazonaws.com/brand/ISS2500.png
```

---

**Ready for website implementation with these brand assets!**
