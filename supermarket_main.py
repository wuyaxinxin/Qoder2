"""
始终生效
超市管理系统 - 主入口程序
系统启动文件
"""

from supermarket_cli import SupermarketCLI


def main():
    """主函数"""
    cli = SupermarketCLI()
    cli.run()


if __name__ == "__main__":
    main()
