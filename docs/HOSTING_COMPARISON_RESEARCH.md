# ISN.BIZ Website Hosting Comparison Research

**Date:** 2026-02-04
**Purpose:** Comprehensive hosting comparison for investor-facing static website
**Current Setup:** TrueNAS/Kusanagi at 100.83.75.4
**Assets:** Already on S3 (isnbiz-assets-1769962280)

---

## Executive Summary

**Recommended Architecture:** Cloudflare Pages for production with TrueNAS for dev/staging

**Key Findings:**
- Cloudflare Pages offers the best value: unlimited bandwidth, 300+ edge locations, zero egress fees
- S3 assets should be served through Cloudflare CDN (free) rather than CloudFront (paid)
- TrueNAS/Kusanagi is excellent for internal dev/staging but not ideal for production investor site
- All modern platforms offer instant rollbacks and deploy previews

---

## Comparison Table

| Feature | TrueNAS/Kusanagi | Netlify | Cloudflare Pages | Vercel | GitHub Pages |
|---------|------------------|---------|------------------|--------|--------------|
| **Deploy Workflow** | Manual/SSH | Git push | Git push | Git push | Git push |
| **Deploy Complexity** | 4/5 (complex) | 1/5 (easy) | 1/5 (easy) | 1/5 (easy) | 2/5 (easy) |
| **CDN Locations** | 1 (self) | ~15+ | 300+ | 100+ | Limited |
| **Uptime SLA** | Self-managed | 99.99% (Enterprise) | N/A (highly reliable) | 99.99% (Enterprise) | N/A |
| **Free SSL** | Let's Encrypt (manual) | Automatic | Automatic | Automatic | Automatic |
| **DDoS Protection** | None built-in | Basic | Enterprise-grade | Basic | Basic |
| **Rollback** | Manual (backups) | Instant (any deploy) | Instant (any deploy) | Instant (any deploy) | Via Git revert |
| **Deploy Previews** | None | Yes (PR-based) | Yes (PR-based) | Yes (PR-based) | None |
| **Form Handling** | Custom backend | Built-in (100 free) | Workers (requires code) | None built-in | None |
| **Custom Domain** | Full control | Yes (free) | Yes (free) | Yes (free) | Yes (free) |
| **Free Bandwidth** | Unlimited (your cost) | 100GB/mo | Unlimited | 100GB/mo | 100GB/mo (soft) |
| **Free Builds** | N/A | 300 min/mo | 500/mo | N/A | N/A |
| **Paid Starts At** | Self-hosted cost | $19/mo | $5/mo (Workers) | $20/mo | Free only |
| **CI/CD Integration** | Manual | GitHub, GitLab, Bitbucket | GitHub, GitLab | GitHub, GitLab | GitHub only |
| **S3 CDN Integration** | Reverse proxy | Via DNS | Native (best) | Via DNS | N/A |

### Scoring Summary (1-10, higher is better)

| Criteria | TrueNAS | Netlify | Cloudflare | Vercel | GitHub Pages |
|----------|---------|---------|------------|--------|--------------|
| Ease of Deploy | 4 | 9 | 9 | 9 | 7 |
| Performance/CDN | 3 | 7 | 10 | 8 | 5 |
| Reliability | 6 | 8 | 10 | 9 | 7 |
| Security | 5 | 7 | 10 | 7 | 6 |
| Rollback/Recovery | 4 | 9 | 9 | 9 | 6 |
| Cost (Free Tier) | 6 | 8 | 10 | 7 | 10 |
| Form Handling | 3 | 9 | 5 | 3 | 2 |
| S3 Integration | 4 | 6 | 10 | 6 | 2 |
| **TOTAL** | **35/80** | **63/80** | **73/80** | **58/80** | **45/80** |

---

## Detailed Analysis

### 1. TrueNAS/Kusanagi (Current: 100.83.75.4)

**Overview:** Self-hosted solution running Kusanagi (WordPress-optimized VM stack) on TrueNAS.

**Pros:**
- Full control over infrastructure
- No external dependencies
- Can run complex backend applications
- Good for internal/private staging
- No monthly hosting fees (just electricity/hardware)

**Cons:**
- Single point of failure (no CDN)
- Manual SSL certificate management
- No automatic rollback capability
- No deploy previews
- Requires maintenance and updates
- Not suitable for global investors (latency)
- DDoS vulnerable without additional protection
- ISP outage = site down

**Best For:** Development, staging, internal tools

**NOT Recommended For:** Production investor-facing site

---

### 2. Netlify

**Overview:** Pioneer in Jamstack hosting with excellent DX and built-in features.

**Pros:**
- Industry-standard for static sites
- Built-in form handling (100 submissions free)
- Instant rollbacks to any previous deploy
- Automatic deploy previews on PRs
- Excellent documentation and community
- Identity/auth features available
- Plugin ecosystem

