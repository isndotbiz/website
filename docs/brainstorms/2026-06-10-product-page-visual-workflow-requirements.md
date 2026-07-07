# Product Page Visual Workflow Requirements

Date: 2026-06-10
Project: iSN.BiZ website and HROC site visual/content workflow
Status: Requirements draft

## Summary

Build a repeatable workflow that starts with a page and asset inventory, then turns each page into a content brief, image prompt pack, LoRA recipe, asset naming plan, CDN/SEO wiring checklist, and QA gate.

The first pass should focus on the six canonical iSN products, because the current pages are content-rich but visually over-reuse Spirit Atlas background imagery. HROC should use the same workflow, but with a different goal: curate, map, and refine the existing generated image library before requesting new images.

## Evidence Used

- `_audit/CANON.md` defines the current iSN product truth: exactly six products, with HROC framed as the 501(c)(3) beneficiary rather than a seventh product.
- `_audit/AUDIT_REPORT.md` records the most recent iSN modernization pass: 19 pages audited, 111/111 Playwright tests passing, canonical SEO/schema/nav/footer rules established.
- Current product HTML pages contain substantial copy but mostly reference reused Spirit Atlas imagery for hero, key art, OG image, and visual study slots.
- `docs/truenas_flux_project_assets_manifest.json` contains an older Flux hero-art manifest for nine legacy projects. It is useful as style evidence and LoRA precedent, but it does not match the current six-product portfolio.
- `hrocincorg/archive/website_internals/image-generator/MASTER_IMAGE_PLAN.md` contains a 45-image HROC prompt plan.
- `hrocincorg/archive/website_internals/IMAGE_GENERATION_SUMMARY.md` records 56 generated HROC images across five categories.
- `hrocincorg/archive/website_internals/generated_images/image_manifest.json` maps HROC image categories, placements, filenames, and alt text.

## Goals

1. Create one workflow that works for both sites without forcing one brand style across both sites.
2. Replace generic or reused product visuals with page-specific key art that reflects the actual product thesis, architecture, and audience.
3. Preserve the existing iSN and HROC brand systems instead of flattening them into generic AI imagery.
4. Produce prompt packs that are reusable, inspectable, and traceable to page requirements.
5. Make every generated asset easy to wire into page hero art, card art, OG/Twitter images, and supporting visual studies.
6. Add QA gates so visual refreshes do not break CDN host rules, image accessibility, SEO metadata, page word-count invariants, or mobile layout.

## Non-Goals

- Do not rewrite the entire site during the brainstorming artifact.
- Do not invent new products, new claims, or new performance metrics.
- Do not treat HROC as a product page in the iSN portfolio.
- Do not generate or deploy images until the image backend, LoRA availability, and output naming contract are confirmed during implementation planning.
- Do not remove the existing HROC image library unless a later QA pass proves a specific image is unusable.

## Current Inventory Findings

### iSN Page Set

The active iSN site has 19 HTML pages:

- Core pages: `index.html`, `about.html`, `services.html`, `portfolio.html`, `investors.html`, `contact.html`
- Product pages: `spiritatlas.html`, `provenance.html`, `signals/index.html`, `phantom-browser.html`, `crucible.html`, `hermes-aingels.html`
- Cause partner page: `hroc-files.html`
- Leadership/legal/system pages: `jonathan.html`, `bri.html`, `lilly.html`, `privacy.html`, `terms.html`, `404.html`

The first visual workflow target should be the product pages plus their portfolio/homepage card appearances:

- `spiritatlas.html`
- `provenance.html`
- `signals/index.html`
- `phantom-browser.html`
- `crucible.html`
- `hermes-aingels.html`
- `portfolio.html`
- `index.html`

### iSN Visual Gap

The product pages have detailed product copy, but their imagery is not specific enough. Provenance, Signals, Phantom Browser, Crucible, and HERMES + AiNGELS mostly use Spirit Atlas background images while alt text describes product-specific visuals. That creates a mismatch between the page story and the visible artifact.

The older Flux manifest partially helps:

