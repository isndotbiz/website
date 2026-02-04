# CODEX CLI 5.2 HANDOFF - 2026-02-04

## CRITICAL FAL.AI SETTINGS

**ONLY USE:**
- `fal-ai/gpt-image-1.5` (generation)
- `fal-ai/gpt-image-1.5/edit` (editing)

**ALWAYS SET:** `quality: "low"` or `image_quality: "low"`

**WHY:** "low" is INVERTED - it's actually the BEST, FASTEST, CHEAPEST option. Previous session burned all credits using "high".

## CURRENT STATE

**WORKING:**
- Theme & design (Neo-Technical Brutalism)
- All CSS/JS
- Site live at https://isn.biz
- S3 CDN: isnbiz-assets-1769962280

**MISSING:**
- Some project images for 9 projects
- Proper founder photos for 4 founders
- Card grid symmetry (needs 3 or 4 per row)

## THE 9 PROJECTS

1. TrueNAS Infrastructure
2. VideoGen YouTube
3. BIN Intelligence
4. SpiritAtlas
5. ComfyUI Automation
6. GEDCOM Processing
7. LLM Optimization
8. Opportunity Bot
9. CLI Tools (may need creation)

## THE 4 FOUNDERS

1. Alicia (VP & CPO)
2. Bri
3. Jonathan (Chairman & CEO)
4. Lilly

## DESIGN RULES

- Cards: ALWAYS 3 or 4 per row
- Everything: CENTERED
- Images: On S3 only (not TrueNAS)
- Pages: On TrueNAS only

## DEPLOYMENT

```bash
# Pages to TrueNAS
scp *.html jdmal@100.83.75.4:/mnt/tank/websites/kusanagi/isn.biz/public/

# Images to S3
aws s3 cp image.webp s3://isnbiz-assets-1769962280/premium_v3/projects/
```

## FULL DETAILS

See: CODEX_HANDOFF_COMPLETE.md in project root
