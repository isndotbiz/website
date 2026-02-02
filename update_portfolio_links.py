# Create portfolio page with 8 project cards linking to deep-dive pages
projects = [
    ("TrueNAS Infrastructure", "project-truenas-infrastructure.html", "On-prem AI/ML platform with zero cloud costs", "Infrastructure"),
    ("VideoGen YouTube", "project-videogen-youtube.html", "Automated video production pipeline", "Content"),
    ("BIN Intelligence", "project-bin-intelligence.html", "Fraud detection and risk analysis", "Security"),
    ("CLI Standards", "project-cli.html", "Engineering excellence framework", "DevOps"),
    ("ComfyUI Automation", "project-comfyui-automation.html", "AI image generation at scale", "AI/ML"),
    ("GEDCOM Processing", "project-ged.html", "Genealogy data integrity platform", "Data"),
    ("LLM Optimization", "project-llm-optimization.html", "AI model evaluation framework", "Research"),
    ("Opportunity Bot", "project-opportunity-bot.html", "Automated business discovery", "AI/ML")
]

html = """
<section class="section portfolio">
    <div class="container">
        <div class="section-header centered">
            <span class="section-label">Our Work</span>
            <h2 class="section-title">Project Portfolio</h2>
            <p class="section-description">Deep-dive into our technical achievements</p>
        </div>
        <div class="portfolio-grid">
"""

for title, url, desc, category in projects:
    html += f'''
            <a href="{url}" class="portfolio-card lift-on-hover">
                <span class="portfolio-category">{category}</span>
                <h3>{title}</h3>
                <p>{desc}</p>
                <span class="portfolio-link">View Details →</span>
            </a>'''

html += """
        </div>
    </div>
</section>
"""

print(html)