**Cons:**
- Free tier limited to 100GB bandwidth
- Form handling costs add up quickly
- Slower cold starts for serverless functions (3+ seconds)
- Recent pricing changes (Sept 2025)
- CDN not as extensive as Cloudflare

**Pricing:**
- Free: 100GB bandwidth, 300 build minutes, 100 form submissions
- Pro: $19/member/month
- Enterprise: Custom pricing, 99.99% SLA

**Best For:** Teams wanting built-in forms and identity

---

### 3. Cloudflare Pages (RECOMMENDED)

**Overview:** Leverages Cloudflare's massive global network (300+ edge locations).

**Pros:**
- **Unlimited bandwidth (free tier)**
- **300+ edge locations worldwide**
- **Enterprise-grade DDoS protection included**
- Fastest cold starts among competitors
- Native integration with Cloudflare CDN for S3 assets
- Zero egress fees
- Bot protection and security features
- Instant rollbacks
- Deploy previews
- $5/month Workers plan unlocks serverless

**Cons:**
- No built-in form handling (need Workers or external service)
- 500 builds/month on free tier
- Less ecosystem/plugins than Netlify
- No publicly stated SLA for Pages specifically

**Pricing:**
- Free: Unlimited sites, unlimited bandwidth, 500 builds/month
- Workers Paid: $5/month (serverless functions)
- Pro: $20/month (additional features)

**Best For:** Global performance, cost optimization, security-first

---

### 4. Vercel

**Overview:** Optimized for Next.js and React applications.

**Pros:**
- Best-in-class Next.js support
- Excellent developer experience
- Fast deployments (~30 seconds)
- Good preview URL system
- Automatic optimizations

**Cons:**
- Free tier prohibits commercial use
- 100GB bandwidth limit
- Expensive overages ($0.15/GB)
- Unpredictable costs at scale
- Overkill for static HTML site
- No form handling

**Pricing:**
- Hobby (Free): 100GB bandwidth, non-commercial only
- Pro: $20/user/month
- Enterprise: $20-25K+/year

**Best For:** Next.js applications, not simple static sites

---

### 5. GitHub Pages

**Overview:** Free hosting directly from GitHub repositories.

**Pros:**
- Completely free for public repos
- Automatic SSL via Let's Encrypt
- Direct Git integration
- Version control built-in
- Simple for basic sites

**Cons:**
- No deploy previews
- No built-in forms
- 100GB soft bandwidth limit
- 1GB repo size limit
- No serverless functions
- Limited CDN
- Build timeout limits
- Public repos only (free)

**Pricing:**
- Free: Public repositories
- Paid GitHub required for private repos

**Best For:** Open-source projects, documentation, personal sites

---

## CDN Strategy for S3 Assets

### Current Setup
- Assets on S3: `isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com`
- Currently referenced directly from HTML

### Recommended: Cloudflare CDN in Front of S3

**Why Cloudflare over CloudFront:**

| Factor | Cloudflare | CloudFront |
|--------|------------|------------|
| Cost | Free (unlimited bandwidth) | $0.085/GB first 10GB |
| Edge Locations | 335 cities, 125+ countries | 100+ cities, 50+ countries |
| DDoS Protection | Enterprise-grade (free) | Additional cost |
| Setup Complexity | Simple DNS change | AWS configuration |
| S3 Egress | Pay S3 egress (~$0.09/GB) | Free if S3 origin |

**Recommended Setup:**

1. **Create Cloudflare account** (free)
2. **Add custom subdomain for assets:** `assets.isn.biz`
3. **Configure DNS CNAME:**
   ```
   assets.isn.biz -> isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com
   ```
4. **Enable Cloudflare proxy** (orange cloud)
5. **Set SSL mode to "Full"**
6. **Configure cache rules:**
   - Images: 1 year cache
   - Other assets: 1 month cache
7. **Update HTML references:**
   ```html
   <!-- From -->
   <img src="https://isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com/...">
   <!-- To -->
   <img src="https://assets.isn.biz/...">
   ```

**Benefits:**
- Cache hit = zero S3 egress cost
- 300+ edge locations for global delivery
- Professional branding (assets.isn.biz vs S3 URL)
- DDoS protection for assets
- Future flexibility (can change origin without URL changes)

---

## Recommended Architecture

### Three-Tier Environment

