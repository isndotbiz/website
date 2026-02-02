#!/usr/bin/env python3
"""
Compare local and TrueNAS ISN.BIZ websites using Playwright.
Takes screenshots and identifies visual differences.
"""

import asyncio
import json
from datetime import datetime
from playwright.async_api import async_playwright
from pathlib import Path

# Site URLs
LOCAL_URL = "http://localhost:9393"
TRUENAS_URL = "https://isn.biz"

# Screenshot output directory
OUTPUT_DIR = Path("screenshots_comparison")
OUTPUT_DIR.mkdir(exist_ok=True)

async def take_screenshot(page, url, name, viewport_width=1920):
    """Take screenshot of a URL at different viewports."""
    await page.goto(url, wait_until="networkidle", timeout=30000)

    # Wait for page to be fully rendered
    await page.wait_for_timeout(2000)

    # Take full page screenshot
    screenshot_path = OUTPUT_DIR / f"{name}_full.png"
    await page.screenshot(path=str(screenshot_path), full_page=True)
    print(f"[OK] Screenshot saved: {screenshot_path}")

    # Take viewport screenshot (above the fold)
    viewport_path = OUTPUT_DIR / f"{name}_viewport.png"
    await page.screenshot(path=str(viewport_path), full_page=False)
    print(f"[OK] Screenshot saved: {viewport_path}")

    return screenshot_path

async def analyze_page(page, url, name):
    """Analyze page structure, styles, and content."""
    await page.goto(url, wait_until="networkidle", timeout=30000)
    await page.wait_for_timeout(2000)

    # Extract computed styles for key elements
    analysis = await page.evaluate("""
        () => {
            const data = {
                title: document.title,
                meta_description: document.querySelector('meta[name="description"]')?.content || 'N/A',
                css_files: [],
                js_files: [],
                images: [],
                fonts: [],
                colors: new Set(),
                body_styles: {},
                hero_styles: {},
                nav_styles: {},
                sections: []
            };

            // Get stylesheets
            document.querySelectorAll('link[rel="stylesheet"]').forEach(link => {
                data.css_files.push(link.href);
            });

            // Get scripts
            document.querySelectorAll('script[src]').forEach(script => {
                data.js_files.push(script.src);
            });

            // Get images
            document.querySelectorAll('img').forEach(img => {
                data.images.push({
                    src: img.src,
                    alt: img.alt,
                    width: img.naturalWidth,
                    height: img.naturalHeight
                });
            });

            // Get fonts
            const fontFamilies = new Set();
            document.querySelectorAll('*').forEach(el => {
                const font = getComputedStyle(el).fontFamily;
                if (font) fontFamilies.add(font);
            });
            data.fonts = Array.from(fontFamilies);

            // Get body styles
            const body = document.body;
            if (body) {
                const bodyStyles = getComputedStyle(body);
                data.body_styles = {
                    backgroundColor: bodyStyles.backgroundColor,
                    color: bodyStyles.color,
                    fontFamily: bodyStyles.fontFamily,
                    fontSize: bodyStyles.fontSize,
                    lineHeight: bodyStyles.lineHeight
                };
            }

            // Get hero section styles
            const hero = document.querySelector('.hero, #hero, [class*="hero"]');
            if (hero) {
                const heroStyles = getComputedStyle(hero);
                data.hero_styles = {
                    backgroundColor: heroStyles.backgroundColor,
                    backgroundImage: heroStyles.backgroundImage,
                    color: heroStyles.color,
                    height: heroStyles.height,
                    display: heroStyles.display,
                    alignItems: heroStyles.alignItems,
                    justifyContent: heroStyles.justifyContent
                };
            }

            // Get nav styles
            const nav = document.querySelector('nav, header');
            if (nav) {
                const navStyles = getComputedStyle(nav);
                data.nav_styles = {
                    backgroundColor: navStyles.backgroundColor,
                    color: navStyles.color,
                    position: navStyles.position,
                    backdropFilter: navStyles.backdropFilter
                };
            }

            // Get all sections
            document.querySelectorAll('section, [class*="section"]').forEach(section => {
                const styles = getComputedStyle(section);
                data.sections.push({
                    className: section.className,
                    id: section.id,
                    backgroundColor: styles.backgroundColor,
                    color: styles.color,
                    padding: styles.padding
                });
            });

            // Extract colors from all elements
            document.querySelectorAll('*').forEach(el => {
                const styles = getComputedStyle(el);
                if (styles.color) data.colors.add(styles.color);
                if (styles.backgroundColor && styles.backgroundColor !== 'rgba(0, 0, 0, 0)') {
                    data.colors.add(styles.backgroundColor);
                }
            });

            data.colors = Array.from(data.colors);
            return data;
        }
    """)

    return analysis

