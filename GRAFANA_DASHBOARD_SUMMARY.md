# ISN.BIZ Grafana Dashboard Summary

## Overview

Successfully configured comprehensive Grafana monitoring for isn.biz website.

**Dashboard URL:** https://grafana.isn.biz/d/f0948e16-c141-4bf3-a7ec-c7ea408128bd/isn-biz-website-monitoring

**Credentials:**
- Username: admin
- Password: Comet0-Avalanche9-Compass8

---

## Dashboard Details

### Created: February 2, 2026

**Dashboard UID:** f0948e16-c141-4bf3-a7ec-c7ea408128bd
**Folder:** ISN.BIZ (UID: cfc2675c2fm68b)
**Refresh Interval:** 30 seconds
**Time Range:** Last 6 hours (configurable)

---

## Panels Configuration

### Row 1: Key Metrics (Status Cards)

1. **Website Status**
   - Type: Stat panel
   - Metric: `probe_success{instance="https://isn.biz"}`
   - Display: Shows "UP" (green) or "DOWN" (red)
   - Current: UP ✅

2. **HTTP Status Code**
   - Type: Stat panel
   - Metric: `probe_http_status_code{instance="https://isn.biz"}`
   - Color coding:
     - 200 = Green (OK)
     - 300-399 = Yellow (Redirect)
     - 400-499 = Orange (Client Error)
     - 500+ = Red (Server Error)
   - Current: 200 ✅

3. **Response Time**
   - Type: Stat panel with area graph
   - Metric: `probe_duration_seconds{instance="https://isn.biz"}`
   - Thresholds:
     - Green: < 1 second
     - Yellow: 1-2 seconds
     - Red: > 2 seconds
   - Current: 0.110s ✅

4. **SSL Certificate Days Until Expiry**
   - Type: Stat panel
   - Metric: `(probe_ssl_earliest_cert_expiry{instance="https://isn.biz"} - time()) / 86400`
   - Thresholds:
     - Red: < 7 days
     - Orange: 7-30 days
     - Yellow: 30-60 days
     - Green: > 60 days
   - Current: 82.5 days ✅

### Row 2: Time Series Charts

5. **Response Time Over Time**
   - Type: Time series graph
   - Shows response time trends
   - Smooth line interpolation
   - 2-second threshold line

6. **Uptime History**
   - Type: Time series graph
   - Shows uptime/downtime events
   - Step-after interpolation
   - Red = down, Green = up

### Row 3: Analytics

7. **HTTP Status Code Distribution (Last 24h)**
   - Type: Bar gauge
   - Shows frequency of each status code
   - Horizontal orientation

8. **Uptime Percentage (24h)**
   - Type: Stat panel with area chart
   - Metric: `avg_over_time(probe_success{instance="https://isn.biz"}[24h]) * 100`
   - Thresholds:
     - Red: < 95%
     - Yellow: 95-99%
     - Green: > 99%
   - Target: 99.9% uptime

9. **SSL Certificate Expiry Date**
   - Type: Stat panel
   - Shows exact expiration timestamp
   - Format: ISO DateTime

---

## Alert Rules Configured

### 1. ISN.BIZ Website Down
- **UID:** isn-biz-site-down
- **Severity:** Critical
- **Condition:** `probe_success < 1`
- **Duration:** 2 minutes
- **Description:** Alerts when website is unreachable for 2+ minutes
- **Action:** Immediate investigation required

### 2. ISN.BIZ Slow Response Time
- **UID:** isn-biz-slow-response
- **Severity:** Warning
- **Condition:** `probe_duration_seconds > 2`
- **Duration:** 5 minutes
- **Description:** Alerts when response time exceeds 2 seconds for 5+ minutes
- **Action:** Performance investigation recommended

### 3. ISN.BIZ SSL Certificate Expiring Soon
- **UID:** isn-biz-ssl-expiring
- **Severity:** Warning
- **Condition:** `(probe_ssl_earliest_cert_expiry - time()) / 86400 < 7`
- **Duration:** 1 hour
- **Description:** Alerts when SSL certificate will expire in less than 7 days
- **Action:** Renew SSL certificate

