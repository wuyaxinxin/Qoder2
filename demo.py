#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: demo.py
作者: 开发者
创建日期: 2025-10-13
版本: 1.0
描述: 学生管理系统演示脚本
      展示系统的主要功能和使用方法
"""

from student_management_system import StudentManagementSystem
from student import Student


def demo_student_management_system():
    """演示学生管理系统的功能"""
    print("=" * 60)
    print(" " * 18 + "学生管理系统演示")
    print("=" * 60)
    
    # 创建系统实例
    system = StudentManagementSystem("demo_students.json")
    
    print("\n1. 添加学生信息...")
    print("-" * 40)
    
    # 添加学生
    students_data = [
        ("张三", 20, "2021001", "计算机科学与技术"),
        ("李四", 19, "2021002", "数学与应用数学"),
        ("王五", 21, "2021003", "物理学"),
        ("赵六", 20, "2021004", "化学"),
        ("钱七", 22, "2021005", "生物学")
    ]
    
    for name, age, student_id, major in students_data:
        if system.add_student(name, age, student_id, major):
            print(f"✓ 成功添加学生：{name} (学号: {student_id})")
        else:
            print(f"✗ 添加学生失败：{name}")
    
    print(f"\n当前系统中共有 {system.get_student_count()} 名学生")
    
    print("\n2. 添加学生成绩...")
    print("-" * 40)
    
    # 添加成绩
    scores_data = [
        ("2021001", "高等数学", 92),
        ("2021001", "程序设计", 88),
        ("2021001", "英语", 85),
        ("2021001", "物理", 78),
        
        ("2021002", "高等数学", 95),
        ("2021002", "线性代数", 90),
        ("2021002", "英语", 82),
        ("2021002", "概率统计", 88),
        
        ("2021003", "高等数学", 83),
        ("2021003", "普通物理", 91),
        ("2021003", "英语", 75),
        ("2021003", "量子力学", 87),
        
        ("2021004", "高等数学", 86),
        ("2021004", "无机化学", 89),
        ("2021004", "英语", 79),
        ("2021004", "有机化学", 92),
        
        ("2021005", "高等数学", 81),
        ("2021005", "普通生物学", 94),
        ("2021005", "英语", 88),
        ("2021005", "分子生物学", 90)
    ]
    
    for student_id, subject, score in scores_data:
        if system.add_student_score(student_id, subject, score):
            student = system.get_student(student_id)
            print(f"✓ {student.name} - {subject}: {score}分")
    
    print("\n3. 显示学生详细信息...")
    print("-" * 40)
    
    # 显示几个学生的详细信息
    for student_id in ["2021001", "2021002"]:
        student = system.get_student(student_id)
        if student:
            print(f"\n学生：{student.name} (学号: {student_id})")
            print(f"专业：{student.major}")
            print(f"成绩记录：")
            for subject, score in student.scores.items():
                print(f"  {subject}: {score:.1f}分")
            print(f"平均分：{student.get_average_score():.2f}")
            
            highest = student.get_highest_score()
            if highest:
                print(f"最高分：{highest[0]} ({highest[1]:.1f}分)")
            
            print(f"是否优秀学生：{'是' if student.is_excellent_student() else '否'}")
    
    print("\n4. 成绩排名...")
    print("-" * 40)
    
    top_students = system.get_top_students(5)
    print("成绩排名前5名：")
    for i, (student, avg_score) in enumerate(top_students, 1):
        print(f"{i:2d}. {student.name:<8} (学号: {student.student_id}) - 平均分: {avg_score:5.2f}")
    
    print("\n5. 优秀学生列表...")
    print("-" * 40)
    
    excellent_students = []
    for student in system.get_all_students():
        if student.is_excellent_student():
            excellent_students.append(student)
    
    if excellent_students:
        print("优秀学生名单（平均分≥85且无不及格科目）：")
        for student in excellent_students:
            avg_score = student.get_average_score()
            print(f"• {student.name:<8} (学号: {student.student_id}) - 平均分: {avg_score:5.2f}")
    else:
        print("暂无优秀学生")
    
    print("\n6. 系统统计信息...")
    print("-" * 40)
    
    stats = system.get_statistics()
    print(f"学生总数：{stats['total_students']}")
    print(f"有成绩学生数：{stats['students_with_scores']}")
    print(f"优秀学生数：{stats['excellent_students']}")
    print(f"成绩记录总数：{stats['total_score_records']}")
    print(f"系统平均分：{stats['average_system_score']:.2f}")
    
    if stats['total_students'] > 0:
        print(f"有成绩学生比例：{stats['students_with_scores']/stats['total_students']*100:.1f}%")
        print(f"优秀学生比例：{stats['excellent_students']/stats['total_students']*100:.1f}%")
    
    print("\n7. 搜索功能演示...")
    print("-" * 40)
    
    # 按姓名搜索
    results = system.search_students(name="张")
    print(f"姓名包含'张'的学生：{len(results)}个")
    for student in results:
        print(f"  • {student.name} (学号: {student.student_id})")
    
    # 按专业搜索
    results = system.search_students(major="计算机")
    print(f"专业包含'计算机'的学生：{len(results)}个")
    for student in results:
        print(f"  • {student.name} - {student.major}")
    
    # 按年龄范围搜索
    results = system.search_students(min_age=20, max_age=21)
    print(f"年龄在20-21岁的学生：{len(results)}个")
    for student in results:
        print(f"  • {student.name} - 年龄: {student.age}")
    
    print("\n8. 数据持久化...")
    print("-" * 40)
    
    # 保存数据
    if system.save_data():
        print("✓ 数据已保存到文件")
    else:
        print("✗ 数据保存失败")
    
    # 创建备份
    if system.backup_data():
        print("✓ 数据备份创建成功")
    else:
        print("✗ 数据备份创建失败")
    
    print("\n" + "=" * 60)
    print("演示完成！")
    print("你可以运行 'python main.py' 启动完整的交互式系统")
    print("或运行 'python test_student_system.py' 执行单元测试")
    print("=" * 60)


def demo_individual_student():
    """演示单个学生类的功能"""
    print("\n" + "=" * 50)
    print(" " * 15 + "学生类功能演示")
    print("=" * 50)
    
    # 创建学生对象
    student = Student("演示学生", 20, "2021999", "演示专业")
    print(f"创建学生：{student.name}")
    
    # 添加成绩
    subjects_scores = [
        ("数学", 95),
        ("英语", 87),
        ("物理", 92),
        ("化学", 88),
        ("生物", 91)
    ]
    
    print("\n添加成绩：")
    for subject, score in subjects_scores:
        student.add_score(subject, score)
    
    # 显示统计信息
    print(f"\n成绩统计：")
    print(f"平均分：{student.get_average_score():.2f}")
    
    highest = student.get_highest_score()
    if highest:
        print(f"最高分：{highest[0]} ({highest[1]:.1f}分)")
    
    lowest = student.get_lowest_score()
    if lowest:
        print(f"最低分：{lowest[0]} ({lowest[1]:.1f}分)")
    
    print(f"及格科目：{len(student.get_passing_subjects())}")
    print(f"不及格科目：{len(student.get_failing_subjects())}")
    print(f"是否优秀学生：{'是' if student.is_excellent_student() else '否'}")
    
    # 显示完整信息
    print("\n完整学生信息：")
    print(student.get_student_info())


if __name__ == "__main__":
    # 主演示
    demo_student_management_system()
    
    # 学生类演示
    demo_individual_student()
    
    print("\n🎉 所有演示完成！")
    print("\n如需了解更多功能，请查看 README.md 文档")
    print("或直接运行 'python main.py' 体验完整系统")