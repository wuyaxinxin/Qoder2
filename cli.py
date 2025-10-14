#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: cli.py
作者: 开发者
创建日期: 2025-10-13
版本: 1.0
描述: 命令行用户界面模块
      提供交互式菜单系统，用户可以通过命令行操作学生管理系统
"""

import os
import sys
from datetime import datetime
from typing import List, Optional
from student_management_system import StudentManagementSystem
from data_manager import DataManager


class StudentManagementCLI:
    """学生管理系统命令行界面"""
    
    def __init__(self):
        """初始化CLI"""
        self.system = StudentManagementSystem()
        self.data_manager = DataManager()
        self.running = True
    
    def run(self):
        """运行主程序"""
        self.show_welcome()
        
        while self.running:
            try:
                self.show_main_menu()
                choice = input("\n请选择操作 (输入数字): ").strip()
                self.handle_main_menu(choice)
            except KeyboardInterrupt:
                print("\n\n感谢使用学生管理系统！再见！")
                break
            except Exception as e:
                print(f"\n发生错误: {e}")
                input("按回车键继续...")
    
    def show_welcome(self):
        """显示欢迎信息"""
        self.clear_screen()
        print("=" * 60)
        print(" " * 18 + "学生管理系统")
        print(" " * 15 + "Student Management System")
        print("=" * 60)
        print(f"当前数据库中共有 {self.system.get_student_count()} 名学生")
        print("=" * 60)
        input("按回车键继续...")
    
    def show_main_menu(self):
        """显示主菜单"""
        self.clear_screen()
        print("\n" + "=" * 50)
        print(" " * 20 + "主菜单")
        print("=" * 50)
        print("1. 学生管理")
        print("2. 成绩管理") 
        print("3. 查询统计")
        print("4. 数据管理")
        print("5. 系统设置")
        print("0. 退出系统")
        print("=" * 50)
    
    def handle_main_menu(self, choice: str):
        """处理主菜单选择"""
        menu_handlers = {
            '1': self.student_management_menu,
            '2': self.score_management_menu,
            '3': self.query_statistics_menu,
            '4': self.data_management_menu,
            '5': self.system_settings_menu,
            '0': self.exit_system
        }
        
        handler = menu_handlers.get(choice)
        if handler:
            handler()
        else:
            print("无效选择，请重新输入！")
            input("按回车键继续...")
    
    def student_management_menu(self):
        """学生管理菜单"""
        while True:
            self.clear_screen()
            print("\n" + "=" * 50)
            print(" " * 18 + "学生管理")
            print("=" * 50)
            print("1. 添加学生")
            print("2. 删除学生")
            print("3. 修改学生信息")
            print("4. 查看学生详情")
            print("5. 显示所有学生")
            print("6. 搜索学生")
            print("0. 返回主菜单")
            print("=" * 50)
            
            choice = input("\n请选择操作: ").strip()
            
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.remove_student()
            elif choice == '3':
                self.update_student()
            elif choice == '4':
                self.view_student_detail()
            elif choice == '5':
                self.show_all_students()
            elif choice == '6':
                self.search_students()
            elif choice == '0':
                break
            else:
                print("无效选择，请重新输入！")
                input("按回车键继续...")
    
    def score_management_menu(self):
        """成绩管理菜单"""
        while True:
            self.clear_screen()
            print("\n" + "=" * 50)
            print(" " * 18 + "成绩管理")
            print("=" * 50)
            print("1. 添加成绩")
            print("2. 修改成绩")
            print("3. 删除成绩")
            print("4. 查看学生成绩")
            print("0. 返回主菜单")
            print("=" * 50)
            
            choice = input("\n请选择操作: ").strip()
            
            if choice == '1':
                self.add_score()
            elif choice == '2':
                self.update_score()
            elif choice == '3':
                self.remove_score()
            elif choice == '4':
                self.view_student_scores()
            elif choice == '0':
                break
            else:
                print("无效选择，请重新输入！")
                input("按回车键继续...")
    
    def query_statistics_menu(self):
        """查询统计菜单"""
        while True:
            self.clear_screen()
            print("\n" + "=" * 50)
            print(" " * 18 + "查询统计")
            print("=" * 50)
            print("1. 成绩排名")
            print("2. 优秀学生")
            print("3. 系统统计")
            print("0. 返回主菜单")
            print("=" * 50)
            
            choice = input("\n请选择操作: ").strip()
            
            if choice == '1':
                self.show_rankings()
            elif choice == '2':
                self.show_excellent_students()
            elif choice == '3':
                self.show_system_statistics()
            elif choice == '0':
                break
            else:
                print("无效选择，请重新输入！")
                input("按回车键继续...")
    
    def data_management_menu(self):
        """数据管理菜单"""
        while True:
            self.clear_screen()
            print("\n" + "=" * 50)
            print(" " * 18 + "数据管理")
            print("=" * 50)
            print("1. 保存数据")
            print("2. 备份数据")
            print("3. 导出数据")
            print("0. 返回主菜单")
            print("=" * 50)
            
            choice = input("\n请选择操作: ").strip()
            
            if choice == '1':
                self.save_data()
            elif choice == '2':
                self.backup_data()
            elif choice == '3':
                self.export_data()
            elif choice == '0':
                break
            else:
                print("无效选择，请重新输入！")
                input("按回车键继续...")
    
    def system_settings_menu(self):
        """系统设置菜单"""
        self.clear_screen()
        print("\n" + "=" * 50)
        print(" " * 18 + "系统设置")
        print("=" * 50)
        print("1. 查看系统信息")
        print("2. 关于系统")
        print("0. 返回主菜单")
        print("=" * 50)
        
        choice = input("\n请选择操作: ").strip()
        
        if choice == '1':
            self.show_system_info()
        elif choice == '2':
            self.show_about()
        elif choice == '0':
            return
        else:
            print("无效选择，请重新输入！")
            input("按回车键继续...")
        
        input("按回车键继续...")
    
    # 学生管理功能实现
    def add_student(self):
        """添加学生"""
        self.clear_screen()
        print("\n" + "=" * 40)
        print(" " * 15 + "添加学生")
        print("=" * 40)
        
        try:
            name = input("请输入学生姓名: ").strip()
            if not name:
                print("姓名不能为空！")
                input("按回车键继续...")
                return
            
            age_str = input("请输入学生年龄: ").strip()
            if not age_str.isdigit():
                print("年龄必须是数字！")
                input("按回车键继续...")
                return
            age = int(age_str)
            
            student_id = input("请输入学号 (格式:2021001): ").strip()
            major = input("请输入专业 (可选): ").strip()
            
            if self.system.add_student(name, age, student_id, major):
                self.system.save_data()
                print(f"\n成功添加学生：{name}")
            else:
                print("\n添加学生失败！")
                
        except Exception as e:
            print(f"添加学生时发生错误: {e}")
        
        input("按回车键继续...")
    
    def remove_student(self):
        """删除学生"""
        self.clear_screen()
        print("\n" + "=" * 40)
        print(" " * 15 + "删除学生")
        print("=" * 40)
        
        student_id = input("请输入要删除的学号: ").strip()
        if not student_id:
            print("学号不能为空！")
            input("按回车键继续...")
            return
        
        student = self.system.get_student(student_id)
        if not student:
            print(f"学号 {student_id} 不存在！")
            input("按回车键继续...")
            return
        
        print(f"\n学生信息：")
        print(f"姓名: {student.name}")
        print(f"年龄: {student.age}")
        print(f"专业: {student.major}")
        print(f"成绩记录数: {len(student.scores)}")
        
        confirm = input(f"\n确认删除学生 {student.name} (学号: {student_id})? (y/n): ").strip().lower()
        if confirm == 'y':
            if self.system.remove_student(student_id):
                self.system.save_data()
                print("删除成功！")
            else:
                print("删除失败！")
        else:
            print("取消删除操作")
        
        input("按回车键继续...")
    
    def update_student(self):
        """修改学生信息"""
        self.clear_screen()
        print("\n" + "=" * 40)
        print(" " * 13 + "修改学生信息")
        print("=" * 40)
        
        student_id = input("请输入学号: ").strip()
        if not student_id:
            print("学号不能为空！")
            input("按回车键继续...")
            return
        
        student = self.system.get_student(student_id)
        if not student:
            print(f"学号 {student_id} 不存在！")
            input("按回车键继续...")
            return
        
        print(f"\n当前学生信息：")
        print(f"姓名: {student.name}")
        print(f"年龄: {student.age}")
        print(f"专业: {student.major}")
        
        print(f"\n请输入新信息 (留空保持不变):")
        new_name = input(f"新姓名 (当前: {student.name}): ").strip()
        new_age_str = input(f"新年龄 (当前: {student.age}): ").strip()
        new_major = input(f"新专业 (当前: {student.major}): ").strip()
        
        update_data = {}
        if new_name:
            update_data['name'] = new_name
        if new_age_str:
            if new_age_str.isdigit():
                update_data['age'] = int(new_age_str)
            else:
                print("年龄必须是数字！")
                input("按回车键继续...")
                return
        if new_major:
            update_data['major'] = new_major
        
        if update_data:
            if self.system.update_student(student_id, **update_data):
                self.system.save_data()
                print("更新成功！")
            else:
                print("更新失败！")
        else:
            print("没有更新任何信息")
        
        input("按回车键继续...")
    
    def view_student_detail(self):
        """查看学生详情"""
        self.clear_screen()
        print("\n" + "=" * 40)
        print(" " * 13 + "查看学生详情")
        print("=" * 40)
        
        student_id = input("请输入学号: ").strip()
        if not student_id:
            print("学号不能为空！")
            input("按回车键继续...")
            return
        
        student = self.system.get_student(student_id)
        if not student:
            print(f"学号 {student_id} 不存在！")
        else:
            print(student.get_student_info())
        
        input("按回车键继续...")
    
    def show_all_students(self):
        """显示所有学生"""
        students = self.system.get_all_students()
        
        if not students:
            print("\n暂无学生记录")
            input("按回车键继续...")
            return
        
        self.clear_screen()
        print("\n" + "=" * 80)
        print(" " * 32 + "所有学生列表")
        print("=" * 80)
        print(f"{'学号':<12} {'姓名':<10} {'年龄':<6} {'专业':<20} {'成绩数':<8} {'平均分':<8}")
        print("-" * 80)
        
        for student in sorted(students, key=lambda s: s.student_id):
            avg_score = student.get_average_score()
            avg_display = f"{avg_score:.1f}" if avg_score > 0 else "无成绩"
            
            print(f"{student.student_id:<12} {student.name:<10} {student.age:<6} "
                  f"{student.major:<20} {len(student.scores):<8} {avg_display:<8}")
        
        print("-" * 80)
        print(f"总计: {len(students)} 名学生")
        input("\n按回车键继续...")
    
    def search_students(self):
        """搜索学生"""
        self.clear_screen()
        print("\n" + "=" * 40)
        print(" " * 15 + "搜索学生")
        print("=" * 40)
        
        print("搜索条件 (留空跳过该条件):")
        name = input("姓名关键词: ").strip()
        major = input("专业关键词: ").strip()
        
        criteria = {}
        if name:
            criteria['name'] = name
        if major:
            criteria['major'] = major
        
        if not criteria:
            print("请至少输入一个搜索条件！")
            input("按回车键继续...")
            return
        
        results = self.system.search_students(**criteria)
        
        print(f"\n搜索结果: 找到 {len(results)} 名学生")
        if results:
            print("-" * 60)
            for student in results:
                avg_score = student.get_average_score()
                avg_display = f"{avg_score:.1f}" if avg_score > 0 else "无成绩"
                print(f"学号: {student.student_id}, 姓名: {student.name}, "
                      f"年龄: {student.age}, 专业: {student.major}, 平均分: {avg_display}")
        
        input("\n按回车键继续...")
    
    def add_score(self):
        """添加成绩"""
        self.clear_screen()
        print("\n" + "=" * 40)
        print(" " * 15 + "添加成绩")
        print("=" * 40)
        
        student_id = input("请输入学号: ").strip()
        if not student_id:
            print("学号不能为空！")
            input("按回车键继续...")
            return
        
        student = self.system.get_student(student_id)
        if not student:
            print(f"学号 {student_id} 不存在！")
            input("按回车键继续...")
            return
        
        print(f"学生: {student.name} ({student_id})")
        
        subject = input("请输入科目名称: ").strip()
        if not subject:
            print("科目名称不能为空！")
            input("按回车键继续...")
            return
        
        score_str = input("请输入成绩 (0-100): ").strip()
        try:
            score = float(score_str)
            if self.system.add_student_score(student_id, subject, score):
                self.system.save_data()
                print("成绩添加成功！")
            else:
                print("成绩添加失败！")
        except ValueError:
            print("成绩必须是数字！")
        
        input("按回车键继续...")
    
    def update_score(self):
        """修改成绩"""
        self.clear_screen()
        print("\n" + "=" * 40)
        print(" " * 15 + "修改成绩")
        print("=" * 40)
        
        student_id = input("请输入学号: ").strip()
        student = self.system.get_student(student_id)
        if not student or not student.scores:
            print("学生不存在或没有成绩记录！")
            input("按回车键继续...")
            return
        
        print(f"\n学生: {student.name} 的成绩:")
        for subject, score in student.scores.items():
            print(f"  {subject}: {score}")
        
        subject = input("\n请输入要修改的科目名称: ").strip()
        if subject not in student.scores:
            print(f"科目 {subject} 不存在！")
            input("按回车键继续...")
            return
        
        new_score_str = input("请输入新成绩 (0-100): ").strip()
        try:
            new_score = float(new_score_str)
            if self.system.add_student_score(student_id, subject, new_score):
                self.system.save_data()
                print("成绩修改成功！")
        except ValueError:
            print("成绩必须是数字！")
        
        input("按回车键继续...")
    
    def remove_score(self):
        """删除成绩"""
        self.clear_screen()
        print("\n" + "=" * 40)
        print(" " * 15 + "删除成绩") 
        print("=" * 40)
        
        student_id = input("请输入学号: ").strip()
        student = self.system.get_student(student_id)
        if not student or not student.scores:
            print("学生不存在或没有成绩记录！")
            input("按回车键继续...")
            return
        
        print(f"\n学生: {student.name} 的成绩:")
        for subject, score in student.scores.items():
            print(f"  {subject}: {score}")
        
        subject = input("\n请输入要删除的科目名称: ").strip()
        if subject not in student.scores:
            print(f"科目 {subject} 不存在！")
            input("按回车键继续...")
            return
        
        confirm = input(f"确认删除 {subject} 的成绩? (y/n): ").strip().lower()
        if confirm == 'y':
            if student.remove_score(subject):
                self.system.save_data()
                print("成绩删除成功！")
        else:
            print("取消删除操作")
        
        input("按回车键继续...")
    
    def view_student_scores(self):
        """查看学生成绩"""
        self.clear_screen()
        print("\n" + "=" * 40)
        print(" " * 13 + "查看学生成绩")
        print("=" * 40)
        
        student_id = input("请输入学号: ").strip()
        student = self.system.get_student(student_id)
        if not student:
            print(f"学号 {student_id} 不存在！")
            input("按回车键继续...")
            return
        
        print(f"\n学生: {student.name} ({student_id})")
        
        if not student.scores:
            print("暂无成绩记录")
        else:
            print("\n成绩详情:")
            print("-" * 30)
            for subject, score in student.scores.items():
                print(f"{subject:<15}: {score:>6.1f}")
            print("-" * 30)
            print(f"{'平均分':<15}: {student.get_average_score():>6.2f}")
        
        input("\n按回车键继续...")
    
    def show_rankings(self):
        """显示成绩排名"""
        self.clear_screen()
        print("\n" + "=" * 60)
        print(" " * 22 + "成绩排名")
        print("=" * 60)
        
        top_students = self.system.get_top_students(10)
        
        if not top_students:
            print("暂无成绩数据")
        else:
            print(f"\n前 {len(top_students)} 名学生:")
            print("-" * 60)
            print(f"{'排名':<6} {'学号':<12} {'姓名':<10} {'专业':<15} {'平均分':<8}")
            print("-" * 60)
            
            for i, (student, avg_score) in enumerate(top_students, 1):
                print(f"{i:<6} {student.student_id:<12} {student.name:<10} "
                      f"{student.major:<15} {avg_score:<8.2f}")
        
        input("\n按回车键继续...")
    
    def show_excellent_students(self):
        """显示优秀学生"""
        self.clear_screen()
        print("\n" + "=" * 60)
        print(" " * 22 + "优秀学生")
        print("=" * 60)
        
        excellent_students = []
        for student in self.system.get_all_students():
            if student.is_excellent_student():
                excellent_students.append(student)
        
        if not excellent_students:
            print("暂无优秀学生")
        else:
            print(f"\n优秀学生 (平均分≥85且无不及格科目):")
            print("-" * 60)
            print(f"{'学号':<12} {'姓名':<10} {'专业':<15} {'平均分':<8}")
            print("-" * 60)
            
            for student in excellent_students:
                avg_score = student.get_average_score()
                print(f"{student.student_id:<12} {student.name:<10} "
                      f"{student.major:<15} {avg_score:<8.2f}")
            
            print(f"\n共 {len(excellent_students)} 名优秀学生")
        
        input("\n按回车键继续...")
    
    def show_system_statistics(self):
        """显示系统统计"""
        self.clear_screen()
        print("\n" + "=" * 50)
        print(" " * 18 + "系统统计")
        print("=" * 50)
        
        stats = self.system.get_statistics()
        
        print(f"学生总数: {stats['total_students']}")
        print(f"有成绩学生数: {stats['students_with_scores']}")
        print(f"优秀学生数: {stats['excellent_students']}")
        print(f"成绩记录总数: {stats['total_score_records']}")
        print(f"系统平均分: {stats['average_system_score']:.2f}")
        
        if stats['total_students'] > 0:
            print(f"有成绩学生比例: {stats['students_with_scores']/stats['total_students']*100:.1f}%")
            print(f"优秀学生比例: {stats['excellent_students']/stats['total_students']*100:.1f}%")
        
        input("\n按回车键继续...")
    
    def save_data(self):
        """保存数据"""
        if self.system.save_data():
            print("数据保存成功！")
        else:
            print("数据保存失败！")
        input("按回车键继续...")
    
    def backup_data(self):
        """备份数据"""
        if self.system.backup_data():
            print("数据备份成功！")
        else:
            print("数据备份失败！")
        input("按回车键继续...")
    
    def export_data(self):
        """导出数据"""
        data = {
            'students': self.system.export_students_to_dict(),
            'export_time': str(datetime.now())
        }
        
        if self.data_manager.export_data(data, "students_export", "json"):
            print("数据导出成功！")
        else:
            print("数据导出失败！")
        input("按回车键继续...")
    
    def show_system_info(self):
        """显示系统信息"""
        print("\n系统信息:")
        print(f"Python版本: {sys.version}")
        print(f"当前工作目录: {os.getcwd()}")
        print(f"学生管理系统版本: 2.0")
    
    def show_about(self):
        """关于系统"""
        print("\n关于学生管理系统:")
        print("这是一个功能完整的学生信息管理系统")
        print("包含学生信息管理、成绩管理、查询统计等功能")
        print("支持数据持久化、备份和导出功能")
        print("作者: 开发者")
        print("版本: 2.0")
    
    def exit_system(self):
        """退出系统"""
        print("\n正在保存数据...")
        self.system.save_data()
        print("感谢使用学生管理系统！再见！")
        self.running = False
    
    def clear_screen(self):
        """清屏"""
        os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    cli = StudentManagementCLI()
    cli.run()