#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
始终生效
云效 (Yunxiao) API 使用示例
演示如何使用云效工具进行项目管理、代码管理和流水线操作
"""

import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional


class YunxiaoDemo:
    """云效工具使用示例类"""
    
    def __init__(self, organization_id: str = None):
        """
        初始化云效示例
        
        Args:
            organization_id: 组织ID,可在云效管理后台获取
        """
        self.organization_id = organization_id
        self.demo_results = []
    
    def print_section(self, title: str):
        """打印章节标题"""
        print(f"\n{'='*60}")
        print(f"  {title}")
        print(f"{'='*60}\n")
    
    def add_result(self, operation: str, status: str, details: Dict = None):
        """记录操作结果"""
        result = {
            "timestamp": datetime.now().isoformat(),
            "operation": operation,
            "status": status,
            "details": details or {}
        }
        self.demo_results.append(result)
        return result
    
    # ==================== 组织管理示例 ====================
    
    def demo_organization_info(self):
        """示例1: 获取当前组织信息"""
        self.print_section("示例1: 获取组织信息")
        
        print("📋 功能说明:")
        print("   获取当前用户所属的组织信息,包括组织ID、名称、成员等")
        print("\n🔧 使用方法:")
        print("   工具: mcp_yunxiao_get_current_organization_info")
        print("   参数: 无需参数")
        print("\n💡 返回信息:")
        print("   - organizationId: 组织ID (后续操作必需)")
        print("   - name: 组织名称")
        print("   - userId: 当前用户ID")
        
        # 实际调用示例(需要在IDE中通过MCP工具调用)
        example_response = {
            "organizationId": "5f7a8b9c0d1e2f3g4h5i",
            "name": "示例科技公司",
            "userId": "user123456"
        }
        
        print(f"\n📊 示例返回数据:")
        print(json.dumps(example_response, indent=2, ensure_ascii=False))
        
        self.add_result(
            "获取组织信息",
            "演示完成",
            example_response
        )
    
    # ==================== 项目管理示例 ====================
    
    def demo_search_projects(self):
        """示例2: 搜索项目"""
        self.print_section("示例2: 搜索项目列表")
        
        print("📋 功能说明:")
        print("   搜索和筛选云效项目,支持多种过滤条件")
        print("\n🔧 使用方法:")
        print("   工具: mcp_yunxiao_search_projects")
        print("   必需参数:")
        print("   - organizationId: 组织ID")
        print("   可选参数:")
        print("   - name: 项目名称关键字")
        print("   - scenarioFilter: 'manage'(我管理的) | 'participate'(我参与的) | 'favorite'(我收藏的)")
        print("   - page: 页码 (默认1)")
        print("   - perPage: 每页数量 (默认20)")
        
        example_params = {
            "organizationId": "5f7a8b9c0d1e2f3g4h5i",
            "scenarioFilter": "participate",
            "page": 1,
            "perPage": 10
        }
        
        example_response = {
            "total": 15,
            "projects": [
                {
                    "id": "proj001",
                    "name": "学生管理系统",
                    "creator": "张三",
                    "gmtCreate": "2025-01-15T10:00:00Z",
                    "status": "NORMAL"
                },
                {
                    "id": "proj002",
                    "name": "课程管理平台",
                    "creator": "李四",
                    "gmtCreate": "2025-02-01T14:30:00Z",
                    "status": "NORMAL"
                }
            ]
        }
        
        print(f"\n📝 请求参数示例:")
        print(json.dumps(example_params, indent=2, ensure_ascii=False))
        print(f"\n📊 返回数据示例:")
        print(json.dumps(example_response, indent=2, ensure_ascii=False))
        
        self.add_result(
            "搜索项目",
            "演示完成",
            {"params": example_params, "response": example_response}
        )
    
    # ==================== 工作项管理示例 ====================
    
    def demo_create_workitem(self):
        """示例3: 创建工作项"""
        self.print_section("示例3: 创建工作项")
        
        print("📋 功能说明:")
        print("   在项目中创建需求、任务或缺陷工作项")
        print("\n🔧 使用方法:")
        print("   工具: mcp_yunxiao_create_work_item")
        print("   必需参数:")
        print("   - organizationId: 组织ID")
        print("   - spaceId: 项目ID")
        print("   - subject: 工作项标题")
        print("   - workitemTypeId: 工作项类型ID")
        print("   - assignedTo: 指派人用户ID")
        print("   可选参数:")
        print("   - description: 描述")
        print("   - sprint: 迭代ID")
        print("   - participants: 参与人列表")
        
        example_params = {
            "organizationId": "5f7a8b9c0d1e2f3g4h5i",
            "spaceId": "proj001",
            "subject": "优化学生信息查询性能",
            "workitemTypeId": "task_type_001",
            "assignedTo": "user123456",
            "description": "当前学生信息查询在数据量大时响应较慢,需要优化查询逻辑和添加缓存机制",
            "sprint": "sprint_2025_03"
        }
        
        example_response = {
            "workItemId": "workitem_12345",
            "subject": "优化学生信息查询性能",
            "status": "待处理",
            "assignedTo": "user123456",
            "gmtCreate": datetime.now().isoformat()
        }
        
        print(f"\n📝 创建参数示例:")
        print(json.dumps(example_params, indent=2, ensure_ascii=False))
        print(f"\n📊 返回数据示例:")
        print(json.dumps(example_response, indent=2, ensure_ascii=False))
        
        self.add_result(
            "创建工作项",
            "演示完成",
            {"params": example_params, "response": example_response}
        )
    
    def demo_search_workitems(self):
        """示例4: 搜索工作项"""
        self.print_section("示例4: 搜索工作项")
        
        print("📋 功能说明:")
        print("   搜索项目中的工作项,支持多种过滤条件")
        print("\n🔧 使用方法:")
        print("   工具: mcp_yunxiao_search_workitems")
        print("   必需参数:")
        print("   - organizationId: 组织ID")
        print("   - spaceId: 项目ID")
        print("   - category: 工作项类型 (Req/Task/Bug)")
        print("   可选参数:")
        print("   - assignedTo: 指派人 (可用'self'表示当前用户)")
        print("   - status: 状态ID")
        print("   - subject: 标题关键字")
        print("   - includeDetails: 是否包含详细描述 (建议设为true)")
        
        example_params = {
            "organizationId": "5f7a8b9c0d1e2f3g4h5i",
            "spaceId": "proj001",
            "category": "Task",
            "assignedTo": "self",
            "status": "100010",  # 进行中
            "includeDetails": True
        }
        
        example_response = {
            "total": 5,
            "workitems": [
                {
                    "workItemId": "workitem_12345",
                    "subject": "优化学生信息查询性能",
                    "status": "进行中",
                    "assignedTo": "张三",
                    "description": "当前学生信息查询在数据量大时响应较慢...",
                    "priority": "高",
                    "gmtCreate": "2025-03-01T10:00:00Z"
                }
            ]
        }
        
        print(f"\n📝 搜索参数示例:")
        print(json.dumps(example_params, indent=2, ensure_ascii=False))
        print(f"\n📊 返回数据示例:")
        print(json.dumps(example_response, indent=2, ensure_ascii=False))
        
        self.add_result(
            "搜索工作项",
            "演示完成",
            {"params": example_params, "response": example_response}
        )
    
    # ==================== 代码管理示例 ====================
    
    def demo_list_repositories(self):
        """示例5: 获取代码仓库列表"""
        self.print_section("示例5: 获取代码仓库列表")
        
        print("📋 功能说明:")
        print("   获取组织下的代码仓库列表")
        print("\n🔧 使用方法:")
        print("   工具: mcp_yunxiao_list_repositories")
        print("   必需参数:")
        print("   - organizationId: 组织ID")
        print("   可选参数:")
        print("   - page: 页码")
        print("   - perPage: 每页数量")
        print("   - search: 搜索关键字")
        
        example_params = {
            "organizationId": "5f7a8b9c0d1e2f3g4h5i",
            "page": 1,
            "perPage": 10,
            "search": "student"
        }
        
        example_response = {
            "total": 3,
            "repositories": [
                {
                    "id": "2835387",
                    "name": "student-management-system",
                    "path": "student-management-system",
                    "httpUrlToRepo": "https://codeup.example.com/org/student-management-system.git",
                    "lastActivityAt": "2025-03-10T15:30:00Z"
                }
            ]
        }
        
        print(f"\n📝 请求参数示例:")
        print(json.dumps(example_params, indent=2, ensure_ascii=False))
        print(f"\n📊 返回数据示例:")
        print(json.dumps(example_response, indent=2, ensure_ascii=False))
        
        self.add_result(
            "获取代码仓库列表",
            "演示完成",
            {"params": example_params, "response": example_response}
        )
    
    def demo_list_branches(self):
        """示例6: 获取分支列表"""
        self.print_section("示例6: 获取分支列表")
        
        print("📋 功能说明:")
        print("   获取代码仓库的分支列表")
        print("\n🔧 使用方法:")
        print("   工具: mcp_yunxiao_list_branches")
        print("   必需参数:")
        print("   - organizationId: 组织ID")
        print("   - repositoryId: 仓库ID")
        
        example_params = {
            "organizationId": "5f7a8b9c0d1e2f3g4h5i",
            "repositoryId": "2835387",
            "page": 1,
            "perPage": 20
        }
        
        example_response = {
            "total": 5,
            "branches": [
                {
                    "name": "master",
                    "commit": {
                        "id": "abc123def456",
                        "message": "feat: 添加学生信息导出功能",
                        "authoredDate": "2025-03-15T10:30:00Z"
                    },
                    "protected": True
                },
                {
                    "name": "develop",
                    "commit": {
                        "id": "def456ghi789",
                        "message": "fix: 修复成绩计算bug",
                        "authoredDate": "2025-03-14T16:20:00Z"
                    },
                    "protected": False
                }
            ]
        }
        
        print(f"\n📝 请求参数示例:")
        print(json.dumps(example_params, indent=2, ensure_ascii=False))
        print(f"\n📊 返回数据示例:")
        print(json.dumps(example_response, indent=2, ensure_ascii=False))
        
        self.add_result(
            "获取分支列表",
            "演示完成",
            {"params": example_params, "response": example_response}
        )
    
    # ==================== 流水线管理示例 ====================
    
    def demo_create_pipeline(self):
        """示例7: 创建流水线"""
        self.print_section("示例7: 创建流水线")
        
        print("📋 功能说明:")
        print("   根据项目信息自动创建CI/CD流水线")
        print("\n🔧 使用方法:")
        print("   工具: mcp_yunxiao_create_pipeline_from_description")
        print("   必需参数:")
        print("   - organizationId: 组织ID")
        print("   - name: 流水线名称")
        print("   - buildLanguage: 编程语言 (java/nodejs/python/go/dotnet)")
        print("   - buildTool: 构建工具 (maven/gradle/npm/yarn/pip/go/dotnet)")
        print("   可选参数:")
        print("   - repoUrl: 仓库地址")
        print("   - branch: 分支名")
        print("   - deployTarget: 部署目标 (vm/k8s/none)")
        
        example_params = {
            "organizationId": "5f7a8b9c0d1e2f3g4h5i",
            "name": "学生管理系统-自动化构建",
            "buildLanguage": "python",
            "buildTool": "pip",
            "repoUrl": "https://codeup.example.com/org/student-management-system.git",
            "branch": "master",
            "deployTarget": "none",
            "pythonVersion": "3.12"
        }
        
        example_response = {
            "pipelineId": "pipeline_67890",
            "name": "学生管理系统-自动化构建",
            "status": "CREATED",
            "webUrl": "https://yunxiao.example.com/pipelines/pipeline_67890"
        }
        
        print(f"\n📝 创建参数示例:")
        print(json.dumps(example_params, indent=2, ensure_ascii=False))
        print(f"\n📊 返回数据示例:")
        print(json.dumps(example_response, indent=2, ensure_ascii=False))
        
        self.add_result(
            "创建流水线",
            "演示完成",
            {"params": example_params, "response": example_response}
        )
    
    def demo_list_pipelines(self):
        """示例8: 获取流水线列表"""
        self.print_section("示例8: 获取流水线列表")
        
        print("📋 功能说明:")
        print("   获取组织下的流水线列表,支持时间筛选")
        print("\n🔧 使用方法:")
        print("   工具: mcp_yunxiao_smart_list_pipelines")
        print("   必需参数:")
        print("   - organizationId: 组织ID")
        print("   可选参数:")
        print("   - timeReference: 时间范围 (today/this week/last month)")
        print("   - pipelineName: 流水线名称")
        print("   - statusList: 状态列表 (SUCCESS,RUNNING,FAIL)")
        
        example_params = {
            "organizationId": "5f7a8b9c0d1e2f3g4h5i",
            "timeReference": "this week",
            "statusList": "SUCCESS,RUNNING",
            "page": 1,
            "perPage": 10
        }
        
        example_response = {
            "total": 8,
            "pipelines": [
                {
                    "pipelineId": "pipeline_67890",
                    "pipelineName": "学生管理系统-自动化构建",
                    "status": "SUCCESS",
                    "gmtCreate": "2025-03-10T09:00:00Z",
                    "gmtExecute": "2025-03-15T14:30:00Z"
                }
            ]
        }
        
        print(f"\n📝 请求参数示例:")
        print(json.dumps(example_params, indent=2, ensure_ascii=False))
        print(f"\n📊 返回数据示例:")
        print(json.dumps(example_response, indent=2, ensure_ascii=False))
        
        self.add_result(
            "获取流水线列表",
            "演示完成",
            {"params": example_params, "response": example_response}
        )
    
    def demo_run_pipeline(self):
        """示例9: 运行流水线"""
        self.print_section("示例9: 运行流水线")
        
        print("📋 功能说明:")
        print("   触发流水线执行")
        print("\n🔧 使用方法:")
        print("   工具: mcp_yunxiao_create_pipeline_run")
        print("   必需参数:")
        print("   - organizationId: 组织ID")
        print("   - pipelineId: 流水线ID")
        print("   可选参数:")
        print("   - branches: 分支列表")
        print("   - environmentVariables: 环境变量")
        
        example_params = {
            "organizationId": "5f7a8b9c0d1e2f3g4h5i",
            "pipelineId": "pipeline_67890",
            "branches": ["master"],
            "environmentVariables": {
                "ENV": "production",
                "BUILD_VERSION": "1.0.0"
            }
        }
        
        example_response = {
            "pipelineRunId": "run_11111",
            "status": "RUNNING",
            "startTime": datetime.now().isoformat()
        }
        
        print(f"\n📝 运行参数示例:")
        print(json.dumps(example_params, indent=2, ensure_ascii=False))
        print(f"\n📊 返回数据示例:")
        print(json.dumps(example_response, indent=2, ensure_ascii=False))
        
        self.add_result(
            "运行流水线",
            "演示完成",
            {"params": example_params, "response": example_response}
        )
    
    # ==================== 综合示例 ====================
    
    def demo_complete_workflow(self):
        """示例10: 完整工作流程"""
        self.print_section("示例10: 完整工作流程演示")
        
        print("📋 场景说明:")
        print("   演示一个完整的研发流程:")
        print("   1. 创建需求工作项")
        print("   2. 创建代码分支")
        print("   3. 提交代码")
        print("   4. 触发流水线构建")
        print("   5. 查看构建结果")
        
        workflow_steps = [
            {
                "step": 1,
                "action": "创建需求",
                "tool": "mcp_yunxiao_create_work_item",
                "params": {
                    "subject": "实现学生成绩统计功能",
                    "workitemTypeId": "req_type_001"
                }
            },
            {
                "step": 2,
                "action": "创建开发分支",
                "tool": "mcp_yunxiao_create_branch",
                "params": {
                    "branch": "feature/grade-statistics",
                    "ref": "master"
                }
            },
            {
                "step": 3,
                "action": "提交代码",
                "tool": "mcp_yunxiao_create_file",
                "params": {
                    "filePath": "grade_statistics.py",
                    "content": "# 成绩统计模块",
                    "branch": "feature/grade-statistics"
                }
            },
            {
                "step": 4,
                "action": "触发流水线",
                "tool": "mcp_yunxiao_create_pipeline_run",
                "params": {
                    "branches": ["feature/grade-statistics"]
                }
            },
            {
                "step": 5,
                "action": "查看构建日志",
                "tool": "mcp_yunxiao_get_pipeline_job_run_log",
                "params": {
                    "pipelineRunId": "run_12345",
                    "jobId": "job_001"
                }
            }
        ]
        
        print(f"\n🔄 工作流程步骤:")
        for step in workflow_steps:
            print(f"\n步骤 {step['step']}: {step['action']}")
            print(f"   工具: {step['tool']}")
            print(f"   参数: {json.dumps(step['params'], ensure_ascii=False)}")
        
        self.add_result(
            "完整工作流程",
            "演示完成",
            {"workflow": workflow_steps}
        )
    
    # ==================== 运行所有示例 ====================
    
    def run_all_demos(self):
        """运行所有示例"""
        print("\n" + "="*60)
        print("  云效 (Yunxiao) API 使用示例集")
        print("="*60)
        print("\n本示例演示了云效工具的主要功能使用方法")
        print("包括组织管理、项目管理、代码管理和流水线管理等\n")
        
        # 运行所有示例
        self.demo_organization_info()
        self.demo_search_projects()
        self.demo_create_workitem()
        self.demo_search_workitems()
        self.demo_list_repositories()
        self.demo_list_branches()
        self.demo_create_pipeline()
        self.demo_list_pipelines()
        self.demo_run_pipeline()
        self.demo_complete_workflow()
        
        # 生成总结报告
        self.generate_summary()
    
    def generate_summary(self):
        """生成示例总结报告"""
        self.print_section("示例执行总结")
        
        print(f"✅ 共执行 {len(self.demo_results)} 个示例")
        print(f"📅 执行时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        print("\n📊 示例列表:")
        for i, result in enumerate(self.demo_results, 1):
            print(f"   {i}. {result['operation']} - {result['status']}")
        
        print("\n💡 使用提示:")
        print("   1. 所有示例都需要先获取组织ID")
        print("   2. 实际使用时需要配置云效认证信息")
        print("   3. 可以在IDE中通过MCP工具直接调用")
        print("   4. 建议先在测试环境验证后再用于生产环境")
        
        print("\n📚 相关文档:")
        print("   - 云效使用指南: YUNXIAO_USAGE_GUIDE.md")
        print("   - 云效演示总结: YUNXIAO_DEMO_SUMMARY.md")
        
        # 保存结果到文件
        self.save_results()
    
    def save_results(self):
        """保存示例结果到JSON文件"""
        output_file = "yunxiao_demo_results.json"
        
        summary = {
            "timestamp": datetime.now().isoformat(),
            "total_demos": len(self.demo_results),
            "results": self.demo_results
        }
        
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(summary, f, indent=2, ensure_ascii=False)
            print(f"\n💾 示例结果已保存到: {output_file}")
        except Exception as e:
            print(f"\n⚠️  保存结果失败: {e}")


def main():
    """主函数"""
    print("始终生效\n")
    
    # 创建示例对象
    demo = YunxiaoDemo()
    
    # 运行所有示例
    demo.run_all_demos()
    
    print("\n" + "="*60)
    print("  演示完成!")
    print("="*60)
    print("\n提示: 这些示例展示了云效工具的使用方法")
    print("实际调用时需要:")
    print("  1. 在IDE中配置云效MCP工具")
    print("  2. 提供有效的组织ID和认证信息")
    print("  3. 通过工具面板或代码调用相应的MCP工具\n")


if __name__ == "__main__":
    main()
