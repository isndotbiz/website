# TrueNAS Infrastructure and AI/ML Platform

Production-grade on-prem infrastructure that powers AI/ML workloads, data services, and observability using a containerized stack on TrueNAS Scale.

## Funder Snapshot
- Problem: AI products need reliable, cost-efficient infrastructure with strong security and observability.
- Solution: A containerized platform with 50+ services, automated secret management, and repeatable deployment.
- Differentiation: Integrated AI router, RAG pipeline, and enterprise-grade monitoring on on-prem hardware.

## What Is Built
- Container platform with AI/ML services, databases, and web tooling.
- AI Router with OpenAI-compatible APIs for local and external models.
- RAG pipeline with crawling, document parsing, and vector storage.
- Monitoring stack (Prometheus, Grafana, Loki, Jaeger).
- Backup and disaster recovery automation (ZFS replication and multi-target strategy).
- 1Password-based secret injection and audit-friendly runbooks.

## Architecture (Sanitized)
```
Internet -> Reverse proxy -> Container services
AI stack -> AI router -> Local and external model providers
Data stack -> PostgreSQL, Redis, Neo4j, ClickHouse, MinIO
Observability -> Prometheus, Grafana, Loki, Jaeger
```

## Tech Stack
- TrueNAS Scale, Docker Compose, Portainer
- Traefik, Tailscale
- PostgreSQL, Redis, Neo4j, ClickHouse, MariaDB, MinIO
- Ollama, llama.cpp, ChromaDB
- Prometheus, Grafana, Loki, Jaeger

## Repository Structure
```
monitoring/          Monitoring and alerting configuration
rag-system/          RAG pipeline and indexing utilities
ai-router/           AI router services and model management
scripts/             Deployment, backup, and verification scripts
security/            Security hardening and audits
```

## Security Note
Internal network details, credentials, and hostnames are intentionally omitted from this README. Use internal runbooks when operating the system.

## Documentation
The repo contains extensive deployment, validation, and system status reports in the top-level markdown files and subdirectories.

## License
Private repository. All rights reserved.
