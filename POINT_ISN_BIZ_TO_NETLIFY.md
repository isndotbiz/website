# Point isn.biz to Netlify

## Quick Steps

### 1. Add Custom Domain in Netlify Dashboard

1. Go to: https://app.netlify.com/projects/isndotbiz/settings/domain-management
2. Click "Add custom domain"
3. Enter: `isn.biz`
4. Click "Verify" then "Add domain"
5. Also add: `www.isn.biz`

### 2. Update Cloudflare DNS

Run these commands (replace YOUR_CF_TOKEN with your Cloudflare API token):

```bash
# Sign into 1Password first
eval $(op signin)

# Get your Cloudflare token
CF_TOKEN=$(op item get "Cloudflare DNS Token (Current)" --vault "TrueNAS Infrastructure" --reveal --fields credential)

# Or manually set it:
# CF_TOKEN="your-cloudflare-api-token-here"

CF_ZONE="a2efe184e74443f824ef58f1c862eb5a"
RECORD_ID="6f99ae3f2e0d2d7b4f59e2a970aca302"

# Update isn.biz to point to Netlify (75.2.60.5)
curl -X PATCH "https://api.cloudflare.com/client/v4/zones/${CF_ZONE}/dns_records/${RECORD_ID}" \
  -H "Authorization: Bearer ${CF_TOKEN}" \
  -H "Content-Type: application/json" \
  --data '{"content":"75.2.60.5","proxied":false,"comment":"Pointing to Netlify"}'

# Add/Update www.isn.biz CNAME to Netlify
curl -X POST "https://api.cloudflare.com/client/v4/zones/${CF_ZONE}/dns_records" \
  -H "Authorization: Bearer ${CF_TOKEN}" \
  -H "Content-Type: application/json" \
  --data '{"type":"CNAME","name":"www","content":"isndotbiz.netlify.app","proxied":false}'
```

### 3. Or Do It Manually in Cloudflare Dashboard

1. Go to: https://dash.cloudflare.com
2. Select isn.biz zone
3. Go to DNS > Records
4. Edit the A record for `isn.biz`:
   - Change IP from `73.140.158.252` to `75.2.60.5`
   - Turn OFF proxy (grey cloud)
5. Add a CNAME for `www`:
   - Type: CNAME
   - Name: www
   - Target: isndotbiz.netlify.app
   - Proxy: OFF

### 4. Wait for SSL

After DNS propagates (5-15 minutes), Netlify will automatically provision an SSL certificate.

## Verify

```bash
# Check DNS propagation
dig isn.biz +short
# Should return: 75.2.60.5

# Check the site
curl -I https://isn.biz
# Should return 200 OK with Netlify headers
```

## Current Status

- Netlify site: https://isndotbiz.netlify.app ✅ (working)
- Custom domain: isn.biz ⏳ (needs DNS update)
- SSL: Will auto-provision after DNS update
