#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: demo.py
作者: 开发者
创建日期: 2025-10-13
版本: 1.0
描述: 学生管理系统演示脚本 - 展示系统主要功能
"""

from student import Student
from student_manager import StudentManager
from utils import format_timestamp
import os


def print_separator(title=""):
    """打印分隔线"""
    if title:
        print(f"\n{'='*70}")
        print(f"  {title}")
        print('='*70)
    else:
        print('-'*70)


def demo_student_basic():
    """演示学生基本功能"""
    print_separator("1. 学生基本功能演示")
    
    # 创建学生对象
    student = Student("张三", 20, "2021001", "计算机科学与技术")
    print(f"创建学生: {student.name}, 学号: {student.student_id}")
    
    # 添加成绩
    print("\n添加成绩:")
    student.add_score("高等数学", 95)
    student.add_score("程序设计", 88)
    student.add_score("英语", 76)
    student.add_score("数据结构", 92)
    
    # 显示学生信息
    print(student.get_student_info())


def demo_student_manager():
    """演示学生管理器功能"""
    print_separator("2. 学生管理器功能演示")
    
    # 创建管理器(使用演示数据文件)
    demo_file = "demo_students.json"
    manager = StudentManager(demo_file)
    manager.clear_all_data()
    
    # 添加多个学生
    print("\n添加学生:")
    manager.add_student("张三", 20, "2021001", "计算机科学与技术")
    manager.add_student("李四", 19, "2021002", "数学与应用数学")
    manager.add_student("王五", 21, "2021003", "计算机科学与技术")
    manager.add_student("赵六", 20, "2021004", "物理学")
    manager.add_student("钱七", 19, "2021005", "数学与应用数学")
    
    print(f"\n当前学生总数: {manager.get_student_count()}")
    
    # 为学生添加成绩
    print("\n添加成绩数据:")
    students_scores = {
        "2021001": [("高等数学", 95), ("程序设计", 88), ("英语", 76), ("数据结构", 92)],
        "2021002": [("高等数学", 98), ("线性代数", 91), ("英语", 85), ("概率论", 88)],
        "2021003": [("高等数学", 72), ("程序设计", 68), ("英语", 65), ("数据结构", 70)],
        "2021004": [("高等数学", 88), ("普通物理", 92), ("英语", 80), ("理论力学", 85)],
        "2021005": [("高等数学", 91), ("线性代数", 87), ("英语", 78), ("概率论", 90)]
    }
    
    for student_id, scores in students_scores.items():
        student = manager.get_student(student_id)
        for subject, score in scores:
            student.add_score(subject, score)
    
    print("✓ 成绩数据添加完成")
    
    # 保存数据
    manager.save_data()
    print(f"✓ 数据已保存到: {demo_file}")
    
    return manager, demo_file


def demo_search_and_query(manager):
    """演示搜索和查询功能"""
    print_separator("3. 搜索和查询功能演示")
    
    # 搜索学生
    print("\n搜索关键词'计算机':")
    results = manager.search_students("计算机")
    for student in results:
        print(f"  - {student.name} ({student.student_id}) - {student.major}")
    
    # 获取特定学生信息
    print("\n查询学号2021001的学生详细信息:")
    student = manager.get_student("2021001")
    if student:
        print_separator()
        print(student.get_student_info())


def demo_statistics(manager):
    """演示统计分析功能"""
    print_separator("4. 统计分析功能演示")
    
    # 系统统计
    stats = manager.get_statistics()
    print("\n系统统计信息:")
    print(f"  学生总数: {stats['total_students']}")
    print(f"  平均年龄: {stats['average_age']}")
    print(f"  优秀学生数: {stats['excellent_students']}")
    
    print("\n  专业分布:")
    for major, count in stats['major_distribution'].items():
        percentage = (count / stats['total_students'] * 100)
        print(f"    {major}: {count}人 ({percentage:.1f}%)")
    
    # 成绩排名
    print("\n成绩排名 Top 3:")
    top_students = manager.get_top_students(3)
    for rank, (student, avg_score) in enumerate(top_students, 1):
        status = "⭐优秀" if student.is_excellent_student() else ""
        print(f"  {rank}. {student.name} ({student.student_id}) - "
              f"平均分: {avg_score:.2f} {status}")
    
    # 优秀学生列表
    print("\n优秀学生列表 (平均分≥85且无不及格):")
    excellent_students = [s for s in manager.get_all_students() 
                         if s.is_excellent_student()]
    
    if excellent_students:
        for student in sorted(excellent_students, 
                             key=lambda s: s.get_average_score(), 
                             reverse=True):
            print(f"  ⭐ {student.name} ({student.student_id}) - "
                  f"平均分: {student.get_average_score():.2f}")
    else:
        print("  暂无优秀学生")


def demo_data_export(manager, demo_file):
    """演示数据导出功能"""
    print_separator("5. 数据导出功能演示")
    
    # 导出CSV
    csv_file = "demo_export.csv"
    manager.export_to_csv(csv_file)
    
    # 显示导出文件内容
    if os.path.exists(csv_file):
        print(f"\nCSV文件内容预览 ({csv_file}):")
        print_separator()
        with open(csv_file, 'r', encoding='utf-8-sig') as f:
            lines = f.readlines()
            for i, line in enumerate(lines[:6]):  # 只显示前6行
                print(line.rstrip())
            if len(lines) > 6:
                print("...")
    
    # JSON数据格式
    print(f"\n\nJSON数据文件 ({demo_file}):")
    print("数据以JSON格式存储，便于程序读取和处理")
    print("包含学生基本信息、成绩详情、创建时间等完整数据")


def demo_update_and_delete(manager):
    """演示更新和删除功能"""
    print_separator("6. 更新和删除功能演示")
    
    # 更新学生信息
    print("\n更新学生信息:")
    student_id = "2021001"
    student = manager.get_student(student_id)
    print(f"原信息: {student.name}, {student.age}岁, {student.major}")
    
    manager.update_student_info(student_id, name="张三丰", age=21)
    student = manager.get_student(student_id)
    print(f"新信息: {student.name}, {student.age}岁, {student.major}")
    
    # 删除成绩
    print("\n删除成绩演示:")
    print(f"当前科目: {list(student.scores.keys())}")
    student.remove_score("英语")
    print(f"删除'英语'后: {list(student.scores.keys())}")
    
    # 恢复原始数据
    manager.update_student_info(student_id, name="张三", age=20)
    student.add_score("英语", 76)


def demo_comprehensive_report():
    """生成综合演示报告"""
    print_separator("7. 综合演示报告")
    
    # 创建一个完整的示例场景
    manager = StudentManager("comprehensive_demo.json")
    manager.clear_all_data()
    
    # 添加班级数据
    print("\n场景: 某大学计算机系2021级1班成绩管理")
    print("\n正在导入学生数据...")
    
    students_data = [
        ("张伟", 20, "2021001", "计算机科学与技术"),
        ("李娜", 19, "2021002", "软件工程"),
        ("王芳", 20, "2021003", "计算机科学与技术"),
        ("刘洋", 21, "2021004", "软件工程"),
        ("陈静", 19, "2021005", "计算机科学与技术"),
    ]
    
    for name, age, sid, major in students_data:
        manager.add_student(name, age, sid, major)
    
    # 添加成绩
    print("\n正在导入成绩数据...")
    scores_data = {
        "2021001": {"高数": 92, "英语": 85, "程序设计": 88, "数据结构": 90},
        "2021002": {"高数": 78, "英语": 92, "程序设计": 82, "数据结构": 85},
        "2021003": {"高数": 88, "英语": 80, "程序设计": 95, "数据结构": 91},
        "2021004": {"高数": 65, "英语": 70, "程序设计": 68, "数据结构": 72},
        "2021005": {"高数": 95, "英语": 88, "程序设计": 92, "数据结构": 94},
    }
    
    for sid, scores in scores_data.items():
        student = manager.get_student(sid)
        for subject, score in scores.items():
            student.add_score(subject, score)
    
    # 生成报告
    print("\n" + "="*70)
    print("  班级成绩分析报告")
    print("="*70)
    
    stats = manager.get_statistics()
    print(f"\n基本信息:")
    print(f"  班级人数: {stats['total_students']} 人")
    print(f"  平均年龄: {stats['average_age']} 岁")
    print(f"  优秀学生: {stats['excellent_students']} 人")
    
    print("\n成绩排名:")
    for rank, (student, avg) in enumerate(manager.get_top_students(10), 1):
        mark = "⭐" if student.is_excellent_student() else "  "
        failing = len(student.get_failing_subjects())
        failing_note = f" (有{failing}门不及格)" if failing > 0 else ""
        print(f"  {mark} {rank}. {student.name:<6} 平均分: {avg:5.2f}{failing_note}")
    
    print("\n课程平均分统计:")
    all_subjects = {}
    for student in manager.get_all_students():
        for subject, score in student.scores.items():
            if subject not in all_subjects:
                all_subjects[subject] = []
            all_subjects[subject].append(score)
    
    for subject, scores in sorted(all_subjects.items()):
        avg = sum(scores) / len(scores)
        print(f"  {subject:<12} 平均分: {avg:.2f}")
    
    manager.save_data()
    print(f"\n报告数据已保存到: comprehensive_demo.json")


def cleanup_demo_files():
    """清理演示文件"""
    demo_files = ["demo_students.json", "demo_export.csv", 
                  "comprehensive_demo.json", "test_students.json"]
    
    print("\n清理演示文件...")
    for file in demo_files:
        if os.path.exists(file):
            try:
                os.remove(file)
                print(f"  ✓ 已删除: {file}")
            except Exception as e:
                print(f"  ✗ 删除失败: {file} - {e}")


def main():
    """主函数"""
    print("\n")
    print("╔" + "="*68 + "╗")
    print("║" + " "*20 + "学生管理系统 - 功能演示" + " "*24 + "║")
    print("╚" + "="*68 + "╝")
    print(f"\n演示时间: {format_timestamp()}")
    
    try:
        # 1. 学生基本功能
        demo_student_basic()
        
        # 2. 学生管理器功能
        manager, demo_file = demo_student_manager()
        
        # 3. 搜索和查询
        demo_search_and_query(manager)
        
        # 4. 统计分析
        demo_statistics(manager)
        
        # 5. 数据导出
        demo_data_export(manager, demo_file)
        
        # 6. 更新和删除
        demo_update_and_delete(manager)
        
        # 7. 综合报告
        demo_comprehensive_report()
        
        # 演示结束
        print_separator("演示完成")
        print("\n✓ 所有功能演示成功!")
        print("\n提示:")
        print("  - 运行 'python main.py' 启动交互式管理系统")
        print("  - 运行 'python test_student_system.py' 执行单元测试")
        print("  - 查看 'README.md' 了解详细文档")
        
        # 询问是否清理演示文件
        print("\n" + "="*70)
        cleanup = input("是否清理演示产生的临时文件? (y/n): ").strip().lower()
        if cleanup == 'y':
            cleanup_demo_files()
            print("\n✓ 清理完成")
        else:
            print("\n保留演示文件，可供查看")
        
    except Exception as e:
        print(f"\n错误: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()

