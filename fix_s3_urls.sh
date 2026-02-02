#!/bin/bash
# Fix S3 URL backslashes in ISN.BIZ website
# This fixes the Windows path separator issue causing image loading failures

echo "========================================="
echo "ISN.BIZ S3 URL Backslash Fix"
echo "========================================="
echo ""

# Backup files first
echo "Creating backups..."
for file in alicia.html bri.html jonathan.html lilly.html index.html portfolio-grid.html; do
    if [ -f "$file" ]; then
        cp "$file" "$file.backup_$(date +%Y%m%d_%H%M%S)"
        echo "  ✓ Backed up $file"
    fi
done
echo ""

# Fix backslashes in founder pages and index
echo "Fixing backslashes in S3 URLs..."
for file in alicia.html bri.html jonathan.html lilly.html index.html; do
    if [ -f "$file" ]; then
        # Replace founders\ with founders/
        sed -i 's|founders\\|founders/|g' "$file"
        echo "  ✓ Fixed $file"
    fi
done
echo ""

# Fix portfolio-grid.html duplicate URL prefix
echo "Fixing duplicate URL prefix in portfolio-grid.html..."
if [ -f "portfolio-grid.html" ]; then
    sed -i 's|premium_v3/https://isnbiz-assets|https://isnbiz-assets|g' portfolio-grid.html
    echo "  ✓ Fixed portfolio-grid.html"
fi
echo ""

# Report changes
echo "========================================="
echo "Changes Applied:"
echo "========================================="
echo "1. Replaced founders\\ with founders/ in:"
echo "   - alicia.html"
echo "   - bri.html"
echo "   - jonathan.html"
echo "   - lilly.html"
echo "   - index.html"
echo ""
echo "2. Removed duplicate URL prefix in:"
echo "   - portfolio-grid.html"
echo ""
echo "========================================="
echo "Next Steps:"
echo "========================================="
echo "1. Review changes with: git diff"
echo "2. Test website: python test_website.py"
echo "3. If satisfied, commit: git add . && git commit -m 'Fix S3 URL path separators'"
echo "4. Upload missing S3 files (see WEBSITE_TEST_ANALYSIS.md)"
echo ""
echo "Backups created with .backup_* extension"
echo "✓ Fix complete!"