---

## Current Status (as of creation)

All metrics are healthy:

- ✅ **Website Status:** UP (probe_success = 1)
- ✅ **Response Time:** 0.110 seconds (well under 2s threshold)
- ✅ **SSL Certificate:** 82.5 days remaining (well above 7d threshold)
- ✅ **HTTP Status:** 200 OK
- ✅ **No active alerts**

---

## Data Source

**Prometheus Instance:** http://prometheus:9090
- Data source UID: prometheus
- Type: Prometheus
- Access: Server (proxy)

**Blackbox Exporter:**
- Job: blackbox-websites-public
- Target: https://isn.biz
- Probe type: website_public

---

## File Exports

1. **grafana-isn-biz-dashboard.json**
   - Full dashboard configuration
   - Can be imported to restore dashboard

2. **grafana-isn-biz-alerts.json**
   - All 3 alert rule definitions
   - Can be imported via provisioning API

3. **isn-biz-dashboard.json**
   - Original dashboard template

---

## Access Information

### Via Web Browser
- URL: https://grafana.isn.biz
- Login: admin / Comet0-Avalanche9-Compass8
- Navigate to: Dashboards → ISN.BIZ folder → ISN.BIZ Website Monitoring

### Via SSH
```bash
ssh -i ~/.ssh/truenas_deploy jdmal@100.83.75.4
```

### Via Grafana API
```bash
# Get dashboard
curl -u 'admin:Comet0-Avalanche9-Compass8' \
  http://172.16.4.15:3000/api/dashboards/uid/f0948e16-c141-4bf3-a7ec-c7ea408128bd

# Get alerts
curl -u 'admin:Comet0-Avalanche9-Compass8' \
  http://172.16.4.15:3000/api/v1/provisioning/alert-rules
```

---

## Maintenance Notes

### Dashboard Updates
To update the dashboard, use the Grafana UI or API:
```bash
curl -X POST -u 'admin:PASSWORD' \
  -H 'Content-Type: application/json' \
  http://172.16.4.15:3000/api/dashboards/db \
  -d @grafana-isn-biz-dashboard.json
```

### Alert Rule Updates
Use the provisioning API:
```bash
curl -X PUT -u 'admin:PASSWORD' \
  -H 'Content-Type: application/json' \
  http://172.16.4.15:3000/api/v1/provisioning/alert-rules/isn-biz-site-down \
  -d @alert-config.json
```

### Backup
Dashboard and alert configurations are exported to:
- `D:\workspace\ISNBIZ_Files\grafana-isn-biz-dashboard.json`
- `D:\workspace\ISNBIZ_Files\grafana-isn-biz-alerts.json`

---

## Next Steps (Recommendations)

1. **Set up notification channels**
   - Configure email alerts
   - Integrate with Slack/Discord/PagerDuty
   - Configure alert routing

2. **Add more metrics**
   - DNS lookup time
   - SSL certificate chain validity
   - Geographic response times (if using multi-region monitoring)

3. **Create additional dashboards**
   - Weekly/Monthly reports
   - Performance trends
   - SLA compliance tracking

4. **Set up contact points**
   - Admin email for critical alerts
   - Team Slack channel for warnings
   - On-call rotation for downtime alerts

---

## Troubleshooting

### Dashboard not loading data
1. Check Prometheus is running: `docker ps | grep prometheus`
2. Verify metrics exist: `curl http://prometheus:9090/api/v1/query?query=probe_success`
3. Check data source connection in Grafana

### Alerts not firing
1. Verify alert rules: Navigate to Alerting → Alert rules
2. Check evaluation status
3. Review notification policies

### Can't access Grafana
1. Verify Traefik is routing correctly: `docker ps | grep traefik`
2. Check DNS resolution: `nslookup grafana.isn.biz`
3. Verify SSL certificate: `curl -v https://grafana.isn.biz`

---

**Created by:** Claude AI + jdmal
**Date:** February 2, 2026
**Grafana Version:** 12.3.1
**Status:** Production Ready ✅
