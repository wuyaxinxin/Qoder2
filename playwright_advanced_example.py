# Playwright 高级功能示例
from playwright.sync_api import sync_playwright
import asyncio

def run(playwright):
    # 启动浏览器
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    
    # 设置视口大小
    page.set_viewport_size({"width": 1280, "height": 720})
    
    # 导航到网站
    page.goto("https://httpbin.org/")
    
    # 等待特定元素出现
    page.wait_for_selector("h1")
    
    # 获取页面标题
    title = page.title()
    print(f"页面标题: {title}")
    
    # 获取页面内容
    content = page.content()
    print(f"页面内容长度: {len(content)} 字符")
    
    # 截取整个页面截图
    page.screenshot(path="httpbin_full_page.png", full_page=True)
    
    # 导航到表单页面
    page.goto("https://httpbin.org/forms/post")
    
    # 填写表单
    page.fill("input[name='custname']","张三")
    page.fill("input[name='custtel']", "13800138000")
    page.fill("input[name='custemail']", "zhangsan@example.com")
    
    # 选择下拉选项
    page.select_option("select[name='size']", "medium")
    
    # 点击复选框
    page.check("input[name='topping'][value='bacon']")
    page.check("input[name='topping'][value='cheese']")
    
    # 截取表单填写后的截图
    page.screenshot(path="form_filled.png")
    
    # 提交表单
    page.click("button[type='submit']")
    
    # 等待页面加载
    page.wait_for_load_state("networkidle")
    
    # 获取结果页面的标题
    result_title = page.title()
    print(f"结果页面标题: {result_title}")
    
    # 关闭浏览器
    browser.close()

# 运行示例
with sync_playwright() as playwright:
    run(playwright)