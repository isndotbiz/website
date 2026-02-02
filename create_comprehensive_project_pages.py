#!/usr/bin/env python3
"""
Generate 9 comprehensive project pages with extensive content and multiple images.
Each page includes: Hero, Overview, Features, Technology, Use Cases, Evidence sections.
"""

# Project data with extensive content
projects_data = {
    'project-gedcom-platform.html': {
        'title': 'GEDCOM Data Integrity Platform',
        'subtitle': 'Production-grade system for cleaning, standardizing, and validating GEDCOM 5.5.1 datasets with audit trails and zero data loss guarantees',
        'category': 'Data Analytics & Platform',
        'hero_bg': 'infrastructure.webp',
        'tech_stack': ['Python 3.11', 'ged4py', 'rapidfuzz', 'python-dateutil', 'Click CLI', 'pytest'],
        'images': ['infrastructure', 'rag_bi', 'enterprise_automation'],
    },
    'project-comfyui-automation.html': {
        'title': 'ComfyUI Flux WAN Automation',
        'subtitle': 'Automation suite for running ComfyUI with Flux models, delivering reproducible workflows and scalable batch generation',
        'category': 'AI Infrastructure & Automation',
        'hero_bg': 'ai_research.webp',
        'tech_stack': ['Python 3.10+', 'ComfyUI API', 'requests', 'aiohttp', 'Pillow', 'fal-client'],
        'images': ['ai_research', 'infrastructure', 'enterprise_automation'],
    },
    'project-spiritatlas.html': {
        'title': 'SpiritAtlas',
        'subtitle': 'Privacy-first Android app delivering spiritual insights with modern architecture, encrypted storage, and consent-gated AI',
        'category': 'Mobile Application',
        'hero_bg': 'androidaps_health.webp',
        'tech_stack': ['Kotlin', 'Android SDK 34', 'Jetpack Compose', 'Hilt', 'EncryptedSharedPreferences'],
        'images': ['androidaps_health', 'ai_research', 'enterprise_automation'],
    },
    'project-videogen-youtube.html': {
        'title': 'VideoGen YouTube Pipeline',
        'subtitle': 'Automated pipeline converting articles into production-ready video assets with AI-powered script generation and editing',
        'category': 'Content Automation & AI',
        'hero_bg': 'enterprise_automation.webp',
        'tech_stack': ['Node.js', 'Python', 'Firecrawl', 'fal.ai', 'ElevenLabs', 'Runway', 'AWS S3'],
        'images': ['enterprise_automation', 'ai_research', 'infrastructure'],
    },
    'project-bin-intelligence.html': {
        'title': 'BIN Intelligence System',
        'subtitle': 'BIN intelligence platform for e-commerce fraud analysis, enrichment, and real-time risk scoring dashboards',
        'category': 'Fraud Prevention & Analytics',
        'hero_bg': 'rag_bi.webp',
        'tech_stack': ['Python 3.11', 'Flask', 'SQLAlchemy', 'PostgreSQL', 'Neutrino API', 'Chart.js'],
        'images': ['rag_bi', 'enterprise_automation', 'ai_research'],
    },
    'project-llm-optimization.html': {
        'title': 'LLM Optimization Framework',
        'subtitle': 'Research framework for testing LLM behavior, cataloging techniques, and visualizing evaluation results',
        'category': 'AI Research & Evaluation',
        'hero_bg': 'ai_research.webp',
        'tech_stack': ['Python', 'Flask', 'SQLite', 'HTML/JS Visualization', 'OPML Processing'],
        'images': ['ai_research', 'infrastructure', 'rag_and_search'],
    },
    'project-opportunity-bot.html': {
        'title': 'AI Opportunity Research Bot',
        'subtitle': 'AI-powered pipeline discovering and analyzing business opportunities from multiple sources with local LLM scoring',
        'category': 'Market Intelligence & AI',
        'hero_bg': 'opportunity_bot.webp',
        'tech_stack': ['Python', 'PRAW', 'BeautifulSoup', 'ChromaDB', 'Local LLM', 'RAG'],
        'images': ['opportunity_bot', 'ai_research', 'rag_and_search'],
    },
    'project-truenas-infrastructure.html': {
        'title': 'TrueNAS AI/ML Infrastructure',
        'subtitle': 'Production-grade on-premise infrastructure powering AI/ML workloads with enterprise observability and automated disaster recovery',
        'category': 'Enterprise Infrastructure',
        'hero_bg': 'infrastructure.webp',
        'tech_stack': ['TrueNAS Scale', 'Docker', 'Ollama', 'Neo4j', 'Qdrant', 'Redis', 'Prometheus'],
        'images': ['infrastructure', 'enterprise_automation', 'rag_and_search'],
    },
    'project-cli-standards.html': {
        'title': 'CLI Engineering Standards',
        'subtitle': 'Internal blueprint standardizing CLI project structure, testing, and quality gates for rapid tooling delivery',
        'category': 'Engineering Excellence',
        'hero_bg': 'enterprise_automation.webp',
        'tech_stack': ['TypeScript', 'Node.js', 'Testing Framework', 'ESLint', 'Conventional Commits'],
        'images': ['enterprise_automation', 'infrastructure', 'ai_research'],
    },
}

print(f"✓ Prepared {len(projects_data)} project configurations")
print("Ready to generate comprehensive HTML pages")
