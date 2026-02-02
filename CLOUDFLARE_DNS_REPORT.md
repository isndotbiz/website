# Cloudflare DNS Configuration Report for ISN.BIZ

**Generated:** 2026-02-02
**Domain:** isn.biz
**Zone ID:** a2efe184e74443f824ef58f1c862eb5a

---

## Zone Information

| Field | Value |
|-------|-------|
| **Domain** | isn.biz |
| **Status** | ACTIVE |
| **Plan** | Free Website (no cost) |
| **Type** | Full (Cloudflare nameservers) |
| **Paused** | No |
| **Development Mode** | Disabled |
| **Created** | 2025-12-09 06:42:44 UTC |
| **Activated** | 2025-12-09 06:57:14 UTC |
| **Last Modified** | 2026-01-26 10:31:51 UTC |

---

## Nameservers

### Active (Cloudflare)
- `kianchau.ns.cloudflare.com`
- `monika.ns.cloudflare.com`

### Original (GoDaddy)
- `ns56.domaincontrol.com`
- `ns55.domaincontrol.com`

**Status:** Successfully migrated from GoDaddy to Cloudflare DNS

---

## Primary A Records - Root & WWW

### isn.biz (Root Domain)
```
Type:          A Record
Content:       73.140.158.252 (WAN IP)
Proxied:       NO (DNS only - gray cloud)
TTL:           1 (Automatic)
Created:       2025-12-09 06:42:47 UTC
Modified:      2026-02-02 07:56:05 UTC ⚠️ TODAY
```

### www.isn.biz
```
Type:          A Record
Content:       73.140.158.252 (WAN IP)
Proxied:       NO (DNS only - gray cloud)
TTL:           1 (Automatic)
Created:       2025-12-09 06:42:47 UTC
Modified:      2026-02-02 07:56:06 UTC ⚠️ TODAY
```

**Critical Finding:** Both records were modified TODAY with proxied status set to `false`. This means the investor website (isn.biz) is NOT behind Cloudflare protection.

---

## Internal Network Records

### 1pass.isn.biz
```
Type:          A Record
Content:       10.0.0.89 (TrueNAS internal)
Proxied:       NO
TTL:           300
Created:       2026-02-02 02:11:37 UTC
```

### rag.isn.biz (⚠️ DUPLICATE RECORDS - CONFLICTING)

**Record 1:**
```
Type:          A Record
Content:       10.0.0.89 (TrueNAS internal)
Proxied:       NO
TTL:           1
Created:       2026-01-25 13:35:16 UTC
```

**Record 2 (CONFLICTING):**
```
Type:          A Record
Content:       73.140.158.252 (WAN IP)
Proxied:       YES (orange cloud)
TTL:           1
Created:       2025-12-29 07:44:32 UTC
```

**ISSUE:** Two conflicting records for rag.isn.biz can cause DNS resolution problems. One points to internal (10.0.0.89), the other to external (73.140.158.252).

---

## Services Behind Cloudflare Proxy (Orange Cloud)

The following 20 subdomains are proxied through Cloudflare (protected, accelerated):

1. alertmanager.isn.biz
2. cadvisor.isn.biz
3. claude.isn.biz
4. dolphin.isn.biz
5. flowise.isn.biz
6. grafana.isn.biz
7. langfuse.isn.biz
8. litellm.isn.biz
9. llama.isn.biz
10. media.isn.biz
11. n8n.isn.biz
12. openwebui.isn.biz
13. portainer.isn.biz
14. prometheus.isn.biz
15. pushgateway.isn.biz
16. security.isn.biz
17. studio.isn.biz
18. supabase.isn.biz
19. tavern.isn.biz
20. traefik.isn.biz

**All point to:** 73.140.158.252 (WAN IP)
**All have TTL:** 1 (Automatic)

---

## Services NOT Behind Cloudflare (Gray Cloud - DNS Only)

The following records are DNS-only (NO Cloudflare protection/acceleration):

