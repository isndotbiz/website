import { existsSync } from "node:fs";
import type { AssetRecord, PromptRecord } from "./shared/schema";
import { readJson, repoPath, writeJson } from "./shared/io";
import { validatePrompts, hasErrors } from "./validate";

type BackendStatus = {
  backend: string;
  available: boolean;
  reason?: string;
};

export function probeBackends(env = process.env): BackendStatus[] {
  return [
    {
      backend: "manual-import",
      available: true,
      reason: "Manual import always available for externally generated images.",
    },
    {
      backend: "runpod",
      available: Boolean(env.RUNPOD_API_KEY && env.RUNPOD_ENDPOINT_ID),
      reason: env.RUNPOD_API_KEY ? undefined : "RUNPOD_API_KEY and RUNPOD_ENDPOINT_ID are required.",
    },
    {
      backend: "fal-ai:gpt-image-2",
      available: Boolean(env.FAL_KEY),
      reason: env.FAL_KEY ? undefined : "FAL_KEY is required.",
    },
    {
      backend: "truenas-comfyui",
      available: Boolean(env.COMFYUI_URL),
      reason: env.COMFYUI_URL ? undefined : "COMFYUI_URL is required.",
    },
  ];
}

export function registerManualImport(prompt: PromptRecord, localPath: string): AssetRecord {
  if (!existsSync(repoPath(localPath))) {
    throw new Error(`Manual import file does not exist: ${localPath}`);
  }
  return {
    site: prompt.site,
    productSlug: prompt.productSlug,
    pagePath: prompt.pagePath,
    slot: prompt.slot,
    sourcePromptId: `${prompt.productSlug}:${prompt.slot}`,
    localPath,
    backend: "manual-import",
    loras: prompt.loras,
    altText: prompt.altText,
    status: "imported",
  };
}

export function main(): void {
  const args = new Set(process.argv.slice(2));
  const prompts = readJson<PromptRecord[]>("docs/visual-workflow/prompts/isn-product-prompts.json");
  const issues = validatePrompts(prompts);
  if (hasErrors(issues)) {
    for (const issue of issues) console.error(`${issue.code}: ${issue.message}`);
    process.exit(1);
  }

  if (args.has("--probe")) {
    console.log(JSON.stringify(probeBackends(), null, 2));
    return;
  }

  writeJson(
    "docs/visual-workflow/manifests/backend-probe.json",
    {
      backends: probeBackends(),
    },
  );
  console.log("Wrote backend probe manifest.");
}

if (import.meta.main) main();
