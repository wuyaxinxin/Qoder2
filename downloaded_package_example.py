"""
GitHub MCP 工具下载示例
这是一个演示如何使用 GitHub MCP 工具下载 Python 包的示例
"""

# 导入必要的库
import json
import os
from typing import Dict, Any

class PackageDownloader:
    """Python 包下载器示例类"""
    
    def __init__(self, download_dir: str = "./downloads"):
        """
        初始化下载器
        
        Args:
            download_dir: 下载目录路径
        """
        self.download_dir = download_dir
        self.downloaded_files: Dict[str, str] = {}
    
    def download_from_github(self, repo_url: str, file_path: str) -> bool:
        """
        从 GitHub 下载文件
        
        Args:
            repo_url: GitHub 仓库 URL
            file_path: 文件路径
            
        Returns:
            bool: 下载是否成功
        """
        print(f"正在从 {repo_url} 下载 {file_path}...")
        # 这里是下载逻辑的占位符
        return True
    
    def save_file(self, filename: str, content: str) -> str:
        """
        保存下载的文件
        
        Args:
            filename: 文件名
            content: 文件内容
            
        Returns:
            str: 保存的文件路径
        """
        if not os.path.exists(self.download_dir):
            os.makedirs(self.download_dir)
        
        file_path = os.path.join(self.download_dir, filename)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        self.downloaded_files[filename] = file_path
        print(f"文件已保存到: {file_path}")
        return file_path
    
    def get_package_info(self) -> Dict[str, Any]:
        """
        获取已下载包的信息
        
        Returns:
            Dict: 包信息字典
        """
        return {
            "download_dir": self.download_dir,
            "total_files": len(self.downloaded_files),
            "files": list(self.downloaded_files.keys())
        }


def demonstrate_download():
    """演示下载功能"""
    print("=" * 60)
    print("GitHub MCP 工具 - Python 包下载示例")
    print("=" * 60)
    
    downloader = PackageDownloader()
    
    # 示例：下载一个简单的 Python 工具文件
    example_content = '''
"""
示例 Python 实用工具模块
从 GitHub 下载的示例代码
"""

def hello_world():
    """打印 Hello World"""
    print("Hello from downloaded package!")

def calculate_average(numbers):
    """计算平均值"""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

if __name__ == "__main__":
    hello_world()
    print(f"Average of [1,2,3,4,5]: {calculate_average([1,2,3,4,5])}")
'''
    
    # 保存示例文件
    downloader.save_file("example_utils.py", example_content)
    
    # 显示下载信息
    info = downloader.get_package_info()
    print(f"\n下载统计:")
    print(f"  下载目录: {info['download_dir']}")
    print(f"  文件总数: {info['total_files']}")
    print(f"  已下载文件: {', '.join(info['files'])}")
    
    print("\n✅ 下载完成!")


if __name__ == "__main__":
    demonstrate_download()
