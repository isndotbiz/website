#!/usr/bin/env python3
"""
Generate professional hero/feature images for all ISN.BIZ projects using fal.ai gpt-image-1.5
Status: Task #5 - Generate project images
"""

import os
import json
import time
import requests
from pathlib import Path

# Configuration
FAL_API_KEY = "64b786c3-d6b1-4fbb-9d46-9211ceea552f:d472cdf8c68b4fe873557ca33bfb25eb"
FAL_API_URL = "https://queue.fal.run/fal-ai/gpt-image-1.5"
OUTPUT_DIR = Path("assets/projects")
BRAND_COLORS = {
    "blue": "#1E9FF2",
    "cyan": "#5FDFDF",
    "charcoal": "#3F4447"
}

# Create output directory
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Project definitions with prompts
PROJECTS = {
    "gedcom": {
        "name": "GEDCOM Processing Platform",
        "slug": "gedcom",
        "description": "Genealogy data cleaning and processing platform",
        "prompts": [
            "Professional genealogy family tree visualization with clean node-based diagram, flowing connections between generations, modern blue and cyan color scheme, tech interface style, corporate aesthetic, high quality digital render",
            "Advanced data cleaning interface showing before/after genealogy records, structured table view, data validation indicators, professional dashboard design, blue and cyan accents, clean modern UI",
            "Large-scale family network graph with thousands of interconnected nodes, stunning visualization of relationships, algorithmic layout, tech art style, blue cyan gradient background",
            "Data processing pipeline visualization for genealogy records, flowchart style, automated workflow steps, modern enterprise software aesthetic, professional color palette"
        ]
    },
    "comfyui": {
        "name": "ComfyUI Flux Automation",
        "slug": "comfyui",
        "description": "AI image generation pipeline automation",
        "prompts": [
            "Modern AI image generation workflow interface, node-based visual programming system, connected processing blocks, neural network visualization, professional blue and cyan color scheme, tech aesthetic",
            "Automated image processing pipeline showing multiple AI models in sequence, data flow visualization, professional automation dashboard, sleek modern design",
            "ComfyUI-style node graph with complex AI workflow, multiple interconnected processing nodes, clean technical diagram, corporate blue and cyan colors, high-tech aesthetic",
            "AI generation studio interface with preview panels, batch processing queue, professional creative tools layout, modern software design"
        ]
    },
    "spiritatlas": {
        "name": "SpiritAtlas",
        "slug": "spiritatlas",
        "description": "Privacy-first mobile spiritual guidance app",
        "prompts": [
            "Elegant mobile app interface for spiritual guidance, peaceful user experience, modern minimalist design with blue and cyan accents, meditation and mindfulness theme, professional app mockup",
            "Privacy-focused mobile app showing encrypted spiritual journals, secure data visualization, trust indicators, professional security-first design, calming blue palette",
            "Beautiful spiritual atlas interface with interactive map metaphor, journey tracking, milestone visualization, modern app design, professional polish",
            "Mobile meditation and reflection interface, clean typography, thoughtful spacing, premium app aesthetic, blue and cyan color harmony"
        ]
    },
    "videogen": {
        "name": "VideoGen YouTube",
        "slug": "videogen",
        "description": "Automated video production pipeline",
        "prompts": [
            "Professional automated video production dashboard, timeline editor interface, AI-powered workflow visualization, modern video editing software aesthetic, blue and cyan professional theme",
            "YouTube content creation automation pipeline, batch processing interface, professional media production tools, sleek modern design",
            "AI video generation workflow showing script-to-video pipeline, automated production stages, professional broadcast quality visualization, corporate design",
            "Content scheduling and automation dashboard for YouTube, analytics integration, professional creator tools interface, modern software design"
        ]
    },
    "bin": {
        "name": "BIN Intelligence",
        "slug": "bin",
        "description": "Fraud prevention and payment analysis platform",
        "prompts": [
            "Advanced fraud detection dashboard showing real-time payment analysis, threat visualization, security monitoring interface, professional fintech design, blue and cyan corporate colors",
            "Payment BIN intelligence platform with data analytics, transaction pattern recognition, professional financial software interface, sleek modern aesthetic",
            "Cybersecurity operations center dashboard for payment fraud prevention, threat indicators, monitoring displays, high-tech professional design",
            "Real-time fraud detection system showing alert dashboards, risk scoring visualization, professional security software interface, corporate polish"
        ]
    },
    "llm": {
        "name": "LLM Optimization Framework",
        "slug": "llm",
        "description": "AI model evaluation and optimization toolkit",
        "prompts": [
            "Professional AI model benchmarking dashboard, performance metrics visualization, comparison charts, modern ML ops interface, blue and cyan technical aesthetic",
            "LLM evaluation framework showing test results, accuracy metrics, model comparison interface, professional AI development tools design",
            "Machine learning optimization pipeline with performance graphs, automated testing workflow, professional data science interface, sleek design",
            "AI model performance monitoring dashboard, real-time metrics, evaluation results visualization, professional ML platform aesthetic"
        ]
    },
    "opportunity": {
        "name": "Opportunity Research Bot",
        "slug": "opportunity",
        "description": "AI-powered business opportunity discovery system",
        "prompts": [
            "Professional business intelligence dashboard showing opportunity discovery, AI analysis results, market insights visualization, modern enterprise software design, blue cyan palette",
            "Automated research bot interface with data gathering visualization, web scraping pipeline, AI analysis workflow, professional corporate design",
            "Business opportunity discovery platform showing trending markets, analysis results, recommendation engine interface, sleek professional aesthetic",
            "AI-powered market research dashboard with opportunity scoring, insight visualization, professional business intelligence design"
        ]
    },
    "truenas": {
        "name": "TrueNAS Infrastructure",
        "slug": "truenas",
        "description": "Enterprise on-premise AI/ML platform",
        "prompts": [
            "Modern data center server rack visualization, professional infrastructure monitoring, enterprise hardware aesthetic, blue and cyan lighting, high-tech corporate design",
            "TrueNAS storage and compute infrastructure dashboard, system monitoring interface, resource utilization graphs, professional enterprise software design",
            "On-premise AI/ML platform architecture diagram, containerized services visualization, infrastructure overview, professional technical documentation aesthetic",
            "Enterprise infrastructure control panel showing storage, compute, and networking, professional datacenter management interface, corporate design"
        ]
    },
    "cli": {
        "name": "CLI Engineering Standards",
        "slug": "cli",
        "description": "Development standards and best practices framework",
        "prompts": [
            "Professional software development standards documentation interface, clean code visualization, engineering best practices layout, modern technical aesthetic, blue and cyan design",
            "CLI tool interface showing standardized command patterns, professional terminal design, developer tools aesthetic, modern monospace typography",
            "Software engineering framework visualization, modular component diagram, architectural standards layout, professional technical documentation",
            "Development standards dashboard showing code quality metrics, compliance indicators, professional engineering tools interface"
        ]
    }
}

