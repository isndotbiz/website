# CLAUDE.md - ISN.BIZ Website

**Project:** ISN.BIZ Inc Investor-Ready Website
**Status:** LIVE IN PRODUCTION at https://isn.biz
**Location:** `D:\workspace\ISNBIZ_Files\`
**Last Updated:** 2026-02-25

---

## Quick Overview

Multi-page static HTML/CSS/JS website for ISN.BIZ Inc (software company). Designed to attract investor funding and showcase the AI/cloud software portfolio. The site is fully live with CI/CD auto-deployment via GitHub Actions to Netlify.

**Architecture:**
```
Browser → Cloudflare (proxy ON, SSL: Full) → Netlify (HTML pages)
                                            → S3 CDN (all images/assets)
```

**Key Facts:**
- **20 HTML pages** (7 main + 4 founder bios + 9 project pages)
- **Design system:** Neo-Technical Brutalism (dark, technical aesthetic)
- **Testing:** Playwright (`tests/site-audit.spec.js`), runs against https://isn.biz
- **CI/CD:** GitHub Actions (`.github/workflows/auto-deploy.yml`) - tests then deploys
- **Repo:** https://github.com/isndotbiz/website.git
- **Netlify site:** `isndotbiz.netlify.app` (site ID: `4d860499-0d6c-49cd-864f-69a0b7a2b3fe`)

---

## Website Pages

### Main Pages
| File | URL | Description |
|------|-----|-------------|
| `index.html` | `/` | Homepage: hero, about, solutions (4), portfolio preview (9), team (4), investors |
| `about.html` | `/about` | Company details, 6 trust badges, team grid (4 founders) |
| `services.html` | `/services` | Solutions portfolio with visual grid |
| `portfolio.html` | `/portfolio` | 8 case studies (4x2), methodology, results |
| `investors.html` | `/investors` | Investment pitch, market, use of funds (6 items) |
| `contact.html` | `/contact` | Contact form (currently stub - shows alert()) |
| `404.html` | (error) | Custom 404 error page |

### Founder Bio Pages
`jonathan.html` (CEO), `bri.html` (COO), `lilly.html` (CFO), `alicia.html` (CPO)

### Project Pages (9 total)
`truenas.html`, `videogen.html`, `bin-intelligence.html`, `spiritatlas.html` (Coming March 2026),
`comfyui.html`, `gedcom.html`, `llm-optimization.html`, `opportunity-bot.html`, `aurallm.html`

### Brand Colors (Neo-Technical Brutalism)

```css
--color-blue: #1E9FF2      /* Primary brand - CTAs, accents */
--color-cyan: #5FDFDF      /* Secondary - highlights, gradients */
--color-charcoal: #0D1117  /* Dark backgrounds */
--accent-pink: #FF2D55     /* Accent highlights */
```

### File Structure

```
ISNBIZ_Files/
├── *.html                          # 20 HTML pages
├── styles.css                      # Main stylesheet
├── script.js                       # Main JavaScript (minimal)
├── enhanced-animations.css         # Animation styles
├── netlify.toml                    # Netlify build config + URL redirects (19 clean URLs)
├── playwright.config.js            # Test config (baseURL: https://isn.biz)
├── package.json                    # Node deps (Playwright only)
├── .github/workflows/auto-deploy.yml  # CI/CD: test → deploy on push to main
├── tests/site-audit.spec.js        # Playwright test suite
├── scripts/                        # Python asset generation scripts (fal.ai)
├── venv_fal/                       # Python venv (gitignored)
├── assets/                         # Local asset copies (gitignored, 154MB - use S3)
├── logo.png                        # ISN.BIZ logo
├── docs/                           # 40+ historical documentation files
├── .serena/memories/               # Serena AI memory files (read these first)
└── .claude/                        # Compound engineering plugin (agents, commands, skills)
```

---

## How to Deploy

### Standard Workflow (CI/CD - Use This)

```bash
cd /d/workspace/ISNBIZ_Files
git add <specific files>
git commit -m "fix: description"
git push origin main
# GitHub Actions: runs Playwright tests → deploys to Netlify if tests pass
```

### Emergency Manual Deploy

```bash
npm install -g netlify-cli
netlify deploy --prod --dir=. \
  --auth=$NETLIFY_AUTH_TOKEN \
  --site=4d860499-0d6c-49cd-864f-69a0b7a2b3fe
```

### Verify Live Site

```bash
curl -I https://isn.biz

