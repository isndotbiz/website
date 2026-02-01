# HROC Founder Photo Enhancement Guide

## Overview
This guide explains how to use fal.ai GPT-Image 1.5 to enhance the HROC founder photos into professional corporate headshots while maintaining their realistic appearance.

## fal.ai API Key Setup

### Get Your API Key
1. Go to 1Password and find the item: **"FAL API Key"** (ID: yfmv5bml45cw5jv5yf4dstk3py)
2. Copy the API key from that item
3. The key provided earlier (c6c9d4c5-ab4e-43dd-8f84-2e1cd9af2e4a) appears to be invalid - you need the correct key from 1Password

### Set Environment Variable
```bash
export FAL_KEY="your-actual-api-key-from-1password"
```

## Source Photos

The script uses the best REAL founder photos from:
`/mnt/d/workspace/projects/HROC_Files/HROC_Website_New/images/founders/`

### Selected Photos:
- **Alicia**: `a/alicia_hero_real.webp` (1.3 MB high-quality photo)
- **Bri**: `b/bri_varied_01.webp` (1.1 MB professional photo)
- **Jonathan**: `j/jonathan_varied_02.webp` (1.3 MB high-quality photo)
- **Lilly**: `l/lilly_varied_01.webp` (1.1 MB professional photo)

## Enhancement Strategy

### fal.ai Model: GPT-Image 1.5 Edit
- **Endpoint**: `fal-ai/gpt-image-1.5/edit`
- **Method**: Image-to-image editing
- **Maintains**: Original person's appearance and features
- **Enhances**: Professional quality, lighting, background, composition

### Parameters Used:
```python
{
    "image_url": "<uploaded-source-photo>",
    "prompt": "<professional-enhancement-prompt>",
    "image_size": "portrait_4_3",        # Professional headshot ratio
    "num_inference_steps": 50,            # High quality
    "guidance_scale": 7.5,                # Balance realism/prompt
    "num_images": 1,                      # One variant per prompt
    "enable_safety_checker": True,
    "output_format": "png"                # High quality output
}
```

### Enhancement Prompts Per Founder

Each founder gets **3 professional variants** with different prompts:

#### Variant 1 (Classic Corporate)
> "Professional executive headshot with warm smile, modern office background with soft natural lighting, high-quality corporate photography, business professional attire"

#### Variant 2 (Business Casual)
> "Professional portrait in business casual attire, confident approachable expression, contemporary workspace setting, natural window lighting, professional photographer quality"

#### Variant 3 (Clean Studio)
> "Corporate headshot with friendly professional demeanor, clean minimalist background, soft studio lighting, executive business portrait style"

## Running the Enhancement Script

### Prerequisites
```bash
# Install required Python package
pip install fal-client --upgrade

# Verify installation
python3 -c "import fal_client; print('fal-client installed successfully')"
```

### Execute the Script
```bash
# Set your API key
export FAL_KEY="your-actual-api-key-from-1password"

# Run the enhancement script
cd /mnt/d/workspace/ISNBIZ_Files
python3 scripts/enhance_founder_photos_gpt15.py
```

### Expected Output
The script will generate **12 images total** (3 variants × 4 founders):

```
/mnt/d/workspace/ISNBIZ_Files/assets/team/
├── alicia_enhanced_01.png
├── alicia_enhanced_02.png
├── alicia_enhanced_03.png
├── bri_enhanced_01.png
├── bri_enhanced_02.png
├── bri_enhanced_03.png
├── jonathan_enhanced_01.png
├── jonathan_enhanced_02.png
├── jonathan_enhanced_03.png
├── lilly_enhanced_01.png
├── lilly_enhanced_02.png
└── lilly_enhanced_03.png
```

## Output Specifications

- **Format**: PNG (high quality, no compression artifacts)
- **Aspect Ratio**: 4:3 portrait (professional headshot standard)
- **Quality**: High-resolution, professional corporate photography quality
- **Realistic**: Maintains actual founder appearance (not AI-generated faces)
- **Professional**: Enhanced lighting, background, composition, and styling

## Alternative: Using fal.ai FLUX Pro Kontext

If you want even more control over the editing, consider using **FLUX.1 Kontext [pro]**:

### Endpoint
```
fal-ai/flux-pro/kontext
```

### Benefits
- 12-billion parameter multimodal model
- Better at preserving character consistency
- Can make specific edits with instructions
- Higher fidelity to source images

### Example Usage
```python
result = fal_client.subscribe(
    "fal-ai/flux-pro/kontext",
    arguments={
        "prompt": "Transform into professional executive headshot with modern office background",
        "image_url": image_url,
        "guidance_scale": 3.5,
        "num_inference_steps": 28,
    }
)
```

## Estimated Costs

Based on fal.ai pricing:
- **GPT-Image 1.5 Edit**: ~$0.10-0.20 per image
- **FLUX Pro Kontext**: ~$0.30-0.50 per image
- **Total for 12 images**: $1.20-$6.00 depending on model

## Troubleshooting

### 401 Unauthorized Error
- Your API key is invalid or expired
- Get the correct key from 1Password: "FAL API Key" (yfmv5bml45cw5jv5yf4dstk3py)
- Ensure you set `FAL_KEY` environment variable, not `FAL_API_KEY`

### Upload Errors
- Ensure source image files exist
- Check file permissions
- Verify image files are not corrupted

### Poor Quality Results
- Increase `num_inference_steps` to 75-100
- Adjust `guidance_scale` (lower = more creative, higher = more literal)
- Try alternative prompts focusing on specific aspects
- Consider using FLUX Pro Kontext for better fidelity

## Documentation References

- [fal.ai GPT-Image 1.5 Edit API](https://fal.ai/models/fal-ai/gpt-image-1.5/edit/api)
- [fal.ai FLUX Pro Kontext](https://fal.ai/models/fal-ai/flux-pro/kontext)
- [fal.ai Client Documentation](https://docs.fal.ai/model-apis/client)
- [GPT Image 1.5 Prompt Guide](https://fal.ai/learn/devs/gpt-image-1-5-prompt-guide)

## Script Location

The enhancement script is located at:
```
/mnt/d/workspace/ISNBIZ_Files/scripts/enhance_founder_photos_gpt15.py
```

## Next Steps

1. Get the correct API key from 1Password
2. Set the `FAL_KEY` environment variable
3. Run the enhancement script
4. Review the 12 generated images
5. Select the best variant for each founder
6. Use in HROC website and marketing materials

---

**CRITICAL REMINDER**: The script uses REAL founder photos as the base - it does NOT generate random people. The output will be enhanced versions of the actual founders, maintaining their appearance while improving professional quality.
