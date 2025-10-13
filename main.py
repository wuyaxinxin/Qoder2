#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: main.py
作者: 开发者
创建日期: 2025-10-13
版本: 1.0
描述: 学生管理系统主程序入口
      整合所有功能模块，提供统一的程序入口
"""

import sys
import os
from datetime import datetime
from cli import StudentManagementCLI


def main():
    """主函数"""
    try:
        print("正在启动学生管理系统...")
        
        # 创建CLI实例并运行
        cli = StudentManagementCLI()
        cli.run()
        
    except KeyboardInterrupt:
        print("\n\n程序被用户中断")
    except Exception as e:
        print(f"\n程序运行出错: {e}")
        import traceback
        traceback.print_exc()
    finally:
        print("程序结束")


if __name__ == "__main__":
    main()