```
                                    PRODUCTION
                                    ┌─────────────────────────────────────┐
                                    │     Cloudflare Pages (isn.biz)      │
          Investors                 │  - 300+ edge locations              │
          ───────────────────────►  │  - DDoS protection                  │
          Global                    │  - Instant rollbacks                │
                                    │  - Unlimited bandwidth              │
                                    └─────────────────────────────────────┘
                                                      │
                                                      │ Git push to main
                                                      │
                                    STAGING           ▼
                                    ┌─────────────────────────────────────┐
          QA / Internal             │   Cloudflare Pages (Preview URLs)   │
          ───────────────────────►  │  - Automatic on PR creation         │
          Testing                   │  - Unique URL per branch            │
                                    │  - Same infrastructure as prod      │
                                    └─────────────────────────────────────┘
                                                      │
                                                      │ PR merge
                                                      │
                                    DEVELOPMENT       ▼
                                    ┌─────────────────────────────────────┐
          Developers                │   TrueNAS/Kusanagi (100.83.75.4)    │
          ───────────────────────►  │  - Local development                │
          Local Network             │  - Heavy experiments                │
                                    │  - Database-backed features         │
                                    │  - No public exposure               │
                                    └─────────────────────────────────────┘


                                    CDN FOR ASSETS
                                    ┌─────────────────────────────────────┐
                                    │  Cloudflare CDN (assets.isn.biz)    │
          All Environments          │        ┌──────────────────┐         │
          ───────────────────────►  │        │ S3 Origin        │         │
                                    │        │ isnbiz-assets-*  │         │
                                    │        └──────────────────┘         │
                                    └─────────────────────────────────────┘
```

### Workflow

1. **Development:**
   - Code locally, push to feature branch
   - Test on TrueNAS if needed for complex features

2. **Staging/Preview:**
   - Create PR to main branch
   - Cloudflare Pages automatically creates preview URL
   - Share preview with stakeholders for approval

3. **Production:**
   - Merge PR to main
   - Cloudflare Pages automatically deploys
   - Instant rollback available if issues

---

## Form Handling Strategy

Since Cloudflare Pages doesn't include built-in forms, choose one:

### Option A: Formspree (Recommended for Simplicity)

```html
<form action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
  <input type="text" name="name" required>
  <input type="email" name="email" required>
  <textarea name="message" required></textarea>
  <button type="submit">Send</button>
</form>
```

- Free: 50 submissions/month
- Paid: $10/month for 1,000 submissions
- No backend code needed
- Spam protection included

### Option B: Cloudflare Workers

```javascript
// Worker function to handle form submission
export default {
  async fetch(request) {
    if (request.method === 'POST') {
      const formData = await request.formData();
      // Process and send to email/database
      return new Response('Thank you!', { status: 200 });
    }
    return new Response('Method not allowed', { status: 405 });
  }
}
```

- Requires Workers Paid ($5/month)
- Full control over processing
- Can integrate with any backend

### Option C: Static Forms

- 500 free submissions/month
- $9/month for 25,000 submissions
- Better value than Netlify Forms

---

## Monitoring Integration

### Cloudflare Pages Analytics (Built-in)

- Page views and unique visitors
- Top pages and referrers
- Geographic distribution
- Real User Metrics (RUM)

### Additional Monitoring Options

| Tool | Purpose | Cost |
|------|---------|------|
| Cloudflare Web Analytics | Free privacy-focused analytics | Free |
| Google Analytics 4 | Detailed visitor tracking | Free |
| Uptime Robot | Uptime monitoring | Free (50 monitors) |
| BetterUptime | Uptime + incident management | Free tier available |
| Sentry | Error tracking | Free tier (5K errors/mo) |

### Recommended Setup

```html
<!-- Cloudflare Web Analytics (privacy-focused) -->
<script defer src='https://static.cloudflareinsights.com/beacon.min.js'
        data-cf-beacon='{"token": "YOUR_TOKEN"}'></script>

<!-- Google Analytics 4 (detailed tracking) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXX');
</script>
```

### Uptime Monitoring

```bash
# Set up with BetterUptime or Uptime Robot
# Monitor: https://isn.biz
# Check interval: 1 minute
# Alert via: Email, Slack, SMS
```

---

## Migration Steps: TrueNAS to Cloudflare Pages

### Phase 1: Setup (30 minutes)

1. **Create Cloudflare account**
   - Go to https://pages.cloudflare.com/
   - Sign up with email

2. **Connect Git repository**
   ```bash
   cd D:\workspace\ISNBIZ_Files
   git remote -v  # Verify GitHub remote
   ```
   - In Cloudflare Pages, click "Create a project"
   - Select "Connect to Git"
   - Authorize GitHub access
   - Select `ISNBIZ_Files` repository

3. **Configure build settings**
   - Build command: (leave blank - static HTML)
   - Output directory: `/` (or `.`)
   - Root directory: (leave blank)

4. **Deploy**
   - Click "Save and Deploy"
   - Wait for initial deployment (~1 minute)
   - Note the temporary URL: `isnbiz-files.pages.dev`

### Phase 2: Custom Domain (15 minutes)

1. **Add isn.biz domain to Cloudflare**
   - Go to Cloudflare dashboard
   - Add site: isn.biz
   - Update nameservers at registrar

