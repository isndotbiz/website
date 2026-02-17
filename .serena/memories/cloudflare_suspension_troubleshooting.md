# Cloudflare Domain Suspension - Troubleshooting Guide

**Date:** 2026-02-15
**Domain:** isn.biz
**Issue:** ToS violation suspension at Cloudflare Registrar level

---

## What Happened

User tried to access `https://isn.biz` and received:
- **Cloudflare Registrar suspension page**
- Page loaded from: `parking.registrar.cloudflare.com/assets/suspended.js`
- Error shown in dashboard: *"The registrar services for this domain have been suspended by Cloudflare for a Terms of Service violation."*

## What Was NOT the Problem

- ✅ Website files were fine (working on Netlify at `isndotbiz.netlify.app`)
- ✅ DNS records were correct (A record pointing to Netlify IP: 75.2.60.5)
- ✅ Cloudflare DNS zone was active (not suspended)
- ✅ No billing/payment issues

## Root Cause

**Registrar-level suspension** - not DNS or hosting issue.
- Domain registered with Cloudflare Registrar (transferred from GoDaddy)
- Cloudflare flagged domain for Terms of Service violation
- Suspension happened at registration level, overriding all DNS settings

## Potential Triggers

The domain has 25+ subdomains running AI/LLM tools and services:
- `openwebui.isn.biz` - AI chat interfaces
- `flowise.isn.biz` - LLM workflow tools  
- `tavern.isn.biz` - AI chat
- `langfuse.isn.biz` - LLM observability
- `portainer.isn.biz` - Container management
- `grafana.isn.biz` - Monitoring dashboards
- Plus many others...

Possible violation triggers:
- AI/LLM tool abuse (if publicly accessible)
- Heavy API usage from AI tools
- Security scanner false positive
- Automated ToS enforcement system flagged activity

## Resolution

**User resolved with Cloudflare support directly.**
- Required human intervention (API cannot fix ToS violations)
- User contacted Cloudflare support via dashboard
- Issue was resolved (exact resolution details not documented)

## How to Diagnose in Future

1. **Check if site loads on Netlify directly:**
   ```
   https://isndotbiz.netlify.app
   ```
   If this works, issue is domain-level, not hosting.

2. **Verify DNS zone status via API:**
   ```bash
   curl -X GET "https://api.cloudflare.com/client/v4/zones?name=isn.biz" \
     -H "Authorization: Bearer {DNS_TOKEN}"
   ```
   Check: `"status": "active"` and `"paused": false`

3. **Check what page isn.biz shows:**
   ```bash
   curl -s https://isn.biz | grep -E "(title|suspended|parking)"
   ```
   If shows "Cloudflare Registrar" + "suspended.js" → Registrar suspension

4. **Check DNS resolution:**
   ```bash
   nslookup isn.biz
   ```
   Should resolve to Netlify IP (75.2.60.5), not Cloudflare proxy IPs

## How to Fix

### Step 1: Log into Cloudflare Dashboard
- **URL:** https://dash.cloudflare.com/
- **Email:** jdm@isn.biz  
- **Password:** In 1Password under "Cloudflare"

### Step 2: Check Registrar Section
- Go to **Domain Registration** → **Manage Domains**
- Find `isn.biz` and check suspension notice
- Read the specific ToS violation reason

### Step 3: Contact Support
- Click **"Help"** → **"Contact Support"**
- Select: **"Domain Registration"** → **"Suspension Appeal"**
- Ask for specific violation details
- Provide any requested information

### Step 4: Temporary Workaround (While Suspended)
- Use Netlify URL directly: `https://isndotbiz.netlify.app`
- Share this with investors/users temporarily
- Or transfer domain back to GoDaddy if Cloudflare won't reinstate

## Prevention

1. **Monitor subdomain usage** - Ensure AI tools aren't abused
2. **Secure all services** - Don't leave admin panels public
3. **Monitor traffic** - Watch for unusual spikes
4. **Keep WHOIS updated** - Ensure business verification is current
5. **Respond to abuse reports** - If Cloudflare emails, act immediately

## Key Credentials

**Cloudflare Login:**
- 1Password: "Cloudflare" in "TrueNAS Infrastructure" vault
- Contains: Email, Password, Global API Key, DNS Token

**Cloudflare Zone ID:** `a2efe184e74443f824ef58f1c862eb5a`

## Related Files

- `CLAUDE.md` - Project instructions (line 527+ has memory guidelines)
- `website_state_2026_02_04` - Deployment state before issue
- `deploy_commands` - Normal deployment procedures

---

**Status:** ✅ Resolved 2026-02-15 (user fixed via Cloudflare support)
**Documented by:** Claude Sonnet 4.5 (following new memory guidelines)
