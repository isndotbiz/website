# Opportunity Research Bot

AI-powered pipeline that discovers, analyzes, and stores business opportunities from public sources.

## Funder Snapshot
- Problem: Finding actionable business opportunities is time-consuming and unstructured.
- Solution: Automated scraping plus LLM analysis with semantic search for rapid discovery.
- Differentiation: Multi-source ingestion, local LLM scoring, and RAG-based retrieval.

## What Is Built
- Scrapers for Reddit, Indie Hackers, and Google dorking.
- LLM analysis pipeline with structured scoring (automation, legitimacy, effort).
- ChromaDB-based semantic search and metadata filtering.
- Production, demo, and personalization pipelines.
- Cron automation and setup scripts.

## Architecture
```
Sources -> Scrapers -> LLM analysis -> Vector DB -> Query interface
```

## Tech Stack
- Python
- PRAW, BeautifulSoup, requests
- ChromaDB vector database
- Local LLM analysis pipeline

## Repository Structure
```
production_opportunity_pipeline.py   Main pipeline
scrapers/                            Source scrapers and config
data/                                ChromaDB storage and cache
query_opportunities.py               Search interface
setup_*.sh                           Automation and setup
```

## Quick Start
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python production_opportunity_pipeline.py --demo
python query_opportunities.py "high automation under $1000"
```

## Documentation
- RUN_ME_FIRST.md
- ARCHITECTURE.md
- README_PRODUCTION.md

## License
MIT (see LICENSE if present).