# Tailscale DNS bypass (needed on this Windows machine)
curl --resolve "isn.biz:443:104.21.18.246" -I https://isn.biz  # via Cloudflare
curl --resolve "isn.biz:443:75.2.60.5" -I https://isn.biz       # via Netlify
```

### Open Tasks Before Feature-Complete

**Critical:**
- [ ] Contact form backend (currently shows `alert()` - needs Netlify Forms or Formspree)

**High Priority:**
- [ ] Google Analytics 4 (no tracking yet - add GA4 ID to all 20 pages)
- [ ] reCAPTCHA on contact form (no spam protection)
- [ ] Alicia headshot regeneration (chin dimple AI artifact)

**Medium:**
- [ ] SpiritAtlas launch (update "Coming March 2026" badge)
- [ ] Privacy policy + Terms of service pages

**Full list:** See `.serena/memories/task_checklist.md`

---

## How to Update

### Change Content in a Page

Edit the relevant `.html` file directly. Key patterns:

```html
<!-- Hero stats -->
<div class="stat">
    <span class="stat-number">11+</span>
    <span class="stat-label">Years</span>
</div>

<!-- Card (MUST maintain 3xN or 4xN grid - CRITICAL RULE) -->
<div class="solution-card">
    <h3>AI-Powered Applications</h3>
    <p>Description...</p>
</div>
```

### Change Colors

Edit `styles.css` (CSS custom properties at top of file):

```css
:root {
    --color-blue: #1E9FF2;      /* Primary brand color */
    --color-cyan: #5FDFDF;      /* Secondary color */
    --color-charcoal: #0D1117;  /* Dark background */
    --accent-pink: #FF2D55;     /* Accent color */
}
```

### Add a New Page

1. Copy an existing similar page as a template
2. Update navigation links on ALL pages (not just the new one)
3. Add a clean URL redirect to `netlify.toml`
4. Add test coverage in `tests/site-audit.spec.js`
5. Commit and push - CI/CD handles deploy

### S3 Asset Management (Current Setup)

All production images served from S3 CDN (not local files):
- **S3 Bucket:** `isnbiz-assets-1769962280` (us-east-1)
- **URL pattern:** `https://isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com/assets/...`
- **Format:** WebP preferred for all images
- Local `assets/` folder is gitignored - do NOT commit it

```bash
# Upload a new asset to S3
aws s3 cp my-image.webp s3://isnbiz-assets-1769962280/assets/ --acl public-read

# Then reference in HTML:
# <img src="https://isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com/assets/my-image.webp" ...>
```

---

## Form Backend Setup

### Current State

JavaScript alert (placeholder):
```javascript
alert('Thank you! We will contact you soon.');
```

### Option 1: Formspree (Easiest)

```html
<form action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
  <!-- Existing form fields -->
</form>
```

- Free tier: 50 submissions/month
- Get YOUR_FORM_ID at: https://formspree.io/
- No backend code needed

### Option 2: Netlify Forms (If using Netlify)

```html
<form name="contact" method="POST" data-netlify="true" netlify-honeypot="bot-field">
  <input type="hidden" name="form-name" value="contact" />
  <!-- Existing form fields -->
</form>
```

- Included with Netlify hosting
- Built-in spam protection
- Email notifications

### Option 3: Custom Backend

```javascript
// Python Flask example
@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    # Send email, store in database, etc.
    return jsonify({'success': True})
```

---

## Important Commands

### Local Preview

```bash
cd /d/workspace/ISNBIZ_Files
python -m http.server 8000
# Open http://localhost:8000
```

### Run Tests

```bash
cd /d/workspace/ISNBIZ_Files
npx playwright test                          # All tests (vs https://isn.biz)
npx playwright test --ui                     # Interactive mode
BASE_URL=http://localhost:8000 npx playwright test  # Against local server
```

### Deploy (Standard)

```bash
cd /d/workspace/ISNBIZ_Files
git add <files>
git commit -m "Description"
git push origin main    # Auto-triggers tests → Netlify deploy
```

### Git Workflow

```bash
cd /d/workspace/ISNBIZ_Files
git status                     # Check changes
git log --oneline -5           # Recent commits
git diff                       # Unstaged changes
git push                       # Push (triggers CI/CD auto-deploy)
```

### Verify Live Site

```bash
curl -I https://isn.biz

# If Tailscale is overriding DNS (use on this machine):
curl --resolve "isn.biz:443:104.21.18.246" -I https://isn.biz
```

---

## Key Decisions Made

### Why Static HTML/CSS/JS?
- **Fast load times** - No framework overhead
- **SEO friendly** - Search engines love clean HTML
- **Easy to deploy** - Works anywhere
- **Low maintenance** - No backend dependencies
- **Cost effective** - Can host for free

### Why Netlify?
- **Easiest deployment** - Drag-and-drop or Git
- **Free SSL** - HTTPS included
- **CDN included** - Global distribution
- **Form handling** - No backend needed
- **Auto-deploy** - Push to Git = deploy

