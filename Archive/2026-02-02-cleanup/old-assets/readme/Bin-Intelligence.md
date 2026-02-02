# BIN Intelligence System

BIN intelligence platform for e-commerce fraud analysis, enrichment, and reporting.

## Funder Snapshot
- Problem: Fraud teams need reliable BIN insights to detect and prevent card-not-present abuse.
- Solution: Automated BIN ingestion, enrichment, classification, and analytics.
- Differentiation: Combined scraping, Neutrino enrichment, and live dashboard plus API.

## What Is Built
- Flask web dashboard and REST API.
- BIN enrichment pipeline using Neutrino API.
- Fraud feed scraping and exploit classification.
- PostgreSQL or SQLite storage via SQLAlchemy.
- CSV export and data quality tooling.

## Architecture
```
Fraud feeds -> BIN enrichment -> Database -> API + dashboard + exports
```

## Tech Stack
- Python 3.11, Flask, SQLAlchemy
- PostgreSQL or SQLite
- Neutrino BIN Lookup API
- Bootstrap and Chart.js UI

## Repository Structure
```
main.py             Flask app and API
models.py           SQLAlchemy schema
bin_enricher.py     Enrichment pipeline
fraud_feed.py       Scrapers
templates/          Dashboard UI
```

## Quick Start
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

export DATABASE_URL="sqlite:///bin_intelligence.db"
export NEUTRINO_API_USER_ID="your_user_id"
export NEUTRINO_API_KEY="your_api_key"

python main.py
```

## Documentation
- API.md
- DEPLOYMENT.md
- CHANGELOG.md

## License
See LICENSE in the repo.
