import { existsSync } from "node:fs";
import type { ImageReference, PageInventory } from "./shared/schema";
import { isApprovedIsnImageUrl, isLikelyPortraitSource } from "./shared/schema";
import { HROC_PAGES, ISN_PAGES } from "./shared/products";
import { lineForOffset, readJson, readText, stripHtml, writeJson, writeText } from "./shared/io";

interface HrocGeneratedImage {
  filename: string;
  category: string;
  placement?: string;
  alt_text?: string;
}

interface HrocManifest {
  images: HrocGeneratedImage[];
}

function attr(tag: string, name: string): string {
  const match = tag.match(new RegExp(`${name}=["']([^"']*)["']`, "i"));
  return match?.[1] ?? "";
}

function metaContent(html: string, selector: RegExp): string {
  const match = html.match(selector);
  return match ? attr(match[0], "content") : "";
}

function headings(html: string, tag: "h1" | "h2"): string[] {
  return [...html.matchAll(new RegExp(`<${tag}\\b[^>]*>([\\s\\S]*?)<\\/${tag}>`, "gi"))].map((m) =>
    stripHtml(m[1] ?? ""),
  );
}

function imgRefs(html: string): ImageReference[] {
  return [...html.matchAll(/<img\b[^>]*>/gi)].map((match) => {
    const tag = match[0];
    return {
      src: attr(tag, "src"),
      alt: attr(tag, "alt"),
      context: "img",
      line: lineForOffset(html, match.index ?? 0),
    };
  });
}

function metadataRefs(html: string): { ogImage?: ImageReference; twitterImage?: ImageReference } {
  const og = html.match(/<meta\b[^>]*property=["']og:image["'][^>]*>/i);
  const twitter = html.match(/<meta\b[^>]*name=["']twitter:image["'][^>]*>/i);
  return {
    ogImage: og
      ? {
          src: attr(og[0], "content"),
          alt: metaContent(html, /<meta\b[^>]*property=["']og:image:alt["'][^>]*>/i),
          context: "og:image",
          line: lineForOffset(html, og.index ?? 0),
        }
      : undefined,
    twitterImage: twitter
      ? {
          src: attr(twitter[0], "content"),
          alt: metaContent(html, /<meta\b[^>]*name=["']twitter:image:alt["'][^>]*>/i),
          context: "twitter:image",
          line: lineForOffset(html, twitter.index ?? 0),
        }
      : undefined,
  };
}

function pageFlags(page: PageInventory): string[] {
  const flags: string[] = [];
  const refs = [...page.images, page.ogImage, page.twitterImage].filter(Boolean) as ImageReference[];

  for (const ref of refs) {
    if (!ref.alt && ref.context === "img") flags.push(`missing-alt:${ref.src}`);
    if (page.site === "isn" && !isApprovedIsnImageUrl(ref.src)) flags.push(`off-host:${ref.src}`);
    if (ref.context === "og:image" && isLikelyPortraitSource(ref.src)) flags.push(`portrait-og:${ref.src}`);
  }

  if (page.role === "product" && page.productSlug !== "spiritatlas") {
    for (const ref of refs) {
      if (ref.src.includes("spiritatlas/images/backgrounds_24")) {
        flags.push(`reused-spiritatlas-background:${ref.context}:${ref.src}`);
      }
    }
  }

  if (page.role === "product" && !page.ogImage) flags.push("missing-og-image");
  if (page.role === "product" && !page.twitterImage) flags.push("missing-twitter-image");
  return [...new Set(flags)];
}

function inventoryPage(def: (typeof ISN_PAGES | typeof HROC_PAGES)[number]): PageInventory {
  const html = readText(def.sourcePath);
  const metadata = metadataRefs(html);
  const page: PageInventory = {
    site: def.site,
    path: def.path,
    title: stripHtml(html.match(/<title[^>]*>([\s\S]*?)<\/title>/i)?.[1] ?? ""),
    description: metaContent(html, /<meta\b[^>]*name=["']description["'][^>]*>/i),
    role: def.role,
    productSlug: def.productSlug,
    headings: {
      h1: headings(html, "h1"),
      h2: headings(html, "h2"),
    },
    images: imgRefs(html),
    ...metadata,
    flags: [],
  };
  page.flags = pageFlags(page);
  return page;
}

function hrocManifestUsage(hrocPages: PageInventory[]): string[] {
  const manifestPath = "hrocincorg/archive/website_internals/generated_images/image_manifest.json";
  if (!existsSync(manifestPath)) return ["HROC generated-image manifest missing."];
  const manifest = readJson<HrocManifest>(manifestPath);
  const usedSrcs = new Set(hrocPages.flatMap((page) => page.images.map((img) => img.src)));
  const lines: string[] = [];
  for (const image of manifest.images) {
    const used = [...usedSrcs].some((src) => src.includes(image.filename));
    if (!used) {
      lines.push(`- unused: ${image.category}/${image.filename} (${image.placement ?? "no placement"})`);
    }
  }
  return lines;
}

function report(isnPages: PageInventory[], hrocPages: PageInventory[]): string {
  const productFlags = isnPages.filter((page) => page.role === "product").flatMap((page) =>
    page.flags.map((flag) => `- ${page.path}: ${flag}`),
  );
  const hrocUnused = hrocManifestUsage(hrocPages);
  return [
    "# Visual Gap Report",
    "",
    "## iSN Product Flags",
    "",
    productFlags.length ? productFlags.join("\n") : "- No product flags found.",
    "",
    "## HROC Manifest Usage",
    "",
    hrocUnused.length ? hrocUnused.join("\n") : "- Every manifest image appears to be used.",
    "",
  ].join("\n");
}

export function buildInventory(): { isnPages: PageInventory[]; hrocPages: PageInventory[] } {
  return {
    isnPages: ISN_PAGES.map(inventoryPage),
    hrocPages: HROC_PAGES.map(inventoryPage),
  };
}

export function main(): void {
  const { isnPages, hrocPages } = buildInventory();
  writeJson("docs/visual-workflow/inventory/isn-pages.json", isnPages);
  writeJson("docs/visual-workflow/inventory/hroc-pages.json", hrocPages);
  writeText("docs/visual-workflow/reports/visual-gap-report.md", report(isnPages, hrocPages));
  console.log(`Wrote ${isnPages.length} iSN pages and ${hrocPages.length} HROC pages.`);
}

if (import.meta.main) main();
