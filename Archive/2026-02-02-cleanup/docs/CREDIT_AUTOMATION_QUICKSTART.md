# Credit Report Automation - Quick Start Guide

**5-Minute Setup for Equifax, Nav, and myFICO Automation**

---

## Prerequisites Checklist

- [ ] Python 3.8+ installed
- [ ] 1Password account with CLI access
- [ ] Accounts on Equifax, Nav, and myFICO
- [ ] WSL or Linux environment

---

## Step 1: Verify Installation (1 minute)

```bash
cd /mnt/d/workspace/scripts/credit-report-automation

# Check 1Password CLI
op --version
op account list

# If not installed:
# sudo apt install 1password-cli
# eval $(op signin)
```

---

## Step 2: Test 1Password Setup (1 minute)

```bash
# Test credential retrieval
./venv/bin/python test_1password.py --vault Research
```

**Expected Output:**
```
✓ 1Password CLI installed: 2.32.0
✓ Signed in to 1Password
✓ Retrieved credentials for: Equifax Business
✓ Retrieved credentials for: Nav
✓ Retrieved credentials for: myFICO

3/3 items configured correctly
```

**If items are missing**, create them in 1Password:

```bash
# Interactive setup
./setup_1password_items.sh

# OR manually in 1Password app:
# Create Login items with these exact names:
#   - "Equifax Business"
#   - "Nav"
#   - "myFICO"
```

---

## Step 3: Run First Test (2 minutes)

```bash
# Test with single service first (Equifax)
./run.sh --vault Research --service equifax
```

**What happens:**
1. Browser opens automatically
2. Navigates to Equifax
3. Enters credentials from 1Password
4. Handles 2FA (if enabled - complete it manually)
5. Captures report as PDF + JSON
6. Closes browser

**Output Location:**
```
/mnt/d/OneDrive/Downloads/credit-reports/20260201_HHMMSS/
├── equifax_business_report.pdf
├── equifax_data.json
└── session_summary.json
```

---

## Step 4: Run All Services (5-10 minutes)

```bash
# Run all three services
./run.sh --vault Research
```

**Services Automated:**
1. **Equifax** - Business credit report
2. **Nav** - Business credit scores
3. **myFICO** - Personal FICO scores (3 bureaus)

**Complete Output:**
```
/mnt/d/OneDrive/Downloads/credit-reports/20260201_143022/
├── session_summary.json           # Overview of entire run
├── equifax_business_report.pdf    # Equifax PDF
├── equifax_data.json              # Equifax structured data
├── nav_business_report.pdf        # Nav PDF
├── nav_data.json                  # Nav structured data
├── myfico_report.pdf              # myFICO PDF
└── myfico_data.json               # myFICO structured data
```

---

## Common Commands

```bash
# Test setup
./venv/bin/python test_1password.py --vault Research

# Run all services (with browser visible)
./run.sh --vault Research

# Run all services (headless mode)
./run.sh --vault Research --headless

# Run single service
./run.sh --vault Research --service equifax
./run.sh --vault Research --service nav
./run.sh --vault Research --service myfico

# Custom output directory
./run.sh --vault Research --output-dir /custom/path

# Get help
./venv/bin/python credit_report_updater.py --help
```

---

## Troubleshooting

### "Not signed in to 1Password"
```bash
eval $(op signin)
```

### "Item not found"
```bash
# List items in vault
op item list --vault Research | grep -i equifax

# Create missing item
./setup_1password_items.sh
```

### "Browser doesn't open"
```bash
# Check Playwright installation
./venv/bin/playwright --version

# Reinstall if needed
source venv/bin/activate
playwright install chromium
```

### "2FA timeout"
- Complete 2FA within 5 minutes
- Have phone ready before starting
- Watch browser window for prompts

### "Selectors not working"
- Website may have changed
- Update `config.json` with new selectors
- Run with browser visible to debug

---

## Advanced Usage

### Schedule Monthly Updates

```bash
# Edit crontab
crontab -e

# Add this line (runs 1st of month at 8 AM)
0 8 1 * * cd /mnt/d/workspace/scripts/credit-report-automation && ./run.sh --vault Research --headless >> /tmp/credit_reports.log 2>&1
```

### Integrate with Python

```python
from credit_report_updater import CreditReportAutomation
from playwright.sync_api import sync_playwright

automation = CreditReportAutomation(headless=True, vault="Research")
with sync_playwright() as playwright:
    automation.setup_browser(playwright)
    results = automation.run_full_automation()

    print(f"✓ Retrieved {len(results['reports'])} reports")
    automation.context.close()
    automation.browser.close()
```

### Import to Database

```python
import json
import sqlite3
from pathlib import Path

def import_latest():
    latest = max(
        Path("/mnt/d/OneDrive/Downloads/credit-reports").glob("*/"),
        key=lambda p: p.name
    )

    conn = sqlite3.connect("/mnt/d/workspace/credit_data.db")
    cursor = conn.cursor()

    # Read Equifax data
    with open(latest / "equifax_data.json") as f:
        data = json.load(f)

    # Insert to database
    cursor.execute("""
        INSERT INTO credit_reports (source, score, retrieved_at)
        VALUES (?, ?, ?)
    """, (data["source"], data["business_score"], data["retrieved_at"]))

    conn.commit()
    conn.close()

import_latest()
```

---

## Security Notes

✅ **Safe Practices**
- Uses 1Password CLI (no hardcoded passwords)
- Credentials never stored in code or config
- Output directory has restricted permissions
- Session logs for audit trail

⚠️ **Important**
- Protect your 1Password master password
- Don't share output files (contain sensitive data)
- Regularly review session logs
- Keep 1Password CLI updated

---

## File Locations

| File | Location |
|------|----------|
| **Main Script** | `/mnt/d/workspace/credit_report_automation.py` |
| **Project Directory** | `/mnt/d/workspace/scripts/credit-report-automation/` |
| **Output (Default)** | `/mnt/d/OneDrive/Downloads/credit-reports/` |
| **Documentation** | `/mnt/d/workspace/CREDIT_REPORT_AUTOMATION.md` |

---

## Next Steps

1. **Today**: Run your first automation
2. **This Week**: Set up monthly cron job
3. **This Month**: Integrate with your database
4. **Ongoing**: Monitor credit scores monthly

---

## Resources

- **Complete Documentation**: `CREDIT_REPORT_AUTOMATION.md`
- **Usage Examples**: `/mnt/d/workspace/scripts/credit-report-automation/EXAMPLES.md`
- **Project README**: `/mnt/d/workspace/scripts/credit-report-automation/README.md`

---

## Quick Test

```bash
# Complete test sequence (3 minutes)
cd /mnt/d/workspace/scripts/credit-report-automation

# 1. Verify 1Password
eval $(op signin)
./venv/bin/python test_1password.py --vault Research

# 2. Test single service
./run.sh --vault Research --service equifax

# 3. Check output
ls -lh /mnt/d/OneDrive/Downloads/credit-reports/*/
```

---

**Ready to start?**
```bash
./run.sh --vault Research
```

**Status**: ✅ Production-Ready
**Setup Time**: 5 minutes
**Run Time**: 5-10 minutes (all 3 services)
