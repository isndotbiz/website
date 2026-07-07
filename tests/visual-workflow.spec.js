// @ts-check
const { execFileSync, spawnSync } = require('node:child_process');
const { existsSync, readFileSync } = require('node:fs');
const path = require('node:path');
const { test, expect } = require('@playwright/test');

const REPO_ROOT = path.resolve(__dirname, '..');

function runBun(args) {
  return execFileSync('bun', args, {
    cwd: REPO_ROOT,
    encoding: 'utf8',
    env: { ...process.env, VISUAL_WORKFLOW_ROOT: REPO_ROOT },
  });
}

function readJson(relativePath) {
  return JSON.parse(readFileSync(path.join(REPO_ROOT, relativePath), 'utf8'));
}

test.describe('Visual workflow tools', () => {
  test('generate inventory, prompts, and a valid planned asset manifest', () => {
    expect(runBun(['tools/visual-workflow/inventory.ts'])).toContain('Wrote 19 iSN pages');
    expect(runBun(['tools/visual-workflow/prompts.ts'])).toContain('Wrote');
    expect(runBun(['tools/visual-workflow/validate.ts'])).toContain('validation passed');

    const isnPages = readJson('docs/visual-workflow/inventory/isn-pages.json');
    const prompts = readJson('docs/visual-workflow/prompts/isn-product-prompts.json');
    const assets = readJson('docs/visual-workflow/manifests/assets.json');
    const productSlugs = ['spiritatlas', 'provenance', 'signals', 'phantom-browser', 'crucible', 'hermes-aingels'];

    expect(isnPages.length).toBeGreaterThanOrEqual(19);
    for (const slug of productSlugs) {
      const productPrompts = prompts.filter(record => record.productSlug === slug);
      expect(productPrompts.some(record => record.slot === 'hero'), `${slug} has hero prompt`).toBe(true);
      expect(productPrompts.some(record => record.slot === 'og'), `${slug} has og prompt`).toBe(true);
      expect(productPrompts.some(record => record.slot === 'card'), `${slug} has card prompt`).toBe(true);
      expect(productPrompts.every(record => record.loras.length > 0), `${slug} prompts include LoRA recipes`).toBe(true);
      expect(assets.some(record => record.productSlug === slug && record.status === 'planned'), `${slug} has planned assets`).toBe(true);
    }

    const gapReport = readFileSync(path.join(REPO_ROOT, 'docs/visual-workflow/reports/visual-gap-report.md'), 'utf8');
    expect(gapReport).toContain('Visual Gap Report');
  });

  test('probe generation backends without requiring external credentials', () => {
    expect(runBun(['tools/visual-workflow/generate.ts'])).toContain('Wrote backend probe');
    const probe = readJson('docs/visual-workflow/manifests/backend-probe.json');
    expect(probe.backends.some(record => record.backend === 'manual-import' && record.available === true)).toBe(true);
    expect(probe.backends.some(record => record.backend === 'fal-ai:gpt-image-2')).toBe(true);
  });

  test('build GPT Image 2 low-quality Fal request manifest without submitting jobs', () => {
    expect(runBun(['tools/visual-workflow/gpt-image-2.ts', '--image-to-image'])).toContain('openai/gpt-image-2 request records');
    const requests = readJson('docs/visual-workflow/manifests/gpt-image-2-requests.json');
    expect(requests.length).toBe(37);
    expect(requests.every(record => record.model === 'openai/gpt-image-2')).toBe(true);
    expect(requests.every(record => record.quality === 'low' && record.input.quality === 'low')).toBe(true);
    expect(requests.every(record => record.outputFormat === 'webp' && record.input.output_format === 'webp')).toBe(true);
    expect(requests.every(record => !record.input.prompt.includes('gpt-image-1'))).toBe(true);
    expect(requests.some(record => record.input.prompt.includes('RAG context'))).toBe(true);
  });

  test('map HROC generated image usage when archived manifest is present', () => {
    const hrocManifest = path.join(REPO_ROOT, 'hrocincorg/archive/website_internals/generated_images/image_manifest.json');
    test.skip(!existsSync(hrocManifest), 'HROC archived generated-image manifest is not present in this checkout.');

    expect(runBun(['tools/visual-workflow/hroc-map.ts'])).toContain('Wrote HROC image map');
    const map = readJson('docs/visual-workflow/manifests/hroc-image-map.json');
    expect(map.length).toBeGreaterThan(0);
    expect(map.every(record => ['used', 'unused', 'repeated', 'candidate'].includes(record.status))).toBe(true);
  });

  test('refuse page wiring before required assets are accepted', () => {
    runBun(['tools/visual-workflow/prompts.ts']);

    const result = spawnSync('bun', ['tools/visual-workflow/wire-pages.ts'], {
      cwd: REPO_ROOT,
      encoding: 'utf8',
      env: { ...process.env, VISUAL_WORKFLOW_ROOT: REPO_ROOT },
    });
    const output = `${result.stdout || ''}${result.stderr || ''}`;

    expect(result.status).not.toBe(0);
    expect(output).toContain('is not accepted');
  });
});
