import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, resolve } from "node:path";

export const repoRoot = resolve(process.env.VISUAL_WORKFLOW_ROOT ?? process.cwd());

export function repoPath(path: string): string {
  return resolve(repoRoot, path);
}

export function readText(path: string): string {
  return readFileSync(repoPath(path), "utf8");
}

export function writeText(path: string, content: string): void {
  const fullPath = repoPath(path);
  mkdirSync(dirname(fullPath), { recursive: true });
  writeFileSync(fullPath, content, "utf8");
}

export function readJson<T>(path: string): T {
  return JSON.parse(readText(path)) as T;
}

export function writeJson(path: string, data: unknown): void {
  writeText(path, `${JSON.stringify(data, null, 2)}\n`);
}

export function stripHtml(value: string): string {
  return value
    .replace(/<script[\s\S]*?<\/script>/gi, "")
    .replace(/<style[\s\S]*?<\/style>/gi, "")
    .replace(/<[^>]+>/g, " ")
    .replace(/&mdash;/g, "-")
    .replace(/&amp;/g, "&")
    .replace(/&#39;/g, "'")
    .replace(/&quot;/g, '"')
    .replace(/\s+/g, " ")
    .trim();
}

export function lineForOffset(text: string, offset: number): number {
  return text.slice(0, offset).split("\n").length;
}