### Why Investor-Focused?
- **Clear CTAs** - Schedule Meeting, Request Pitch Deck
- **Professional design** - Dark investor section
- **Trust signals** - DUNS, UBI, EIN displayed
- **Measurable results** - Portfolio metrics shown
- **Mobile-first** - 70%+ investors on mobile

### Design Choices
- **Metallic backgrounds** - Professional, tech-forward
- **Blue/cyan colors** - Trust, technology, innovation
- **Minimal JavaScript** - Fast, accessible
- **Responsive design** - Works on all devices

---

## Where to Find Things

### Key Files

| What | Where |
|------|-------|
| HTML pages | `*.html` (20 files in root) |
| Main CSS | `styles.css` |
| Main JavaScript | `script.js` |
| Animation CSS | `enhanced-animations.css` |
| Netlify config + redirects | `netlify.toml` |
| CI/CD workflow | `.github/workflows/auto-deploy.yml` |
| Playwright tests | `tests/site-audit.spec.js` |
| Python asset scripts | `scripts/` |
| AI asset memories | `.serena/memories/` |
| Compound eng. plugin | `.claude/` (agents, commands, skills) |
| Historical docs | `docs/` (40+ markdown files) |

### Open Tasks & State

- **Task checklist:** `.serena/memories/task_checklist.md`
- **Deploy commands:** `.serena/memories/deploy_commands.md`
- **Live infra state:** `.serena/memories/website_state_2026_02_04.md`
- **External TODOs:** `DEPLOYMENT_GAPS.md` (GA4, form backend, etc.)

---

## Company Information

### ISN.BIZ Inc

**Legal:**
- **DUNS:** 080513772
- **UBI:** 603-522-339
- **EIN:** 47-4530188
- **Founded:** July 8, 2015
- **Type:** Software development company

**Focus:**
- AI-Powered Applications (Claude, GPT, Qwen)
- Cloud Solutions (AWS, Azure, scalable)
- Enterprise Software (custom business apps)
- Data Analytics (RAG, vector databases)

**Website:**
- **Live:** https://isn.biz (production, deployed Feb 2026)
- **Netlify:** https://isndotbiz.netlify.app

---

## Troubleshooting

### "Form not submitting"
- Check form backend is configured (Formspree/Netlify/custom)
- Test with browser console open for errors
- Verify action URL is correct

### "Images not loading"
- All production images are on S3 CDN (`isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com`)
- Check browser console for 404 errors
- Verify S3 URL is correct and file was uploaded with `--acl public-read`
- Local `assets/` folder is gitignored and not deployed

### "Mobile menu not working"
- Ensure `script.js` is loading
- Check browser console for JavaScript errors
- Test on actual mobile device, not just resize

### "Site looks different on mobile"
- Test on actual devices, not just browser resize
- Check CSS media queries (480px, 768px, 992px, 1200px)
- Use Chrome DevTools device emulation

### "Netlify deploy failed"
- Check build logs in Netlify dashboard
- Verify all files are committed to Git
- Ensure no large files (>100MB) in repo

---

## Related Documentation

**Workspace:**
- `/mnt/d/workspace/CLAUDE.md` - Workspace overview
- `/mnt/d/workspace/.serena/WEBSITES.md` - Website deployment details
- `/mnt/d/workspace/.serena/PROJECT_OVERVIEW.md` - Complete project context

**Infrastructure:**
- `/mnt/d/workspace/.serena/INFRASTRUCTURE.md` - Server options (Kusanagi)

**HROC Website (Reference):**
- `/mnt/d/workspace/HROC_Files/CLAUDE.md` - Similar project
- `/mnt/d/workspace/.serena/WEBSITES.md` - Shared infrastructure

---

## Serena & Memory Usage Guidelines

### Available Project Memories

This project uses Serena's memory system to preserve important knowledge. Current memories (as of 2026-02-25):

- **`project_overview`** - What this project is, tech stack, all 20 pages, critical rules
- **`website_state_2026_02_04`** - Live infrastructure state: URLs, Netlify, Cloudflare, S3, CI/CD
- **`deploy_commands`** - Full deployment procedures (CI/CD, manual, tests, asset generation)
- **`task_checklist`** - Open tasks, completed items, known issues
- **`suggested_commands`** - Dev, build, test, and deploy commands with examples
- **`codebase_structure`** - Detailed directory tree and file organization
- **`code_style_conventions`** - Team coding standards and patterns
- **`task_completion_workflow`** - Quality checklist for completing development tasks
- **`codex_handoff_2026_02_04`** - fal.ai settings, 9 projects list, image policy
- **`cloudflare_suspension_troubleshooting`** - How the domain suspension was resolved

### When to Automatically Read Memories

**Always read at conversation start:**
- `project_overview` - Provides essential context about the project