- Spirit Atlas has a matching generated hero.
- Provenance has a legacy GEDFix prompt that can be adapted.
- Phantom Browser has a legacy prompt.
- Crucible has a legacy LLM Security Research prompt that can be adapted.
- HROC Files has a legacy prompt.
- Signals and HERMES + AiNGELS need new current-specific prompt records.

### HROC Page Set

The current HROC site under `hrocincorg/HROC_Website_New` has nine HTML pages:

- `index.html`
- `donate.html`
- `documents.html`
- `jonathan.html`
- `bri.html`
- `lilly.html`
- `privacy-policy.html`
- `terms.html`
- `404.html`

HROC has a stronger existing image foundation than iSN:

- 7 hero banners
- 12 service icons
- 10 background patterns
- 15 community photos
- 12 informational graphics

The HROC workflow should first map existing images to the current nine pages, identify mismatches, and only then generate missing or replacement assets.

## Workflow Requirements

### 1. Inventory Truth

For each site, produce a machine-readable and human-readable inventory before any prompt writing:

- Page path
- Page role
- Canonical title and description
- H1/H2 structure
- Current image URLs
- Current image alt text
- Current OG/Twitter image
- Current content gaps
- Current visual gaps
- Whether the page is product, company, leadership, legal, cause partner, or system page

The inventory should flag:

- Reused images with mismatched alt text
- Portrait or 9:16 images used as 1200x630 OG images
- Images not on approved hosts
- Missing product-specific hero/key art
- Missing portfolio/homepage card art
- HROC images that exist in the manifest but are not used

### 2. Page Brief

Every page receiving new or remapped visuals needs a page brief:

- Audience
- Page job
- Emotional tone
- Product or mission thesis
- Primary scene
- Supporting scenes
- Must-show elements
- Must-avoid elements
- Output slots needed
- Alt text requirements

For iSN product pages, the brief should be technical, dense, investor-grade, and specific to the architecture.

For HROC pages, the brief should be dignified, trauma-informed, community-centered, and culturally careful. Avoid poverty spectacle, medical panic imagery, and generic nonprofit stock-photo language.

### 3. Prompt Pack

Each prompt pack should include these outputs:

- Hero/key art, landscape 16:9
- OG/Twitter card, 1200x630
- Portfolio/homepage card crop, 4:3 or 16:9
- Three supporting visual studies for product pages where the page already has a key-art grid
- Optional diagram-style or interface-style supporting images when the page explains architecture

Each prompt should include:

- Brand direction
- Scene
- Composition
- Lighting/material direction
- Product-specific details
- Negative constraints
- Output size/aspect ratio
- LoRA stack
- Alt text draft
- Intended page slot
- Asset filename

### 4. LoRA Recipe

The existing iSN Flux manifest establishes a useful baseline stack:

- `ethereal_glow_v2.safetensors`: luminous gradient/energy layer
- `hyperrealism_flux_cinematic.safetensors`: cinematic detail and light shaping
- `portrait_engine_flux.safetensors`: polished rendering
- `dark_fantasy_cosmic_flux.safetensors` or `ethereal_dark.safetensors`: dark atmospheric grounding
- `ethereal_fantasy_flux.safetensors`: high-end otherworldly atmosphere
- One product-specific Spirit Atlas LoRA: `psychedelic_surrealism.safetensors`, `sacred_geometry.safetensors`, or `glowing_particles.safetensors`

Implementation planning must confirm exact LoRA availability and exact parameter names for the chosen image backend. Until then, strengths below are creative recommendations, not verified execution config.

Recommended baseline strengths:

- Ethereal glow: model 0.28-0.32, clip 0.24-0.28
- Hyperreal cinematic: model 0.22-0.26, clip 0.18-0.22
- Polished rendering: model 0.14-0.17, clip 0.11-0.14
- Dark/cosmic grounding: model 0.16-0.20, clip 0.13-0.16
- Ethereal fantasy: model 0.12-0.15, clip 0.10-0.13
- Product-specific motif LoRA: model 0.10-0.14, clip 0.08-0.11

## iSN Product Prompt Matrix

### Spirit Atlas

