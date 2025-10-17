#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: demo_course_system.py
作者: 开发者
创建日期: 2025-10-16
版本: 1.0
描述: 课程管理系统完整功能演示脚本
      演示学生-课程一体化系统的主要功能
"""

from integrated_system import IntegratedSystem
from course_statistics import CourseStatistics


def print_section(title):
    """打印节标题"""
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70)


def demo_course_management():
    """演示课程管理功能"""
    print_section("1. 课程管理演示")
    
    # 创建一体化系统
    system = IntegratedSystem(
        student_data_file="demo_students.json",
        course_data_file="demo_courses.json"
    )
    
    # 添加学生
    print("\n【添加学生】")
    system.student_system.add_student("张三", 20, "2021001", "计算机科学")
    system.student_system.add_student("李四", 21, "2021002", "软件工程")
    system.student_system.add_student("王五", 20, "2021003", "计算机科学")
    system.student_system.add_student("赵六", 22, "2021004", "软件工程")
    
    # 添加课程
    print("\n【添加课程】")
    system.course_system.add_course(
        course_id="CS101",
        course_name="数据结构与算法",
        teacher="张教授",
        credit=3.0,
        capacity=60,
        description="学习各种数据结构和算法的基础课程",
        semester="2024春季",
        schedule="周一3-4节，周三5-6节"
    )
    
    system.course_system.add_course(
        course_id="CS102",
        course_name="操作系统原理",
        teacher="李教授",
        credit=3.5,
        capacity=50,
        semester="2024春季",
        schedule="周二1-2节，周四3-4节"
    )
    
    system.course_system.add_course(
        course_id="MATH201",
        course_name="高等数学",
        teacher="王教授",
        credit=4.0,
        capacity=80,
        semester="2024春季",
        schedule="周一1-2节，周三1-2节"
    )
    
    return system


def demo_enrollment(system):
    """演示选课功能"""
    print_section("2. 选课管理演示")
    
    print("\n【学生选课】")
    # 张三选课
    system.enroll_student_to_course("2021001", "CS101")
    system.enroll_student_to_course("2021001", "CS102")
    system.enroll_student_to_course("2021001", "MATH201")
    
    # 李四选课
    system.enroll_student_to_course("2021002", "CS101")
    system.enroll_student_to_course("2021002", "MATH201")
    
    # 王五选课
    system.enroll_student_to_course("2021003", "CS101")
    system.enroll_student_to_course("2021003", "CS102")
    
    # 赵六选课
    system.enroll_student_to_course("2021004", "CS102")
    system.enroll_student_to_course("2021004", "MATH201")
    
    print("\n【查看学生选课列表】")
    info = system.get_student_course_info("2021001")
    print(f"\n学生: {info['student_name']}")
    print(f"专业: {info['major']}")
    print(f"已选课程:")
    for course in info['enrolled_courses']:
        print(f"  - {course['course_id']}: {course['course_name']} ({course['credit']}学分)")


def demo_score_management(system):
    """演示成绩管理功能"""
    print_section("3. 成绩管理演示")
    
    print("\n【录入课程成绩】")
    # 为CS101录入成绩
    system.set_course_score_integrated("2021001", "CS101", 95.0)
    system.set_course_score_integrated("2021002", "CS101", 88.0)
    system.set_course_score_integrated("2021003", "CS101", 92.0)
    
    # 为CS102录入成绩
    system.set_course_score_integrated("2021001", "CS102", 87.0)
    system.set_course_score_integrated("2021003", "CS102", 90.0)
    system.set_course_score_integrated("2021004", "CS102", 85.0)
    
    # 为MATH201录入成绩
    system.set_course_score_integrated("2021001", "MATH201", 78.0)
    system.set_course_score_integrated("2021002", "MATH201", 82.0)
    system.set_course_score_integrated("2021004", "MATH201", 75.0)


def demo_statistics(system):
    """演示统计分析功能"""
    print_section("4. 统计分析演示")
    
    # 课程成绩统计
    print("\n【课程成绩分析 - CS101】")
    stats = system.course_statistics.get_course_score_statistics("CS101")
    if stats['has_scores']:
        print(f"课程名称: {stats['course_name']}")
        print(f"参与人数: {stats['total_students']}")
        print(f"平均分: {stats['average_score']:.2f}")
        print(f"最高分: {stats['max_score']:.1f}")
        print(f"最低分: {stats['min_score']:.1f}")
        print(f"优秀率: {stats['excellent_rate']:.1f}%")
        print(f"及格率: {stats['pass_rate']:.1f}%")
        print(f"\n分数段分布:")
        for grade_range, count in stats['score_distribution'].items():
            print(f"  {grade_range}分: {count}人")
    
    # 学生学分统计
    print("\n【学生学分统计 - 张三】")
    credit_stats = system.course_statistics.get_student_credit_statistics("2021001")
    print(f"总选课程数: {credit_stats['total_courses']}")
    print(f"总学分: {credit_stats['total_credits']}")
    print(f"已获学分: {credit_stats['earned_credits']}")
    print(f"平均绩点(GPA): {credit_stats['gpa']:.2f}")
    
    # 热门课程排行
    print("\n【热门课程排行】")
    popular = system.course_statistics.get_popular_courses(top_n=5)
    for i, course_info in enumerate(popular, 1):
        print(f"{i}. {course_info['course_name']}")
        print(f"   选课人数: {course_info['enrolled_count']}/{course_info['capacity']}")
        print(f"   选课率: {course_info['enrollment_rate']:.1f}%")


def demo_transcript(system):
    """演示成绩单生成"""
    print_section("5. 学生成绩单")
    
    transcript = system.get_student_transcript("2021001")
    print(transcript)


def demo_course_report(system):
    """演示课程报告"""
    print_section("6. 课程分析报告")
    
    report = system.course_statistics.generate_course_report("CS101")
    print(report)


def demo_system_overview(system):
    """演示系统总览"""
    print_section("7. 系统总览")
    
    overview = system.get_system_overview()
    
    print("\n【学生统计】")
    student_stats = overview['student_statistics']
    print(f"学生总数: {student_stats['total_students']}")
    print(f"有成绩学生数: {student_stats['students_with_scores']}")
    print(f"优秀学生数: {student_stats['excellent_students']}")
    print(f"系统平均分: {student_stats['average_system_score']:.2f}")
    
    print("\n【课程统计】")
    course_stats = overview['course_statistics']
    print(f"课程总数: {course_stats['total_courses']}")
    print(f"选课记录数: {course_stats['total_enrollments']}")
    print(f"平均选课率: {course_stats['avg_enrollment_rate']:.1f}%")
    print(f"教师总数: {course_stats['total_teachers']}")
    
    print("\n【集成信息】")
    integration_info = overview['integration_info']
    print(f"选课学生数: {integration_info['students_with_courses']}")


def demo_data_management(system):
    """演示数据管理功能"""
    print_section("8. 数据管理演示")
    
    print("\n【保存数据】")
    system.save_all_data()
    
    print("\n【备份数据】")
    system.backup_all_data()
    
    print("\n【导出课程数据(CSV)】")
    system.course_data_manager.export_courses_csv(system.course_system)


def cleanup_demo_files():
    """清理演示文件"""
    import os
    demo_files = [
        "data/demo_students.json",
        "data/demo_courses.json"
    ]
    
    for file_path in demo_files:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"已清理: {file_path}")


def main():
    """主函数"""
    print("="*70)
    print("  课程管理系统完整功能演示")
    print("="*70)
    print("\n本演示将展示学生-课程一体化管理系统的主要功能:")
    print("1. 课程管理（添加课程）")
    print("2. 选课管理（学生选课、查看选课列表）")
    print("3. 成绩管理（录入成绩）")
    print("4. 统计分析（课程统计、学生统计、热门课程）")
    print("5. 成绩单生成")
    print("6. 课程报告")
    print("7. 系统总览")
    print("8. 数据管理（保存、备份、导出）")
    
    input("\n按回车键开始演示...")
    
    try:
        # 执行演示
        system = demo_course_management()
        input("\n按回车键继续...")
        
        demo_enrollment(system)
        input("\n按回车键继续...")
        
        demo_score_management(system)
        input("\n按回车键继续...")
        
        demo_statistics(system)
        input("\n按回车键继续...")
        
        demo_transcript(system)
        input("\n按回车键继续...")
        
        demo_course_report(system)
        input("\n按回车键继续...")
        
        demo_system_overview(system)
        input("\n按回车键继续...")
        
        demo_data_management(system)
        
        print("\n" + "="*70)
        print("  演示完成！")
        print("="*70)
        
        # 询问是否清理演示文件
        cleanup = input("\n是否清理演示生成的文件？(y/n): ").strip().lower()
        if cleanup == 'y':
            cleanup_demo_files()
        
    except Exception as e:
        print(f"\n演示过程中出现错误: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
