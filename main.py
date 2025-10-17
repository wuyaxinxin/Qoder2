#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: main.py
作者: 开发者
创建日期: 2025-10-13
版本: 2.0
描述: 学生-课程一体化管理系统主程序入口
      整合学生管理和课程管理功能，提供统一的程序入口
"""

import sys
import os
from datetime import datetime
from cli import StudentManagementCLI
from integrated_system import IntegratedSystem
from course_cli import CourseCLI


def show_main_menu():
    """显示主菜单"""
    print("\n" + "="*50)
    print("学生-课程一体化管理系统")
    print("="*50)
    print("1. 学生管理")
    print("2. 课程管理")
    print("3. 数据管理")
    print("0. 退出系统")
    print("="*50)


def main():
    """主函数"""
    try:
        print("正在启动学生-课程一体化管理系统...")
        
        # 创建一体化系统实例
        integrated_system = IntegratedSystem()
        
        # 创建CLI实例
        student_cli = StudentManagementCLI()
        course_cli = CourseCLI(integrated_system)
        
        # 主循环
        while True:
            show_main_menu()
            choice = input("\n请选择功能模块: ").strip()
            
            if choice == '0':
                # 保存数据
                print("\n正在保存数据...")
                integrated_system.save_all_data()
                print("数据已保存，感谢使用！")
                break
            elif choice == '1':
                # 学生管理
                student_cli.run()
            elif choice == '2':
                # 课程管理
                course_cli.run()
            elif choice == '3':
                # 数据管理
                data_menu(integrated_system)
            else:
                print("无效的选择，请重新输入")
        
    except KeyboardInterrupt:
        print("\n\n程序被用户中断")
    except Exception as e:
        print(f"\n程序运行出错: {e}")
        import traceback
        traceback.print_exc()
    finally:
        print("程序结束")


def data_menu(integrated_system: IntegratedSystem):
    """数据管理菜单"""
    print("\n" + "="*50)
    print("数据管理")
    print("="*50)
    print("1. 保存所有数据")
    print("2. 备份所有数据")
    print("3. 查看系统总览")
    print("0. 返回")
    print("="*50)
    
    choice = input("\n请选择操作: ").strip()
    
    if choice == '1':
        integrated_system.save_all_data()
    elif choice == '2':
        integrated_system.backup_all_data()
    elif choice == '3':
        overview = integrated_system.get_system_overview()
        print("\n=== 系统总览 ===\n")
        print(f"学生总数: {overview['student_statistics']['total_students']}")
        print(f"课程总数: {overview['course_statistics']['total_courses']}")
        print(f"选课记录数: {overview['course_statistics']['total_enrollments']}")
        print(f"平均选课率: {overview['course_statistics']['avg_enrollment_rate']:.1f}%")
        input("\n按回车键继续...")


if __name__ == "__main__":
    main()