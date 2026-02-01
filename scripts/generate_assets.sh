#!/bin/bash
# Quick launcher for AI asset generation
# Usage: ./generate_assets.sh [options]

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_SCRIPT="$SCRIPT_DIR/generate_ai_assets.py"

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}╔════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║     ISN.BIZ AI Asset Generation Tool                  ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════╝${NC}"
echo ""

# Check if FAL_KEY is set
if [ -z "$FAL_KEY" ]; then
    echo -e "${YELLOW}⚠  FAL_KEY environment variable not set${NC}"
    echo ""
    echo "Please set your fal.ai API key:"
    echo -e "${GREEN}  export FAL_KEY='your-api-key-here'${NC}"
    echo ""
    echo "Get your API key from: https://fal.ai/"
    echo ""
    read -p "Enter your FAL_KEY now (or press Enter to exit): " user_key

    if [ -z "$user_key" ]; then
        echo "Exiting..."
        exit 1
    fi

    export FAL_KEY="$user_key"
    echo -e "${GREEN}✓ API key set${NC}"
    echo ""
fi

# Check dependencies
if ! python3 -c "import fal_client" 2>/dev/null; then
    echo -e "${YELLOW}⚠  Missing dependencies${NC}"
    echo ""
    read -p "Install required packages? (y/n): " install

    if [ "$install" = "y" ]; then
        echo "Installing dependencies..."
        pip install -r "$SCRIPT_DIR/requirements-assets.txt"
        echo ""
    else
        echo "Please install dependencies manually:"
        echo -e "${GREEN}  pip install -r $SCRIPT_DIR/requirements-assets.txt${NC}"
        exit 1
    fi
fi

# Show menu
echo "Select generation mode:"
echo ""
echo "  1) Test mode (4 images, one per category)"
echo "  2) Full generation (23 images, all assets)"
echo "  3) Hero backgrounds only (5 images)"
echo "  4) Portfolio mockups only (8 images)"
echo "  5) Service icons only (6 images)"
echo "  6) Section dividers only (4 images)"
echo "  7) Custom (specify categories)"
echo ""
read -p "Enter choice (1-7): " choice

case $choice in
    1)
        echo -e "${GREEN}Running in test mode...${NC}"
        python3 "$PYTHON_SCRIPT" --test
        ;;
    2)
        echo -e "${GREEN}Generating all assets...${NC}"
        python3 "$PYTHON_SCRIPT"
        ;;
    3)
        echo -e "${GREEN}Generating hero backgrounds...${NC}"
        python3 "$PYTHON_SCRIPT" --categories hero_backgrounds
        ;;
    4)
        echo -e "${GREEN}Generating portfolio mockups...${NC}"
        python3 "$PYTHON_SCRIPT" --categories portfolio_mockups
        ;;
    5)
        echo -e "${GREEN}Generating service icons...${NC}"
        python3 "$PYTHON_SCRIPT" --categories service_icons
        ;;
    6)
        echo -e "${GREEN}Generating section dividers...${NC}"
        python3 "$PYTHON_SCRIPT" --categories section_dividers
        ;;
    7)
        echo ""
        echo "Available categories:"
        echo "  - hero_backgrounds"
        echo "  - portfolio_mockups"
        echo "  - service_icons"
        echo "  - section_dividers"
        echo ""
        read -p "Enter categories (space-separated): " categories
        echo -e "${GREEN}Generating selected categories...${NC}"
        python3 "$PYTHON_SCRIPT" --categories $categories
        ;;
    *)
        echo -e "${RED}Invalid choice${NC}"
        exit 1
        ;;
esac

# Show results
if [ $? -eq 0 ]; then
    echo ""
    echo -e "${GREEN}╔════════════════════════════════════════════════════════╗${NC}"
    echo -e "${GREEN}║              Generation Complete!                      ║${NC}"
    echo -e "${GREEN}╚════════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo "Assets saved to:"
    echo -e "${BLUE}  /mnt/d/workspace/ISNBIZ_Files/assets/images/${NC}"
    echo ""
    echo "View generated files:"
    echo -e "${GREEN}  ls -lh /mnt/d/workspace/ISNBIZ_Files/assets/images/*/${NC}"
    echo ""
    echo "Next steps:"
    echo "  1. Review generated images"
    echo "  2. Optimize for web (optional)"
    echo "  3. Integrate into website HTML"
    echo ""
else
    echo ""
    echo -e "${RED}Generation failed. Check error messages above.${NC}"
    exit 1
fi