Page: `spiritatlas.html`
Visual thesis: Ritual-forward cosmic entity discovery, premium mystical mobile experience, archetype reveal.

Primary prompt:

```text
EtherealGlow, luminous gradients, HyperRealism, premium cinematic detail, fluxtrait polished rendering, ethereal dark grounding, ethereal fantasy atmosphere, glowing particles and ambient dust. Hero artwork for Spirit Atlas on iSN.BiZ: a ritual-forward mobile cosmic entity discovery experience, luminous archetype cards suspended around a premium phone-like artifact, zodiac geometry, chakra color traces, numerology marks, and a dark celestial field with precise cyan and magenta energy accents. Editorial product-marketing key art, cinematic light sculpting, atmospheric depth, high-end web banner composition, no text overlays, no logos, no UI chrome, no readable symbols that imply real astrology claims.
```

Recommended LoRA stack:

- `ethereal_glow_v2.safetensors`
- `hyperrealism_flux_cinematic.safetensors`
- `portrait_engine_flux.safetensors`
- `ethereal_dark.safetensors`
- `ethereal_fantasy_flux.safetensors`
- `SpiritAtlas/glowing_particles.safetensors`

Supporting studies:

- Zodiac/entity reveal chamber
- Chakra/numerology ritual surface
- Premium archetype-card library wall

### Provenance

Page: `provenance.html`
Visual thesis: Genealogy data integrity, GEDCOM repair, lineage verification, archival trust surface.

Primary prompt:

```text
EtherealGlow, luminous gradients, HyperRealism, premium cinematic detail, fluxtrait polished rendering, cc_dark fantasy dramatic contrast, ethereal fantasy atmosphere, sacred geometry motifs. Hero artwork for Provenance on iSN.BiZ: cross-platform genealogy data integrity platform, archival family records transforming into a verified lineage graph, GEDCOM validation nodes, duplicate-merge evidence trails, trust badges rendered as abstract seals, and a calm technical workspace with cyan-blue audit paths. Editorial product-marketing key art, cinematic light sculpting, archival texture, high-end web banner composition, no text overlays, no logos, no UI chrome, no fake names, no readable private records.
```

Recommended LoRA stack:

- `ethereal_glow_v2.safetensors`
- `hyperrealism_flux_cinematic.safetensors`
- `portrait_engine_flux.safetensors`
- `dark_fantasy_cosmic_flux.safetensors`
- `ethereal_fantasy_flux.safetensors`
- `SpiritAtlas/sacred_geometry.safetensors`

Supporting studies:

- Scan/check/fix GEDCOM pipeline
- Dedupe/merge/review evidence board
- Tauri/SvelteKit/CLI multi-surface platform diagram as key art

### Signals

Page: `signals/index.html`
Visual thesis: Market-intelligence pipeline, scanner fusion, forward-returns ledger, delayed-feed auditability.

Primary prompt:

```text
EtherealGlow, luminous gradients, HyperRealism, premium cinematic detail, fluxtrait polished rendering, cc_dark fantasy dramatic contrast, ethereal fantasy atmosphere, psychedelic surreal geometry. Hero artwork for Signals on iSN.BiZ: market intelligence signal pipeline with EDGAR, EMMA, USDA, Federal Register, and enforcement-feed scanner streams converging into a live forward-returns ledger, ranked alerts, ticker resolution, delayed-feed audit window, and evidence trails. Dense investor-grade technical command surface, cinematic cyan grid light, subtle magenta anomaly highlights, high-end web banner composition, no text overlays, no logos, no UI chrome, no real tickers, no financial advice language.
```

Recommended LoRA stack:

- `ethereal_glow_v2.safetensors`
- `hyperrealism_flux_cinematic.safetensors`
- `portrait_engine_flux.safetensors`
- `dark_fantasy_cosmic_flux.safetensors`
- `ethereal_fantasy_flux.safetensors`
- `SpiritAtlas/psychedelic_surrealism.safetensors`

Supporting studies:

- Source ingestion scanner fleet
- Enrichment and ticker-resolution stage
- Cross-signal fusion/ranking stage
- Forward-returns ledger publish stage

