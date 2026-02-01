#!/bin/bash
# run_fal_tests.sh
# Convenience script to run fal.ai model comparison tests

set -e  # Exit on error

echo "================================================================================"
echo "fal.ai Model Comparison Test Runner"
echo "================================================================================"
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if API key is set
if [ -z "$FAL_KEY" ]; then
    echo -e "${RED}ERROR: FAL_KEY environment variable not set!${NC}"
    echo ""
    echo "The value 'yfmv5bml45cw5jv5yf4dstk3py' from 1Password is an item ID, not the API key."
    echo ""
    echo "To get your actual API key:"
    echo "  1. Open 1Password"
    echo "  2. Find 'FAL API Key' entry"
    echo "  3. Copy the actual API key value"
    echo "  4. Run: export FAL_KEY='your-actual-api-key-here'"
    echo ""
    echo "OR generate a new key at: https://fal.ai/dashboard/keys"
    echo ""
    exit 1
fi

# Display API key info (first 10 chars only for security)
echo -e "${GREEN}✓ API Key detected${NC}"
echo "  First 10 characters: ${FAL_KEY:0:10}..."
echo "  Key length: ${#FAL_KEY} characters"
echo ""

# Navigate to workspace root
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
WORKSPACE_DIR="$( dirname "$SCRIPT_DIR" )"
cd "$WORKSPACE_DIR"

echo "Working directory: $WORKSPACE_DIR"
echo ""

# Check if virtual environment exists
if [ ! -d "venv_fal" ]; then
    echo -e "${YELLOW}Virtual environment not found. Creating...${NC}"
    python3 -m venv venv_fal
    source venv_fal/bin/activate
    pip install --quiet fal-client requests
    echo -e "${GREEN}✓ Virtual environment created${NC}"
    echo ""
else
    source venv_fal/bin/activate
    echo -e "${GREEN}✓ Virtual environment activated${NC}"
    echo ""
fi

# Check if packages are installed
if ! python -c "import fal_client" 2>/dev/null; then
    echo -e "${YELLOW}Installing required packages...${NC}"
    pip install --quiet fal-client requests
    echo -e "${GREEN}✓ Packages installed${NC}"
    echo ""
fi

# Menu
echo "================================================================================"
echo "Select test to run:"
echo "================================================================================"
echo "1. Quick API verification test (1 image, ~30 seconds)"
echo "2. Full model comparison (8-12 images, 2-5 minutes)"
echo "3. View existing results"
echo "4. Exit"
echo ""
read -p "Enter choice [1-4]: " choice

case $choice in
    1)
        echo ""
        echo "================================================================================"
        echo "Running Quick API Verification Test"
        echo "================================================================================"
        echo ""
        python scripts/quick_test_fal.py
        ;;
    2)
        echo ""
        echo "================================================================================"
        echo "Running Full Model Comparison Test"
        echo "================================================================================"
        echo ""
        echo "This will test 4 models and generate 2-3 images per model."
        echo "Estimated time: 2-5 minutes"
        echo ""
        read -p "Continue? [y/N]: " confirm
        if [[ $confirm =~ ^[Yy]$ ]]; then
            python scripts/test_fal_models_v2.py
        else
            echo "Cancelled."
            exit 0
        fi
        ;;
    3)
        echo ""
        if [ -f "assets/test-samples/model_comparison_report.md" ]; then
            echo "================================================================================"
            echo "Existing Test Results"
            echo "================================================================================"
            echo ""
            cat assets/test-samples/model_comparison_report.md
            echo ""
            echo "Images location: assets/test-samples/"
            ls -lh assets/test-samples/*.png 2>/dev/null || echo "No images found yet."
        else
            echo -e "${YELLOW}No test results found yet.${NC}"
            echo "Run option 1 or 2 to generate results."
        fi
        ;;
    4)
        echo "Exiting."
        exit 0
        ;;
    *)
        echo -e "${RED}Invalid choice. Exiting.${NC}"
        exit 1
        ;;
esac

echo ""
echo "================================================================================"
echo "Done!"
echo "================================================================================"
