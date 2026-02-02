#!/bin/bash
#
# Complete ISN.BIZ Deployment Workflow
# 1. Optimize and upload all images to S3
# 2. Update HTML files to use S3 URLs
# 3. Deploy HTML/CSS/JS to TrueNAS Kusanagi
# 4. Configure SSL and DNS
#

set -e

echo "════════════════════════════════════════════════════════════════════"
echo "  ISN.BIZ COMPLETE DEPLOYMENT WORKFLOW"
echo "════════════════════════════════════════════════════════════════════"
echo ""
echo "This script will:"
echo "  1. Optimize all images and upload to S3"
echo "  2. Update HTML files to reference S3 URLs"
echo "  3. Deploy HTML/CSS/JS to TrueNAS (NO images on TrueNAS)"
echo "  4. Guide you through SSL and DNS setup"
echo ""
read -p "Continue? (y/N) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Deployment cancelled."
    exit 0
fi

# Step 1: Upload images to S3
echo ""
echo "════════════════════════════════════════════════════════════════════"
echo "  STEP 1: Upload Images to S3"
echo "════════════════════════════════════════════════════════════════════"
echo ""

if [ ! -f "upload_images_to_s3.py" ]; then
    echo "❌ Error: upload_images_to_s3.py not found"
    exit 1
fi

echo "Installing required Python packages..."
pip install boto3 pillow --quiet

echo ""
echo "Uploading images to S3..."
python3 upload_images_to_s3.py || {
    echo "❌ S3 upload failed"
    exit 1
}

echo ""
echo "✅ Step 1 complete: All images uploaded to S3"

# Step 2: Update HTML files
echo ""
echo "════════════════════════════════════════════════════════════════════"
echo "  STEP 2: Update HTML Files to Use S3 URLs"
echo "════════════════════════════════════════════════════════════════════"
echo ""

if [ ! -f "s3_url_mapping.json" ]; then
    echo "❌ Error: s3_url_mapping.json not found (should be created by Step 1)"
    exit 1
fi

python3 update_html_to_s3_urls.py || {
    echo "❌ HTML update failed"
    exit 1
}

echo ""
echo "✅ Step 2 complete: HTML files updated with S3 URLs"

# Step 3: Deploy to TrueNAS
echo ""
echo "════════════════════════════════════════════════════════════════════"
echo "  STEP 3: Deploy to TrueNAS Kusanagi"
echo "════════════════════════════════════════════════════════════════════"
echo ""
echo "Now deploying HTML/CSS/JS files to TrueNAS..."
echo "(Images are served from S3, not deployed to TrueNAS)"
echo ""

# Create deployment package (NO images)
DEPLOY_TEMP="/tmp/isn-biz-deploy"
rm -rf "$DEPLOY_TEMP"
mkdir -p "$DEPLOY_TEMP"

echo "Creating deployment package..."
cp *.html "$DEPLOY_TEMP/" 2>/dev/null || true
cp *.css "$DEPLOY_TEMP/" 2>/dev/null || true
cp *.js "$DEPLOY_TEMP/" 2>/dev/null || true

# Check package size
PACKAGE_SIZE=$(du -sh "$DEPLOY_TEMP" | cut -f1)
FILE_COUNT=$(find "$DEPLOY_TEMP" -type f | wc -l)

echo "  Package size: $PACKAGE_SIZE"
echo "  File count: $FILE_COUNT files"
echo "  (No image files - all served from S3)"
echo ""

# Compress for transfer
cd "$DEPLOY_TEMP"
tar czf /tmp/isn-biz-site-s3.tar.gz *
cd - > /dev/null

echo "  Compressed package: $(du -h /tmp/isn-biz-site-s3.tar.gz | cut -f1)"
echo ""

# Now run the TrueNAS deployment
echo "Running TrueNAS deployment script..."
if [ ! -f "deploy_to_truenas.sh" ]; then
    echo "❌ Error: deploy_to_truenas.sh not found"
    exit 1
fi

