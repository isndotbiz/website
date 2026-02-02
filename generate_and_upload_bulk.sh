#!/bin/bash
# Quick Start: Generate and Upload Bulk Images
# Usage: ./generate_and_upload_bulk.sh

set -e

echo "=================================="
echo "BULK IMAGE GENERATION & UPLOAD"
echo "=================================="
echo ""

# Check if virtual environment exists
if [ ! -d "venv_fal" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv_fal
    source venv_fal/bin/activate
    echo "Installing dependencies..."
    pip install fal-client pillow requests boto3
else
    source venv_fal/bin/activate
fi

echo ""
echo "Step 1: Generating 30+ images with FAL API..."
echo "Settings: LOW quality, 1024x1024, WebP format"
echo ""

python3 generate_bulk_images.py

echo ""
echo "Step 2: Uploading to S3..."
echo ""

python3 upload_generated_to_s3.py

echo ""
echo "=================================="
echo "COMPLETE!"
echo "=================================="
echo ""
echo "Images generated: assets/generated/"
echo "S3 location: s3://isn-biz-premium-assets/premium_v3/generated/"
echo "URL mapping: assets/generated/s3_urls.json"
echo ""
echo "Next step: Update HTML files with S3 URLs"
echo ""
