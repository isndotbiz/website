import type { ImageSlot, LoraRecipe, PageRole } from "./schema";

export interface ProductDefinition {
  slug: string;
  title: string;
  pagePath: string;
  visualThesis: string;
  motif: "glowing_particles" | "sacred_geometry" | "psychedelic_surrealism";
  legacySlugs: string[];
  supportingStudies: string[];
}

export interface PageDefinition {
  site: "isn" | "hroc";
  path: string;
  sourcePath: string;
  role: PageRole;
  productSlug?: string;
}

export const ISN_PRODUCTS: ProductDefinition[] = [
  {
    slug: "spiritatlas",
    title: "Spirit Atlas",
    pagePath: "spiritatlas.html",
    visualThesis: "Ritual-forward cosmic entity discovery, premium mystical mobile experience, archetype reveal.",
    motif: "glowing_particles",
    legacySlugs: ["spiritatlas"],
    supportingStudies: [
      "Zodiac/entity reveal chamber",
      "Chakra/numerology ritual surface",
      "Premium archetype-card library wall",
    ],
  },
  {
    slug: "provenance",
    title: "Provenance",
    pagePath: "provenance.html",
    visualThesis: "Genealogy data integrity, GEDCOM repair, lineage verification, archival trust surface.",
    motif: "sacred_geometry",
    legacySlugs: ["gedfix"],
    supportingStudies: [
      "Scan/check/fix GEDCOM pipeline",
      "Dedupe/merge/review evidence board",
      "Tauri/SvelteKit/CLI multi-surface platform diagram as key art",
    ],
  },
  {
    slug: "signals",
    title: "Signals",
    pagePath: "signals/index.html",
    visualThesis: "Market-intelligence pipeline, scanner fusion, forward-returns ledger, delayed-feed auditability.",
    motif: "psychedelic_surrealism",
    legacySlugs: [],
    supportingStudies: [
      "Source ingestion scanner fleet",
      "Enrichment and ticker-resolution stage",
      "Cross-signal fusion/ranking stage",
      "Forward-returns ledger publish stage",
    ],
  },
  {
    slug: "phantom-browser",
    title: "Phantom Browser",
    pagePath: "phantom-browser.html",
    visualThesis: "Stealth browser orchestration, fingerprint coherence, proxy reputation, resilient automation.",
    motif: "psychedelic_surrealism",
    legacySlugs: ["phantom-browser"],
    supportingStudies: [
      "Fingerprint coherence triangle",
      "Proxy/IP reputation gate",
      "Browser profile fleet orchestration",
    ],
  },
  {
    slug: "crucible",
    title: "Crucible",
    pagePath: "crucible.html",
    visualThesis: "LLM red-team and adversarial evaluation stack, jailbreak research, judge harness, transcript scoring.",
    motif: "sacred_geometry",
    legacySlugs: ["llm-security-research"],
    supportingStudies: [
      "Jailbreak methodology workbench",
      "Eval/judge harness scoring matrix",
      "Transcript capture and scenario simulator",
    ],
  },
  {
    slug: "hermes-aingels",
    title: "HERMES + AiNGELS",
    pagePath: "hermes-aingels.html",
    visualThesis: "NFT-as-Agent architecture, Base L2, ERC-6551 token-bound accounts, cryptographic identity lattice.",
    motif: "sacred_geometry",
    legacySlugs: [],
    supportingStudies: [
      "Token-bound account identity vault",
      "Genesis and 12-sister lineage tree",
      "Agent birth pipeline and reveal sequence",
    ],
  },
];

export const ISN_PAGES: PageDefinition[] = [
  { site: "isn", path: "/", sourcePath: "index.html", role: "home" },
  { site: "isn", path: "/about", sourcePath: "about.html", role: "core" },
  { site: "isn", path: "/services", sourcePath: "services.html", role: "core" },
  { site: "isn", path: "/portfolio", sourcePath: "portfolio.html", role: "core" },
  { site: "isn", path: "/investors", sourcePath: "investors.html", role: "core" },
  { site: "isn", path: "/contact", sourcePath: "contact.html", role: "core" },
  ...ISN_PRODUCTS.map((product) => ({
    site: "isn" as const,
    path: product.pagePath === "signals/index.html" ? "/signals/" : `/${product.slug}`,
    sourcePath: product.pagePath,
    role: "product" as const,
    productSlug: product.slug,
  })),
  { site: "isn", path: "/hroc-files", sourcePath: "hroc-files.html", role: "cause-partner" },
  { site: "isn", path: "/jonathan", sourcePath: "jonathan.html", role: "leadership" },
  { site: "isn", path: "/bri", sourcePath: "bri.html", role: "leadership" },
  { site: "isn", path: "/lilly", sourcePath: "lilly.html", role: "leadership" },
  { site: "isn", path: "/privacy", sourcePath: "privacy.html", role: "legal" },
  { site: "isn", path: "/terms", sourcePath: "terms.html", role: "legal" },
  { site: "isn", path: "/404", sourcePath: "404.html", role: "system" },
];

