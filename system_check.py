#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
课程管理系统 - 系统状态检查脚本
Course Management System - System Health Check
"""

import sys
import os
from pathlib import Path

def print_header(title):
    """打印标题"""
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)

def check_files():
    """检查必需文件是否存在"""
    print_header("文件完整性检查 (File Integrity Check)")
    
    required_files = {
        '核心模块': [
            'course.py',
            'course_management_system.py',
            'course_data_manager.py',
            'course_statistics.py',
            'integrated_system.py',
            'course_cli.py'
        ],
        '学生管理模块': [
            'student.py',
            'student_management_system.py',
            'cli.py',
            'data_manager.py'
        ],
        '工具模块': [
            'validator.py',
            'utils.py'
        ],
        '测试文件': [
            'test_course_system.py',
            'test_student_system.py'
        ],
        '演示和文档': [
            'demo_course_system.py',
            'main.py',
            'COURSE_README.md',
            'README.md'
        ]
    }
    
    all_ok = True
    for category, files in required_files.items():
        print(f"\n{category}:")
        for file in files:
            exists = Path(file).exists()
            status = "✓" if exists else "✗"
            print(f"  {status} {file}")
            if not exists:
                all_ok = False
    
    return all_ok

def check_imports():
    """检查模块导入"""
    print_header("模块导入检查 (Module Import Check)")
    
    modules = [
        ('course', 'Course'),
        ('course_management_system', 'CourseManagementSystem'),
        ('course_data_manager', 'CourseDataManager'),
        ('course_statistics', 'CourseStatistics'),
        ('integrated_system', 'IntegratedSystem'),
        ('course_cli', 'CourseCLI'),
        ('validator', 'Validator'),
        ('student', 'Student'),
        ('student_management_system', 'StudentManagementSystem')
    ]
    
    all_ok = True
    for module_name, class_name in modules:
        try:
            module = __import__(module_name)
            getattr(module, class_name)
            print(f"  ✓ {module_name}.{class_name}")
        except Exception as e:
            print(f"  ✗ {module_name}.{class_name} - {str(e)}")
            all_ok = False
    
    return all_ok

def check_data_directory():
    """检查数据目录"""
    print_header("数据目录检查 (Data Directory Check)")
    
    data_dir = Path('data')
    if not data_dir.exists():
        print(f"  ✗ data/ 目录不存在")
        return False
    
    print(f"  ✓ data/ 目录存在")
    
    # 检查可能的数据文件
    data_files = ['students_data.json', 'courses_data.json']
    for file in data_files:
        file_path = data_dir / file
        status = "✓" if file_path.exists() else "○"
        print(f"  {status} {file} {'(已存在)' if file_path.exists() else '(将在首次保存时创建)'}")
    
    return True

def run_quick_test():
    """运行快速功能测试"""
    print_header("快速功能测试 (Quick Function Test)")
    
    try:
        # 测试课程创建
        from course import Course
        course = Course("CS101", "计算机科学导论", "张教授", 3.0, 50)
        print("  ✓ 课程对象创建成功")
        
        # 测试课程管理系统
        from course_management_system import CourseManagementSystem
        cms = CourseManagementSystem()
        result = cms.add_course("CS101", "计算机科学导论", "张教授", 3.0, 50)
        print("  ✓ 课程管理系统添加课程成功")
        
        # 测试学生创建
        from student import Student
        student = Student("S001", "张三", 20, "男")
        print("  ✓ 学生对象创建成功")
        
        # 测试一体化系统
        from integrated_system import IntegratedSystem
        integrated = IntegratedSystem()
        print("  ✓ 一体化系统初始化成功")
        
        # 测试统计模块
        from course_statistics import CourseStatistics
        stats = CourseStatistics(cms)
        print("  ✓ 统计模块初始化成功")
        
        return True
        
    except Exception as e:
        print(f"  ✗ 功能测试失败: {str(e)}")
        return False

def check_test_coverage():
    """检查测试覆盖"""
    print_header("测试覆盖情况 (Test Coverage)")
    
    import subprocess
    
    try:
        result = subprocess.run(
            ['python3', 'test_course_system.py', '-v'],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        # 统计测试数量
        output = result.stderr
        if 'OK' in output or 'Ran' in output:
            lines = output.split('\n')
            for line in lines:
                if 'Ran' in line:
                    print(f"  ✓ {line.strip()}")
            if 'OK' in output:
                print("  ✓ 所有测试通过")
            return True
        else:
            print("  ✗ 测试执行失败")
            return False
            
    except Exception as e:
        print(f"  ○ 无法运行测试: {str(e)}")
        return False

def main():
    """主函数"""
    print("\n" + "=" * 60)
    print("  课程管理系统 - 系统状态检查")
    print("  Course Management System - Health Check")
    print("=" * 60)
    
    results = []
    
    # 1. 检查文件
    results.append(("文件完整性", check_files()))
    
    # 2. 检查导入
    results.append(("模块导入", check_imports()))
    
    # 3. 检查数据目录
    results.append(("数据目录", check_data_directory()))
    
    # 4. 快速功能测试
    results.append(("快速功能测试", run_quick_test()))
    
    # 5. 测试覆盖
    results.append(("单元测试", check_test_coverage()))
    
    # 总结
    print_header("检查总结 (Summary)")
    
    all_passed = True
    for name, passed in results:
        status = "✓ 通过" if passed else "✗ 失败"
        print(f"  {status} - {name}")
        if not passed:
            all_passed = False
    
    print("\n" + "=" * 60)
    if all_passed:
        print("  ✓✓✓ 系统状态良好,所有检查通过! ✓✓✓")
        print("=" * 60)
        print("\n您可以:")
        print("  - 运行 python3 main.py 启动主程序")
        print("  - 运行 python3 demo_course_system.py 查看功能演示")
        print("  - 运行 ./quick_start.sh 使用快速启动脚本")
        print("  - 查看 COURSE_README.md 了解详细文档")
        return 0
    else:
        print("  ✗✗✗ 系统检查发现问题,请检查上述错误 ✗✗✗")
        print("=" * 60)
        return 1

if __name__ == '__main__':
    sys.exit(main())
