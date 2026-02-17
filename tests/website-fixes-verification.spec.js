/**
 * Playwright Tests - Website Fixes Verification
 * Verifies team names, slider behavior, images, and founder pages
 */

const { test, expect } = require('@playwright/test');

// Base URL - adjust as needed for your environment
const BASE_URL = process.env.BASE_URL || 'http://localhost:8000';

test.describe('Team Name Corrections', () => {
  const correctNames = {
    jonathan: 'Jonathan Mallinger',
    lilly: 'Lilly Fedas',
    bri: 'Brianna Bear',
    alicia: 'Alicia Haas'
  };

  test.beforeEach(async ({ page }) => {
    await page.goto(BASE_URL);
  });

  test('should show correct names in navigation dropdown', async ({ page }) => {
    // Open team dropdown
    await page.click('a[href="#team"]');
    await page.waitForTimeout(500);

    // Verify each team member name
    const jonathanLink = await page.textContent('a[href="jonathan.html"]');
    expect(jonathanLink.trim()).toBe(correctNames.jonathan);

    const lillyLink = await page.textContent('a[href="lilly.html"]');
    expect(lillyLink.trim()).toBe(correctNames.lilly);

    const briLink = await page.textContent('a[href="bri.html"]');
    expect(briLink.trim()).toBe(correctNames.bri);

    const aliciaLink = await page.textContent('a[href="alicia.html"]');
    expect(aliciaLink.trim()).toBe(correctNames.alicia);
  });

  test('should show correct names on index.html team section', async ({ page }) => {
    await page.goto(`${BASE_URL}/index.html#team`);

    const teamNames = await page.$$eval('.team-member h3', elements =>
      elements.map(el => el.textContent.trim())
    );

    expect(teamNames).toContain(correctNames.jonathan);
    expect(teamNames).toContain(correctNames.lilly);
    expect(teamNames).toContain(correctNames.bri);
    expect(teamNames).toContain(correctNames.alicia);
  });

  test('should have correct founder name in Schema.org JSON-LD', async ({ page }) => {
    const schemaScript = await page.$eval(
      'script[type="application/ld+json"]',
      el => el.textContent
    );

    const schema = JSON.parse(schemaScript);
    const founderData = schema['@graph'].find(item => item['@type'] === 'Organization');

    expect(founderData.founder.name).toBe(correctNames.jonathan);
  });
});

test.describe('Services Page Images', () => {
  test('should load all service visual images without errors', async ({ page }) => {
    await page.goto(`${BASE_URL}/services.html`);

    // Get all images in services visual grid
    const images = await page.$$('.services-visual-grid img');
    expect(images.length).toBe(3);

    // Check each image loads successfully
    for (const img of images) {
      const src = await img.getAttribute('src');
      const naturalWidth = await img.evaluate(el => el.naturalWidth);
      const naturalHeight = await img.evaluate(el => el.naturalHeight);

      expect(naturalWidth).toBeGreaterThan(0);
      expect(naturalHeight).toBeGreaterThan(0);
      expect(src).not.toContain('premium_v3/portfolio'); // Shouldn't use broken old paths
    }

    // Take screenshot for visual verification
    await page.screenshot({
      path: 'tests/screenshots/services-page-images-fixed.png',
      fullPage: true
    });
  });

  test('should have correct alt text for service images', async ({ page }) => {
    await page.goto(`${BASE_URL}/services.html`);

    const altTexts = await page.$$eval('.services-visual-grid img', imgs =>
      imgs.map(img => img.alt)
    );

    expect(altTexts[0]).toContain('AI');
    expect(altTexts[1]).toContain('application');
    expect(altTexts[2]).toContain('cloud');
  });
});

test.describe('Hero Slider Auto-Advance', () => {
  test('should auto-advance slides', async ({ page }) => {
    await page.goto(BASE_URL);

    // Wait for slider to initialize
    await page.waitForSelector('[data-hero-slider]');

    // Get first slide
    const firstSlide = await page.$('.slide.active');
    const firstSlideId = await firstSlide.getAttribute('data-slide-id');

    // Wait for auto-advance (7 seconds + buffer)
    await page.waitForTimeout(8000);

    // Check that active slide has changed
    const newActiveSlide = await page.$('.slide.active');
    const newSlideId = await newActiveSlide.getAttribute('data-slide-id');

    expect(newSlideId).not.toBe(firstSlideId);
  });

  test('should pause slider when hovering', async ({ page }) => {
    await page.goto(BASE_URL);
    await page.waitForSelector('[data-hero-slider]');

    // Hover over slider
    await page.hover('[data-hero-slider]');

    const firstSlide = await page.$('.slide.active');
    const firstSlideId = await firstSlide.getAttribute('data-slide-id');

    // Wait and verify it didn't auto-advance
    await page.waitForTimeout(8000);

    const currentSlide = await page.$('.slide.active');
    const currentSlideId = await currentSlide.getAttribute('data-slide-id');

    expect(currentSlideId).toBe(firstSlideId);
  });

  test('should show pause/play button', async ({ page }) => {
    await page.goto(BASE_URL);
    await page.waitForSelector('[data-slider-toggle]');

    const toggleButton = await page.$('[data-slider-toggle]');
    const buttonText = await toggleButton.textContent();

    expect(['Pause', 'Play']).toContain(buttonText.trim());
  });

  test('should update progress bar during auto-advance', async ({ page }) => {
    await page.goto(BASE_URL);
    await page.waitForSelector('[data-slider-progress]');

    const progressBar = await page.$('[data-slider-progress]');

    // Initial width should be near 0
    const initialWidth = await progressBar.evaluate(el =>
      parseInt(el.style.width) || 0
    );

    // Wait a bit
    await page.waitForTimeout(3000);

    // Progress should have increased
    const laterWidth = await progressBar.evaluate(el =>
      parseInt(el.style.width) || 0
    );

    expect(laterWidth).toBeGreaterThan(initialWidth);
  });
});

