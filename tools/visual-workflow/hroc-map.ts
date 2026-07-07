import type { AssetRecord } from "./shared/schema";
import { HROC_PAGES } from "./shared/products";
import { readJson, readText, writeJson } from "./shared/io";

interface HrocImageManifestEntry {
  filename: string;
  category: string;
  placement?: string;
  alt_text?: string;
}

interface HrocImageManifest {
  images: HrocImageManifestEntry[];
}

export interface HrocImageMapRecord {
  filename: string;
  category: string;
  placement: string;
  status: "used" | "unused" | "repeated" | "candidate";
  pages: string[];
  altText: string;
}

function pageUses(filename: string): string[] {
  return HROC_PAGES.filter((page) => readText(page.sourcePath).includes(filename)).map((page) => page.sourcePath);
}

export function buildHrocImageMap(): HrocImageMapRecord[] {
  const manifest = readJson<HrocImageManifest>("hrocincorg/archive/website_internals/generated_images/image_manifest.json");
  return manifest.images.map((image) => {
    const pages = pageUses(image.filename);
    const status = pages.length > 1 ? "repeated" : pages.length === 1 ? "used" : "unused";
    return {
      filename: image.filename,
      category: image.category,
      placement: image.placement ?? "",
      status,
      pages,
      altText: image.alt_text ?? "",
    };
  });
}

export function replacementPrompts(map: HrocImageMapRecord[]): AssetRecord[] {
  return map
    .filter((record) => record.status === "unused" && /hero|donate|document|impact/i.test(record.placement))
    .map((record) => ({
      site: "hroc" as const,
      pagePath: record.placement || "hrocincorg/HROC_Website_New/index.html",
      slot: "supporting" as const,
      altText: record.altText || `HROC ${record.category} visual`,
      status: "planned" as const,
      notes: `Candidate from existing manifest: ${record.filename}`,
    }));
}

export function main(): void {
  const map = buildHrocImageMap();
  writeJson("docs/visual-workflow/manifests/hroc-image-map.json", map);
  writeJson("docs/visual-workflow/prompts/hroc-remap-prompts.json", replacementPrompts(map));
  console.log(`Wrote HROC image map for ${map.length} images.`);
}

if (import.meta.main) main();
