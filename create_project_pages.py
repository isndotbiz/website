#!/usr/bin/env python3
"""Generate project deep-dive HTML pages"""

projects = [
    {
        "filename": "project-truenas-infrastructure.html",
        "title": "TrueNAS Infrastructure & AI/ML Platform",
        "category": "Infrastructure & Platform",
        "description": "Production-grade on-prem infrastructure powering AI/ML workloads, data services, and observability",
        "status": "Production",
        "platform": "TrueNAS Scale",
        "overview": "This platform is the operational backbone for the company. It delivers a multi-service, AI-ready environment with automated secret management, monitoring, and disaster recovery.",
        "capabilities": [
            {"icon": "🐳", "title": "Containerized AI Services", "desc": "Docker-based platform running AI/ML services with automated orchestration", "techs": ["Docker Compose", "Portainer", "Traefik", "Tailscale"]},
            {"icon": "🤖", "title": "AI Router & Model Management", "desc": "OpenAI-compatible API router for local and external models", "techs": ["Ollama", "llama.cpp", "OpenAI API", "Model versioning"]},
            {"icon": "🗄️", "title": "Multi-Database Platform", "desc": "Enterprise-grade database stack supporting diverse workloads", "techs": ["PostgreSQL", "Neo4j", "Redis", "ClickHouse", "ChromaDB"]},
            {"icon": "📚", "title": "RAG Pipeline", "desc": "Complete retrieval-augmented generation infrastructure", "techs": ["Document ingestion", "Vector embeddings", "Semantic search"]},
            {"icon": "📊", "title": "Observability Stack", "desc": "Production-grade monitoring with metrics, logs, and tracing", "techs": ["Prometheus", "Grafana", "Loki", "Jaeger"]},
            {"icon": "🔐", "title": "Security & Secrets", "desc": "Automated secret injection with audit-friendly runbooks", "techs": ["1Password", "Secret rotation", "Security audits"]}
        ],
        "tech_stack": {
            "Infrastructure": ["TrueNAS Scale", "Docker Compose", "Portainer", "Traefik", "Tailscale"],
            "Databases": ["PostgreSQL", "Redis", "Neo4j", "ClickHouse", "MariaDB", "ChromaDB"],
            "AI/ML": ["Ollama", "llama.cpp", "ChromaDB", "OpenAI API"],
            "Observability": ["Prometheus", "Grafana", "Loki", "Jaeger"]
        },
        "evidence": [
            {"icon": "📁", "title": "Extensive Automation", "desc": "Complete suite of deployment, backup, and verification scripts"},
            {"icon": "🔍", "title": "Monitoring & Alerting", "desc": "Production monitoring with dashboards and alerts"},
            {"icon": "🤖", "title": "RAG Pipeline", "desc": "Complete RAG system with document processing"},
            {"icon": "🔐", "title": "Security Hardening", "desc": "Comprehensive security audits and secret management"}
        ]
    },
    {
        "filename": "project-videogen-youtube.html",
        "title": "VideoGen YouTube Automation",
        "category": "Content Automation",
        "description": "End-to-end pipeline converting web articles into production-ready video assets for YouTube",
        "status": "Production",
        "platform": "Node.js & Python",
        "overview": "Automated pipeline that converts web articles into production-ready video assets, scripts, and upload workflows. Eliminates expensive manual video production while maintaining consistent quality.",
        "capabilities": [
            {"icon": "🎬", "title": "Orchestrated Pipeline", "desc": "Complete workflow from scraping to video assembly", "techs": ["Node.js", "Python", "Firecrawl", "Axios"]},
            {"icon": "✍️", "title": "Script Generation", "desc": "AI-powered script and storyboard generation", "techs": ["GPT integration", "Storyboards", "Narration scripts"]},
            {"icon": "🎨", "title": "Visual Assets", "desc": "Image and animation generation integrations", "techs": ["fal.ai", "Runway", "Multi-provider"]},
            {"icon": "🎙️", "title": "Narration & Assembly", "desc": "Voice narration and video assembly automation", "techs": ["ElevenLabs", "Descript", "FFmpeg"]},
            {"icon": "☁️", "title": "Storage & Upload", "desc": "AWS S3 storage and YouTube OAuth automation", "techs": ["AWS S3", "YouTube API", "OAuth"]},
            {"icon": "📚", "title": "Operational Runbooks", "desc": "Extensive documentation and automation scripts", "techs": ["Guides", "Runbooks", "Automation"]}
        ],
        "tech_stack": {
            "Core": ["Node.js", "Python", "Firecrawl", "Axios", "Cheerio"],
            "AI Services": ["fal.ai", "Runway", "ElevenLabs", "Descript"],
            "Storage": ["AWS S3", "YouTube OAuth"],
            "Automation": ["Orchestration scripts", "Workflow management"]
        },
        "evidence": [
            {"icon": "🎯", "title": "Pipeline Entrypoint", "desc": "orchestrate.js and multiple automation scripts"},
            {"icon": "📖", "title": "Extensive Documentation", "desc": "Comprehensive runbooks and guides"},
            {"icon": "🗺️", "title": "Roadmap & Status", "desc": "PROJECT_OVERVIEW_AND_ROADMAP.md with metrics"},
            {"icon": "🔧", "title": "Production Scripts", "desc": "Battle-tested automation tooling"}
        ]
    }
]
# Truncated for brevity - full script continues...

