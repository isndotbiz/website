# ISN.BIZ 2026 WordPress Theme - Installation Guide

## Quick Start (5 Minutes)

### Step 1: Upload Theme
```bash
# Via FTP/SFTP or WordPress admin
# Upload wp-theme-isnbiz-2026 folder to /wp-content/themes/
```

### Step 2: Activate
```bash
# WordPress Admin: Appearance > Themes > Activate "ISN.BIZ 2026"
# OR via WP-CLI:
wp theme activate isnbiz-2026
```

### Step 3: Create Pages
Create these 6 pages in WordPress admin:

1. **Home** (Template: Default)
2. **Portfolio** (Template: Portfolio)
3. **About** (Template: Default)
4. **Services** (Template: Default)
5. **Investors** (Template: Default)
6. **Contact** (Template: Default)

### Step 4: Set Homepage
```
Settings > Reading > Your homepage displays > A static page
Homepage: Select "Home"
```

### Step 5: Create Menu
```
Appearance > Menus > Create Menu "Primary Menu"
Add all 6 pages
Assign to: Primary Menu location
Save Menu
```

**Done!** Your site is live.

---

## Detailed Installation (Kusanagi/Production)

### Prerequisites
- WordPress 6.0+
- PHP 8.0+
- Kusanagi server access (10.0.0.89)
- SSH key configured for jdmal@10.0.0.89

### 1. Prepare Theme Package
```bash
cd D:\workspace\ISNBIZ_Files
zip -r wp-theme-isnbiz-2026.zip wp-theme-isnbiz-2026/
```

### 2. Upload to Kusanagi
```bash
# Copy theme to server
scp wp-theme-isnbiz-2026.zip jdmal@10.0.0.89:/tmp/

# SSH into server
ssh jdmal@10.0.0.89

# Extract theme
cd /var/www/html/isn.biz/wp-content/themes/
sudo unzip /tmp/wp-theme-isnbiz-2026.zip

# Fix permissions
sudo chown -R nginx:nginx isnbiz-2026
sudo chmod -R 755 isnbiz-2026
```

### 3. Activate Theme
```bash
# Via WP-CLI
cd /var/www/html/isn.biz
wp theme activate isnbiz-2026
```

### 4. Create Pages (Automated)
```bash
# Create all required pages
wp post create --post_type=page --post_title='Home' --post_status=publish
wp post create --post_type=page --post_title='Portfolio' --post_status=publish --page_template='page-portfolio.php'
wp post create --post_type=page --post_title='About' --post_status=publish
wp post create --post_type=page --post_title='Services' --post_status=publish
wp post create --post_type=page --post_title='Investors' --post_status=publish
wp post create --post_type=page --post_title='Contact' --post_status=publish
```

### 5. Configure Settings
```bash
# Get Home page ID
HOME_ID=$(wp post list --post_type=page --post_title='Home' --field=ID --format=ids)

# Set homepage
wp option update show_on_front page
wp option update page_on_front $HOME_ID

# Set permalinks
wp rewrite structure '/%postname%/'
wp rewrite flush

# Set site details
wp option update blogname 'iSN.BiZ Inc'
wp option update blogdescription 'Building the future of enterprise software with innovative, AI-powered solutions since 2015'
```

### 6. Create Navigation Menu
```bash
# Create menu
wp menu create "Primary Menu"

# Get page IDs
ABOUT_ID=$(wp post list --post_type=page --post_title='About' --field=ID --format=ids)
SERVICES_ID=$(wp post list --post_type=page --post_title='Services' --field=ID --format=ids)
PORTFOLIO_ID=$(wp post list --post_type=page --post_title='Portfolio' --field=ID --format=ids)
INVESTORS_ID=$(wp post list --post_type=page --post_title='Investors' --field=ID --format=ids)
CONTACT_ID=$(wp post list --post_type=page --post_title='Contact' --field=ID --format=ids)

# Add pages to menu
wp menu item add-post primary-menu $ABOUT_ID
wp menu item add-post primary-menu $SERVICES_ID
wp menu item add-post primary-menu $PORTFOLIO_ID
wp menu item add-post primary-menu $INVESTORS_ID
wp menu item add-post primary-menu $CONTACT_ID

# Assign menu to location
wp menu location assign primary-menu primary
```

### 7. Clear Cache
```bash
# Kusanagi cache
kusanagi cache clear

# WordPress cache (if using plugin)
wp cache flush
```

### 8. Verify Installation
```bash
# Check theme is active
wp theme list --status=active

# Check pages exist
wp post list --post_type=page

# Check menu is assigned
wp menu location list

# Visit site
curl -I https://isn.biz
```

---

## Post-Installation Configuration

### SSL Certificate
```bash
# If not already configured
kusanagi ssl isn.biz
```

### Email Configuration
Install WP Mail SMTP plugin for reliable email delivery:
```bash
wp plugin install wp-mail-smtp --activate
# Configure via WordPress admin
```

### Performance Optimization
```bash
# Enable Kusanagi caching
kusanagi cache on isn.biz

# Enable page cache
kusanagi pagecache on isn.biz

# Configure CDN (if using)
kusanagi cdn on isn.biz
```

### Security Headers
Add to nginx config (`/etc/nginx/sites-available/isn.biz.conf`):
```nginx
add_header X-Frame-Options "SAMEORIGIN" always;
add_header X-Content-Type-Options "nosniff" always;
add_header X-XSS-Protection "1; mode=block" always;
add_header Referrer-Policy "strict-origin-when-cross-origin" always;
```

Then reload:
```bash
sudo systemctl reload nginx
```

---

## Customization