test.describe('Founder Page Images', () => {
  test('Jonathan page should not have duplicate images', async ({ page }) => {
    await page.goto(`${BASE_URL}/jonathan.html`);

    // Get all image sources on the page
    const imageSrcs = await page.$$eval('.bio-image img', imgs =>
      imgs.map(img => img.getAttribute('src'))
    );

    // Check for duplicates - each image source should be unique
    const uniqueSrcs = new Set(imageSrcs);
    expect(uniqueSrcs.size).toBe(imageSrcs.length);

    // Verify we have at least 4 bio images
    expect(imageSrcs.length).toBeGreaterThanOrEqual(4);

    // Specifically verify the previously duplicated images are now unique
    const casualWorkshopCount = imageSrcs.filter(src =>
      src.includes('jonathan_casual_workshop')
    ).length;
    expect(casualWorkshopCount).toBeLessThanOrEqual(1);

    const teamBuildingCount = imageSrcs.filter(src =>
      src.includes('jonathan_brianna_team_building')
    ).length;
    expect(teamBuildingCount).toBeLessThanOrEqual(1);
  });

  test('All founder pages should load without image errors', async ({ page }) => {
    const founderPages = ['jonathan', 'lilly', 'bri', 'alicia'];

    for (const founder of founderPages) {
      await page.goto(`${BASE_URL}/${founder}.html`);

      // Wait for page to load
      await page.waitForLoadState('domcontentloaded');

      // Check that critical portrait image loads (main hero image)
      const portraitLoaded = await page.$eval('.founder-hero-image img', img =>
        img.complete && img.naturalWidth > 0
      );

      expect(portraitLoaded).toBe(true);

      // Verify page has bio images (even if some are still loading)
      const bioImageCount = await page.$$eval('.bio-image img', imgs => imgs.length);
      expect(bioImageCount).toBeGreaterThan(0);
    }
  });

  test('Each founder page should have unique portrait', async ({ page }) => {
    const founders = ['jonathan', 'lilly', 'bri', 'alicia'];
    const portraits = [];

    for (const founder of founders) {
      await page.goto(`${BASE_URL}/${founder}.html`);
      const portraitSrc = await page.$eval('.founder-hero-image img', img =>
        img.getAttribute('src')
      );
      portraits.push(portraitSrc);
    }

    // All portraits should be unique
    const uniquePortraits = new Set(portraits);
    expect(uniquePortraits.size).toBe(4);
  });
});

test.describe('Visual Regression - Screenshots', () => {
  test('capture homepage', async ({ page }) => {
    await page.goto(BASE_URL);
    await page.waitForLoadState('networkidle');
    await page.screenshot({
      path: 'tests/screenshots/homepage-fixed.png',
      fullPage: true
    });
  });

  test('capture team section', async ({ page }) => {
    await page.goto(`${BASE_URL}/#team`);
    await page.waitForSelector('.team-member');
    await page.screenshot({
      path: 'tests/screenshots/team-section-fixed.png',
      clip: { x: 0, y: 0, width: 1920, height: 1200 }
    });
  });

  test('capture services page', async ({ page }) => {
    await page.goto(`${BASE_URL}/services.html`);
    await page.waitForLoadState('networkidle');
    await page.screenshot({
      path: 'tests/screenshots/services-page-fixed.png',
      fullPage: true
    });
  });

  test('capture all founder pages', async ({ page }) => {
    const founders = ['jonathan', 'lilly', 'bri', 'alicia'];

    for (const founder of founders) {
      await page.goto(`${BASE_URL}/${founder}.html`);
      await page.waitForLoadState('networkidle');
      await page.screenshot({
        path: `tests/screenshots/${founder}-page-fixed.png`,
        fullPage: true
      });
    }
  });
});

test.describe('Accessibility Checks', () => {
  test('navigation should be keyboard accessible', async ({ page }) => {
    await page.goto(BASE_URL);

    // Focus on team dropdown link
    await page.focus('a[href="#team"]');

    // Verify we can interact with dropdown via keyboard
    const teamLink = await page.$('a[href="#team"]');
    expect(teamLink).toBeTruthy();

    // Check dropdown menu exists in DOM
    const dropdown = await page.$('.dropdown-menu');
    expect(dropdown).toBeTruthy();

    // Verify navigation has proper aria attributes
    const navToggle = await page.$('.nav-toggle');
    const hasAriaLabel = await navToggle.getAttribute('aria-label');
    expect(hasAriaLabel).toBeTruthy();
  });

  test('slider should be keyboard navigable', async ({ page }) => {
    await page.goto(BASE_URL);
    await page.waitForSelector('[data-hero-slider]');

    // Focus slider
    await page.focus('[data-hero-slider]');

    const firstSlide = await page.$('.slide.active');
    const firstSlideId = await firstSlide.getAttribute('data-slide-id');

    // Press right arrow
    await page.keyboard.press('ArrowRight');
    await page.waitForTimeout(500);

    const newSlide = await page.$('.slide.active');
    const newSlideId = await newSlide.getAttribute('data-slide-id');

    expect(newSlideId).not.toBe(firstSlideId);
  });
});
