#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Yunxiao 工具使用示例

本示例展示了如何使用 Yunxiao 工具进行项目管理、工作项操作和流水线管理等操作。
注意：实际使用时需要有效的认证令牌。
"""

import json
from typing import Dict, List, Any

# 模拟 Yunxiao 工具的使用
class YunxiaoExample:
    def __init__(self):
        # 模拟组织ID和项目ID
        self.organization_id = "org-12345"
        self.project_id = "proj-67890"
        self.user_id = "user-001"
    
    def get_current_organization_info(self) -> Dict[str, Any]:
        """
        获取当前用户和组织信息
        
        Returns:
            Dict: 包含组织信息的字典
        """
        print("获取当前组织信息...")
        # 模拟 API 调用
        return {
            "organizationId": self.organization_id,
            "userId": self.user_id,
            "userName": "test_user",
            "organizationName": "Test Organization"
        }
    
    def search_projects(self, name: str = None) -> List[Dict[str, Any]]:
        """
        搜索项目
        
        Args:
            name (str, optional): 项目名称搜索关键字
            
        Returns:
            List[Dict]: 项目列表
        """
        print(f"搜索项目，关键字: {name}")
        # 模拟 API 调用
        return [
            {
                "id": self.project_id,
                "name": "示例项目",
                "description": "这是一个示例项目",
                "status": "NORMAL",
                "creator": self.user_id
            }
        ]
    
    def get_project(self, project_id: str) -> Dict[str, Any]:
        """
        获取项目信息
        
        Args:
            project_id (str): 项目ID
            
        Returns:
            Dict: 项目信息
        """
        print(f"获取项目信息，项目ID: {project_id}")
        # 模拟 API 调用
        return {
            "id": project_id,
            "name": "示例项目",
            "description": "这是一个示例项目",
            "status": "NORMAL",
            "creator": self.user_id,
            "organizationId": self.organization_id
        }
    
    def search_workitems(self, category: str, space_id: str) -> List[Dict[str, Any]]:
        """
        搜索工作项
        
        Args:
            category (str): 工作项类型 (Req, Task, Bug)
            space_id (str): 项目空间ID
            
        Returns:
            List[Dict]: 工作项列表
        """
        print(f"搜索工作项，类型: {category}, 项目空间ID: {space_id}")
        # 模拟 API 调用
        return [
            {
                "workItemId": "wi-001",
                "subject": "示例需求",
                "description": "这是一个示例需求",
                "status": "Pending Confirmation",
                "assignedTo": self.user_id,
                "category": category
            },
            {
                "workItemId": "wi-002",
                "subject": "示例任务",
                "description": "这是一个示例任务",
                "status": "In Progress",
                "assignedTo": self.user_id,
                "category": category
            }
        ]
    
    def create_work_item(self, subject: str, workitem_type_id: str, assigned_to: str) -> Dict[str, Any]:
        """
        创建工作项
        
        Args:
            subject (str): 工作项标题
            workitem_type_id (str): 工作项类型ID
            assigned_to (str): 指派给
            
        Returns:
            Dict: 创建的工作项信息
        """
        print(f"创建工作项: {subject}")
        # 模拟 API 调用
        return {
            "workItemId": "wi-003",
            "subject": subject,
            "description": "",
            "status": "Pending Confirmation",
            "assignedTo": assigned_to,
            "workitemTypeId": workitem_type_id,
            "spaceId": self.project_id
        }
    
    def update_work_item(self, work_item_id: str, update_fields: Dict[str, Any]) -> Dict[str, Any]:
        """
        更新工作项
        
        Args:
            work_item_id (str): 工作项ID
            update_fields (Dict): 要更新的字段
            
        Returns:
            Dict: 更新后的工作项信息
        """
        print(f"更新工作项: {work_item_id}")
        # 模拟 API 调用
        return {
            "workItemId": work_item_id,
            "updatedFields": update_fields
        }
    
    def list_pipelines(self) -> List[Dict[str, Any]]:
        """
        列出流水线
        
        Returns:
            List[Dict]: 流水线列表
        """
        print("列出流水线...")
        # 模拟 API 调用
        return [
            {
                "pipelineId": "pl-001",
                "name": "构建流水线",
                "status": "SUCCESS",
                "organizationId": self.organization_id
            }
        ]
    
    def get_pipeline(self, pipeline_id: str) -> Dict[str, Any]:
        """
        获取流水线详情
        
        Args:
            pipeline_id (str): 流水线ID
            
        Returns:
            Dict: 流水线详情
        """
        print(f"获取流水线详情，流水线ID: {pipeline_id}")
        # 模拟 API 调用
        return {
            "pipelineId": pipeline_id,
            "name": "构建流水线",
            "description": "用于构建项目的流水线",
            "status": "SUCCESS",
            "organizationId": self.organization_id,
            "stages": [
                {
                    "name": "构建阶段",
                    "jobs": ["编译", "测试"]
                }
            ]
        }

def main():
    """主函数，演示 Yunxiao 工具的使用"""
    print("=== Yunxiao 工具使用示例 ===\n")
    
    # 创建示例对象
    yunxiao = YunxiaoExample()
    
    # 1. 获取当前组织信息
    org_info = yunxiao.get_current_organization_info()
    print(f"组织信息: {json.dumps(org_info, ensure_ascii=False, indent=2)}\n")
    
    # 2. 搜索项目
    projects = yunxiao.search_projects("示例")
    print(f"搜索到的项目: {json.dumps(projects, ensure_ascii=False, indent=2)}\n")
    
    # 3. 获取项目详情
    if projects:
        project = yunxiao.get_project(projects[0]["id"])
        print(f"项目详情: {json.dumps(project, ensure_ascii=False, indent=2)}\n")
    
    # 4. 搜索工作项
    workitems = yunxiao.search_workitems("Req", project["id"])
    print(f"搜索到的工作项: {json.dumps(workitems, ensure_ascii=False, indent=2)}\n")
    
    # 5. 创建新的工作项
    new_workitem = yunxiao.create_work_item(
        subject="新功能开发",
        workitem_type_id="type-req-001",
        assigned_to=org_info["userId"]
    )
    print(f"创建的工作项: {json.dumps(new_workitem, ensure_ascii=False, indent=2)}\n")
    
    # 6. 更新工作项
    updated_workitem = yunxiao.update_work_item(
        work_item_id=new_workitem["workItemId"],
        update_fields={
            "status": "In Progress",
            "description": "正在开发新功能"
        }
    )
    print(f"更新后的工作项: {json.dumps(updated_workitem, ensure_ascii=False, indent=2)}\n")
    
    # 7. 列出流水线
    pipelines = yunxiao.list_pipelines()
    print(f"流水线列表: {json.dumps(pipelines, ensure_ascii=False, indent=2)}\n")
    
    # 8. 获取流水线详情
    if pipelines:
        pipeline = yunxiao.get_pipeline(pipelines[0]["pipelineId"])
        print(f"流水线详情: {json.dumps(pipeline, ensure_ascii=False, indent=2)}\n")
    
    print("=== 示例结束 ===")

if __name__ == "__main__":
    main()