- **isn.biz** (root domain) - 73.140.158.252
- **www.isn.biz** - 73.140.158.252
- **nas.isn.biz** - 73.140.158.252
- **router.isn.biz** - 73.140.158.252
- **1pass.isn.biz** - 10.0.0.89 (internal)
- **rag.isn.biz** - 10.0.0.89 (internal, one of two records)

---

## Mail Configuration

### MX Records
```
isn.biz → mx01.mail.icloud.com (priority: 10)
isn.biz → mx02.mail.icloud.com (priority: 10)
```

### DKIM
```
sig1._domainkey.isn.biz → sig1.dkim.isn.biz.at.icloudmailadmin.com
```

### SPF
```
v=spf1 include:icloud.com ~all
```

**Email Status:** ✓ Configured for iCloud email hosting

---

## SSL/TLS Certificate Status

### ACME Challenge Records (Let's Encrypt)
- _acme-challenge.alertmanager.isn.biz
- _acme-challenge.grafana.isn.biz
- _acme-challenge.isn.biz
- _acme-challenge.llama.isn.biz
- _acme-challenge.prometheus.isn.biz
- _acme-challenge.rag.isn.biz
- _acme-challenge.traefik.isn.biz
- _acme-challenge.www.isn.biz

**Status:** ✓ Active SSL/TLS certificates with Let's Encrypt

### Domain Verification
```
apple-domain=X0gx3mprPd7m6M3H
```

---

## CNAME Records

### auth.isn.biz
```
Type:    CNAME
Target:  isn.biz
Proxied: YES (orange cloud)
TTL:     1
Created: 2026-01-21 03:51:16 UTC
```

---

## DNS Summary

| Metric | Value |
|--------|-------|
| **Total Records** | 41 |
| **A Records** | 27 |
| **CNAME Records** | 2 |
| **MX Records** | 2 |
| **TXT Records** | 10 |

---

## Critical Findings

### 1. ⚠️ Duplicate RAG.ISN.BIZ Records
Two conflicting A records exist for rag.isn.biz:
- 10.0.0.89 (internal TrueNAS, not proxied)
- 73.140.158.252 (external WAN IP, proxied via Cloudflare)

**Impact:** DNS resolution unpredictable - clients may get either response

**Action Needed:** Delete one record. Decide:
- Option A: Keep 10.0.0.89 (internal access only) → DELETE 73.140.158.252
- Option B: Keep 73.140.158.252 (external access) → DELETE 10.0.0.89

---

### 2. ⚠️ Investor Website NOT Protected
**Root domain (isn.biz) is NOT behind Cloudflare proxy**

Current Setup:
- ✓ Points to correct IP: 73.140.158.252
- ✗ Proxied: NO (gray cloud)
- ✗ No Cloudflare DDoS protection
- ✗ No Web Application Firewall (WAF)
- ✗ No CDN acceleration
- ✗ No caching optimization

Missing Benefits:
- DDoS attack protection
- Web Application Firewall rules
- Global CDN for faster load times
- Automatic caching
- Bot management
- Rate limiting

**Recommendation:** Enable Cloudflare proxy (orange cloud) for isn.biz

---

### 3. ⚠️ WWW Subdomain NOT Protected
**www.isn.biz is also NOT behind Cloudflare proxy**

Same issues as root domain. Both should be proxied together.

---

### 4. 🔍 Recent Changes Today
Both isn.biz and www.isn.biz were modified on **2026-02-02**:
- isn.biz: 07:56:05 UTC
- www.isn.biz: 07:56:06 UTC

Both changes set `proxied: false`, disabling Cloudflare protection.

**Questions:**
- Was this intentional?
- Was it accidental?
- Should protection be re-enabled?

---

### 5. 🔐 Internal Network Exposure
The following internal IPs are exposed via DNS:
- 1pass.isn.biz → 10.0.0.89 (TrueNAS)
- rag.isn.biz → 10.0.0.89 (TrueNAS)

