const { chromium } = require('playwright');
const fs = require('fs');

async function detailedComparison() {
  const browser = await chromium.launch();
  const context = await browser.newContext({
    viewport: { width: 1920, height: 1080 }
  });

  const report = {
    local: {},
    truenas: {},
    differences: []
  };

  // Analyze local version
  console.log('Analyzing local version...');
  const localPage = await context.newPage();
  await localPage.goto('http://localhost:9393', { waitUntil: 'networkidle', timeout: 30000 });

  report.local = await localPage.evaluate(() => {
    // Get all stylesheets
    const stylesheets = Array.from(document.styleSheets).map(sheet => {
      try {
        return {
          href: sheet.href,
          rules: sheet.cssRules ? sheet.cssRules.length : 0
        };
      } catch (e) {
        return { href: sheet.href, error: 'Cannot access' };
      }
    });

    // Get all loaded resources
    const resources = performance.getEntriesByType('resource').map(r => ({
      name: r.name,
      type: r.initiatorType,
      size: r.transferSize
    }));

    // Get computed styles for key elements
    const heroSection = document.querySelector('.hero-section, #hero');
    const navBar = document.querySelector('nav, .navbar');
    const body = document.body;

    const getStyles = (element) => {
      if (!element) return null;
      const styles = window.getComputedStyle(element);
      return {
        backgroundColor: styles.backgroundColor,
        backgroundImage: styles.backgroundImage,
        color: styles.color,
        fontFamily: styles.fontFamily,
        fontSize: styles.fontSize,
        padding: styles.padding,
        margin: styles.margin
      };
    };

    // Get all CSS custom properties (variables)
    const rootStyles = getComputedStyle(document.documentElement);
    const cssVariables = {};
    for (let i = 0; i < rootStyles.length; i++) {
      const prop = rootStyles[i];
      if (prop.startsWith('--')) {
        cssVariables[prop] = rootStyles.getPropertyValue(prop);
      }
    }

    // Check for specific CSS classes
    const hasClasses = {
      'hero-section': !!document.querySelector('.hero-section'),
      'hero-content': !!document.querySelector('.hero-content'),
      'hero-gradient': !!document.querySelector('.hero-gradient'),
      'stats-grid': !!document.querySelector('.stats-grid'),
      'cta-button': !!document.querySelector('.cta-button'),
      'cta-primary': !!document.querySelector('.cta-primary'),
      'cta-secondary': !!document.querySelector('.cta-secondary')
    };

    // Get background images
    const backgroundImages = Array.from(document.querySelectorAll('*')).filter(el => {
      const bg = getComputedStyle(el).backgroundImage;
      return bg && bg !== 'none';
    }).map(el => ({
      tag: el.tagName,
      class: el.className,
      backgroundImage: getComputedStyle(el).backgroundImage
    }));

    return {
      title: document.title,
      stylesheets,
      resources,
      cssVariables,
      hasClasses,
      bodyStyles: getStyles(body),
      heroStyles: getStyles(heroSection),
      navStyles: getStyles(navBar),
      backgroundImages,
      scripts: Array.from(document.scripts).map(s => s.src || 'inline'),
      fonts: Array.from(document.fonts).map(f => f.family)
    };
  });

  await localPage.close();

  // Analyze TrueNAS version
  console.log('Analyzing TrueNAS version...');
  const truenasPage = await context.newPage();
  await truenasPage.goto('https://isn.biz', { waitUntil: 'networkidle', timeout: 30000 });

  report.truenas = await truenasPage.evaluate(() => {
    // Same analysis as above
    const stylesheets = Array.from(document.styleSheets).map(sheet => {
      try {
        return {
          href: sheet.href,
          rules: sheet.cssRules ? sheet.cssRules.length : 0
        };
      } catch (e) {
        return { href: sheet.href, error: 'Cannot access' };
      }
    });

    const resources = performance.getEntriesByType('resource').map(r => ({
      name: r.name,
      type: r.initiatorType,
      size: r.transferSize
    }));

    const heroSection = document.querySelector('.hero-section, #hero');
    const navBar = document.querySelector('nav, .navbar');
    const body = document.body;

    const getStyles = (element) => {
      if (!element) return null;
      const styles = window.getComputedStyle(element);
      return {
        backgroundColor: styles.backgroundColor,
        backgroundImage: styles.backgroundImage,
        color: styles.color,
        fontFamily: styles.fontFamily,
        fontSize: styles.fontSize,
        padding: styles.padding,
        margin: styles.margin
      };
    };

    const rootStyles = getComputedStyle(document.documentElement);
    const cssVariables = {};
    for (let i = 0; i < rootStyles.length; i++) {
      const prop = rootStyles[i];
      if (prop.startsWith('--')) {
        cssVariables[prop] = rootStyles.getPropertyValue(prop);
      }
    }

    const hasClasses = {
      'hero-section': !!document.querySelector('.hero-section'),
      'hero-content': !!document.querySelector('.hero-content'),
      'hero-gradient': !!document.querySelector('.hero-gradient'),
      'stats-grid': !!document.querySelector('.stats-grid'),
      'cta-button': !!document.querySelector('.cta-button'),
      'cta-primary': !!document.querySelector('.cta-primary'),
      'cta-secondary': !!document.querySelector('.cta-secondary')
    };

    const backgroundImages = Array.from(document.querySelectorAll('*')).filter(el => {
      const bg = getComputedStyle(el).backgroundImage;
      return bg && bg !== 'none';
    }).map(el => ({
      tag: el.tagName,
      class: el.className,
      backgroundImage: getComputedStyle(el).backgroundImage
    }));

    return {
      title: document.title,
      stylesheets,
      resources,
      cssVariables,
      hasClasses,
      bodyStyles: getStyles(body),
      heroStyles: getStyles(heroSection),
      navStyles: getStyles(navBar),
      backgroundImages,
      scripts: Array.from(document.scripts).map(s => s.src || 'inline'),
      fonts: Array.from(document.fonts).map(f => f.family)
    };
  });

  await truenasPage.close();
  await browser.close();

  // Compare and find differences
  console.log('\n=== COMPARISON REPORT ===\n');

  // Compare CSS variables
  console.log('CSS VARIABLES:');
  const localVars = Object.keys(report.local.cssVariables);
  const truenasVars = Object.keys(report.truenas.cssVariables);

  const onlyLocal = localVars.filter(v => !truenasVars.includes(v));
  const onlyTruenas = truenasVars.filter(v => !localVars.includes(v));
  const different = localVars.filter(v =>
    truenasVars.includes(v) &&
    report.local.cssVariables[v] !== report.truenas.cssVariables[v]
  );

  if (onlyLocal.length > 0) {
    console.log('  Only in LOCAL:');
    onlyLocal.forEach(v => console.log(`    ${v}: ${report.local.cssVariables[v]}`));
  }
  if (onlyTruenas.length > 0) {
    console.log('  Only in TRUENAS:');
    onlyTruenas.forEach(v => console.log(`    ${v}: ${report.truenas.cssVariables[v]}`));
  }
  if (different.length > 0) {
    console.log('  DIFFERENT VALUES:');
    different.forEach(v => {
      console.log(`    ${v}:`);
      console.log(`      LOCAL:    ${report.local.cssVariables[v]}`);
      console.log(`      TRUENAS:  ${report.truenas.cssVariables[v]}`);
    });
  }

  // Compare stylesheets
  console.log('\nSTYLESHEETS:');
  console.log('  Local:', report.local.stylesheets.length, 'stylesheets');
  report.local.stylesheets.forEach(s => console.log(`    - ${s.href || 'inline'} (${s.rules} rules)`));
  console.log('  TrueNAS:', report.truenas.stylesheets.length, 'stylesheets');
  report.truenas.stylesheets.forEach(s => console.log(`    - ${s.href || 'inline'} (${s.rules} rules)`));

  // Compare classes
  console.log('\nCSS CLASSES:');
  for (const className in report.local.hasClasses) {
    const localHas = report.local.hasClasses[className];
    const truenasHas = report.truenas.hasClasses[className];
    if (localHas !== truenasHas) {
      console.log(`  ${className}: LOCAL=${localHas}, TRUENAS=${truenasHas}`);
    }
  }

  // Compare hero styles
  console.log('\nHERO SECTION STYLES:');
  if (report.local.heroStyles && report.truenas.heroStyles) {
    for (const prop in report.local.heroStyles) {
      if (report.local.heroStyles[prop] !== report.truenas.heroStyles[prop]) {
        console.log(`  ${prop}:`);
        console.log(`    LOCAL:    ${report.local.heroStyles[prop]}`);
        console.log(`    TRUENAS:  ${report.truenas.heroStyles[prop]}`);
      }
    }
  } else {
    console.log('  LOCAL hero:', report.local.heroStyles);
    console.log('  TRUENAS hero:', report.truenas.heroStyles);
  }

  // Compare background images
  console.log('\nBACKGROUND IMAGES:');
  console.log('  LOCAL:', report.local.backgroundImages.length, 'elements with backgrounds');
  console.log('  TRUENAS:', report.truenas.backgroundImages.length, 'elements with backgrounds');

  // Save full report
  fs.writeFileSync('screenshots/comparison-report.json', JSON.stringify(report, null, 2));
  console.log('\n✅ Full report saved to screenshots/comparison-report.json');
}

detailedComparison().catch(console.error);
