# ComfyUI Flux WAN Automation

Automation suite for running ComfyUI with Flux and WAN models on GPU hosts and generating repeatable batches of images and workflows.

## Funder Snapshot
- Problem: Generative image pipelines are hard to scale beyond manual UI use.
- Solution: Programmatic ComfyUI workflow generation, execution, and batch orchestration.
- Differentiation: API-driven workflow control, LoRA management, and ready-made generator scripts.

## What Is Built
- ComfyUI API manager for status checks and prompt queueing.
- Flux workflow builder with LoRA support and configurable parameters.
- Config-driven model management for Flux, VAE, and CLIP assets.
- Batch generators for social and campaign content.
- Shell tools for starting services and managing LoRA downloads.
- Workflow JSON artifacts for reproducible runs.

## Architecture
```
Workflow JSON -> ComfyUI API -> GPU execution -> Output images
```

## Tech Stack
- Python 3.10+
- requests, aiohttp, Pillow, PyYAML
- Integrations: fal-client, replicate, gradio-client
- YAML configuration

## Repository Structure
```
src/                     Core ComfyUI and Flux handlers
configs/                 Model and server configuration
scripts/                 Control scripts and LoRA manager
workflows/               Saved workflow JSONs
```

## Quick Start
```
python -m venv venv
source venv/bin/activate
pip install -e .

./setup.sh
./scripts/comfy-ctl.sh start
python generate_images.py
```

## Configuration
- configs/config.yaml defines server host/port and model paths.
- Set CIVITAI_TOKEN for LoRA downloads if using the LoRA manager.

## License
See LICENSE if present in the repo.
