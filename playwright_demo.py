# Playwright Python 使用示例
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