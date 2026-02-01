# AI Asset Generation Quick Start Guide
**isn.biz Website Assets - Ready-to-Use Prompts**
**Created:** 2026-02-01

---

## 🚀 Quick Setup

### 1. API Keys Needed

```bash
# fal.ai (Flux 2 Pro, Recraft V3)
export FAL_KEY="your_fal_api_key"

# OpenAI (GPT Image 1.5)
export OPENAI_API_KEY="your_openai_api_key"
```

Get API keys:
- **fal.ai:** https://fal.ai/ (sign up free, pay-per-use)
- **OpenAI:** https://platform.openai.com/ (sign up, add payment method)

### 2. Install Dependencies

```bash
pip install fal-client openai requests pillow
```

---

## 📋 Ready-to-Use Prompts by Asset Type

### Hero Section Backgrounds (Use Flux 2 Pro)

**Service:** fal.ai/flux-2-pro
**Resolution:** 2560x1440
**Cost:** ~$0.05 each

#### 1. Digital Network Background
```
PROMPT:
Ultra-modern abstract digital network background, flowing data streams and glowing nodes,
bright blue #1E9FF2 and cyan #5FDFDF on dark charcoal #3F4447 background,
futuristic technology aesthetic, clean professional design, high resolution 2560x1440,
cinematic lighting, depth of field, photorealistic render, trending on artstation

NEGATIVE:
cluttered, busy, text, logos, people, faces, amateur, low quality, watermark
```

#### 2. Abstract Geometric Background
```
PROMPT:
Minimalist geometric abstract background, floating 3D shapes and polygons,
gradient from bright blue #1E9FF2 to cyan #5FDFDF, dark charcoal #3F4447 accents,
modern tech aesthetic, clean composition, professional corporate design,
2560x1440 resolution, studio lighting, sharp focus, ultra detailed

NEGATIVE:
cluttered, messy, chaotic, text, watermarks, low resolution, busy
```

#### 3. Data Visualization Background
```
PROMPT:
Sleek data visualization abstract background, glowing charts and graphs elements,
circuit board patterns, color scheme of electric blue #1E9FF2 and vibrant cyan #5FDFDF
on charcoal #3F4447 base, futuristic dashboard aesthetic, professional tech design,
2560x1440 high resolution, cinematic composition, photorealistic 3D render

NEGATIVE:
messy, cluttered, amateur, cartoonish, low quality, text, people
```

#### 4. Metallic Tech Background
```
PROMPT:
Premium metallic technology background, brushed metal texture with blue #1E9FF2
and cyan #5FDFDF lighting effects, dark charcoal #3F4447 base, abstract tech patterns,
sophisticated modern design, enterprise-grade aesthetic, 2560x1440 resolution,
professional studio lighting, ultra sharp, photorealistic

NEGATIVE:
rusty, old, vintage, cluttered, low quality, amateur, busy
```

#### 5. Particle Flow Background
```
PROMPT:
Dynamic particle flow abstract background, glowing particles in motion,
energy streams in bright blue #1E9FF2 and cyan #5FDFDF colors,
dark charcoal #3F4447 background, cutting-edge technology aesthetic,
clean modern composition, 2560x1440 high resolution, volumetric lighting,
photorealistic render, professional grade

NEGATIVE:
static, boring, cluttered, messy, text, low resolution, amateur
```

---

### Service Icons (Use Recraft V3)

**Service:** fal.ai/recraft/v3
**Resolution:** 512x512 SVG
**Cost:** ~$0.04 each

#### 1. Custom Development Icon
```
PROMPT:
Modern icon for custom software development, code brackets with gear symbol,
bright blue #1E9FF2 and cyan #5FDFDF gradient, flat vector design,
clean professional tech icon style, simple geometric shapes,
512x512, transparent background, scalable vector graphic, minimalist

NEGATIVE:
3D, realistic, photographic, cluttered, complex, busy, detailed texture
```

#### 2. AI/ML Icon
```
PROMPT:
Sleek AI machine learning icon, neural network nodes connected with lines,
blue #1E9FF2 to cyan #5FDFDF gradient, modern flat icon design,
professional tech icon style, simple clean geometric shapes,
512x512, transparent background, vector illustration, minimalist

NEGATIVE:
3D, photorealistic, complex, cluttered, messy, detailed, textured
```

