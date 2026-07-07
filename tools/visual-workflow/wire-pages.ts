import { readFileSync, writeFileSync } from "node:fs";
import type { AssetRecord, ImageSlot } from "./shared/schema";
import { isApprovedIsnImageUrl } from "./shared/schema";
import { ISN_PRODUCTS } from "./shared/products";
import { readJson, repoPath, writeJson } from "./shared/io";

type Replacement = {
  pagePath: string;
  productSlug: string;
  slot: ImageSlot;
  from: string;
  to: string;
};

function acceptedAsset(assets: AssetRecord[], productSlug: string, slot: ImageSlot): AssetRecord {
  const asset = assets.find((item) => item.site === "isn" && item.productSlug === productSlug && item.slot === slot);
  if (!asset) throw new Error(`Missing asset ${productSlug}:${slot}`);
  if (asset.status !== "accepted") throw new Error(`Asset ${productSlug}:${slot} is not accepted`);
  if (!asset.cdnUrl) throw new Error(`Asset ${productSlug}:${slot} has no CDN URL`);
  if (!isApprovedIsnImageUrl(asset.cdnUrl)) throw new Error(`Asset ${productSlug}:${slot} uses off-host CDN URL`);
  return asset;
}

function currentProductImages(html: string, productSlug: string): string[] {
  const product = ISN_PRODUCTS.find((item) => item.slug === productSlug);
  const sources = new Set<string>();
  for (const match of html.matchAll(/<img\b[^>]*src=["']([^"']+)["'][^>]*>/gi)) {
    const tag = match[0];
    if (tag.toLowerCase().includes(productSlug) || (product && tag.includes(product.title))) sources.add(match[1]);
  }
  return [...sources];
}

export function planReplacements(assets: AssetRecord[]): Replacement[] {
  const replacements: Replacement[] = [];
  for (const product of ISN_PRODUCTS) {
    const hero = acceptedAsset(assets, product.slug, "hero");
    const og = acceptedAsset(assets, product.slug, "og");
    const card = acceptedAsset(assets, product.slug, "card");
    const productHtml = readFileSync(repoPath(product.pagePath), "utf8");
    for (const src of currentProductImages(productHtml, product.slug)) {
      replacements.push({ pagePath: product.pagePath, productSlug: product.slug, slot: "hero", from: src, to: hero.cdnUrl! });
    }
    for (const meta of ["og:image", "twitter:image"]) {
      const regex = new RegExp(`(<meta[^>]+(?:property|name)=["']${meta}["'][^>]+content=["'])([^"']+)(["'])`, "i");
      const current = productHtml.match(regex)?.[2];
      if (current) replacements.push({ pagePath: product.pagePath, productSlug: product.slug, slot: "og", from: current, to: og.cdnUrl! });
    }
    for (const pagePath of ["index.html", "portfolio.html"]) {
      const html = readFileSync(repoPath(pagePath), "utf8");
      for (const src of currentProductImages(html, product.slug)) {
        replacements.push({ pagePath, productSlug: product.slug, slot: "card", from: src, to: card.cdnUrl! });
      }
    }
  }
  return replacements;
}

export function applyReplacements(replacements: Replacement[]): void {
  const byPage = new Map<string, Replacement[]>();
  for (const replacement of replacements) {
    byPage.set(replacement.pagePath, [...(byPage.get(replacement.pagePath) ?? []), replacement]);
  }
  for (const [pagePath, pageReplacements] of byPage.entries()) {
    const fullPath = repoPath(pagePath);
    let html = readFileSync(fullPath, "utf8");
    for (const replacement of pageReplacements) {
      html = html.split(replacement.from).join(replacement.to);
    }
    writeFileSync(fullPath, html, "utf8");
  }
}

export function main(): void {
  const args = new Set(process.argv.slice(2));
  const apply = args.has("--apply");
  const assets = readJson<AssetRecord[]>("docs/visual-workflow/manifests/assets.json");
  const replacements = planReplacements(assets);
  writeJson("docs/visual-workflow/reports/wire-pages-report.json", { apply, replacements });
  if (apply) applyReplacements(replacements);
  console.log(`${apply ? "Applied" : "Planned"} ${replacements.length} page image replacements.`);
}

if (import.meta.main) main();
