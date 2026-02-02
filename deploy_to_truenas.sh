#!/bin/bash
#
# ISN.BIZ Static Site Deployment to TrueNAS Kusanagi
# Deploys the investor-ready website to TrueNAS and configures SSL
#

set -e  # Exit on error

echo "════════════════════════════════════════════════════════════"
echo "  ISN.BIZ DEPLOYMENT TO TRUENAS KUSANAGI"
echo "════════════════════════════════════════════════════════════"
echo ""

# Configuration
TRUENAS_HOST="10.0.0.89"
TRUENAS_USER="jdmal"
SITE_DIR="/mnt/tank/websites/kusanagi/isn.biz"
BACKUP_DIR="/mnt/tank/backups/websites/isn.biz_$(date +%Y%m%d_%H%M%S)"
LOCAL_DIR="$(pwd)"
DOMAIN="isn.biz"

echo "Configuration:"
echo "  TrueNAS Host: $TRUENAS_HOST"
echo "  Site Directory: $SITE_DIR"
echo "  Domain: $DOMAIN"
echo ""

# Step 1: Get SSH credentials from 1Password
echo "Step 1: Authenticating with 1Password..."
eval $(op signin) 2>/dev/null || { echo "❌ 1Password signin failed"; exit 1; }
echo "✓ 1Password authenticated"

# Try to get SSH key, fallback to password
SSH_KEY_PATH="/tmp/truenas_deploy_key"
if op read "op://TrueNAS Infrastructure/Xeon Gold SSH/private key" > "$SSH_KEY_PATH" 2>/dev/null; then
    chmod 600 "$SSH_KEY_PATH"
    SSH_CMD="ssh -i $SSH_KEY_PATH"
    SCP_CMD="scp -i $SSH_KEY_PATH"
    echo "✓ Using SSH key authentication"
else
    SSH_CMD="ssh"
    SCP_CMD="scp"
    echo "✓ Using password authentication (will prompt)"
fi

# Step 2: Test connection
echo ""
echo "Step 2: Testing TrueNAS connection..."
$SSH_CMD $TRUENAS_USER@$TRUENAS_HOST "echo '✓ Connected to TrueNAS'" || {
    echo "❌ Cannot connect to TrueNAS at $TRUENAS_HOST"
    echo "   Make sure you're on the 10.0.0.0/24 network"
    exit 1
}

# Step 3: Check Kusanagi directory structure
echo ""
echo "Step 3: Checking Kusanagi directory structure..."
$SSH_CMD $TRUENAS_USER@$TRUENAS_HOST "ls -la /mnt/tank/websites/kusanagi/ 2>/dev/null || sudo ls -la /mnt/tank/websites/kusanagi/ 2>/dev/null" || {
    echo "❌ Cannot access Kusanagi directory"
    echo "   May need sudo access or directory doesn't exist"
    exit 1
}

# Step 4: Backup existing site (if any)
echo ""
echo "Step 4: Backing up existing site (if present)..."
$SSH_CMD $TRUENAS_USER@$TRUENAS_HOST "
    if [ -d '$SITE_DIR' ]; then
        echo 'Creating backup at $BACKUP_DIR'
        sudo mkdir -p '$BACKUP_DIR'
        sudo cp -r '$SITE_DIR' '$BACKUP_DIR/'
        echo '✓ Backup created'
    else
        echo 'No existing site to backup'
    fi
"

# Step 5: Create site directory
echo ""
echo "Step 5: Preparing site directory..."
$SSH_CMD $TRUENAS_USER@$TRUENAS_HOST "
    sudo mkdir -p '$SITE_DIR'
    sudo chown -R www-data:www-data '$SITE_DIR'
    sudo chmod 755 '$SITE_DIR'
    echo '✓ Site directory ready'
"

# Step 6: Transfer files
echo ""
echo "Step 6: Transferring website files (173MB)..."
echo "This may take a few minutes..."

# Create tarball for faster transfer
cd "$LOCAL_DIR"
tar czf /tmp/isn-biz-site.tar.gz \
    --exclude='*.md' \
    --exclude='*.sh' \
    --exclude='*.py' \
    --exclude='.git*' \
    --exclude='node_modules' \
    --exclude='venv*' \
    --exclude='scripts' \
    --exclude='docs' \
    --exclude='temp' \
    --exclude='logs' \
    *.html *.css *.js assets/ 2>/dev/null

echo "  Compressed site to $(du -h /tmp/isn-biz-site.tar.gz | cut -f1)"

# Transfer tarball
$SCP_CMD /tmp/isn-biz-site.tar.gz $TRUENAS_USER@$TRUENAS_HOST:/tmp/

