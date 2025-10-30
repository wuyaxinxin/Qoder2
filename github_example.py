#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GitHub API 使用示例
此脚本展示了如何使用 GitHub API 工具
"""

import os
from github import Github


def search_repositories(query, max_results=5):
    """
    搜索 GitHub 仓库
    
    Args:
        query (str): 搜索关键词
        max_results (int): 最大返回结果数
    
    Returns:
        list: 仓库信息列表
    """
    # 注意：需要设置 GITHUB_TOKEN 环境变量
    g = Github(os.getenv("GITHUB_TOKEN"))
    
    repositories = []
    try:
        # 搜索仓库
        repos = g.search_repositories(query)[:max_results]
        for repo in repos:
            repositories.append({
                "name": repo.name,
                "full_name": repo.full_name,
                "description": repo.description,
                "stars": repo.stargazers_count,
                "url": repo.html_url
            })
    except Exception as e:
        print(f"搜索仓库时出错: {e}")
    
    return repositories


def get_repository_contents(owner, repo_name, file_path=""):
    """
    获取仓库文件内容
    
    Args:
        owner (str): 仓库所有者
        repo_name (str): 仓库名称
        file_path (str): 文件路径（可选）
    
    Returns:
        dict: 文件信息
    """
    g = Github(os.getenv("GITHUB_TOKEN"))
    
    try:
        repo = g.get_repo(f"{owner}/{repo_name}")
        contents = repo.get_contents(file_path)
        return {
            "name": contents.name,
            "path": contents.path,
            "sha": contents.sha,
            "size": contents.size,
            "content": contents.decoded_content.decode("utf-8") if contents.size < 10000 else "文件过大，仅显示前10000字符"
        }
    except Exception as e:
        print(f"获取文件内容时出错: {e}")
        return None


def create_issue(owner, repo_name, title, body):
    """
    在仓库中创建一个 issue
    
    Args:
        owner (str): 仓库所有者
        repo_name (str): 仓库名称
        title (str): issue 标题
        body (str): issue 内容
    
    Returns:
        dict: issue 信息
    """
    g = Github(os.getenv("GITHUB_TOKEN"))
    
    try:
        repo = g.get_repo(f"{owner}/{repo_name}")
        issue = repo.create_issue(title=title, body=body)
        return {
            "number": issue.number,
            "title": issue.title,
            "url": issue.html_url,
            "state": issue.state
        }
    except Exception as e:
        print(f"创建 issue 时出错: {e}")
        return None


def main():
    """
    主函数 - 演示 GitHub API 的使用
    """
    print("GitHub API 使用示例")
    print("=" * 30)
    
    # 示例1: 搜索仓库
    print("\n1. 搜索仓库示例:")
    repos = search_repositories("machine learning language:python", 3)
    for i, repo in enumerate(repos, 1):
        print(f"{i}. {repo['name']}")
        print(f"   描述: {repo['description']}")
        print(f"   星标: {repo['stars']}")
        print(f"   链接: {repo['url']}")
        print()
    
    # 注意：以下功能需要有效的 GITHUB_TOKEN
    # 示例2: 获取文件内容
    # print("\n2. 获取文件内容示例:")
    # content = get_repository_contents("octocat", "Hello-World", "README.md")
    # if content:
    #     print(f"文件名: {content['name']}")
    #     print(f"路径: {content['path']}")
    #     print(f"大小: {content['size']} 字节")
    #     print("内容预览:")
    #     print(content['content'][:200] + "..." if len(content['content']) > 200 else content['content'])
    
    # 示例3: 创建 issue
    # print("\n3. 创建 issue 示例:")
    # issue = create_issue("your-username", "your-repo", "示例 Issue", "这是通过 API 创建的示例 issue")
    # if issue:
    #     print(f"Issue #{issue['number']}: {issue['title']}")
    #     print(f"状态: {issue['state']}")
    #     print(f"链接: {issue['url']}")


if __name__ == "__main__":
    main()