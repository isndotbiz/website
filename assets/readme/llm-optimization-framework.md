# LLM Optimization Framework

Research and evaluation framework for testing LLM behavior, cataloging attack techniques, and visualizing results through dashboards and mindmaps.

## Funder Snapshot
- Problem: LLM safety and performance require structured evaluation and measurable evidence.
- Solution: A framework that captures evaluations, organizes techniques, and visualizes results for decision makers.
- Differentiation: Combined taxonomy, OPML exports, and web dashboards for analysis and reporting.

## What Is Built
- Flask dashboard for evaluation stats, reports, and OPML browsing.
- Technique reference library and data generation scripts.
- Mindmap and visualization assets for interactive review.
- Deployment and verification scripts for hosting the dashboard.

## Architecture
```
Evaluation data -> SQLite/JSON -> Dashboard + Reports -> Mindmap and OPML exports
```

## Tech Stack
- Python, Flask
- SQLite
- HTML/JS visualization assets
- OPML and JSON conversion utilities

## Repository Structure
```
app_final.py                Flask dashboard
techniques_*.md             Technique library and summaries
techniques_mindmap.html     Visualization assets
setup_*.sh                  Deployment and verification scripts
```

## Status
Documentation and tooling are present for dashboard deployment and technique cataloging. Metrics and model results can be populated from evaluation databases when available.

## License
Internal research. See repo notes.
