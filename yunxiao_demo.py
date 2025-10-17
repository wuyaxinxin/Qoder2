"""
云效（Yunxiao）API 使用示例

本示例展示了如何使用云效的各种工具功能。
在实际使用前，需要配置云效的访问凭证。

功能示例：
1. 获取当前用户信息
2. 获取组织信息
3. 查询项目列表
4. 管理工作项
5. 代码仓库操作
"""

class YunxiaoDemo:
    """云效 API 使用示例类"""
    
    def __init__(self, organization_id=None):
        """
        初始化云效示例
        
        Args:
            organization_id: 组织ID（可在云效管理后台获取）
        """
        self.organization_id = organization_id
        
    def example_user_info(self):
        """
        示例1: 获取当前用户信息
        
        对应工具: mcp_yunxiao_get_current_user
        用途: 获取当前登录用户的基本信息
        """
        print("=" * 50)
        print("示例1: 获取当前用户信息")
        print("=" * 50)
        print("工具名称: get_current_user")
        print("功能说明: 获取基于 token 的当前用户信息")
        print("使用场景: 验证身份、获取用户ID等")
        print()
        
    def example_organization_info(self):
        """
        示例2: 获取组织信息
        
        对应工具: mcp_yunxiao_get_current_organization_info
        用途: 获取当前用户所属的组织信息
        """
        print("=" * 50)
        print("示例2: 获取组织信息")
        print("=" * 50)
        print("工具名称: get_current_organization_info")
        print("功能说明: 获取当前用户和组织的基础信息")
        print("使用场景: 获取组织ID、组织名称等")
        print()
        
    def example_list_projects(self):
        """
        示例3: 查询项目列表
        
        对应工具: mcp_yunxiao_search_projects
        用途: 搜索云效项目列表
        """
        print("=" * 50)
        print("示例3: 查询项目列表")
        print("=" * 50)
        print("工具名称: search_projects")
        print("功能说明: 搜索和过滤项目列表")
        print("参数说明:")
        print("  - organizationId: 组织ID（必填）")
        print("  - page: 页码（默认1）")
        print("  - perPage: 每页数量（默认20）")
        print("  - name: 项目名称关键词")
        print("使用场景: 查看我参与的项目、管理的项目等")
        print()
        
    def example_search_workitems(self):
        """
        示例4: 搜索工作项
        
        对应工具: mcp_yunxiao_search_workitems
        用途: 查询需求、任务、缺陷等工作项
        """
        print("=" * 50)
        print("示例4: 搜索工作项")
        print("=" * 50)
        print("工具名称: search_workitems")
        print("功能说明: 搜索项目中的工作项")
        print("参数说明:")
        print("  - organizationId: 组织ID（必填）")
        print("  - spaceId: 项目ID（必填）")
        print("  - category: 工作项类型，如 Req/Task/Bug（必填）")
        print("  - assignedTo: 指派人ID")
        print("  - status: 状态ID")
        print("使用场景: 查询我的任务、跟踪Bug等")
        print()
        
    def example_list_repositories(self):
        """
        示例5: 获取代码仓库列表
        
        对应工具: mcp_yunxiao_list_repositories
        用途: 查询 Codeup 代码仓库
        """
        print("=" * 50)
        print("示例5: 获取代码仓库列表")
        print("=" * 50)
        print("工具名称: list_repositories")
        print("功能说明: 获取 CodeUp 代码仓库列表")
        print("参数说明:")
        print("  - organizationId: 组织ID（必填）")
        print("  - page: 页码（默认1）")
        print("  - perPage: 每页数量（默认20）")
        print("  - search: 搜索关键词")
        print("使用场景: 浏览和管理代码仓库")
        print()
        
    def example_list_pipelines(self):
        """
        示例6: 获取流水线列表
        
        对应工具: mcp_yunxiao_list_pipelines
        用途: 查询 Flow 流水线
        """
        print("=" * 50)
        print("示例6: 获取流水线列表")
        print("=" * 50)
        print("工具名称: list_pipelines")
        print("功能说明: 获取组织中的流水线列表")
        print("参数说明:")
        print("  - organizationId: 组织ID（必填）")
        print("  - page: 页码（默认1）")
        print("  - perPage: 每页数量（默认10，最大30）")
        print("  - pipelineName: 流水线名称过滤")
        print("  - statusList: 状态过滤（SUCCESS,RUNNING,FAIL等）")
        print("使用场景: 监控 CI/CD 流水线状态")
        print()
        
    def example_create_workitem(self):
        """
        示例7: 创建工作项
        
        对应工具: mcp_yunxiao_create_work_item
        用途: 创建新的需求、任务或缺陷
        """
        print("=" * 50)
        print("示例7: 创建工作项")
        print("=" * 50)
        print("工具名称: create_work_item")
        print("功能说明: 在项目中创建新的工作项")
        print("参数说明:")
        print("  - organizationId: 组织ID（必填）")
        print("  - spaceId: 项目ID（必填）")
        print("  - subject: 标题（必填）")
        print("  - workitemTypeId: 工作项类型ID（必填）")
        print("  - assignedTo: 指派人用户ID（必填）")
        print("  - description: 描述")
        print("  - sprint: 所属迭代ID")
        print("使用场景: 快速创建任务、提交Bug等")
        print()
        
    def run_all_examples(self):
        """运行所有示例说明"""
        print("\n")
        print("*" * 60)
        print("云效（Yunxiao）API 工具使用示例")
        print("*" * 60)
        print()
        
        self.example_user_info()
        self.example_organization_info()
        self.example_list_projects()
        self.example_search_workitems()
        self.example_list_repositories()
        self.example_list_pipelines()
        self.example_create_workitem()
        
        print("=" * 50)
        print("配置说明")
        print("=" * 50)
        print("使用云效 API 前需要配置访问凭证：")
        print("1. 登录云效管理后台")
        print("2. 获取个人访问令牌（Personal Access Token）")
        print("3. 在组织设置中获取组织ID")
        print("4. 配置环境变量或通过 IDE 设置凭证")
        print()
        print("常用云效功能模块：")
        print("  - 项目管理: 创建项目、管理工作项、迭代规划")
        print("  - 代码管理: 代码仓库、分支、提交、合并请求")
        print("  - 流水线: CI/CD 自动化构建和部署")
        print("  - 应用交付: 应用发布和环境管理")
        print("  - 制品仓库: 构建产物存储和管理")
        print()