# Extract on server
$SSH_CMD $TRUENAS_USER@$TRUENAS_HOST "
    cd /tmp
    sudo tar xzf isn-biz-site.tar.gz -C '$SITE_DIR'
    sudo chown -R www-data:www-data '$SITE_DIR'
    sudo chmod -R 755 '$SITE_DIR'
    sudo find '$SITE_DIR' -type f -exec chmod 644 {} \;
    rm -f /tmp/isn-biz-site.tar.gz
    echo '✓ Files extracted and permissions set'
"

rm -f /tmp/isn-biz-site.tar.gz
echo "✓ Website files deployed"

# Step 7: Configure Nginx/Web Server
echo ""
echo "Step 7: Checking web server configuration..."
$SSH_CMD $TRUENAS_USER@$TRUENAS_HOST "
    # Check if Kusanagi nginx config exists
    if [ -f /etc/nginx/sites-available/isn.biz ]; then
        echo '✓ Nginx configuration exists'
    else
        echo '⚠ Nginx configuration may need to be created'
        echo '  Please configure manually or use Kusanagi tools'
    fi
"

# Step 8: SSL Certificate Setup
echo ""
echo "Step 8: SSL Certificate configuration..."
echo "Checking for existing certificates..."

$SSH_CMD $TRUENAS_USER@$TRUENAS_HOST "
    # Check for existing SSL cert
    if [ -f /etc/letsencrypt/live/$DOMAIN/fullchain.pem ]; then
        echo '✓ SSL certificate already exists for $DOMAIN'
        echo '  Certificate path: /etc/letsencrypt/live/$DOMAIN/'
    else
        echo '⚠ No SSL certificate found'
        echo ''
        echo 'To set up SSL, run ONE of the following:'
        echo ''
        echo '  Option 1: Using certbot (Let'\''s Encrypt)'
        echo '  sudo certbot --nginx -d $DOMAIN -d www.$DOMAIN'
        echo ''
        echo '  Option 2: Using acme.sh'
        echo '  sudo acme.sh --issue -d $DOMAIN -d www.$DOMAIN --nginx'
        echo ''
        echo '  Option 3: Using Kusanagi tools'
        echo '  sudo kusanagi ssl $DOMAIN'
    fi
"

# Step 9: DNS/Cloudflare Check
echo ""
echo "Step 9: Cloudflare DNS verification..."
echo "⚠ IMPORTANT: Verify Cloudflare DNS settings manually:"
echo ""
echo "  1. Log into Cloudflare dashboard"
echo "  2. Verify A record points to TrueNAS IP (likely 10.0.0.89 or public IP)"
echo "  3. Ensure proxy status (orange cloud) is set correctly"
echo "  4. Check SSL/TLS mode is set to 'Full' or 'Full (strict)'"
echo "  5. Verify existing subdomains are NOT affected"
echo ""

# Step 10: Verify deployment
echo ""
echo "Step 10: Verifying deployment..."
$SSH_CMD $TRUENAS_USER@$TRUENAS_HOST "
    echo 'Files in $SITE_DIR:'
    sudo ls -lh '$SITE_DIR' | head -20
    echo ''
    echo 'File count:'
    sudo find '$SITE_DIR' -type f | wc -l
    echo ''
    echo 'Directory size:'
    sudo du -sh '$SITE_DIR'
"

# Step 11: Final instructions
echo ""
echo "════════════════════════════════════════════════════════════"
echo "  DEPLOYMENT COMPLETE!"
echo "════════════════════════════════════════════════════════════"
echo ""
echo "✓ Website files deployed to: $SITE_DIR"
echo "✓ Backup created at: $BACKUP_DIR"
echo ""
echo "NEXT STEPS:"
echo ""
echo "1. Configure/restart web server:"
echo "   sudo systemctl restart nginx"
echo ""
echo "2. Set up SSL certificate (if not already done):"
echo "   sudo certbot --nginx -d $DOMAIN -d www.$DOMAIN"
echo ""
echo "3. Test the site:"
echo "   curl -I http://$DOMAIN"
echo "   curl -I https://$DOMAIN"
echo ""
echo "4. Verify in browser:"
echo "   https://$DOMAIN"
echo ""
echo "5. Check subdomains are still working:"
echo "   - Test each service subdomain"
echo "   - Verify nginx proxy configurations"
echo ""
echo "ROLLBACK (if needed):"
echo "   sudo cp -r $BACKUP_DIR/isn.biz/* $SITE_DIR/"
echo ""
echo "════════════════════════════════════════════════════════════"

# Cleanup
rm -f "$SSH_KEY_PATH" 2>/dev/null

exit 0
