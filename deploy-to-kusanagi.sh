#!/bin/bash
#
# ISN.BIZ WordPress Deployment to Kusanagi on TrueNAS
#
# This script:
# 1. Provisions a new Kusanagi site for isn.biz
# 2. Installs WordPress
# 3. Configures SSL with Let's Encrypt
# 4. Deploys the ISN.BIZ 2026 WordPress theme
# 5. Configures WordPress settings
#
# Usage: Run this script ON the TrueNAS server (10.0.0.89)
#        ssh jdmal@10.0.0.89
#        bash deploy-to-kusanagi.sh
#

set -e  # Exit on error

# Color output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
DOMAIN="isn.biz"
SITE_TITLE="iSN.BiZ Inc"
ADMIN_EMAIL="contact@isn.biz"
PHP_VERSION="8.2"
THEME_NAME="wp-theme-isnbiz-2026"

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}ISN.BIZ WordPress Deployment to Kusanagi${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# Check if running as root
if [[ $EUID -eq 0 ]]; then
   echo -e "${RED}ERROR: Do not run this script as root${NC}"
   echo "Run as regular user with sudo access"
   exit 1
fi

# Check if Kusanagi is installed
if ! command -v kusanagi &> /dev/null; then
    echo -e "${RED}ERROR: Kusanagi not found${NC}"
    echo "Please install Kusanagi first: https://kusanagi.tokyo/en/"
    exit 1
fi

echo -e "${GREEN}✓ Kusanagi found${NC}"
echo ""

# Step 1: Check if site already exists
echo -e "${YELLOW}[1/7] Checking if site already exists...${NC}"
if [ -d "/home/kusanagi/${DOMAIN}" ]; then
    echo -e "${YELLOW}WARNING: Site ${DOMAIN} already exists${NC}"
    read -p "Do you want to remove it and start fresh? (yes/no): " -r
    if [[ $REPLY =~ ^[Yy]es$ ]]; then
        echo "Removing existing site..."
        sudo kusanagi remove ${DOMAIN} --yes
        echo -e "${GREEN}✓ Existing site removed${NC}"
    else
        echo "Skipping provision step..."
    fi
else
    echo -e "${GREEN}✓ Site does not exist, ready to provision${NC}"
fi
echo ""

# Step 2: Provision Kusanagi site
echo -e "${YELLOW}[2/7] Provisioning Kusanagi site for ${DOMAIN}...${NC}"
if [ ! -d "/home/kusanagi/${DOMAIN}" ]; then
    echo "Creating new Kusanagi site..."

    # Generate random database password
    DB_PASSWORD=$(openssl rand -base64 32 | tr -d "=+/" | cut -c1-25)

    sudo kusanagi provision \
        --wordpress \
        --fqdn ${DOMAIN} \
        --dbname isnbiz_wp \
        --dbuser isnbiz_user \
        --dbpass "${DB_PASSWORD}" \
        --php ${PHP_VERSION} \
        ${DOMAIN}

    echo -e "${GREEN}✓ Kusanagi site provisioned${NC}"
    echo -e "${BLUE}Database credentials:${NC}"
    echo "  DB Name: isnbiz_wp"
    echo "  DB User: isnbiz_user"
    echo "  DB Pass: ${DB_PASSWORD}"
    echo ""
    echo -e "${YELLOW}IMPORTANT: Save these credentials!${NC}"
    echo ""
else
    echo -e "${GREEN}✓ Using existing site${NC}"
fi
echo ""

# Step 3: Install WordPress
echo -e "${YELLOW}[3/7] Installing WordPress...${NC}"

# Prompt for admin credentials
echo "WordPress admin credentials:"
read -p "Admin username [admin]: " WP_ADMIN_USER
WP_ADMIN_USER=${WP_ADMIN_USER:-admin}

read -sp "Admin password (leave empty to generate): " WP_ADMIN_PASS
echo ""
if [ -z "$WP_ADMIN_PASS" ]; then
    WP_ADMIN_PASS=$(openssl rand -base64 32 | tr -d "=+/" | cut -c1-25)
    echo -e "${BLUE}Generated password: ${WP_ADMIN_PASS}${NC}"
fi

cd /home/kusanagi/${DOMAIN}/DocumentRoot

# Check if WordPress is already installed
if sudo -u kusanagi wp core is-installed 2>/dev/null; then
    echo -e "${YELLOW}WordPress already installed, skipping...${NC}"
else
    sudo -u kusanagi wp core install \
        --url="https://${DOMAIN}" \
        --title="${SITE_TITLE}" \
        --admin_user="${WP_ADMIN_USER}" \
        --admin_password="${WP_ADMIN_PASS}" \
        --admin_email="${ADMIN_EMAIL}"

    echo -e "${GREEN}✓ WordPress installed${NC}"
    echo -e "${BLUE}WordPress admin credentials:${NC}"
    echo "  URL: https://${DOMAIN}/wp-admin"
    echo "  Username: ${WP_ADMIN_USER}"
    echo "  Password: ${WP_ADMIN_PASS}"
    echo ""
    echo -e "${YELLOW}IMPORTANT: Save these credentials!${NC}"
fi
echo ""

# Step 4: Configure SSL
echo -e "${YELLOW}[4/7] Configuring SSL with Let's Encrypt...${NC}"
read -p "Configure SSL? (yes/no) [yes]: " -r
CONFIGURE_SSL=${REPLY:-yes}

if [[ $CONFIGURE_SSL =~ ^[Yy]es$ ]]; then
    sudo kusanagi ssl --email ${ADMIN_EMAIL} ${DOMAIN}
    echo -e "${GREEN}✓ SSL configured${NC}"
else
    echo "Skipping SSL configuration"
fi
echo ""

# Step 5: Deploy theme
echo -e "${YELLOW}[5/7] Deploying ISN.BIZ 2026 theme...${NC}"

# Check if theme package exists in /tmp
THEME_PACKAGE="/tmp/${THEME_NAME}.tar.gz"
if [ ! -f "$THEME_PACKAGE" ]; then
    echo -e "${RED}ERROR: Theme package not found at ${THEME_PACKAGE}${NC}"
    echo ""
    echo "Please transfer the theme package first:"
    echo "  scp D:/workspace/ISNBIZ_Files/${THEME_NAME}.tar.gz jdmal@10.0.0.89:/tmp/"
    echo ""
    read -p "Press Enter after transferring the file, or Ctrl+C to exit..."
fi

# Extract theme
cd /home/kusanagi/${DOMAIN}/DocumentRoot/wp-content/themes/

if [ -d "${THEME_NAME}" ]; then
    echo -e "${YELLOW}Theme directory exists, removing...${NC}"
    sudo rm -rf ${THEME_NAME}
fi

sudo tar -xzf ${THEME_PACKAGE}
sudo chown -R kusanagi:www ${THEME_NAME}/
sudo chmod -R 755 ${THEME_NAME}/

echo -e "${GREEN}✓ Theme deployed${NC}"
echo ""

# Step 6: Activate theme
echo -e "${YELLOW}[6/7] Activating theme...${NC}"
cd /home/kusanagi/${DOMAIN}/DocumentRoot
sudo -u kusanagi wp theme activate ${THEME_NAME}
echo -e "${GREEN}✓ Theme activated${NC}"
echo ""

# Step 7: Configure WordPress settings
echo -e "${YELLOW}[7/7] Configuring WordPress settings...${NC}"

# Set permalinks to post name
sudo -u kusanagi wp rewrite structure '/%postname%/' --hard

# Disable comments
sudo -u kusanagi wp plugin install disable-comments --activate

# Set timezone
sudo -u kusanagi wp option update timezone_string 'America/Los_Angeles'

# Update site description
sudo -u kusanagi wp option update blogdescription 'Building the future of enterprise software with innovative, AI-powered solutions since 2015'

# Create pages
echo "Creating WordPress pages..."

# Check and create pages
for page in "Home" "About" "Services" "Portfolio" "Investors" "Contact"; do
    PAGE_EXISTS=$(sudo -u kusanagi wp post list --post_type=page --name=$(echo $page | tr '[:upper:]' '[:lower:]') --format=count)
    if [ "$PAGE_EXISTS" -eq "0" ]; then
        sudo -u kusanagi wp post create \
            --post_type=page \
            --post_title="$page" \
            --post_status=publish \
            --post_author=1
        echo "  - Created: $page"
    else
        echo "  - Exists: $page"
    fi
done

# Set front page
HOME_ID=$(sudo -u kusanagi wp post list --post_type=page --name=home --field=ID --format=csv)
if [ ! -z "$HOME_ID" ]; then
    sudo -u kusanagi wp option update show_on_front 'page'
    sudo -u kusanagi wp option update page_on_front $HOME_ID
    echo "  - Set Home as front page"
fi

# Create menu
MENU_EXISTS=$(sudo -u kusanagi wp menu list --format=count)
if [ "$MENU_EXISTS" -eq "0" ]; then
    sudo -u kusanagi wp menu create "Primary Menu"
    MENU_ID=$(sudo -u kusanagi wp menu list --format=csv | tail -n1 | cut -d',' -f1)

    # Add pages to menu
    for page in "About" "Services" "Portfolio" "Investors" "Contact"; do
        PAGE_ID=$(sudo -u kusanagi wp post list --post_type=page --name=$(echo $page | tr '[:upper:]' '[:lower:]') --field=ID --format=csv)
        if [ ! -z "$PAGE_ID" ]; then
            sudo -u kusanagi wp menu item add-post $MENU_ID $PAGE_ID
        fi
    done

    # Assign menu to location
    sudo -u kusanagi wp menu location assign $MENU_ID primary
    echo "  - Created and assigned Primary Menu"
fi

echo -e "${GREEN}✓ WordPress configured${NC}"
echo ""

# Restart services
echo -e "${YELLOW}Restarting services...${NC}"
sudo kusanagi restart ${DOMAIN}
echo -e "${GREEN}✓ Services restarted${NC}"
echo ""

# Final summary
echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}DEPLOYMENT COMPLETE!${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""
echo -e "${BLUE}Site Information:${NC}"
echo "  URL: https://${DOMAIN}"
echo "  Admin: https://${DOMAIN}/wp-admin"
echo "  Theme: ISN.BIZ 2026"
echo ""
echo -e "${BLUE}Credentials:${NC}"
echo "  Username: ${WP_ADMIN_USER}"
echo "  Password: ${WP_ADMIN_PASS}"
echo ""
echo -e "${YELLOW}Next Steps:${NC}"
echo "1. Login to WordPress admin"
echo "2. Assign page templates (Portfolio page → Template: Portfolio)"
echo "3. Customize content as needed"
echo "4. Test all pages and functionality"
echo "5. Update DNS to point ${DOMAIN} to this server"
echo ""
echo -e "${GREEN}Your investor-ready website is live! 🚀${NC}"
