#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
云效 API 使用示例
演示如何通过 MCP 工具调用云效的各种 API
"""

def demo_organization_info():
    """
    示例1: 获取当前组织信息
    这是最基础的云效 API 调用，用于获取当前用户所属的组织信息
    """
    print("=" * 60)
    print("示例1: 获取当前组织信息")
    print("=" * 60)
    print("工具名称: mcp_yunxiao_get_current_organization_info")
    print("说明: 获取基于 token 的当前用户和组织基本信息")
    print("\n调用方式:")
    print("""
    使用 Qoder IDE 的工具调用功能:
    mcp_yunxiao_get_current_organization_info(random_string="demo")
    
    返回信息包括:
    - 组织ID (organizationId)
    - 组织名称
    - 用户ID (userId)
    - 用户名称
    等基本信息
    """)
    print()


def demo_list_repositories():
    """
    示例2: 获取代码仓库列表
    演示如何获取组织下的所有代码仓库
    """
    print("=" * 60)
    print("示例2: 获取代码仓库列表")
    print("=" * 60)
    print("工具名称: mcp_yunxiao_list_repositories")
    print("说明: 获取组织下的所有 Codeup 代码仓库")
    print("\n调用方式:")
    print("""
    参数:
    - organizationId: 组织ID (必填)
    - page: 页码，默认1
    - perPage: 每页数量，默认20
    - search: 搜索关键词 (可选)
    - orderBy: 排序字段，如 'created_at', 'name' 等
    - sort: 排序方式，'asc' 或 'desc'
    
    示例:
    mcp_yunxiao_list_repositories(
        organizationId="your_org_id",
        page=1,
        perPage=20,
        search="project-name"
    )
    """)
    print()


def demo_search_workitems():
    """
    示例3: 搜索工作项
    演示如何搜索项目中的需求、任务、缺陷等工作项
    """
    print("=" * 60)
    print("示例3: 搜索工作项")
    print("=" * 60)
    print("工具名称: mcp_yunxiao_search_workitems")
    print("说明: 搜索项目中的工作项（需求/任务/缺陷等）")
    print("\n调用方式:")
    print("""
    参数:
    - organizationId: 组织ID (必填)
    - spaceId: 项目ID (必填)
    - category: 工作项类型，如 'Req', 'Task', 'Bug' (必填)
    - assignedTo: 指派人ID，可用 'self' 表示当前用户
    - status: 状态ID
    - subject: 标题关键词
    - createdAfter: 创建开始时间 (YYYY-MM-DD)
    - createdBefore: 创建结束时间 (YYYY-MM-DD)
    
    示例:
    mcp_yunxiao_search_workitems(
        organizationId="your_org_id",
        spaceId="project_id",
        category="Task",
        assignedTo="self",
        status="100010"  # 进行中
    )
    """)
    print()


def demo_list_pipelines():
    """
    示例4: 获取流水线列表
    演示如何获取组织下的所有流水线
    """
    print("=" * 60)
    print("示例4: 获取流水线列表")
    print("=" * 60)
    print("工具名称: mcp_yunxiao_list_pipelines")
    print("说明: 获取组织下的所有 CI/CD 流水线")
    print("\n调用方式:")
    print("""
    参数:
    - organizationId: 组织ID (必填)
    - page: 页码，默认1
    - perPage: 每页数量，默认10，最大30
    - pipelineName: 流水线名称过滤
    - statusList: 状态列表，如 'SUCCESS,RUNNING,FAIL'
    - createStartTime: 创建开始时间 (毫秒时间戳)
    - createEndTime: 创建结束时间 (毫秒时间戳)
    
    示例:
    mcp_yunxiao_list_pipelines(
        organizationId="your_org_id",
        page=1,
        perPage=10,
        statusList="SUCCESS,RUNNING"
    )
    """)
    print()


def demo_create_pipeline():
    """
    示例5: 创建流水线
    演示如何根据描述自动创建流水线
    """
    print("=" * 60)
    print("示例5: 创建流水线")
    print("=" * 60)
    print("工具名称: mcp_yunxiao_create_pipeline_from_description")
    print("说明: 根据项目信息自动创建 CI/CD 流水线")
    print("\n调用方式:")
    print("""
    参数:
    - organizationId: 组织ID (必填)
    - name: 流水线名称 (必填)
    - buildLanguage: 编程语言，如 'java', 'nodejs', 'python' (必填)
    - buildTool: 构建工具，如 'maven', 'gradle', 'npm' (必填)
    - repoUrl: 代码仓库URL
    - branch: 分支名称
    - deployTarget: 部署目标，'vm', 'k8s', 'none'
    
    示例:
    mcp_yunxiao_create_pipeline_from_description(
        organizationId="your_org_id",
        name="My Java Pipeline",
        buildLanguage="java",
        buildTool="maven",
        branch="main",
        deployTarget="none"
    )
    """)
    print()


def demo_get_file_contents():
    """
    示例6: 获取代码文件内容
    演示如何从 Codeup 仓库读取文件内容
    """
    print("=" * 60)
    print("示例6: 获取代码文件内容")
    print("=" * 60)
    print("工具名称: mcp_yunxiao_get_file_blobs")
    print("说明: 从代码仓库获取文件内容")
    print("\n调用方式:")
    print("""
    参数:
    - organizationId: 组织ID (必填)
    - repositoryId: 仓库ID (必填)
    - filePath: 文件路径，需要 URL 编码 (必填)
    - ref: 分支名称、标签或 commit SHA (必填)
    
    示例:
    mcp_yunxiao_get_file_blobs(
        organizationId="your_org_id",
        repositoryId="repo_id",
        filePath="/src/main/java/Main.java",
        ref="master"
    )
    """)
    print()


def print_usage_tips():
    """
    打印使用提示
    """
    print("\n" + "=" * 60)
    print("使用提示")
    print("=" * 60)
    print("""
1. 认证配置:
   - 云效 API 需要配置访问令牌
   - 请确保已在系统中配置了有效的认证信息

2. 组织ID获取:
   - 可以通过 get_current_organization_info 获取当前组织ID
   - 也可以在云效控制台的组织设置中查看

3. 常用工作流:
   a) 代码管理: 
      list_repositories → get_file_blobs → create_file
   
   b) 项目管理:
      search_projects → search_workitems → create_work_item
   
   c) 流水线管理:
      list_pipelines → create_pipeline → create_pipeline_run
   
   d) 部署管理:
      list_applications → create_change_order

4. 更多工具:
   - 支持 100+ 云效 API 工具
   - 涵盖代码、项目、流水线、部署等全流程
   - 详细文档请参考 yunxiao_usage_guide.md
    """)
    print("=" * 60)


def main():
    """
    主函数：展示所有示例
    """
    print("\n")
    print("*" * 60)
    print(" " * 15 + "云效 API 使用示例")
    print("*" * 60)
    print()
    
    # 展示各个示例
    demo_organization_info()
    demo_list_repositories()
    demo_search_workitems()
    demo_list_pipelines()
    demo_create_pipeline()
    demo_get_file_contents()
    
    # 打印使用提示
    print_usage_tips()
    
    print("\n✅ 示例展示完成！")
    print("💡 在 Qoder IDE 中，你可以直接通过自然语言调用这些工具")
    print("   例如: '帮我获取组织信息' 或 '创建一个 Java 流水线'\n")


if __name__ == "__main__":
    main()