#### 3. Cloud Architecture Icon
```
PROMPT:
Modern cloud computing icon, stylized cloud with server nodes inside,
bright blue #1E9FF2 and cyan #5FDFDF colors, flat design with subtle depth,
professional tech icon, 512x512, transparent background,
clean minimalist style, crisp vector illustration, simple shapes

NEGATIVE:
realistic, 3D, cluttered, outdated, low quality, complex, busy
```

#### 4. Data Engineering Icon
```
PROMPT:
Professional data engineering icon, database cylinders with data flow arrows,
blue #1E9FF2 and cyan #5FDFDF gradient, modern flat icon design,
clean tech aesthetic, 512x512, transparent background,
geometric precision, high quality vector style, simple minimalist

NEGATIVE:
3D, photorealistic, messy, amateur, low quality, complex, detailed
```

#### 5. Security Icon
```
PROMPT:
Modern cybersecurity icon, shield with lock symbol and circuit elements,
bright blue #1E9FF2 to cyan #5FDFDF gradient, flat design with subtle depth,
professional security icon style, 512x512, transparent background,
clean geometric design, vector illustration quality, minimalist

NEGATIVE:
3D, realistic, cluttered, outdated, low quality, complex, busy
```

#### 6. Mobile Development Icon
```
PROMPT:
Sleek mobile development icon, smartphone outline with code brackets inside,
blue #1E9FF2 and cyan #5FDFDF colors, modern flat icon design,
professional tech style, 512x512, transparent background,
clean minimalist aesthetic, crisp vector style illustration, simple

NEGATIVE:
3D, photorealistic, messy, amateur, low quality, blurry, complex
```

---

### Portfolio Mockups (Use Flux 2 Pro)

**Service:** fal.ai/flux-2-pro
**Resolution:** 1920x1080
**Cost:** ~$0.05 each

#### 1. AI Chatbot Dashboard
```
PROMPT:
Modern AI chatbot dashboard interface mockup, dark theme UI with blue #1E9FF2
and cyan #5FDFDF accent colors, conversation threads panel on left,
analytics graphs on right, clean professional design, realistic software interface,
high detail, flat design with subtle depth, 1920x1080 resolution,
professional UI/UX design, contemporary SaaS aesthetic

NEGATIVE:
cluttered, amateur, outdated, low quality, blurry, messy, cartoon
```

#### 2. Mobile App Profile Screen
```
PROMPT:
Premium mobile app interface mockup on iPhone 15 Pro, wellness app profile screen,
user stats and progress circles, blue #1E9FF2 and cyan #5FDFDF color scheme,
modern iOS design, clean minimalist UI, realistic phone mockup with shadow,
professional app design, 1920x1080 resolution, studio lighting on device

NEGATIVE:
cluttered, amateur, outdated phone model, low quality, messy, busy
```

#### 3. Analytics Dashboard
```
PROMPT:
Professional analytics dashboard interface, modern data visualization with charts,
bar graphs and line charts in blue #1E9FF2 and cyan #5FDFDF colors,
dark theme with charcoal #3F4447 background, clean grid layout,
enterprise-grade UI design, 1920x1080 resolution, high detail,
realistic software interface, contemporary dashboard design

NEGATIVE:
cluttered, messy, amateur, outdated, low quality, busy, confusing
```

#### 4. Cloud Architecture Diagram
```
PROMPT:
Modern cloud architecture diagram visualization, AWS style infrastructure,
isometric 3D elements showing servers and connections, blue #1E9FF2 and cyan #5FDFDF,
clean professional infographic style, dark charcoal #3F4447 background,
technical but accessible, 1920x1080 resolution, high quality technical illustration

NEGATIVE:
cluttered, messy, confusing, amateur, low quality, too complex, busy
```

---

### Team/About Page Visuals (Use Flux 2 Pro)

**Service:** fal.ai/flux-2-pro
**Resolution:** 1920x1080
**Cost:** ~$0.05 each

#### 1. Team Collaboration Scene
```
PROMPT:
Modern coworking space with diverse team collaborating around laptop,
bright and energetic atmosphere, contemporary interior design with plants and natural light,
wide angle shot capturing the full environment, warm color palette with blue accents,
lifestyle photography style, natural window lighting from left,
professional corporate imagery, authentic expressions, 1920x1080 resolution

NEGATIVE:
staged, unnatural, harsh lighting, amateur, formal suits, stiff poses, flash
```