### Change Brand Colors
Edit `/wp-content/themes/isnbiz-2026/assets/css/main.css` lines 18-25:
```css
:root {
    --color-blue: #1E9FF2;      /* Your primary color */
    --color-cyan: #5FDFDF;      /* Your secondary color */
    --color-charcoal: #0D1117;  /* Dark backgrounds */
}
```

### Add Custom Logo
```
WordPress Admin > Appearance > Customize > Site Identity > Logo
Upload: 400x100px PNG/WebP
```

### Modify Contact Form Recipient
Edit `/wp-content/themes/isnbiz-2026/functions.php` line ~235:
```php
$to = get_option('admin_email'); // Change to your email
```

---

## Troubleshooting

### Theme Not Showing After Activation
```bash
# Check file permissions
sudo chown -R nginx:nginx /var/www/html/isn.biz/wp-content/themes/isnbiz-2026
sudo chmod -R 755 /var/www/html/isn.biz/wp-content/themes/isnbiz-2026

# Check PHP errors
tail -f /var/log/nginx/isn.biz_error.log
```

### Menu Not Displaying
```bash
# Verify menu exists and is assigned
wp menu list
wp menu location list

# Recreate if needed
wp menu create "Primary Menu"
wp menu location assign primary-menu primary
```

### Images Not Loading (S3)
```bash
# Test S3 URL directly
curl -I https://isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com/premium_v3/logos/navbar_logo.webp

# Check CORS on S3 bucket
# Ensure bucket allows GET from your domain
```

### Contact Form Not Sending
```bash
# Test WordPress email
wp shell
wp_mail('your-email@example.com', 'Test', 'Test message');

# If fails, install SMTP plugin
wp plugin install wp-mail-smtp --activate
```

### Styles Not Loading
```bash
# Clear all caches
kusanagi cache clear
wp cache flush

# Hard refresh browser (Ctrl+Shift+R)

# Check file exists
ls -la /var/www/html/isn.biz/wp-content/themes/isnbiz-2026/assets/css/main.css
```

---

## Maintenance

### Theme Updates
```bash
# Backup before updating
cd /var/www/html/isn.biz/wp-content/themes
sudo tar -czf isnbiz-2026-backup-$(date +%Y%m%d).tar.gz isnbiz-2026/

# Upload new version
scp wp-theme-isnbiz-2026.zip jdmal@10.0.0.89:/tmp/

# Extract
sudo unzip -o /tmp/wp-theme-isnbiz-2026.zip
sudo chown -R nginx:nginx isnbiz-2026
```

### Database Backups
```bash
# Weekly backup via cron
echo "0 2 * * 0 cd /var/www/html/isn.biz && wp db export /backup/isn-biz-\$(date +\%Y\%m\%d).sql" | crontab -
```

---

## Support

**Technical Issues:**
- Check WordPress debug log: `/wp-content/debug.log`
- Check nginx error log: `/var/log/nginx/isn.biz_error.log`
- Check PHP error log: `/var/log/php-fpm/error.log`

**Theme Support:**
- Email: info@isn.biz
- Documentation: See README.md

**Kusanagi Support:**
- Documentation: https://kusanagi.tokyo/document/
- Community: https://kusanagi-community.com/

---

## Complete Installation Script

Save as `install-theme.sh` and run on Kusanagi server:

```bash
#!/bin/bash

# ISN.BIZ 2026 Theme Installation Script
# Usage: ./install-theme.sh

set -e

SITE_PATH="/var/www/html/isn.biz"
THEME_ZIP="/tmp/wp-theme-isnbiz-2026.zip"

echo "=== ISN.BIZ 2026 Theme Installation ==="

# Extract theme
echo "Extracting theme..."
cd $SITE_PATH/wp-content/themes
sudo unzip -o $THEME_ZIP
sudo chown -R nginx:nginx isnbiz-2026
sudo chmod -R 755 isnbiz-2026

# Activate theme
echo "Activating theme..."
cd $SITE_PATH
wp theme activate isnbiz-2026

# Create pages
echo "Creating pages..."
wp post create --post_type=page --post_title='Home' --post_status=publish --porcelain > /tmp/home_id.txt
wp post create --post_type=page --post_title='Portfolio' --post_status=publish --page_template='page-portfolio.php'
wp post create --post_type=page --post_title='About' --post_status=publish
wp post create --post_type=page --post_title='Services' --post_status=publish
wp post create --post_type=page --post_title='Investors' --post_status=publish
wp post create --post_type=page --post_title='Contact' --post_status=publish

# Set homepage
echo "Configuring homepage..."
HOME_ID=$(cat /tmp/home_id.txt)
wp option update show_on_front page
wp option update page_on_front $HOME_ID

# Configure permalinks
echo "Setting permalinks..."
wp rewrite structure '/%postname%/'
wp rewrite flush

# Create menu
echo "Creating navigation menu..."
wp menu create "Primary Menu"
wp menu item add-post primary-menu $(wp post list --post_type=page --post_title='About' --field=ID --format=ids)
wp menu item add-post primary-menu $(wp post list --post_type=page --post_title='Services' --field=ID --format=ids)
wp menu item add-post primary-menu $(wp post list --post_type=page --post_title='Portfolio' --field=ID --format=ids)
wp menu item add-post primary-menu $(wp post list --post_type=page --post_title='Investors' --field=ID --format=ids)
wp menu item add-post primary-menu $(wp post list --post_type=page --post_title='Contact' --field=ID --format=ids)
wp menu location assign primary-menu primary

# Clear cache
echo "Clearing cache..."
kusanagi cache clear

echo "=== Installation Complete! ==="
echo "Visit https://isn.biz to see your new site"
```

---

**Installation Date:** 2026-02-01
**Theme Version:** 3.0.0
**WordPress Version:** 6.0+
**Server:** Kusanagi on TrueNAS (10.0.0.89)
