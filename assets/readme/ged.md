# GEDCOM Processing and Family Tree Cleaning System

Professional-grade pipeline for cleaning, standardizing, and validating GEDCOM 5.5.1 genealogical data with audit trails and zero data loss guarantees.

## Funder Snapshot
- Problem: Genealogy datasets are inconsistent, hard to validate, and expensive to clean manually.
- Solution: Automated GEDCOM processing with integrity-first safeguards and repeatable workflows.
- Differentiation: Auditable changes, backups and rollback, and relationship-preserving deduplication.
- Proof in repo: Production-ready CLI (gedfix), processing scripts, and full execution reports.

## What Is Built
- Python package and CLI for scan, fix, dedupe, and validation operations.
- Rule-based normalization for dates, names, and places with AutoFix notes.
- Relationship-preserving deduplication and safe merge logic.
- Data integrity verification, backups, and rollback tooling.
- Comprehensive processing reports and methodology documentation.

## Architecture (High Level)
```
Input GEDCOM
  -> Scan and analyze issues
  -> Normalize dates, names, places
  -> Deduplicate facts and individuals
  -> Validate relationships and integrity
  -> Export cleaned GEDCOM + reports
```

## Documented Results (Repository Run)
- 2,272 date issues resolved with AutoFix notes.
- 181 name/place standardizations applied.
- 584 media files reattached with linking suggestions.
- 100% data integrity preserved with backups and verification.
- See PROJECT_COMPLETE.md for full details.

## Tech Stack
- Python 3.11
- ged4py, click, rapidfuzz, python-dateutil
- CLI entrypoint: gedfix

## Repository Structure
```
gedfix/                  Core library and CLI
scripts/                 Processing, integrity, and rollback utilities
data/processing/          Workspaces, exports, and reports
docs/                     Methodology and analysis docs
```

## Quick Start
```
python -m venv venv
source venv/bin/activate
pip install -e .

gedfix scan input.ged --report scan_report.json
gedfix fix input.ged --out cleaned.ged --level standard --backup-dir ./backups
./scripts/verify_data_integrity.sh input.ged cleaned.ged
```

## Documentation
- PROCESSING_PLAN.md
- DATA_INTEGRITY_TOOLS.md
- PROJECT_COMPLETE.md

## License
MIT
