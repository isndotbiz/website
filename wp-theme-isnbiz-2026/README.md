# ISN.BIZ 2026 WordPress Theme

**Version:** 3.0.0
**Author:** ISN.BIZ Inc
**License:** Proprietary
**Requires WordPress:** 6.0+
**Requires PHP:** 8.0+

## Overview

Production-ready WordPress theme for ISN.BIZ Inc — an enterprise software development company specializing in AI-powered solutions and cloud infrastructure. This theme is fully converted from the static HTML/CSS/JS investor-ready website with complete WCAG 2.1 AA compliance, S3 asset integration, and WordPress best practices.

## Features

- **Neo-Technical Brutalism Design** - Modern, distinctive aesthetic perfect for tech companies
- **WCAG 2.1 AA Compliant** - Fully accessible with proper ARIA labels, skip links, and keyboard navigation
- **S3 Asset Integration** - All images served from S3 bucket for optimal performance
- **Responsive Design** - Mobile-first approach with breakpoints at 480px, 768px, 992px, 1200px
- **Performance Optimized** - Minimal bloat, optimized assets, preconnect hints
- **Investor-Focused** - Dedicated sections for investment opportunities and portfolio showcase
- **Contact Form** - Built-in AJAX contact form with WordPress integration
- **Translation Ready** - All strings properly internationalized with `isnbiz-2026` text domain

## Installation

### 1. Upload Theme

**Option A: Via WordPress Admin**
1. Go to Appearance > Themes > Add New
2. Click "Upload Theme"
3. Choose `wp-theme-isnbiz-2026.zip` file
4. Click "Install Now"
5. Activate the theme

**Option B: Manual Upload**
1. Upload the `wp-theme-isnbiz-2026` directory to `/wp-content/themes/`
2. Activate the theme through WordPress admin

### 2. Configure Menus

1. Go to Appearance > Menus
2. Create a new menu called "Primary Menu"
3. Add these pages:
   - About
   - Services
   - Portfolio
   - Investors
   - Contact
4. Assign to "Primary Menu" location
5. Save

### 3. Create Pages

Create the following pages with the specified templates:

**Homepage (Front Page)**
- Title: Home
- Template: Default Template
- Content: Leave empty (template handles everything)
- Set as: Settings > Reading > Homepage displays > A static page > Homepage: Home

**Portfolio Page**
- Title: Portfolio
- Template: Portfolio
- Slug: `portfolio`

**Other Pages** (use Default Template or create custom templates as needed):
- About (slug: `about`)
- Services (slug: `services`)
- Investors (slug: `investors`)
- Contact (slug: `contact`)

### 4. Configure Settings

**General Settings:**
- Site Title: iSN.BiZ Inc
- Tagline: Building the future of enterprise software with innovative, AI-powered solutions since 2015

**Reading Settings:**
- Your homepage displays: A static page
- Homepage: Home
- Posts page: (leave blank if not using blog)

**Permalink Settings:**
- Select "Post name" for clean URLs

## Theme Structure

```
wp-theme-isnbiz-2026/
├── style.css                    # Theme header + imports
├── functions.php                # Theme setup and functions
├── index.php                    # Homepage template
├── page.php                     # Default page template
├── page-portfolio.php           # Portfolio template
├── header.php                   # Site header
├── footer.php                   # Site footer
├── assets/
│   ├── css/
│   │   ├── main.css             # Main stylesheet (from styles.css - 37KB)
│   │   └── slider.css           # Slider styles (11KB)
│   └── js/
│       ├── main.js              # Main JavaScript (687B)
│       └── slider.js            # Slider initialization (9KB)
├── template-parts/
│   ├── solutions-grid.php       # Solutions section
│   ├── portfolio-preview.php    # Portfolio preview cards
│   ├── investor-section.php     # Investor section
│   └── contact-form.php         # Contact form
├── screenshot.txt               # Placeholder - create screenshot.png (1200x900px)
├── INSTALLATION_GUIDE.md        # Detailed installation guide
└── README.md                    # This file
```

## S3 Assets

All images are served from S3 bucket:
```
https://isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com/premium_v3/
```

**Helper Function:**
```php
// Use this in templates to get S3 URLs
isnbiz_s3_url('logos/navbar_logo.webp')
// Returns: https://isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com/premium_v3/logos/navbar_logo.webp
```

**Asset Categories:**
- `logos/` - Logo variants (navbar, hero, footer, favicon, apple-touch-icon)
- `portfolio/` - Portfolio project images
- `services/` - Service section images
- `founders/` - Team member photos
- `hero/` - Hero background images
- `sections/` - Section background images
- `og/` - Open Graph social sharing images

## Customization

### Brand Colors

The theme uses ISN.BIZ brand colors defined in CSS variables:

```css
--color-blue: #1E9FF2      /* Primary brand blue */
--color-cyan: #5FDFDF      /* Secondary brand cyan */
--color-charcoal: #0D1117  /* Dark backgrounds */
--color-concrete: #1C1F26  /* Concrete gray */
--color-steel: #2A2F3A     /* Steel surface */
--color-white: #F0F4F8     /* Off-white */
--color-accent: #FF2D55    /* Electric pink accent */
```

To customize, edit `/assets/css/main.css` starting at line 18.

### Typography

Three font families are used:
- **Display:** Archivo Black (headings, bold statements)
- **Monospace:** JetBrains Mono (technical labels, code)
- **Body:** IBM Plex Sans (paragraph text, UI elements)

Fonts are loaded from Google Fonts in `functions.php`.

### Custom Logo

1. Go to Appearance > Customize > Site Identity
2. Upload your logo (recommended: 400x100px)
3. The theme will use your custom logo instead of the default S3 logo

### Contact Form

