#!/bin/bash

echo "============================================================"
echo "HROC FOUNDER PHOTO ENHANCEMENT"
echo "Using fal.ai Portrait Enhance & FLUX 1.1 Pro Ultra"
echo "============================================================"
echo ""

# Check if API key is set
if [ -z "$FAL_API_KEY" ]; then
    echo "FAL_API_KEY not found in environment."
    echo ""
    echo "To get your API key:"
    echo "1. Go to https://fal.ai/"
    echo "2. Sign up/login"
    echo "3. Go to API Keys section"
    echo "4. Create or copy your API key"
    echo ""
    read -p "Enter your FAL API key: " api_key
    export FAL_API_KEY="$api_key"
    echo ""
fi

# Check Python availability
if ! command -v python3 &> /dev/null; then
    echo "ERROR: python3 not found. Please install Python 3."
    exit 1
fi

# Check requests library
echo "Checking dependencies..."
python3 -c "import requests" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "Installing requests library..."
    pip install requests
fi

echo ""
echo "Starting enhancement process..."
echo "This will create 24 enhanced photos (6 per founder)"
echo "Estimated cost: ~$5.52"
echo ""
read -p "Press Enter to continue or Ctrl+C to cancel..."
echo ""

# Run the enhancement script
python3 /home/jdmal/workspace/ISNBIZ_Files/scripts/enhance_founder_photos.py

echo ""
echo "============================================================"
echo "Enhancement complete!"
echo "Check: /home/jdmal/workspace/ISNBIZ_Files/assets/team/"
echo "============================================================"
