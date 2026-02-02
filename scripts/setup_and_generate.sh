#!/bin/bash
###############################################################################
# Professional Website Asset Generator - Setup & Run Script
# Uses fal.ai's latest 2026 models
###############################################################################

set -e  # Exit on error

echo "=============================================================================="
echo "🎨 Professional Website Asset Generator"
echo "Using fal.ai's Latest 2026 Models"
echo "=============================================================================="
echo ""

# Check if API key is set
if [ -z "$FAL_KEY" ]; then
    echo "❌ ERROR: FAL_KEY environment variable is not set!"
    echo ""
    echo "📋 Setup Instructions:"
    echo "   1. Open 1Password"
    echo "   2. Search for 'fal'"
    echo "   3. Copy the API key"
    echo "   4. Run: export FAL_KEY='your-api-key-here'"
    echo "   5. Run this script again"
    echo ""
    exit 1
fi

echo "✅ API key detected"
echo ""

# Check Python version
if ! command -v python3 &> /dev/null; then
    echo "❌ ERROR: python3 not found. Please install Python 3.8+."
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
echo "✅ Python detected: $PYTHON_VERSION"
echo ""

# Check/install dependencies
echo "📦 Checking dependencies..."
python3 -c "import requests" 2>/dev/null || {
    echo "Installing requests library..."
    pip install requests
}
echo "✅ Dependencies ready"
echo ""

# Navigate to script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo "📁 Working directory: $SCRIPT_DIR"
echo ""

# Confirm before proceeding
echo "=============================================================================="
echo "⚠️  ASSET GENERATION DETAILS"
echo "=============================================================================="
echo ""
echo "This will generate the following assets:"
echo ""
echo "  • 5 Hero Backgrounds (2560×1440)"
echo "    Model: FLUX.2 Max"
echo "    Est. time: ~2-3 minutes"
echo "    Est. cost: ~$0.25-0.50"
echo ""
echo "  • 10 Portfolio Mockups (1920×1080)"
echo "    Model: FLUX1.1 Pro Ultra"
echo "    Est. time: ~3-4 minutes"
echo "    Est. cost: ~$0.30-0.60"
echo ""
echo "  • 6 Service Icons (1024×1024)"
echo "    Model: FLUX.2 Pro"
echo "    Est. time: ~2 minutes"
echo "    Est. cost: ~$0.15-0.30"
echo ""
echo "  • 4 Team Visuals (1920×1080)"
echo "    Model: FLUX.2 Max"
echo "    Est. time: ~2 minutes"
echo "    Est. cost: ~$0.20-0.40"
echo ""
echo "  • 2-3 Video Assets (10s each, 1080p)"
echo "    Model: Kling 2.6 Pro"
echo "    Est. time: ~6-10 minutes"
echo "    Est. cost: ~$1.40-2.10"
echo ""
echo "=============================================================================="
echo "  TOTAL ESTIMATED TIME: 15-20 minutes"
echo "  TOTAL ESTIMATED COST: ~$2.30-$3.90"
echo "=============================================================================="
echo ""

read -p "🚀 Proceed with generation? (y/n) " -n 1 -r
echo ""

if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Cancelled."
    exit 0
fi

echo ""
echo "=============================================================================="
echo "🎨 Starting Asset Generation"
echo "=============================================================================="
echo ""

# Run the generator
python3 generate_website_assets.py

# Check if generation was successful
if [ $? -eq 0 ]; then
    echo ""
    echo "=============================================================================="
    echo "✅ GENERATION COMPLETE!"
    echo "=============================================================================="
    echo ""
    echo "Assets saved to:"
    echo "  /home/jdmal/workspace/ISNBIZ_Files/assets/generated/"
    echo ""
    echo "Next steps:"
    echo "  1. Review the generated assets"
    echo "  2. Check the manifest.json file for details"
    echo "  3. Integrate assets into your website"
    echo ""
    echo "=============================================================================="
else
    echo ""
    echo "=============================================================================="
    echo "❌ GENERATION FAILED"
    echo "=============================================================================="
    echo ""
    echo "Please check the error messages above and try again."
    echo ""
    exit 1
fi
