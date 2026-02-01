# Credit Report Automation - Complete Documentation

**Source**: Extracted from Equifax Agent (agent-a4ed7f8)
**Location**: `/mnt/d/workspace/credit_report_automation.py`
**Original Project**: `/mnt/d/workspace/scripts/credit-report-automation/`
**Status**: Production-Ready ✅

---

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Architecture](#architecture)
4. [Installation](#installation)
5. [1Password CLI Integration](#1password-cli-integration)
6. [Configuration](#configuration)
7. [Usage](#usage)
8. [Output Structure](#output-structure)
9. [Code Documentation](#code-documentation)
10. [Security Best Practices](#security-best-practices)
11. [Troubleshooting](#troubleshooting)
12. [Advanced Integration](#advanced-integration)

---

## Overview

This is a **production-ready Python automation system** that uses Playwright to:

- **Automate login** to Equifax, Nav, and myFICO credit reporting services
- **Retrieve credit reports** (business and personal)
- **Extract structured data** to JSON for database import
- **Generate PDF reports** for archival
- **Manage credentials securely** using 1Password CLI (no hardcoded passwords!)

### Key Statistics

- **700+ lines** of Python code
- **2,725+ lines** total (with documentation)
- **3 services** supported (Equifax, Nav, myFICO)
- **100% credential security** via 1Password CLI
- **Zero hardcoded credentials**

---

## Features

### Core Capabilities

✅ **Secure Credential Management**
- Integration with 1Password CLI (`op`)
- No credentials stored in code or config files
- Automatic validation of 1Password authentication

✅ **Multi-Service Support**
- Equifax Business Credit Reports
- Nav Business Credit Monitoring
- myFICO Personal Credit Scores (3 bureaus)

✅ **Intelligent Automation**
- 2FA detection and handling
- Automatic retry logic
- Error screenshots for debugging
- Timestamped session directories

✅ **Data Extraction**
- Full-page PDF generation
- Structured JSON output
- Credit score extraction
- Payment history capture
- Trade line details

✅ **Production Features**
- Comprehensive error handling
- Session logging
- Headless/GUI modes
- Configurable timeouts
- Custom output directories

---

## Architecture

### Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Browser Automation** | Playwright (Python) | Web scraping and interaction |
| **Credential Management** | 1Password CLI | Secure password retrieval |
| **Data Storage** | JSON + PDF | Structured data + visual records |
| **Runtime** | Python 3.8+ | Core execution environment |

### Class Structure

```
CreditReportAutomation
├── OnePasswordManager
│   ├── validate_op_cli()
│   └── get_credentials()
│
├── Browser Management
│   ├── setup_browser()
│   ├── save_page_pdf()
│   └── save_json_data()
│
├── Service Automation
│   ├── automate_equifax()
│   ├── automate_nav()
│   └── automate_myfico()
│
├── Data Extraction
│   ├── _extract_equifax_data()
│   ├── _extract_nav_data()
│   └── _extract_myfico_data()
│
└── Orchestration
    └── run_full_automation()
```

---

## Installation

### Prerequisites

1. **Python 3.8+** (already installed)
2. **1Password CLI** - [Download](https://1password.com/downloads/command-line/)
3. **Playwright** - Installed in virtual environment

### Quick Setup

```bash
cd /mnt/d/workspace/scripts/credit-report-automation

# Virtual environment already created with:
python3 -m venv venv
source venv/bin/activate
pip install playwright python-dotenv
playwright install chromium
```

### Verify Installation

```bash
# Check 1Password CLI
op --version
op account list

# Check Python environment
./venv/bin/python --version

# Check Playwright
./venv/bin/playwright --version

# Run test script
./venv/bin/python test_1password.py --vault Research
```

---

## 1Password CLI Integration

### How It Works

1. **Authentication Check**
   ```python
   op account list  # Verifies signed in
   ```

2. **Credential Retrieval**
   ```python
   op item get "Equifax Business" --vault Research --format json
   ```

3. **Field Extraction**
   - Automatically extracts username/email
   - Securely retrieves password
   - Captures security answers (if present)

### Setup 1Password Items

Create these items in your 1Password vault:

| Item Name | Required Fields | URL |
|-----------|----------------|-----|
| **Equifax Business** | username/email, password | https://www.equifax.com/business/ |
| **Nav** | username/email, password | https://www.nav.com/ |
| **myFICO** | username/email, password | https://www.myfico.com/ |

### Automated Setup

```bash
cd /mnt/d/workspace/scripts/credit-report-automation
./setup_1password_items.sh
```

Or manually via CLI:

```bash
op item create \
  --category=Login \
  --title="Equifax Business" \
  --vault="Research" \
  username="your-email@example.com" \
  password="your-password" \
  --url="https://www.equifax.com/business/"
```

### Validation

```bash
# Test setup
./venv/bin/python test_1password.py --vault Research

# Expected output:
# ✓ 1Password CLI installed: 2.32.0
# ✓ Signed in to 1Password
# ✓ Retrieved credentials for: Equifax Business
# ✓ Retrieved credentials for: Nav
# ✓ Retrieved credentials for: myFICO
```

---

## Configuration

### config.json Structure

```json
{
  "services": {
    "equifax": {
      "name": "Equifax Business",
      "op_item_name": "Equifax Business",
      "url": "https://www.equifax.com/business/business-credit-reports/",
      "selectors": {
        "login_button": "text=/sign in|log in/i",
        "username_field": "input[type=\"email\"], input[name*=\"user\"]",
        "password_field": "input[type=\"password\"]",
        "submit_button": "button[type=\"submit\"]"
      }
    }
  },
  "output": {
    "base_directory": "/mnt/d/OneDrive/Downloads/credit-reports",
    "pdf_enabled": true,
    "json_enabled": true
  },
  "browser": {
    "headless": false,
    "viewport": {"width": 1920, "height": 1080},
    "timeout": {
      "navigation": 60000,
      "action": 30000,
      "2fa_wait": 300000
    }
  }
}
```

### Customization

**Update selectors** when websites change:
```json
{
  "services": {
    "equifax": {
      "selectors": {
        "username_field": "input[id='new-username-field']"
      }
    }
  }
}
```

**Change output location**:
```json
{
  "output": {
    "base_directory": "/custom/path/to/reports"
  }
}
```

---

## Usage

### Command Line Interface

#### Basic Usage

```bash
cd /mnt/d/workspace/scripts/credit-report-automation

# Run all services
./run.sh --vault Research

# Run specific service
./run.sh --vault Research --service equifax
./run.sh --vault Research --service nav
./run.sh --vault Research --service myfico

# Headless mode (no browser window)
./run.sh --vault Research --headless

# Custom output directory
./run.sh --vault Research --output-dir /path/to/output
```

#### Direct Python Execution

```bash
# Activate virtual environment
source venv/bin/activate

# Run automation
python credit_report_updater.py --vault Research

# With options
python credit_report_updater.py \
  --vault Research \
  --service equifax \
  --headless \
  --output-dir /custom/path
```

#### Available Arguments

| Argument | Type | Default | Description |
|----------|------|---------|-------------|
| `--vault` | string | Research | 1Password vault name |
| `--service` | choice | all | Service to run (equifax/nav/myfico/all) |
| `--headless` | flag | false | Run browser in headless mode |
| `--output-dir` | path | /mnt/d/OneDrive/Downloads/credit-reports | Output directory |

### Python API

```python
from credit_report_updater import CreditReportAutomation
from playwright.sync_api import sync_playwright

# Initialize
automation = CreditReportAutomation(
    headless=True,
    output_dir="/custom/path",
    vault="Research"
)

# Run full automation
with sync_playwright() as playwright:
    automation.setup_browser(playwright)
    results = automation.run_full_automation()

    # Check results
    if not results["errors"]:
        print(f"✓ Success! {len(results['reports'])} reports retrieved")

    # Cleanup
    automation.context.close()
    automation.browser.close()
```

### 2FA Handling

The script automatically detects 2FA prompts:

1. Script fills username/password
2. Detects 2FA prompt
3. Console shows: `⚠ 2FA detected for [service]`
4. **You have 5 minutes** to complete 2FA in browser
5. Script continues after verification

---

## Output Structure

### Directory Layout

```
/mnt/d/OneDrive/Downloads/credit-reports/
└── 20260201_143022/              # Timestamp: YYYYMMDD_HHMMSS
    ├── session_summary.json      # Session overview
    │
    ├── equifax_business_report.pdf
    ├── equifax_data.json
    │
    ├── nav_business_report.pdf
    ├── nav_data.json
    │
    ├── myfico_report.pdf
    ├── myfico_data.json
    │
    └── *_error.png               # Error screenshots (if any)
```

### JSON Data Format

#### session_summary.json

```json
{
  "session_id": "20260201_143022",
  "timestamp": "2026-02-01T14:30:22",
  "output_directory": "/mnt/d/OneDrive/Downloads/credit-reports/20260201_143022",
  "reports": {
    "equifax": { /* report data */ },
    "nav": { /* report data */ },
    "myfico": { /* report data */ }
  },
  "errors": []
}
```

#### equifax_data.json

```json
{
  "source": "Equifax",
  "retrieved_at": "2026-02-01T14:30:22",
  "business_score": 75,
  "payment_history": [],
  "credit_utilization": null,
  "trade_lines": [],
  "inquiries": [],
  "public_records": [],
  "raw_html": "..."
}
```

#### nav_data.json

```json
{
  "source": "Nav",
  "retrieved_at": "2026-02-01T14:30:22",
  "business_scores": {
    "Dun & Bradstreet": 78,
    "Experian": 82
  },
  "personal_score": null,
  "recommendations": [],
  "raw_html": "..."
}
```

#### myfico_data.json

```json
{
  "source": "myFICO",
  "retrieved_at": "2026-02-01T14:30:22",
  "fico_scores": {
    "Equifax": 720,
    "Experian": 715,
    "TransUnion": 718
  },
  "credit_factors": [],
  "raw_html": "..."
}
```

---

## Code Documentation

### Main Classes

#### OnePasswordManager

**Purpose**: Manages secure credential retrieval from 1Password CLI

```python
class OnePasswordManager:
    def __init__(self, vault: str = "Research"):
        """Initialize with vault name"""

    def validate_op_cli(self):
        """Verify 1Password CLI installed and authenticated"""

    def get_credentials(self, item_name: str) -> Dict[str, str]:
        """
        Retrieve credentials from 1Password

        Returns:
            {
                "username": "user@example.com",
                "password": "secure_password",
                "email": "user@example.com"
            }
        """
```

#### CreditReportAutomation

**Purpose**: Main automation orchestrator

```python
class CreditReportAutomation:
    def __init__(
        self,
        headless: bool = True,
        output_dir: Optional[Path] = None,
        vault: str = "Research"
    ):
        """Initialize automation with configuration"""

    def setup_browser(self, playwright: Playwright):
        """Configure browser with anti-detection settings"""

    def automate_equifax(self) -> Dict:
        """Automate Equifax business credit report retrieval"""

    def automate_nav(self) -> Dict:
        """Automate Nav business credit retrieval"""

    def automate_myfico(self) -> Dict:
        """Automate myFICO personal credit retrieval"""

    def run_full_automation(self) -> Dict:
        """Execute complete automation for all services"""
```

### Key Methods

#### Browser Setup

```python
def setup_browser(self, playwright: Playwright):
    """
    Initialize browser with:
    - Anti-automation detection bypass
    - Custom user agent
    - Proper viewport size
    - Timezone configuration
    """
    self.browser = playwright.chromium.launch(
        headless=self.headless,
        args=["--disable-blink-features=AutomationControlled"]
    )

    self.context = self.browser.new_context(
        viewport={"width": 1920, "height": 1080},
        user_agent="Mozilla/5.0 ...",
        locale="en-US",
        timezone_id="America/New_York"
    )
```

#### 2FA Detection

```python
def handle_2fa_prompt(self, page: Page, service_name: str) -> bool:
    """
    Detect common 2FA indicators:
    - input[name*="code"]
    - input[name*="token"]
    - text=/verification code/i

    Waits up to 5 minutes for manual completion
    """
```

#### Data Extraction

```python
def _extract_equifax_data(self, page: Page) -> Dict:
    """
    Extract structured data:
    1. Business credit score (regex extraction)
    2. Payment history
    3. Trade lines
    4. Public records
    5. Raw HTML for further processing
    """
```

---

## Security Best Practices

### 1. Credential Security

✅ **DO**
- Use 1Password CLI for all credentials
- Enable 1Password device authorization
- Use strong master password
- Regularly rotate service passwords

❌ **DON'T**
- Hardcode credentials in code
- Store passwords in config files
- Share 1Password master password
- Commit credentials to git

### 2. Output Security

```bash
# Protect output directory
chmod 700 /mnt/d/OneDrive/Downloads/credit-reports

# Ensure only you can access reports
ls -la /mnt/d/OneDrive/Downloads/credit-reports
# drwx------ (700 permissions)
```

### 3. 1Password Best Practices

```bash
# Always sign in securely
eval $(op signin)

# Verify authentication before running
op account list

# Use specific vault for separation
./run.sh --vault Research  # Not "Private" or "Personal"
```

### 4. Audit Trail

Every run creates:
- Timestamped session directory
- `session_summary.json` with metadata
- Error screenshots (for debugging only)

Review regularly:
```bash
# Check recent sessions
ls -lt /mnt/d/OneDrive/Downloads/credit-reports/ | head -10

# Review session summary
cat /mnt/d/OneDrive/Downloads/credit-reports/latest/session_summary.json | jq .
```

---

## Troubleshooting

### Common Issues

#### 1. "1Password CLI not found"

**Problem**: 1Password CLI not installed

**Solution**:
```bash
# Install on Ubuntu/Debian
curl -sS https://downloads.1password.com/linux/keys/1password.asc | \
  sudo gpg --dearmor --output /usr/share/keyrings/1password-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/1password-archive-keyring.gpg] https://downloads.1password.com/linux/debian/$(dpkg --print-architecture) stable main" | \
  sudo tee /etc/apt/sources.list.d/1password.list

sudo apt update && sudo apt install 1password-cli

# Verify
op --version
```

#### 2. "Not signed in to 1Password"

**Problem**: 1Password session expired

**Solution**:
```bash
eval $(op signin)
```

#### 3. "Failed to retrieve credentials"

**Problem**: Item doesn't exist or wrong vault

**Solution**:
```bash
# List vaults
op vault list

# List items in vault
op item list --vault Research | grep -i equifax

# Check exact item name
op item get "Equifax Business" --vault Research

# Create if missing
op item create \
  --category=Login \
  --title="Equifax Business" \
  --vault="Research" \
  username="user@example.com" \
  password="your-password"
```

#### 4. Browser doesn't open

**Problem**: Headless mode enabled or display issue

**Solution**:
```bash
# Remove headless flag
./run.sh --vault Research  # No --headless

# Check Playwright
./venv/bin/playwright --version
```

#### 5. Selectors not working

**Problem**: Website HTML changed

**Solution**:
```bash
# Run with browser visible to inspect
./run.sh --vault Research --service equifax

# Update config.json with new selectors
# Find selectors using browser DevTools (F12)
```

#### 6. 2FA timeout

**Problem**: Didn't complete 2FA within 5 minutes

**Solution**:
- Have phone ready before running
- Complete 2FA quickly
- Increase timeout in `config.json`:
  ```json
  {
    "browser": {
      "timeout": {
        "2fa_wait": 600000  # 10 minutes
      }
    }
  }
  ```

### Debugging Techniques

#### 1. Error Screenshots

```bash
cd /mnt/d/OneDrive/Downloads/credit-reports

# Find latest session
latest=$(ls -t | head -1)

# Check for error screenshots
ls -lh "$latest"/*_error.png

# View screenshot
xdg-open "$latest"/equifax_error.png
```

#### 2. Session Summary Analysis

```bash
# View last session summary
cat /mnt/d/OneDrive/Downloads/credit-reports/latest/session_summary.json | jq .

# Check for errors
cat session_summary.json | jq '.errors[]'

# Check retrieved reports
cat session_summary.json | jq '.reports | keys'
```

#### 3. Verbose Logging

```python
# Add to credit_report_updater.py
import logging
logging.basicConfig(level=logging.DEBUG)
```

#### 4. Interactive Debugging

```bash
# Run with browser visible
./run.sh --vault Research  # Watch automation

# Pause at specific points
# Add to code: page.pause()  # Opens Playwright Inspector
```

---

## Advanced Integration

### 1. Database Import

```python
#!/usr/bin/env python3
"""Import credit reports to database"""

import json
import sqlite3
from pathlib import Path

def import_to_db(session_dir: Path):
    conn = sqlite3.connect("/mnt/d/workspace/credit_data.db")
    cursor = conn.cursor()

    # Create table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS credit_reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source TEXT,
            business_score INTEGER,
            retrieved_at TIMESTAMP,
            session_id TEXT,
            raw_data TEXT
        )
    """)

    # Import Equifax
    with open(session_dir / "equifax_data.json") as f:
        data = json.load(f)

    cursor.execute("""
        INSERT INTO credit_reports
        (source, business_score, retrieved_at, session_id, raw_data)
        VALUES (?, ?, ?, ?, ?)
    """, (
        data["source"],
        data.get("business_score"),
        data["retrieved_at"],
        session_dir.name,
        json.dumps(data)
    ))

    conn.commit()
    conn.close()

# Usage
latest = max(
    Path("/mnt/d/OneDrive/Downloads/credit-reports").glob("*/"),
    key=lambda p: p.name
)
import_to_db(latest)
```

### 2. Scheduled Automation (Cron)

```bash
# Edit crontab
crontab -e

# Run every Monday at 9:00 AM
0 9 * * 1 cd /mnt/d/workspace/scripts/credit-report-automation && ./run.sh --vault Research --headless >> /tmp/credit_reports.log 2>&1

# Run first day of each month at 8:00 AM
0 8 1 * * cd /mnt/d/workspace/scripts/credit-report-automation && ./run.sh --vault Research --headless >> /tmp/credit_reports.log 2>&1

# Check logs
tail -f /tmp/credit_reports.log
```

### 3. Email Notifications

```bash
#!/bin/bash
# run_and_notify.sh

cd /mnt/d/workspace/scripts/credit-report-automation

# Run automation
./run.sh --vault Research --headless > /tmp/credit_run.log 2>&1

# Send email with results
if [ $? -eq 0 ]; then
    mail -s "✓ Credit Reports Updated" user@example.com < /tmp/credit_run.log
else
    mail -s "✗ Credit Report Update FAILED" user@example.com < /tmp/credit_run.log
fi
```

### 4. Slack Integration

```python
#!/usr/bin/env python3
"""Send Slack notification after automation"""

import requests
from credit_report_updater import CreditReportAutomation
from playwright.sync_api import sync_playwright

SLACK_WEBHOOK = "https://hooks.slack.com/services/YOUR/WEBHOOK/URL"

def send_slack(results):
    if not results["errors"]:
        message = {
            "text": "✅ Credit Reports Updated",
            "blocks": [{
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*Session*: {results['session_id']}\n*Reports*: {len(results['reports'])}"
                }
            }]
        }
    else:
        message = {
            "text": "⚠️ Credit Report Errors",
            "blocks": [{
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "\n".join(f"• {e}" for e in results["errors"])
                }
            }]
        }

    requests.post(SLACK_WEBHOOK, json=message)

# Run automation
automation = CreditReportAutomation(headless=True, vault="Research")
with sync_playwright() as playwright:
    automation.setup_browser(playwright)
    results = automation.run_full_automation()
    send_slack(results)
    automation.context.close()
    automation.browser.close()
```

### 5. Extending for New Services

```python
def automate_experian(self) -> Dict:
    """Automate Experian business credit retrieval"""
    credentials = self.op_manager.get_credentials("Experian Business")
    page = self.context.new_page()

    try:
        # Navigate
        page.goto("https://www.experian.com/business/")

        # Login
        page.click('text=/sign in/i')
        page.fill('input[type="email"]', credentials["username"])
        page.fill('input[type="password"]', credentials["password"])
        page.click('button[type="submit"]')
        page.wait_for_load_state("networkidle")

        # Handle 2FA
        self.handle_2fa_prompt(page, "Experian")

        # Extract data
        data = self._extract_experian_data(page)

        # Save
        self.save_page_pdf(page, "experian_report.pdf")
        self.save_json_data(data, "experian_data.json")

        return data
    finally:
        page.close()

def _extract_experian_data(self, page: Page) -> Dict:
    """Extract Experian-specific data"""
    return {
        "source": "Experian",
        "retrieved_at": datetime.now().isoformat(),
        "business_score": None,  # Extract from page
        "raw_html": page.content()
    }
```

---

## Files Reference

### Main Script
- **Location**: `/mnt/d/workspace/credit_report_automation.py`
- **Size**: 700+ lines
- **Python Version**: 3.8+

### Project Directory
- **Location**: `/mnt/d/workspace/scripts/credit-report-automation/`
- **Contents**:
  - `credit_report_updater.py` - Main automation script
  - `test_1password.py` - Setup validation tool
  - `config.json` - Service configuration
  - `requirements.txt` - Python dependencies
  - `run.sh` - Quick launcher
  - `setup_1password_items.sh` - 1Password item creator
  - `venv/` - Python virtual environment

### Documentation
- `README.md` - Complete user guide
- `START_HERE.md` - Quick start guide
- `EXAMPLES.md` - 16+ usage examples
- `PROJECT_SUMMARY.md` - Technical overview
- `INSTALLATION_COMPLETE.md` - Setup validation
- `QUICKSTART.md` - 5-minute setup

---

## Quick Reference

### Essential Commands

```bash
# Test setup
cd /mnt/d/workspace/scripts/credit-report-automation
./venv/bin/python test_1password.py --vault Research

# Run all services
./run.sh --vault Research

# Run single service
./run.sh --vault Research --service equifax

# Headless mode
./run.sh --vault Research --headless

# Custom output
./run.sh --vault Research --output-dir /custom/path

# Get help
./venv/bin/python credit_report_updater.py --help
```

### 1Password Commands

```bash
# Sign in
eval $(op signin)

# List vaults
op vault list

# List items
op item list --vault Research

# Get item
op item get "Equifax Business" --vault Research --format json

# Create item
op item create --category=Login --title="Service Name" \
  --vault="Research" username="email" password="pass"
```

### Output Locations

```bash
# Default output
/mnt/d/OneDrive/Downloads/credit-reports/YYYYMMDD_HHMMSS/

# Session files
session_summary.json          # Overview
equifax_business_report.pdf   # Equifax PDF
equifax_data.json            # Equifax data
nav_business_report.pdf      # Nav PDF
nav_data.json               # Nav data
myfico_report.pdf           # myFICO PDF
myfico_data.json            # myFICO data
```

---

## Support & Resources

### Documentation Files
1. `START_HERE.md` - Begin here
2. `INSTALLATION_COMPLETE.md` - Setup validation
3. `QUICKSTART.md` - 5-minute start
4. `README.md` - Complete docs
5. `EXAMPLES.md` - Usage examples
6. This file - Complete reference

### External Resources
- [Playwright Documentation](https://playwright.dev/python/)
- [1Password CLI Documentation](https://developer.1password.com/docs/cli/)
- [Python Documentation](https://docs.python.org/3/)

### Troubleshooting Steps
1. Check error screenshots in output directory
2. Review `session_summary.json`
3. Run with `--headless` disabled
4. Validate 1Password setup with test script
5. Update selectors in `config.json` if needed

---

**Generated**: 2026-02-01
**Source**: Equifax Agent (a4ed7f8)
**Status**: Production-Ready ✅
**Next Step**: `./run.sh --vault Research`