#### 2. Casual Team Meeting
```
PROMPT:
Diverse team in casual meeting, standing around whiteboard with ideas,
bright modern office with large windows, natural daylight, collaborative atmosphere,
contemporary workspace design, warm inviting colors with tech aesthetic,
candid professional photography, authentic engagement, wide shot,
1920x1080 resolution, lifestyle business photography style

NEGATIVE:
formal, staged, harsh lighting, outdated office, stiff, unnatural, dark
```

#### 3. Individual Working Scene
```
PROMPT:
Professional developer working on laptop in modern office space,
focused and engaged, natural window light from side, contemporary workspace,
plants and tech aesthetic, warm atmosphere with blue accent lighting,
lifestyle professional photography, authentic work scene, medium shot,
1920x1080 resolution, shallow depth of field, professional grade

NEGATIVE:
staged, studio backdrop, harsh flash, formal suit, stiff pose, amateur
```

---

### Service Illustrations (Use Flux 2 Pro)

**Service:** fal.ai/flux-2-pro
**Resolution:** 1024x1024
**Cost:** ~$0.05 each

#### 1. Custom Development Illustration
```
PROMPT:
Modern abstract illustration of custom software development concept,
floating code elements and geometric shapes, bright blue #1E9FF2 and cyan #5FDFDF gradient,
professional tech illustration, clean minimalist design, conceptual digital art,
high resolution 1024x1024, transparent background style, vector-style clean edges,
contemporary tech aesthetic

NEGATIVE:
cluttered, realistic photo, photographic, busy, low quality, amateur, messy
```

#### 2. AI/ML Illustration
```
PROMPT:
Sleek AI machine learning illustration, neural network visualization with flowing data,
connected nodes and pathways, blue #1E9FF2 to cyan #5FDFDF gradient,
modern tech illustration, clean professional design, futuristic aesthetic,
1024x1024 high resolution, conceptual tech art style, minimalist composition

NEGATIVE:
cartoonish, cluttered, messy, amateur, low quality, photorealistic, busy
```

#### 3. Cloud Architecture Illustration
```
PROMPT:
Modern cloud computing illustration, abstract cloud with server infrastructure,
geometric shapes representing data flow, bright blue #1E9FF2 and cyan #5FDFDF,
professional tech illustration, clean contemporary design, technical but accessible,
1024x1024 resolution, minimalist style, vector-style edges, conceptual art

NEGATIVE:
cluttered, photorealistic, messy, amateur, low quality, busy, complex
```

---

### Abstract Section Backgrounds (Use Flux 2 Pro)

**Service:** fal.ai/flux-2-pro
**Resolution:** 1920x1080
**Cost:** ~$0.03 each

#### 1. Subtle Geometric Pattern
```
PROMPT:
Subtle abstract geometric pattern background, overlapping transparent shapes,
blue #1E9FF2 and cyan #5FDFDF with dark charcoal #3F4447 base,
minimal clean design, very subtle depth, professional corporate aesthetic,
1920x1080 resolution, soft lighting, non-distracting background pattern

NEGATIVE:
busy, cluttered, harsh, distracting, amateur, overwhelming, loud
```

#### 2. Minimal Circuit Pattern
```
PROMPT:
Minimal circuit board pattern background, very subtle tech lines and connection points,
blue #1E9FF2 and cyan #5FDFDF faint glowing accents on charcoal #3F4447,
professional subtle background design, clean modern aesthetic, 1920x1080 resolution,
non-distracting pattern, soft glow effects, understated tech theme

NEGATIVE:
cluttered, busy, messy, harsh, overwhelming, distracting, amateur
```

---

### Infographics (Use GPT Image 1.5)

**Service:** OpenAI GPT Image 1.5
**Resolution:** 1920x1080
**Cost:** ~$0.10 each

#### 1. Development Process Infographic
```
PROMPT:
Professional infographic showing 5-stage software development process,
clean horizontal timeline with numbered steps 1 through 5,
modern icons for each stage: Discovery, Design, Development, Testing, Deployment,
blue #1E9FF2 and cyan #5FDFDF color scheme on dark charcoal #3F4447 background,
arrows connecting stages, large clear text labels, professional typography,
1920x1080 resolution, clean modern infographic design, high contrast for readability

NEGATIVE:
cluttered, messy, hard to read, amateur, confusing layout, too much text, busy
```