**Good News:** These only resolve on internal network (10.0.0.0/24 LAN)
**Security:** Isolation is working as designed

---

## Account & Plan Information

| Setting | Value |
|---------|-------|
| **Account** | Jdmallin25x40@gmail.com's Account |
| **Plan** | Free Website |
| **Cost** | $0/month |
| **Custom Certificates Quota** | 0 |
| **Page Rules** | 3 available |
| **Phishing Detected** | No |

---

## Recommendations

### IMMEDIATE (Critical Priority)

1. **Resolve duplicate rag.isn.biz records**
   - Two conflicting A records exist
   - Can cause unpredictable DNS resolution
   - **Action:** Delete one, keep the other
   - **Urgency:** HIGH

2. **Enable Cloudflare proxy for isn.biz**
   - Currently DNS-only (gray cloud)
   - Investor website has no DDoS/WAF protection
   - **Action:** Change proxied status to YES (orange cloud)
   - **Urgency:** HIGH (production website)

3. **Enable Cloudflare proxy for www.isn.biz**
   - Currently DNS-only (gray cloud)
   - Should match root domain proxy status
   - **Action:** Change proxied status to YES
   - **Urgency:** HIGH

### MEDIUM PRIORITY

4. **Review proxy status changes**
   - Both isn.biz and www.isn.biz changed TODAY
   - Understand if this was intentional
   - Document the reason for the change

5. **Review NAS and router proxy status**
   - nas.isn.biz and router.isn.biz currently not proxied
   - Consider security implications
   - Decide if they should be proxied or remain DNS-only

6. **Review internal network exposure**
   - 1pass.isn.biz and rag.isn.biz expose internal IPs
   - Only accessible from LAN (good isolation)
   - Consider if this is intentional

### MONITORING

7. **Set up DNS monitoring**
   - Monitor for unexpected DNS changes
   - Alert on duplicate records
   - Track proxy status changes

8. **Review Cloudflare analytics**
   - Once proxy is enabled, monitor traffic
   - Check DDoS attack notifications
   - Review WAF activity

9. **Certificate renewal monitoring**
   - ACME challenges are active
   - Monitor Let's Encrypt certificate renewal
   - Ensure all subdomains maintain valid certs

---

## How to Make Changes

### Enable Proxy for isn.biz

1. Go to Cloudflare Dashboard: https://dash.cloudflare.com/
2. Select domain: isn.biz
3. Go to DNS tab
4. Find "isn.biz" A record (73.140.158.252)
5. Click the icon next to it to toggle proxy (gray ☁️ → orange ☁️)
6. Save

OR via API:
```bash
curl -X PATCH https://api.cloudflare.com/client/v4/zones/a2efe184e74443f824ef58f1c862eb5a/dns_records/6f99ae3f2e0d2d7b4f59e2a970aca302 \
  -H "Authorization: Bearer TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"proxied": true}'
```

### Delete Duplicate rag.isn.biz Record

Option 1: Web Dashboard
1. Cloudflare Dashboard → isn.biz → DNS
2. Find the duplicate rag.isn.biz record
3. Click delete (trash icon)

Option 2: API
```bash
# Delete the conflicting external record (73.140.158.252)
curl -X DELETE https://api.cloudflare.com/client/v4/zones/a2efe184e74443f824ef58f1c862eb5a/dns_records/3375647e36332df4bfea8a348a9b289d \
  -H "Authorization: Bearer TOKEN"
```

---

## Additional Notes

- **Registrar:** GoDaddy (migration was successful)
- **Email Provider:** iCloud
- **Free Plan Limitations:**
  - No custom SSL certificates
  - Limited page rules (3)
  - Basic security features only
- **Upgrade Options:** Consider Business plan for WAF, advanced DDoS, etc.

---

**Last Updated:** 2026-02-02
**Report Status:** Action items identified
**API Token Used:** Cloudflare DNS Token (Current)
