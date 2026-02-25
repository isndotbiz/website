// @ts-check
const { test, expect } = require('@playwright/test');

const BASE_URL = process.env.BASE_URL || 'https://isn.biz';

const ALL_PAGES = [
  { path: '/', name: 'Home' },
  { path: '/about', name: 'About' },
  { path: '/services', name: 'Services' },
  { path: '/portfolio', name: 'Portfolio' },
  { path: '/investors', name: 'Investors' },
  { path: '/contact', name: 'Contact' },
  { path: '/opportunity-bot', name: 'Opportunity Bot' },
  { path: '/truenas', name: 'TrueNAS' },
  { path: '/bin-intelligence', name: 'BIN Intelligence' },
  { path: '/spiritatlas', name: 'SpiritAtlas' },
  { path: '/videogen', name: 'VideoGen' },
  { path: '/comfyui', name: 'ComfyUI' },
  { path: '/gedcom', name: 'GEDCOM' },
  { path: '/llm-optimization', name: 'LLM Optimization' },
  { path: '/aurallm', name: 'AuraLLM' },
  { path: '/jonathan', name: 'Jonathan' },
  { path: '/bri', name: 'Bri' },
  { path: '/lilly', name: 'Lilly' },
  { path: '/alicia', name: 'Alicia' },
];

const PRODUCT_PAGES = ALL_PAGES.filter(p =>
  ['/opportunity-bot', '/truenas', '/bin-intelligence', '/spiritatlas',
   '/videogen', '/comfyui', '/gedcom', '/llm-optimization', '/aurallm'].includes(p.path)
);

const FOUNDER_PAGES = ALL_PAGES.filter(p =>
  ['/jonathan', '/bri', '/lilly', '/alicia'].includes(p.path)
);

// Use domcontentloaded for all goto() calls - we test DOM structure, not image downloads
const GOTO_OPTS = { waitUntil: 'domcontentloaded' };

// ==================== PAGE LOADING ====================
test.describe('Page Loading', () => {
  for (const page of ALL_PAGES) {
    test(`${page.name} loads with 200 status`, async ({ request }) => {
      const resp = await request.get(`${BASE_URL}${page.path}`);
      expect(resp.status()).toBe(200);
    });
  }
});

// ==================== NAV UNIFORMITY ====================
test.describe('Navigation Uniformity', () => {
  for (const page of ALL_PAGES) {
    test(`${page.name} has standard nav with 6 menu items`, async ({ page: p }) => {
      await p.goto(`${BASE_URL}${page.path}`, GOTO_OPTS);

      // Nav exists
      const nav = p.locator('nav.nav');
      await expect(nav).toBeVisible();

      // Logo links to /
      const logoLink = nav.locator('.logo a');
      await expect(logoLink).toHaveAttribute('href', '/');

      // Logo image exists
      const logoImg = nav.locator('.logo-img');
      await expect(logoImg).toHaveCount(1);

      // 6 menu items: About, Services, Portfolio, Investors, Team, Contact
      const menuItems = nav.locator('.nav-menu > li');
      await expect(menuItems).toHaveCount(6);

      // Correct hrefs for main nav links (skip Team at index 4 - it's a dropdown with #team)
      const expectedLinks = ['/about', '/services', '/portfolio', '/investors'];
      for (let i = 0; i < expectedLinks.length; i++) {
        await expect(menuItems.nth(i).locator('a')).toHaveAttribute('href', expectedLinks[i]);
      }
      await expect(menuItems.nth(5).locator('a')).toHaveAttribute('href', '/contact');

      // Mobile toggle exists
      const toggle = nav.locator('.nav-toggle');
      await expect(toggle).toHaveCount(1);
    });
  }
});

// ==================== FOOTER UNIFORMITY ====================
test.describe('Footer Uniformity', () => {
  for (const page of ALL_PAGES) {
    test(`${page.name} has standard 4-column footer`, async ({ page: p }) => {
      await p.goto(`${BASE_URL}${page.path}`, GOTO_OPTS);

      const footer = p.locator('footer.footer');
      await expect(footer).toBeAttached();

      // 4 footer columns
      const columns = footer.locator('.footer-column');
      await expect(columns).toHaveCount(4);

      // Credentials present
      await expect(footer.locator('text=080513772')).toBeAttached(); // DUNS
      await expect(footer.locator('text=603-522-339')).toBeAttached(); // UBI
      await expect(footer.locator('text=47-4530188')).toBeAttached(); // EIN

      // Leadership links
      await expect(footer.locator('a[href="/jonathan"]')).toBeAttached();
      await expect(footer.locator('a[href="/bri"]')).toBeAttached();
      await expect(footer.locator('a[href="/lilly"]')).toBeAttached();
      await expect(footer.locator('a[href="/alicia"]')).toBeAttached();

      // Footer bottom
      await expect(footer.locator('.footer-bottom')).toBeAttached();
      await expect(footer.locator('text=2026 iSN.BiZ Inc')).toBeAttached();
    });
  }
});