### Phantom Browser

Page: `phantom-browser.html`
Visual thesis: Stealth browser orchestration, fingerprint coherence, proxy reputation, resilient automation.

Primary prompt:

```text
EtherealGlow, luminous gradients, HyperRealism, premium cinematic detail, fluxtrait polished rendering, cc_dark fantasy dramatic contrast, ethereal fantasy atmosphere, psychedelic surreal geometry. Hero artwork for Phantom Browser on iSN.BiZ: Rust and Tauri stealth browser orchestration system, profile fleet nodes, coherent browser fingerprints, residential and mobile proxy mesh, IP reputation scoring gates, and a CreepJS-style diagnostic environment rendered as abstract instrumentation. Dark technical operations room, cyan grid precision, magenta risk signals, cinematic light sculpting, high-end web banner composition, no text overlays, no logos, no UI chrome, no illegal activity depiction.
```

Recommended LoRA stack:

- `ethereal_glow_v2.safetensors`
- `hyperrealism_flux_cinematic.safetensors`
- `portrait_engine_flux.safetensors`
- `dark_fantasy_cosmic_flux.safetensors`
- `ethereal_fantasy_flux.safetensors`
- `SpiritAtlas/psychedelic_surrealism.safetensors`

Supporting studies:

- Fingerprint coherence triangle
- Proxy/IP reputation gate
- Browser profile fleet orchestration

### Crucible

Page: `crucible.html`
Visual thesis: LLM red-team and adversarial evaluation stack, jailbreak research, judge harness, transcript scoring.

Primary prompt:

```text
EtherealGlow, luminous gradients, HyperRealism, premium cinematic detail, fluxtrait polished rendering, cc_dark fantasy dramatic contrast, ethereal fantasy atmosphere, sacred geometry motifs. Hero artwork for Crucible on iSN.BiZ: LLM red-team laboratory and adversarial evaluation harness, model transcript streams entering a judge stack, jailbreak scenario simulator, scored eval matrix, RAG research mode, and safety boundary instrumentation. Dark high-trust AI security lab, precise cyan evaluation grids, warning-magenta adversarial traces, cinematic atmosphere, high-end web banner composition, no text overlays, no logos, no UI chrome, no depiction of real harmful instructions.
```

Recommended LoRA stack:

- `ethereal_glow_v2.safetensors`
- `hyperrealism_flux_cinematic.safetensors`
- `portrait_engine_flux.safetensors`
- `dark_fantasy_cosmic_flux.safetensors`
- `ethereal_fantasy_flux.safetensors`
- `SpiritAtlas/sacred_geometry.safetensors`

Supporting studies:

- Jailbreak methodology workbench
- Eval/judge harness scoring matrix
- Transcript capture and scenario simulator

### HERMES + AiNGELS

Page: `hermes-aingels.html`
Visual thesis: NFT-as-Agent architecture, Base L2, ERC-6551 token-bound accounts, cryptographic identity lattice.

Primary prompt:

```text
EtherealGlow, luminous gradients, HyperRealism, premium cinematic detail, fluxtrait polished rendering, ethereal dark grounding, ethereal fantasy atmosphere, sacred geometry motifs, glowing particles and ambient dust. Hero artwork for HERMES + AiNGELS on iSN.BiZ: NFT-as-Agent architecture on Base L2, ERC-6551 token-bound accounts as luminous identity vessels, cryptographic anchor set, voice and visual identity artifacts, 12-sister lineage tree, and genesis covenant agent represented as a precise celestial network. Premium mythic-technical key art, cyan blockchain lattice, magenta reveal energy, cinematic depth, high-end web banner composition, no text overlays, no logos, no UI chrome, no celebrity likenesses.
```

Recommended LoRA stack:

- `ethereal_glow_v2.safetensors`
- `hyperrealism_flux_cinematic.safetensors`
- `portrait_engine_flux.safetensors`
- `ethereal_dark.safetensors`
- `ethereal_fantasy_flux.safetensors`
- `SpiritAtlas/sacred_geometry.safetensors`
- `SpiritAtlas/glowing_particles.safetensors`