**Read when relevant to task:**
- Deployment mentioned → Read `deploy_commands` + `website_state_2026_02_04`
- Code changes → Read `code_style_conventions` + `codebase_structure`
- Troubleshooting live site → Read `website_state_2026_02_04`
- Task planning → Read `task_checklist`
- Workflow questions → Read `task_completion_workflow`
- Image generation → Read `codex_handoff_2026_02_04` (critical fal.ai settings)

### When to Write/Update Memories

**Automatically write after:**
- ✅ Solving major issues (document the problem + solution)
- ✅ Deployment changes (update `website_state_*`)
- ✅ Infrastructure changes (S3 buckets, server IPs, DNS)
- ✅ Learning important gotchas or patterns
- ✅ Completing multi-step tasks

**Memory naming convention:**
- Use snake_case: `cloudflare_troubleshooting`
- Include dates for snapshots: `website_state_2026_02_15`
- Be descriptive: `deployment_rollback_procedure` not just `rollback`

**Example scenarios:**
```
Scenario: Cloudflare domain suspended
→ After fix: Write "cloudflare_suspension_troubleshooting"
→ Content: What happened, why, how to fix, prevention

Scenario: New S3 bucket created
→ Update: "website_state_2026_02_04" or create new snapshot
→ Content: Bucket name, region, purpose, CDN config

Scenario: Deployment process changes
→ Update: "deploy_commands"
→ Content: New commands, removed steps, why changed
```

### When to Use Serena Code Tools

**Use Serena's semantic tools for:**
- 🔍 Finding specific functions/classes: `mcp__serena__find_symbol`
- 📊 Understanding file structure: `mcp__serena__get_symbols_overview`
- ✏️ Editing specific methods: `mcp__serena__replace_symbol_body`
- 🔗 Finding code references: `mcp__serena__find_referencing_symbols`
- 🔎 Pattern searching: `mcp__serena__search_for_pattern`

**Use standard Read/Edit tools for:**
- Reading non-code files (HTML, CSS, markdown)
- Simple text replacements
- Configuration files

### Critical Infrastructure Info (Always in Memories)

Keep these always documented in `website_state_*` memory:
- ✅ Live URLs (production, staging, CDN)
- ✅ Server IPs and locations
- ✅ S3 bucket names and regions
- ✅ Cloudflare zone IDs
- ✅ Netlify site names
- ✅ GitHub repository URLs
- ✅ Deployment status and last deploy date

---

## Common Tasks for Claude

### Update Company Stats

Edit `index.html` lines ~45-57:
```html
<div class="stat">
    <span class="stat-number">NEW_VALUE</span>
    <span class="stat-label">Label</span>
</div>
```

### Add Portfolio Item

Copy existing structure in `index.html` lines ~207-235:
```html
<div class="portfolio-item">
    <span class="portfolio-tag">Industry Tag</span>
    <h3>Project Title</h3>
    <p>Description of project and results...</p>
    <div class="portfolio-tech">
        <span>Tech 1</span>
        <span>Tech 2</span>
    </div>
    <div class="portfolio-metric">
        <strong>Metric:</strong> Result
    </div>
</div>
```

### Update Contact Information

Edit `index.html` line ~480:
```html
<p><strong>Email:</strong> new-email@isn.biz</p>
<p><strong>Phone:</strong> (XXX) XXX-XXXX</p>
```

### Add Analytics

Add before `</head>` in `index.html`:
```html
<!-- Google Analytics 4 -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

---

**Last Updated:** 2026-02-25
**Maintained by:** jdmal + Claude AI
**Status:** LIVE IN PRODUCTION at https://isn.biz

**Next priority:** Contact form backend + Google Analytics 4 (see `.serena/memories/task_checklist.md`)

## RAG Access

RAG system on TrueNAS (canonical reference: `True_Nas` repo, `docs/state/RAG-REFERENCE.md`).

| Context | URL |
|---------|-----|
| Tailscale | `http://100.67.89.29:8400` |
| LAN / Docker | `http://10.0.0.89:8400` |

**API Key:** `op://Research/RAG API Key/credential`
**Auth header:** `x-api-key: <key>` (lowercase)
**Response:** `{query, mode, count, duration_ms, results: [{id, collection, content, similarity, metadata}]}`

**MCP tools** (preferred in Claude Code):
- `mcp__rag__rag_search(query="...", collection="...")`
- `mcp__rag__rag_ingest(collection="...", documents=[...])`
- `mcp__rag__rag_collections()`

31 collections, 11,458 docs, all `mxbai-embed-large` 1024-dim.

## Canonical Stack Policy

- Read `docs/state/STACK_CANONICAL.md` before editing RAG/orchestrator configuration.
- Treat TrueNAS Apps as canonical data plane unless explicitly documented otherwise.
- Use `op://` references for secrets; never embed literal credentials.
