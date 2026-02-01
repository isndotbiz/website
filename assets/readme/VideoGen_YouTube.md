# VideoGen_YouTube

Automated pipeline that converts web articles into production-ready video assets, scripts, and upload workflows for YouTube and short-form platforms.

## Funder Snapshot
- Problem: Educational video production is slow, expensive, and inconsistent.
- Solution: End-to-end automation from content sourcing to scripts, visuals, narration, assembly, and upload.
- Differentiation: Multi-provider integrations and batch orchestration for scalable output.

## What Is Built
- Orchestrated pipeline (orchestrate.js) for scrape -> dataset -> script generation.
- Script, storyboard, narration, and slide-deck generators.
- Image and animation generation integrations.
- Video assembly and upload automation.
- Extensive runbooks, guides, and automation scripts.

## Architecture
```
Article URL
 -> scrape + JSON/JSONL dataset
 -> script + storyboard + narration
 -> images + animations
 -> video assembly
 -> upload + SEO metadata
```

## Tech Stack
- Node.js + Python
- Firecrawl, Axios, Cheerio
- fal.ai, Runway, ElevenLabs, Descript
- AWS S3, YouTube OAuth

## Repository Structure
```
orchestrate.js            Pipeline entry
video_pipeline/           Core pipeline logic
scripts/                  Automation helpers
docs/                     Guides and runbooks
```

## Quick Start
```
npm install
node orchestrate.js "https://example.com/article"
```

## Roadmap
See PROJECT_OVERVIEW_AND_ROADMAP.md for the implementation plan and next steps.

## License
See LICENSE in the repo.