// ==================== SECTIONS VISIBLE (not hidden by CSS) ====================
test.describe('Section Visibility', () => {
  for (const page of ALL_PAGES) {
    test(`${page.name} sections become visible on scroll`, async ({ page: p }) => {
      await p.goto(`${BASE_URL}${page.path}`, GOTO_OPTS);
      // Wait for DOMContentLoaded scripts (including IntersectionObserver setup)
      await p.waitForTimeout(500);

      // Scroll incrementally through the page to trigger IntersectionObserver for all sections
      await p.evaluate(async () => {
        const delay = ms => new Promise(r => setTimeout(r, ms));
        const totalHeight = document.body.scrollHeight;
        for (let y = 0; y < totalHeight; y += 300) {
          window.scrollTo(0, y);
          await delay(80);
        }
        window.scrollTo(0, totalHeight);
      });
      await p.waitForTimeout(1000);

      // All .section elements should have an animation class (visible or animate-in)
      const sections = await p.locator('.section').all();
      for (const section of sections) {
        const classes = await section.getAttribute('class');
        expect(classes, `Section missing animation class on ${page.name}`).toMatch(/visible|animate-in/);
      }
    });
  }
});

// ==================== IMAGE LOADING ====================
test.describe('Images Load from S3', () => {
  test.setTimeout(60000); // 60s per test for image-heavy pages

  for (const page of ALL_PAGES) {
    test(`${page.name} all images load successfully`, async ({ page: p }) => {
      const failedImages = [];

      // Listen for failed image requests
      p.on('response', response => {
        if (response.url().match(/\.(webp|png|jpg|jpeg)/) && response.status() >= 400) {
          failedImages.push({ url: response.url(), status: response.status() });
        }
      });

      await p.goto(`${BASE_URL}${page.path}`, GOTO_OPTS);
      await p.waitForTimeout(2000);

      // Scroll through page to trigger lazy-loaded images
      await p.evaluate(async () => {
        const delay = ms => new Promise(r => setTimeout(r, ms));
        for (let i = 0; i < document.body.scrollHeight; i += 500) {
          window.scrollTo(0, i);
          await delay(100);
        }
      });
      await p.waitForTimeout(3000);

      // Check all images point to S3
      const imgSrcs = await p.locator('img').evaluateAll(imgs =>
        imgs.map(img => ({ src: img.src, loaded: img.complete && img.naturalWidth > 0 }))
      );

      const localImages = imgSrcs.filter(i => i.src && !i.src.includes('s3') && !i.src.startsWith('data:'));
      expect(localImages, `Found local (non-S3) images on ${page.name}: ${JSON.stringify(localImages)}`).toHaveLength(0);

      expect(failedImages, `Failed images on ${page.name}: ${JSON.stringify(failedImages)}`).toHaveLength(0);
    });
  }
});

// ==================== WORD COUNTS ====================
test.describe('Word Count Minimums', () => {
  for (const page of PRODUCT_PAGES) {
    test(`${page.name} has >= 1332 words`, async ({ page: p }) => {
      await p.goto(`${BASE_URL}${page.path}`, GOTO_OPTS);
      const text = await p.locator('body').innerText();
      const words = text.split(/\s+/).filter(w => w.length > 0).length;
      expect(words, `${page.name} has ${words} words (minimum 1332)`).toBeGreaterThanOrEqual(1332);
    });
  }

  for (const page of FOUNDER_PAGES) {
    test(`${page.name} has >= 666 words`, async ({ page: p }) => {
      await p.goto(`${BASE_URL}${page.path}`, GOTO_OPTS);
      const text = await p.locator('body').innerText();
      const words = text.split(/\s+/).filter(w => w.length > 0).length;
      expect(words, `${page.name} has ${words} words (minimum 666)`).toBeGreaterThanOrEqual(666);
    });
  }
});

// ==================== META TAGS / SEO ====================
test.describe('SEO Basics', () => {
  for (const page of ALL_PAGES) {
    test(`${page.name} has title and meta description`, async ({ page: p }) => {
      await p.goto(`${BASE_URL}${page.path}`, GOTO_OPTS);

      const title = await p.title();
      expect(title.length, `${page.name} title is empty`).toBeGreaterThan(5);

      const metaDesc = await p.locator('meta[name="description"]').getAttribute('content');
      expect(metaDesc, `${page.name} missing meta description`).toBeTruthy();
      expect(metaDesc.length, `${page.name} meta description too short`).toBeGreaterThan(20);
    });
  }
});

// ==================== MOBILE RESPONSIVE ====================
test.describe('Mobile Responsive', () => {
  test.use({ viewport: { width: 375, height: 812 } }); // iPhone X

  for (const page of ALL_PAGES.slice(0, 5)) { // Test first 5 pages on mobile
    test(`${page.name} renders on mobile without horizontal scroll`, async ({ page: p }) => {
      await p.goto(`${BASE_URL}${page.path}`, GOTO_OPTS);
      await p.waitForTimeout(500);

      const bodyWidth = await p.evaluate(() => document.body.scrollWidth);
      const viewportWidth = await p.evaluate(() => window.innerWidth);
      expect(bodyWidth, `${page.name} has horizontal overflow: body=${bodyWidth} viewport=${viewportWidth}`).toBeLessThanOrEqual(viewportWidth + 5);
    });
  }
});

// ==================== PERFORMANCE ====================
test.describe('Performance', () => {
  test('Home page loads under 5 seconds', async ({ page: p }) => {
    const start = Date.now();
    await p.goto(`${BASE_URL}/`, { waitUntil: 'domcontentloaded' });
    const loadTime = Date.now() - start;
    expect(loadTime, `Home page took ${loadTime}ms`).toBeLessThan(5000);
  });
});
