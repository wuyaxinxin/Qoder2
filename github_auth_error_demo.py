"""
始终生效

GitHub权限不足错误复现演示脚本

本脚本专门用于演示和复现GitHub MCP工具在缺少认证时的各种错误信息。
包括 401 Unauthorized、403 Forbidden 等常见认证错误。

功能:
1. 模拟未认证状态下调用需要认证的GitHub工具
2. 展示各种权限不足的错误信息
3. 提供错误处理和降级方案示例
"""

import json
from datetime import datetime


class GitHubAuthErrorDemo:
    """GitHub权限错误复现演示类"""
    
    def __init__(self):
        """初始化"""
        self.error_cases = []
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
    def simulate_401_unauthorized(self):
        """
        复现 401 Unauthorized 错误
        
        场景: 未提供认证信息或认证信息无效
        """
        print("=" * 70)
        print("错误场景 1: 401 Unauthorized - 未授权访问")
        print("=" * 70)
        print()
        print("📋 错误描述:")
        print("  当尝试访问需要认证的GitHub资源时，如果没有提供有效的")
        print("  Personal Access Token，将返回 401 Unauthorized 错误。")
        print()
        print("🔧 触发操作:")
        print("  工具: mcp_github_search_repositories")
        print("  参数: { query: 'python student management' }")
        print("  认证: 未提供 GitHub Token")
        print()
        print("❌ 错误信息:")
        print("-" * 70)
        print("Status: 401")
        print("Message: Bad credentials")
        print("Documentation: https://docs.github.com/rest")
        print()
        print("详细错误:")
        error_response = {
            "message": "Bad credentials",
            "documentation_url": "https://docs.github.com/rest"
        }
        print(json.dumps(error_response, indent=2, ensure_ascii=False))
        print("-" * 70)
        print()
        print("📊 错误分析:")
        print("  原因: GitHub API 要求提供有效的认证凭据")
        print("  影响: 无法使用搜索、创建、修改等需要认证的功能")
        print("  限制: 匿名访问仅限于极少数公开只读接口")
        print()
        
    def simulate_403_forbidden(self):
        """
        复现 403 Forbidden 错误
        
        场景: Token权限不足或访问私有资源
        """
        print("=" * 70)
        print("错误场景 2: 403 Forbidden - 权限不足")
        print("=" * 70)
        print()
        print("📋 错误描述:")
        print("  即使提供了Token，如果Token权限不足或尝试访问私有资源，")
        print("  也会返回 403 Forbidden 错误。")
        print()
        print("🔧 触发操作 A: Token 权限不足")
        print("  工具: mcp_github_create_repository")
        print("  参数: { name: 'test-repo', private: true }")
        print("  认证: Token 缺少 'repo' 权限")
        print()
        print("❌ 错误信息:")
        print("-" * 70)
        print("Status: 403")
        print("Message: Resource not accessible by integration")
        print()
        error_response = {
            "message": "Resource not accessible by integration",
            "documentation_url": "https://docs.github.com/rest/repos/repos#create-a-repository-for-the-authenticated-user"
        }
        print(json.dumps(error_response, indent=2, ensure_ascii=False))
        print("-" * 70)
        print()
        
        print("🔧 触发操作 B: 访问私有仓库")
        print("  工具: mcp_github_get_file_contents")
        print("  参数: {")
        print("    owner: 'private-org',")
        print("    repo: 'private-repo',")
        print("    path: 'README.md'")
        print("  }")
        print("  认证: 无权访问该私有仓库")
        print()
        print("❌ 错误信息:")
        print("-" * 70)
        print("Status: 403")
        print("Message: You don't have access to this resource")
        print("-" * 70)
        print()
        print("📊 错误分析:")
        print("  原因1: Token 权限范围不足")
        print("  原因2: 尝试访问无权限的私有资源")
        print("  原因3: 组织或仓库的安全策略限制")
        print()
        
    def simulate_404_not_found_with_auth_issue(self):
        """
        复现看似404实际是权限问题的错误
        
        场景: 私有资源返回404而非403以保护隐私
        """
        print("=" * 70)
        print("错误场景 3: 404 Not Found - 隐藏的权限问题")
        print("=" * 70)
        print()
        print("📋 错误描述:")
        print("  GitHub 对于未授权访问的私有资源，会返回 404 而非 403，")
        print("  以避免泄露私有仓库的存在信息。")
        print()
        print("🔧 触发操作:")
        print("  工具: mcp_github_get_file_contents")
        print("  参数: {")
        print("    owner: 'some-company',")
        print("    repo: 'secret-project',")
        print("    path: 'config.json'")
        print("  }")
        print("  认证: 未提供 Token 或 Token 无该仓库访问权")
        print()
        print("❌ 错误信息:")
        print("-" * 70)
        print("Status: 404")
        print("Message: Not Found")
        print()
        error_response = {
            "message": "Not Found",
            "documentation_url": "https://docs.github.com/rest/repos/contents#get-repository-content"
        }
        print(json.dumps(error_response, indent=2, ensure_ascii=False))
        print("-" * 70)
        print()
        print("⚠️  注意:")
        print("  此 404 错误可能意味着:")
        print("  • 资源确实不存在")
        print("  • 或者资源存在但你没有访问权限")
        print("  GitHub 不会明确告知是哪种情况")
        print()
        
    def simulate_rate_limit_error(self):
        """
        复现 Rate Limit 错误
        
        场景: 未认证用户的请求速率限制更严格
        """
        print("=" * 70)
        print("错误场景 4: 403 Rate Limit Exceeded - 速率限制")
        print("=" * 70)
        print()
        print("📋 错误描述:")
        print("  未认证用户每小时仅能发起 60 次请求，")
        print("  认证用户可以发起 5000 次请求。")
        print()
        print("🔧 触发条件:")
        print("  - 短时间内多次调用 GitHub API")
        print("  - 未提供认证 Token")
        print("  - 超过速率限制阈值")
        print()
        print("❌ 错误信息:")
        print("-" * 70)
        print("Status: 403")
        print("Message: API rate limit exceeded")
        print()
        error_response = {
            "message": "API rate limit exceeded for xxx.xxx.xxx.xxx. (But here's the good news: Authenticated requests get a higher rate limit. Check out the documentation for more details.)",
            "documentation_url": "https://docs.github.com/rest/overview/resources-in-the-rest-api#rate-limiting"
        }
        print(json.dumps(error_response, indent=2, ensure_ascii=False))
        print("-" * 70)
        print()
        print("📊 速率限制对比:")
        print("  未认证用户: 60 次/小时")
        print("  已认证用户: 5,000 次/小时")
        print("  企业账号: 15,000 次/小时")
        print()
        
    def show_token_permission_error(self):
        """
        展示 Token 权限范围不足的错误
        """
        print("=" * 70)
        print("错误场景 5: Token 权限范围(Scope)不足")
        print("=" * 70)
        print()
        print("📋 错误描述:")
        print("  Token 存在但缺少执行特定操作所需的权限范围。")
        print()
        
        # 示例1: 创建仓库需要 repo 权限
        print("🔧 示例 1: 创建仓库")
        print("  操作: mcp_github_create_repository")
        print("  需要权限: repo (完整仓库控制)")
        print("  当前权限: public_repo (仅公开仓库)")
        print()
        print("❌ 错误:")
        print("  Status: 403")
        print("  Message: Resource not accessible by integration")
        print("  说明: Token 缺少创建私有仓库的权限")
        print()
        
        # 示例2: 创建 Issue 需要特定权限
        print("🔧 示例 2: 创建 Issue")
        print("  操作: mcp_github_create_issue")
        print("  需要权限: repo 或 public_repo")
        print("  当前权限: read:org (仅组织读取)")
        print()
        print("❌ 错误:")
        print("  Status: 403")
        print("  Message: Resource not accessible by integration")
        print()
        
        # 权限列表
        print("📋 常用 Token 权限范围:")
        print("-" * 70)
        permissions = {
            "repo": "完整仓库访问(包括私有仓库)",
            "public_repo": "公开仓库访问",
            "repo:status": "提交状态访问",
            "repo_deployment": "部署访问",
            "read:org": "读取组织信息",
            "write:org": "管理组织",
            "admin:org": "完整组织管理",
            "workflow": "GitHub Actions 工作流",
            "delete_repo": "删除仓库权限"
        }
        for scope, desc in permissions.items():
            print(f"  • {scope:20s} - {desc}")
        print("-" * 70)
        print()
        
    def demonstrate_fallback_strategy(self):
        """
        演示权限不足时的降级策略
        """
        print("=" * 70)
        print("💡 权限不足时的降级策略")
        print("=" * 70)
        print()
        print("当遇到 GitHub 权限错误时，可以采用以下降级方案:")
        print()
        
        print("策略 1: 使用无需认证的工具")
        print("-" * 70)
        print("  原计划: mcp_github_get_file_contents (需要认证)")
        print("  降级为: mcp_fetch_fetch_markdown (无需认证)")
        print("  适用场景: 获取公开仓库的文件内容")
        print("  限制: 仅限公开资源，无法访问私有内容")
        print()
        
        print("策略 2: 缓存和本地存储")
        print("-" * 70)
        print("  方案: 一次性获取数据后本地缓存")
        print("  优点: 减少 API 调用次数，避免速率限制")
        print("  实现: 使用 JSON 文件或数据库存储")
        print()
        
        print("策略 3: 批量操作优化")
        print("-" * 70)
        print("  方案: 合并多个小请求为批量请求")
        print("  优点: 提高效率，节省配额")
        print("  示例: 使用 GraphQL API 替代多次 REST 调用")
        print()
        
        print("策略 4: 用户授权流程")
        print("-" * 70)
        print("  步骤:")
        print("    1. 检测到权限不足")
        print("    2. 提示用户配置 Token")
        print("    3. 验证 Token 权限范围")
        print("    4. 保存并使用 Token")
        print()
        
    def generate_error_summary(self):
        """
        生成错误汇总报告
        """
        print("\n")
        print("=" * 70)
        print("📊 GitHub 权限错误汇总")
        print("=" * 70)
        print()
        
        summary_table = [
            ("错误码", "错误类型", "常见原因", "解决方案"),
            ("-" * 8, "-" * 20, "-" * 30, "-" * 30),
            ("401", "Unauthorized", "未提供 Token", "配置 Personal Access Token"),
            ("403", "Forbidden", "Token 权限不足", "使用具有足够权限的 Token"),
            ("403", "Forbidden", "访问私有资源", "获取仓库访问权限"),
            ("403", "Rate Limit", "请求次数超限", "使用认证 Token 提高限额"),
            ("404", "Not Found", "资源不存在或无权访问", "检查资源是否存在及权限"),
            ("422", "Validation Failed", "参数验证失败", "检查请求参数格式"),
        ]
        
        for row in summary_table:
            print(f"  {row[0]:8s} | {row[1]:20s} | {row[2]:30s} | {row[3]:30s}")
        
        print()
        print("=" * 70)
        print()
        
    def run_all_demos(self):
        """运行所有错误演示"""
        print("\n")
        print("*" * 70)
        print("GitHub 权限不足错误复现演示")
        print(f"运行时间: {self.timestamp}")
        print("*" * 70)
        print()
        
        # 运行各种错误场景
        self.simulate_401_unauthorized()
        input("按回车继续下一个错误场景...")
        print("\n")
        
        self.simulate_403_forbidden()
        input("按回车继续下一个错误场景...")
        print("\n")
        
        self.simulate_404_not_found_with_auth_issue()
        input("按回车继续下一个错误场景...")
        print("\n")
        
        self.simulate_rate_limit_error()
        input("按回车继续下一个错误场景...")
        print("\n")
        
        self.show_token_permission_error()
        input("按回车继续查看降级策略...")
        print("\n")
        
        self.demonstrate_fallback_strategy()
        input("按回车查看错误汇总...")
        print("\n")
        
        self.generate_error_summary()
        
        # 最终总结
        print("=" * 70)
        print("✅ 演示完成")
        print("=" * 70)
        print()
        print("已复现的错误类型:")
        print("  ✓ 401 Unauthorized - 未授权访问")
        print("  ✓ 403 Forbidden - 权限不足")
        print("  ✓ 403 Rate Limit - 速率限制")
        print("  ✓ 404 Not Found - 隐藏的权限问题")
        print("  ✓ Token Scope 不足 - 权限范围错误")
        print()
        print("📚 下一步:")
        print("  1. 配置 GitHub Personal Access Token")
        print("  2. 确保 Token 具有所需的权限范围")
        print("  3. 在 IDE 中配置 GitHub 集成")
        print("  4. 重试失败的操作")
        print()


