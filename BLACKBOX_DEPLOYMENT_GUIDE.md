# Blackbox Exporter Deployment Guide

**Purpose:** Deploy Blackbox Exporter to enable website monitoring
**Status:** Ready to deploy
**Time Required:** 15-30 minutes

---

## Quick Start (Copy-Paste Commands)

### Step 1: SSH to TrueNAS

```bash
ssh -i ~/.ssh/truenas_deploy jdmal@100.83.75.4
```

### Step 2: Create Blackbox Configuration

```bash
# Create directory
mkdir -p /docker-volumes/blackbox-exporter

# Create config file
cat > /docker-volumes/blackbox-exporter/blackbox.yml << 'EOF'
modules:
  website_public:
    prober: http
    timeout: 5s
    http:
      valid_http_versions: ["HTTP/1.1", "HTTP/2.0"]
      valid_status_codes:
        - 200
        - 301
        - 302
        - 304
      method: GET
      prefer_ipv4: true
      tls_config:
        insecure_skip_verify: false
  website_public_with_redirect:
    prober: http
    timeout: 5s
    http:
      valid_http_versions: ["HTTP/1.1", "HTTP/2.0"]
      valid_status_codes:
        - 200
        - 301
        - 302
        - 304
        - 307
        - 308
      method: GET
      prefer_ipv4: true
      follow_redirects: true
      tls_config:
        insecure_skip_verify: false
EOF

# Verify file created
cat /docker-volumes/blackbox-exporter/blackbox.yml
```

### Step 3: Deploy Blackbox Container

```bash
docker run -d \
  --name blackbox-exporter \
  --restart unless-stopped \
  -p 9115:9115 \
  -v /docker-volumes/blackbox-exporter/blackbox.yml:/etc/blackbox_exporter/config.yml:ro \
  prom/blackbox-exporter:latest

# Verify container is running
docker ps | grep blackbox
```

### Step 4: Test Blackbox Directly

```bash
# Test if Blackbox is responding
curl 'http://localhost:9115/probe?target=https://isn.biz&module=website_public'

# You should see metrics like:
# probe_success 1
# probe_duration_seconds 0.XXX
# probe_http_status_code 200
```

### Step 5: Configure Prometheus Scrape Job

```bash
# Edit Prometheus config
docker exec prometheus sh -c 'cat /etc/prometheus/prometheus.yml' > /tmp/prometheus.yml

# Create backup
cp /tmp/prometheus.yml /tmp/prometheus.yml.backup

# Add scrape job using cat or your editor
cat >> /tmp/prometheus.yml << 'EOF'

  - job_name: 'blackbox-websites-public'
    metrics_path: /probe
    params:
      module: [website_public]
    static_configs:
      - targets: ['https://isn.biz']
    relabel_configs:
      - source_labels: [__address__]
        target_label: __param_target
      - source_labels: [__param_target]
        target_label: instance
      - target_label: __address__
        replacement: blackbox-exporter:9115
EOF

# Copy updated config to container
docker cp /tmp/prometheus.yml prometheus:/etc/prometheus/prometheus.yml

# Reload Prometheus (without restart)
docker exec prometheus curl -X POST http://localhost:9090/-/reload
```

### Step 6: Verify Metrics Flowing

```bash
# Wait 30-60 seconds, then check Prometheus
curl 'http://prometheus:9090/api/v1/query?query=probe_success{instance="https://isn.biz"}'

# Should return JSON like:
# {"status":"success","data":{"resultType":"instant","result":[{"metric":{"instance":"https://isn.biz"},"value":[TIMESTAMP,"1"]}]}}
```

### Step 7: Check Dashboard

```bash
# Should now see data in Grafana
# Open: https://grafana.isn.biz
# or: http://100.83.75.4:3000
# Navigate to: Dashboards → ISN.BIZ → ISN.BIZ Website Monitoring
# All panels should show green "UP" status
```

---

## Docker Compose Alternative

If you prefer using docker-compose, add to your docker-compose.yml:

```yaml
  blackbox-exporter:
    image: prom/blackbox-exporter:latest
    container_name: blackbox-exporter
    ports:
      - "9115:9115"
    volumes:
      - /docker-volumes/blackbox-exporter/blackbox.yml:/etc/blackbox_exporter/config.yml:ro
    restart: unless-stopped
    networks:
      - monitoring
```

Then:
```bash
docker-compose up -d blackbox-exporter
```

---

## Manual Prometheus Configuration

If auto-reload doesn't work, manually edit the config file:

```bash
# Find Prometheus config location
docker inspect prometheus | grep -i "prometheus.yml"

# Edit directly
vim /path/to/prometheus.yml

# Add this section under scrape_configs:
  - job_name: 'blackbox-websites-public'
    metrics_path: /probe
    params:
      module: [website_public]
    static_configs:
      - targets: ['https://isn.biz']
    relabel_configs:
      - source_labels: [__address__]
        target_label: __param_target
      - source_labels: [__param_target]
        target_label: instance
      - target_label: __address__
        replacement: blackbox-exporter:9115
    scrape_interval: 30s
    scrape_timeout: 10s

# Restart Prometheus to apply changes
docker restart prometheus
```

---

## Troubleshooting

### Blackbox Container Won't Start

```bash
# Check logs
docker logs blackbox-exporter

# Common issue: port already in use
docker ps -a | grep 9115
docker rm blackbox-exporter  # Remove old container
# Then redeploy with docker run command above
```

### Prometheus Can't Connect to Blackbox

```bash
# Verify containers can see each other
docker network ls
docker network inspect bridge  # or your network name

# Test connection from Prometheus
docker exec prometheus curl http://blackbox-exporter:9115/

# If it fails, try using IP instead
docker inspect blackbox-exporter | grep "IPAddress"
```

