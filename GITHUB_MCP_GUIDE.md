# GitHub MCP 工具使用指南

## 📋 概述

本指南展示了如何使用 GitHub 的 MCP（Model Context Protocol）工具集，涵盖从基础查询到高级操作的各种功能。

---

## ✅ 成功示例：已实际运行

### 示例1: 获取 Python 官方仓库信息（无需认证）

**工具**: `mcp_fetch_fetch_markdown`

**调用代码**:
```python
# 使用工具: mcp_fetch_fetch_markdown
# 参数: url = "https://github.com/python/cpython"
```

**成功结果**:
```
✅ 状态: 成功
✅ 获取内容包括:
  - 仓库名称: cpython
  - 仓库描述: The Python programming language
  - Stars: 69.4k ⭐
  - Forks: 33.1k 🔱
  - 完整 README 内容
  - 文件目录结构
  - 贡献者信息
  - 开发文档链接
```

**优点**:
- ✅ 无需 GitHub 认证
- ✅ 可访问任何公开仓库
- ✅ 返回完整页面内容
- ✅ 适合快速查看项目信息

---

## 🔐 需要认证的工具

### 示例2: 搜索仓库

**工具**: `mcp_github_search_repositories`

**调用参数**:
```json
{
  "query": "student management system python",
  "perPage": 5,
  "page": 1
}
```

**搜索语法**:
- `language:python` - 指定编程语言
- `stars:>1000` - Star 数量筛选
- `user:python` - 特定用户的仓库
- `topic:machine-learning` - 按主题搜索
- `created:>2024-01-01` - 按创建时间筛选

**返回数据结构**:
```json
{
  "items": [
    {
      "name": "repository-name",
      "full_name": "owner/repository-name",
      "description": "项目描述",
      "stars_count": 1234,
      "forks_count": 567,
      "language": "Python",
      "html_url": "https://github.com/..."
    }
  ],
  "total_count": 100
}
```

---

### 示例3: 获取文件内容

**工具**: `mcp_github_get_file_contents`

**调用参数**:
```json
{
  "owner": "python",
  "repo": "cpython",
  "path": "README.rst",
  "branch": "main"
}
```

**使用场景**:
- 📖 查看项目文档
- 🔍 研究源代码
- ⚙️ 读取配置文件
- 📋 分析项目结构

---

### 示例4: 创建 Issue

**工具**: `mcp_github_create_issue`

**调用参数**:
```json
{
  "owner": "your-username",
  "repo": "your-repo",
  "title": "优化学生管理系统查询性能",
  "body": "## 问题描述\n当前查询学生列表时速度较慢\n\n## 建议方案\n1. 添加数据库索引\n2. 使用分页加载\n3. 缓存常用查询\n\n## 预期效果\n查询速度提升至100ms以内",
  "labels": ["enhancement", "performance"],
  "assignees": ["developer-name"]
}
```

**最佳实践**:
- ✅ 使用 Markdown 格式编写
- ✅ 清晰描述问题和解决方案
- ✅ 添加相关标签
- ✅ 指定负责人

---

### 示例5: 创建 Pull Request

**工具**: `mcp_github_create_pull_request`

**调用参数**:
```json
{
  "owner": "your-username",
  "repo": "your-repo",
  "title": "添加数据导出功能",
  "head": "feature/export-data",
  "base": "main",
  "body": "## 功能说明\n实现学生数据的CSV和JSON格式导出\n\n## 主要变更\n- 新增 data_exporter.py 模块\n- 添加导出接口\n- 更新用户文档\n\n## 测试\n- [x] 单元测试通过\n- [x] CSV导出功能正常\n- [x] JSON导出功能正常",
  "draft": false
}
```

**PR 描述模板**:
```markdown
## 变更说明
简要描述本次变更的内容

## 变更类型
- [ ] Bug 修复
- [x] 新功能
- [ ] 性能优化
- [ ] 文档更新

## 测试清单
- [x] 单元测试
- [x] 集成测试
- [ ] 性能测试

## 相关 Issue
Closes #123
```

---

### 示例6: 搜索代码

**工具**: `mcp_github_search_code`

**调用参数**:
```json
{
  "q": "def main language:python repo:python/cpython",
  "sort": "indexed",
  "order": "desc",
  "per_page": 10
}
```

**搜索语法**:
```
# 基础搜索
"def Student" language:python

# 在特定仓库中搜索
"class Manager" repo:user/repo

# 按文件类型搜索
"import json" extension:py

# 组合条件
"student.save()" language:python path:src/
```

---

### 示例7: Fork 仓库

**工具**: `mcp_github_fork_repository`

**调用参数**:
```json
{
  "owner": "python",
  "repo": "cpython",
  "organization": ""  // 留空则 fork 到个人账号
}
```

**工作流程**:
1. Fork 原始仓库
2. Clone 到本地
3. 创建功能分支
4. 提交更改
5. 推送到 Fork 仓库
6. 创建 Pull Request

---

### 示例8: 创建分支

**工具**: `mcp_github_create_branch`

**调用参数**:
```json
{
  "owner": "your-username",
  "repo": "your-repo",
  "branch": "feature/new-export-function",
  "from_branch": "main"
}
```

**分支命名规范**:
- `feature/` - 新功能
- `bugfix/` - Bug修复
- `hotfix/` - 紧急修复
- `refactor/` - 代码重构
- `docs/` - 文档更新

---

## 🔑 GitHub 认证配置

### 步骤1: 生成 Personal Access Token

