# fal.ai Model Comparison for HROC Founder Photo Enhancement

## Overview
This document compares different fal.ai models and approaches for enhancing the HROC founder photos into professional corporate headshots.

## Available Scripts

| Script | Model | Method | Best For |
|--------|-------|--------|----------|
| `enhance_founder_photos_gpt15.py` | GPT-Image 1.5 Edit | Upload + Edit | Highest quality, creative enhancements |
| `enhance_founder_photos_base64.py` | GPT-Image 1.5 Edit | Base64 Data URI | Same as above, bypasses upload issues |
| `enhance_founder_photos_headshot.py` | Headshot Generator | Specialized headshot | Quick professional headshots |

## Model Comparison

### 1. GPT-Image 1.5 Edit
**Endpoint**: `fal-ai/gpt-image-1.5/edit`

#### Strengths
- State-of-the-art image generation quality
- Excellent at understanding complex prompts
- Maintains good fidelity to source image
- Highly customizable with parameters
- Can make subtle or dramatic changes

#### Parameters
```python
{
    "image_url": "<source-image>",
    "prompt": "<detailed-enhancement-prompt>",
    "image_size": "portrait_4_3",
    "num_inference_steps": 50,        # Higher = better quality
    "guidance_scale": 7.5,             # Balance: 5-10 typical
    "input_fidelity": 0.7,             # How much to preserve source
    "num_images": 1,
    "enable_safety_checker": True,
    "output_format": "png"
}
```

#### Best Use Cases
- When you need maximum control over the output
- When you want to specify detailed enhancement instructions
- For creating multiple style variations
- When quality is more important than speed

#### Estimated Cost
- **~$0.10-0.20 per image**
- Total for 12 images: **$1.20-$2.40**

#### Example Prompts
```
"Professional executive headshot with warm smile, modern office
background with soft natural lighting, high-quality corporate
photography, business professional attire"

"Professional portrait in business casual attire, confident
approachable expression, contemporary workspace setting, natural
window lighting, professional photographer quality"
```

---

### 2. Headshot Generator
**Endpoint**: `fal-ai/image-apps-v2/headshot-photo`

#### Strengths
- Specialized for headshot generation
- Simpler API (fewer parameters)
- Faster processing
- Optimized for professional portraits
- Good default settings

#### Parameters
```python
{
    "image_url": "<source-image>",
    "background": "modern office" | "professional studio" | "contemporary workspace",
    "output_format": "png"
}
```

#### Best Use Cases
- Quick professional headshot generation
- When you trust the model's default enhancements
- Simpler workflow with fewer decisions
- Standard corporate photography style

#### Estimated Cost
- **~$0.10-0.15 per image**
- Total for 12 images: **$1.20-$1.80**

---

### 3. FLUX Pro 1.1 Kontext
**Endpoint**: `fal-ai/flux-pro/kontext`

#### Strengths
- 12-billion parameter model
- Excellent at preserving character consistency
- High fidelity to source images
- Multimodal understanding
- Professional-grade results

#### Parameters
```python
{
    "image_url": "<source-image>",
    "prompt": "<transformation-description>",
    "guidance_scale": 3.5,
    "num_inference_steps": 28,
    "num_images": 1
}
```

#### Best Use Cases
- Maximum fidelity to original person
- When character consistency is critical
- High-end professional photography
- When budget allows for premium quality

#### Estimated Cost
- **~$0.30-0.50 per image**
- Total for 12 images: **$3.60-$6.00**

---

### 4. Face Enhancement
**Endpoint**: `fal-ai/image-editing/face-enhancement`

#### Strengths
- Focused on facial features
- Natural-looking retouching
- Maintains realistic appearance
- Quick processing
- Good for subtle improvements

#### Best Use Cases
- Enhancing existing good photos
- Subtle retouching (skin, eyes, etc.)
- When photos just need polish
- Maintaining very high authenticity

---

### 5. Crystal Upscaler (Clarity AI)
**Endpoint**: `clarityai/crystal-upscaler`

#### Strengths
- Specialized for portrait upscaling
- Excellent facial detail preservation
- Professional headshot restoration
- High-resolution output
- Social media optimization

