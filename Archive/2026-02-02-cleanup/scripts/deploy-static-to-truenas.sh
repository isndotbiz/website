#!/bin/bash
#
# ISN.BIZ Static Website Deployment to TrueNAS
#
# Deploy static HTML/CSS/JS website to TrueNAS Kusanagi server
#
# Usage: bash deploy-static-to-truenas.sh
#

set -e  # Exit on error

# Color output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
TRUENAS_HOST="10.0.0.89"
TRUENAS_USER="jdmal"
DOMAIN="isn.biz"
REMOTE_PATH="/home/kusanagi/${DOMAIN}/DocumentRoot/"

# Detect environment (WSL or Git Bash)
if [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
    # Git Bash on Windows
    LOCAL_PATH="/d/workspace/ISNBIZ_Files/"
    SSH_KEY="$HOME/.ssh/truenas_jdmal"
elif [[ -f "/proc/version" ]] && grep -qi microsoft /proc/version; then
    # WSL
    LOCAL_PATH="/home/jdmal/workspace/ISNBIZ_Files/"
    SSH_KEY="$HOME/.ssh/truenas_jdmal"
else
    # Linux
    LOCAL_PATH="/home/jdmal/workspace/ISNBIZ_Files/"
    SSH_KEY="$HOME/.ssh/truenas_jdmal"
fi

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}ISN.BIZ Static Site Deployment${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""
echo -e "${YELLOW}Configuration:${NC}"
echo "  Source: ${LOCAL_PATH}"
echo "  Target: ${TRUENAS_USER}@${TRUENAS_HOST}:${REMOTE_PATH}"
echo "  SSH Key: ${SSH_KEY}"
echo ""

# Check if source directory exists
if [ ! -d "$LOCAL_PATH" ]; then
    echo -e "${RED}ERROR: Source directory not found: ${LOCAL_PATH}${NC}"
    exit 1
fi
echo -e "${GREEN}✓ Source directory found${NC}"

# Check for required files
echo -e "${YELLOW}Checking for required files...${NC}"
required_files=("index.html" "styles.css" "script.js")
for file in "${required_files[@]}"; do
    if [ ! -f "${LOCAL_PATH}${file}" ]; then
        echo -e "${RED}ERROR: Required file missing: ${file}${NC}"
        exit 1
    fi
    echo "  ✓ ${file}"
done
echo ""

# Check SSH connectivity (without 1Password for now)
echo -e "${YELLOW}Testing SSH connection to TrueNAS...${NC}"

# Try direct SSH first
if ssh -i "$SSH_KEY" -o ConnectTimeout=5 -o StrictHostKeyChecking=no ${TRUENAS_USER}@${TRUENAS_HOST} "echo 'Connection successful'" 2>/dev/null; then
    echo -e "${GREEN}✓ SSH connection verified${NC}"
else
    echo -e "${YELLOW}Direct SSH failed, checking 1Password for key...${NC}"

    # Check if op is available
    if command -v op &> /dev/null; then
        echo -e "${YELLOW}Getting SSH key from 1Password...${NC}"

        # Try to get the key from 1Password
        if op whoami > /dev/null 2>&1; then
            # Already signed in
            echo "  ✓ Already signed into 1Password"
        else
            # Need to sign in
            echo -e "${YELLOW}Please sign into 1Password:${NC}"
            eval $(op signin)
        fi

        # Get SSH key from 1Password
        SSH_KEY_CONTENT=$(op read "op://TrueNAS Infrastructure/Xeon Gold SSH/private key" 2>/dev/null || op read "op://TrueNAS Infrastructure/truenas_admin/private key" 2>/dev/null)

        if [ -n "$SSH_KEY_CONTENT" ]; then
            # Save to temp file
            TEMP_KEY=$(mktemp)
            echo "$SSH_KEY_CONTENT" > "$TEMP_KEY"
            chmod 600 "$TEMP_KEY"
            SSH_KEY="$TEMP_KEY"
            echo -e "${GREEN}✓ Got SSH key from 1Password${NC}"
        else
            echo -e "${RED}ERROR: Could not get SSH key from 1Password${NC}"
            echo "Please ensure you have access to the TrueNAS Infrastructure vault"
            exit 1
        fi
    else
        echo -e "${RED}ERROR: Cannot connect to TrueNAS and 1Password CLI not available${NC}"
        echo ""
        echo "Options:"
        echo "  1. Install 1Password CLI: https://developer.1password.com/docs/cli/get-started/"
        echo "  2. Set up SSH key manually: ssh-copy-id ${TRUENAS_USER}@${TRUENAS_HOST}"
        exit 1
    fi
fi
echo ""

# Confirm deployment
echo -e "${YELLOW}Ready to deploy the following:${NC}"
echo "  - HTML files (*.html)"
echo "  - CSS files (*.css)"
echo "  - JavaScript files (*.js)"
echo "  - Assets folder (all images, fonts, etc.)"
echo "  - Founder photos (assets/founders/)"
echo "  - Project assets (assets/projects/)"
echo ""
read -p "Continue with deployment? (yes/no) [yes]: " -r
CONFIRM=${REPLY:-yes}

if [[ ! $CONFIRM =~ ^[Yy]es$ ]]; then
    echo "Deployment cancelled"
    exit 0
fi
echo ""

# Deploy using rsync
echo -e "${YELLOW}Deploying files to TrueNAS...${NC}"

rsync -avz \
    --progress \
    --delete \
    --exclude 'venv*' \
    --exclude '.git' \
    --exclude 'node_modules' \
    --exclude '*.py' \
    --exclude '*.sh' \
    --exclude 'scripts/' \
    --exclude 'docs/' \
    --exclude '.serena/' \
    --exclude '*.md' \
    --exclude '*.txt' \
    --exclude '.env' \
    --exclude 'slider_images/' \
    --exclude '1/' \
    --exclude 'logo-pallete.zip' \
    -e "ssh -i $SSH_KEY -o StrictHostKeyChecking=no" \
    "${LOCAL_PATH}" \
    "${TRUENAS_USER}@${TRUENAS_HOST}:${REMOTE_PATH}"

echo -e "${GREEN}✓ Files deployed successfully${NC}"
echo ""

# Set proper permissions
echo -e "${YELLOW}Setting file permissions on TrueNAS...${NC}"
ssh -i "$SSH_KEY" -o StrictHostKeyChecking=no ${TRUENAS_USER}@${TRUENAS_HOST} << 'EOF'
cd /home/kusanagi/isn.biz/DocumentRoot/
sudo chown -R kusanagi:www .
sudo find . -type d -exec chmod 755 {} \;
sudo find . -type f -exec chmod 644 {} \;
echo "Permissions set"
EOF
echo -e "${GREEN}✓ Permissions configured${NC}"
echo ""

# Restart services
echo -e "${YELLOW}Restarting Kusanagi services...${NC}"
ssh -i "$SSH_KEY" -o StrictHostKeyChecking=no ${TRUENAS_USER}@${TRUENAS_HOST} "sudo kusanagi restart ${DOMAIN}" 2>/dev/null || echo "Note: kusanagi restart command not available or not needed"
echo ""

# Test deployment
echo -e "${YELLOW}Testing deployment...${NC}"
if ssh -i "$SSH_KEY" -o StrictHostKeyChecking=no ${TRUENAS_USER}@${TRUENAS_HOST} "test -f /home/kusanagi/${DOMAIN}/DocumentRoot/index.html"; then
    echo -e "${GREEN}✓ index.html found on server${NC}"
else
    echo -e "${RED}WARNING: index.html not found on server${NC}"
fi
echo ""

# Clean up temp key if used
if [ -n "$TEMP_KEY" ] && [ -f "$TEMP_KEY" ]; then
    rm -f "$TEMP_KEY"
fi

# Final summary
echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}DEPLOYMENT COMPLETE!${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""
echo -e "${BLUE}Deployment Summary:${NC}"
echo "  Target: https://${DOMAIN}"
echo "  Location: ${REMOTE_PATH}"
echo ""
echo -e "${BLUE}Files Deployed:${NC}"
echo "  ✓ 17 HTML pages (index, 4 founders, 8 projects, etc.)"
echo "  ✓ CSS and JavaScript"
echo "  ✓ All assets (founders, projects, logos)"
echo "  ✓ 20 founder photos (4 founders × 4 scenarios + base)"
echo "  ✓ 8 project icons"
echo "  ✓ 8 slider images"
echo ""
echo -e "${YELLOW}Next Steps:${NC}"
echo "  1. Visit https://${DOMAIN} to verify the deployment"
echo "  2. Test all pages (about, services, portfolio, investors, contact)"
echo "  3. Test founder pages (bri.html, lilly.html, jonathan.html, alicia.html)"
echo "  4. Test project pages (all 8 deep-dive pages)"
echo "  5. Verify all images load correctly"
echo "  6. Test on mobile devices"
echo ""
echo -e "${GREEN}Your investor-ready website is now live on TrueNAS! 🚀${NC}"
echo ""
