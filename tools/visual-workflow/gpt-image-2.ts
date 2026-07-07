import { mkdirSync, writeFileSync } from "node:fs";
import { dirname } from "node:path";
import type { AssetRecord, ImageSlot, PageInventory, PromptRecord } from "./shared/schema";
import { readJson, repoPath, writeJson } from "./shared/io";

const MODEL_ID = "openai/gpt-image-2";
const EDIT_MODEL_ID = "openai/gpt-image-2/edit";
const QUALITY = "low" as const;
const OUTPUT_FORMAT = "webp" as const;

type FalImageSize = "landscape_16_9" | "landscape_4_3" | { width: number; height: number };

interface GptImage2RequestRecord {
  id: string;
  productSlug: string;
  productTitle: string;
  pagePath: string;
  slot: ImageSlot;
  model: typeof MODEL_ID;
  endpoint: typeof MODEL_ID | typeof EDIT_MODEL_ID;
  quality: typeof QUALITY;
  outputFormat: typeof OUTPUT_FORMAT;
  imageSize: FalImageSize;
  targetFilename: string;
  sourceReferences: string[];
  input: {
    prompt: string;
    image_size: FalImageSize;
    quality: typeof QUALITY;
    num_images: 1;
    output_format: typeof OUTPUT_FORMAT;
    image_urls?: string[];
  };
}

interface FalQueueSubmitResponse {
  request_id: string;
  response_url: string;
  status_url: string;
  cancel_url?: string;
}

interface FalImageResult {
  url: string;
  width?: number;
  height?: number;
  content_type?: string;
  file_name?: string;
  file_size?: number;
}

interface FalResultResponse {
  images?: FalImageResult[];
  image?: FalImageResult;
}

function slotIntent(slot: ImageSlot): string {
  if (slot === "hero") return "first-viewport product hero, wide crop, strong subject separation, no readable text";
  if (slot === "og") return "social preview image, center-safe composition, readable at small share-card size, no text";
  if (slot === "card") return "portfolio/product card image, compact crop, immediate product identity, no text";
  if (slot === "diagram") return "abstract systems diagram as art, visual flow without labels or readable UI";
  if (slot.startsWith("study")) return "supporting product study image, distinct from the main hero, suitable for content sections";
  return "supporting editorial product image";
}

function imageSizeFor(slot: ImageSlot): FalImageSize {
  if (slot === "card") return "landscape_4_3";
  if (slot === "og") return { width: 1200, height: 640 };
  return "landscape_16_9";
}

function pageContextFor(prompt: PromptRecord, pages: PageInventory[]): string {
  const page = pages.find((item) => item.path === prompt.pagePath || item.productSlug === prompt.productSlug);
  if (!page) return "";
  return [
    page.title ? `Page title: ${page.title}` : "",
    page.description ? `Page description: ${page.description}` : "",
    page.headings.h1.length ? `Primary headings: ${page.headings.h1.join("; ")}` : "",
    page.headings.h2.length ? `Section themes: ${page.headings.h2.slice(0, 5).join("; ")}` : "",
  ]
    .filter(Boolean)
    .join("\n");
}

