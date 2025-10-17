# 云效（Yunxiao）工具使用指南

## 📋 概述

本指南展示了如何使用云效平台的各种工具功能，包括项目管理、代码管理、流水线等核心功能。

## 🔧 前置准备

### 认证配置
使用云效工具前需要配置访问凭证：

1. **登录云效管理后台** - https://devops.aliyun.com/
2. **获取个人访问令牌（Personal Access Token）**
   - 进入个人设置 → 访问令牌
   - 创建新令牌并保存
3. **获取组织ID**
   - 进入组织设置 → 基本信息
   - 复制组织ID
4. **配置凭证**
   - 在 IDE 中配置云效插件
   - 或设置环境变量

---

## 🎯 实际使用示例

### 示例1: 获取当前用户信息

**工具名称**: `mcp_yunxiao_get_current_user`

**用途**: 验证身份、获取用户ID

**调用参数**:
```json
{
  "random_string": "demo"
}
```

**返回示例**:
```json
{
  "id": "user123",
  "name": "张三",
  "email": "zhangsan@example.com",
  "accountId": "account456"
}
```

**使用场景**:
- 确认当前登录用户
- 获取用户ID用于后续操作
- 验证令牌是否有效

---

### 示例2: 获取组织信息

**工具名称**: `mcp_yunxiao_get_current_organization_info`

**用途**: 获取组织ID和基本信息

**调用参数**:
```json
{
  "random_string": "demo"
}
```

**返回示例**:
```json
{
  "organizationId": "org789",
  "organizationName": "示例公司",
  "userId": "user123"
}
```

**使用场景**:
- 获取后续操作必需的 organizationId
- 确认当前所属组织

---

### 示例3: 查询项目列表

**工具名称**: `mcp_yunxiao_search_projects`

**用途**: 搜索和筛选云效项目

**调用参数**:
```json
{
  "organizationId": "org789",
  "page": 1,
  "perPage": 10,
  "scenarioFilter": "participate"
}
```

**scenarioFilter 选项**:
- `participate` - 我参与的项目
- `manage` - 我管理的项目
- `favorite` - 我收藏的项目

**返回示例**:
```json
{
  "result": [
    {
      "id": "project001",
      "name": "学生管理系统",
      "identifier": "student-sys",
      "status": "ACTIVE",
      "creator": "user123"
    }
  ],
  "totalCount": 25,
  "page": 1
}
```

**使用场景**:
- 查看我参与的所有项目
- 获取项目ID用于工作项查询
- 项目管理和统计

---

### 示例4: 搜索工作项

**工具名称**: `mcp_yunxiao_search_workitems`

**用途**: 查询需求、任务、缺陷等工作项

**调用参数**:
```json
{
  "organizationId": "org789",
  "spaceId": "project001",
  "category": "Task",
  "assignedTo": "self",
  "page": 1,
  "perPage": 20
}
```

**category 类型**:
- `Req` - 需求
- `Task` - 任务
- `Bug` - 缺陷

**返回示例**:
```json
{
  "result": [
    {
      "id": "workitem001",
      "subject": "优化查询性能",
      "category": "Task",
      "status": "进行中",
      "assignedTo": "user123",
      "sprint": "迭代1"
    }
  ],
  "totalCount": 15
}
```

**使用场景**:
- 查看我的任务列表
- 跟踪Bug处理进度
- 统计需求完成情况

---

### 示例5: 获取代码仓库列表

**工具名称**: `mcp_yunxiao_list_repositories`

**用途**: 查询Codeup代码仓库

**调用参数**:
```json
{
  "organizationId": "org789",
  "page": 1,
  "perPage": 10,
  "search": "student"
}
```

**返回示例**:
```json
{
  "result": [
    {
      "id": "repo001",
      "name": "student-management",
      "path": "org789/student-management",
      "httpUrl": "https://codeup.aliyun.com/org789/student-management.git",
      "defaultBranch": "master"
    }
  ]
}
```

**使用场景**:
- 浏览组织的代码仓库
- 获取仓库地址进行克隆
- 管理代码权限

---

### 示例6: 查询流水线列表

**工具名称**: `mcp_yunxiao_list_pipelines`

**用途**: 查询CI/CD流水线及状态

**调用参数**:
```json
{
  "organizationId": "org789",
  "page": 1,
  "perPage": 10,
  "statusList": "SUCCESS,RUNNING,FAIL"
}
```

**statusList 选项**:
- `SUCCESS` - 成功
- `RUNNING` - 运行中
- `FAIL` - 失败
- `CANCELED` - 已取消
- `WAITING` - 等待中

