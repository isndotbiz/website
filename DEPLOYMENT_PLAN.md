# ISN.BIZ Complete Deployment Plan

## What's Being Created

### Pages (17 total)
**Main Site:**
- index.html ✅ (enhanced)
- about.html
- services.html  
- portfolio.html
- investors.html
- contact.html

**Founder Pages (4):**
- bri.html ✅ (Bri - Secretary/COO)
- lilly.html ✅ (Lilly - Treasurer/CFO)
- jonathan.html ✅ (Jonathan - Chairman/CEO)
- alicia.html ✅ (Alicia - VP/CPO)

**Project Deep-Dives (8):**
- truenas-infrastructure.html (TrueNAS AI/ML Platform)
- videogen-youtube.html (Video Production Pipeline)
- bin-intelligence.html (Fraud Detection Platform)
- cli.html (CLI Engineering Standards)
- comfyui-flux.html (AI Image Generation)
- ged.html (GEDCOM Processing Platform)
- llm-optimization.html (LLM Research Framework)
- opportunity-bot.html (Business Discovery Bot)
- spirit-atlas.html (Privacy-First Mobile App)

### Images Being Generated

**Founder Photos (16 total):**
- 4 per founder in different professional situations
- NOT looking at camera (candid style)
- Source: D:\workspace\ISNBIZ_Files\1\*.png
- Using FAL Edit API

**Project Images (40-50 total):**
- 4-6 images per project
- Technical, professional visualizations
- Using FAL gpt-image-1.5 (low quality for speed)

All converted to WebP, uploaded to S3, served via TrueNAS

### Design Fixes
- ❌ Remove "$1500/mo savings" mentions
- ✅ Fix symmetry (5 cards, perfect alignment)
- ✅ Fix text contrast (WCAG 4.5:1 minimum)
- ✅ More founder spacing
- ✅ Smaller founder images

## S3 Structure
```
isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com/
├── premium_v3/
│   ├── founders/
│   │   ├── bri_office.webp
│   │   ├── bri_meeting.webp
│   │   ├── bri_presentation.webp
│   │   ├── bri_strategy.webp
│   │   ├── (same pattern for lilly, jonathan, alicia)
│   └── projects/
│       ├── truenas_dashboard.webp
│       ├── truenas_infrastructure.webp
│       ├── videogen_pipeline.webp
│       ├── (etc...)
```

## Deployment Sequence
1. ✅ Design fixes applied
2. ✅ Pages created
3. ⏳ Images generated
4. ⏳ Convert to WebP
5. ⏳ Upload to S3
6. ⏳ Deploy to TrueNAS (10.0.0.89)
7. ⏳ Test all pages on https://isn.biz

