// Simple Playwright test to verify installation
const { chromium } = require('playwright');

(async () => {
  console.log('🚀 Launching browser...');
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();

  console.log('🌐 Navigating to example.com...');
  await page.goto('https://example.com');

  console.log('📸 Taking screenshot...');
  await page.screenshot({ path: 'example-screenshot.png' });

  console.log('📄 Getting page title...');
  const title = await page.title();
  console.log(`   Title: ${title}`);

  console.log('🔍 Getting page content...');
  const content = await page.textContent('h1');
  console.log(`   H1 text: ${content}`);

  await browser.close();
  console.log('✅ Test completed successfully!');
  console.log('📷 Screenshot saved as: example-screenshot.png');
})();
