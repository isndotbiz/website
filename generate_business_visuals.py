#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate Professional Business Visuals for ISN.BIZ
Using fal.ai/gpt-image-1.5 for high-quality, brand-aligned images
"""

import fal_client
import json
import os
import sys
from pathlib import Path
from datetime import datetime

# Fix Windows console encoding
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

# Load .env file
from dotenv import load_dotenv
load_dotenv()

# Set FAL_KEY from environment
if 'FAL_API_KEY' in os.environ:
    os.environ['FAL_KEY'] = os.environ['FAL_API_KEY']

# ISN.BIZ Brand Colors
BRAND_COLORS = {
    'blue': '#1E9FF2',
    'cyan': '#5FDFDF',
    'charcoal': '#3F4447'
}

# Output directory
OUTPUT_DIR = Path(__file__).parent / "assets" / "business"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Professional business image prompts
IMAGE_PROMPTS = {
    # Category 1: Modern Office Scenes
    "office_collaboration_modern": {
        "prompt": "Ultra-modern tech office, diverse team collaborating around large touchscreen display, "
                 "sleek glass walls, natural lighting, minimalist design, vibrant blue #1E9FF2 accent walls, "
                 "cyan #5FDFDF LED strips, professional atmosphere, 8k quality, architectural photography",
        "category": "office"
    },
    "office_innovation_lab": {
        "prompt": "High-tech innovation lab, engineers working with holographic displays, "
                 "blue and cyan color scheme, modern workspace with standing desks, "
                 "bright open space, technology-focused, professional business setting, cinematic lighting",
        "category": "office"
    },
    "office_boardroom_premium": {
        "prompt": "Premium executive boardroom, floor-to-ceiling windows with city skyline, "
                 "ultra-modern conference table with blue accent lighting, professional business meeting, "
                 "sophisticated interior design, 8k quality, corporate elegance",
        "category": "office"
    },
    "office_open_workspace": {
        "prompt": "Contemporary open-plan office, collaborative workspace with blue and cyan color accents, "
                 "modern furniture, technology everywhere, diverse professionals at work, "
                 "natural light flooding through windows, professional photography",
        "category": "office"
    },

    # Category 2: Tech Dashboards & Data Visualization
    "dashboard_analytics_premium": {
        "prompt": "Advanced analytics dashboard on 4K display, beautiful data visualizations with blue and cyan graphs, "
                 "real-time metrics, clean modern UI design, professional business intelligence platform, "
                 "glowing screens in dark modern office, ultra-detailed, 8k quality",
        "category": "dashboard"
    },
    "dashboard_ai_monitoring": {
        "prompt": "AI monitoring dashboard showing neural network visualizations, blue and cyan data streams, "
                 "real-time performance metrics, futuristic interface design, "
                 "professional tech aesthetic, glowing holographic elements, 8k quality",
        "category": "dashboard"
    },
    "dashboard_cloud_control": {
        "prompt": "Cloud infrastructure control panel, network topology visualization in blue and cyan, "
                 "server status indicators, modern UI/UX design, professional tech interface, "
                 "sleek dark theme with vibrant accents, ultra-high resolution",
        "category": "dashboard"
    },
    "dashboard_enterprise_metrics": {
        "prompt": "Enterprise business metrics dashboard, KPI visualizations with professional blue color scheme, "
                 "clean charts and graphs, modern corporate interface, financial data displays, "
                 "sophisticated design, 8k quality screen capture",
        "category": "dashboard"
    },

    # Category 3: Business Growth & Success
    "growth_chart_upward": {
        "prompt": "Dramatic upward business growth chart with glowing blue and cyan lines, "
                 "3D visualization, financial success metrics, professional corporate aesthetic, "
                 "dark background with vibrant data, futuristic business graphics, 8k quality",
        "category": "growth"
    },
    "growth_global_expansion": {
        "prompt": "Global business expansion visualization, 3D world map with blue network connections, "
                 "illuminated nodes showing worldwide presence, professional corporate graphics, "
                 "cyan data streams, modern tech aesthetic, cinematic quality",
        "category": "growth"
    },
    "growth_success_trajectory": {
        "prompt": "Abstract representation of business success, ascending arrow made of blue and cyan light trails, "
                 "professional corporate atmosphere, modern digital art, inspirational business visual, "
                 "clean composition, 8k quality",
        "category": "growth"
    },

    # Category 4: Team Collaboration
    "team_strategy_session": {
        "prompt": "Professional strategy session, diverse team around interactive digital whiteboard, "
                 "blue and cyan visual elements, modern collaborative workspace, "
                 "engaged professionals brainstorming, natural lighting, corporate photography, 8k quality",
        "category": "team"
    },
    "team_innovation_workshop": {
        "prompt": "Innovation workshop with creative professionals, modern office setting with blue accents, "
                 "collaborative work environment, technology integration, diverse team members, "
                 "professional business atmosphere, high-quality photography",
        "category": "team"
    },
    "team_digital_collaboration": {
        "prompt": "Remote team collaboration via large video wall, modern tech office with blue and cyan lighting, "
                 "professional digital workspace, multiple screens showing team members, "
                 "contemporary business environment, 8k quality",
        "category": "team"
    },

    # Category 5: Technology Infrastructure
    "infrastructure_server_room": {
        "prompt": "Ultra-modern server room with blue LED indicators, rows of enterprise servers, "
                 "cyan status lights, professional data center, clean organized cables, "
                 "high-tech atmosphere, industrial photography, 8k quality",
        "category": "infrastructure"
    },
    "infrastructure_cloud_network": {
        "prompt": "Cloud network visualization, abstract representation of distributed servers, "
                 "blue and cyan connection lines, nodes glowing with data transfer, "
                 "professional tech graphics, futuristic design, 3D rendered, ultra-high quality",
        "category": "infrastructure"
    },
    "infrastructure_datacenter": {
        "prompt": "Enterprise data center with modern architecture, blue atmospheric lighting, "
                 "rows of server racks with cyan indicators, professional IT infrastructure, "
                 "clean technical environment, architectural photography, 8k quality",
        "category": "infrastructure"
    },

    # Category 6: Software Interfaces
    "interface_ai_platform": {
        "prompt": "Modern AI platform interface, clean UI design with blue and cyan accents, "
                 "neural network visualization, professional software dashboard, "
                 "sleek dark theme, intuitive layout, 8k screen capture quality",
        "category": "interface"
    },
    "interface_enterprise_app": {
        "prompt": "Enterprise application interface, professional business software UI, "
                 "blue color scheme with cyan highlights, modern dashboard design, "
                 "clean data tables and charts, sophisticated UX, ultra-high resolution",
        "category": "interface"
    },
    "interface_cloud_console": {
        "prompt": "Cloud management console, modern admin interface with blue theme, "
                 "resource monitoring panels, professional tech platform, cyan status indicators, "
                 "clean organized layout, 8k quality screenshot",
        "category": "interface"
    },

    # Category 7: Innovation & Future Tech
    "innovation_ai_neural": {
        "prompt": "Abstract AI neural network visualization, blue and cyan glowing nodes connected by light trails, "
                 "3D representation of machine learning, professional tech graphics, "
                 "dark background with vibrant digital elements, futuristic aesthetic, 8k quality",
        "category": "innovation"
    },
    "innovation_quantum_computing": {
        "prompt": "Quantum computing visualization, abstract quantum bits in blue and cyan, "
                 "futuristic technology representation, professional scientific graphics, "
                 "glowing particles and energy waves, cinematic tech aesthetic, ultra-high quality",
        "category": "innovation"
    },
    "innovation_automation_flow": {
        "prompt": "Business process automation flowchart, blue and cyan connection lines, "
                 "modern workflow visualization, professional infographic style, "
                 "clean design with glowing elements, corporate tech graphics, 8k quality",
        "category": "innovation"
    },
    "innovation_digital_transformation": {
        "prompt": "Digital transformation concept, transitioning from analog to digital, "
                 "blue and cyan digital particles forming business icons, professional corporate visual, "
                 "modern tech aesthetic, inspirational business graphics, cinematic quality",
        "category": "innovation"
    }
}

def generate_image(name, config):
    """Generate a single image using fal.ai/gpt-image-1.5"""
    print(f"\n{'='*60}")
    print(f"Generating: {name}")
    print(f"Category: {config['category']}")
    print(f"Prompt: {config['prompt'][:100]}...")
    print(f"{'='*60}")

    try:
        result = fal_client.subscribe(
            "fal-ai/gpt-image-1.5",
            arguments={
                "prompt": config['prompt'],
                "image_size": "1536x1024",  # Landscape format for professional business
                "num_images": 1,
                "enable_safety_checker": True,
                "output_format": "png"
            },
            with_logs=True,
            on_queue_update=lambda update: print(f"  Status: processing...")
        )

        # Handle different result types
        if hasattr(result, 'images'):
            images = result.images
        elif isinstance(result, dict) and 'images' in result:
            images = result['images']
        else:
            print(f"[ERROR] Unexpected result type: {type(result)}")
            print(f"  Result: {result}")
            return None

        if images and len(images) > 0:
            # Handle image object
            if hasattr(images[0], 'url'):
                image_url = images[0].url
            elif isinstance(images[0], dict):
                image_url = images[0]['url']
            else:
                print(f"[ERROR] Unexpected image format: {type(images[0])}")
                return None

            print(f"[SUCCESS] Generated successfully!")
            print(f"   URL: {image_url}")
            return image_url
        else:
            print(f"[ERROR] No image returned in result")
            return None

    except Exception as e:
        print(f"[ERROR] Error generating {name}: {e}")
        import traceback
        traceback.print_exc()
        return None

def download_image(url, filepath):
    """Download image from URL"""
    import urllib.request
    try:
        print(f"  Downloading to: {filepath}")
        urllib.request.urlretrieve(url, filepath)
        print(f"  [SUCCESS] Downloaded successfully")
        return True
    except Exception as e:
        print(f"  [ERROR] Download failed: {e}")
        return False

def main():
    """Generate all business visuals"""
    print("\n" + "="*60)
    print("ISN.BIZ Business Visuals Generation")
    print("Using fal.ai/gpt-image-1.5")
    print("="*60)
    print(f"\nBrand Colors:")
    print(f"  Primary Blue: {BRAND_COLORS['blue']}")
    print(f"  Accent Cyan: {BRAND_COLORS['cyan']}")
    print(f"  Dark Charcoal: {BRAND_COLORS['charcoal']}")
    print(f"\nTotal Images to Generate: {len(IMAGE_PROMPTS)}")
    print(f"Output Directory: {OUTPUT_DIR}")
    print("\n" + "="*60)

    results = {
        "generated_at": datetime.now().isoformat(),
        "brand_colors": BRAND_COLORS,
        "total_images": len(IMAGE_PROMPTS),
        "images": {}
    }

    success_count = 0
    failed_count = 0

    for i, (name, config) in enumerate(IMAGE_PROMPTS.items(), 1):
        print(f"\n[{i}/{len(IMAGE_PROMPTS)}] Processing: {name}")

        # Generate image
        image_url = generate_image(name, config)

        if image_url:
            # Download image
            filename = f"{name}.png"
            filepath = OUTPUT_DIR / filename

            if download_image(image_url, filepath):
                results['images'][name] = {
                    'filename': filename,
                    'filepath': str(filepath),
                    'url': image_url,
                    'category': config['category'],
                    'prompt': config['prompt']
                }
                success_count += 1
            else:
                failed_count += 1
        else:
            failed_count += 1

    # Save results to JSON
    results['success_count'] = success_count
    results['failed_count'] = failed_count

    json_path = OUTPUT_DIR / "s3_urls_business.json"
    with open(json_path, 'w') as f:
        json.dump(results, f, indent=2)

    print("\n" + "="*60)
    print("GENERATION COMPLETE")
    print("="*60)
    print(f"[SUCCESS] Successful: {success_count}")
    print(f"[FAILED] Failed: {failed_count}")
    print(f"[TOTAL] Total: {len(IMAGE_PROMPTS)}")
    print(f"\n[OUTPUT] Images saved to: {OUTPUT_DIR}")
    print(f"[CATALOG] Catalog saved to: {json_path}")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
