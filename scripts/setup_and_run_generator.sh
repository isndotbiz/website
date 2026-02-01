#!/bin/bash
#
# Setup and run the fal.ai website asset generator
# This script helps configure the API key and runs the Python generator
#

set -e

echo "=========================================="
echo "fal.ai Website Asset Generator - Setup"
echo "=========================================="
echo ""

# Check if FAL_KEY is already set
if [ -z "$FAL_KEY" ]; then
    echo "FAL_KEY not found in environment."
    echo ""
    echo "To get your fal.ai API key:"
    echo "1. Search for 'fal' in 1Password"
    echo "2. Copy the API key"
    echo "3. Paste it when prompted below"
    echo ""
    read -p "Enter your fal.ai API key: " FAL_KEY
    export FAL_KEY
    echo ""
    echo "✓ API key set for this session"
else
    echo "✓ FAL_KEY found in environment"
fi

# Check Python dependencies
echo ""
echo "Checking Python dependencies..."

if ! command -v python3 &> /dev/null; then
    echo "✗ Python 3 not found. Please install Python 3.8 or higher."
    exit 1
fi

echo "✓ Python 3 found: $(python3 --version)"

# Check for required packages
echo "Checking required packages..."
python3 -c "import requests" 2>/dev/null || {
    echo "Installing requests package..."
    pip install requests
}

echo "✓ All dependencies satisfied"
echo ""

# Create output directory
OUTPUT_DIR="/mnt/d/workspace/ISNBIZ_Files/assets/generated"
mkdir -p "$OUTPUT_DIR"/{hero,portfolio,icons,team,video}
echo "✓ Output directories created at: $OUTPUT_DIR"
echo ""

# Display generation plan
echo "=========================================="
echo "Generation Plan"
echo "=========================================="
echo ""
echo "Using Latest 2026 Models:"
echo "  • FLUX.2 Pro - State-of-the-art image generation"
echo "  • Veo 3 - Google's latest video generation"
echo ""
echo "Assets to Generate:"
echo "  • 5 Hero Backgrounds (2560x1440)"
echo "  • 10 Portfolio Mockups"
echo "  • 6 Service Icons (1024x1024)"
echo "  • 4 Team/About Visuals"
echo "  • 2 Video Assets (1080p, 8s loops)"
echo ""
echo "Brand Colors:"
echo "  • Blue: #1E9FF2"
echo "  • Cyan: #5FDFDF"
echo "  • Charcoal: #3F4447"
echo ""
echo "Estimated Time: 10-20 minutes"
echo "Estimated Cost: $5-15 USD"
echo ""
read -p "Ready to start generation? (y/n) " -n 1 -r
echo ""

if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Generation cancelled."
    exit 0
fi

# Run the generator
echo ""
echo "=========================================="
echo "Starting Asset Generation"
echo "=========================================="
echo ""

cd /mnt/d/workspace/ISNBIZ_Files/scripts
python3 generate_website_assets.py

echo ""
echo "=========================================="
echo "Generation Complete!"
echo "=========================================="
echo ""
echo "Your assets are ready at:"
echo "$OUTPUT_DIR"
echo ""
echo "To use in your website:"
echo "1. Review the generated assets"
echo "2. Select your favorites"
echo "3. Copy to your website's assets directory"
echo "4. Update your HTML/CSS to reference the new assets"
echo ""
echo "A manifest.json file has been created with details of all generated assets."
echo ""
