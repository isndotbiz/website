#!/usr/bin/env python3
"""
Premium Asset Generator for isn.biz
Generates 40+ award-winning quality assets using fal.ai
"""

import os
import sys
import time
import requests
from pathlib import Path
from PIL import Image
from io import BytesIO
import json

# Configuration
FAL_API_KEY = os.getenv('FAL_API_KEY')
if not FAL_API_KEY:
    print("ERROR: FAL_API_KEY environment variable not set")
    print("Please set it from 1Password: export FAL_API_KEY='your-key'")
    sys.exit(1)

BASE_DIR = Path("/mnt/d/workspace/ISNBIZ_Files/assets/premium")
MODEL = "fal-ai/nano-banana-pro"

# Brand colors
BRAND_COLORS = {
    'blue': '#1E9FF2',
    'cyan': '#5FDFDF'
}

# Asset definitions
ASSETS = {
    'hero': [
        {
            'name': 'abstract_tech_network',
            'prompt': 'Abstract technological network visualization, interconnected nodes and lines, digital mesh, holographic blue #1E9FF2 and cyan #5FDFDF colors, modern corporate style, clean minimalist design, professional business aesthetic, 8k ultra detailed, award-winning design, premium quality',
            'size': 'landscape_16_9'
        },
        {
            'name': 'corporate_modern_gradient',
            'prompt': 'Modern corporate gradient background, smooth flowing waves, geometric patterns, professional blue #1E9FF2 transitioning to cyan #5FDFDF, clean minimalist design, sophisticated business aesthetic, premium quality, 8k resolution, award-winning design',
            'size': 'landscape_16_9'
        },
        {
            'name': 'data_visualization_abstract',
            'prompt': 'Abstract data visualization background, floating charts and graphs, holographic data streams, blue #1E9FF2 and cyan #5FDFDF color scheme, modern analytics aesthetic, clean professional design, premium quality, 8k ultra detailed, futuristic corporate style',
            'size': 'landscape_16_9'
        },
        {
            'name': 'ai_innovation_neural',
            'prompt': 'AI and innovation theme, neural network patterns, artificial intelligence visualization, brain-inspired connectivity, blue #1E9FF2 and cyan #5FDFDF holographic effects, modern tech aesthetic, professional premium design, 8k resolution, award-winning quality',
            'size': 'landscape_16_9'
        },
        {
            'name': 'tech_geometric_abstract',
            'prompt': 'Abstract geometric technology background, 3D polygonal shapes, modern tech patterns, blue #1E9FF2 and cyan #5FDFDF color palette, clean corporate design, minimalist professional aesthetic, premium quality, 8k ultra detailed, sophisticated business style',
            'size': 'landscape_16_9'
        },
        {
            'name': 'digital_transformation',
            'prompt': 'Digital transformation concept, evolving technology patterns, modern business evolution visualization, flowing digital elements, blue #1E9FF2 and cyan #5FDFDF colors, professional corporate aesthetic, clean premium design, 8k resolution, award-winning quality',
            'size': 'landscape_16_9'
        },
        {
            'name': 'cloud_computing_abstract',
            'prompt': 'Cloud computing abstract visualization, floating cloud formations with tech elements, connected infrastructure, blue #1E9FF2 and cyan #5FDFDF gradient, modern professional design, clean minimalist aesthetic, premium quality, 8k ultra detailed, corporate style',
            'size': 'landscape_16_9'
        },
        {
            'name': 'innovation_hub_modern',
            'prompt': 'Innovation hub modern background, creative tech workspace visualization, collaborative digital environment, blue #1E9FF2 and cyan #5FDFDF color scheme, professional premium design, clean sophisticated aesthetic, 8k resolution, award-winning quality',
            'size': 'landscape_16_9'
        }
    ],
    'icons': [
        {
            'name': 'ai_ml_icon',
            'prompt': 'Minimalist AI and machine learning icon, neural network symbol, clean geometric design, blue #1E9FF2 and cyan #5FDFDF colors, professional square format, simple modern style, premium quality icon design, crisp lines, corporate aesthetic',
            'size': 'square'
        },
        {
            'name': 'cloud_services_icon',
            'prompt': 'Minimalist cloud services icon, clean cloud symbol with tech elements, blue #1E9FF2 and cyan #5FDFDF colors, professional square format, simple geometric design, premium quality icon, crisp modern style, corporate aesthetic',
            'size': 'square'
        },
        {
            'name': 'mobile_dev_icon',
            'prompt': 'Minimalist mobile development icon, smartphone symbol with code elements, blue #1E9FF2 and cyan #5FDFDF colors, professional square format, clean geometric design, premium quality icon, modern corporate style, crisp lines',
            'size': 'square'
        },
        {
            'name': 'data_analytics_icon',
            'prompt': 'Minimalist data analytics icon, chart and graph symbol, clean geometric design, blue #1E9FF2 and cyan #5FDFDF colors, professional square format, simple modern style, premium quality icon design, crisp lines, corporate aesthetic',
            'size': 'square'
        },
        {
            'name': 'security_icon',
            'prompt': 'Minimalist security icon, shield and lock symbol, clean geometric design, blue #1E9FF2 and cyan #5FDFDF colors, professional square format, simple modern style, premium quality icon design, crisp lines, corporate aesthetic',
            'size': 'square'
        },
        {
            'name': 'development_icon',
            'prompt': 'Minimalist software development icon, code brackets symbol, clean geometric design, blue #1E9FF2 and cyan #5FDFDF colors, professional square format, simple modern style, premium quality icon design, crisp lines, corporate aesthetic',
            'size': 'square'
        },
        {
            'name': 'devops_icon',
            'prompt': 'Minimalist DevOps icon, infinite loop symbol with gears, clean geometric design, blue #1E9FF2 and cyan #5FDFDF colors, professional square format, simple modern style, premium quality icon design, crisp lines, corporate aesthetic',
            'size': 'square'
        },
        {
            'name': 'testing_qa_icon',
            'prompt': 'Minimalist testing and QA icon, checkmark and bug symbol, clean geometric design, blue #1E9FF2 and cyan #5FDFDF colors, professional square format, simple modern style, premium quality icon design, crisp lines, corporate aesthetic',
            'size': 'square'
        },
        {
            'name': 'consulting_icon',
            'prompt': 'Minimalist consulting icon, lightbulb and people symbol, clean geometric design, blue #1E9FF2 and cyan #5FDFDF colors, professional square format, simple modern style, premium quality icon design, crisp lines, corporate aesthetic',
            'size': 'square'
        },
        {
            'name': 'support_icon',
            'prompt': 'Minimalist support icon, headset and user symbol, clean geometric design, blue #1E9FF2 and cyan #5FDFDF colors, professional square format, simple modern style, premium quality icon design, crisp lines, corporate aesthetic',
            'size': 'square'
        },
        {
            'name': 'integration_icon',
            'prompt': 'Minimalist integration icon, connected puzzle pieces symbol, clean geometric design, blue #1E9FF2 and cyan #5FDFDF colors, professional square format, simple modern style, premium quality icon design, crisp lines, corporate aesthetic',
            'size': 'square'
        },
        {
            'name': 'analytics_reporting_icon',
            'prompt': 'Minimalist analytics reporting icon, dashboard and metrics symbol, clean geometric design, blue #1E9FF2 and cyan #5FDFDF colors, professional square format, simple modern style, premium quality icon design, crisp lines, corporate aesthetic',
            'size': 'square'
        }
    ],
    'portfolio': [
        {
            'name': 'admin_dashboard_modern',
            'prompt': 'Modern admin dashboard interface screenshot, clean UI design, data tables and charts, blue #1E9FF2 and cyan #5FDFDF accent colors, professional business application, realistic web interface, premium quality design, minimalist corporate aesthetic, 8k resolution',
            'size': 'landscape_16_9'
        },
        {
            'name': 'mobile_app_banking',
            'prompt': 'Mobile banking app interface screenshot, modern smartphone UI, transaction list and balance display, blue #1E9FF2 and cyan #5FDFDF colors, clean professional design, realistic mobile mockup, premium quality interface, corporate aesthetic, high resolution',
            'size': 'portrait_9_16'
        },
        {
            'name': 'web_app_crm',
            'prompt': 'CRM web application interface screenshot, customer management dashboard, contact lists and pipelines, blue #1E9FF2 and cyan #5FDFDF accent colors, professional business software, realistic web interface, premium quality design, modern corporate style, 8k resolution',
            'size': 'landscape_16_9'
        },
        {
            'name': 'api_documentation_portal',
            'prompt': 'API documentation portal interface screenshot, developer documentation layout, code examples and endpoints, blue #1E9FF2 and cyan #5FDFDF theme colors, professional tech documentation, realistic web interface, premium quality design, modern developer aesthetic, 8k resolution',
            'size': 'landscape_16_9'
        },
        {
            'name': 'data_visualization_dashboard',
            'prompt': 'Data visualization dashboard screenshot, interactive charts and graphs, real-time analytics display, blue #1E9FF2 and cyan #5FDFDF color scheme, professional business intelligence, realistic web interface, premium quality design, modern corporate aesthetic, 8k resolution',
            'size': 'landscape_16_9'
        },
        {
            'name': 'project_management_tool',
            'prompt': 'Project management tool interface screenshot, kanban board with tasks, team collaboration features, blue #1E9FF2 and cyan #5FDFDF accent colors, professional productivity app, realistic web interface, premium quality design, modern business aesthetic, 8k resolution',
            'size': 'landscape_16_9'
        },
        {
            'name': 'ecommerce_platform',
            'prompt': 'E-commerce platform interface screenshot, product listings and shopping cart, modern online store design, blue #1E9FF2 and cyan #5FDFDF accent colors, professional retail interface, realistic web application, premium quality design, corporate aesthetic, 8k resolution',
            'size': 'landscape_16_9'
        },
        {
            'name': 'saas_analytics_platform',
            'prompt': 'SaaS analytics platform screenshot, metrics dashboard with KPIs, user analytics and reports, blue #1E9FF2 and cyan #5FDFDF color theme, professional business software, realistic web interface, premium quality design, modern corporate style, 8k resolution',
            'size': 'landscape_16_9'
        },
        {
            'name': 'enterprise_resource_planning',
            'prompt': 'Enterprise resource planning interface screenshot, ERP system dashboard, inventory and finance modules, blue #1E9FF2 and cyan #5FDFDF accent colors, professional enterprise software, realistic web interface, premium quality design, corporate aesthetic, 8k resolution',
            'size': 'landscape_16_9'
        },
        {
            'name': 'mobile_app_fitness',
            'prompt': 'Fitness tracking mobile app screenshot, workout plans and progress charts, modern smartphone interface, blue #1E9FF2 and cyan #5FDFDF colors, professional health app design, realistic mobile mockup, premium quality interface, clean aesthetic, high resolution',
            'size': 'portrait_9_16'
        },
        {
            'name': 'learning_management_system',
            'prompt': 'Learning management system screenshot, course catalog and student dashboard, educational platform interface, blue #1E9FF2 and cyan #5FDFDF accent colors, professional e-learning design, realistic web application, premium quality interface, modern aesthetic, 8k resolution',
            'size': 'landscape_16_9'
        },
        {
            'name': 'inventory_management_app',
            'prompt': 'Inventory management application screenshot, stock tracking dashboard, warehouse management interface, blue #1E9FF2 and cyan #5FDFDF color scheme, professional business software, realistic web interface, premium quality design, corporate aesthetic, 8k resolution',
            'size': 'landscape_16_9'
        },
        {
            'name': 'social_media_dashboard',
            'prompt': 'Social media management dashboard screenshot, post scheduling and analytics, multi-platform management interface, blue #1E9FF2 and cyan #5FDFDF accent colors, professional marketing tool, realistic web application, premium quality design, modern aesthetic, 8k resolution',
            'size': 'landscape_16_9'
        },
        {
            'name': 'helpdesk_ticketing_system',
            'prompt': 'Helpdesk ticketing system screenshot, support ticket management, customer service dashboard interface, blue #1E9FF2 and cyan #5FDFDF color theme, professional support software, realistic web interface, premium quality design, corporate aesthetic, 8k resolution',
            'size': 'landscape_16_9'
        },
        {
            'name': 'business_intelligence_portal',
            'prompt': 'Business intelligence portal screenshot, executive dashboard with insights, real-time reporting interface, blue #1E9FF2 and cyan #5FDFDF accent colors, professional BI platform, realistic web application, premium quality design, modern corporate style, 8k resolution',
            'size': 'landscape_16_9'
        }
    ],
    'backgrounds': [
        {
            'name': 'section_divider_gradient',
            'prompt': 'Abstract section divider background, smooth gradient waves, flowing organic shapes, blue #1E9FF2 to cyan #5FDFDF transition, clean minimalist design, professional corporate aesthetic, premium quality, 8k resolution, modern business style',
            'size': 'landscape_16_9'
        },
        {
            'name': 'cta_background_dynamic',
            'prompt': 'Dynamic call-to-action background, energetic geometric patterns, modern tech elements, blue #1E9FF2 and cyan #5FDFDF colors, professional business design, clean premium aesthetic, 8k ultra detailed, award-winning quality, corporate style',
            'size': 'landscape_16_9'
        },
        {
            'name': 'feature_block_abstract',
            'prompt': 'Abstract feature block background, subtle geometric patterns, modern tech texture, light blue #1E9FF2 and cyan #5FDFDF tones, clean professional design, minimalist corporate aesthetic, premium quality, 8k resolution, sophisticated business style',
            'size': 'landscape_16_9'
        },
        {
            'name': 'testimonial_area_soft',
            'prompt': 'Soft testimonial area background, gentle gradient waves, calming abstract shapes, subtle blue #1E9FF2 and cyan #5FDFDF colors, professional trust-building design, clean premium aesthetic, 8k resolution, modern corporate style, award-winning quality',
            'size': 'landscape_16_9'
        },
        {
            'name': 'footer_background_elegant',
            'prompt': 'Elegant footer background, sophisticated dark gradient with subtle blue #1E9FF2 and cyan #5FDFDF accents, modern tech pattern overlay, professional corporate design, clean premium aesthetic, 8k resolution, award-winning quality',
            'size': 'landscape_16_9'
        },
        {
            'name': 'pricing_section_modern',
            'prompt': 'Modern pricing section background, clean geometric grid, subtle tech elements, light blue #1E9FF2 and cyan #5FDFDF gradient, professional business design, minimalist corporate aesthetic, premium quality, 8k resolution, sophisticated style',
            'size': 'landscape_16_9'
        },
        {
            'name': 'contact_form_background',
            'prompt': 'Contact form background, welcoming gradient design, smooth flowing patterns, blue #1E9FF2 and cyan #5FDFDF colors, professional approachable aesthetic, clean modern design, premium quality, 8k resolution, corporate business style',
            'size': 'landscape_16_9'
        },
        {
            'name': 'services_grid_backdrop',
            'prompt': 'Services grid backdrop, subtle hexagonal pattern, modern tech texture, very light blue #1E9FF2 and cyan #5FDFDF tones, clean professional design, minimalist corporate aesthetic, premium quality, 8k resolution, award-winning business style',
            'size': 'landscape_16_9'
        }
    ],
    'infographics': [
        {
            'name': 'process_workflow_diagram',
            'prompt': 'Modern process workflow infographic diagram, step-by-step visualization with icons, connected flow elements, blue #1E9FF2 and cyan #5FDFDF color scheme, clean professional design, minimalist business aesthetic, premium quality illustration, 8k resolution, award-winning design',
            'size': 'landscape_16_9'
        },
        {
            'name': 'tech_stack_visualization',
            'prompt': 'Technology stack visualization infographic, layered architecture diagram, modern tech icons and labels, blue #1E9FF2 and cyan #5FDFDF colors, professional developer aesthetic, clean design, premium quality illustration, 8k resolution, corporate style',
            'size': 'landscape_16_9'
        },
        {
            'name': 'growth_metrics_chart',
            'prompt': 'Business growth metrics infographic, ascending charts and statistics, performance indicators visualization, blue #1E9FF2 and cyan #5FDFDF color scheme, professional business design, clean modern aesthetic, premium quality illustration, 8k resolution, award-winning style',
            'size': 'landscape_16_9'
        },
        {
            'name': 'team_collaboration_illustration',
            'prompt': 'Team collaboration infographic illustration, people working together with tech elements, modern workplace visualization, blue #1E9FF2 and cyan #5FDFDF colors, professional business design, clean aesthetic, premium quality illustration, 8k resolution, corporate style',
            'size': 'landscape_16_9'
        },
        {
            'name': 'service_benefits_diagram',
            'prompt': 'Service benefits diagram infographic, circular arrangement of key features, icon-based visualization, blue #1E9FF2 and cyan #5FDFDF color palette, professional business design, clean modern aesthetic, premium quality illustration, 8k resolution, award-winning style',
            'size': 'landscape_16_9'
        }
    ]
}


