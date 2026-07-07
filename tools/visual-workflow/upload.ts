import type { AssetRecord } from "./shared/schema";
import { isApprovedIsnImageUrl } from "./shared/schema";
import { readJson, writeJson } from "./shared/io";

const ISN_CDN_PREFIX = "https://b2c.isn.biz/file/isnbiz-cdn";

export function cdnKeyFor(asset: AssetRecord): string {
  if (!asset.productSlug) throw new Error("iSN product asset requires productSlug");
  return `assets/generated/product-visuals/${asset.productSlug}/${asset.slot}.webp`;
}

export function registerCdnUrl(asset: AssetRecord, cdnUrl?: string): AssetRecord {
  const nextUrl = cdnUrl ?? (asset.site === "isn" ? `${ISN_CDN_PREFIX}/${cdnKeyFor(asset)}` : asset.cdnUrl);
  if (!nextUrl) throw new Error(`No CDN URL available for ${asset.pagePath}:${asset.slot}`);
  if (asset.site === "isn" && !isApprovedIsnImageUrl(nextUrl)) {
    throw new Error(`CDN URL is not approved for iSN: ${nextUrl}`);
  }
  return {
    ...asset,
    cdnUrl: nextUrl,
    status: "uploaded",
  };
}

export function main(): void {
  const args = process.argv.slice(2);
  const accept = args.includes("--accept");
  const assets = readJson<AssetRecord[]>("docs/visual-workflow/manifests/assets.json");
  const registered = assets.map((asset) => {
    if (asset.status !== "imported" && asset.status !== "generated") return asset;
    const uploaded = registerCdnUrl(asset);
    return accept ? { ...uploaded, status: "accepted" as const } : uploaded;
  });
  writeJson("docs/visual-workflow/manifests/assets.json", registered);
  console.log(`Registered CDN metadata for ${registered.filter((asset) => asset.cdnUrl).length} assets.`);
}

if (import.meta.main) main();
