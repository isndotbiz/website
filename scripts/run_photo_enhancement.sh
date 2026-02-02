#!/bin/bash
#
# Run founder photo enhancement using fal.ai
# This script:
# 1. Activates virtual environment
# 2. Gets FAL API key from 1Password
# 3. Runs the photo enhancement script
#

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

echo "=============================================================================="
echo "FOUNDER PHOTO ENHANCEMENT - Setup"
echo "=============================================================================="

# Step 1: Activate virtual environment
echo ""
echo "Step 1: Activating virtual environment..."
if [ ! -d "$PROJECT_DIR/venv_fal" ]; then
    echo "ERROR: Virtual environment not found at $PROJECT_DIR/venv_fal"
    echo ""
    echo "Create it with:"
    echo "  python3 -m venv venv_fal"
    echo "  source venv_fal/bin/activate"
    echo "  pip install fal-client requests"
    exit 1
fi

source "$PROJECT_DIR/venv_fal/bin/activate"
echo "✓ Virtual environment activated"

# Step 2: Check if fal-client is installed
echo ""
echo "Step 2: Checking dependencies..."
if ! python -c "import fal_client" 2>/dev/null; then
    echo "Installing fal-client..."
    pip install fal-client requests
fi
echo "✓ Dependencies installed"

# Step 3: Get FAL API key from 1Password
echo ""
echo "Step 3: Getting FAL API key from 1Password..."

# Check if already signed in
if ! op whoami &>/dev/null; then
    echo "Signing into 1Password..."
    eval $(op signin)
fi

export FAL_KEY=$(op read "op://Research/FAL API Key/credential")

if [ -z "$FAL_KEY" ]; then
    echo "ERROR: Could not retrieve FAL API key from 1Password"
    echo ""
    echo "Make sure:"
    echo "  1. 1Password CLI is installed"
    echo "  2. You're signed in: eval \$(op signin)"
    echo "  3. The key exists: op item get 'FAL API Key' --vault Research"
    exit 1
fi

echo "✓ FAL API key retrieved (${#FAL_KEY} characters)"

# Step 4: Run the enhancement script
echo ""
echo "=============================================================================="
echo "STARTING PHOTO ENHANCEMENT"
echo "=============================================================================="
echo ""

python "$SCRIPT_DIR/fix_necks_and_create_community_photos.py"

EXIT_CODE=$?

echo ""
echo "=============================================================================="
if [ $EXIT_CODE -eq 0 ]; then
    echo "PHOTO ENHANCEMENT COMPLETE!"
    echo "=============================================================================="
    echo ""
    echo "Check results:"
    echo "  Fixed necks:      $PROJECT_DIR/assets/founders/fixed_necks/"
    echo "  Community photos: $PROJECT_DIR/assets/founders/community/"
else
    echo "PHOTO ENHANCEMENT FAILED (exit code: $EXIT_CODE)"
    echo "=============================================================================="
    echo ""
    echo "Check the error messages above for details."
fi

exit $EXIT_CODE
