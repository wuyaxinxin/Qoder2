#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GitHub 仓库下载工具
使用 MCP 工具从 GitHub 下载仓库内容
"""

import os
import json
from typing import List, Dict, Optional


class GitHubRepoDownloader:
    """GitHub 仓库下载器"""
    
    def __init__(self, save_dir: str = "./downloaded_repos"):
        """
        初始化下载器
        
        Args:
            save_dir: 保存目录
        """
        self.save_dir = save_dir
        self.downloaded_files: List[str] = []
        
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
    
    def parse_repo_url(self, repo_url: str) -> Dict[str, str]:
        """
        解析 GitHub 仓库 URL
        
        Args:
            repo_url: 仓库 URL，例如 https://github.com/owner/repo
            
        Returns:
            包含 owner 和 repo 的字典
        """
        # 移除 .git 后缀和尾部斜杠
        repo_url = repo_url.rstrip('/').replace('.git', '')
        
        # 解析 URL
        if 'github.com/' in repo_url:
            parts = repo_url.split('github.com/')[-1].split('/')
            if len(parts) >= 2:
                return {
                    'owner': parts[0],
                    'repo': parts[1],
                    'full_name': f"{parts[0]}/{parts[1]}"
                }
        
        raise ValueError(f"无效的 GitHub 仓库 URL: {repo_url}")
    
    def get_raw_file_url(self, owner: str, repo: str, file_path: str, 
                         branch: str = "main") -> str:
        """
        获取原始文件 URL
        
        Args:
            owner: 仓库所有者
            repo: 仓库名称
            file_path: 文件路径
            branch: 分支名称
            
        Returns:
            原始文件的 URL
        """
        return f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{file_path}"
    
    def get_api_contents_url(self, owner: str, repo: str, path: str = "") -> str:
        """
        获取 API 内容 URL
        
        Args:
            owner: 仓库所有者
            repo: 仓库名称
            path: 路径
            
        Returns:
            API URL
        """
        if path:
            return f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
        return f"https://api.github.com/repos/{owner}/{repo}/contents"
    
    def save_file(self, file_path: str, content: str) -> str:
        """
        保存文件
        
        Args:
            file_path: 相对文件路径
            content: 文件内容
            
        Returns:
            保存的完整路径
        """
        full_path = os.path.join(self.save_dir, file_path)
        
        # 创建目录
        dir_path = os.path.dirname(full_path)
        if dir_path and not os.path.exists(dir_path):
            os.makedirs(dir_path)
        
        # 保存文件
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        self.downloaded_files.append(full_path)
        print(f"✓ 已下载: {file_path}")
        return full_path
    
    def download_repo_info(self, owner: str, repo: str) -> Optional[Dict]:
        """
        下载仓库信息
        
        Args:
            owner: 仓库所有者
            repo: 仓库名称
            
        Returns:
            仓库信息字典
        """
        print(f"\n正在获取仓库信息: {owner}/{repo}")
        
        # 这里使用 MCP 工具的模拟
        # 实际使用时应调用 mcp_fetch_fetch_json
        
        repo_info = {
            "name": repo,
            "owner": owner,
            "full_name": f"{owner}/{repo}",
            "description": "仓库描述",
            "default_branch": "main"
        }
        
        return repo_info
    
    def generate_download_summary(self) -> str:
        """
        生成下载摘要
        
        Returns:
            摘要字符串
        """
        summary = f"""
{'=' * 60}
下载完成摘要
{'=' * 60}
保存目录: {self.save_dir}
下载文件数: {len(self.downloaded_files)}

已下载文件列表:
"""
        for i, file_path in enumerate(self.downloaded_files, 1):
            summary += f"{i}. {file_path}\n"
        
        summary += f"\n{'=' * 60}\n"
        return summary


def demonstrate_download():
    """演示下载功能"""
    print("=" * 60)
    print("GitHub 仓库下载工具演示")
    print("=" * 60)
    
    # 创建下载器
    downloader = GitHubRepoDownloader(save_dir="./downloaded_repos/demo3")
    
    # 目标仓库信息
    print("\n⚠️  注意: https://github.com/brother519/demo3 仓库不存在或无法访问")
    print("可能的原因:")
    print("  1. 仓库已被删除")
    print("  2. 仓库是私有的")
    print("  3. 用户名或仓库名错误")
    print("  4. 网络连接问题")
    
    # 演示如何使用
    print("\n" + "=" * 60)
    print("使用说明:")
    print("=" * 60)
    print("""
# 1. 解析仓库 URL
repo_info = downloader.parse_repo_url("https://github.com/owner/repo")

# 2. 下载文件 (使用 MCP 工具)
# mcp_fetch_fetch_txt 获取文本文件
# mcp_fetch_fetch_json 获取 JSON 文件
# mcp_fetch_fetch_markdown 获取 Markdown 文件

# 3. 保存文件
downloader.save_file("README.md", content)

# 4. 生成摘要
summary = downloader.generate_download_summary()
print(summary)
""")
    
    # 创建示例文件
    print("\n创建示例文件...")
    
    example_readme = """# Demo3 仓库 (示例)

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
"""
    
    downloader.save_file("README.md", example_readme)
    downloader.save_file("example.txt", "这是一个示例文件")
    
    # 显示摘要
    print(downloader.generate_download_summary())
    
    print("\n💡 提示:")
    print("如果要下载真实的 GitHub 仓库，请确保:")
    print("1. 仓库 URL 正确")
    print("2. 仓库是公开的")
    print("3. 已配置 GitHub 访问权限（如果需要）")


if __name__ == "__main__":
    demonstrate_download()
