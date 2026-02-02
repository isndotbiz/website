#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ISN.BIZ Website Comprehensive Test Suite
Tests all pages, images, links, and functionality
"""

import asyncio
import json
import sys
from datetime import datetime
from pathlib import Path
from playwright.async_api import async_playwright, Page
import re

# Fix encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

# Configuration
BASE_URL = "https://isn.biz"
SCREENSHOT_DIR = Path("/tmp/playwright-screenshots")
SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)

# All pages to test
PAGES = {
    "Main Pages": [
        ("Home", ""),
        ("About", "about.html"),
        ("Portfolio", "portfolio.html"),
        ("Investors", "investors.html"),
        ("Slider Gallery", "slider-gallery.html"),
        ("Portfolio Grid", "portfolio-grid.html"),
    ],
    "Founder Pages": [
        ("Alicia", "alicia.html"),
        ("Bri", "bri.html"),
        ("Jonathan", "jonathan.html"),
        ("Lilly", "lilly.html"),
    ],
    "Project Pages": [
        ("CLI Standards", "project-cli-standards.html"),
        ("ComfyUI Automation", "project-comfyui-automation.html"),
        ("GEDCOM Platform", "project-gedcom-platform.html"),
        ("LLM Optimization", "project-llm-optimization.html"),
        ("Opportunity Bot", "project-opportunity-bot.html"),
        ("SpiritAtlas", "project-spiritatlas.html"),
        ("TrueNAS Infrastructure", "project-truenas-infrastructure.html"),
        ("VideoGen YouTube", "project-videogen-youtube.html"),
    ],
}

class WebsiteTest:
    def __init__(self):
        self.results = {
            "test_date": datetime.now().isoformat(),
            "base_url": BASE_URL,
            "pages_tested": 0,
            "pages_passed": 0,
            "pages_failed": 0,
            "total_images": 0,
            "images_loaded": 0,
            "images_failed": 0,
            "broken_links": [],
            "page_results": [],
            "errors": [],
        }

    async def check_image(self, page: Page, img_element) -> dict:
        """Check if an image loaded successfully"""
        try:
            src = await img_element.get_attribute("src")
            alt = await img_element.get_attribute("alt") or "No alt text"

            # Get natural dimensions - if they exist, image loaded
            natural_width = await img_element.evaluate("img => img.naturalWidth")
            natural_height = await img_element.evaluate("img => img.naturalHeight")

            # Check if image actually loaded
            complete = await img_element.evaluate("img => img.complete")

            loaded = complete and natural_width > 0 and natural_height > 0

            return {
                "src": src,
                "alt": alt,
                "loaded": loaded,
                "width": natural_width,
                "height": natural_height,
                "complete": complete,
            }
        except Exception as e:
            return {
                "src": "unknown",
                "alt": "unknown",
                "loaded": False,
                "error": str(e),
            }

    async def check_response_status(self, page: Page, url: str) -> int:
        """Check HTTP status code for a URL"""
        try:
            response = await page.goto(url, wait_until="networkidle", timeout=30000)
            return response.status if response else 0
        except Exception as e:
            return 0

    async def test_page(self, page: Page, category: str, name: str, path: str) -> dict:
        """Test a single page"""
        url = f"{BASE_URL}/{path}" if path else BASE_URL
        print(f"\n{'='*80}")
        print(f"Testing: {name} ({url})")
        print(f"{'='*80}")

        result = {
            "category": category,
            "name": name,
            "url": url,
            "path": path,
            "status_code": 0,
            "page_loaded": False,
            "images": [],
            "image_stats": {"total": 0, "loaded": 0, "failed": 0},
            "links_checked": 0,
            "broken_links": [],
            "errors": [],
            "screenshot": None,
        }

        try:
            # Navigate to page
            print(f"Loading page...")
            response = await page.goto(url, wait_until="networkidle", timeout=30000)
            result["status_code"] = response.status if response else 0
            result["page_loaded"] = result["status_code"] == 200

            if not result["page_loaded"]:
                result["errors"].append(f"Page returned status {result['status_code']}")
                print(f"❌ Page failed to load: HTTP {result['status_code']}")
                return result

            print(f"✅ Page loaded: HTTP {result['status_code']}")

            # Wait for page to be fully rendered
            await page.wait_for_timeout(2000)

            # Check all images
            print(f"\nChecking images...")
            images = await page.query_selector_all("img")
            result["image_stats"]["total"] = len(images)

            for idx, img in enumerate(images):
                img_result = await self.check_image(page, img)
                result["images"].append(img_result)

                if img_result["loaded"]:
                    result["image_stats"]["loaded"] += 1
                    print(f"  ✅ Image {idx+1}/{len(images)}: {img_result['src'][:60]}...")
                else:
                    result["image_stats"]["failed"] += 1
                    error_msg = img_result.get("error", "Failed to load")
                    result["errors"].append(f"Image failed: {img_result['src']} - {error_msg}")
                    print(f"  ❌ Image {idx+1}/{len(images)}: {img_result['src'][:60]}... - {error_msg}")

            # Take screenshot
            screenshot_name = f"{category.lower().replace(' ', '_')}_{path.replace('.html', '') or 'index'}.png"
            screenshot_path = SCREENSHOT_DIR / screenshot_name
            await page.screenshot(path=str(screenshot_path), full_page=True)
            result["screenshot"] = str(screenshot_path)
            print(f"\n📸 Screenshot saved: {screenshot_path}")

            # Summary
            print(f"\n📊 Page Summary:")
            print(f"   Images: {result['image_stats']['loaded']}/{result['image_stats']['total']} loaded")
            if result["image_stats"]["failed"] > 0:
                print(f"   ⚠️  {result['image_stats']['failed']} images failed to load")

        except Exception as e:
            result["errors"].append(f"Page test error: {str(e)}")
            print(f"❌ Error testing page: {e}")

        return result

    async def run_all_tests(self):
        """Run all tests"""
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(
                viewport={"width": 1920, "height": 1080},
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            )
            page = await context.new_page()

            print(f"\n{'#'*80}")
            print(f"# ISN.BIZ Website Comprehensive Test Suite")
            print(f"# Base URL: {BASE_URL}")
            print(f"# Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"{'#'*80}\n")

            # Test all pages
            for category, pages in PAGES.items():
                print(f"\n{'*'*80}")
                print(f"* Category: {category}")
                print(f"{'*'*80}")

                for name, path in pages:
                    result = await self.test_page(page, category, name, path)
                    self.results["page_results"].append(result)
                    self.results["pages_tested"] += 1

                    # Update totals
                    self.results["total_images"] += result["image_stats"]["total"]
                    self.results["images_loaded"] += result["image_stats"]["loaded"]
                    self.results["images_failed"] += result["image_stats"]["failed"]

                    if result["page_loaded"] and result["image_stats"]["failed"] == 0:
                        self.results["pages_passed"] += 1
                    else:
                        self.results["pages_failed"] += 1

                    self.results["errors"].extend(result["errors"])
                    self.results["broken_links"].extend(result["broken_links"])

            await browser.close()

    def generate_report(self) -> str:
        """Generate comprehensive test report"""
        report = []
        report.append("=" * 80)
        report.append("ISN.BIZ WEBSITE TEST REPORT")
        report.append("=" * 80)
        report.append(f"Test Date: {self.results['test_date']}")
        report.append(f"Base URL: {self.results['base_url']}")
        report.append("")

        # Overall Summary
        report.append("OVERALL SUMMARY")
        report.append("-" * 80)
        report.append(f"Pages Tested:    {self.results['pages_tested']}")
        report.append(f"Pages Passed:    {self.results['pages_passed']} ✅")
        report.append(f"Pages Failed:    {self.results['pages_failed']} ❌")
        report.append(f"Success Rate:    {(self.results['pages_passed']/self.results['pages_tested']*100):.1f}%")
        report.append("")
        report.append(f"Total Images:    {self.results['total_images']}")
        report.append(f"Images Loaded:   {self.results['images_loaded']} ✅")
        report.append(f"Images Failed:   {self.results['images_failed']} ❌")
        if self.results['total_images'] > 0:
            report.append(f"Image Success:   {(self.results['images_loaded']/self.results['total_images']*100):.1f}%")
        report.append("")

        # Detailed Results by Category
        for category in ["Main Pages", "Founder Pages", "Project Pages"]:
            category_results = [r for r in self.results["page_results"] if r["category"] == category]
            if not category_results:
                continue

            report.append("")
            report.append(f"{category.upper()}")
            report.append("-" * 80)

            for result in category_results:
                status = "✅ PASS" if result["page_loaded"] and result["image_stats"]["failed"] == 0 else "❌ FAIL"
                report.append(f"\n{status} - {result['name']}")
                report.append(f"  URL: {result['url']}")
                report.append(f"  Status Code: {result['status_code']}")
                report.append(f"  Images: {result['image_stats']['loaded']}/{result['image_stats']['total']} loaded")

                if result['screenshot']:
                    report.append(f"  Screenshot: {result['screenshot']}")

                if result["errors"]:
                    report.append(f"  Errors:")
                    for error in result["errors"][:5]:  # Limit to first 5 errors
                        report.append(f"    - {error}")
                    if len(result["errors"]) > 5:
                        report.append(f"    ... and {len(result['errors']) - 5} more errors")

        # Failed Images Details
        if self.results["images_failed"] > 0:
            report.append("")
            report.append("FAILED IMAGES DETAILS")
            report.append("-" * 80)

            failed_count = 0
            for page_result in self.results["page_results"]:
                failed_images = [img for img in page_result["images"] if not img["loaded"]]
                if failed_images:
                    report.append(f"\n{page_result['name']} ({page_result['url']}):")
                    for img in failed_images[:10]:  # Limit to 10 per page
                        failed_count += 1
                        report.append(f"  - {img['src']}")
                        if 'error' in img:
                            report.append(f"    Error: {img['error']}")

        # Screenshots Location
        report.append("")
        report.append("SCREENSHOTS")
        report.append("-" * 80)
        report.append(f"Screenshots saved to: {SCREENSHOT_DIR}")
        report.append(f"Total screenshots: {len([r for r in self.results['page_results'] if r['screenshot']])}")

        # Recommendations
        report.append("")
        report.append("RECOMMENDATIONS")
        report.append("-" * 80)

        if self.results["pages_failed"] == 0:
            report.append("✅ All pages loaded successfully!")
        else:
            report.append(f"⚠️  {self.results['pages_failed']} pages had issues - review errors above")

        if self.results["images_failed"] == 0:
            report.append("✅ All images loaded successfully from S3!")
        else:
            report.append(f"❌ {self.results['images_failed']} images failed to load - check S3 URLs and permissions")

        report.append("")
        report.append("=" * 80)

        return "\n".join(report)

    def save_json_report(self, filepath: str):
        """Save detailed JSON report"""
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, indent=2, ensure_ascii=False)

async def main():
    tester = WebsiteTest()
    await tester.run_all_tests()

    # Generate and print report
    report = tester.generate_report()
    print("\n" * 2)
    print(report)

    # Save reports
    report_dir = Path("D:/workspace/ISNBIZ_Files/test_reports")
    report_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Save text report
    text_report_path = report_dir / f"test_report_{timestamp}.txt"
    with open(text_report_path, 'w', encoding='utf-8') as f:
        f.write(report)
    print(f"\n📄 Text report saved: {text_report_path}")

    # Save JSON report
    json_report_path = report_dir / f"test_report_{timestamp}.json"
    tester.save_json_report(str(json_report_path))
    print(f"📄 JSON report saved: {json_report_path}")

    print(f"\n✅ Testing complete!")

    # Exit with error code if tests failed
    if tester.results["pages_failed"] > 0 or tester.results["images_failed"] > 0:
        exit(1)
    else:
        exit(0)

if __name__ == "__main__":
    asyncio.run(main())