def main():
    """主函数：运行示例"""
    demo = YunxiaoDemo()
    demo.run_all_examples()
    
    # 实际使用示例（需要有效的组织ID）
    print("=" * 50)
    print("实际调用示例代码")
    print("=" * 50)
    print("""
# 示例1: 获取当前用户信息
# 使用工具: mcp_yunxiao_get_current_user
# 参数: random_string (任意字符串)

# 示例2: 获取组织信息  
# 使用工具: mcp_yunxiao_get_current_organization_info
# 参数: random_string (任意字符串)

# 示例3: 查询项目列表
# 使用工具: mcp_yunxiao_search_projects
# 参数:
#   - organizationId: "your_org_id"
#   - page: 1
#   - perPage: 10

# 示例4: 搜索工作项
# 使用工具: mcp_yunxiao_search_workitems
# 参数:
#   - organizationId: "your_org_id"
#   - spaceId: "your_project_id"
#   - category: "Task"  # 或 "Req", "Bug"
#   - page: 1
#   - perPage: 20

# 示例5: 获取代码仓库列表
# 使用工具: mcp_yunxiao_list_repositories
# 参数:
#   - organizationId: "your_org_id"
#   - page: 1
#   - perPage: 10
    """)


def demo_actual_calls():
    """
    演示实际的工具调用流程
    注意: 需要配置有效的云效认证才能成功执行
    """
    print("\n" + "=" * 60)
    print("云效工具实际调用演示")
    print("=" * 60)
    
    # 示例1: 获取当前用户信息
    print("\n[示例1] 获取当前用户信息")
    print("-" * 40)
    print("调用: mcp_yunxiao_get_current_user")
    print("参数: random_string='demo'")
    print("返回: 用户ID、用户名、邮箱等信息")
    print("用途: 确认当前登录身份")
    
    # 示例2: 获取组织信息
    print("\n[示例2] 获取组织信息")
    print("-" * 40)
    print("调用: mcp_yunxiao_get_current_organization_info")
    print("参数: random_string='demo'")
    print("返回: 组织ID、组织名称等")
    print("用途: 获取后续操作所需的 organizationId")
    
    # 示例3: 查询项目列表（需要 organizationId）
    print("\n[示例3] 查询项目列表")
    print("-" * 40)
    print("调用: mcp_yunxiao_search_projects")
    print("参数:")
    print("  - organizationId: '<从示例2获取>'")
    print("  - page: 1")
    print("  - perPage: 10")
    print("  - scenarioFilter: 'participate'  # 我参与的项目")
    print("返回: 项目列表（包含项目ID、名称、状态等）")
    
    # 示例4: 查询代码仓库
    print("\n[示例4] 查询代码仓库")
    print("-" * 40)
    print("调用: mcp_yunxiao_list_repositories")
    print("参数:")
    print("  - organizationId: '<组织ID>'")
    print("  - page: 1")
    print("  - perPage: 10")
    print("  - search: 'Qoder'  # 搜索关键词")
    print("返回: 代码仓库列表")
    
    # 示例5: 查询流水线列表
    print("\n[示例5] 查询流水线")
    print("-" * 40)
    print("调用: mcp_yunxiao_list_pipelines")
    print("参数:")
    print("  - organizationId: '<组织ID>'")
    print("  - page: 1")
    print("  - perPage: 10")
    print("  - statusList: 'SUCCESS,RUNNING'")
    print("返回: 流水线列表及运行状态")
    
    # 示例6: 创建工作项（任务）
    print("\n[示例6] 创建工作项")
    print("-" * 40)
    print("调用: mcp_yunxiao_create_work_item")
    print("参数:")
    print("  - organizationId: '<组织ID>'")
    print("  - spaceId: '<项目ID>'")
    print("  - subject: '优化学生管理系统性能'")
    print("  - workitemTypeId: '<工作项类型ID>'")
    print("  - assignedTo: '<用户ID>'")
    print("  - description: '对查询功能进行性能优化'")
    print("返回: 新创建的工作项信息")
    
    print("\n" + "=" * 60)
    print("调用流程总结")
    print("=" * 60)
    print("""
1. 首先调用 get_current_user 和 get_current_organization_info
   获取必要的 organizationId 和 userId

2. 使用 organizationId 查询项目、代码仓库、流水线等资源

3. 根据需要创建或修改工作项、提交代码、运行流水线

4. 所有返回结果都是 JSON 格式，可以进一步处理和分析
    """)


if __name__ == "__main__":
    main()
    demo_actual_calls()