2. **Configure Pages custom domain**
   - In Pages project settings
   - Custom domains > Add custom domain
   - Enter: `isn.biz` and `www.isn.biz`

3. **Verify SSL**
   - Cloudflare automatically provisions SSL
   - Test: `https://isn.biz`

### Phase 3: CDN for S3 Assets (15 minutes)

1. **Add subdomain for assets**
   - In Cloudflare DNS
   - Add CNAME: `assets` -> `isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com`
   - Enable proxy (orange cloud)

2. **Update HTML references**
   - Find/replace S3 URLs with assets.isn.biz
   - Commit and push changes

3. **Configure cache rules**
   - Page Rules or Cache Rules
   - `assets.isn.biz/*`: Cache Everything, Edge TTL: 1 month

### Phase 4: Form Setup (10 minutes)

1. **Create Formspree account**
   - Go to https://formspree.io/
   - Create new form

2. **Update contact form**
   ```html
   <form action="https://formspree.io/f/YOUR_ID" method="POST">
   ```

3. **Test submission**

### Phase 5: Monitoring (10 minutes)

1. **Enable Cloudflare Web Analytics**
   - In Cloudflare dashboard
   - Analytics & Logs > Web Analytics
   - Add site

2. **Set up uptime monitoring**
   - Create Uptime Robot account
   - Add monitor for https://isn.biz

### Phase 6: Decommission TrueNAS Production (Optional)

1. **Update DNS to remove old records**
2. **Keep TrueNAS for dev/staging**
3. **Document new architecture**

---

## Final Recommendation

### Primary Recommendation: Cloudflare Pages

**Why Cloudflare Pages is the best choice for ISN.BIZ:**

1. **Cost Efficiency**
   - Unlimited bandwidth (free)
   - Zero egress fees
   - Native S3 CDN integration (free)
   - Total cost: $0-5/month

2. **Performance**
   - 300+ edge locations (more than any competitor)
   - Fastest cold starts
   - Enterprise-grade infrastructure

3. **Security**
   - Enterprise DDoS protection (free)
   - Bot mitigation
   - Automatic SSL
   - No exposed origin server

4. **Developer Experience**
   - Git-based deployments
   - Automatic preview URLs
   - Instant rollbacks
   - Simple configuration

5. **Investor Confidence**
   - Professional infrastructure backing
   - Global availability
   - High reliability track record

### Alternative: Netlify

**Choose Netlify if:**
- Built-in form handling is critical
- You need Netlify Identity features
- Team prefers Netlify's ecosystem/plugins

### Keep TrueNAS/Kusanagi For:

- Local development
- Internal staging
- Database-backed experiments
- Private/internal tools
- Heavy computational tasks

---

## Cost Summary

### Cloudflare Pages (Recommended)

| Item | Cost |
|------|------|
| Cloudflare Pages | $0 (free) |
| Cloudflare CDN for S3 | $0 (free) |
| S3 Storage | ~$2-5/month |
| S3 Egress (with CF cache) | ~$1-2/month |
| Formspree (forms) | $0-10/month |
| **Total** | **$3-17/month** |

### Current TrueNAS Self-Hosted

| Item | Cost |
|------|------|
| Electricity | ~$20-50/month |
| Hardware depreciation | ~$50/month |
| Time/maintenance | ~$100/month (opportunity cost) |
| S3 direct egress | ~$5-20/month |
| **Total** | **$175-220/month** |

### Savings: ~$160-200/month by switching to Cloudflare Pages

---

## References

### Sources Used

- [Vercel vs Netlify vs Cloudflare Pages Comparison](https://www.digitalapplied.com/blog/vercel-vs-netlify-vs-cloudflare-pages-comparison)
- [Bejamas Platform Comparison](https://bejamas.com/compare/cloudflare-pages-vs-netlify-vs-vercel)
- [Cloudflare Pages Pricing](https://developers.cloudflare.com/pages/functions/pricing/)
- [Netlify Pricing](https://www.netlify.com/pricing/)
- [Vercel Pricing](https://vercel.com/pricing)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Cloudflare CDN with S3 Setup](https://dev.to/joelnet/how-i-setup-my-own-personal-cdn-3h06)
- [CloudFront vs Cloudflare CDN Comparison](https://dev.to/clickit_devops/cloudfront-vs-cloudflare-choosing-the-right-cdn-39jk)
- [10 Best Static Website Hosting Providers 2026](https://crystallize.com/blog/static-hosting)
- [Serverless Cold Starts Comparison](https://punits.dev/blog/vercel-netlify-cloudflare-serverless-cold-starts/)
- [TrueNAS Web Hosting Community](https://www.truenas.com/community/threads/web-hosting-on-truenas-scale.99040/)

---

**Document Created:** 2026-02-04
**Author:** Claude AI
**Status:** Ready for review and implementation
