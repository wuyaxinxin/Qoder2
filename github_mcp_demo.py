"""
GitHub MCP 工具使用示例

本示例展示了如何使用 GitHub 的各种 MCP 工具。
包括需要认证和无需认证的工具。

功能示例:
1. 搜索仓库
2. 获取仓库内容 
3. 获取文件内容
4. 创建 Issue
5. 创建 Pull Request
6. 搜索代码
7. 获取提交记录
"""

class GitHubMCPDemo:
    """GitHub MCP 工具使用示例类"""
    
    def __init__(self):
        """初始化示例"""
        self.examples = []
        
    def example_fetch_markdown(self):
        """
        示例1: 获取 GitHub 页面的 Markdown 内容（无需认证）
        
        工具: mcp_fetch_fetch_markdown
        优点: 无需认证即可访问公开仓库
        用途: 查看仓库 README、文档等
        """
        print("=" * 60)
        print("示例1: 获取 GitHub 页面内容（无需认证）")
        print("=" * 60)
        print("工具名称: mcp_fetch_fetch_markdown")
        print("功能: 获取任意公开 GitHub 页面的 Markdown 格式内容")
        print()
        print("调用示例:")
        print("  URL: https://github.com/python/cpython")
        print("  返回: 页面的 Markdown 格式内容")
        print()
        print("使用场景:")
        print("  ✓ 查看仓库 README")
        print("  ✓ 阅读项目文档")
        print("  ✓ 获取仓库基本信息")
        print("  ✓ 无需 GitHub 认证")
        print()
        
    def example_search_repositories(self):
        """
        示例2: 搜索 GitHub 仓库（需要认证）
        
        工具: mcp_github_search_repositories
        用途: 搜索符合条件的 GitHub 仓库
        """
        print("=" * 60)
        print("示例2: 搜索 GitHub 仓库（需要认证）")
        print("=" * 60)
        print("工具名称: mcp_github_search_repositories")
        print("功能: 根据关键词搜索 GitHub 仓库")
        print()
        print("调用参数:")
        print("  - query: 搜索关键词（必填）")
        print("  - perPage: 每页结果数（默认30，最大100）")
        print("  - page: 页码（默认1）")
        print()
        print("查询示例:")
        print("  query: 'student management system python'")
        print("  query: 'language:python stars:>1000'")
        print("  query: 'user:python'")
        print()
        print("使用场景:")
        print("  ✓ 寻找开源项目")
        print("  ✓ 技术选型调研")
        print("  ✓ 学习优秀代码")
        print()
        print("⚠️  注意: 需要 GitHub Personal Access Token")
        print()
        
    def example_get_file_contents(self):
        """
        示例3: 获取文件内容（需要认证）
        
        工具: mcp_github_get_file_contents
        用途: 获取仓库中特定文件的内容
        """
        print("=" * 60)
        print("示例3: 获取文件内容")
        print("=" * 60)
        print("工具名称: mcp_github_get_file_contents")
        print("功能: 读取仓库中的文件内容")
        print()
        print("调用参数:")
        print("  - owner: 仓库所有者")
        print("  - repo: 仓库名称")
        print("  - path: 文件路径")
        print("  - branch: 分支名（可选）")
        print()
        print("示例:")
        print("  owner: 'python'")
        print("  repo: 'cpython'")
        print("  path: 'README.rst'")
        print("  branch: 'main'")
        print()
        print("使用场景:")
        print("  ✓ 查看源代码")
        print("  ✓ 读取配置文件")
        print("  ✓ 分析项目结构")
        print()
        
    def example_create_issue(self):
        """
        示例4: 创建 Issue（需要认证）
        
        工具: mcp_github_create_issue
        用途: 在仓库中创建新的 Issue
        """
        print("=" * 60)
        print("示例4: 创建 Issue")
        print("=" * 60)
        print("工具名称: mcp_github_create_issue")
        print("功能: 创建 GitHub Issue 提交问题或建议")
        print()
        print("调用参数:")
        print("  - owner: 仓库所有者（必填）")
        print("  - repo: 仓库名称（必填）")
        print("  - title: Issue 标题（必填）")
        print("  - body: Issue 描述")
        print("  - labels: 标签列表")
        print("  - assignees: 指派人列表")
        print()
        print("示例:")
        print("  title: '优化查询性能'")
        print("  body: '当前查询速度较慢，建议添加索引'")
        print("  labels: ['enhancement', 'performance']")
        print()
        print("使用场景:")
        print("  ✓ 报告 Bug")
        print("  ✓ 提出功能建议")
        print("  ✓ 记录待办事项")
        print()
        
    def example_create_pull_request(self):
        """
        示例5: 创建 Pull Request（需要认证）
        
        工具: mcp_github_create_pull_request
        用途: 创建代码合并请求
        """
        print("=" * 60)
        print("示例5: 创建 Pull Request")
        print("=" * 60)
        print("工具名称: mcp_github_create_pull_request")
        print("功能: 创建 PR 请求代码合并")
        print()
        print("调用参数:")
        print("  - owner: 仓库所有者（必填）")
        print("  - repo: 仓库名称（必填）")
        print("  - title: PR 标题（必填）")
        print("  - head: 源分支（必填）")
        print("  - base: 目标分支（必填）")
        print("  - body: PR 描述")
        print("  - draft: 是否为草稿")
        print()
        print("示例:")
        print("  title: '添加数据导出功能'")
        print("  head: 'feature/export'")
        print("  base: 'main'")
        print("  body: '实现 CSV 和 JSON 格式数据导出'")
        print()
        print("使用场景:")
        print("  ✓ 提交代码更改")
        print("  ✓ 协作开发")
        print("  ✓ 代码审查")
        print()
        
    def example_search_code(self):
        """
        示例6: 搜索代码（需要认证）
        
        工具: mcp_github_search_code
        用途: 在 GitHub 中搜索代码片段
        """
        print("=" * 60)
        print("示例6: 搜索代码")
        print("=" * 60)
        print("工具名称: mcp_github_search_code")
        print("功能: 在 GitHub 仓库中搜索代码")
        print()
        print("调用参数:")
        print("  - q: 搜索查询（必填）")
        print("  - sort: 排序方式（indexed）")
        print("  - order: 排序顺序（asc/desc）")
        print("  - per_page: 每页结果数")
        print()
        print("查询语法:")
        print("  'def main in:file language:python'")
        print("  'class Student repo:user/repo'")
        print("  'import requests language:python'")
        print()
        print("使用场景:")
        print("  ✓ 查找代码示例")
        print("  ✓ 学习最佳实践")
        print("  ✓ 发现相似实现")
        print()
        
    def example_list_commits(self):
        """
        示例7: 获取提交记录（需要认证）
        
        工具: mcp_github_list_commits
        用途: 查看仓库的提交历史
        """
        print("=" * 60)
        print("示例7: 获取提交记录")
        print("=" * 60)
        print("工具名称: mcp_github_list_commits")
        print("功能: 查看代码提交历史")
        print()
        print("调用参数:")
        print("  - owner: 仓库所有者（必填）")
        print("  - repo: 仓库名称（必填）")
        print("  - sha: 分支名或 SHA")
        print("  - page: 页码")
        print("  - perPage: 每页数量")
        print()
        print("使用场景:")
        print("  ✓ 查看开发历史")
        print("  ✓ 追踪代码变更")
        print("  ✓ 了解项目进展")
        print()
        
    def example_fork_repository(self):
        """
        示例8: Fork 仓库（需要认证）
        
        工具: mcp_github_fork_repository
        用途: Fork 一个仓库到自己账号
        """
        print("=" * 60)
        print("示例8: Fork 仓库")
        print("=" * 60)
        print("工具名称: mcp_github_fork_repository")
        print("功能: 复制仓库到自己的账号")
        print()
        print("调用参数:")
        print("  - owner: 原仓库所有者（必填）")
        print("  - repo: 原仓库名称（必填）")
        print("  - organization: 目标组织（可选）")
        print()
        print("使用场景:")
        print("  ✓ 参与开源项目")
        print("  ✓ 创建项目分支")
        print("  ✓ 学习和实验")
        print()
        
    def run_all_examples(self):
        """运行所有示例说明"""
        print("\n")
        print("*" * 70)
        print("GitHub MCP 工具使用示例")
        print("*" * 70)
        print()
        
        self.example_fetch_markdown()
        self.example_search_repositories()
        self.example_get_file_contents()
        self.example_create_issue()
        self.example_create_pull_request()
        self.example_search_code()
        self.example_list_commits()
        self.example_fork_repository()
        
        print("=" * 60)
        print("GitHub 认证配置")
        print("=" * 60)
        print("使用需要认证的工具前，需要配置 GitHub Personal Access Token:")
        print()
        print("1. 登录 GitHub")
        print("2. 进入 Settings → Developer settings → Personal access tokens")
        print("3. 点击 'Generate new token (classic)'")
        print("4. 选择所需权限:")
        print("   - repo: 完整的仓库访问权限")
        print("   - public_repo: 公开仓库访问")
        print("   - read:org: 读取组织信息")
        print("5. 生成并保存 Token")
        print("6. 在 IDE 中配置 GitHub 插件")
        print()
        
        print("=" * 60)
        print("工具分类")
        print("=" * 60)
        print()
        print("✅ 无需认证的工具:")
        print("  - mcp_fetch_fetch_markdown")
        print("  - mcp_fetch_fetch_html")
        print("  - mcp_fetch_fetch_txt")
        print()
        print("🔐 需要认证的工具:")
        print("  - mcp_github_search_repositories")
        print("  - mcp_github_get_file_contents")
        print("  - mcp_github_create_issue")
        print("  - mcp_github_create_pull_request")
        print("  - mcp_github_search_code")
        print("  - mcp_github_list_commits")
        print("  - mcp_github_fork_repository")
        print("  - mcp_github_create_branch")
        print("  - 等更多工具...")
        print()
        
        print("=" * 60)
        print("实际调用成功示例")
        print("=" * 60)
        print()
        print("✅ 成功调用示例 1: 获取 Python 官方仓库页面")
        print("工具: mcp_fetch_fetch_markdown")
        print("URL: https://github.com/python/cpython")
        print("结果: 成功获取仓库页面内容，包含:")
        print("  - 仓库描述: The Python programming language")
        print("  - Stars: 69.4k")
        print("  - Forks: 33.1k")
        print("  - README 内容")
        print("  - 文件列表")
        print("  - 贡献者信息")
        print()
        print("⚠️  需要认证的工具返回 401 错误（正常）")
        print("配置 GitHub Token 后即可正常使用所有工具")
        print()


