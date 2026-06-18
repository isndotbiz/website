# ISN.BIZ Website

> Canonical global rules: `~/.claude/CLAUDE.md`. This file = website-specific stack + deploy + conventions.

Live investor-ready website for ISN.BIZ Inc. LIVE at https://isn.biz.

## Stack / Architecture
- 20 static HTML pages + CSS/JS — no framework
- Hosting: Cloudflare Pages
- CDN/proxy: Cloudflare (SSL: Full)
- Images: Backblaze B2 via `b2c.isn.biz` + AWS S3 bucket `isnbiz-assets-1769962280` (legacy)
- CI/CD: GitHub Actions → Playwright tests → deploy on push to main

## Key Files
```
ISNBIZ_Files/
├── *.html              # 20 pages (7 main, 4 bios, 9 project pages)
├── styles.css          # CSS vars: --color-blue #1E9FF2, --color-cyan #5FDFDF, --color-charcoal #0D1117
├── tests/site-audit.spec.js  # Playwright suite (baseURL: https://isn.biz)
└── .github/workflows/auto-deploy.yml
```

## Dev Commands
```bash
python -m http.server 8000                           # local preview :8000
npx playwright test                                  # test against https://isn.biz
BASE_URL=http://localhost:8000 npx playwright test   # test locally
```

## Deploy
```bash
git push origin main   # triggers CI: tests → deploy
```

## Image Upload (Backblaze B2)
```bash
# URL pattern: https://b2c.isn.biz/file/isnbiz-cdn/assets/image.webp
```

## Conventions
- Cards MUST maintain 3xN or 4xN grid layout
- Design: Neo-Technical Brutalism (dark, technical)
- New pages: copy template → update all nav links → add redirect → add test
- Local `assets/` is gitignored (154MB) — use B2 CDN URLs only
- WebP format preferred for all images

## Open Tasks
- [ ] Contact form backend (wire up Cloudflare Worker or Formspree)
- [ ] Google Analytics 4 on all 20 pages

## Knowledge Substrate — RAG + Graphify (search before you research)

> Canonical wiring: `~/Workspace/Research/RAG-GRAPHIFY-WIRING.md`. Endpoints/collections drift — verify against `rag-system/CLAUDE.md` + `mcp__rag__list_collections`; never hardcode.

**RAG (knowledge-first).** Before any web research, search RAG first; ≥3 relevant hits = enough.
- PAI/Claude Code: `mcp__rag__search_knowledge_base` / `mcp__rag__query_knowledge_base` / `mcp__rag__list_collections` / `mcp__rag__ingest_document`.
- Sandboxed (codex/opencode/Hermes): `POST /v1/search`, health `GET /v1/health`, auth `X-API-Key`. `https://rag.isn.biz` / `http://100.83.75.4:8400`. Key: 1Password `RAG-API-Key-Current`. Never trust Xeon `100.65.249.20`.
- Ingest every research artifact into the most-specific collection before session end (`POST /v1/ingest`).

**Graphify (graph-first for structure).** Treat codebase/architecture/file-relationship questions as Graphify queries first.
- Canonical workspace `~/Workspace/Research/graphify/`; artifacts `graphify/ingested/<category>/<source>--<name>/graph.json`; merged `graphify/merged/agent-system-merged-graph.json`.
- Always pass explicit graph paths: `graphify query "<q>" --graph <path>`. Never scatter `graphify-out/`; move into `graphify/ingested/...` and refresh manifests. No symlinks.
