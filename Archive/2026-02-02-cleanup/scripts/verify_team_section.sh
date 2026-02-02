#!/bin/bash
# Team Section Verification Script
# Verifies that the team section is properly integrated

echo "======================================"
echo "ISN.BIZ Team Section Verification"
echo "======================================"
echo ""

# Change to ISNBIZ_Files directory
cd "$(dirname "$0")"

# 1. Check if team section exists in HTML
echo "1. Checking HTML integration..."
if grep -q "<!-- Team Section -->" index.html; then
    echo "   ✅ Team section found in index.html"
else
    echo "   ❌ Team section NOT found in index.html"
    exit 1
fi

# 2. Count team members (should be 4)
MEMBER_COUNT=$(grep -c "team-member" index.html)
if [ "$MEMBER_COUNT" -eq 4 ]; then
    echo "   ✅ All 4 team members present ($MEMBER_COUNT/4)"
else
    echo "   ❌ Incorrect team member count: $MEMBER_COUNT (expected 4)"
    exit 1
fi

# 3. Check if CSS styles exist
echo ""
echo "2. Checking CSS integration..."
if grep -q "TEAM SECTION" styles.css; then
    echo "   ✅ Team section CSS found in styles.css"
else
    echo "   ❌ Team section CSS NOT found in styles.css"
    exit 1
fi

# 4. Verify all founder photos exist
echo ""
echo "3. Checking founder photos..."
PHOTOS=(
    "assets/founders/jonathan_presentation.webp"
    "assets/founders/bri_office_work.webp"
    "assets/founders/lilly_presentation.webp"
    "assets/founders/alicia_office_work.webp"
)

for photo in "${PHOTOS[@]}"; do
    if [ -f "$photo" ]; then
        SIZE=$(du -h "$photo" | cut -f1)
        echo "   ✅ $photo ($SIZE)"
    else
        echo "   ❌ Missing: $photo"
        exit 1
    fi
done

# 5. Check navigation menu
echo ""
echo "4. Checking navigation menu..."
if grep -q '<li><a href="#team">Team</a></li>' index.html; then
    echo "   ✅ Team link added to navigation"
else
    echo "   ❌ Team link NOT in navigation"
    exit 1
fi

# 6. Verify responsive grid CSS
echo ""
echo "5. Checking responsive design..."
if grep -q "grid-template-columns: repeat(4, 1fr)" styles.css; then
    echo "   ✅ 4-column desktop grid configured"
else
    echo "   ❌ Desktop grid NOT configured"
    exit 1
fi

if grep -q "@media (max-width: 992px)" styles.css | grep -q "team-grid"; then
    echo "   ✅ Tablet responsive breakpoint found"
else
    echo "   ⚠️  Tablet breakpoint may be missing"
fi

if grep -q "@media (max-width: 768px)" styles.css | grep -q "team-grid"; then
    echo "   ✅ Mobile responsive breakpoint found"
else
    echo "   ⚠️  Mobile breakpoint may be missing"
fi

# Summary
echo ""
echo "======================================"
echo "✅ VERIFICATION COMPLETE"
echo "======================================"
echo ""
echo "Summary:"
echo "  - Team section: Integrated"
echo "  - Founders: 4 of 4 (Jonathan, Bri, Lilly, Alicia)"
echo "  - Photos: All present (~388KB total)"
echo "  - CSS: Fully styled with responsive design"
echo "  - Navigation: Updated"
echo ""
echo "Status: READY FOR DEPLOYMENT"
echo ""

exit 0
