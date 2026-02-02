const { chromium } = require('playwright');
const fs = require('fs');

async function compareWebsites() {
  const browser = await chromium.launch();
  const context = await browser.newContext({
    viewport: { width: 1920, height: 1080 }
  });

  // Create screenshots directory
  if (!fs.existsSync('screenshots')) {
    fs.mkdirSync('screenshots');
  }

  // Screenshot local version
  console.log('Taking screenshot of local version (http://localhost:9393)...');
  const localPage = await context.newPage();
  try {
    await localPage.goto('http://localhost:9393', { waitUntil: 'networkidle', timeout: 30000 });
    await localPage.screenshot({
      path: 'screenshots/local-full.png',
      fullPage: true
    });
    await localPage.screenshot({
      path: 'screenshots/local-viewport.png',
      fullPage: false
    });
    console.log('✅ Local screenshots saved');

    // Get local page details
    const localTitle = await localPage.title();
    const localHTML = await localPage.content();

    // Extract some styling information
    const localStyles = await localPage.evaluate(() => {
      const styles = window.getComputedStyle(document.body);
      return {
        backgroundColor: styles.backgroundColor,
        color: styles.color,
        fontFamily: styles.fontFamily,
        fontSize: styles.fontSize
      };
    });

    console.log('Local page title:', localTitle);
    console.log('Local body styles:', localStyles);

    // Save HTML for comparison
    fs.writeFileSync('screenshots/local.html', localHTML);

  } catch (error) {
    console.error('❌ Error with local site:', error.message);
  }
  await localPage.close();

  // Screenshot TrueNAS version
  console.log('\nTaking screenshot of TrueNAS version (https://isn.biz)...');
  const truenasPage = await context.newPage();
  try {
    await truenasPage.goto('https://isn.biz', { waitUntil: 'networkidle', timeout: 30000 });
    await truenasPage.screenshot({
      path: 'screenshots/truenas-full.png',
      fullPage: true
    });
    await truenasPage.screenshot({
      path: 'screenshots/truenas-viewport.png',
      fullPage: false
    });
    console.log('✅ TrueNAS screenshots saved');

    // Get TrueNAS page details
    const truenasTitle = await truenasPage.title();
    const truenasHTML = await truenasPage.content();

    // Extract styling information
    const truenasStyles = await truenasPage.evaluate(() => {
      const styles = window.getComputedStyle(document.body);
      return {
        backgroundColor: styles.backgroundColor,
        color: styles.color,
        fontFamily: styles.fontFamily,
        fontSize: styles.fontSize
      };
    });

    console.log('TrueNAS page title:', truenasTitle);
    console.log('TrueNAS body styles:', truenasStyles);

    // Save HTML for comparison
    fs.writeFileSync('screenshots/truenas.html', truenasHTML);

  } catch (error) {
    console.error('❌ Error with TrueNAS site:', error.message);
  }
  await truenasPage.close();

  await browser.close();

  console.log('\n✅ Screenshot comparison complete!');
  console.log('Screenshots saved in ./screenshots/');
  console.log('  - local-full.png (full page)');
  console.log('  - local-viewport.png (above the fold)');
  console.log('  - truenas-full.png (full page)');
  console.log('  - truenas-viewport.png (above the fold)');
  console.log('  - local.html (HTML source)');
  console.log('  - truenas.html (HTML source)');
}

compareWebsites().catch(console.error);
