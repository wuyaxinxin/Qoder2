#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: test_student_system.py
作者: 开发者
创建日期: 2025-10-13
版本: 1.0
描述: 学生管理系统测试脚本
"""

import unittest
import os
from student import Student
from student_manager import StudentManager
from validator import Validator


class TestStudent(unittest.TestCase):
    """测试Student类"""
    
    def setUp(self):
        """每个测试前的准备"""
        self.student = Student("张三", 20, "2021001", "计算机科学")
    
    def test_student_creation(self):
        """测试学生对象创建"""
        self.assertEqual(self.student.name, "张三")
        self.assertEqual(self.student.age, 20)
        self.assertEqual(self.student.student_id, "2021001")
        self.assertEqual(self.student.major, "计算机科学")
    
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
        
        # 删除不存在的科目
        self.assertFalse(self.student.remove_score("物理"))
    
    def test_average_score(self):
        """测试平均分计算"""
        self.assertEqual(self.student.get_average_score(), 0.0)
        
        self.student.add_score("数学", 90)
        self.student.add_score("英语", 80)
        self.assertEqual(self.student.get_average_score(), 85.0)
    
    def test_highest_lowest_score(self):
        """测试最高分和最低分"""
        self.assertIsNone(self.student.get_highest_score())
        self.assertIsNone(self.student.get_lowest_score())
        
        self.student.add_score("数学", 90)
        self.student.add_score("英语", 80)
        self.student.add_score("物理", 95)
        
        highest = self.student.get_highest_score()
        self.assertEqual(highest[0], "物理")
        self.assertEqual(highest[1], 95)
        
        lowest = self.student.get_lowest_score()
        self.assertEqual(lowest[0], "英语")
        self.assertEqual(lowest[1], 80)
    
    def test_passing_subjects(self):
        """测试及格科目"""
        self.student.add_score("数学", 90)
        self.student.add_score("英语", 55)
        self.student.add_score("物理", 75)
        
        passing = self.student.get_passing_subjects()
        self.assertEqual(len(passing), 2)
        self.assertIn("数学", passing)
        self.assertIn("物理", passing)
        
        failing = self.student.get_failing_subjects()
        self.assertEqual(len(failing), 1)
        self.assertIn("英语", failing)
    
    def test_excellent_student(self):
        """测试优秀学生判断"""
        self.assertFalse(self.student.is_excellent_student())
        
        self.student.add_score("数学", 90)
        self.student.add_score("英语", 88)
        self.student.add_score("物理", 92)
        
        self.assertTrue(self.student.is_excellent_student())
        
        # 有不及格科目不是优秀学生
        self.student.add_score("化学", 55)
        self.assertFalse(self.student.is_excellent_student())


class TestStudentManager(unittest.TestCase):
    """测试StudentManager类"""
    
    def setUp(self):
        """每个测试前的准备"""
        self.test_file = "test_students.json"
        self.manager = StudentManager(self.test_file)
        self.manager.clear_all_data()
    
    def tearDown(self):
        """每个测试后的清理"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def test_add_student(self):
        """测试添加学生"""
        self.assertTrue(self.manager.add_student("张三", 20, "2021001", "计算机"))
        self.assertEqual(self.manager.get_student_count(), 1)
        
        # 重复学号
        self.assertFalse(self.manager.add_student("李四", 19, "2021001", "数学"))
        self.assertEqual(self.manager.get_student_count(), 1)
    
    def test_remove_student(self):
        """测试删除学生"""
        self.manager.add_student("张三", 20, "2021001", "计算机")
        self.assertTrue(self.manager.remove_student("2021001"))
        self.assertEqual(self.manager.get_student_count(), 0)
        
        # 删除不存在的学生
        self.assertFalse(self.manager.remove_student("2021999"))
    
    def test_get_student(self):
        """测试获取学生"""
        self.manager.add_student("张三", 20, "2021001", "计算机")
        student = self.manager.get_student("2021001")
        
        self.assertIsNotNone(student)
        self.assertEqual(student.name, "张三")
        
        # 获取不存在的学生
        self.assertIsNone(self.manager.get_student("2021999"))
    
    def test_update_student(self):
        """测试更新学生信息"""
        self.manager.add_student("张三", 20, "2021001", "计算机")
        self.assertTrue(self.manager.update_student_info("2021001", name="张三丰", age=21))
        
        student = self.manager.get_student("2021001")
        self.assertEqual(student.name, "张三丰")
        self.assertEqual(student.age, 21)
    
    def test_search_students(self):
        """测试搜索学生"""
        self.manager.add_student("张三", 20, "2021001", "计算机")
        self.manager.add_student("李四", 19, "2021002", "数学")
        self.manager.add_student("王五", 21, "2021003", "计算机")
        
        # 按姓名搜索
        results = self.manager.search_students("张")
        self.assertEqual(len(results), 1)
        
        # 按专业搜索
        results = self.manager.search_students("计算机")
        self.assertEqual(len(results), 2)
    
    def test_statistics(self):
        """测试统计信息"""
        self.manager.add_student("张三", 20, "2021001", "计算机")
        self.manager.add_student("李四", 22, "2021002", "数学")
        
        stats = self.manager.get_statistics()
        self.assertEqual(stats['total_students'], 2)
        self.assertEqual(stats['average_age'], 21.0)
        self.assertEqual(stats['major_distribution']['计算机'], 1)
        self.assertEqual(stats['major_distribution']['数学'], 1)
    
    def test_top_students(self):
        """测试成绩排名"""
        # 添加学生并录入成绩
        self.manager.add_student("张三", 20, "2021001", "计算机")
        self.manager.add_student("李四", 19, "2021002", "数学")
        
        student1 = self.manager.get_student("2021001")
        student1.add_score("数学", 90)
        student1.add_score("英语", 85)
        
        student2 = self.manager.get_student("2021002")
        student2.add_score("数学", 95)
        student2.add_score("英语", 92)
        
        top_students = self.manager.get_top_students(5)
        self.assertEqual(len(top_students), 2)
        
        # 第一名应该是李四
        self.assertEqual(top_students[0][0].name, "李四")
    
    def test_save_and_load(self):
        """测试数据保存和加载"""
        self.manager.add_student("张三", 20, "2021001", "计算机")
        student = self.manager.get_student("2021001")
        student.add_score("数学", 90)
        
        self.assertTrue(self.manager.save_data())
        
        # 创建新管理器并加载数据
        new_manager = StudentManager(self.test_file)
        self.assertEqual(new_manager.get_student_count(), 1)
        
        loaded_student = new_manager.get_student("2021001")
        self.assertIsNotNone(loaded_student)
        self.assertEqual(loaded_student.name, "张三")
        self.assertEqual(loaded_student.get_score("数学"), 90)