#### Parameters
```python
{
    "image_url": "<source-image>",
    "scale": 2,  # Upscaling factor
}
```

#### Best Use Cases
- Upscaling lower resolution photos
- Restoring facial details
- Creating high-res versions
- Combining with other enhancements

#### Estimated Cost
- **$0.016 per megapixel**
- Typical cost: **$0.05-0.20 per image**

---

## Recommended Approach

### Option A: Maximum Quality (Recommended)
1. **GPT-Image 1.5 Edit** for creative professional enhancements
   - Use detailed prompts for each variant
   - Generate 3 variants per founder
   - Cost: ~$2.40 for 12 images

2. **Optional**: Follow up with Crystal Upscaler if higher resolution needed

### Option B: Budget-Conscious
1. **Headshot Generator** for quick professional results
   - Simpler, faster, cheaper
   - Still professional quality
   - Cost: ~$1.50 for 12 images

### Option C: Premium Quality
1. **FLUX Pro 1.1 Kontext** for maximum fidelity
   - Best character consistency
   - Professional-grade results
   - Cost: ~$5.00 for 12 images

2. **Optional**: Crystal Upscaler for final touch

### Option D: Multi-Stage Enhancement
1. **Face Enhancement** for initial polish (~$0.05/image)
2. **Headshot Generator** for background/composition (~$0.15/image)
3. **Crystal Upscaler** for final high-res output (~$0.10/image)
4. Total: ~$3.60 for 12 images

---

## Technical Considerations

### Image Upload Methods

#### Method 1: File Upload
```python
image_url = fal_client.upload_file(str(image_path))
```
- **Pros**: Clean, standard approach
- **Cons**: Requires valid API key, can fail with auth issues

#### Method 2: Base64 Data URI
```python
with open(image_path, 'rb') as f:
    data = base64.b64encode(f.read()).decode()
    image_url = f"data:image/webp;base64,{data}"
```
- **Pros**: No upload required, works around auth issues
- **Cons**: Larger payload, slower for very large images

#### Method 3: Public URL
```python
image_url = "https://your-server.com/founder-photo.webp"
```
- **Pros**: No upload needed, efficient
- **Cons**: Requires hosting images publicly

---

## Parameter Tuning Guide

### For GPT-Image 1.5 Edit

#### `num_inference_steps`
- **25-30**: Fast, lower quality
- **50**: Balanced (recommended)
- **75-100**: Slower, highest quality

#### `guidance_scale`
- **3-5**: More creative, less literal
- **7-8**: Balanced (recommended)
- **10-15**: Very literal, follows prompt strictly

#### `input_fidelity`
- **0.5**: More creative freedom
- **0.7**: Balanced (recommended)
- **0.9**: Maximum preservation of source

---

## Prompt Engineering Tips

### Effective Headshot Enhancement Prompts

#### Structure
```
[Shot Type] + [Expression] + [Setting/Background] + [Lighting] + [Quality/Style]
```

#### Examples

**Conservative/Professional**
```
Professional executive headshot, warm smile, modern office background,
soft natural lighting, high-quality corporate photography
```

**Approachable/Friendly**
```
Professional portrait, friendly confident expression, contemporary
workspace, natural window lighting, corporate casual style
```

**Creative/Editorial**
```
Magazine-quality portrait, engaging professional demeanor, clean
minimalist setting, studio lighting, editorial photography style
```

### Keywords That Work Well
- **Expression**: warm smile, confident, approachable, professional, friendly
- **Lighting**: natural lighting, soft lighting, studio lighting, window light
- **Background**: modern office, contemporary workspace, professional studio, clean background
- **Quality**: high-quality, professional photography, corporate photography, executive portrait

### Keywords to Avoid
- "AI-generated" (defeats the purpose)
- "perfect" (can look unrealistic)
- Specific brand names
- Overly technical photography terms

---

## Quality Assurance Checklist

After generation, verify each image:

