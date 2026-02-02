# ISN.BIZ SSL Certificate Monitoring Guide

## Quick Status Check

### Current Certificate Status (As of 2026-02-02)

| Property | Value |
|----------|-------|
| **Issuer** | Let's Encrypt (R13) |
| **Domains Covered** | isn.biz, www.isn.biz |
| **Protocol** | TLS 1.3 |
| **Cipher** | TLS_AES_128_GCM_SHA256 |
| **Validity** | Jan 26, 2026 - Apr 26, 2026 |
| **Days Remaining** | 82 days |
| **Status** | ✓ Valid and Trusted |

---

## Verification Commands

### Check Certificate Status (Quick)

```bash
# Check isn.biz certificate
openssl s_client -connect isn.biz:443 -servername isn.biz </dev/null 2>/dev/null | openssl x509 -noout -dates

# Check www.isn.biz certificate
openssl s_client -connect www.isn.biz:443 -servername www.isn.biz </dev/null 2>/dev/null | openssl x509 -noout -dates
```

### Check Full Certificate Details

```bash
# Get all certificate information
openssl s_client -connect isn.biz:443 -servername isn.biz </dev/null 2>/dev/null | openssl x509 -noout -text
```

### Verify Certificate Chain

```bash
# Verify certificate chain is complete
openssl s_client -connect isn.biz:443 -servername isn.biz </dev/null 2>/dev/null | grep "Verify return code"

# Expected output: "Verify return code: 0 (ok)"
```

### Check TLS Protocol Version

```bash
# Verify TLS 1.3 is in use
openssl s_client -connect isn.biz:443 -servername isn.biz </dev/null 2>/dev/null | grep "Protocol"

# Expected output: "Protocol  : TLSv1.3"
```

---

## Monitoring Checklist

### Monthly Checks

- [ ] Verify certificate is still valid: `openssl s_client -connect isn.biz:443 -servername isn.biz </dev/null 2>/dev/null | openssl x509 -noout -dates`
- [ ] Check TLS protocol version
- [ ] Verify both domains work (isn.biz and www.isn.biz)
- [ ] Review Netlify dashboard for certificate status
- [ ] Confirm no browser SSL warnings on https://isn.biz

### Critical Dates

- **April 1, 2026**: Renewal verification recommended
- **April 15, 2026**: Auto-renewal should occur
- **April 26, 2026**: Original certificate expiry

### What to Watch For

- Red warnings in browser address bar
- "Not secure" indicators
- Certificate name mismatch warnings
- Expired certificate warnings

---

## Automated Monitoring Script

Create a cron job to monitor certificate expiry:

```bash
#!/bin/bash
# Certificate monitoring script
# Save as: /usr/local/bin/check_isn_cert.sh

DOMAIN="isn.biz"
EXPIRY_DAYS=14  # Alert if less than 14 days remaining

# Get certificate expiry date
EXPIRY=$(openssl s_client -connect $DOMAIN:443 -servername $DOMAIN </dev/null 2>/dev/null | openssl x509 -noout -enddate | cut -d= -f2)
EXPIRY_UNIX=$(date -d "$EXPIRY" +%s)
NOW_UNIX=$(date +%s)
DAYS_LEFT=$(( ($EXPIRY_UNIX - $NOW_UNIX) / 86400 ))

# Alert if less than threshold
if [ $DAYS_LEFT -lt $EXPIRY_DAYS ]; then
    echo "WARNING: $DOMAIN certificate expires in $DAYS_LEFT days!"
    # Send alert email, Slack notification, etc.
else
    echo "OK: $DOMAIN certificate valid for $DAYS_LEFT more days"
fi
```

### Install Cron Job

```bash
# Add to crontab (runs daily at 9 AM)
0 9 * * * /usr/local/bin/check_isn_cert.sh

# Edit crontab
crontab -e
```

---

## Troubleshooting

### Certificate Not Found

```bash
# Error: "Error getting certificate: certificate verify failed"
# Solution: Check if domain is reachable
curl https://isn.biz
```

### TLS Version Mismatch

```bash
# If not TLS 1.3, check Netlify settings
# 1. Go to https://app.netlify.com/
# 2. Select isn.biz domain
# 3. Go to Domain Settings
# 4. Verify HTTPS settings
```

### Certificate Renewal Failed

