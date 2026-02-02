#!/usr/bin/env python3
import json
import requests

# Grafana configuration
GRAFANA_URL = "http://172.16.4.15:3000"
GRAFANA_USER = "admin"
GRAFANA_PASS = "Comet0-Avalanche9-Compass8"

# Read dashboard JSON
with open('isn-biz-dashboard.json', 'r') as f:
    dashboard_data = json.load(f)

# Upload to Grafana
response = requests.post(
    f"{GRAFANA_URL}/api/dashboards/db",
    json=dashboard_data,
    auth=(GRAFANA_USER, GRAFANA_PASS),
    headers={"Content-Type": "application/json"}
)

print(f"Status: {response.status_code}")
print(f"Response: {response.text}")

if response.status_code == 200:
    result = response.json()
    print(f"\nDashboard created successfully!")
    print(f"URL: {GRAFANA_URL}{result.get('url')}")
    print(f"UID: {result.get('uid')}")