- [ ] Face/identity clearly recognizable as the founder
- [ ] Professional business attire (or appropriate casual)
- [ ] Natural-looking lighting and skin tones
- [ ] Clean, appropriate background
- [ ] High resolution and sharp details
- [ ] No AI artifacts or distortions
- [ ] Appropriate facial expression (friendly, professional)
- [ ] Good composition and framing
- [ ] Suitable for corporate website use
- [ ] Maintains authenticity (doesn't look overly processed)

---

## Troubleshooting

### Issue: 401 Unauthorized
**Solution**: Get correct API key from 1Password "FAL API Key" item

### Issue: Poor Quality Results
**Solutions**:
1. Increase `num_inference_steps` to 75-100
2. Adjust `guidance_scale` (try 8-10)
3. Refine prompt with more specific details
4. Try different model (FLUX Kontext for better fidelity)

### Issue: Person Doesn't Look Like Founder
**Solutions**:
1. Increase `input_fidelity` to 0.8-0.9
2. Use more conservative prompt
3. Try Headshot Generator (simpler, better preservation)
4. Use FLUX Kontext (better character consistency)

### Issue: Unrealistic/AI-Looking
**Solutions**:
1. Reduce `guidance_scale` to 5-6
2. Use more natural prompt language
3. Increase `input_fidelity`
4. Try Face Enhancement instead (more subtle)

---

## Execution Instructions

### Step 1: Get API Key
```bash
# Get from 1Password: "FAL API Key" (yfmv5bml45cw5jv5yf4dstk3py)
export FAL_KEY="your-actual-api-key"
```

### Step 2: Choose Your Script

#### Option A: GPT-Image 1.5 (Recommended)
```bash
python3 /mnt/d/workspace/ISNBIZ_Files/scripts/enhance_founder_photos_base64.py
```

#### Option B: Headshot Generator
```bash
python3 /mnt/d/workspace/ISNBIZ_Files/scripts/enhance_founder_photos_headshot.py
```

### Step 3: Review Results
```bash
ls -lh /mnt/d/workspace/ISNBIZ_Files/assets/team/
```

### Step 4: Select Best Variants
- Review all 3 variants per founder
- Choose the most professional and realistic
- Use for HROC website and marketing

---

## Expected Output

### File Structure
```
/mnt/d/workspace/ISNBIZ_Files/assets/team/
├── alicia_enhanced_01.png    (GPT-Image 1.5)
├── alicia_enhanced_02.png
├── alicia_enhanced_03.png
├── alicia_headshot_01.png    (Headshot Generator)
├── alicia_headshot_02.png
├── alicia_headshot_03.png
├── bri_enhanced_01.png
├── ... (same pattern for Bri, Jonathan, Lilly)
```

### File Specifications
- **Format**: PNG (lossless, high quality)
- **Aspect Ratio**: 4:3 portrait
- **Size**: 2-5 MB per image (high resolution)
- **Quality**: Professional corporate photography standard

---

## Cost Summary

| Model | Cost/Image | Total (12 images) | Quality | Speed |
|-------|------------|-------------------|---------|-------|
| GPT-Image 1.5 | $0.15 | $1.80 | Excellent | Medium |
| Headshot Generator | $0.12 | $1.44 | Very Good | Fast |
| FLUX Pro Kontext | $0.40 | $4.80 | Excellent+ | Slow |
| Face Enhancement | $0.05 | $0.60 | Good | Fast |
| Crystal Upscaler | $0.08 | $0.96 | N/A (upscale) | Fast |

---

## References

- [GPT-Image 1.5 Edit API](https://fal.ai/models/fal-ai/gpt-image-1.5/edit/api)
- [Headshot Generator](https://fal.ai/models/fal-ai/image-apps-v2/headshot-photo)
- [FLUX Pro Kontext](https://fal.ai/models/fal-ai/flux-pro/kontext)
- [Face Enhancement](https://fal.ai/models/fal-ai/image-editing/face-enhancement)
- [Crystal Upscaler](https://fal.ai/models/clarityai/crystal-upscaler)
- [fal.ai Client Documentation](https://docs.fal.ai/model-apis/client)
- [GPT Image 1.5 Prompt Guide](https://fal.ai/learn/devs/gpt-image-1-5-prompt-guide)
- [Creating LinkedIn Headshots with Flux](https://dev.to/derekdillman/creating-the-perfect-linkedin-headshot-using-ai-with-flux-lora-and-falai-1lc1)

---

**Last Updated**: 2026-02-01
