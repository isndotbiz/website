#!/usr/bin/env python3
"""
Bulk Image Generator for ISN.BIZ Website
Generates 20+ images using FAL GPT-Image-1.5 API with LOW quality for speed
"""

import fal_client
import os
import json
import base64
from pathlib import Path
from PIL import Image
import io

# FAL API key
os.environ['FAL_KEY'] = '64b786c3-d6b1-4fbb-9d46-9211ceea552f:d472cdf8c68b4fe873557ca33bfb25eb'

# Output directory
OUTPUT_DIR = Path('assets/generated')
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Image generation prompts
PROMPTS = {
    # Hero backgrounds (4 variations)
    'hero_tech_grid': 'abstract technology grid pattern, blue and cyan geometric shapes, futuristic digital network, clean modern aesthetic, dark background with glowing elements, 4k, professional',
    'hero_data_flow': 'flowing data streams, digital information network, blue and cyan particle effects, abstract tech visualization, dark sleek background, modern corporate style',
    'hero_ai_neural': 'neural network visualization, artificial intelligence concept art, glowing blue nodes and connections, abstract tech pattern, professional business aesthetic',
    'hero_cloud_tech': 'cloud computing abstract visualization, distributed network architecture, blue and cyan tech elements, modern professional design, dark background',

    # Project illustrations (6 projects × 2-3 each = 12-18 images)
    'project_ai_chat': 'AI chatbot interface with modern UI, conversational AI assistant, clean blue interface design, professional dashboard mockup, minimalist style',
    'project_ai_analysis': 'AI data analysis dashboard, charts and graphs, machine learning visualization, blue and cyan color scheme, modern tech interface',
    'project_cloud_servers': 'cloud server infrastructure diagram, distributed computing network, blue tech visualization, modern isometric style, professional',
    'project_cloud_scale': 'scalable cloud architecture, load balancing visualization, modern tech infrastructure, blue and cyan elements, professional diagram',
    'project_enterprise_dashboard': 'enterprise software dashboard, business analytics interface, modern UI design, blue color scheme, professional mockup',
    'project_enterprise_workflow': 'business process workflow diagram, enterprise automation visualization, modern clean design, blue and cyan accents',
    'project_data_pipeline': 'data pipeline architecture, ETL process visualization, blue tech diagram, modern professional style, abstract representation',
    'project_data_analytics': 'data analytics dashboard with charts, business intelligence visualization, modern UI, blue and cyan color scheme',
    'project_opportunity_bot': 'AI opportunity discovery interface, automated research dashboard, modern blue UI, professional design',
    'project_opportunity_search': 'search and discovery interface, AI-powered recommendations, clean modern design, blue color scheme',
    'project_infrastructure': 'server infrastructure diagram, network topology visualization, blue and cyan tech elements, professional isometric style',
    'project_infrastructure_monitoring': 'infrastructure monitoring dashboard, system health metrics, modern UI design, blue color scheme',
    'project_portfolio_browser': 'portfolio browsing interface, project showcase dashboard, modern clean UI, blue and cyan accents',
    'project_portfolio_analytics': 'portfolio analytics dashboard, project metrics visualization, professional UI design, blue color scheme',

    # Abstract tech elements (4 images)
    'tech_particles': 'abstract technology particles floating in space, blue and cyan glowing elements, dark background, modern digital art',
    'tech_waves': 'smooth flowing tech waves, digital wave pattern, blue gradient, abstract modern design, clean aesthetic',
    'tech_hexagons': 'hexagonal tech pattern, geometric network structure, blue and cyan colors, futuristic design, transparent elements',
    'tech_circuits': 'abstract circuit board pattern, electronic pathways, blue glowing traces, modern tech aesthetic, dark background',

    # Company/office scenes (3 images)
    'office_modern': 'modern tech office workspace, clean minimal design, blue accent colors, professional corporate environment, natural lighting',
    'office_collaboration': 'team collaboration in modern tech office, people working on computers, blue and white interior, professional atmosphere',
    'office_server_room': 'modern server room with blue lighting, data center infrastructure, professional tech environment, clean organized racks',

    # Technology visualizations (3 images)
    'tech_globe_network': 'digital globe with network connections, global technology visualization, blue and cyan lines, dark background, modern',
    'tech_code_matrix': 'abstract code visualization, digital matrix effect, blue and cyan code streams, modern tech aesthetic',
    'tech_api_network': 'API network diagram, microservices architecture, blue tech visualization, modern professional style',

    # Dashboard mockups (3 images)
    'dashboard_metrics': 'business metrics dashboard, KPI visualization, modern UI design, blue color scheme, charts and graphs',
    'dashboard_realtime': 'real-time monitoring dashboard, live data feeds, modern interface, blue and cyan elements, professional',
    'dashboard_control': 'control panel dashboard, system management interface, modern clean UI, blue color scheme, professional design',
}

