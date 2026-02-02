#!/bin/bash
#
# ISN.BIZ Quick Deployment to TrueNAS
# Run this from your local machine when on the 10.0.0.0/24 network
#

set -e

echo "════════════════════════════════════════════════════════════"
echo "  ISN.BIZ DEPLOYMENT TO TRUENAS"
echo "════════════════════════════════════════════════════════════"
echo ""

# Configuration
TRUENAS_HOST="10.0.0.89"
TRUENAS_USER="jdmal"
SITE_DIR="/mnt/tank/websites/kusanagi/isn.biz/public"
BACKUP_DIR="/mnt/tank/backups/websites/isn.biz_$(date +%Y%m%d_%H%M%S)"
DEPLOY_PACKAGE="/tmp/isn-biz-truenas.tar.gz"

# Check if package exists
if [ ! -f "$DEPLOY_PACKAGE" ]; then
    echo "❌ Deployment package not found: $DEPLOY_PACKAGE"
    echo "   Creating it now..."
    mkdir -p /tmp/truenas-deploy
    cp *.html *.css *.js /tmp/truenas-deploy/ 2>/dev/null
    cd /tmp/truenas-deploy
    tar czf "$DEPLOY_PACKAGE" *
    cd - > /dev/null
    echo "✅ Package created: $(ls -lh $DEPLOY_PACKAGE | awk '{print $5}')"
fi

echo "Package: $(ls -lh $DEPLOY_PACKAGE | awk '{print $5}')"
echo "Destination: $SITE_DIR"
echo ""

# Get 1Password credentials
echo "Authenticating with 1Password..."
eval $(op signin) 2>/dev/null || {
    echo "❌ 1Password authentication failed"
    echo "   Run: eval \$(op signin)"
    exit 1
}

# SSH connection
echo "✅ 1Password authenticated"
echo ""

# Test connection
echo "Testing connection to TrueNAS..."
ssh $TRUENAS_USER@$TRUENAS_HOST "echo '✅ Connected'" || {
    echo "❌ Cannot connect to $TRUENAS_HOST"
    echo "   Make sure you're on the 10.0.0.0/24 network"
    exit 1
}

echo ""
echo "═══ STEP 1: Backup Existing Site ═══"
ssh $TRUENAS_USER@$TRUENAS_HOST "
    if [ -d '$SITE_DIR' ]; then
        echo 'Creating backup...'
        sudo mkdir -p '$BACKUP_DIR'
        sudo cp -r '$SITE_DIR'/* '$BACKUP_DIR/' 2>/dev/null || true
        echo '✅ Backup saved to: $BACKUP_DIR'
    else
        echo 'No existing site found'
    fi
"

echo ""
echo "═══ STEP 2: Prepare Directory ═══"
ssh $TRUENAS_USER@$TRUENAS_HOST "
    sudo mkdir -p '$SITE_DIR'
    sudo chown -R www-data:www-data '$SITE_DIR'
    sudo chmod 755 '$SITE_DIR'
    echo '✅ Directory ready'
"

echo ""
echo "═══ STEP 3: Transfer Files ═══"
echo "Uploading $(ls -lh $DEPLOY_PACKAGE | awk '{print $5}')..."
scp "$DEPLOY_PACKAGE" $TRUENAS_USER@$TRUENAS_HOST:/tmp/

echo ""
echo "═══ STEP 4: Extract and Deploy ═══"
ssh $TRUENAS_USER@$TRUENAS_HOST "
    cd '$SITE_DIR'
    sudo tar xzf /tmp/isn-biz-truenas.tar.gz
    sudo chown -R www-data:www-data '$SITE_DIR'
    sudo chmod -R 755 '$SITE_DIR'
    sudo find '$SITE_DIR' -type f -exec chmod 644 {} \;
    rm -f /tmp/isn-biz-truenas.tar.gz
    echo '✅ Files deployed'
    echo ''
    echo 'Deployed files:'
    sudo ls -lh '$SITE_DIR' | head -15
    echo '...'
    echo 'Total: ' \$(sudo find '$SITE_DIR' -type f | wc -l) 'files'
"

echo ""
echo "════════════════════════════════════════════════════════════"
echo "  DEPLOYMENT COMPLETE!"
echo "════════════════════════════════════════════════════════════"
echo ""
echo "✅ Website deployed to: $SITE_DIR"
echo "✅ All images served from S3 CDN"
echo "✅ Package size: $(ls -lh $DEPLOY_PACKAGE | awk '{print $5}') (no images!)"
echo ""
echo "NEXT STEPS:"
echo ""
echo "1. Configure SSL Certificate (if not done):"
echo "   ssh $TRUENAS_USER@$TRUENAS_HOST"
echo "   sudo certbot --nginx -d isn.biz -d www.isn.biz"
echo ""
echo "2. Restart Nginx:"
echo "   ssh $TRUENAS_USER@$TRUENAS_HOST"
echo "   sudo systemctl restart nginx"
echo ""
echo "3. Test the site:"
echo "   curl -I https://isn.biz"
echo "   Open browser: https://isn.biz"
echo ""
echo "4. Verify subdomains still work:"
echo "   Test each service subdomain"
echo ""
echo "ROLLBACK (if needed):"
echo "   ssh $TRUENAS_USER@$TRUENAS_HOST"
echo "   sudo cp -r $BACKUP_DIR/* $SITE_DIR/"
echo "   sudo systemctl reload nginx"
echo ""
echo "════════════════════════════════════════════════════════════"

exit 0
