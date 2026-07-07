# Product Visual Workflow

This folder holds the generated planning artifacts for the iSN product-page visual refresh. The workflow separates strategy, prompt design, asset production, acceptance, CDN registration, and page wiring so pages are not rewritten before real assets exist.

## Commands

Run from the repository root.

```sh
bun tools/visual-workflow/inventory.ts
bun tools/visual-workflow/prompts.ts
bun tools/visual-workflow/gpt-image-2.ts
bun tools/visual-workflow/generate.ts
bun tools/visual-workflow/hroc-map.ts
bun tools/visual-workflow/validate.ts
```

Use `bun tools/visual-workflow/generate.ts --probe` to inspect configured generation backends without calling them.

Use `bun tools/visual-workflow/gpt-image-2.ts` to build a dry-run request manifest for Fal `openai/gpt-image-2`. The request builder always uses `quality: "low"` and `output_format: "webp"`.

To submit jobs after `FAL_KEY` is available:

```sh
bun tools/visual-workflow/gpt-image-2.ts --submit
```

Add `--image-to-image` to include filtered current page images as `image_urls` references. Add `--limit=1` for a small paid smoke test before running the full 37-image batch.

## Artifact Map

- `inventory/isn-pages.json`: image, meta, and content inventory for current iSN pages.
- `inventory/hroc-pages.json`: image, meta, and content inventory for HROC pages.
- `prompts/isn-product-prompts.json`: product, slot, LoRA, and prompt records.
- `prompts/hroc-remap-prompts.json`: replacement prompt candidates for unused HROC generated assets.
- `manifests/assets.json`: planned, imported, generated, uploaded, accepted, and rejected product visual assets.
- `manifests/backend-probe.json`: available generation backends based on current environment variables.
- `manifests/gpt-image-2-requests.json`: Fal `openai/gpt-image-2` request bodies with meta-prompts, low quality, WebP output, and optional image-to-image references.
- `manifests/hroc-image-map.json`: HROC generated image usage map.
- `reports/visual-gap-report.md`: current page visual gaps and source risks.

## Asset Gates

`wire-pages.ts` only creates a dry-run replacement report unless `--apply` is passed. It also requires accepted CDN assets for each product hero, Open Graph, and card slot before replacing page HTML. That keeps generated prompts and unfinished local images from leaking into production pages.