bash deploy_to_truenas.sh || {
    echo "❌ TrueNAS deployment failed"
    exit 1
}

echo ""
echo "✅ Step 3 complete: Site deployed to TrueNAS"

# Step 4: SSL and DNS guidance
echo ""
echo "════════════════════════════════════════════════════════════════════"
echo "  STEP 4: SSL Certificate and DNS Configuration"
echo "════════════════════════════════════════════════════════════════════"
echo ""
echo "⚠ IMPORTANT: Complete these steps manually"
echo ""
echo "A. SSL Certificate (Choose ONE method):"
echo ""
echo "   Method 1 - Certbot (Recommended):"
echo "   $ ssh jdmal@10.0.0.89"
echo "   $ sudo certbot --nginx -d isn.biz -d www.isn.biz"
echo ""
echo "   Method 2 - ACME.sh:"
echo "   $ ssh jdmal@10.0.0.89"
echo "   $ sudo acme.sh --issue -d isn.biz -d www.isn.biz --nginx"
echo ""
echo "   Method 3 - Kusanagi SSL:"
echo "   $ ssh jdmal@10.0.0.89"
echo "   $ sudo kusanagi ssl isn.biz"
echo ""
echo "B. Cloudflare DNS Settings:"
echo ""
echo "   1. Log into Cloudflare dashboard"
echo "   2. Select isn.biz domain"
echo "   3. Verify DNS records:"
echo "      - A record: isn.biz → [Your Public IP or 10.0.0.89 if behind VPN]"
echo "      - A record: www.isn.biz → [Same IP]"
echo "   4. SSL/TLS Settings:"
echo "      - Encryption mode: Full (strict)"
echo "      - Always Use HTTPS: ON"
echo "      - Automatic HTTPS Rewrites: ON"
echo "   5. IMPORTANT: Verify subdomains are NOT affected"
echo "      - Check all existing subdomain records"
echo "      - Test each service after deployment"
echo ""
echo "C. Verify Deployment:"
echo ""
echo "   Test commands:"
echo "   $ curl -I https://isn.biz"
echo "   $ curl -I https://www.isn.biz"
echo ""
echo "   Browser tests:"
echo "   - https://isn.biz"
echo "   - https://www.isn.biz"
echo "   - Check all founder pages"
echo "   - Check all project pages"
echo "   - Verify images load from S3"
echo ""
echo "D. Subdomain Health Check:"
echo ""
echo "   Test each existing subdomain to ensure they still work:"
echo "   - Any Portainer/monitoring subdomains"
echo "   - Any API subdomains"
echo "   - Any other service subdomains"
echo ""

# Final summary
echo ""
echo "════════════════════════════════════════════════════════════════════"
echo "  DEPLOYMENT SUMMARY"
echo "════════════════════════════════════════════════════════════════════"
echo ""
echo "✅ Images optimized and uploaded to S3"
echo "✅ HTML files updated to use S3 URLs"
echo "✅ Site deployed to TrueNAS Kusanagi"
echo ""
echo "📋 What was deployed to TrueNAS:"
echo "   - HTML files only ($FILE_COUNT files, $PACKAGE_SIZE)"
echo "   - CSS files"
echo "   - JavaScript files"
echo "   - NO image files (served from S3)"
echo ""
echo "🌐 Images served from:"
echo "   https://isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com/"
echo ""
echo "⏭ Next steps:"
echo "   1. Complete SSL certificate setup (see above)"
echo "   2. Verify Cloudflare DNS settings"
echo "   3. Test the site in browser"
echo "   4. Verify all subdomains still work"
echo ""
echo "📝 Backups created:"
echo "   - HTML backups: *.html.backup"
echo "   - TrueNAS backup: /mnt/tank/backups/websites/isn.biz_[timestamp]"
echo ""
echo "════════════════════════════════════════════════════════════════════"

# Cleanup
rm -rf "$DEPLOY_TEMP"
rm -f /tmp/isn-biz-site-s3.tar.gz

echo ""
echo "🎉 Deployment complete!"
echo ""

exit 0
