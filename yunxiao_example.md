# Yunxiao 工具使用示例

## 概述
本文档展示了如何在 Qoder IDE 中使用 Yunxiao 工具来完成常见的开发任务。

## 常用 Yunxiao 工具示例

### 1. 获取组织信息
```json
{
  "tool": "mcp_yunxiao_get_current_organization_info",
  "parameters": {
    "random_string": "org-info-request"
  }
}
```

### 2. 列出代码仓库
```json
{
  "tool": "mcp_yunxiao_list_repositories",
  "parameters": {
    "organizationId": "your-organization-id"
  }
}
```

### 3. 创建工作项
```json
{
  "tool": "mcp_yunxiao_create_work_item",
  "parameters": {
    "organizationId": "your-organization-id",
    "spaceId": "your-project-id",
    "subject": "示例任务",
    "workitemTypeId": "task-type-id",
    "assignedTo": "assignee-user-id"
  }
}
```

### 4. 搜索工作项
```json
{
  "tool": "mcp_yunxiao_search_workitems",
  "parameters": {
    "organizationId": "your-organization-id",
    "category": "Task",
    "spaceId": "your-project-id",
    "assignedTo": "self"
  }
}
```

### 5. 创建流水线
```json
{
  "tool": "mcp_yunxiao_create_pipeline_from_description",
  "parameters": {
    "organizationId": "your-organization-id",
    "name": "示例流水线",
    "buildLanguage": "java",
    "buildTool": "maven"
  }
}
```

## 使用说明

1. 确保您已配置 Yunxiao 访问凭据
2. 将示例中的占位符替换为实际值
3. 在 Qoder IDE 中调用相应的工具