#### 2. Key Statistics Infographic
```
PROMPT:
Modern statistics infographic with 4 key metrics displayed prominently,
large bold numbers in bright blue #1E9FF2, supporting text in white,
icons for each statistic in cyan #5FDFDF, dark charcoal #3F4447 background,
clean grid layout, professional presentation style, high contrast,
1920x1080 resolution, corporate infographic design, easy to read

Example stats: "500+ Projects", "15 Years", "50+ Clients", "99% Satisfaction"

NEGATIVE:
cluttered, busy, hard to read, amateur, low contrast, confusing, messy
```

---

## 🎯 Generation Workflow

### Step 1: Generate Hero Backgrounds

```python
import fal_client

# Generate hero background
result = fal_client.subscribe(
    "fal-ai/flux-2-pro",
    arguments={
        "prompt": "Ultra-modern abstract digital network background...",
        "negative_prompt": "cluttered, busy, text, logos...",
        "image_size": {
            "width": 2560,
            "height": 1440
        },
        "num_inference_steps": 28,
        "guidance_scale": 3.5,
        "num_images": 1
    }
)

# Download image
import requests
img_url = result["images"][0]["url"]
img_data = requests.get(img_url).content
with open("hero-bg-network.png", "wb") as f:
    f.write(img_data)

print(f"Generated: hero-bg-network.png")
```

### Step 2: Generate Service Icons (SVG)

```python
# Generate vector icon
result = fal_client.subscribe(
    "fal-ai/recraft/v3/text-to-image",
    arguments={
        "prompt": "Modern icon for custom software development...",
        "style": "digital_illustration",
        "size": "square_hd"
    }
)

# Download SVG
img_url = result["images"][0]["url"]
img_data = requests.get(img_url).content
with open("icon-custom-dev.svg", "wb") as f:
    f.write(img_data)

print(f"Generated: icon-custom-dev.svg")
```

### Step 3: Generate Infographics (GPT Image 1.5)

```python
from openai import OpenAI

client = OpenAI()

response = client.images.generate(
    model="gpt-image-1.5",
    prompt="Professional infographic showing 5-stage software development...",
    size="1920x1080",
    quality="high",
    n=1
)

# Download image
import requests
img_url = response.data[0].url
img_data = requests.get(img_url).content
with open("infographic-process.png", "wb") as f:
    f.write(img_data)

print(f"Generated: infographic-process.png")
```

---

## 📦 Complete Generation Script

```python
#!/usr/bin/env python3
"""
Complete isn.biz Asset Generation
Generates all required assets with optimal services
"""

import fal_client
from openai import OpenAI
import requests
import os

# Brand colors
COLORS = {
    "blue": "#1E9FF2",
    "cyan": "#5FDFDF",
    "charcoal": "#3F4447"
}

def save_image(url, filename):
    """Download and save image from URL"""
    img_data = requests.get(url).content
    os.makedirs(os.path.dirname(filename) or ".", exist_ok=True)
    with open(filename, "wb") as f:
        f.write(img_data)
    print(f"✅ Saved: {filename}")

def generate_flux2_hero(prompt, negative, filename):
    """Generate hero background with Flux 2 Pro"""
    result = fal_client.subscribe(
        "fal-ai/flux-2-pro",
        arguments={
            "prompt": prompt,
            "negative_prompt": negative,
            "image_size": {"width": 2560, "height": 1440},
            "num_inference_steps": 28,
            "guidance_scale": 3.5
        }
    )
    save_image(result["images"][0]["url"], filename)

def generate_recraft_icon(prompt, filename):
    """Generate icon with Recraft V3"""
    result = fal_client.subscribe(
        "fal-ai/recraft/v3/text-to-image",
        arguments={
            "prompt": prompt,
            "style": "digital_illustration",
            "size": "square_hd"
        }
    )
    save_image(result["images"][0]["url"], filename)

def main():
    print("🚀 Generating isn.biz website assets...\n")

    # 1. Hero Backgrounds
    print("1️⃣ Generating Hero Backgrounds (Flux 2 Pro)...")
    hero_prompts = [
        {
            "name": "network",
            "prompt": f"Ultra-modern abstract digital network background, flowing data streams and glowing nodes, bright blue {COLORS['blue']} and cyan {COLORS['cyan']} on dark charcoal {COLORS['charcoal']} background, futuristic technology aesthetic, clean professional design, 2560x1440 resolution, cinematic lighting, depth of field, photorealistic render",
            "negative": "cluttered, busy, text, logos, people, faces, amateur, low quality"
        },
        {
            "name": "geometric",
            "prompt": f"Minimalist geometric abstract background, floating 3D shapes and polygons, gradient from bright blue {COLORS['blue']} to cyan {COLORS['cyan']}, dark charcoal {COLORS['charcoal']} accents, modern tech aesthetic, clean composition, 2560x1440 resolution, studio lighting, ultra detailed",
            "negative": "cluttered, messy, chaotic, text, watermarks, low resolution"
        }
    ]

    for hero in hero_prompts:
        generate_flux2_hero(
            hero["prompt"],
            hero["negative"],
            f"assets/hero-bg-{hero['name']}.png"
        )

    # 2. Service Icons
    print("\n2️⃣ Generating Service Icons (Recraft V3)...")
    icon_prompts = [
        {
            "name": "custom-dev",
            "prompt": f"Modern icon for custom software development, code brackets with gear symbol, bright blue {COLORS['blue']} and cyan {COLORS['cyan']} gradient, flat vector design, clean professional tech icon, 512x512, transparent background, minimalist"
        },
        {
            "name": "ai-ml",
            "prompt": f"Sleek AI machine learning icon, neural network nodes connected, blue {COLORS['blue']} to cyan {COLORS['cyan']} gradient, modern flat icon design, 512x512, transparent background, minimalist"
        }
    ]

    for icon in icon_prompts:
        generate_recraft_icon(
            icon["prompt"],
            f"assets/icons/icon-{icon['name']}.svg"
        )

    print("\n✅ Asset generation complete!")
    print("\n📊 Summary:")
    print("  - Hero backgrounds: 2")
    print("  - Service icons: 2")
    print("  - Estimated cost: $0.20-0.30")

if __name__ == "__main__":
    main()
```

