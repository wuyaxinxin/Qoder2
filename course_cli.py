#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: course_cli.py
作者: 开发者
创建日期: 2025-10-16
版本: 1.0
描述: 课程管理命令行界面
      提供课程管理的交互式命令行界面
"""

import os
from typing import Optional
from integrated_system import IntegratedSystem
from course_statistics import CourseStatistics


class CourseCLI:
    """课程管理命令行界面类"""
    
    def __init__(self, integrated_system: IntegratedSystem):
        """
        初始化课程CLI
        
        Args:
            integrated_system (IntegratedSystem): 一体化系统对象
        """
        self.system = integrated_system
        self.course_system = integrated_system.course_system
        self.student_system = integrated_system.student_system
        self.statistics = integrated_system.course_statistics
    
    def clear_screen(self):
        """清屏"""
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def pause(self):
        """暂停等待用户按键"""
        input("\n按回车键继续...")
    
    def show_main_menu(self):
        """显示主菜单"""
        print("\n" + "="*50)
        print("课程管理系统 - 主菜单")
        print("="*50)
        print("1. 课程信息管理")
        print("2. 选课管理")
        print("3. 课程统计")
        print("4. 成绩管理")
        print("5. 数据管理")
        print("0. 返回上级菜单")
        print("="*50)
    
    def show_course_info_menu(self):
        """显示课程信息管理菜单"""
        print("\n" + "="*50)
        print("课程信息管理")
        print("="*50)
        print("1. 添加课程")
        print("2. 删除课程")
        print("3. 修改课程")
        print("4. 查询课程")
        print("5. 列出所有课程")
        print("0. 返回上级菜单")
        print("="*50)
    
    def show_enrollment_menu(self):
        """显示选课管理菜单"""
        print("\n" + "="*50)
        print("选课管理")
        print("="*50)
        print("1. 学生选课")
        print("2. 学生退课")
        print("3. 查看学生选课列表")
        print("4. 查看课程学生名单")
        print("5. 批量选课")
        print("0. 返回上级菜单")
        print("="*50)
    
    def show_statistics_menu(self):
        """显示课程统计菜单"""
        print("\n" + "="*50)
        print("课程统计")
        print("="*50)
        print("1. 课程选课统计")
        print("2. 课程成绩分析")
        print("3. 学生选课汇总")
        print("4. 热门课程排行")
        print("5. 教师课程统计")
        print("6. 系统总览")
        print("0. 返回上级菜单")
        print("="*50)
    
    def add_course(self):
        """添加课程"""
        print("\n=== 添加课程 ===")
        
        try:
            course_id = input("请输入课程ID (如CS101): ").strip()
            course_name = input("请输入课程名称: ").strip()
            teacher = input("请输入授课教师: ").strip()
            credit = float(input("请输入学分 (0.5-10.0): "))
            capacity = int(input("请输入课程容量: "))
            description = input("请输入课程描述 (可选): ").strip()
            semester = input("请输入开课学期 (如2024春季): ").strip()
            schedule = input("请输入上课时间 (如周一3-4节): ").strip()
            
            self.course_system.add_course(
                course_id=course_id,
                course_name=course_name,
                teacher=teacher,
                credit=credit,
                capacity=capacity,
                description=description,
                semester=semester,
                schedule=schedule
            )
            
        except ValueError as e:
            print(f"错误：输入格式不正确 - {e}")
        except Exception as e:
            print(f"错误：{e}")
    
    def remove_course(self):
        """删除课程"""
        print("\n=== 删除课程 ===")
        
        course_id = input("请输入要删除的课程ID: ").strip()
        
        # 显示课程信息
        course = self.course_system.get_course(course_id)
        if course:
            print(f"\n课程信息：")
            print(f"课程ID: {course.course_id}")
            print(f"课程名称: {course.course_name}")
            print(f"已选人数: {course.enrolled_count}")
            
            confirm = input("\n确认删除该课程？(y/n): ").strip().lower()
            if confirm == 'y':
                self.course_system.remove_course(course_id)
        else:
            print(f"错误：课程 {course_id} 不存在")
    
    def update_course(self):
        """修改课程"""
        print("\n=== 修改课程 ===")
        
        course_id = input("请输入要修改的课程ID: ").strip()
        
        course = self.course_system.get_course(course_id)
        if not course:
            print(f"错误：课程 {course_id} 不存在")
            return
        
        print(f"\n当前课程信息：")
        print(course.get_course_info())
        
        print("\n请输入要修改的信息（留空表示不修改）：")
        
        updates = {}
        
        course_name = input(f"课程名称 [{course.course_name}]: ").strip()
        if course_name:
            updates['course_name'] = course_name
        
        teacher = input(f"授课教师 [{course.teacher}]: ").strip()
        if teacher:
            updates['teacher'] = teacher
        
        credit_str = input(f"学分 [{course.credit}]: ").strip()
        if credit_str:
            try:
                updates['credit'] = float(credit_str)
            except ValueError:
                print("学分输入格式错误，已跳过")
        
        capacity_str = input(f"课程容量 [{course.capacity}]: ").strip()
        if capacity_str:
            try:
                updates['capacity'] = int(capacity_str)
            except ValueError:
                print("容量输入格式错误，已跳过")
        
        description = input(f"课程描述: ").strip()
        if description:
            updates['description'] = description
        
        semester = input(f"开课学期 [{course.semester}]: ").strip()
        if semester:
            updates['semester'] = semester
        
        schedule = input(f"上课时间 [{course.schedule}]: ").strip()
        if schedule:
            updates['schedule'] = schedule
        
        if updates:
            self.course_system.update_course(course_id, **updates)
        else:
            print("未修改任何信息")
    
    def search_courses(self):
        """查询课程"""
        print("\n=== 查询课程 ===")
        print("1. 按课程ID/名称搜索")
        print("2. 按教师搜索")
        print("3. 按学期搜索")
        
        choice = input("\n请选择查询方式: ").strip()
        
        results = []
        
        if choice == '1':
            keyword = input("请输入关键词: ").strip()
            results = self.course_system.search_courses(keyword=keyword)
        elif choice == '2':
            teacher = input("请输入教师名称: ").strip()
            results = self.course_system.search_courses(teacher=teacher)
        elif choice == '3':
            semester = input("请输入学期: ").strip()
            results = self.course_system.search_courses(semester=semester)
        else:
            print("无效的选择")
            return
        
        if results:
            print(f"\n找到 {len(results)} 门课程：")
            for course in results:
                print(f"\n{course.course_id} - {course.course_name}")
                print(f"  教师: {course.teacher}")
                print(f"  学分: {course.credit}")
                print(f"  选课情况: {course.enrolled_count}/{course.capacity}")
        else:
            print("未找到符合条件的课程")
    
    def list_all_courses(self):
        """列出所有课程"""
        print("\n=== 所有课程列表 ===")
        
        courses = self.course_system.list_all_courses(sort_by="course_id")
        
        if not courses:
            print("暂无课程")
            return
        
        print(f"\n共有 {len(courses)} 门课程：")
        print(f"\n{'课程ID':<12} {'课程名称':<25} {'教师':<12} {'学分':<8} {'选课情况':<15} {'选课率'}")
        print("-" * 90)
        
        for course in courses:
            enrollment_info = f"{course.enrolled_count}/{course.capacity}"
            rate = f"{course.get_enrollment_rate():.1f}%"
            
            print(f"{course.course_id:<12} {course.course_name:<25} {course.teacher:<12} "
                  f"{course.credit:<8.1f} {enrollment_info:<15} {rate}")
    
    def enroll_student(self):
        """学生选课"""
        print("\n=== 学生选课 ===")
        
        student_id = input("请输入学号: ").strip()
        course_id = input("请输入课程ID: ").strip()
        
        # 显示课程信息
        course = self.course_system.get_course(course_id)
        if course:
            print(f"\n课程信息：")
            print(f"课程名称: {course.course_name}")
            print(f"授课教师: {course.teacher}")
            print(f"学分: {course.credit}")
            print(f"剩余名额: {course.get_available_seats()}")
            
            confirm = input("\n确认选课？(y/n): ").strip().lower()
            if confirm == 'y':
                self.system.enroll_student_to_course(student_id, course_id)
        else:
            print(f"错误：课程 {course_id} 不存在")
    
    def drop_course(self):
        """学生退课"""
        print("\n=== 学生退课 ===")
        
        student_id = input("请输入学号: ").strip()
        course_id = input("请输入课程ID: ").strip()
        
        confirm = input("确认退课？(y/n): ").strip().lower()
        if confirm == 'y':
            self.system.drop_student_course(student_id, course_id)
    
    def show_student_courses(self):
        """查看学生选课列表"""
        print("\n=== 学生选课列表 ===")
        
        student_id = input("请输入学号: ").strip()
        
        info = self.system.get_student_course_info(student_id)
        
        if 'error' in info:
            print(info['error'])
            return
        
        print(f"\n学生姓名: {info['student_name']}")
        print(f"专业: {info['major']}")
        print(f"\n学分统计:")
        credit_stats = info['credit_statistics']
        print(f"  总学分: {credit_stats['total_credits']}")
        print(f"  已获学分: {credit_stats['earned_credits']}")
        print(f"  平均绩点: {credit_stats['gpa']}")
        
        courses = info['enrolled_courses']
        if courses:
            print(f"\n已选课程 ({len(courses)}门):")
            print(f"\n{'课程ID':<12} {'课程名称':<25} {'教师':<12} {'学分':<8} {'成绩'}")
            print("-" * 75)
            
            for c in courses:
                score_str = f"{c['score']:.1f}" if c['score'] else "未录入"
                print(f"{c['course_id']:<12} {c['course_name']:<25} {c['teacher']:<12} "
                      f"{c['credit']:<8.1f} {score_str}")
        else:
            print("\n暂无选课记录")
    
    def show_course_students(self):
        """查看课程学生名单"""
        print("\n=== 课程学生名单 ===")
        
        course_id = input("请输入课程ID: ").strip()
        
        info = self.system.get_course_student_info(course_id)
        
        if 'error' in info:
            print(info['error'])
            return
        
        print(f"\n课程名称: {info['course_name']}")
        print(f"授课教师: {info['teacher']}")
        
        students = info['students']
        if students:
            print(f"\n选课学生 ({len(students)}人):")
            print(f"\n{'学号':<12} {'姓名':<15} {'专业':<20} {'成绩'}")
            print("-" * 65)
            
            for s in students:
                score_str = f"{s['score']:.1f}" if s['score'] else "未录入"
                print(f"{s['student_id']:<12} {s['name']:<15} {s['major']:<20} {score_str}")
        else:
            print("\n暂无学生选课")
    
    def run(self) -> bool:
        """运行课程管理CLI"""
        while True:
            self.show_main_menu()
            choice = input("\n请选择操作: ").strip()
            
            if choice == '0':
                return True
            elif choice == '1':
                self.course_info_menu()
            elif choice == '2':
                self.enrollment_menu()
            elif choice == '3':
                self.statistics_menu()
            elif choice == '4':
                self.score_menu()
            elif choice == '5':
                self.data_menu()
            else:
                print("无效的选择，请重新输入")
            
            self.pause()
    
    def course_info_menu(self):
        """课程信息管理菜单"""
        while True:
            self.show_course_info_menu()
            choice = input("\n请选择操作: ").strip()
            
            if choice == '0':
                break
            elif choice == '1':
                self.add_course()
            elif choice == '2':
                self.remove_course()
            elif choice == '3':
                self.update_course()
            elif choice == '4':
                self.search_courses()
            elif choice == '5':
                self.list_all_courses()
            else:
                print("无效的选择")
            
            self.pause()
    
    def enrollment_menu(self):
        """选课管理菜单"""
        while True:
            self.show_enrollment_menu()
            choice = input("\n请选择操作: ").strip()
            
            if choice == '0':
                break
            elif choice == '1':
                self.enroll_student()
            elif choice == '2':
                self.drop_course()
            elif choice == '3':
                self.show_student_courses()
            elif choice == '4':
                self.show_course_students()
            elif choice == '5':
                print("批量选课功能开发中...")
            else:
                print("无效的选择")
            
            self.pause()
    
    def statistics_menu(self):
        """课程统计菜单"""
        while True:
            self.show_statistics_menu()
            choice = input("\n请选择操作: ").strip()
            
            if choice == '0':
                break
            elif choice == '1':
                self.show_enrollment_statistics()
            elif choice == '2':
                self.show_score_analysis()
            elif choice == '3':
                self.show_student_summary()
            elif choice == '4':
                self.show_popular_courses()
            elif choice == '5':
                self.show_teacher_statistics()
            elif choice == '6':
                self.show_system_overview()
            else:
                print("无效的选择")
            
            self.pause()
    
    def show_enrollment_statistics(self):
        """显示选课统计"""
        print("\n=== 课程选课统计 ===")
        course_id = input("请输入课程ID: ").strip()
        
        course = self.course_system.get_course(course_id)
        if course:
            print(course.get_course_info())
        else:
            print(f"错误：课程 {course_id} 不存在")
    
    def show_score_analysis(self):
        """显示成绩分析"""
        print("\n=== 课程成绩分析 ===")
        course_id = input("请输入课程ID: ").strip()
        
        report = self.statistics.generate_course_report(course_id)
        print(report)
    
    def show_student_summary(self):
        """显示学生选课汇总"""
        print("\n=== 学生选课汇总 ===")
        student_id = input("请输入学号: ").strip()
        
        transcript = self.system.get_student_transcript(student_id)
        print(transcript)
    
    def show_popular_courses(self):
        """显示热门课程"""
        print("\n=== 热门课程排行 ===")
        
        popular = self.statistics.get_popular_courses(top_n=10)
        
        if popular:
            print(f"\n{'排名':<6} {'课程ID':<12} {'课程名称':<25} {'选课人数':<12} {'选课率'}")
            print("-" * 75)
            
            for i, course_info in enumerate(popular, 1):
                print(f"{i:<6} {course_info['course_id']:<12} {course_info['course_name']:<25} "
                      f"{course_info['enrolled_count']:<12} {course_info['enrollment_rate']:.1f}%")
        else:
            print("暂无课程数据")
    
    def show_teacher_statistics(self):
        """显示教师统计"""
        print("\n=== 教师课程统计 ===")
        teacher = input("请输入教师姓名: ").strip()
        
        stats = self.statistics.get_teacher_statistics(teacher)
        
        print(f"\n教师: {stats['teacher_name']}")
        print(f"课程总数: {stats['total_courses']}")
        print(f"学生总数: {stats['total_students']}")
        print(f"平均选课率: {stats['avg_enrollment_rate']:.1f}%")
        
        if stats['courses']:
            print(f"\n课程列表:")
            for c in stats['courses']:
                print(f"  {c['course_id']} - {c['course_name']}: {c['enrolled_count']}人")
    
    def show_system_overview(self):
        """显示系统总览"""
        print("\n=== 系统总览 ===")
        
        overview = self.system.get_system_overview()
        
        print("\n【学生统计】")
        student_stats = overview['student_statistics']
        print(f"  学生总数: {student_stats['total_students']}")
        print(f"  有成绩学生数: {student_stats['students_with_scores']}")
        print(f"  优秀学生数: {student_stats['excellent_students']}")
        
        print("\n【课程统计】")
        course_stats = overview['course_statistics']
        print(f"  课程总数: {course_stats['total_courses']}")
        print(f"  选课记录数: {course_stats['total_enrollments']}")
        print(f"  平均选课率: {course_stats['avg_enrollment_rate']:.1f}%")
        print(f"  教师总数: {course_stats['total_teachers']}")
    
    def score_menu(self):
        """成绩管理菜单"""
        print("\n=== 成绩管理 ===")
        print("1. 录入课程成绩")
        print("2. 查询课程成绩")
        
        choice = input("\n请选择操作: ").strip()
        
        if choice == '1':
            self.input_score()
        elif choice == '2':
            self.query_score()
    
    def input_score(self):
        """录入成绩"""
        print("\n=== 录入课程成绩 ===")
        
        student_id = input("请输入学号: ").strip()
        course_id = input("请输入课程ID: ").strip()
        
        try:
            score = float(input("请输入成绩 (0-100): "))
            self.system.set_course_score_integrated(student_id, course_id, score)
        except ValueError:
            print("错误：成绩格式不正确")
    
    def query_score(self):
        """查询成绩"""
        print("\n=== 查询课程成绩 ===")
        
        student_id = input("请输入学号: ").strip()
        course_id = input("请输入课程ID: ").strip()
        
        score = self.course_system.get_course_score(student_id, course_id)
        
        if score is not None:
            print(f"\n成绩: {score:.1f}")
        else:
            print("\n暂无成绩记录")
    
    def data_menu(self):
        """数据管理菜单"""
        print("\n=== 数据管理 ===")
        print("1. 保存数据")
        print("2. 备份数据")
        print("3. 导出课程数据(CSV)")
        
        choice = input("\n请选择操作: ").strip()
        
        if choice == '1':
            self.system.save_all_data()
        elif choice == '2':
            self.system.backup_all_data()
        elif choice == '3':
            self.system.course_data_manager.export_courses_csv(self.course_system)