**返回示例**:
```json
{
  "result": [
    {
      "pipelineId": "pipeline001",
      "name": "学生系统部署",
      "status": "SUCCESS",
      "createTime": "2025-10-16T10:00:00Z",
      "creator": "user123"
    }
  ]
}
```

**使用场景**:
- 监控构建状态
- 查看部署历史
- 分析失败原因

---

### 示例7: 创建工作项

**工具名称**: `mcp_yunxiao_create_work_item`

**用途**: 创建新的任务、需求或缺陷

**调用参数**:
```json
{
  "organizationId": "org789",
  "spaceId": "project001",
  "subject": "优化学生管理系统查询性能",
  "workitemTypeId": "taskType001",
  "assignedTo": "user123",
  "description": "对学生信息查询功能进行性能优化，目标响应时间小于100ms",
  "sprint": "sprint001"
}
```

**返回示例**:
```json
{
  "workItemId": "workitem002",
  "subject": "优化学生管理系统查询性能",
  "identifier": "TASK-123",
  "status": "待处理",
  "createdAt": "2025-10-16T11:00:00Z"
}
```

**使用场景**:
- 快速创建开发任务
- 提交Bug报告
- 记录需求

---

### 示例8: 运行流水线

**工具名称**: `mcp_yunxiao_create_pipeline_run`

**用途**: 触发流水线执行

**调用参数**:
```json
{
  "organizationId": "org789",
  "pipelineId": "pipeline001",
  "branchMode": false,
  "branches": ["master"]
}
```

**返回示例**:
```json
{
  "pipelineRunId": "run001",
  "status": "RUNNING",
  "startTime": "2025-10-16T12:00:00Z"
}
```

**使用场景**:
- 手动触发部署
- 执行自动化测试
- 构建发布版本

---

## 📊 常见使用流程

### 流程1: 查看我的待办任务

```plaintext
1. 调用 get_current_user 获取用户信息
2. 调用 get_current_organization_info 获取组织ID
3. 调用 search_projects 获取我参与的项目
4. 对每个项目调用 search_workitems
   - category: "Task"
   - assignedTo: "self"
   - status: 过滤进行中的状态
```

### 流程2: 创建并跟踪Bug

```plaintext
1. 获取组织ID和项目ID
2. 调用 create_work_item 创建Bug
   - category: "Bug"
   - 填写详细描述和重现步骤
3. 定期调用 get_work_item 查看处理进度
4. Bug修复后更新状态
```

### 流程3: 监控代码部署

```plaintext
1. 调用 list_repositories 找到目标仓库
2. 调用 list_pipelines 查看相关流水线
3. 调用 create_pipeline_run 触发部署
4. 轮询 get_pipeline_run 监控执行状态
5. 查看 get_pipeline_job_run_log 分析日志
```

---

## 💡 最佳实践

### 1. 错误处理
- 始终检查返回状态码
- 处理认证失败（401错误）
- 实现重试机制

### 2. 性能优化
- 使用分页避免一次性加载大量数据
- 缓存organizationId等常用信息
- 合理设置查询条件

### 3. 安全建议
- 不要在代码中硬编码访问令牌
- 定期更换访问令牌
- 使用最小权限原则

### 4. 数据管理
- 及时清理过期数据
- 定期备份重要信息
- 使用统一的命名规范

---

## 🔗 相关资源

- **云效官方文档**: https://help.aliyun.com/product/153742.html
- **API参考**: https://next.api.aliyun.com/api/devops
- **示例代码**: `yunxiao_demo.py`

---

## 📝 示例执行结果

以下是实际运行 `yunxiao_demo.py` 的输出示例：

```
************************************************************
云效（Yunxiao）API 工具使用示例
************************************************************

示例1: 获取当前用户信息
- 工具: get_current_user
- 用途: 验证身份、获取用户ID

示例2: 获取组织信息
- 工具: get_current_organization_info  
- 用途: 获取organizationId

[更多示例输出...]
```

---

## ❓ 常见问题

### Q1: 认证失败怎么办？
**A**: 检查访问令牌是否有效，确认是否过期，重新生成令牌。

### Q2: 找不到organizationId？
**A**: 登录云效后台 → 组织设置 → 基本信息，可以看到组织ID。

### Q3: 如何获取workitemTypeId？
**A**: 调用 `list_work_item_types` 工具查看项目中可用的工作项类型。

### Q4: 流水线运行失败如何排查？
**A**: 使用 `get_pipeline_job_run_log` 查看详细日志，检查配置和权限。

---

**最后更新**: 2025-10-16  
**版本**: 1.0