export const HROC_PAGES: PageDefinition[] = [
  { site: "hroc", path: "/", sourcePath: "hrocincorg/HROC_Website_New/index.html", role: "home" },
  { site: "hroc", path: "/donate", sourcePath: "hrocincorg/HROC_Website_New/donate.html", role: "core" },
  { site: "hroc", path: "/documents", sourcePath: "hrocincorg/HROC_Website_New/documents.html", role: "core" },
  { site: "hroc", path: "/bri", sourcePath: "hrocincorg/HROC_Website_New/bri.html", role: "leadership" },
  { site: "hroc", path: "/jonathan", sourcePath: "hrocincorg/HROC_Website_New/jonathan.html", role: "leadership" },
  { site: "hroc", path: "/lilly", sourcePath: "hrocincorg/HROC_Website_New/lilly.html", role: "leadership" },
  { site: "hroc", path: "/privacy", sourcePath: "hrocincorg/HROC_Website_New/privacy-policy.html", role: "legal" },
  { site: "hroc", path: "/terms", sourcePath: "hrocincorg/HROC_Website_New/terms.html", role: "legal" },
  { site: "hroc", path: "/404", sourcePath: "hrocincorg/HROC_Website_New/404.html", role: "system" },
];

export const REQUIRED_ISN_SLOTS: ImageSlot[] = ["hero", "og", "card"];

export const BASE_LORAS = {
  etherealGlow: {
    file: "ethereal_glow_v2.safetensors",
    trigger: "EtherealGlow, luminous gradients",
    strengthModel: 0.3,
    strengthClip: 0.26,
  },
  hyperreal: {
    file: "hyperrealism_flux_cinematic.safetensors",
    trigger: "HyperRealism, premium cinematic detail",
    strengthModel: 0.25,
    strengthClip: 0.21,
  },
  polished: {
    file: "portrait_engine_flux.safetensors",
    trigger: "fluxtrait polished rendering",
    strengthModel: 0.16,
    strengthClip: 0.13,
  },
  darkFantasy: {
    file: "dark_fantasy_cosmic_flux.safetensors",
    trigger: "cc_dark fantasy dramatic contrast",
    strengthModel: 0.18,
    strengthClip: 0.15,
  },
  etherealDark: {
    file: "ethereal_dark.safetensors",
    trigger: "ethereal dark grounding",
    strengthModel: 0.18,
    strengthClip: 0.15,
  },
  etherealFantasy: {
    file: "ethereal_fantasy_flux.safetensors",
    trigger: "ethereal fantasy atmosphere",
    strengthModel: 0.14,
    strengthClip: 0.12,
  },
} satisfies Record<string, LoraRecipe>;

export function motifLora(product: ProductDefinition): LoraRecipe {
  if (product.motif === "glowing_particles") {
    return {
      file: "SpiritAtlas/glowing_particles.safetensors",
      trigger: "glowing particles and ambient dust",
      strengthModel: 0.14,
      strengthClip: 0.12,
    };
  }
  if (product.motif === "psychedelic_surrealism") {
    return {
      file: "SpiritAtlas/psychedelic_surrealism.safetensors",
      trigger: "psychedelic surreal geometry",
      strengthModel: 0.12,
      strengthClip: 0.1,
    };
  }
  return {
    file: "SpiritAtlas/sacred_geometry.safetensors",
    trigger: "sacred geometry motifs",
    strengthModel: 0.14,
    strengthClip: 0.12,
  };
}

export function loraStackFor(product: ProductDefinition): LoraRecipe[] {
  return [
    BASE_LORAS.etherealGlow,
    BASE_LORAS.hyperreal,
    BASE_LORAS.polished,
    product.motif === "glowing_particles" ? BASE_LORAS.etherealDark : BASE_LORAS.darkFantasy,
    BASE_LORAS.etherealFantasy,
    motifLora(product),
  ];
}