### Metrics Not Appearing in Prometheus

```bash
# Check Prometheus targets page
curl http://prometheus:9090/targets

# Manual query attempt
curl 'http://prometheus:9090/api/v1/query?query=probe_success'

# Check Prometheus logs
docker logs prometheus | tail -20

# Common issue: config syntax error - check for trailing commas
docker exec prometheus sh -c 'cat /etc/prometheus/prometheus.yml | grep -A 5 "blackbox"'
```

### Grafana Dashboard Still Shows No Data

```bash
# Wait 1-2 minutes for first scrape cycle
# Then refresh dashboard

# Check if Prometheus scraping is working
curl 'http://prometheus:9090/api/v1/query?query=up{job="blackbox-websites-public"}'

# Should show: "value": ["1"]  (1 = scraping successfully)
```

---

## Verification Checklist

After deployment, verify each step:

- [ ] Blackbox container is running: `docker ps | grep blackbox`
- [ ] Blackbox responds to requests: `curl http://localhost:9115/metrics`
- [ ] Can probe website: `curl 'http://localhost:9115/probe?target=https://isn.biz&module=website_public'`
- [ ] Prometheus scraped config: `curl http://prometheus:9090/api/v1/targets`
- [ ] Metrics exist in Prometheus: `curl 'http://prometheus:9090/api/v1/query?query=probe_success'`
- [ ] Grafana dashboard shows data: Visit https://grafana.isn.biz/d/f0948e16-c141-4bf3-a7ec-c7ea408128bd
- [ ] All 9 panels have data (not blank)
- [ ] Website status shows "UP" in green
- [ ] Response time shows value (not N/A)
- [ ] SSL days shows number (not blank)

---

## What Gets Monitored After Deployment

### Every 30 seconds, Blackbox will:

1. **DNS Resolution** - Resolve isn.biz hostname
2. **TCP Connection** - Connect to port 443 (HTTPS)
3. **TLS Handshake** - Verify SSL certificate
4. **HTTP Request** - Send GET request to /
5. **Status Verification** - Check response is 200 OK
6. **Metrics Collection** - Generate metrics:
   - probe_success (1 or 0)
   - probe_duration_seconds
   - probe_http_status_code
   - probe_ssl_earliest_cert_expiry
   - probe_dns_lookup_time_seconds
   - And 10+ more detailed metrics

### Grafana displays:

1. **Real-time status** - UP/DOWN indicator
2. **Response time** - How fast site responds
3. **SSL expiry** - When certificate needs renewal
4. **Uptime history** - 24-hour timeline
5. **Uptime percentage** - SLA compliance

### Alerts will fire if:

1. **Site is DOWN** - After 2 minutes of downtime
2. **Slow Response** - Response time > 2 seconds for 5 minutes
3. **SSL Expiring** - Certificate expires in < 7 days

---

## Important Notes

### Network Connectivity

- Blackbox needs outbound HTTPS access to isn.biz
- If behind firewall, ensure port 443 is allowed
- If using proxy, configure in Blackbox config

### Certificate Validation

Current config validates SSL certificates:
```yaml
tls_config:
  insecure_skip_verify: false  # Strict validation
```

Change to `true` only if needed for self-signed certs.

### Probe Frequency

Default: Every 30 seconds
- Can adjust in scrape_interval
- More frequent = higher Prometheus load
- Less frequent = less reactive to issues

### Data Retention

Prometheus default: 15 days of data
- Change via `--storage.tsdb.retention.time` parameter
- Or in Prometheus config

---

## Rollback Procedure

If something goes wrong:

```bash
# Stop Blackbox
docker stop blackbox-exporter

# Restore Prometheus config from backup
docker cp /tmp/prometheus.yml.backup prometheus:/etc/prometheus/prometheus.yml

# Restart Prometheus
docker restart prometheus

# Remove Blackbox container
docker rm blackbox-exporter

# Investigate issue and retry
```

---

## Performance Expectations

### Resource Usage

- **Blackbox memory:** ~50-100MB
- **Prometheus additional:** ~10-50MB (for website metrics)
- **Grafana dashboard load:** < 1 second

### Prometheus Metric Growth

- ~50 new metrics every 30 seconds from Blackbox
- ~15 days of data = ~172,800 data points per metric
- Estimated storage: 500MB-2GB depending on other metrics

---

## Maintenance

### Daily
- Visually check dashboard for anomalies
- Verify website shows "UP"

### Weekly
- Review uptime percentage
- Check for response time patterns
- Verify alerts if any were triggered

### Monthly
- Review and adjust alert thresholds
- Export dashboard data for reporting
- Check Prometheus storage usage

### Quarterly
- Update Blackbox Exporter version
- Review and enhance monitoring
- Update documentation

---

## Support

### If Deployment Fails

1. Check the Troubleshooting section above
2. Review container logs: `docker logs blackbox-exporter`
3. Verify network connectivity: `docker network ls`
4. Test Blackbox manually: `curl http://localhost:9115/metrics`

### Common Commands

```bash
# View Blackbox logs
docker logs -f blackbox-exporter

# Restart Blackbox
docker restart blackbox-exporter

# View resource usage
docker stats blackbox-exporter

# Remove and redeploy
docker rm blackbox-exporter
# Then rerun docker run command above
```

---

**Last Updated:** February 2, 2026
**Status:** Ready for deployment
**Estimated Time:** 15-30 minutes
**Risk Level:** Low (containerized, no system changes)

Next Step: Follow the "Quick Start" section above to deploy Blackbox Exporter.
