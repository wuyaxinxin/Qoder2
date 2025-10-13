#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: main.py
作者: 开发者
创建日期: 2025-10-13
版本: 2.0
描述: 学生管理系统主程序 - 提供交互式命令行界面
"""

import os
import sys
from student_manager import StudentManager
from student import Student
from utils import format_timestamp


class StudentManagementSystem:
    """学生管理系统交互界面"""
    
    def __init__(self):
        """初始化系统"""
        self.manager = StudentManager()
        self.running = True
    
    def clear_screen(self):
        """清屏"""
        os.system('clear' if os.name != 'nt' else 'cls')
    
    def display_menu(self):
        """显示主菜单"""
        print("\n" + "="*60)
        print(" "*20 + "学生管理系统")
        print("="*60)
        print("【学生管理】")
        print("  1. 添加学生")
        print("  2. 删除学生")
        print("  3. 修改学生信息")
        print("  4. 查询学生")
        print("  5. 显示所有学生")
        print()
        print("【成绩管理】")
        print("  6. 添加/修改成绩")
        print("  7. 删除成绩")
        print("  8. 查看学生成绩详情")
        print()
        print("【统计分析】")
        print("  9. 系统统计信息")
        print(" 10. 成绩排名")
        print(" 11. 优秀学生列表")
        print()
        print("【数据管理】")
        print(" 12. 保存数据")
        print(" 13. 导出CSV")
        print(" 14. 清空所有数据")
        print()
        print("  0. 退出系统")
        print("="*60)
    
    def add_student_menu(self):
        """添加学生菜单"""
        print("\n【添加学生】")
        try:
            name = input("请输入姓名: ").strip()
            age = int(input("请输入年龄: "))
            student_id = input("请输入学号(7位数字，如2021001): ").strip()
            major = input("请输入专业: ").strip()
            
            self.manager.add_student(name, age, student_id, major)
        except ValueError:
            print("错误：年龄必须是数字")
        except Exception as e:
            print(f"错误：{str(e)}")
    
    def remove_student_menu(self):
        """删除学生菜单"""
        print("\n【删除学生】")
        student_id = input("请输入要删除的学号: ").strip()
        
        # 确认删除
        student = self.manager.get_student(student_id)
        if student:
            confirm = input(f"确定要删除学生 {student.name} ({student_id}) 吗？(y/n): ")
            if confirm.lower() == 'y':
                self.manager.remove_student(student_id)
        else:
            print(f"错误：找不到学号为 {student_id} 的学生")
    
    def update_student_menu(self):
        """修改学生信息菜单"""
        print("\n【修改学生信息】")
        student_id = input("请输入学号: ").strip()
        
        student = self.manager.get_student(student_id)
        if not student:
            print(f"错误：找不到学号为 {student_id} 的学生")
            return
        
        print(f"\n当前信息：{student.name}, {student.age}岁, {student.major}")
        print("提示：直接回车跳过不修改的项目")
        
        name = input(f"新姓名 (当前: {student.name}): ").strip()
        age_str = input(f"新年龄 (当前: {student.age}): ").strip()
        major = input(f"新专业 (当前: {student.major}): ").strip()
        
        try:
            age = int(age_str) if age_str else None
            self.manager.update_student_info(
                student_id,
                name if name else None,
                age,
                major if major else None
            )
        except ValueError:
            print("错误：年龄必须是数字")
    
    def search_student_menu(self):
        """查询学生菜单"""
        print("\n【查询学生】")
        keyword = input("请输入关键词(姓名/学号/专业): ").strip()
        
        results = self.manager.search_students(keyword)
        
        if not results:
            print(f"未找到匹配 '{keyword}' 的学生")
            return
        
        print(f"\n找到 {len(results)} 名学生：")
        print("-" * 80)
        print(f"{'学号':<12} {'姓名':<10} {'年龄':<6} {'专业':<20} {'平均分':<10}")
        print("-" * 80)
        
        for student in results:
            avg_score = student.get_average_score()
            avg_str = f"{avg_score:.2f}" if avg_score > 0 else "无成绩"
            print(f"{student.student_id:<12} {student.name:<10} {student.age:<6} "
                  f"{student.major:<20} {avg_str:<10}")
    
    def display_all_students(self):
        """显示所有学生"""
        print("\n【所有学生列表】")
        students = self.manager.get_all_students()
        
        if not students:
            print("暂无学生数据")
            return
        
        print(f"\n总计 {len(students)} 名学生：")
        print("-" * 90)
        print(f"{'学号':<12} {'姓名':<10} {'年龄':<6} {'专业':<20} {'平均分':<10} {'科目数':<8}")
        print("-" * 90)
        
        for student in sorted(students, key=lambda s: s.student_id):
            avg_score = student.get_average_score()
            avg_str = f"{avg_score:.2f}" if avg_score > 0 else "无成绩"
            print(f"{student.student_id:<12} {student.name:<10} {student.age:<6} "
                  f"{student.major:<20} {avg_str:<10} {len(student.scores):<8}")
    
    def add_score_menu(self):
        """添加/修改成绩菜单"""
        print("\n【添加/修改成绩】")
        student_id = input("请输入学号: ").strip()
        
        student = self.manager.get_student(student_id)
        if not student:
            print(f"错误：找不到学号为 {student_id} 的学生")
            return
        
        print(f"\n学生：{student.name} ({student_id})")
        subject = input("请输入科目名称: ").strip()
        
        try:
            score = float(input("请输入成绩(0-100): "))
            if student.add_score(subject, score):
                self.manager.save_data()
        except ValueError:
            print("错误：成绩必须是数字")
    
    def remove_score_menu(self):
        """删除成绩菜单"""
        print("\n【删除成绩】")
        student_id = input("请输入学号: ").strip()
        
        student = self.manager.get_student(student_id)
        if not student:
            print(f"错误：找不到学号为 {student_id} 的学生")
            return
        
        print(f"\n学生：{student.name} ({student_id})")
        if not student.scores:
            print("该学生暂无成绩记录")
            return
        
        print("现有成绩：", ", ".join(student.scores.keys()))
        subject = input("请输入要删除的科目: ").strip()
        
        if student.remove_score(subject):
            self.manager.save_data()
    
    def view_student_details(self):
        """查看学生成绩详情"""
        print("\n【学生成绩详情】")
        student_id = input("请输入学号: ").strip()
        
        student = self.manager.get_student(student_id)
        if not student:
            print(f"错误：找不到学号为 {student_id} 的学生")
            return
        
        print(student.get_student_info())
    
    def show_statistics(self):
        """显示系统统计信息"""
        print("\n【系统统计信息】")
        stats = self.manager.get_statistics()
        
        print(f"\n学生总数: {stats['total_students']}")
        print(f"平均年龄: {stats['average_age']}")
        print(f"优秀学生: {stats['excellent_students']}")
        
        print("\n专业分布:")
        for major, count in stats['major_distribution'].items():
            percentage = (count / stats['total_students'] * 100) if stats['total_students'] > 0 else 0
            print(f"  {major}: {count}人 ({percentage:.1f}%)")
    
    def show_ranking(self):
        """显示成绩排名"""
        print("\n【成绩排名】")
        try:
            limit = int(input("请输入显示人数(默认10): ") or "10")
        except ValueError:
            limit = 10
        
        top_students = self.manager.get_top_students(limit)
        
        if not top_students:
            print("暂无学生成绩数据")
            return
        
        print(f"\n前 {len(top_students)} 名学生：")
        print("-" * 70)
        print(f"{'排名':<6} {'学号':<12} {'姓名':<10} {'专业':<20} {'平均分':<10}")
        print("-" * 70)
        
        for rank, (student, avg_score) in enumerate(top_students, 1):
            print(f"{rank:<6} {student.student_id:<12} {student.name:<10} "
                  f"{student.major:<20} {avg_score:.2f}")
    
    def show_excellent_students(self):
        """显示优秀学生列表"""
        print("\n【优秀学生列表】")
        print("(平均分≥85且无不及格科目)")
        
        excellent_students = [s for s in self.manager.get_all_students() 
                             if s.is_excellent_student()]
        
        if not excellent_students:
            print("暂无优秀学生")
            return
        
        print(f"\n共 {len(excellent_students)} 名优秀学生：")
        print("-" * 70)
        print(f"{'学号':<12} {'姓名':<10} {'专业':<20} {'平均分':<10}")
        print("-" * 70)
        
        for student in sorted(excellent_students, 
                             key=lambda s: s.get_average_score(), 
                             reverse=True):
            print(f"{student.student_id:<12} {student.name:<10} "
                  f"{student.major:<20} {student.get_average_score():.2f}")
    
    def export_csv_menu(self):
        """导出CSV菜单"""
        print("\n【导出CSV】")
        filename = input("请输入文件名(默认students_export.csv): ").strip()
        if not filename:
            filename = "students_export.csv"
        
        self.manager.export_to_csv(filename)
    
    def clear_data_menu(self):
        """清空数据菜单"""
        print("\n【清空所有数据】")
        print("警告：此操作将删除所有学生数据，且不可恢复！")
        confirm1 = input("确定要继续吗？(yes/no): ").strip()
        
        if confirm1.lower() == 'yes':
            confirm2 = input("请再次确认(输入'DELETE'): ").strip()
            if confirm2 == 'DELETE':
                self.manager.clear_all_data()
            else:
                print("已取消操作")
        else:
            print("已取消操作")
    
    def run(self):
        """运行系统主循环"""
        print("\n欢迎使用学生管理系统！")
        print(f"数据文件：{self.manager.data_file}")
        print(f"当前时间：{format_timestamp()}")
        
        while self.running:
            self.display_menu()
            
            try:
                choice = input("\n请选择操作(0-14): ").strip()
                
                if choice == '1':
                    self.add_student_menu()
                elif choice == '2':
                    self.remove_student_menu()
                elif choice == '3':
                    self.update_student_menu()
                elif choice == '4':
                    self.search_student_menu()
                elif choice == '5':
                    self.display_all_students()
                elif choice == '6':
                    self.add_score_menu()
                elif choice == '7':
                    self.remove_score_menu()
                elif choice == '8':
                    self.view_student_details()
                elif choice == '9':
                    self.show_statistics()
                elif choice == '10':
                    self.show_ranking()
                elif choice == '11':
                    self.show_excellent_students()
                elif choice == '12':
                    self.manager.save_data()
                    print("数据已保存")
                elif choice == '13':
                    self.export_csv_menu()
                elif choice == '14':
                    self.clear_data_menu()
                elif choice == '0':
                    self.quit_system()
                else:
                    print("无效的选择，请重新输入")
                
                input("\n按回车键继续...")
                
            except KeyboardInterrupt:
                print("\n\n检测到中断信号...")
                self.quit_system()
            except Exception as e:
                print(f"\n发生错误：{str(e)}")
                input("按回车键继续...")
    
    def quit_system(self):
        """退出系统"""
        print("\n正在保存数据...")
        self.manager.save_data()
        print("感谢使用学生管理系统，再见！")
        self.running = False


def main():
    """主函数"""
    system = StudentManagementSystem()
    system.run()


if __name__ == "__main__":
    main()
