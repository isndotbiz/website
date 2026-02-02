#!/bin/bash
#
# Run all ISN.BIZ generation scripts
#

set -e

echo "========================================================================"
echo "ISN.BIZ - Running ALL Scripts"
echo "========================================================================"
echo ""

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Step 1: Ensure venv is set up
echo "Step 1: Setting up virtual environment..."
if [ ! -d "venv_fal" ]; then
    echo "Creating venv_fal..."
    python3 -m venv venv_fal
fi

# Activate venv (Windows path)
if [ -f "venv_fal/Scripts/activate" ]; then
    source venv_fal/Scripts/activate
elif [ -f "venv_fal/bin/activate" ]; then
    source venv_fal/bin/activate
else
    echo "ERROR: Could not find venv activation script"
    exit 1
fi

echo "✓ Virtual environment activated"
echo ""

# Step 2: Install packages
echo "Step 2: Installing required packages..."
pip install -q fal-client requests pillow boto3
echo "✓ Packages installed"
echo ""

# Step 3: Get FAL API key from 1Password
echo "Step 3: Getting FAL API key from 1Password..."
if ! command -v op &> /dev/null; then
    echo "ERROR: 1Password CLI not found"
    echo "Please install: https://developer.1password.com/docs/cli/get-started/"
    exit 1
fi

# Sign in if needed
if ! op whoami &>/dev/null; then
    echo "Signing into 1Password..."
    eval $(op signin)
fi

# Get API key
export FAL_KEY=$(op read "op://Research/FAL API Key/credential" 2>/dev/null)
if [ -z "$FAL_KEY" ]; then
    echo "ERROR: Could not get FAL API key from 1Password"
    echo "Check that 'FAL API Key' exists in 'Research' vault"
    exit 1
fi

echo "✓ FAL API key retrieved"
echo ""

# Step 4: Run photo enhancement script
echo "========================================================================"
echo "Running: Photo Enhancement (Fix necks + Community photos)"
echo "========================================================================"
echo ""

python scripts/fix_necks_and_create_community_photos.py
echo ""
echo "✓ Photo enhancement complete"
echo ""

# Step 5: Check generation status
echo "========================================================================"
echo "Running: Generation Status Check"
echo "========================================================================"
echo ""

bash check_generation_status.sh
echo ""

# Step 6: Convert to WebP (optional)
echo "========================================================================"
echo "Optional: Convert to WebP for optimization"
echo "========================================================================"
echo ""
echo "To convert images to WebP, run:"
echo "  for img in assets/founders/community/*.png; do"
echo "    cwebp -q 85 \"\$img\" -o \"\${img%.png}.webp\""
echo "  done"
echo ""

echo "========================================================================"
echo "ALL SCRIPTS COMPLETE!"
echo "========================================================================"
echo ""
echo "Generated:"
echo "  - Community outreach photos (8 images)"
echo "  - Neck proportion fixes (2 images)"
echo "  - All saved to assets/founders/"
echo ""
echo "Next steps:"
echo "  1. Review images in assets/founders/fixed_necks/ and community/"
echo "  2. Convert to WebP (optional)"
echo "  3. Commit to git"
echo "  4. Deploy to TrueNAS"
echo ""