async def compare_sites():
    """Compare local and TrueNAS sites."""
    print("Starting site comparison...")
    print(f"Local: {LOCAL_URL}")
    print(f"TrueNAS: {TRUENAS_URL}")
    print("-" * 60)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            screen={'width': 1920, 'height': 1080}
        )
        page = await context.new_page()

        # Take screenshots
        print("\n[SCREENSHOTS] Taking screenshots...")
        print("\nLocal site:")
        local_screenshot = await take_screenshot(page, LOCAL_URL, "local")

        print("\nTrueNAS site:")
        truenas_screenshot = await take_screenshot(page, TRUENAS_URL, "truenas")

        # Analyze both sites
        print("\n[ANALYSIS] Analyzing local site...")
        local_analysis = await analyze_page(page, LOCAL_URL, "local")

        print("[ANALYSIS] Analyzing TrueNAS site...")
        truenas_analysis = await analyze_page(page, TRUENAS_URL, "truenas")

        await browser.close()

    # Save analysis to JSON
    analysis_file = OUTPUT_DIR / "analysis.json"
    with open(analysis_file, 'w') as f:
        json.dump({
            'timestamp': datetime.now().isoformat(),
            'local': local_analysis,
            'truenas': truenas_analysis
        }, f, indent=2)

    print(f"\n[OK] Analysis saved: {analysis_file}")

    # Generate comparison report
    generate_report(local_analysis, truenas_analysis)