def quick_demo():
    """快速演示模式 - 不需要交互"""
    print("\n" + "=" * 70)
    print("🚀 快速演示模式 - GitHub 权限错误复现")
    print("=" * 70)
    print()
    
    print("❌ 错误 1: 401 Unauthorized")
    print("  场景: 调用 mcp_github_search_repositories 未提供 Token")
    print("  错误: Bad credentials")
    print()
    
    print("❌ 错误 2: 403 Forbidden")
    print("  场景: Token 权限不足")
    print("  错误: Resource not accessible by integration")
    print()
    
    print("❌ 错误 3: 403 Rate Limit")
    print("  场景: 未认证用户超过 60 次/小时限制")
    print("  错误: API rate limit exceeded")
    print()
    
    print("❌ 错误 4: 404 Not Found")
    print("  场景: 尝试访问私有仓库但无权限")
    print("  错误: Not Found (实际是权限问题)")
    print()
    
    print("💡 解决方案:")
    print("  → 配置 GitHub Personal Access Token")
    print("  → 确保 Token 包含必要权限: repo, public_repo, workflow")
    print("  → 在项目设置中配置 Token")
    print()


def generate_full_report():
    """生成完整的错误报告(非交互式)"""
    demo = GitHubAuthErrorDemo()
    
    print("\n")
    print("*" * 70)
    print("GitHub 权限不足错误完整复现报告")
    print(f"生成时间: {demo.timestamp}")
    print("*" * 70)
    print("\n")
    
    # 场景1: 401错误
    print("=" * 70)
    print("场景 1: 401 Unauthorized - 未授权访问")
    print("=" * 70)
    print()
    print("触发操作:")
    print("  工具: mcp_github_search_repositories")
    print("  参数: { query: 'python' }")
    print("  状态: ❌ 失败")
    print()
    print("错误响应:")
    print("  HTTP Status: 401")
    print("  Error: Bad credentials")
    print("  Message: Requires authentication")
    print()
    print("完整错误信息:")
    print(json.dumps({
        "message": "Bad credentials",
        "documentation_url": "https://docs.github.com/rest"
    }, indent=2, ensure_ascii=False))
    print("\n")
    
    # 场景2: 403错误 - 权限不足
    print("=" * 70)
    print("场景 2: 403 Forbidden - Token权限不足")
    print("=" * 70)
    print()
    print("触发操作:")
    print("  工具: mcp_github_create_repository")
    print("  参数: { name: 'test-repo', private: true }")
    print("  Token: 只有 public_repo 权限")
    print("  状态: ❌ 失败")
    print()
    print("错误响应:")
    print("  HTTP Status: 403")
    print("  Error: Resource not accessible by integration")
    print()
    print("完整错误信息:")
    print(json.dumps({
        "message": "Resource not accessible by integration",
        "documentation_url": "https://docs.github.com/rest/repos/repos#create-a-repository-for-the-authenticated-user"
    }, indent=2, ensure_ascii=False))
    print("\n")
    
    # 场景3: 403错误 - 速率限制
    print("=" * 70)
    print("场景 3: 403 Forbidden - API速率限制")
    print("=" * 70)
    print()
    print("触发条件:")
    print("  - 未认证状态")
    print("  - 1小时内调用超过60次")
    print("  状态: ❌ 失败")
    print()
    print("错误响应:")
    print("  HTTP Status: 403")
    print("  Error: API rate limit exceeded")
    print()
    print("完整错误信息:")
    print(json.dumps({
        "message": "API rate limit exceeded for xxx.xxx.xxx.xxx. (But here's the good news: Authenticated requests get a higher rate limit. Check out the documentation for more details.)",
        "documentation_url": "https://docs.github.com/rest/overview/resources-in-the-rest-api#rate-limiting"
    }, indent=2, ensure_ascii=False))
    print()
    print("速率限制详情:")
    print("  未认证: 60 请求/小时")
    print("  已认证: 5,000 请求/小时")
    print("\n")
    
    # 场景4: 404错误(实际是权限问题)
    print("=" * 70)
    print("场景 4: 404 Not Found - 隐藏的权限问题")
    print("=" * 70)
    print()
    print("触发操作:")
    print("  工具: mcp_github_get_file_contents")
    print("  仓库: private-org/secret-repo")
    print("  文件: config.json")
    print("  状态: ❌ 失败")
    print()
    print("错误响应:")
    print("  HTTP Status: 404")
    print("  Error: Not Found")
    print()
    print("⚠️  注意: 此404可能意味着:")
    print("  1. 资源真的不存在")
    print("  2. 或资源存在但你无权访问")
    print("  GitHub不会明确告知具体原因")
    print("\n")
    
    # 场景5: Token Scope不足
    print("=" * 70)
    print("场景 5: Token权限范围(Scope)不足")
    print("=" * 70)
    print()
    print("常见权限不足案例:")
    print()
    print("案例 A: 创建Issue")
    print("  需要: repo 或 public_repo")
    print("  当前: read:org")
    print("  结果: ❌ 403 Forbidden")
    print()
    print("案例 B: 创建仓库")
    print("  需要: repo (完整权限)")
    print("  当前: public_repo (仅公开)")
    print("  结果: ❌ 403 Forbidden (无法创建私有仓库)")
    print()
    print("案例 C: 管理工作流")
    print("  需要: workflow")
    print("  当前: repo (仅代码权限)")
    print("  结果: ❌ 403 Forbidden")
    print("\n")
    
    # 权限范围表
    print("=" * 70)
    print("GitHub Token 权限范围对照表")
    print("=" * 70)
    print()
    scopes = [
        ("repo", "完整仓库控制(包括私有)", "创建/修改/删除仓库"),
        ("public_repo", "公开仓库访问", "仅操作公开仓库"),
        ("workflow", "GitHub Actions控制", "管理工作流"),
        ("write:packages", "包发布权限", "发布到GitHub Packages"),
        ("delete_repo", "删除仓库", "删除仓库操作"),
        ("admin:org", "组织管理", "完整组织管理权限"),
        ("read:org", "读取组织", "查看组织信息"),
    ]
    
    print(f"{'权限范围':<20} {'说明':<25} {'典型用途'}")
    print("-" * 70)
    for scope, desc, usage in scopes:
        print(f"{scope:<20} {desc:<25} {usage}")
    print("\n")
    
    # 解决方案
    print("=" * 70)
    print("💡 解决方案汇总")
    print("=" * 70)
    print()
    print("方案 1: 配置Personal Access Token")
    print("  步骤:")
    print("    1. 访问 https://github.com/settings/tokens")
    print("    2. 点击 'Generate new token (classic)'")
    print("    3. 选择权限: repo, workflow, read:org")
    print("    4. 生成并复制Token")
    print("    5. 在IDE中配置Token")
    print()
    print("方案 2: 使用降级策略")
    print("  对于公开资源:")
    print("    - 使用 mcp_fetch_fetch_markdown (无需认证)")
    print("    - 使用 mcp_fetch_fetch_html")
    print("  对于私有资源:")
    print("    - 必须配置有效Token")
    print()
    print("方案 3: 优化API调用")
    print("  - 使用缓存减少重复请求")
    print("  - 批量操作替代多次单独调用")
    print("  - 使用GraphQL API(更高效)")
    print("\n")
    
    # 错误汇总表
    print("=" * 70)
    print("错误代码快速参考表")
    print("=" * 70)
    print()
    print(f"{'HTTP状态码':<12} {'错误类型':<25} {'常见原因':<30}")
    print("-" * 70)
    errors = [
        ("401", "Unauthorized", "未提供Token或Token无效"),
        ("403", "Forbidden", "Token权限不足"),
        ("403", "Rate Limit Exceeded", "API调用频率超限"),
        ("404", "Not Found", "资源不存在或无访问权限"),
        ("422", "Validation Failed", "请求参数格式错误"),
    ]
    for code, error_type, reason in errors:
        print(f"{code:<12} {error_type:<25} {reason:<30}")
    print("\n")
    
    # 总结
    print("=" * 70)
    print("✅ 报告生成完成")
    print("=" * 70)
    print()
    print("已复现的错误场景:")
    print("  ✓ 401 Unauthorized - 未提供认证")
    print("  ✓ 403 Forbidden - 权限不足")
    print("  ✓ 403 Rate Limit - 速率限制")
    print("  ✓ 404 Not Found - 权限隐藏")
    print("  ✓ Token Scope错误 - 权限范围不足")
    print()
    print("关键要点:")
    print("  • 大多数GitHub MCP工具需要认证")
    print("  • Token必须具有相应的权限范围(Scopes)")
    print("  • 未认证用户仅60次/小时请求限制")
    print("  • 404错误可能隐藏真实的权限问题")
    print("  • 使用fetch工具可作为降级方案")
    print()
    print("建议操作:")
    print("  1. 立即配置GitHub Personal Access Token")
    print("  2. 确保Token包含: repo, workflow, read:org权限")
    print("  3. 在项目中妥善保管Token(使用环境变量)")
    print("  4. 定期检查和更新Token权限")
    print()
    print("=" * 70)
    print()


def main():
    """主函数"""
    import sys
    
    # 检查是否有命令行参数
    if len(sys.argv) > 1:
        mode = sys.argv[1]
    else:
        print("\n选择运行模式:")
        print("1. 完整演示(交互式) - 详细展示所有错误场景")
        print("2. 快速演示 - 快速浏览所有错误类型")
        print("3. 生成完整报告 - 非交互式完整演示")
        print()
        mode = input("请选择 (1/2/3,直接回车默认为快速演示): ").strip() or "2"
    
    if mode == "1":
        demo = GitHubAuthErrorDemo()
        demo.run_all_demos()
    elif mode == "3":
        generate_full_report()
    else:
        quick_demo()
    
    print("\n✅ 演示完成!")


if __name__ == "__main__":
    main()