class TestValidator(unittest.TestCase):
    """测试Validator类"""
    
    def test_is_empty(self):
        """测试空值检查"""
        self.assertTrue(Validator.is_empty(None))
        self.assertTrue(Validator.is_empty(""))
        self.assertTrue(Validator.is_empty([]))
        self.assertFalse(Validator.is_empty("test"))
    
    def test_validate_student_id(self):
        """测试学号验证"""
        self.assertTrue(Validator.validate_student_id("2021001"))
        self.assertTrue(Validator.validate_student_id("2025999"))
        self.assertFalse(Validator.validate_student_id("202101"))  # 太短
        self.assertFalse(Validator.validate_student_id("1921001"))  # 年份错误
    
    def test_validate_score(self):
        """测试成绩验证"""
        self.assertTrue(Validator.validate_score(85))
        self.assertTrue(Validator.validate_score(0))
        self.assertTrue(Validator.validate_score(100))
        self.assertFalse(Validator.validate_score(-10))
        self.assertFalse(Validator.validate_score(150))
        self.assertFalse(Validator.validate_score("abc"))
    
    def test_validate_age(self):
        """测试年龄验证"""
        self.assertTrue(Validator.validate_age(20))
        self.assertTrue(Validator.validate_age(18))
        self.assertFalse(Validator.validate_age(-5))
        self.assertFalse(Validator.validate_age(200))
        self.assertFalse(Validator.validate_age("abc"))


def run_tests():
    """运行所有测试"""
    print("="*70)
    print(" "*20 + "学生管理系统测试")
    print("="*70)
    
    # 创建测试套件
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # 添加测试
    suite.addTests(loader.loadTestsFromTestCase(TestStudent))
    suite.addTests(loader.loadTestsFromTestCase(TestStudentManager))
    suite.addTests(loader.loadTestsFromTestCase(TestValidator))
    
    # 运行测试
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # 显示测试结果
    print("\n" + "="*70)
    print("测试结果汇总:")
    print(f"运行测试数: {result.testsRun}")
    print(f"成功: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"失败: {len(result.failures)}")
    print(f"错误: {len(result.errors)}")
    print("="*70)
    
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    exit(0 if success else 1)
