#!/bin/bash

# Quick Start Script for Premium Asset Generation
# This script guides users through the setup and execution

clear

cat << "EOF"
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║               ISN.BIZ PREMIUM ASSET LIBRARY GENERATOR                         ║
║                   Award-Winning Quality Assets                                ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝

This script will help you generate 40+ premium assets for the isn.biz website.

Assets include:
  • 8 Hero Backgrounds (stunning full-width images)
  • 12 Service Icons (minimalist, professional)
  • 15 Portfolio Mockups (realistic interface screenshots)
  • 8 Abstract Backgrounds (versatile section backgrounds)
  • 5 Infographics (visual storytelling elements)

All assets feature ISN.BIZ brand colors (Blue #1E9FF2, Cyan #5FDFDF)
Optimized as WebP format for maximum performance.

EOF

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "STEP 1: VERIFY SETUP"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Run verification
python3 verify_setup.py

VERIFY_RESULT=$?

if [ $VERIFY_RESULT -ne 0 ]; then
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "SETUP INCOMPLETE"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    echo "Please complete the setup steps above, then run this script again."
    echo ""
    echo "Most common issue: FAL API Key not set"
    echo "  1. Get your key from 1Password: 'FAL API Key'"
    echo "  2. Run: export FAL_API_KEY='your-key-here'"
    echo "  3. Run: ./quick_start.sh"
    echo ""
    exit 1
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "STEP 2: GENERATE ASSETS"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Ready to generate 40+ premium assets!"
echo ""
echo "Estimated time: 5-10 minutes"
echo "API calls: 48 (with 2-second rate limiting)"
echo "Output: /home/jdmal/workspace/ISNBIZ_Files/assets/premium/"
echo ""
read -p "Press Enter to start generation, or Ctrl+C to cancel..."
echo ""

# Run the main pipeline
./generate_and_upload_premium_assets.sh

if [ $? -eq 0 ]; then
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "SUCCESS!"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    echo "✓ Assets generated successfully"
    echo "✓ All assets saved to: /home/jdmal/workspace/ISNBIZ_Files/assets/premium/"
    echo ""
    echo "Next steps:"
    echo ""
    echo "1. Review your assets:"
    echo "   Open: assets/premium/asset_reference.html"
    echo ""
    echo "2. Check asset URLs:"
    echo "   View: assets/premium/asset_urls.json"
    echo ""
    echo "3. Read usage guide:"
    echo "   View: ASSET_USAGE_GUIDE.md"
    echo ""
    echo "4. Browse catalog:"
    echo "   View: ASSET_CATALOG.md"
    echo ""
    echo "Your premium asset library is ready to use!"
    echo ""
else
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "ERROR"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    echo "Asset generation encountered an error."
    echo "Please check the output above for details."
    echo ""
    exit 1
fi