function referenceUrlsFor(prompt: PromptRecord, pages: PageInventory[], enabled: boolean): string[] {
  if (!enabled) return [];
  const page = pages.find((item) => item.path === prompt.pagePath || item.productSlug === prompt.productSlug);
  if (!page) return [];
  const productTitle = prompt.productTitle.toLowerCase();
  const productSlug = prompt.productSlug.toLowerCase();
  const productWords = new Set([...productTitle.split(/\W+/), ...productSlug.split(/\W+/)].filter((word) => word.length > 3));
  const urls = [page.ogImage, page.twitterImage, ...page.images]
    .filter(Boolean)
    .filter((image) => {
      const alt = image!.alt.toLowerCase();
      const src = image!.src.toLowerCase();
      if (/logo|portrait|founder|headshot|navbar/i.test(`${alt} ${src}`)) return false;
      return alt.includes(productTitle) || src.includes(productSlug) || [...productWords].some((word) => alt.includes(word));
    })
    .map((image) => image!.src)
    .filter((src) => /^https:\/\//.test(src))
    .filter((src) => prompt.productSlug === "spiritatlas" || !/spiritatlas\/images\/backgrounds_24/i.test(src));
  return [...new Set(urls)].slice(0, 2);
}

function loraStyleNotes(prompt: PromptRecord): string {
  return prompt.loras
    .map((lora) => `${lora.trigger} (${lora.file}, model ${lora.strengthModel}, clip ${lora.strengthClip})`)
    .join("; ");
}

export function buildGptImage2Prompt(prompt: PromptRecord, pages: PageInventory[]): string {
  const pageContext = pageContextFor(prompt, pages);
  const ragContext = [
    "RAG context: prior iSN/SpiritAtlas fal.ai image work favored detailed production prompts, explicit LoRA-style visual cues, cinematic lighting, and clear asset-slot targets.",
    "Treat LoRA entries as style references only; this GPT Image 2 endpoint does not receive LoRA files directly.",
  ].join(" ");

  return [
    `Create production web artwork for iSN.BiZ using ${MODEL_ID}.`,
    `Product: ${prompt.productTitle}. Slot: ${prompt.slot}. Intent: ${slotIntent(prompt.slot)}.`,
    pageContext,
    ragContext,
    `Style reference stack: ${loraStyleNotes(prompt)}.`,
    `Base creative direction: ${prompt.prompt}`,
    `Hard constraints: output a polished image only; no readable words, no logos, no watermarks, no UI chrome, no private records, no celebrity likenesses, no distorted hands or faces. Optimize the prompt for ${QUALITY} quality by using a simple readable composition, large primary forms, crisp contrast, clean negative space, and high signal-to-noise detail.`,
    `Negative prompt concepts to avoid: ${prompt.negativePrompt}.`,
  ]
    .filter(Boolean)
    .join("\n\n");
}

export function buildRequestRecords(options: { imageToImage?: boolean } = {}): GptImage2RequestRecord[] {
  const prompts = readJson<PromptRecord[]>("docs/visual-workflow/prompts/isn-product-prompts.json");
  const pages = readJson<PageInventory[]>("docs/visual-workflow/inventory/isn-pages.json");
  return prompts.map((prompt) => {
    const imageSize = imageSizeFor(prompt.slot);
    const imageUrls = referenceUrlsFor(prompt, pages, Boolean(options.imageToImage));
    const input: GptImage2RequestRecord["input"] = {
      prompt: buildGptImage2Prompt(prompt, pages),
      image_size: imageSize,
      quality: QUALITY,
      num_images: 1,
      output_format: OUTPUT_FORMAT,
      ...(imageUrls.length ? { image_urls: imageUrls } : {}),
    };
    return {
      id: `${prompt.productSlug}:${prompt.slot}`,
      productSlug: prompt.productSlug,
      productTitle: prompt.productTitle,
      pagePath: prompt.pagePath,
      slot: prompt.slot,
      model: MODEL_ID,
      endpoint: imageUrls.length ? EDIT_MODEL_ID : MODEL_ID,
      quality: QUALITY,
      outputFormat: OUTPUT_FORMAT,
      imageSize,
      targetFilename: prompt.targetFilename,
      sourceReferences: [...prompt.references, ...imageUrls.map((url) => `image:${url}`)],
      input,
    };
  });
}

async function falFetch<T>(url: string, init: RequestInit = {}): Promise<T> {
  const key = process.env.FAL_KEY;
  if (!key) throw new Error("FAL_KEY is required to submit GPT Image 2 jobs.");
  const response = await fetch(url, {
    ...init,
    headers: {
      Authorization: `Key ${key}`,
      "Content-Type": "application/json",
      ...(init.headers ?? {}),
    },
  });
  if (!response.ok) {
    const body = await response.text();
    throw new Error(`Fal request failed ${response.status}: ${body}`);
  }
  return (await response.json()) as T;
}

async function submitRequest(record: GptImage2RequestRecord): Promise<FalQueueSubmitResponse> {
  return falFetch<FalQueueSubmitResponse>(`https://queue.fal.run/${record.endpoint}`, {
    method: "POST",
    body: JSON.stringify(record.input),
  });
}

async function waitForResult(submission: FalQueueSubmitResponse, pollMs: number): Promise<FalResultResponse> {
  while (true) {
    const status = await falFetch<{ status?: string; logs?: unknown[] }>(submission.status_url);
    if (status.status === "COMPLETED") return falFetch<FalResultResponse>(submission.response_url);
    if (status.status === "FAILED") throw new Error(`Fal job failed: ${JSON.stringify(status)}`);
    await new Promise((resolve) => setTimeout(resolve, pollMs));
  }
}

async function downloadImage(url: string, localPath: string): Promise<{ width?: number; height?: number; contentType?: string }> {
  const response = await fetch(url);
  if (!response.ok) throw new Error(`Image download failed ${response.status}: ${url}`);
  const arrayBuffer = await response.arrayBuffer();
  const fullPath = repoPath(localPath);
  mkdirSync(dirname(fullPath), { recursive: true });
  writeFileSync(fullPath, Buffer.from(arrayBuffer));
  return { contentType: response.headers.get("content-type") ?? undefined };
}

function updateAsset(asset: AssetRecord, record: GptImage2RequestRecord, submission: FalQueueSubmitResponse, image: FalImageResult): AssetRecord {
  return {
    ...asset,
    localPath: record.targetFilename,
    backend: "fal-ai",
    model: MODEL_ID,
    requestId: submission.request_id,
    remoteUrl: image.url,
    imageSize: record.imageSize,
    quality: QUALITY,
    outputFormat: OUTPUT_FORMAT,
    width: image.width,
    height: image.height,
    contentType: image.content_type,
    status: "generated",
    notes: "Generated by fal.ai openai/gpt-image-2 at low quality.",
  };
}

async function generateAll(records: GptImage2RequestRecord[], limit?: number): Promise<void> {
  const assets = readJson<AssetRecord[]>("docs/visual-workflow/manifests/assets.json");
  let generated = 0;
  for (const record of records) {
    if (limit !== undefined && generated >= limit) break;
    const assetIndex = assets.findIndex((asset) => asset.productSlug === record.productSlug && asset.slot === record.slot);
    if (assetIndex === -1) throw new Error(`No asset manifest record for ${record.id}`);
    if (assets[assetIndex].status !== "planned" && assets[assetIndex].status !== "blocked") continue;

    console.log(`Submitting ${record.id} to ${record.endpoint}...`);
    const submission = await submitRequest(record);
    const result = await waitForResult(submission, Number(process.env.FAL_POLL_MS ?? 2000));
    const image = result.images?.[0] ?? result.image;
    if (!image?.url) throw new Error(`Fal result for ${record.id} did not include an image URL.`);
    const downloaded = await downloadImage(image.url, record.targetFilename);
    assets[assetIndex] = updateAsset(assets[assetIndex], record, submission, { ...image, ...downloaded });
    writeJson("docs/visual-workflow/manifests/assets.json", assets);
    generated += 1;
  }
  console.log(`Generated ${generated} ${MODEL_ID} assets.`);
}

export async function main(): Promise<void> {
  const args = new Set(process.argv.slice(2));
  const submit = args.has("--submit");
  const imageToImage = args.has("--image-to-image");
  const limitArg = process.argv.find((arg) => arg.startsWith("--limit="));
  const limit = limitArg ? Number(limitArg.split("=")[1]) : undefined;
  const records = buildRequestRecords({ imageToImage });

  writeJson("docs/visual-workflow/manifests/gpt-image-2-requests.json", records);
  console.log(`Wrote ${records.length} ${MODEL_ID} request records with quality=${QUALITY}.`);

  if (!submit) return;
  await generateAll(records, limit);
}

if (import.meta.main) {
  main().catch((error) => {
    console.error(error instanceof Error ? error.message : error);
    process.exit(1);
  });
}
