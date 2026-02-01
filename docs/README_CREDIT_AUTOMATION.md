# Credit Report Automation - Start Here

**Extracted from Equifax Agent on 2026-02-01**

## What You Have

A complete, production-ready automation system that retrieves credit reports from:
- **Equifax Business** - Business credit reports
- **Nav** - Business credit monitoring
- **myFICO** - Personal FICO scores (all 3 bureaus)

**Key Feature**: Uses 1Password CLI for 100% secure credential management - **zero hardcoded passwords!**

## Files in This Directory

| File | Description |
|------|-------------|
| `credit_report_automation.py` | Main automation script (620 lines) |
| `CREDIT_AUTOMATION_QUICKSTART.md` | 5-minute quick start guide - **START HERE** |
| `CREDIT_REPORT_AUTOMATION.md` | Complete documentation (1,090 lines) |
| `CREDIT_AUTOMATION_INDEX.md` | File index and overview |
| `CREDIT_AUTOMATION_SUMMARY.txt` | Text summary of extraction |

## Full Project Location

The complete project with virtual environment and all dependencies is located at:

```
/mnt/d/workspace/scripts/credit-report-automation/
```

This includes:
- Virtual environment with Playwright installed
- Test scripts for validation
- Configuration files
- Helper scripts
- Complete documentation suite

## Quick Start (5 Minutes)

```bash
cd /mnt/d/workspace/scripts/credit-report-automation

# 1. Test setup
./venv/bin/python test_1password.py --vault Research

# 2. Create 1Password items (if needed)
#    Items needed: "Equifax Business", "Nav", "myFICO"

# 3. Run automation
./run.sh --vault Research

# 4. Check output
ls -lh /mnt/d/OneDrive/Downloads/credit-reports/*/
```

## Documentation Order

Read in this order:

1. **CREDIT_AUTOMATION_QUICKSTART.md** ← Start here (5-minute guide)
2. **CREDIT_AUTOMATION_INDEX.md** ← Overview of all files
3. **CREDIT_REPORT_AUTOMATION.md** ← Complete reference
4. **Full project docs** at `/mnt/d/workspace/scripts/credit-report-automation/`

## Key Features

✅ **Secure**: 1Password CLI integration (no hardcoded passwords)
✅ **Smart**: 2FA detection and handling
✅ **Reliable**: Comprehensive error handling with screenshots
✅ **Complete**: PDF reports + JSON structured data
✅ **Documented**: 2,500+ lines of documentation

## Common Commands

```bash
# Test 1Password setup
cd /mnt/d/workspace/scripts/credit-report-automation
./venv/bin/python test_1password.py --vault Research

# Run all services
./run.sh --vault Research

# Run single service
./run.sh --vault Research --service equifax

# Headless mode (no browser window)
./run.sh --vault Research --headless
```

## Output

Each run creates a timestamped directory with:
- `session_summary.json` - Overview of the run
- `equifax_business_report.pdf` + `equifax_data.json`
- `nav_business_report.pdf` + `nav_data.json`
- `myfico_report.pdf` + `myfico_data.json`
- Error screenshots (if any issues)

Default location: `/mnt/d/OneDrive/Downloads/credit-reports/YYYYMMDD_HHMMSS/`

## Need Help?

- **Setup issues**: See `CREDIT_REPORT_AUTOMATION.md` → "Troubleshooting"
- **Usage examples**: See `/mnt/d/workspace/scripts/credit-report-automation/EXAMPLES.md`
- **Test setup**: Run `test_1password.py --vault Research`

## Prerequisites

- [x] Python 3.8+ (installed)
- [x] 1Password CLI (needs to be installed if not already)
- [x] Virtual environment with Playwright (already set up in project directory)

## Installation Check

```bash
# Check 1Password CLI
op --version
op account list

# If not installed:
# sudo apt install 1password-cli
# eval $(op signin)
```

## Next Step

**Read this file first**: `CREDIT_AUTOMATION_QUICKSTART.md`

Then run your first test:
```bash
cd /mnt/d/workspace/scripts/credit-report-automation
./run.sh --vault Research --service equifax
```

---

**Status**: ✅ Production-Ready  
**Extracted**: 2026-02-01  
**Source**: Equifax Agent (agent-a4ed7f8.jsonl)
