import type { ImageSlot, PromptRecord } from "./shared/schema";
import { ISN_PRODUCTS, loraStackFor } from "./shared/products";
import { writeJson } from "./shared/io";

const NEGATIVE_PROMPT = [
  "text",
  "logo",
  "watermark",
  "letters",
  "signature",
  "readable private records",
  "UI chrome",
  "low quality",
  "distorted anatomy",
].join(", ");

const PRODUCT_PROMPTS: Record<string, string> = {
  spiritatlas:
    "Hero artwork for Spirit Atlas on iSN.BiZ: a ritual-forward mobile cosmic entity discovery experience, luminous archetype cards suspended around a premium phone-like artifact, zodiac geometry, chakra color traces, numerology marks, and a dark celestial field with precise cyan and magenta energy accents. Editorial product-marketing key art, cinematic light sculpting, atmospheric depth, high-end web banner composition, no text overlays, no logos, no UI chrome, no readable symbols that imply real astrology claims.",
  provenance:
    "Hero artwork for Provenance on iSN.BiZ: cross-platform genealogy data integrity platform, archival family records transforming into a verified lineage graph, GEDCOM validation nodes, duplicate-merge evidence trails, trust badges rendered as abstract seals, and a calm technical workspace with cyan-blue audit paths. Editorial product-marketing key art, cinematic light sculpting, archival texture, high-end web banner composition, no text overlays, no logos, no UI chrome, no fake names, no readable private records.",
  signals:
    "Hero artwork for Signals on iSN.BiZ: market intelligence signal pipeline with EDGAR, EMMA, USDA, Federal Register, and enforcement-feed scanner streams converging into a live forward-returns ledger, ranked alerts, ticker resolution, delayed-feed audit window, and evidence trails. Dense investor-grade technical command surface, cinematic cyan grid light, subtle magenta anomaly highlights, high-end web banner composition, no text overlays, no logos, no UI chrome, no real tickers, no financial advice language.",
  "phantom-browser":
    "Hero artwork for Phantom Browser on iSN.BiZ: Rust and Tauri stealth browser orchestration system, profile fleet nodes, coherent browser fingerprints, residential and mobile proxy mesh, IP reputation scoring gates, and a CreepJS-style diagnostic environment rendered as abstract instrumentation. Dark technical operations room, cyan grid precision, magenta risk signals, cinematic light sculpting, high-end web banner composition, no text overlays, no logos, no UI chrome, no illegal activity depiction.",
  crucible:
    "Hero artwork for Crucible on iSN.BiZ: LLM red-team laboratory and adversarial evaluation harness, model transcript streams entering a judge stack, jailbreak scenario simulator, scored eval matrix, RAG research mode, and safety boundary instrumentation. Dark high-trust AI security lab, precise cyan evaluation grids, warning-magenta adversarial traces, cinematic atmosphere, high-end web banner composition, no text overlays, no logos, no UI chrome, no depiction of real harmful instructions.",
  "hermes-aingels":
    "Hero artwork for HERMES + AiNGELS on iSN.BiZ: NFT-as-Agent architecture on Base L2, ERC-6551 token-bound accounts as luminous identity vessels, cryptographic anchor set, voice and visual identity artifacts, 12-sister lineage tree, and genesis covenant agent represented as a precise celestial network. Premium mythic-technical key art, cyan blockchain lattice, magenta reveal energy, cinematic depth, high-end web banner composition, no text overlays, no logos, no UI chrome, no celebrity likenesses.",
};

const SLOT_ASPECT: Record<ImageSlot, string> = {
  hero: "16:9",
  og: "1200x630",
  card: "4:3",
  "study-01": "16:9",
  "study-02": "16:9",
  "study-03": "16:9",
  diagram: "16:9",
  supporting: "16:9",
};

function slotsFor(productSlug: string): ImageSlot[] {
  const base: ImageSlot[] = ["hero", "og", "card"];
  return productSlug === "signals"
    ? [...base, "study-01", "study-02", "study-03", "diagram"]
    : [...base, "study-01", "study-02", "study-03"];
}

function promptForSlot(slug: string, slot: ImageSlot, basePrompt: string): string {
  if (slot === "og") return `${basePrompt} Compose for a clean 1200x630 social preview crop.`;
  if (slot === "card") return `${basePrompt} Compose as a compact product card crop with the subject readable at small size.`;
  if (slot.startsWith("study")) return `${basePrompt} Focus this study on ${slot.replace("-", " ")} as a supporting visual, not the main hero.`;
  if (slot === "diagram") return `${basePrompt} Emphasize abstract data-flow diagram composition without text labels.`;
  return basePrompt;
}

export function buildIsnPromptRecords(): PromptRecord[] {
  return ISN_PRODUCTS.flatMap((product) => {
    const loras = loraStackFor(product);
    const triggerPrefix = loras.map((lora) => lora.trigger).join(", ");
    const basePrompt = `${triggerPrefix}. ${PRODUCT_PROMPTS[product.slug]}`;
    return slotsFor(product.slug).map((slot) => ({
      site: "isn" as const,
      productSlug: product.slug,
      productTitle: product.title,
      pagePath: product.pagePath,
      slot,
      aspectRatio: SLOT_ASPECT[slot],
      targetFilename: `assets/generated/product-visuals/${product.slug}/${slot}.webp`,
      prompt: promptForSlot(product.slug, slot, basePrompt),
      negativePrompt: NEGATIVE_PROMPT,
      loras,
      altText: `${product.title} ${slot} visual - ${product.visualThesis}`,
      references: product.legacySlugs.map((legacy) => `legacy:${legacy}`),
      status: "planned" as const,
    }));
  });
}

export function main(): void {
  const prompts = buildIsnPromptRecords();
  writeJson("docs/visual-workflow/prompts/isn-product-prompts.json", prompts);
  writeJson(
    "docs/visual-workflow/manifests/assets.json",
    prompts.map((prompt) => ({
      site: prompt.site,
      productSlug: prompt.productSlug,
      pagePath: prompt.pagePath,
      slot: prompt.slot,
      sourcePromptId: `${prompt.productSlug}:${prompt.slot}`,
      loras: prompt.loras,
      altText: prompt.altText,
      status: "planned",
    })),
  );
  console.log(`Wrote ${prompts.length} iSN prompt records.`);
}

if (import.meta.main) main();
