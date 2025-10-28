#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
学生管理系统报表生成脚本
用法: python3 generate_reports.py
"""

from data_processor import StudentDataProcessor
import os
from datetime import datetime


def generate_all_reports():
    """生成所有报表"""
    
    print("="*60)
    print(" " * 18 + "学生管理系统报表生成" + " " * 18)
    print("="*60)
    print()
    
    # 初始化数据处理器
    processor = StudentDataProcessor()
    
    # 加载数据
    print("正在加载数据...")
    if not processor.load_all_data():
        print("错误: 数据加载失败,请检查data目录下的JSON文件")
        return
    
    print(f"✓ 学生数据: {len(processor.students)} 条记录")
    print(f"✓ 课程数据: {len(processor.courses)} 条记录")
    print(f"✓ 教师数据: {len(processor.teachers)} 条记录")
    print()
    
    # 确保报表目录存在
    output_dir = "reports/"
    os.makedirs(output_dir, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # 1. 生成成绩分布报表
    print("【1/6】生成成绩分布报表...")
    distribution = processor.get_student_score_distribution()
    filename = f"{output_dir}score_distribution_{timestamp}.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("="*60 + "\n")
        f.write(" "*18 + "学生成绩分布统计报表" + " "*18 + "\n")
        f.write("="*60 + "\n\n")
        
        total = sum(distribution.values())
        for grade_range, count in distribution.items():
            percentage = (count / total * 100) if total > 0 else 0
            f.write(f"  {grade_range:<20}{count:>8}人  ({percentage:>5.2f}%)\n")
        
        f.write("\n" + "-"*60 + "\n")
        f.write(f"  总计{total:>27}人\n")
    print(f"  ✓ 已保存: {filename}")
    
    # 2. 生成专业统计报表
    print("【2/6】生成专业统计报表...")
    major_scores = processor.get_major_average_scores()
    filename = f"{output_dir}major_statistics_{timestamp}.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("="*60 + "\n")
        f.write(" "*18 + "专业平均分统计报表" + " "*18 + "\n")
        f.write("="*60 + "\n\n")
        
        for rank, (major, avg_score) in enumerate(major_scores.items(), 1):
            f.write(f"  {rank}. {major:<30}{avg_score:>10.2f}分\n")
    print(f"  ✓ 已保存: {filename}")
    
    # 3. 生成课程热度报表
    print("【3/6】生成课程选课热度报表...")
    courses = processor.get_course_popularity()
    filename = f"{output_dir}course_popularity_{timestamp}.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("="*70 + "\n")
        f.write(" "*22 + "课程选课热度排名" + " "*22 + "\n")
        f.write("="*70 + "\n\n")
        
        for rank, course in enumerate(courses[:10], 1):
            f.write(f"  {rank}. {course['courseName']:<25}")
            f.write(f"选课人数: {course['enrolledCount']:>4}人\n")
    print(f"  ✓ 已保存: {filename}")
    
    # 4. 生成教师工作量报表
    print("【4/6】生成教师工作量报表...")
    teachers = processor.get_teacher_workload()
    filename = f"{output_dir}teacher_workload_{timestamp}.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("="*60 + "\n")
        f.write(" "*18 + "教师工作量统计报表" + " "*18 + "\n")
        f.write("="*60 + "\n\n")
        
        for rank, teacher in enumerate(teachers, 1):
            f.write(f"  {rank}. {teacher['name']:<15}")
            f.write(f"{teacher['subject']:<20}")
            f.write(f"授课班级: {teacher['classCount']:>2}个\n")
    print(f"  ✓ 已保存: {filename}")
    
    # 5. 生成优秀学生名单
    print("【5/6】生成优秀学生名单...")
    students = processor.get_excellent_students()
    filename = f"{output_dir}excellent_students_{timestamp}.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("="*70 + "\n")
        f.write(" "*20 + "优秀学生名单(平均分≥85)" + " "*20 + "\n")
        f.write("="*70 + "\n\n")
        
        for rank, student in enumerate(students, 1):
            f.write(f"  {rank}. {student['name']:<10}")
            f.write(f"{student['studentId']:<12}")
            f.write(f"{student['major']:<20}")
            f.write(f"平均分: {student['averageScore']:>6.2f}\n")
        
        f.write("\n" + "-"*70 + "\n")
        f.write(f"  共 {len(students)} 名优秀学生\n")
    print(f"  ✓ 已保存: {filename}")
    
    # 6. 生成课程通过率报表
    print("【6/6】生成课程通过率报表...")
    pass_rates = processor.get_course_pass_rates()
    filename = f"{output_dir}course_pass_rate_{timestamp}.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("="*60 + "\n")
        f.write(" "*18 + "课程通过率统计报表" + " "*18 + "\n")
        f.write("="*60 + "\n\n")
        
        for course in pass_rates:
            f.write(f"  {course['courseName']:<30}{course['passRate']:>6.2f}%  ({course['passedStudents']}/{course['totalStudents']})\n")
    print(f"  ✓ 已保存: {filename}")
    
    print()
    print("="*60)
    print("所有报表生成完成!")
    print(f"报表文件保存在: {output_dir}")
    print("="*60)


if __name__ == "__main__":
    generate_all_reports()
