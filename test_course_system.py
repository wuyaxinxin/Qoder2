#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: test_course_system.py
作者: 开发者
创建日期: 2025-10-16
版本: 1.0
描述: 课程管理系统单元测试
      包含Course类、CourseManagementSystem类和集成测试
"""

import unittest
import os
import json
from datetime import datetime
from course import Course
from course_management_system import CourseManagementSystem
from course_statistics import CourseStatistics
from course_data_manager import CourseDataManager
from integrated_system import IntegratedSystem


class TestCourse(unittest.TestCase):
    """Course类测试"""
    
    def setUp(self):
        """测试前准备"""
        self.course = Course(
            course_id="CS101",
            course_name="数据结构与算法",
            teacher="张教授",
            credit=3.0,
            capacity=60,
            description="数据结构基础课程",
            semester="2024春季",
            schedule="周一3-4节"
        )
    
    def test_course_creation(self):
        """测试课程创建"""
        self.assertEqual(self.course.course_id, "CS101")
        self.assertEqual(self.course.course_name, "数据结构与算法")
        self.assertEqual(self.course.teacher, "张教授")
        self.assertEqual(self.course.credit, 3.0)
        self.assertEqual(self.course.capacity, 60)
        self.assertEqual(self.course.enrolled_count, 0)
    
    def test_add_student(self):
        """测试添加学生"""
        result = self.course.add_student("2021001")
        self.assertTrue(result)
        self.assertEqual(self.course.enrolled_count, 1)
        self.assertTrue(self.course.has_student("2021001"))
    
    def test_add_duplicate_student(self):
        """测试重复添加学生"""
        self.course.add_student("2021001")
        result = self.course.add_student("2021001")
        self.assertFalse(result)
        self.assertEqual(self.course.enrolled_count, 1)
    
    def test_remove_student(self):
        """测试移除学生"""
        self.course.add_student("2021001")
        result = self.course.remove_student("2021001")
        self.assertTrue(result)
        self.assertEqual(self.course.enrolled_count, 0)
        self.assertFalse(self.course.has_student("2021001"))
    
    def test_is_full(self):
        """测试课程满员检查"""
        # 添加学生至满员
        for i in range(60):
            self.course.add_student(f"2021{i:03d}")
        
        self.assertTrue(self.course.is_full())
        
        # 尝试再添加学生应失败
        result = self.course.add_student("2021999")
        self.assertFalse(result)
    
    def test_enrollment_rate(self):
        """测试选课率计算"""
        self.course.add_student("2021001")
        self.course.add_student("2021002")
        self.course.add_student("2021003")
        
        rate = self.course.get_enrollment_rate()
        expected_rate = (3 / 60) * 100
        self.assertAlmostEqual(rate, expected_rate, places=2)
    
    def test_available_seats(self):
        """测试剩余容量"""
        self.course.add_student("2021001")
        self.course.add_student("2021002")
        
        available = self.course.get_available_seats()
        self.assertEqual(available, 58)
    
    def test_to_dict(self):
        """测试序列化为字典"""
        self.course.add_student("2021001")
        data = self.course.to_dict()
        
        self.assertIsInstance(data, dict)
        self.assertEqual(data['course_id'], "CS101")
        self.assertEqual(data['course_name'], "数据结构与算法")
        self.assertIn("2021001", data['enrolled_students'])
    
    def test_from_dict(self):
        """测试从字典反序列化"""
        self.course.add_student("2021001")
        data = self.course.to_dict()
        
        restored_course = Course.from_dict(data)
        
        self.assertEqual(restored_course.course_id, self.course.course_id)
        self.assertEqual(restored_course.course_name, self.course.course_name)
        self.assertEqual(restored_course.enrolled_count, self.course.enrolled_count)
        self.assertTrue(restored_course.has_student("2021001"))


class TestCourseManagementSystem(unittest.TestCase):
    """CourseManagementSystem类测试"""
    
    def setUp(self):
        """测试前准备"""
        self.system = CourseManagementSystem()
    
    def test_add_course(self):
        """测试添加课程"""
        result = self.system.add_course(
            course_id="CS101",
            course_name="数据结构与算法",
            teacher="张教授",
            credit=3.0,
            capacity=60
        )
        self.assertTrue(result)
        self.assertEqual(self.system.get_course_count(), 1)
    
    def test_add_duplicate_course(self):
        """测试重复添加课程"""
        self.system.add_course("CS101", "数据结构", "张教授", 3.0, 60)
        result = self.system.add_course("CS101", "算法", "李教授", 2.0, 50)
        self.assertFalse(result)
        self.assertEqual(self.system.get_course_count(), 1)
    
    def test_remove_course(self):
        """测试删除课程"""
        self.system.add_course("CS101", "数据结构", "张教授", 3.0, 60)
        result = self.system.remove_course("CS101")
        self.assertTrue(result)
        self.assertEqual(self.system.get_course_count(), 0)
    
    def test_remove_course_with_students(self):
        """测试删除有学生选课的课程"""
        self.system.add_course("CS101", "数据结构", "张教授", 3.0, 60)
        self.system.enroll_student("2021001", "CS101")
        
        result = self.system.remove_course("CS101")
        self.assertFalse(result)
        self.assertEqual(self.system.get_course_count(), 1)
    
    def test_update_course(self):
        """测试更新课程"""
        self.system.add_course("CS101", "数据结构", "张教授", 3.0, 60)
        
        result = self.system.update_course(
            "CS101",
            course_name="数据结构与算法",
            teacher="李教授"
        )
        
        self.assertTrue(result)
        course = self.system.get_course("CS101")
        self.assertEqual(course.course_name, "数据结构与算法")
        self.assertEqual(course.teacher, "李教授")
    
    def test_enroll_student(self):
        """测试学生选课"""
        self.system.add_course("CS101", "数据结构", "张教授", 3.0, 60)
        result = self.system.enroll_student("2021001", "CS101")
        
        self.assertTrue(result)
        course = self.system.get_course("CS101")
        self.assertEqual(course.enrolled_count, 1)
    
    def test_drop_course(self):
        """测试学生退课"""
        self.system.add_course("CS101", "数据结构", "张教授", 3.0, 60)
        self.system.enroll_student("2021001", "CS101")
        
        result = self.system.drop_course("2021001", "CS101")
        
        self.assertTrue(result)
        course = self.system.get_course("CS101")
        self.assertEqual(course.enrolled_count, 0)
    
    def test_set_course_score(self):
        """测试设置课程成绩"""
        self.system.add_course("CS101", "数据结构", "张教授", 3.0, 60)
        self.system.enroll_student("2021001", "CS101")
        
        result = self.system.set_course_score("2021001", "CS101", 90.0)
        
        self.assertTrue(result)
        score = self.system.get_course_score("2021001", "CS101")
        self.assertEqual(score, 90.0)
    
    def test_search_courses(self):
        """测试搜索课程"""
        self.system.add_course("CS101", "数据结构", "张教授", 3.0, 60)
        self.system.add_course("CS102", "算法设计", "张教授", 2.5, 50)
        self.system.add_course("MATH201", "高等数学", "李教授", 4.0, 80)
        
        # 按教师搜索
        results = self.system.search_courses(teacher="张教授")
        self.assertEqual(len(results), 2)
        
        # 按关键词搜索
        results = self.system.search_courses(keyword="数据")
        self.assertEqual(len(results), 1)


class TestCourseStatistics(unittest.TestCase):
    """CourseStatistics类测试"""
    
    def setUp(self):
        """测试前准备"""
        self.course_system = CourseManagementSystem()
        self.statistics = CourseStatistics(self.course_system)
        
        # 准备测试数据
        self.course_system.add_course("CS101", "数据结构", "张教授", 3.0, 60)
        self.course_system.enroll_student("2021001", "CS101")
        self.course_system.enroll_student("2021002", "CS101")
        self.course_system.enroll_student("2021003", "CS101")
        
        # 设置成绩
        self.course_system.set_course_score("2021001", "CS101", 95.0)
        self.course_system.set_course_score("2021002", "CS101", 85.0)
        self.course_system.set_course_score("2021003", "CS101", 75.0)
    
    def test_course_score_statistics(self):
        """测试课程成绩统计"""
        stats = self.statistics.get_course_score_statistics("CS101")
        
        self.assertTrue(stats['has_scores'])
        self.assertEqual(stats['total_students'], 3)
        self.assertAlmostEqual(stats['average_score'], 85.0, places=1)
        self.assertEqual(stats['max_score'], 95.0)
        self.assertEqual(stats['min_score'], 75.0)
    
    def test_student_credit_statistics(self):
        """测试学生学分统计"""
        # 添加多门课程
        self.course_system.add_course("CS102", "算法", "李教授", 2.5, 50)
        self.course_system.enroll_student("2021001", "CS102")
        self.course_system.set_course_score("2021001", "CS102", 88.0)
        
        stats = self.statistics.get_student_credit_statistics("2021001")
        
        self.assertEqual(stats['total_courses'], 2)
        self.assertAlmostEqual(stats['total_credits'], 5.5, places=1)
        self.assertGreater(stats['gpa'], 0)
    
    def test_popular_courses(self):
        """测试热门课程排行"""
        self.course_system.add_course("CS102", "算法", "李教授", 2.5, 50)
        self.course_system.enroll_student("2021004", "CS102")
        
        popular = self.statistics.get_popular_courses(top_n=10)
        
        self.assertGreater(len(popular), 0)
        # CS101应该排在前面（3个学生）
        self.assertEqual(popular[0]['course_id'], "CS101")


class TestCourseDataManager(unittest.TestCase):
    """CourseDataManager类测试"""
    
    def setUp(self):
        """测试前准备"""
        self.test_file = "test_courses.json"
        self.data_manager = CourseDataManager(data_dir="data", filename=self.test_file)
        self.course_system = CourseManagementSystem()
        
        # 添加测试数据
        self.course_system.add_course("CS101", "数据结构", "张教授", 3.0, 60)
        self.course_system.enroll_student("2021001", "CS101")
    
    def tearDown(self):
        """测试后清理"""
        test_path = os.path.join("data", self.test_file)
        if os.path.exists(test_path):
            os.remove(test_path)
    
    def test_save_and_load(self):
        """测试保存和加载数据"""
        # 保存数据
        save_result = self.data_manager.save_courses(self.course_system)
        self.assertTrue(save_result)
        
        # 创建新系统并加载数据
        new_system = CourseManagementSystem()
        load_result = self.data_manager.load_courses(new_system)
        self.assertTrue(load_result)
        
        # 验证数据
        self.assertEqual(new_system.get_course_count(), 1)
        course = new_system.get_course("CS101")
        self.assertIsNotNone(course)
        self.assertEqual(course.course_name, "数据结构")
        self.assertEqual(course.enrolled_count, 1)


class TestIntegratedSystem(unittest.TestCase):
    """IntegratedSystem集成测试"""
    
    def setUp(self):
        """测试前准备"""
        self.system = IntegratedSystem(
            student_data_file="test_students.json",
            course_data_file="test_courses.json"
        )
        
        # 添加测试学生
        self.system.student_system.add_student("张三", 20, "2021001", "计算机科学")
        self.system.student_system.add_student("李四", 21, "2021002", "软件工程")
        
        # 添加测试课程
        self.system.course_system.add_course("CS101", "数据结构", "张教授", 3.0, 60)
    
    def tearDown(self):
        """测试后清理"""
        for filename in ["test_students.json", "test_courses.json"]:
            test_path = os.path.join("data", filename)
            if os.path.exists(test_path):
                os.remove(test_path)
    
    def test_integrated_enrollment(self):
        """测试集成选课功能"""
        result = self.system.enroll_student_to_course("2021001", "CS101")
        self.assertTrue(result)
        
        # 验证选课记录
        course_info = self.system.get_student_course_info("2021001")
        self.assertEqual(len(course_info['enrolled_courses']), 1)
    
    def test_integrated_score(self):
        """测试集成成绩录入"""
        self.system.enroll_student_to_course("2021001", "CS101")
        result = self.system.set_course_score_integrated("2021001", "CS101", 90.0)
        
        self.assertTrue(result)
        
        # 验证成绩同步
        course_score = self.system.course_system.get_course_score("2021001", "CS101")
        self.assertEqual(course_score, 90.0)
        
        # 验证学生成绩
        student = self.system.student_system.get_student("2021001")
        self.assertGreater(len(student.scores), 0)
    
    def test_student_transcript(self):
        """测试学生成绩单生成"""
        self.system.enroll_student_to_course("2021001", "CS101")
        self.system.set_course_score_integrated("2021001", "CS101", 90.0)
        
        transcript = self.system.get_student_transcript("2021001")
        
        self.assertIsInstance(transcript, str)
        self.assertIn("张三", transcript)
        self.assertIn("数据结构", transcript)
        self.assertIn("90.0", transcript)


def run_tests():
    """运行所有测试"""
    # 创建测试套件
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # 添加测试类
    suite.addTests(loader.loadTestsFromTestCase(TestCourse))
    suite.addTests(loader.loadTestsFromTestCase(TestCourseManagementSystem))
    suite.addTests(loader.loadTestsFromTestCase(TestCourseStatistics))
    suite.addTests(loader.loadTestsFromTestCase(TestCourseDataManager))
    suite.addTests(loader.loadTestsFromTestCase(TestIntegratedSystem))
    
    # 运行测试
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # 返回测试结果
    return result.wasSuccessful()


if __name__ == "__main__":
    print("="*70)
    print("课程管理系统单元测试")
    print("="*70)
    
    success = run_tests()
    
    print("\n" + "="*70)
    if success:
        print("✓ 所有测试通过!")
    else:
        print("✗ 部分测试失败，请检查错误信息")
    print("="*70)
