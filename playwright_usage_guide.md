# Playwright 使用指南

## 什么是 Playwright？

Playwright 是一个用于自动化 Chromium、Firefox 和 WebKit 浏览器的库，具有跨浏览器、功能强大、可靠且快速的特点。

## 安装 Playwright

### Node.js 版本
```bash
npm init playwright@latest
```

或者
```bash
npm i -D @playwright/test
npx playwright install
```

### Python 版本
```bash
pip install playwright
playwright install
```

## 基本使用示例

### JavaScript/Node.js 示例
```javascript
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
```

### Python 示例
```python
from playwright.sync_api import sync_playwright

def run(playwright):
    # 启动浏览器
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    
    # 导航到网站
    page.goto("https://example.com")
    
    # 截取屏幕截图
    page.screenshot(path="example_python.png")
    
    # 获取页面标题
    title = page.title()
    print(f"页面标题: {title}")
    
    # 关闭浏览器
    browser.close()

# 运行示例
with sync_playwright() as playwright:
    run(playwright)
```

## 高级功能

### 表单操作
```python
# 填写表单
page.fill("input[name='username']", "your_username")
page.fill("input[name='password']", "your_password")

# 点击按钮
page.click("button[type='submit']")

# 选择下拉选项
page.select_option("select[name='country']", "China")
```

### 等待操作
```python
# 等待元素出现
page.wait_for_selector(".result-item")

# 等待网络空闲
page.wait_for_load_state("networkidle")

# 等待 URL 匹配
page.wait_for_url("**/success")
```

### 页面交互
```python
# 悬停
page.hover(".menu-item")

# 双击
page.dblclick(".element")

# 右键点击
page.click(".element", button="right")
```

## 常用配置选项

### 浏览器启动选项
```javascript
// 有头模式（显示浏览器窗口）
const browser = await chromium.launch({ headless: false });

// 无头模式（不显示浏览器窗口）
const browser = await chromium.launch({ headless: true });

// 设置窗口大小
const browser = await chromium.launch({ 
  headless: false,
  args: ['--window-size=1920,1080'] 
});
```

### 页面设置
```python
# 设置视口大小
page.set_viewport_size({"width": 1280, "height": 720})

# 设置用户代理
page.set_extra_http_headers({
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
})
```

## 截图功能

```python
# 基本截图
page.screenshot(path="screenshot.png")

# 全页面截图
page.screenshot(path="full_page.png", full_page=True)

# 元素截图
page.locator(".specific-element").screenshot(path="element.png")

# 设置截图质量
page.screenshot(path="quality.png", quality=80, type="jpeg")
```

## 调试技巧

1. 使用 `headless: false` 模式查看实际操作过程
2. 使用 `page.pause()` 在特定位置暂停执行
3. 启用详细日志：`DEBUG=pw:api`

## 最佳实践

1. 总是使用等待机制而不是硬编码的延迟
2. 尽可能使用语义化的选择器
3. 合理组织测试代码结构
4. 处理异常情况
5. 清理资源（关闭浏览器）

## 常见问题

### 元素未找到
使用更稳定的定位器：
```python
# 推荐使用 role 定位器
page.get_by_role("button", name="Submit").click()

# 或者使用测试ID
page.get_by_test_id("submit-button").click()
```

### 页面加载问题
```python
# 等待特定元素加载完成
page.wait_for_selector(".content-loaded")

# 等待网络请求完成
page.wait_for_load_state("networkidle")
```

通过以上示例和指南，您可以开始使用 Playwright 进行浏览器自动化测试和网页操作了。