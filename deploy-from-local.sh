#!/bin/bash
#
# ISN.BIZ WordPress Deployment - LOCAL MACHINE SCRIPT
#
# Run this script from your local machine (WSL/Git Bash)
# It will:
# 1. Transfer the theme package to TrueNAS
# 2. Transfer the deployment script
# 3. Execute the deployment on TrueNAS
#
# Usage: bash deploy-from-local.sh
#

set -e

# Color output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Configuration
TRUENAS_HOST="10.0.0.89"
TRUENAS_USER="jdmal"
SSH_KEY="$HOME/.ssh/truenas_jdmal"
THEME_DIR="D:/workspace/ISNBIZ_Files"
THEME_NAME="wp-theme-isnbiz-2026"

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}ISN.BIZ Deployment from Local Machine${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# Check if we're in WSL or Git Bash
if [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
    # Git Bash on Windows
    THEME_DIR="/d/workspace/ISNBIZ_Files"
elif [[ -f "/proc/version" ]] && grep -qi microsoft /proc/version; then
    # WSL
    THEME_DIR="/home/jdmal/workspace/ISNBIZ_Files"
fi

echo -e "${YELLOW}Environment:${NC}"
echo "  TrueNAS: ${TRUENAS_USER}@${TRUENAS_HOST}"
echo "  SSH Key: ${SSH_KEY}"
echo "  Theme Dir: ${THEME_DIR}"
echo ""

# Check if theme package exists
THEME_PACKAGE="${THEME_DIR}/${THEME_NAME}.tar.gz"
if [ ! -f "$THEME_PACKAGE" ]; then
    echo -e "${RED}ERROR: Theme package not found${NC}"
    echo "Expected: ${THEME_PACKAGE}"
    exit 1
fi
echo -e "${GREEN}✓ Theme package found ($(du -h "$THEME_PACKAGE" | cut -f1))${NC}"
echo ""

# Check if deployment script exists
DEPLOY_SCRIPT="${THEME_DIR}/deploy-to-kusanagi.sh"
if [ ! -f "$DEPLOY_SCRIPT" ]; then
    echo -e "${RED}ERROR: Deployment script not found${NC}"
    echo "Expected: ${DEPLOY_SCRIPT}"
    exit 1
fi
echo -e "${GREEN}✓ Deployment script found${NC}"
echo ""

# Check SSH connectivity
echo -e "${YELLOW}Testing SSH connection to TrueNAS...${NC}"
if ! ssh -i "$SSH_KEY" -o ConnectTimeout=5 ${TRUENAS_USER}@${TRUENAS_HOST} "echo 'Connection successful'" 2>/dev/null; then
    echo -e "${RED}ERROR: Cannot connect to TrueNAS${NC}"
    echo ""
    echo "Trying to set up SSH key..."
    echo "Please enter your TrueNAS password when prompted:"
    ssh-copy-id -i "$SSH_KEY" ${TRUENAS_USER}@${TRUENAS_HOST}

    if [ $? -ne 0 ]; then
        echo -e "${RED}SSH key setup failed${NC}"
        exit 1
    fi
    echo -e "${GREEN}✓ SSH key added successfully${NC}"
fi
echo -e "${GREEN}✓ SSH connection verified${NC}"
echo ""

# Step 1: Transfer theme package
echo -e "${YELLOW}[1/3] Transferring theme package to TrueNAS...${NC}"
scp -i "$SSH_KEY" "$THEME_PACKAGE" ${TRUENAS_USER}@${TRUENAS_HOST}:/tmp/
echo -e "${GREEN}✓ Theme package transferred${NC}"
echo ""

# Step 2: Transfer deployment script
echo -e "${YELLOW}[2/3] Transferring deployment script to TrueNAS...${NC}"
scp -i "$SSH_KEY" "$DEPLOY_SCRIPT" ${TRUENAS_USER}@${TRUENAS_HOST}:/tmp/deploy-to-kusanagi.sh
ssh -i "$SSH_KEY" ${TRUENAS_USER}@${TRUENAS_HOST} "chmod +x /tmp/deploy-to-kusanagi.sh"
echo -e "${GREEN}✓ Deployment script transferred${NC}"
echo ""

# Step 3: Execute deployment
echo -e "${YELLOW}[3/3] Executing deployment on TrueNAS...${NC}"
echo -e "${BLUE}Connecting to TrueNAS and running deployment...${NC}"
echo ""

ssh -i "$SSH_KEY" -t ${TRUENAS_USER}@${TRUENAS_HOST} "bash /tmp/deploy-to-kusanagi.sh"

echo ""
echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}LOCAL DEPLOYMENT COMPLETE!${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""
echo -e "${BLUE}What just happened:${NC}"
echo "  ✓ Theme package transferred to TrueNAS"
echo "  ✓ WordPress provisioned on Kusanagi"
echo "  ✓ Theme deployed and activated"
echo "  ✓ Pages and menus created"
echo ""
echo -e "${YELLOW}Next:${NC}"
echo "  1. Login to https://isn.biz/wp-admin"
echo "  2. Assign page templates"
echo "  3. Point DNS to TrueNAS"
echo ""
