export const APPROVED_ISN_IMAGE_HOSTS = [
  "b2c.isn.biz",
  "s3.amazonaws.com",
  "isnbiz-assets",
  "amazonaws.com",
] as const;

export type SiteId = "isn" | "hroc";

export type PageRole =
  | "home"
  | "core"
  | "product"
  | "cause-partner"
  | "leadership"
  | "legal"
  | "system";

export type ImageSlot =
  | "hero"
  | "og"
  | "card"
  | "study-01"
  | "study-02"
  | "study-03"
  | "diagram"
  | "supporting";

export type AssetStatus =
  | "planned"
  | "generated"
  | "imported"
  | "uploaded"
  | "accepted"
  | "blocked"
  | "rejected";

export interface ImageReference {
  src: string;
  alt: string;
  context: "img" | "og:image" | "twitter:image" | "json-ld" | "preload";
  line?: number;
}

export interface PageInventory {
  site: SiteId;
  path: string;
  title: string;
  description: string;
  role: PageRole;
  productSlug?: string;
  headings: {
    h1: string[];
    h2: string[];
  };
  images: ImageReference[];
  ogImage?: ImageReference;
  twitterImage?: ImageReference;
  flags: string[];
}

export interface LoraRecipe {
  file: string;
  trigger: string;
  strengthModel: number;
  strengthClip: number;
}

export interface PromptRecord {
  site: SiteId;
  productSlug: string;
  productTitle: string;
  pagePath: string;
  slot: ImageSlot;
  aspectRatio: string;
  targetFilename: string;
  prompt: string;
  negativePrompt: string;
  loras: LoraRecipe[];
  altText: string;
  references: string[];
  status: "planned" | "blocked";
}

export interface AssetRecord {
  site: SiteId;
  productSlug?: string;
  pagePath: string;
  slot: ImageSlot;
  sourcePromptId?: string;
  localPath?: string;
  cdnUrl?: string;
  backend?: string;
  model?: string;
  requestId?: string;
  remoteUrl?: string;
  imageSize?: string | { width: number; height: number };
  quality?: "auto" | "low" | "medium" | "high";
  outputFormat?: "jpeg" | "png" | "webp";
  width?: number;
  height?: number;
  contentType?: string;
  seed?: string | number;
  loras?: LoraRecipe[];
  altText: string;
  status: AssetStatus;
  notes?: string;
}

export interface ValidationIssue {
  severity: "error" | "warning";
  code: string;
  message: string;
  path?: string;
}

export function isApprovedIsnImageUrl(src: string): boolean {
  if (!src || src.startsWith("data:")) return true;
  try {
    const url = new URL(src);
    return APPROVED_ISN_IMAGE_HOSTS.some((host) => url.hostname.includes(host));
  } catch {
    return false;
  }
}

export function isLikelyPortraitSource(src: string): boolean {
  return /(^|\/)(9x16|portrait|vertical|founders?|headshot)/i.test(src);
}