def call_fal_api(prompt, image_size, seed=None):
    """Call fal.ai API to generate image"""
    url = f"https://fal.run/{MODEL}"

    headers = {
        "Authorization": f"Key {FAL_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "prompt": prompt,
        "image_size": image_size,
        "num_inference_steps": 4,
        "num_images": 1,
        "enable_safety_checker": False
    }

    if seed:
        payload["seed"] = seed

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()

        if 'images' in result and len(result['images']) > 0:
            return result['images'][0]['url']
        else:
            print(f"Unexpected response format: {result}")
            return None

    except Exception as e:
        print(f"API Error: {str(e)}")
        if hasattr(e, 'response') and e.response:
            print(f"Response: {e.response.text}")
        return None


def download_and_convert_to_webp(image_url, output_path, quality=90):
    """Download image and convert to WebP format"""
    try:
        response = requests.get(image_url)
        response.raise_for_status()

        img = Image.open(BytesIO(response.content))

        # Convert to RGB if necessary
        if img.mode in ('RGBA', 'LA', 'P'):
            background = Image.new('RGB', img.size, (255, 255, 255))
            if img.mode == 'P':
                img = img.convert('RGBA')
            background.paste(img, mask=img.split()[-1] if img.mode in ('RGBA', 'LA') else None)
            img = background

        # Save as WebP
        img.save(output_path, 'WEBP', quality=quality, method=6)
        print(f"✓ Saved: {output_path.name}")
        return True

    except Exception as e:
        print(f"✗ Error saving {output_path.name}: {str(e)}")
        return False