```bash
# Check Netlify logs for renewal errors
# 1. https://app.netlify.com/sites/[site-name]/overview
# 2. Look for SSL/TLS notifications
# 3. Check email for Let's Encrypt renewal notifications
```

---

## Auto-Renewal (Netlify)

If hosting on Netlify:

1. **Automatic Renewal**: Enabled by default
2. **Renewal Timeline**: 45 days before expiry
3. **No Action Needed**: Let's Encrypt handles everything
4. **Verification**: Monitor Netlify dashboard

### Check Netlify Certificate Status

```bash
# Use Netlify CLI
netlify sites

# Get specific site details
netlify sites info --name="isn-biz"
```

---

## SSL Labs Report

For comprehensive SSL security assessment:

1. Go to: https://www.ssllabs.com/ssltest/
2. Enter: isn.biz
3. Check results for:
   - Overall rating (should be A or A+)
   - Protocol support
   - Cipher strength
   - Certificate validity
   - HSTS headers

---

## Renewal Notification Setup

### Option 1: Email Notifications (Automatic)

Let's Encrypt sends renewal notifications to the domain owner email address registered with Netlify.

### Option 2: Manual Verification (April 1)

Set calendar reminder to verify:
```bash
openssl s_client -connect isn.biz:443 -servername isn.biz </dev/null 2>/dev/null | openssl x509 -noout -enddate
```

### Option 3: Slack Notification

```bash
#!/bin/bash
# Send certificate status to Slack
DAYS_LEFT=$(openssl s_client -connect isn.biz:443 -servername isn.biz </dev/null 2>/dev/null | openssl x509 -noout -enddate | xargs -I {} date -d {} +%s | xargs -I {} echo $(( ({} - $(date +%s)) / 86400 )))

curl -X POST -H 'Content-type: application/json' \
  --data "{'text':'SSL cert for isn.biz valid for $DAYS_LEFT more days'}" \
  YOUR_SLACK_WEBHOOK_URL
```

---

## Common SSL Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| Certificate has expired | Renewal failed | Check Netlify dashboard, manual renewal if needed |
| Common name mismatch | Domain not in SAN | Verify DNS CNAME points to Netlify |
| Self-signed certificate | Temporary cert | Usually resolves automatically |
| Connection refused | Site down or port closed | Check Netlify deployment status |
| Protocol error | TLS version issue | Verify Netlify has TLS 1.3 enabled |

---

## Verification Timeline

### February 2026
- ✓ Certificate verified and valid
- 82 days remaining

### March 2026
- Monitor for renewal process
- Check weekly in Netlify dashboard

### April 1, 2026
- **Recommended verification date**
- Run certificate check command
- Confirm auto-renewal started

### April 15, 2026
- Renewal should be in progress
- Check Netlify for new certificate

### April 26, 2026
- Original certificate expiry date
- New certificate should be active by now

---

## Contact Information for Support

### Netlify Support
- Dashboard: https://app.netlify.com/
- Status Page: https://www.netlify.com/status/
- Support Email: support@netlify.com

### Let's Encrypt
- Documentation: https://letsencrypt.org/docs/
- Support: https://letsencrypt.org/contact/

### Emergency Contacts
- If certificate renewal fails 48 hours before expiry:
  1. Check Netlify notifications
  2. Check email for Let's Encrypt alerts
  3. Contact Netlify support immediately
  4. Provide domain and deployment details

---

## Quick Reference

### Status Check (One-Liner)
```bash
openssl s_client -connect isn.biz:443 -servername isn.biz </dev/null 2>/dev/null | openssl x509 -noout -dates && echo "Certificate valid"
```

### Full Verification (One-Liner)
```bash
openssl s_client -connect isn.biz:443 -servername isn.biz </dev/null 2>/dev/null | grep -E "Verify return code|Subject:|Issuer:|Not After" && echo "Certificate details retrieved"
```

### Check Both Domains (One-Liner)
```bash
for domain in isn.biz www.isn.biz; do echo "=== $domain ==="; openssl s_client -connect $domain:443 -servername $domain </dev/null 2>/dev/null | openssl x509 -noout -dates; done
```

---

**Last Updated:** 2026-02-02
**Certificate Status:** Valid and Trusted ✓
**Next Review:** April 1, 2026
**Maintained by:** SSL Monitoring Guide v1.0
