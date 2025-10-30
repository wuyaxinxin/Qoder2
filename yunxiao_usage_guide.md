# Yunxiao 工具使用指南

Yunxiao 是阿里云提供的一套研发协同工具，支持项目管理、代码托管、流水线构建等功能。本文档将介绍如何使用 Yunxiao 工具。

## 目录

1. [准备工作](#准备工作)
2. [认证配置](#认证配置)
3. [常用功能示例](#常用功能示例)
   - [获取组织信息](#获取组织信息)
   - [项目管理](#项目管理)
   - [工作项管理](#工作项管理)
   - [流水线管理](#流水线管理)
4. [错误处理](#错误处理)

## 准备工作

在使用 Yunxiao 工具之前，需要确保：

1. 已安装 Python 3.6+
2. 已安装必要的依赖包
3. 拥有有效的 Yunxiao 访问权限

## 认证配置

Yunxiao 工具需要通过认证令牌来访问 API。通常有以下几种方式配置认证：

1. 环境变量方式：
   ```bash
   export YUNXIAO_TOKEN="your_token_here"
   ```

2. 配置文件方式：
   ```python
   import os
   token = os.getenv("YUNXIAO_TOKEN")
   ```

## 常用功能示例

### 获取组织信息

```python
# 获取当前用户和组织信息
org_info = yunxiao.get_current_organization_info()
print(f"组织信息: {org_info}")
```

### 项目管理

#### 搜索项目
```python
# 搜索项目
projects = yunxiao.search_projects("示例项目")
print(f"搜索到的项目: {projects}")
```

#### 获取项目详情
```python
# 获取项目详情
project = yunxiao.get_project("project_id")
print(f"项目详情: {project}")
```

### 工作项管理

#### 搜索工作项
```python
# 搜索工作项
workitems = yunxiao.search_workitems("Req", "project_space_id")
print(f"工作项列表: {workitems}")
```

#### 创建工作项
```python
# 创建工作项
new_workitem = yunxiao.create_work_item(
    subject="新功能开发",
    workitem_type_id="type-req-001",
    assigned_to="user_id"
)
print(f"创建的工作项: {new_workitem}")
```

#### 更新工作项
```python
# 更新工作项
updated_workitem = yunxiao.update_work_item(
    work_item_id="workitem_id",
    update_fields={
        "status": "In Progress",
        "description": "正在开发中"
    }
)
print(f"更新后的工作项: {updated_workitem}")
```

### 流水线管理

#### 列出流水线
```python
# 列出流水线
pipelines = yunxiao.list_pipelines()
print(f"流水线列表: {pipelines}")
```

#### 获取流水线详情
```python
# 获取流水线详情
pipeline = yunxiao.get_pipeline("pipeline_id")
print(f"流水线详情: {pipeline}")
```

## 错误处理

在使用 Yunxiao 工具时，可能会遇到以下常见错误：

1. **认证失败 (401)**：
   ```
   Yunxiao API error (401): Authentication failed
   ```
   解决方案：检查认证令牌是否正确配置。

2. **权限不足 (403)**：
   ```
   Yunxiao API error (403): Permission denied
   ```
   解决方案：确认用户是否拥有相应资源的访问权限。

3. **资源不存在 (404)**：
   ```
   Yunxiao API error (404): Resource not found
   ```
   解决方案：检查请求的资源ID是否正确。

## 运行示例代码

要运行示例代码，请执行以下步骤：

1. 确保已正确配置认证信息
2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
3. 运行示例：
   ```bash
   python yunxiao_usage_example.py
   ```

## 注意事项

1. 所有 API 调用都应包含适当的错误处理机制
2. 敏感信息（如认证令牌）不应硬编码在代码中
3. 在生产环境中使用时，建议添加重试机制和日志记录