def generate_report(local, truenas):
    """Generate a detailed comparison report."""
    report_file = OUTPUT_DIR / "comparison_report.md"

    with open(report_file, 'w') as f:
        f.write("# ISN.BIZ Website Comparison Report\n\n")
        f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("---\n\n")

        # Title comparison
        f.write("## Page Titles\n\n")
        f.write(f"- **Local:** {local['title']}\n")
        f.write(f"- **TrueNAS:** {truenas['title']}\n")
        if local['title'] != truenas['title']:
            f.write(f"  - [WARN] **DIFFERENT**\n")
        f.write("\n")

        # Body styles
        f.write("## Body Styles\n\n")
        f.write("### Local\n")
        for key, value in local['body_styles'].items():
            f.write(f"- **{key}:** {value}\n")
        f.write("\n### TrueNAS\n")
        for key, value in truenas['body_styles'].items():
            f.write(f"- **{key}:** {value}\n")

        # Find differences
        f.write("\n### Differences\n")
        differences = []
        for key in local['body_styles']:
            if local['body_styles'].get(key) != truenas['body_styles'].get(key):
                differences.append(f"- **{key}:** Local=`{local['body_styles'].get(key)}` vs TrueNAS=`{truenas['body_styles'].get(key)}`")

        if differences:
            f.write("\n".join(differences) + "\n")
        else:
            f.write("[OK] No differences\n")
        f.write("\n")

        # Hero section
        f.write("## Hero Section Styles\n\n")
        f.write("### Local\n")
        for key, value in local['hero_styles'].items():
            f.write(f"- **{key}:** {value}\n")
        f.write("\n### TrueNAS\n")
        for key, value in truenas['hero_styles'].items():
            f.write(f"- **{key}:** {value}\n")

        # Find hero differences
        f.write("\n### Differences\n")
        hero_differences = []
        for key in local['hero_styles']:
            if local['hero_styles'].get(key) != truenas['hero_styles'].get(key):
                hero_differences.append(f"- **{key}:** Local=`{local['hero_styles'].get(key)}` vs TrueNAS=`{truenas['hero_styles'].get(key)}`")

        if hero_differences:
            f.write("\n".join(hero_differences) + "\n")
        else:
            f.write("[OK] No differences\n")
        f.write("\n")

        # Navigation
        f.write("## Navigation Styles\n\n")
        f.write("### Local\n")
        for key, value in local['nav_styles'].items():
            f.write(f"- **{key}:** {value}\n")
        f.write("\n### TrueNAS\n")
        for key, value in truenas['nav_styles'].items():
            f.write(f"- **{key}:** {value}\n")

        # Find nav differences
        f.write("\n### Differences\n")
        nav_differences = []
        for key in local['nav_styles']:
            if local['nav_styles'].get(key) != truenas['nav_styles'].get(key):
                nav_differences.append(f"- **{key}:** Local=`{local['nav_styles'].get(key)}` vs TrueNAS=`{truenas['nav_styles'].get(key)}`")

        if nav_differences:
            f.write("\n".join(nav_differences) + "\n")
        else:
            f.write("[OK] No differences\n")
        f.write("\n")

        # Fonts
        f.write("## Fonts\n\n")
        f.write(f"### Local ({len(local['fonts'])} fonts)\n")
        for font in sorted(local['fonts'])[:10]:  # Top 10
            f.write(f"- {font}\n")
        f.write(f"\n### TrueNAS ({len(truenas['fonts'])} fonts)\n")
        for font in sorted(truenas['fonts'])[:10]:  # Top 10
            f.write(f"- {font}\n")

        # Font differences
        local_fonts = set(local['fonts'])
        truenas_fonts = set(truenas['fonts'])
        only_local = local_fonts - truenas_fonts
        only_truenas = truenas_fonts - local_fonts

        if only_local:
            f.write(f"\n### Only in Local\n")
            for font in sorted(only_local):
                f.write(f"- {font}\n")

        if only_truenas:
            f.write(f"\n### Only in TrueNAS\n")
            for font in sorted(only_truenas):
                f.write(f"- {font}\n")
        f.write("\n")

        # CSS files
        f.write("## CSS Files\n\n")
        f.write("### Local\n")
        for css in local['css_files']:
            f.write(f"- {css}\n")
        f.write("\n### TrueNAS\n")
        for css in truenas['css_files']:
            f.write(f"- {css}\n")
        f.write("\n")

        # Images
        f.write("## Images\n\n")
        f.write(f"### Local ({len(local['images'])} images)\n")
        for img in local['images'][:10]:  # Top 10
            f.write(f"- **{img['src']}** ({img['width']}x{img['height']})\n")
        f.write(f"\n### TrueNAS ({len(truenas['images'])} images)\n")
        for img in truenas['images'][:10]:  # Top 10
            f.write(f"- **{img['src']}** ({img['width']}x{img['height']})\n")
        f.write("\n")

        # Color palette
        f.write("## Color Palette\n\n")
        f.write(f"### Local ({len(local['colors'])} unique colors)\n")
        for color in sorted(local['colors'])[:20]:  # Top 20
            f.write(f"- {color}\n")
        f.write(f"\n### TrueNAS ({len(truenas['colors'])} unique colors)\n")
        for color in sorted(truenas['colors'])[:20]:  # Top 20
            f.write(f"- {color}\n")
        f.write("\n")

        # Sections
        f.write("## Sections\n\n")
        f.write(f"### Local ({len(local['sections'])} sections)\n")
        for section in local['sections']:
            f.write(f"- **{section['className'] or section['id'] or 'unnamed'}**\n")
            f.write(f"  - Background: {section['backgroundColor']}\n")
            f.write(f"  - Color: {section['color']}\n")
        f.write(f"\n### TrueNAS ({len(truenas['sections'])} sections)\n")
        for section in truenas['sections']:
            f.write(f"- **{section['className'] or section['id'] or 'unnamed'}**\n")
            f.write(f"  - Background: {section['backgroundColor']}\n")
            f.write(f"  - Color: {section['color']}\n")
        f.write("\n")

        # Summary
        f.write("## Summary\n\n")
        total_differences = len(differences) + len(hero_differences) + len(nav_differences)

        if total_differences > 0:
            f.write(f"[WARN] **Found {total_differences} style differences**\n\n")
            f.write("### Key Differences:\n")
            if differences:
                f.write("- Body styles differ\n")
            if hero_differences:
                f.write("- Hero section styles differ\n")
            if nav_differences:
                f.write("- Navigation styles differ\n")
            if only_local:
                f.write(f"- {len(only_local)} fonts only in local\n")
            if only_truenas:
                f.write(f"- {len(only_truenas)} fonts only in TrueNAS\n")
        else:
            f.write("[OK] **No major style differences detected**\n")

    print(f"\n[OK] Report saved: {report_file}")
    print("\n" + "="*60)
    print("COMPARISON COMPLETE!")
    print("="*60)
    print(f"\nScreenshots: {OUTPUT_DIR}/")
    print(f"Report: {report_file}")
    print(f"Analysis: {OUTPUT_DIR}/analysis.json")

if __name__ == "__main__":
    asyncio.run(compare_sites())
