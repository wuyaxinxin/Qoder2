// Playwright 使用示例
const { chromium } = require('playwright');

(async () => {
  // 启动浏览器
  const browser = await chromium.launch({ headless: false });
  const page = await browser.newPage();
  
  // 导航到网站
  await page.goto('https://example.com');
  
  // 截取屏幕截图
  await page.screenshot({ path: 'example.png' });
  
  // 获取页面标题
  const title = await page.title();
  console.log('页面标题:', title);
  
  // 关闭浏览器
  await browser.close();
})();