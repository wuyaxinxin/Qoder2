# Demo3 仓库 (示例)

这是一个演示如何使用 GitHub MCP 工具下载仓库的示例。

## 功能特性

- ✅ 仓库信息解析
- ✅ 文件下载管理
- ✅ 目录结构保持
- ✅ 下载进度追踪

## 使用方法

```python
from github_repo_downloader import GitHubRepoDownloader

# 创建下载器
downloader = GitHubRepoDownloader()

# 下载仓库
downloader.download_repo("https://github.com/owner/repo")
```

## 注意事项

1. 确保有网络连接
2. 确保仓库是公开的
3. 遵守 GitHub 使用条款
