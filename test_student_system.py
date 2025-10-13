#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: test_student_system.py
作者: 开发者
创建日期: 2025-10-13
版本: 1.0
描述: 学生管理系统单元测试
      测试所有主要功能模块
"""

import unittest
import os
import json
import tempfile
from datetime import datetime
from student import Student
from student_management_system import StudentManagementSystem
from validator import Validator
from data_manager import DataManager


class TestStudent(unittest.TestCase):
    """测试Student类"""
    
    def setUp(self):
        """测试前准备"""
        self.student = Student("张三", 20, "2021001", "计算机科学")
    
    def test_student_creation(self):
        """测试学生对象创建"""
        self.assertEqual(self.student.name, "张三")
        self.assertEqual(self.student.age, 20)
        self.assertEqual(self.student.student_id, "2021001")
        self.assertEqual(self.student.major, "计算机科学")
        self.assertEqual(len(self.student.scores), 0)
    
    def test_add_score(self):
        """测试添加成绩"""
        self.assertTrue(self.student.add_score("数学", 95))
        self.assertEqual(self.student.get_score("数学"), 95)
        
        # 测试无效成绩
        self.assertFalse(self.student.add_score("物理", 150))
        self.assertFalse(self.student.add_score("化学", -10))
    
    def test_remove_score(self):
        """测试删除成绩"""
        self.student.add_score("数学", 95)
        self.assertTrue(self.student.remove_score("数学"))
        self.assertIsNone(self.student.get_score("数学"))
        
        # 测试删除不存在的成绩
        self.assertFalse(self.student.remove_score("英语"))
    
    def test_get_average_score(self):
        """测试平均分计算"""
        self.assertEqual(self.student.get_average_score(), 0.0)
        
        self.student.add_score("数学", 90)
        self.student.add_score("英语", 80)
        self.assertEqual(self.student.get_average_score(), 85.0)
    
    def test_get_highest_score(self):
        """测试最高分获取"""
        self.assertIsNone(self.student.get_highest_score())
        
        self.student.add_score("数学", 90)
        self.student.add_score("英语", 95)
        self.student.add_score("物理", 85)
        
        highest = self.student.get_highest_score()
        self.assertEqual(highest[0], "英语")
        self.assertEqual(highest[1], 95)
    
    def test_get_lowest_score(self):
        """测试最低分获取"""
        self.assertIsNone(self.student.get_lowest_score())
        
        self.student.add_score("数学", 90)
        self.student.add_score("英语", 95)
        self.student.add_score("物理", 85)
        
        lowest = self.student.get_lowest_score()
        self.assertEqual(lowest[0], "物理")
        self.assertEqual(lowest[1], 85)
    
    def test_is_excellent_student(self):
        """测试优秀学生判断"""
        self.assertFalse(self.student.is_excellent_student())
        
        # 平均分高但有不及格科目
        self.student.add_score("数学", 95)
        self.student.add_score("英语", 55)
        self.assertFalse(self.student.is_excellent_student())
        
        # 优秀学生
        self.student.add_score("英语", 85)
        self.assertTrue(self.student.is_excellent_student())


class TestValidator(unittest.TestCase):
    """测试Validator类"""
    
    def test_is_empty(self):
        """测试空值检查"""
        self.assertTrue(Validator.is_empty(None))
        self.assertTrue(Validator.is_empty(""))
        self.assertTrue(Validator.is_empty([]))
        self.assertTrue(Validator.is_empty({}))
        self.assertFalse(Validator.is_empty("test"))
        self.assertFalse(Validator.is_empty([1, 2, 3]))
    
    def test_is_email(self):
        """测试邮箱验证"""
        self.assertTrue(Validator.is_email("test@example.com"))
        self.assertTrue(Validator.is_email("user.name@domain.org"))
        self.assertFalse(Validator.is_email("invalid-email"))
        self.assertFalse(Validator.is_email("@domain.com"))
        self.assertFalse(Validator.is_email("user@"))
    
    def test_validate_student_id(self):
        """测试学号验证"""
        self.assertTrue(Validator.validate_student_id("2021001"))
        self.assertTrue(Validator.validate_student_id("2023999"))
        self.assertFalse(Validator.validate_student_id("1921001"))  # 年份不对
        self.assertFalse(Validator.validate_student_id("202100"))   # 位数不够
        self.assertFalse(Validator.validate_student_id("2021abc"))  # 含字母
    
    def test_validate_score(self):
        """测试成绩验证"""
        self.assertTrue(Validator.validate_score(85))
        self.assertTrue(Validator.validate_score(100))
        self.assertTrue(Validator.validate_score(0))
        self.assertTrue(Validator.validate_score(75.5))
        self.assertFalse(Validator.validate_score(-10))
        self.assertFalse(Validator.validate_score(150))
        self.assertFalse(Validator.validate_score("abc"))
    
    def test_validate_age(self):
        """测试年龄验证"""
        self.assertTrue(Validator.validate_age(20))
        self.assertTrue(Validator.validate_age(0))
        self.assertTrue(Validator.validate_age(150))
        self.assertFalse(Validator.validate_age(-1))
        self.assertFalse(Validator.validate_age(200))
        self.assertFalse(Validator.validate_age("abc"))


class TestStudentManagementSystem(unittest.TestCase):
    """测试StudentManagementSystem类"""
    
    def setUp(self):
        """测试前准备"""
        # 创建临时文件用于测试
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.json')
        self.temp_file.close()
        self.system = StudentManagementSystem(self.temp_file.name)
    
    def tearDown(self):
        """测试后清理"""
        if os.path.exists(self.temp_file.name):
            os.unlink(self.temp_file.name)
    
    def test_add_student(self):
        """测试添加学生"""
        self.assertTrue(self.system.add_student("张三", 20, "2021001", "计算机科学"))
        self.assertEqual(self.system.get_student_count(), 1)
        
        # 测试重复学号
        self.assertFalse(self.system.add_student("李四", 19, "2021001", "数学"))
        self.assertEqual(self.system.get_student_count(), 1)
        
        # 测试无效数据
        self.assertFalse(self.system.add_student("", 20, "2021002", "物理"))
        self.assertFalse(self.system.add_student("王五", 200, "2021003", "化学"))
        self.assertFalse(self.system.add_student("赵六", 20, "invalid", "生物"))
    
    def test_remove_student(self):
        """测试删除学生"""
        self.system.add_student("张三", 20, "2021001", "计算机科学")
        self.assertTrue(self.system.remove_student("2021001"))
        self.assertEqual(self.system.get_student_count(), 0)
        
        # 测试删除不存在的学生
        self.assertFalse(self.system.remove_student("2021999"))
    
    def test_update_student(self):
        """测试更新学生信息"""
        self.system.add_student("张三", 20, "2021001", "计算机科学")
        
        # 更新姓名
        self.assertTrue(self.system.update_student("2021001", name="张三丰"))
        student = self.system.get_student("2021001")
        self.assertEqual(student.name, "张三丰")
        
        # 更新年龄
        self.assertTrue(self.system.update_student("2021001", age=21))
        self.assertEqual(student.age, 21)
        
        # 更新专业
        self.assertTrue(self.system.update_student("2021001", major="软件工程"))
        self.assertEqual(student.major, "软件工程")
        
        # 测试更新不存在的学生
        self.assertFalse(self.system.update_student("2021999", name="测试"))
    
    def test_search_students(self):
        """测试搜索学生"""
        self.system.add_student("张三", 20, "2021001", "计算机科学")
        self.system.add_student("李四", 19, "2021002", "计算机科学")
        self.system.add_student("王五", 21, "2021003", "数学")
        
        # 按姓名搜索
        results = self.system.search_students(name="张")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "张三")
        
        # 按专业搜索
        results = self.system.search_students(major="计算机")
        self.assertEqual(len(results), 2)
        
        # 按年龄范围搜索
        results = self.system.search_students(min_age=20, max_age=21)
        self.assertEqual(len(results), 2)
    
    def test_add_student_score(self):
        """测试添加学生成绩"""
        self.system.add_student("张三", 20, "2021001", "计算机科学")
        
        self.assertTrue(self.system.add_student_score("2021001", "数学", 95))
        student = self.system.get_student("2021001")
        self.assertEqual(student.get_score("数学"), 95)
        
        # 测试给不存在的学生添加成绩
        self.assertFalse(self.system.add_student_score("2021999", "英语", 85))
    
    def test_get_top_students(self):
        """测试获取成绩排名"""
        self.system.add_student("张三", 20, "2021001", "计算机科学")
        self.system.add_student("李四", 19, "2021002", "数学")
        self.system.add_student("王五", 21, "2021003", "物理")
        
        self.system.add_student_score("2021001", "数学", 95)
        self.system.add_student_score("2021001", "英语", 85)  # 平均分90
        
        self.system.add_student_score("2021002", "数学", 88)
        self.system.add_student_score("2021002", "英语", 92)  # 平均分90
        
        self.system.add_student_score("2021003", "数学", 75)  # 平均分75
        
        top_students = self.system.get_top_students(3)
        self.assertEqual(len(top_students), 3)
        
        # 检查排序（平均分相同时按学号排序）
        self.assertEqual(top_students[0][1], 90)  # 第一名平均分
        self.assertEqual(top_students[2][1], 75)  # 第三名平均分
    
    def test_get_statistics(self):
        """测试获取统计信息"""
        stats = self.system.get_statistics()
        self.assertEqual(stats['total_students'], 0)
        self.assertEqual(stats['students_with_scores'], 0)
        
        self.system.add_student("张三", 20, "2021001", "计算机科学")
        self.system.add_student("李四", 19, "2021002", "数学")
        
        stats = self.system.get_statistics()
        self.assertEqual(stats['total_students'], 2)
        self.assertEqual(stats['students_with_scores'], 0)
        
        self.system.add_student_score("2021001", "数学", 95)
        self.system.add_student_score("2021001", "英语", 85)
        
        stats = self.system.get_statistics()
        self.assertEqual(stats['students_with_scores'], 1)
        self.assertEqual(stats['total_score_records'], 2)
        self.assertEqual(stats['average_system_score'], 90.0)
    
    def test_save_and_load_data(self):
        """测试数据保存和加载"""
        # 添加测试数据
        self.system.add_student("张三", 20, "2021001", "计算机科学")
        self.system.add_student_score("2021001", "数学", 95)
        
        # 保存数据
        self.assertTrue(self.system.save_data())
        
        # 创建新的系统实例并加载数据
        new_system = StudentManagementSystem(self.temp_file.name)
        self.assertEqual(new_system.get_student_count(), 1)
        
        student = new_system.get_student("2021001")
        self.assertIsNotNone(student)
        self.assertEqual(student.name, "张三")
        self.assertEqual(student.get_score("数学"), 95)


class TestDataManager(unittest.TestCase):
    """测试DataManager类"""
    
    def setUp(self):
        """测试前准备"""
        self.temp_dir = tempfile.mkdtemp()
        self.data_manager = DataManager(self.temp_dir)
    
    def tearDown(self):
        """测试后清理"""
        import shutil
        shutil.rmtree(self.temp_dir)
    
    def test_save_and_load_json(self):
        """测试JSON保存和加载"""
        test_data = {"name": "测试", "value": 123}
        
        # 保存数据
        self.assertTrue(self.data_manager.save_json(test_data, "test.json"))
        
        # 加载数据
        loaded_data = self.data_manager.load_json("test.json")
        self.assertIsNotNone(loaded_data)
        self.assertEqual(loaded_data["name"], "测试")
        self.assertEqual(loaded_data["value"], 123)
        
        # 测试加载不存在的文件
        result = self.data_manager.load_json("nonexistent.json")
        self.assertIsNone(result)
    
    def test_backup_file(self):
        """测试文件备份"""
        test_data = {"test": "backup"}
        self.data_manager.save_json(test_data, "test.json")
        
        # 备份文件
        self.assertTrue(self.data_manager.backup_file("test.json"))
        
        # 检查备份文件是否存在
        backup_files = self.data_manager.get_file_list("backups")
        self.assertTrue(len(backup_files) > 0)
        self.assertTrue(any("test_backup_" in f for f in backup_files))
    
    def test_export_data(self):
        """测试数据导出"""
        test_data = {
            "students": {
                "2021001": {
                    "name": "张三",
                    "age": 20,
                    "student_id": "2021001",
                    "major": "计算机科学",
                    "scores": {"数学": 95, "英语": 85},
                    "created_time": "2023-01-01T00:00:00"
                }
            }
        }
        
        # 导出为JSON
        self.assertTrue(self.data_manager.export_data(test_data, "students", "json"))
        
        # 检查导出文件是否存在
        export_files = self.data_manager.get_file_list("exports")
        self.assertTrue(len(export_files) > 0)
        self.assertTrue(any("students_" in f and f.endswith(".json") for f in export_files))


def run_tests():
    """运行所有测试"""
    print("开始运行学生管理系统测试...")
    print("=" * 60)
    
    # 创建测试套件
    test_classes = [
        TestStudent,
        TestValidator,
        TestStudentManagementSystem,
        TestDataManager
    ]
    
    total_tests = 0
    total_passed = 0
    total_failed = 0
    
    for test_class in test_classes:
        print(f"\n运行 {test_class.__name__} 测试:")
        print("-" * 40)
        
        suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(suite)
        
        tests_run = result.testsRun
        failures = len(result.failures)
        errors = len(result.errors)
        passed = tests_run - failures - errors
        
        total_tests += tests_run
        total_passed += passed
        total_failed += failures + errors
        
        print(f"测试结果：运行 {tests_run} 个测试，通过 {passed} 个，失败 {failures + errors} 个")
    
    print("\n" + "=" * 60)
    print("测试总结:")
    print(f"总共运行: {total_tests} 个测试")
    print(f"通过: {total_passed} 个")
    print(f"失败: {total_failed} 个")
    print(f"成功率: {(total_passed/total_tests*100):.1f}%" if total_tests > 0 else "N/A")
    
    if total_failed == 0:
        print("\n🎉 所有测试都通过了！")
    else:
        print(f"\n⚠️  有 {total_failed} 个测试失败，请检查代码")
    
    return total_failed == 0


if __name__ == "__main__":
    run_tests()