The contact form uses AJAX and WordPress's built-in `wp_mail()` function.

**To customize recipient:**
- Email sent to: `get_option('admin_email')` (WordPress admin email)
- Change in: `functions.php` line ~235

**To integrate with third-party services:**
- Mailchimp, SendGrid, etc. can be integrated via plugins
- Or modify the AJAX handler in `functions.php`

### Adding Portfolio Projects

Edit `template-parts/portfolio-preview.php` to add/modify the preview cards on the homepage.

For the full portfolio page (`page-portfolio.php`), add additional project sections following the existing pattern.

## Page Templates

### Default Page Template (`page.php`)
- Generic page layout
- Hero section with page title
- Content area for WordPress editor content

### Portfolio Template (`page-portfolio.php`)
- Dedicated portfolio layout
- 9 detailed project sections
- Technology stack displays
- Metrics and results cards
- CTA sections

### Custom Templates (To Create)
Follow this pattern to create custom templates for About, Services, Investors, Contact:

```php
<?php
/**
 * Template Name: Your Template Name
 *
 * @package ISN_BIZ_2026
 */

get_header();
?>

<!-- Your custom content here -->

<?php
get_footer();
```

## WordPress Best Practices

This theme follows WordPress coding standards:

- **Security:** All output escaped with `esc_html()`, `esc_attr()`, `esc_url()`
- **Internationalization:** All strings wrapped in `__()` or `esc_html_e()`
- **Accessibility:** WCAG 2.1 AA compliant, proper ARIA labels
- **Performance:** Minimal queries, optimized assets, conditional loading
- **Hooks:** Standard WordPress action/filter hooks
- **Navigation:** Custom walker for accessibility-enhanced menus

## Deployment to Kusanagi

This theme is designed for deployment on Kusanagi (like HROC.org at 10.0.0.89).

### Pre-Deployment Checklist

- [ ] All pages created with correct templates
- [ ] Primary menu configured and assigned
- [ ] Site title and tagline set
- [ ] Permalink structure set to "Post name"
- [ ] Admin email configured (for contact form)
- [ ] SSL certificate configured
- [ ] S3 assets accessible (test URLs)

### Deployment Steps

1. **Backup Current Site** (if applicable)
   ```bash
   ssh jdmal@10.0.0.89
   cd /var/www/html/isn.biz
   wp db export backup-$(date +%Y%m%d).sql
   ```

2. **Upload Theme**
   ```bash
   scp -r wp-theme-isnbiz-2026 jdmal@10.0.0.89:/var/www/html/isn.biz/wp-content/themes/
   ```

3. **Activate via WP-CLI**
   ```bash
   ssh jdmal@10.0.0.89
   cd /var/www/html/isn.biz
   wp theme activate isnbiz-2026
   ```

4. **Create Pages**
   ```bash
   wp post create --post_type=page --post_title='Home' --post_status=publish
   wp post create --post_type=page --post_title='Portfolio' --post_status=publish --page_template='page-portfolio.php'
   wp post create --post_type=page --post_title='About' --post_status=publish
   wp post create --post_type=page --post_title='Services' --post_status=publish
   wp post create --post_type=page --post_title='Investors' --post_status=publish
   wp post create --post_type=page --post_title='Contact' --post_status=publish
   ```

5. **Set Homepage**
   ```bash
   # Get the Home page ID
   HOME_ID=$(wp post list --post_type=page --post_title='Home' --field=ID)

   # Set as homepage
   wp option update show_on_front page
   wp option update page_on_front $HOME_ID
   ```

6. **Configure Permalinks**
   ```bash
   wp rewrite structure '/%postname%/'
   wp rewrite flush
   ```

7. **Clear Cache**
   ```bash
   # If using Kusanagi caching
   kusanagi cache clear
   ```

## Troubleshooting

### S3 Images Not Loading
- Check S3 bucket permissions (public read access)
- Verify bucket URL in `functions.php` (line ~109)
- Check CORS configuration on S3 bucket

### Contact Form Not Sending
- Verify WordPress can send email: `wp shell` then `wp_mail('test@example.com', 'Test', 'Test')`
- Check spam folder
- Consider SMTP plugin (WP Mail SMTP)

### Menu Not Showing
- Ensure menu is assigned to "Primary Menu" location
- Check that pages exist and are published
- Verify menu items have correct URLs

### Styles Not Loading
- Hard refresh browser (Ctrl+Shift+R)
- Check file permissions on server
- Verify theme files uploaded correctly
- Clear WordPress cache/CDN cache

## Support

For theme support, customization, or deployment assistance:

- **Email:** info@isn.biz
- **Website:** https://isn.biz
- **Documentation:** See `.serena/` directory in ISNBIZ_Files workspace

## Credits

**Design & Development:** ISN.BIZ Inc
**Original Static Site:** ISNBIZ_Files (index.html, portfolio.html, etc.)
**WordPress Conversion:** 2026-02-01
**Fonts:** Google Fonts (JetBrains Mono, Archivo Black, IBM Plex Sans)
**Assets:** AWS S3 (isnbiz-assets-1769962280)

## License

Proprietary - © 2026 ISN.BIZ Inc. All rights reserved.

This theme is proprietary software developed for ISN.BIZ Inc. Unauthorized copying, modification, distribution, or use is prohibited.

---

**Version History:**

- **3.0.0** (2026-02-01) - Initial WordPress theme conversion from static HTML/CSS/JS site
  - Complete homepage with all sections
  - Portfolio page template with 9 projects
  - WCAG 2.1 AA compliant
  - S3 asset integration
  - Contact form with AJAX
  - Responsive design
  - WordPress best practices

---

**Maintained by:** ISN.BIZ Inc Development Team
**Last Updated:** February 1, 2026