def generate_image(prompt, output_path, image_num, project_name):
    """Generate image using fal.ai gpt-image-1.5 model"""
    print(f"\n[{project_name}] Generating image {image_num}...")
    print(f"Prompt: {prompt[:100]}...")

    headers = {
        "Authorization": f"Key {FAL_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "prompt": prompt,
        "image_size": "1536x1024",  # Landscape format (permitted: 1024x1024, 1536x1024, 1024x1536)
        "num_images": 1,
        "enable_safety_checker": False,
        "image_quality": "low",  # IMPORTANT: Set to low quality as required
        "output_format": "webp"
    }

    try:
        # Submit job
        response = requests.post(FAL_API_URL, headers=headers, json=payload)
        response.raise_for_status()

        result = response.json()

        # Check if we got a request_id (queued) or direct result
        if "request_id" in result:
            request_id = result["request_id"]
            print(f"Job queued: {request_id}")

            # Use status_url from response or construct it
            status_url = result.get("status_url", f"{FAL_API_URL}/requests/{request_id}/status")
            max_attempts = 60
            attempt = 0

            while attempt < max_attempts:
                time.sleep(3)
                status_response = requests.get(status_url, headers=headers)
                status_response.raise_for_status()
                status_data = status_response.json()

                status = status_data.get("status")
                if status == "COMPLETED":
                    # Get the actual result from response_url
                    response_url = status_data.get("response_url", f"{FAL_API_URL}/requests/{request_id}")
                    result_response = requests.get(response_url, headers=headers)
                    result_response.raise_for_status()
                    result = result_response.json()
                    break
                elif status == "FAILED":
                    print(f"Generation failed: {status_data.get('error')}")
                    return False

                attempt += 1
                if attempt % 5 == 0:
                    print(f"Waiting... ({attempt}/{max_attempts})")

            if attempt >= max_attempts:
                print("Timeout waiting for generation")
                return False

        # Download image
        if "images" in result and len(result["images"]) > 0:
            image_url = result["images"][0]["url"]
            print(f"Downloading from: {image_url}")

            img_response = requests.get(image_url)
            img_response.raise_for_status()

            with open(output_path, "wb") as f:
                f.write(img_response.content)

            print(f"[OK] Saved to: {output_path}")
            return True
        else:
            print(f"No image in response: {result}")
            return False

    except Exception as e:
        print(f"Error generating image: {e}")
        return False