def demo_actual_usage():
    """演示实际的工具调用"""
    print("\n" + "=" * 60)
    print("实际工具调用演示")
    print("=" * 60)
    print()
    
    print("示例 1: 无需认证 - 获取仓库内容")
    print("-" * 40)
    print("调用: mcp_fetch_fetch_markdown")
    print("参数: { url: 'https://github.com/python/cpython' }")
    print("状态: ✅ 成功")
    print("返回: 完整的仓库页面 Markdown 内容")
    print()
    
    print("示例 2: 需要认证 - 搜索仓库")
    print("-" * 40)
    print("调用: mcp_github_search_repositories")
    print("参数: {")
    print("  query: 'student management system python',")
    print("  perPage: 5")
    print("}")
    print("状态: ⚠️  需要配置 GitHub Token")
    print("错误: Authentication Failed: Bad credentials")
    print()
    
    print("=" * 60)
    print("推荐使用流程")
    print("=" * 60)
    print()
    print("1. 对于公开仓库的基本信息查看:")
    print("   使用 mcp_fetch_fetch_markdown（无需认证）")
    print()
    print("2. 对于复杂查询和操作:")
    print("   配置 Token 后使用 GitHub 专用工具")
    print()
    print("3. 常见工作流:")
    print("   a) 搜索仓库 → mcp_github_search_repositories")
    print("   b) 查看代码 → mcp_github_get_file_contents")
    print("   c) Fork 项目 → mcp_github_fork_repository")
    print("   d) 创建分支 → mcp_github_create_branch")
    print("   e) 提交 PR → mcp_github_create_pull_request")
    print()


def main():
    """主函数: 运行示例"""
    demo = GitHubMCPDemo()
    demo.run_all_examples()
    demo_actual_usage()
    
    print("=" * 60)
    print("总结")
    print("=" * 60)
    print()
    print("✅ 已演示 8 个 GitHub MCP 工具的使用方法")
    print("✅ 成功调用无需认证的工具（fetch_markdown）")
    print("✅ 说明了需要认证工具的配置方法")
    print()
    print("📚 相关文档:")
    print("  - GitHub API: https://docs.github.com/rest")
    print("  - Personal Access Tokens: https://github.com/settings/tokens")
    print()
    print("🚀 下一步:")
    print("  1. 配置 GitHub Personal Access Token")
    print("  2. 尝试创建 Issue 或 PR")
    print("  3. 搜索感兴趣的开源项目")
    print()


if __name__ == "__main__":
    main()