1. 登录 GitHub
2. 点击头像 → Settings
3. Developer settings → Personal access tokens → Tokens (classic)
4. Generate new token (classic)
5. 设置 Token 名称和有效期
6. 选择权限范围:
   - ✅ `repo` - 完整仓库访问
   - ✅ `public_repo` - 公开仓库访问
   - ✅ `read:org` - 读取组织信息
   - ✅ `workflow` - 访问 Actions
   - ✅ `gist` - 创建 Gist

7. 生成并保存 Token（只显示一次！）

### 步骤2: 配置 Token

**方式1: 环境变量**
```bash
export GITHUB_TOKEN="ghp_your_token_here"
```

**方式2: IDE 配置**
- 在 Qoder IDE 中配置 GitHub MCP 插件
- 输入 Token 并保存

### 步骤3: 验证配置
```python
# 测试调用需要认证的工具
# 如果配置正确，将返回数据而非 401 错误
```

---

## 📊 工具功能对比

| 工具名称 | 认证要求 | 主要功能 | 使用难度 |
|---------|---------|---------|---------|
| `fetch_markdown` | ❌ 不需要 | 获取页面内容 | ⭐ 简单 |
| `search_repositories` | ✅ 需要 | 搜索仓库 | ⭐⭐ 中等 |
| `get_file_contents` | ✅ 需要 | 读取文件 | ⭐ 简单 |
| `create_issue` | ✅ 需要 | 创建Issue | ⭐⭐ 中等 |
| `create_pull_request` | ✅ 需要 | 创建PR | ⭐⭐⭐ 复杂 |
| `search_code` | ✅ 需要 | 搜索代码 | ⭐⭐ 中等 |
| `fork_repository` | ✅ 需要 | Fork仓库 | ⭐ 简单 |
| `create_branch` | ✅ 需要 | 创建分支 | ⭐ 简单 |

---

## 🎯 实际应用场景

### 场景1: 学习开源项目

```
1. 搜索相关项目 (search_repositories)
   ↓
2. 查看项目信息 (fetch_markdown)
   ↓
3. Fork 到自己账号 (fork_repository)
   ↓
4. 阅读源代码 (get_file_contents)
   ↓
5. 创建学习笔记 Issue (create_issue)
```

### 场景2: 参与开源贡献

```
1. Fork 项目 (fork_repository)
   ↓
2. 创建功能分支 (create_branch)
   ↓
3. 本地开发和测试
   ↓
4. 提交 Pull Request (create_pull_request)
   ↓
5. 参与代码审查
```

### 场景3: 技术调研

```
1. 搜索相关仓库 (search_repositories)
   ↓
2. 搜索代码实现 (search_code)
   ↓
3. 查看提交历史 (list_commits)
   ↓
4. 分析项目结构 (get_file_contents)
   ↓
5. 整理调研报告
```

---

## ⚡ 快速参考

### 无需认证工具
```python
# 获取仓库页面
mcp_fetch_fetch_markdown(url="https://github.com/owner/repo")

# 获取 HTML 内容
mcp_fetch_fetch_html(url="https://github.com/owner/repo")

# 获取纯文本
mcp_fetch_fetch_txt(url="https://github.com/owner/repo")
```

### 常用认证工具
```python
# 搜索仓库
mcp_github_search_repositories(
    query="python student",
    perPage=10
)

# 获取文件
mcp_github_get_file_contents(
    owner="owner",
    repo="repo",
    path="README.md"
)

# 创建 Issue
mcp_github_create_issue(
    owner="owner",
    repo="repo",
    title="Bug Report",
    body="Description"
)
```

---

## 🐛 常见问题

### Q1: 为什么返回 401 错误？
**A**: 需要配置 GitHub Personal Access Token。按照"认证配置"部分设置。

### Q2: Token 权限不足怎么办？
**A**: 重新生成 Token 时选择更多权限，特别是 `repo` 权限。

### Q3: 如何提高搜索精度？
**A**: 使用高级搜索语法，如 `language:`, `stars:`, `user:` 等限定符。

### Q4: API 调用次数有限制吗？
**A**: 
- 未认证: 60次/小时
- 已认证: 5000次/小时

### Q5: 如何查看更多文件？
**A**: 使用 `get_file_contents` 可以读取仓库中任意文件。

---

## 📚 相关资源

- **GitHub API 文档**: https://docs.github.com/rest
- **Personal Access Tokens**: https://github.com/settings/tokens
- **搜索语法**: https://docs.github.com/search-github/searching-on-github
- **Markdown 指南**: https://guides.github.com/features/mastering-markdown/

---

## 🎓 学习路径

### 初级（无需认证）
1. ✅ 使用 fetch_markdown 查看项目
2. ✅ 了解 GitHub 仓库结构
3. ✅ 学习 README 编写规范

### 中级（基础认证）
1. 配置 Personal Access Token
2. 搜索和发现有趣的项目
3. Fork 并学习优秀代码
4. 创建自己的 Issue

### 高级（完整工作流）
1. 参与开源项目贡献
2. 提交 Pull Request
3. 进行代码审查
4. 管理项目分支和发布

---

## ✨ 总结

✅ **成功调用**: 演示了 `mcp_fetch_fetch_markdown` 工具  
✅ **获取数据**: Python 官方仓库的完整信息  
✅ **文档完整**: 提供了 8 个常用工具的使用说明  
✅ **实践指导**: 包含认证配置和应用场景  

**下一步行动**:
1. 配置 GitHub Personal Access Token
2. 尝试搜索感兴趣的项目
3. Fork 一个项目进行学习
4. 创建第一个 Issue 或 PR

---

**文档版本**: 1.0  
**最后更新**: 2025-10-16  
**示例代码**: `github_mcp_demo.py`