def generate_project_images(project_slug, project_data):
    """Generate all images for a project"""
    print(f"\n{'='*60}")
    print(f"PROJECT: {project_data['name']}")
    print(f"{'='*60}")

    results = []

    for idx, prompt in enumerate(project_data["prompts"], 1):
        output_filename = f"{project_slug}_{idx}.webp"
        output_path = OUTPUT_DIR / output_filename

        # Skip if already exists
        if output_path.exists():
            print(f"\n[{project_data['name']}] Image {idx} already exists: {output_filename}")
            results.append({
                "filename": output_filename,
                "prompt": prompt,
                "status": "existing"
            })
            continue

        success = generate_image(prompt, output_path, idx, project_data['name'])

        results.append({
            "filename": output_filename,
            "prompt": prompt,
            "status": "success" if success else "failed"
        })

        # Rate limiting
        time.sleep(3)

    return results

def create_manifest(all_results):
    """Create manifest file with all generated images"""
    manifest = {
        "generated_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "model": "fal-ai/gpt-image-1.5",
        "image_quality": "low",
        "brand_colors": BRAND_COLORS,
        "projects": {}
    }

    for project_slug, results in all_results.items():
        project_data = PROJECTS[project_slug]
        manifest["projects"][project_slug] = {
            "name": project_data["name"],
            "description": project_data["description"],
            "images": results
        }

    manifest_path = OUTPUT_DIR / "manifest.json"
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)

    print(f"\n[OK] Manifest saved to: {manifest_path}")

def print_summary(all_results):
    """Print generation summary"""
    print(f"\n{'='*60}")
    print("GENERATION SUMMARY")
    print(f"{'='*60}")

    total_images = 0
    total_success = 0
    total_existing = 0
    total_failed = 0

    for project_slug, results in all_results.items():
        project_name = PROJECTS[project_slug]["name"]
        success = sum(1 for r in results if r["status"] == "success")
        existing = sum(1 for r in results if r["status"] == "existing")
        failed = sum(1 for r in results if r["status"] == "failed")

        print(f"\n{project_name}:")
        print(f"  [OK] Generated: {success}")
        print(f"  [INFO] Existing: {existing}")
        if failed > 0:
            print(f"  [FAIL] Failed: {failed}")

        total_images += len(results)
        total_success += success
        total_existing += existing
        total_failed += failed

    print(f"\n{'='*60}")
    print(f"TOTALS:")
    print(f"  Total images: {total_images}")
    print(f"  [OK] Generated: {total_success}")
    print(f"  [INFO] Existing: {total_existing}")
    print(f"  [FAIL] Failed: {total_failed}")
    print(f"{'='*60}")

def main():
    print("ISN.BIZ Project Image Generation")
    print("Using fal.ai gpt-image-1.5 (low quality mode)")
    print(f"Output directory: {OUTPUT_DIR.absolute()}")

    all_results = {}

    # Generate images for each project
    for project_slug, project_data in PROJECTS.items():
        results = generate_project_images(project_slug, project_data)
        all_results[project_slug] = results

    # Create manifest
    create_manifest(all_results)

    # Print summary
    print_summary(all_results)

    print("\n[OK] All project images generated!")
    print(f"[OK] Images saved to: {OUTPUT_DIR.absolute()}")
    print(f"[OK] Manifest: {OUTPUT_DIR.absolute()}/manifest.json")

if __name__ == "__main__":
    main()
