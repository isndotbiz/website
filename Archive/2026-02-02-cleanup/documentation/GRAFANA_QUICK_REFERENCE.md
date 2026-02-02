# ISN.BIZ Grafana - Quick Reference

## Quick Access

**Dashboard:** https://grafana.isn.biz/d/f0948e16-c141-4bf3-a7ec-c7ea408128bd/isn-biz-website-monitoring

**Login:** admin / Comet0-Avalanche9-Compass8

**SSH:** `ssh -i ~/.ssh/truenas_deploy jdmal@100.83.75.4`

---

## At a Glance

| Metric | Current | Threshold | Status |
|--------|---------|-----------|--------|
| Website | UP | Must be UP | ✅ |
| Response | 0.110s | < 2s | ✅ |
| SSL Cert | 82.5 days | > 7 days | ✅ |
| HTTP Status | 200 | 200-299 | ✅ |

---

## Dashboard Panels

1. Website Status (UP/DOWN)
2. HTTP Status Code (200, 404, 500, etc.)
3. Response Time (seconds)
4. SSL Days Until Expiry
5. Response Time Graph (6h)
6. Uptime History (6h)
7. Status Code Distribution (24h)
8. Uptime Percentage (24h)
9. SSL Expiry Date

---

## Alerts Configured

| Alert | Trigger | Duration |
|-------|---------|----------|
| Site Down | probe_success < 1 | 2 min |
| Slow Response | response > 2s | 5 min |
| SSL Expiring | < 7 days | 1 hour |

---

## Common Commands

### Check Metrics
```bash
# Current uptime
ssh -i ~/.ssh/truenas_deploy jdmal@100.83.75.4 \
  "docker exec prometheus wget -qO- 'http://localhost:9090/api/v1/query?query=probe_success{instance=\"https://isn.biz\"}'"

# Response time
ssh -i ~/.ssh/truenas_deploy jdmal@100.83.75.4 \
  "docker exec prometheus wget -qO- 'http://localhost:9090/api/v1/query?query=probe_duration_seconds{instance=\"https://isn.biz\"}'"
```

### Export Dashboard
```bash
ssh -i ~/.ssh/truenas_deploy jdmal@100.83.75.4 \
  "curl -s -u 'admin:Comet0-Avalanche9-Compass8' \
  http://172.16.4.15:3000/api/dashboards/uid/f0948e16-c141-4bf3-a7ec-c7ea408128bd"
```

---

## Files Location

All configuration files saved to: `D:\workspace\ISNBIZ_Files\`

- `GRAFANA_DASHBOARD_SUMMARY.md` - Full documentation
- `GRAFANA_CONFIGURATION_COMPLETE.md` - Setup report
- `grafana-isn-biz-dashboard.json` - Dashboard backup
- `grafana-isn-biz-alerts.json` - Alert rules backup

---

## Troubleshooting

**No data showing:**
1. Check Prometheus: `docker ps | grep prometheus`
2. Verify target: http://100.83.75.4:9090/targets

**Can't access Grafana:**
1. Check DNS: `nslookup grafana.isn.biz`
2. Check Traefik: `docker ps | grep traefik`

**Alerts not working:**
1. Navigate to: Alerting → Alert rules
2. Check evaluation state
3. Verify contact points configured

---

**Created:** February 2, 2026
**Status:** ✅ Production Ready
