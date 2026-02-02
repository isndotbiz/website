#!/bin/bash

# Premium Asset Generation and Upload Pipeline for ISN.BIZ
# This script generates 40+ premium assets and uploads them to S3

set -e

echo "=============================================================================="
echo "ISN.BIZ PREMIUM ASSET GENERATION & UPLOAD PIPELINE"
echo "=============================================================================="
echo ""

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check if FAL_API_KEY is set
if [ -z "$FAL_API_KEY" ]; then
    echo -e "${RED}ERROR: FAL_API_KEY environment variable not set${NC}"
    echo ""
    echo "Please retrieve your FAL API Key from 1Password and set it:"
    echo "  export FAL_API_KEY='your-fal-api-key-here'"
    echo ""
    echo "Then run this script again."
    exit 1
fi

echo -e "${GREEN}✓ FAL_API_KEY is set${NC}"
echo ""

# Check Python packages
echo -e "${BLUE}Checking Python dependencies...${NC}"
if ! python3 -m pip install -q -r requirements_assets.txt; then
    echo -e "${RED}ERROR: Failed to install Python dependencies${NC}"
    exit 1
fi
echo -e "${GREEN}✓ Python dependencies installed${NC}"
echo ""

# Check AWS credentials
echo -e "${BLUE}Checking AWS credentials...${NC}"
if ! aws sts get-caller-identity &> /dev/null; then
    echo -e "${YELLOW}WARNING: AWS credentials not configured${NC}"
    echo "You'll need to configure AWS CLI before uploading to S3:"
    echo "  aws configure"
    echo ""
    echo "Continuing with generation only..."
    SKIP_UPLOAD=true
else
    echo -e "${GREEN}✓ AWS credentials configured${NC}"
    SKIP_UPLOAD=false
fi
echo ""

# Step 1: Generate assets
echo "=============================================================================="
echo "STEP 1: GENERATING PREMIUM ASSETS"
echo "=============================================================================="
echo ""
echo "This will generate 40+ award-winning quality assets:"
echo "  - 8 Hero Backgrounds"
echo "  - 12 Service Icons"
echo "  - 15 Portfolio Mockups"
echo "  - 8 Abstract Backgrounds"
echo "  - 5 Infographics/Illustrations"
echo ""
echo "Estimated time: 5-10 minutes (with API rate limiting)"
echo ""
read -p "Press Enter to start generation, or Ctrl+C to cancel..."
echo ""

python3 generate_premium_assets.py

if [ $? -ne 0 ]; then
    echo -e "${RED}ERROR: Asset generation failed${NC}"
    exit 1
fi

echo ""
echo -e "${GREEN}✓ Asset generation complete!${NC}"
echo ""

# Step 2: Upload to S3 (if credentials are available)
if [ "$SKIP_UPLOAD" = false ]; then
    echo "=============================================================================="
    echo "STEP 2: UPLOADING ASSETS TO S3"
    echo "=============================================================================="
    echo ""
    echo "This will upload all assets to: isnbiz-assets-1769962280"
    echo ""
    read -p "Press Enter to start upload, or Ctrl+C to cancel..."
    echo ""

    python3 upload_assets_to_s3.py

    if [ $? -ne 0 ]; then
        echo -e "${RED}ERROR: S3 upload failed${NC}"
        exit 1
    fi

    echo ""
    echo -e "${GREEN}✓ S3 upload complete!${NC}"
    echo ""
else
    echo "=============================================================================="
    echo "STEP 2: S3 UPLOAD SKIPPED"
    echo "=============================================================================="
    echo ""
    echo "To upload assets to S3, configure AWS credentials and run:"
    echo "  python3 upload_assets_to_s3.py"
    echo ""
fi

# Summary
echo "=============================================================================="
echo "PIPELINE COMPLETE!"
echo "=============================================================================="
echo ""
echo -e "${GREEN}✓ Assets generated: /home/jdmal/workspace/ISNBIZ_Files/assets/premium/${NC}"
if [ "$SKIP_UPLOAD" = false ]; then
    echo -e "${GREEN}✓ Assets uploaded to S3: isnbiz-assets-1769962280${NC}"
    echo -e "${GREEN}✓ Asset reference page: /home/jdmal/workspace/ISNBIZ_Files/assets/premium/asset_reference.html${NC}"
fi
echo ""
echo "Next steps:"
echo "  1. Review generated assets in assets/premium/ directory"
if [ "$SKIP_UPLOAD" = false ]; then
    echo "  2. Open asset_reference.html in browser to see all assets"
    echo "  3. Use asset URLs in your website"
else
    echo "  2. Configure AWS credentials and upload to S3"
fi
echo ""
echo "=============================================================================="