def generate_image(prompt_key, prompt_text, index):
    """Generate a single image using FAL API"""
    print(f"\n[{index}/{len(PROMPTS)}] Generating: {prompt_key}")
    print(f"Prompt: {prompt_text[:80]}...")

    try:
        result = fal_client.subscribe(
            "fal-ai/fast-turbo-diffusion",
            arguments={
                "prompt": prompt_text,
                "image_size": "landscape_16_9",  # Good for web backgrounds
                "num_inference_steps": 4,  # Fast generation
                "num_images": 1,
                "enable_safety_checker": False,  # Faster
            },
            with_logs=False
        )

        # Get the image (either URL or base64)
        if 'images' in result and len(result['images']) > 0:
            image_data = result['images'][0]
            image_url = image_data.get('url')

            if image_url:
                # Check if it's a base64 data URL
                if image_url.startswith('data:image'):
                    # Extract base64 data
                    base64_data = image_url.split(',')[1]
                    image_bytes = base64.b64decode(base64_data)
                    img = Image.open(io.BytesIO(image_bytes))
                else:
                    # Download from URL
                    import requests
                    response = requests.get(image_url, timeout=30)
                    if response.status_code == 200:
                        img = Image.open(io.BytesIO(response.content))
                    else:
                        print(f"[FAIL] Failed to download: HTTP {response.status_code}")
                        return False

                # Save as WebP
                output_path = OUTPUT_DIR / f"{prompt_key}.webp"
                img.save(output_path, 'WEBP', quality=85)
                print(f"[OK] Saved: {output_path}")
                return True
            else:
                print(f"[FAIL] No image URL in result")
        else:
            print(f"[FAIL] No images in result")

        return False

    except Exception as e:
        print(f"[ERROR] {str(e)}")
        return False

def main():
    """Generate all images"""
    print("=" * 80)
    print("BULK IMAGE GENERATION FOR ISN.BIZ")
    print("=" * 80)
    print(f"Total prompts: {len(PROMPTS)}")
    print(f"Output directory: {OUTPUT_DIR}")
    print(f"Format: WebP")
    print(f"Quality: LOW (for speed)")
    print("=" * 80)

    # Generate all images
    success_count = 0
    failed_prompts = []

    for index, (prompt_key, prompt_text) in enumerate(PROMPTS.items(), 1):
        success = generate_image(prompt_key, prompt_text, index)
        if success:
            success_count += 1
        else:
            failed_prompts.append(prompt_key)

    # Summary
    print("\n" + "=" * 80)
    print("GENERATION COMPLETE")
    print("=" * 80)
    print(f"[OK] Successfully generated: {success_count}/{len(PROMPTS)}")
    print(f"[FAIL] Failed: {len(failed_prompts)}")
    if failed_prompts:
        print("\nFailed prompts:")
        for key in failed_prompts:
            print(f"  - {key}")
    print(f"\nImages saved to: {OUTPUT_DIR.absolute()}")
    print("=" * 80)

    # Create catalog file
    catalog = {
        'total_images': success_count,
        'output_directory': str(OUTPUT_DIR),
        'format': 'webp',
        'quality': 'low',
        'categories': {
            'hero_backgrounds': [k for k in PROMPTS.keys() if k.startswith('hero_')],
            'project_illustrations': [k for k in PROMPTS.keys() if k.startswith('project_')],
            'tech_elements': [k for k in PROMPTS.keys() if k.startswith('tech_')],
            'office_scenes': [k for k in PROMPTS.keys() if k.startswith('office_')],
            'dashboards': [k for k in PROMPTS.keys() if k.startswith('dashboard_')],
        },
        'failed': failed_prompts
    }

    catalog_path = OUTPUT_DIR / 'catalog.json'
    with open(catalog_path, 'w') as f:
        json.dump(catalog, f, indent=2)
    print(f"\nCatalog saved to: {catalog_path}")

if __name__ == '__main__':
    main()