def generate_assets():
    """Generate all assets"""
    print("=" * 80)
    print("PREMIUM ASSET GENERATOR FOR ISN.BIZ")
    print("=" * 80)
    print()

    total_assets = sum(len(assets) for assets in ASSETS.values())
    current = 0
    successful = 0
    failed = 0

    for category, assets in ASSETS.items():
        print(f"\n{'=' * 80}")
        print(f"Generating {category.upper()} assets ({len(assets)} items)")
        print(f"{'=' * 80}\n")

        category_dir = BASE_DIR / category
        category_dir.mkdir(parents=True, exist_ok=True)

        for asset in assets:
            current += 1
            name = asset['name']
            prompt = asset['prompt']
            size = asset['size']

            print(f"[{current}/{total_assets}] Generating: {name}")
            print(f"  Size: {size}")
            print(f"  Prompt: {prompt[:100]}...")

            # Generate image
            image_url = call_fal_api(prompt, size)

            if image_url:
                output_path = category_dir / f"{name}.webp"
                if download_and_convert_to_webp(image_url, output_path):
                    successful += 1
                else:
                    failed += 1

                # Rate limiting - be respectful to API
                time.sleep(2)
            else:
                failed += 1
                print(f"  ✗ Failed to generate image")

            print()

    # Summary
    print("\n" + "=" * 80)
    print("GENERATION COMPLETE")
    print("=" * 80)
    print(f"Total assets: {total_assets}")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Success rate: {(successful/total_assets*100):.1f}%")
    print()
    print(f"Assets saved to: {BASE_DIR}")
    print("=" * 80)

    # Create manifest
    manifest = {
        'generated_at': time.strftime('%Y-%m-%d %H:%M:%S'),
        'total_assets': total_assets,
        'successful': successful,
        'failed': failed,
        'categories': {cat: len(assets) for cat, assets in ASSETS.items()},
        'brand_colors': BRAND_COLORS,
        'model': MODEL
    }

    manifest_path = BASE_DIR / 'manifest.json'
    with open(manifest_path, 'w') as f:
        json.dump(manifest, f, indent=2)

    print(f"\nManifest saved to: {manifest_path}")


if __name__ == '__main__':
    generate_assets()