Supporting studies:

- Token-bound account identity vault
- Genesis and 12-sister lineage tree
- Agent birth pipeline and reveal sequence

## iSN Cross-Page Asset Requirements

Each product should receive:

- `hero.webp`: product page hero/key art
- `og.webp`: 1200x630 social image
- `card.webp`: portfolio and homepage card art
- `study-01.webp`, `study-02.webp`, `study-03.webp`: supporting visual studies when the page has a key-art grid

Recommended path pattern:

```text
assets/generated/product-visuals/<product-slug>/<slot>.webp
```

Recommended CDN pattern after upload:

```text
https://b2c.isn.biz/file/isnbiz-cdn/assets/generated/product-visuals/<product-slug>/<slot>.webp
```

Every image needs:

- Source prompt
- LoRA stack and strengths
- Generation backend and model
- Date generated
- Intended page slot
- Alt text
- Local source path
- CDN URL after upload
- Acceptance status

## HROC Visual Workflow

HROC should not start from blank prompts. It should start by mapping existing generated assets into the current site.

Required HROC inventory actions:

1. Load the 56-image manifest.
2. Map each image to the current nine HROC pages.
3. Identify unused high-quality images.
4. Identify repeated images that should stay repeated versus repeated images caused by missing better matches.
5. Verify whether S3 and B2/CDN URLs are current and accessible during implementation.
6. Flag any image that looks culturally insensitive, too generic, too polished/stock-like, medically alarming, or inconsistent with the current HROC page tone.

HROC prompt generation should be limited to these cases:

- Missing current-page hero
- Missing document/transparency image
- Missing donate/contribution impact visual
- Missing leadership visual that should match current founder pages
- Replacement for an image that fails dignity, accuracy, or quality review

HROC prompt style:

```text
Professional documentary-style image for Healing Roots Outreach Collective: dignified mobile harm-reduction outreach in King and Pierce Counties, Indigenous-led and peer-based care, community members receiving practical support with consent and respect, warm Pacific Northwest natural light, calm grounded composition, authentic service environment, brand accents in magenta, cyan, lime, and deep plum, trauma-informed visual language, no poverty spectacle, no staged suffering, no visible private medical details, no readable personal documents, no text overlays, no logos unless explicitly requested.
```

HROC should favor photographic/documentary image generation over surreal or highly cinematic iSN-style visuals.

## QA Requirements

Before any refreshed page is considered complete:

- All images load successfully.
- Every image URL is on an approved host defined by `_audit/CANON.md`.
- Product pages remain above the test-locked body-copy threshold.
- OG images are true 1200x630 assets, not portrait crops mislabeled as 1200x630.
- Alt text describes the actual image, not the desired image.
- Homepage and portfolio cards use the same product-specific visual language as their product pages.
- Mobile widths do not introduce horizontal scroll.
- The existing Playwright audit suite stays green.
- HROC pages are checked separately against the HROC site rules and deployment target.

## Acceptance Criteria

The workflow is successful when:

1. A page inventory exists for both iSN and HROC.
2. The six iSN product pages each have a current product-specific prompt pack and LoRA recipe.
3. Homepage and portfolio card visuals are covered for all six iSN products.
4. HROC has an image mapping report before any new HROC image generation is requested.
5. Every proposed image has slot, filename, prompt, LoRA stack, alt text, and QA criteria.
6. The next implementation plan can proceed without re-litigating product count, HROC role, or brand style.

## Planning Notes

Implementation planning should decide:

- Image backend: Flux/Comfy, fal.ai, Gemini, OpenAI image generation, or another available pipeline.
- Whether the named LoRAs are available in the selected backend.
- Whether to generate iSN product visuals in one batch or page-by-page.
- Whether asset upload to B2/CDN is manual, scripted, or part of an existing deployment flow.
- Whether to store prompt metadata as JSON, markdown, or both.
- Whether to add image-manifest validation to the existing Playwright or static audit suite.

Recommended next skill: `compound-engineering:ce-plan`.
