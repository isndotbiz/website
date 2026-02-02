#!/usr/bin/env python3
"""
Visual comparison of local vs TrueNAS sites using Playwright
"""
import asyncio
from playwright.async_api import async_playwright
from PIL import Image
import sys

async def screenshot_site(url, output_path):
    """Take screenshot of a site"""
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={'width': 1920, 'height': 1080})

        try:
            await page.goto(url, wait_until='networkidle', timeout=30000)
            await page.screenshot(path=output_path, full_page=True)
            print(f"✅ Screenshot saved: {output_path}")

            # Get page info
            title = await page.title()
            return True, title
        except Exception as e:
            print(f"❌ Error: {e}")
            return False, str(e)
        finally:
            await browser.close()

async def compare_sites():
    """Compare local vs TrueNAS sites"""
    print("="*80)
    print("  VISUAL COMPARISON: Local vs TrueNAS")
    print("="*80)
    print()

    local_url = "http://localhost:9393"
    truenas_url = "https://isn.biz"

    # Screenshot local
    print(f"📸 Screenshotting LOCAL: {local_url}")
    local_success, local_title = await screenshot_site(local_url, "screenshot_local.png")
    print(f"   Title: {local_title}")
    print()

    # Screenshot TrueNAS
    print(f"📸 Screenshotting TRUENAS: {truenas_url}")
    truenas_success, truenas_title = await screenshot_site(truenas_url, "screenshot_truenas.png")
    print(f"   Title: {truenas_title}")
    print()

    if local_success and truenas_success:
        # Compare image dimensions
        local_img = Image.open("screenshot_local.png")
        truenas_img = Image.open("screenshot_truenas.png")

        print("="*80)
        print("  COMPARISON RESULTS")
        print("="*80)
        print()
        print(f"Local size:    {local_img.size}")
        print(f"TrueNAS size:  {truenas_img.size}")
        print()

        if local_title == truenas_title:
            print(f"✅ Titles match: {local_title}")
        else:
            print(f"❌ Titles differ:")
            print(f"   Local:   {local_title}")
            print(f"   TrueNAS: {truenas_title}")

        print()
        print("📁 Screenshots saved:")
        print("   - screenshot_local.png")
        print("   - screenshot_truenas.png")
        print()
        print("👀 Open both images to visually compare!")
        print()

        if local_img.size == truenas_img.size:
            print("✅ Page dimensions match - likely identical!")
        else:
            print("⚠️ Page dimensions differ - check screenshots")
    else:
        print("❌ Screenshot comparison failed")

if __name__ == "__main__":
    asyncio.run(compare_sites())
