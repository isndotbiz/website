#!/bin/bash
# Quick status check for image generation

echo "================================"
echo "ISN.BIZ Business Visuals Status"
echo "================================"
echo ""

cd /d/workspace/ISNBIZ_Files

TOTAL=24
GENERATED=$(ls -1 assets/business/*.png 2>/dev/null | wc -l)
PERCENT=$((GENERATED * 100 / TOTAL))

echo "Progress: $GENERATED / $TOTAL images ($PERCENT%)"
echo ""

if [ -f "assets/business/s3_urls_business.json" ]; then
    echo "Catalog file exists"
    grep -o '"success_count": [0-9]*' assets/business/s3_urls_business.json 2>/dev/null
    grep -o '"failed_count": [0-9]*' assets/business/s3_urls_business.json 2>/dev/null
fi

echo ""
echo "Total size: $(du -sh assets/business/ | cut -f1)"
echo ""

if [ "$GENERATED" -eq "$TOTAL" ]; then
    echo "STATUS: COMPLETE!"
else
    echo "STATUS: IN PROGRESS..."
fi

echo "================================"
