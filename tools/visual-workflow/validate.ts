import type { AssetRecord, PromptRecord, ValidationIssue } from "./shared/schema";
import { isApprovedIsnImageUrl } from "./shared/schema";
import { ISN_PRODUCTS, REQUIRED_ISN_SLOTS } from "./shared/products";
import { readJson } from "./shared/io";

export function validatePrompts(prompts: PromptRecord[]): ValidationIssue[] {
  const issues: ValidationIssue[] = [];
  for (const product of ISN_PRODUCTS) {
    const records = prompts.filter((prompt) => prompt.site === "isn" && prompt.productSlug === product.slug);
    for (const slot of REQUIRED_ISN_SLOTS) {
      if (!records.some((record) => record.slot === slot)) {
        issues.push({
          severity: "error",
          code: "missing-product-slot",
          message: `${product.slug} is missing prompt slot ${slot}`,
        });
      }
    }
  }

  for (const prompt of prompts) {
    if (!prompt.altText.trim()) {
      issues.push({ severity: "error", code: "missing-alt", message: `${prompt.productSlug}:${prompt.slot} missing alt text` });
    }
    if (!prompt.loras.length) {
      issues.push({ severity: "error", code: "missing-loras", message: `${prompt.productSlug}:${prompt.slot} missing LoRA stack` });
    }
    if (!prompt.prompt.trim()) {
      issues.push({ severity: "error", code: "missing-prompt", message: `${prompt.productSlug}:${prompt.slot} missing prompt` });
    }
  }
  return issues;
}

export function validateAssets(assets: AssetRecord[]): ValidationIssue[] {
  const issues: ValidationIssue[] = [];
  for (const asset of assets) {
    const label = `${asset.productSlug ?? asset.pagePath}:${asset.slot}`;
    if (!asset.altText?.trim()) {
      issues.push({ severity: "error", code: "asset-missing-alt", message: `${label} missing alt text` });
    }
    if ((asset.status === "uploaded" || asset.status === "accepted") && !asset.cdnUrl) {
      issues.push({ severity: "error", code: "accepted-without-cdn", message: `${label} has ${asset.status} status without CDN URL` });
    }
    if (asset.site === "isn" && asset.cdnUrl && !isApprovedIsnImageUrl(asset.cdnUrl)) {
      issues.push({ severity: "error", code: "off-host-cdn", message: `${label} CDN URL is not on an approved host`, path: asset.cdnUrl });
    }
    if (asset.slot === "og" && asset.localPath && !asset.localPath.includes("/og.")) {
      issues.push({ severity: "warning", code: "og-slot-name", message: `${label} local path does not look like an OG asset` });
    }
  }
  return issues;
}

export function hasErrors(issues: ValidationIssue[]): boolean {
  return issues.some((issue) => issue.severity === "error");
}

export function main(): void {
  const prompts = readJson<PromptRecord[]>("docs/visual-workflow/prompts/isn-product-prompts.json");
  const assets = readJson<AssetRecord[]>("docs/visual-workflow/manifests/assets.json");
  const issues = [...validatePrompts(prompts), ...validateAssets(assets)];
  if (!issues.length) {
    console.log("Visual workflow validation passed.");
    return;
  }
  for (const issue of issues) {
    console.log(`${issue.severity.toUpperCase()} ${issue.code}: ${issue.message}${issue.path ? ` (${issue.path})` : ""}`);
  }
  if (hasErrors(issues)) process.exit(1);
}

if (import.meta.main) main();