---

## 🎨 Post-Processing Checklist

After generation:

1. **Verify colors:**
   - [ ] Use color picker to verify hex codes
   - [ ] Check brand consistency

2. **Optimize files:**
   ```bash
   # Convert to WebP
   cwebp -q 85 hero-bg-network.png -o hero-bg-network.webp

   # Optimize PNG
   optipng -o7 hero-bg-network.png
   ```

3. **Create responsive versions:**
   ```bash
   # Generate @2x version
   convert hero-bg-network.png -resize 5120x2880 hero-bg-network@2x.png

   # Generate mobile version
   convert hero-bg-network.png -resize 1280x720 hero-bg-network-mobile.png
   ```

4. **Test assets:**
   - [ ] View on actual website
   - [ ] Test on mobile devices
   - [ ] Verify file sizes (<500KB)
   - [ ] Check loading performance

---

## 💰 Cost Calculator

| Asset Type | Quantity | Cost Each | Total |
|------------|----------|-----------|-------|
| Hero backgrounds | 5 | $0.05 | $0.25 |
| Service icons | 6 | $0.04 | $0.24 |
| Portfolio mockups | 8 | $0.05 | $0.40 |
| Team visuals | 4 | $0.05 | $0.20 |
| Service illustrations | 6 | $0.05 | $0.30 |
| Abstract backgrounds | 8 | $0.03 | $0.24 |
| Infographics | 3 | $0.10 | $0.30 |
| **TOTAL** | **40** | - | **$1.93** |

**With iterations (3x):** ~$6.00
**With buffer:** ~$10.00

---

## 🆘 Quick Troubleshooting

**Problem:** Colors don't match brand
- Use exact hex codes in prompts
- Try Flux 2 Pro for best color accuracy
- Post-process to adjust if needed

**Problem:** Output quality is poor
- Add quality keywords: "professional, ultra detailed"
- Increase resolution in prompt
- Use higher-tier service (Flux 2 Pro)

**Problem:** Text is illegible
- Switch to GPT Image 1.5 for text-heavy images
- Specify text explicitly in prompt
- Increase font size in prompt

**Problem:** Style is inconsistent
- Use same service for similar assets
- Reuse successful prompt templates
- Generate in same session

---

## 📞 Support Resources

**API Issues:**
- fal.ai: https://fal.ai/docs
- OpenAI: https://platform.openai.com/docs

**Community:**
- fal.ai Discord: https://discord.gg/fal-ai
- Reddit: r/StableDiffusion, r/aiArt

**Additional Guides:**
- Full research: `AI_IMAGE_GENERATION_RESEARCH_2026.md`
- Original guide: `AI_ASSET_GENERATION_GUIDE.md`

---

**Ready to generate! Start with the hero backgrounds and iterate from there.**

🎉 **Pro Tip:** Generate 2-3 variations of each asset first, then select the best ones before moving to the next asset type.
