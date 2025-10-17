#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: integrated_system.py
作者: 开发者
创建日期: 2025-10-16
版本: 1.0
描述: 学生-课程一体化管理系统
      整合学生管理和课程管理功能，提供统一的管理入口
"""

from typing import Dict, List, Optional, Any
from student_management_system import StudentManagementSystem
from course_management_system import CourseManagementSystem
from course_statistics import CourseStatistics
from course_data_manager import CourseDataManager
from data_manager import DataManager


class IntegratedSystem:
    """一体化管理系统类"""
    
    def __init__(self, student_data_file: str = "students_data.json",
                 course_data_file: str = "courses_data.json"):
        """
        初始化一体化系统
        
        Args:
            student_data_file (str): 学生数据文件
            course_data_file (str): 课程数据文件
        """
        # 初始化子系统
        self.student_system = StudentManagementSystem(student_data_file)
        self.course_system = CourseManagementSystem()
        self.course_data_manager = CourseDataManager(filename=course_data_file)
        self.course_statistics = CourseStatistics(self.course_system)
        self.data_manager = DataManager()
        
        # 加载课程数据
        self.course_data_manager.load_courses(self.course_system)
    
    def enroll_student_to_course(self, student_id: str, course_id: str) -> bool:
        """
        学生选课（验证学生存在性）
        
        Args:
            student_id (str): 学生学号
            course_id (str): 课程ID
            
        Returns:
            bool: 选课成功返回True，否则返回False
        """
        # 验证学生是否存在
        student = self.student_system.get_student(student_id)
        if not student:
            print(f"错误：学生 {student_id} 不存在")
            return False
        
        # 执行选课
        return self.course_system.enroll_student(student_id, course_id)
    
    def drop_student_course(self, student_id: str, course_id: str) -> bool:
        """
        学生退课（验证学生存在性）
        
        Args:
            student_id (str): 学生学号
            course_id (str): 课程ID
            
        Returns:
            bool: 退课成功返回True，否则返回False
        """
        # 验证学生是否存在
        student = self.student_system.get_student(student_id)
        if not student:
            print(f"错误：学生 {student_id} 不存在")
            return False
        
        # 执行退课
        return self.course_system.drop_course(student_id, course_id)
    
    def set_course_score_integrated(self, student_id: str, course_id: str, 
                                    score: float) -> bool:
        """
        录入课程成绩（同时更新学生成绩和课程成绩）
        
        Args:
            student_id (str): 学生学号
            course_id (str): 课程ID
            score (float): 成绩
            
        Returns:
            bool: 录入成功返回True，否则返回False
        """
        # 验证学生是否存在
        student = self.student_system.get_student(student_id)
        if not student:
            print(f"错误：学生 {student_id} 不存在")
            return False
        
        # 验证课程是否存在
        course = self.course_system.get_course(course_id)
        if not course:
            print(f"错误：课程 {course_id} 不存在")
            return False
        
        # 验证选课关系
        enrollment_key = f"{student_id}_{course_id}"
        if enrollment_key not in self.course_system.enrollments:
            print(f"错误：学生 {student_id} 未选课程 {course_id}")
            return False
        
        # 更新课程系统中的成绩
        if not self.course_system.set_course_score(student_id, course_id, score):
            return False
        
        # 同时更新学生对象中的成绩（使用课程名称作为科目）
        subject_name = f"{course.course_name}"
        student.add_score(subject_name, score)
        
        print(f"✓ 成绩录入完成：学生 {student.name}，课程 {course.course_name}，成绩 {score}")
        return True
    
    def get_student_course_info(self, student_id: str) -> Dict[str, Any]:
        """
        获取学生的完整选课信息
        
        Args:
            student_id (str): 学生学号
            
        Returns:
            Dict[str, Any]: 学生选课信息
        """
        student = self.student_system.get_student(student_id)
        if not student:
            return {'error': f"学生 {student_id} 不存在"}
        
        # 获取选课列表
        enrolled_courses = self.course_system.get_student_courses(student_id)
        
        # 获取学分统计
        credit_stats = self.course_statistics.get_student_credit_statistics(student_id)
        
        return {
            'student_id': student_id,
            'student_name': student.name,
            'major': student.major,
            'enrolled_courses': enrolled_courses,
            'credit_statistics': credit_stats
        }
    
    def get_course_student_info(self, course_id: str) -> Dict[str, Any]:
        """
        获取课程的完整学生信息
        
        Args:
            course_id (str): 课程ID
            
        Returns:
            Dict[str, Any]: 课程学生信息
        """
        course = self.course_system.get_course(course_id)
        if not course:
            return {'error': f"课程 {course_id} 不存在"}
        
        # 获取选课学生列表
        student_ids = self.course_system.get_course_students(course_id)
        
        # 获取学生详细信息
        students_info = []
        for sid in student_ids:
            student = self.student_system.get_student(sid)
            if student:
                score = self.course_system.get_course_score(sid, course_id)
                students_info.append({
                    'student_id': sid,
                    'name': student.name,
                    'major': student.major,
                    'score': score
                })
        
        # 获取课程统计
        score_stats = self.course_statistics.get_course_score_statistics(course_id)
        
        return {
            'course_id': course_id,
            'course_name': course.course_name,
            'teacher': course.teacher,
            'students': students_info,
            'statistics': score_stats
        }
    
    def batch_enroll_students(self, student_ids: List[str], course_id: str) -> Dict[str, Any]:
        """
        批量选课
        
        Args:
            student_ids (List[str]): 学生学号列表
            course_id (str): 课程ID
            
        Returns:
            Dict[str, Any]: 批量操作结果
        """
        success_count = 0
        failed_count = 0
        failed_students = []
        
        for student_id in student_ids:
            if self.enroll_student_to_course(student_id, course_id):
                success_count += 1
            else:
                failed_count += 1
                failed_students.append(student_id)
        
        return {
            'total': len(student_ids),
            'success': success_count,
            'failed': failed_count,
            'failed_students': failed_students
        }
    
    def get_student_transcript(self, student_id: str) -> str:
        """
        生成学生成绩单
        
        Args:
            student_id (str): 学生学号
            
        Returns:
            str: 格式化的成绩单
        """
        student = self.student_system.get_student(student_id)
        if not student:
            return f"错误：学生 {student_id} 不存在"
        
        # 获取选课信息
        enrolled_courses = self.course_system.get_student_courses(student_id)
        credit_stats = self.course_statistics.get_student_credit_statistics(student_id)
        
        transcript = f"""
{'='*60}
学生成绩单
{'='*60}

【学生信息】
学号: {student.student_id}
姓名: {student.name}
专业: {student.major}
年龄: {student.age}

【学分统计】
总选课程数: {credit_stats['total_courses']}
总学分: {credit_stats['total_credits']}
已获学分: {credit_stats['earned_credits']}
剩余学分: {credit_stats['remaining_credits']}
平均绩点(GPA): {credit_stats['gpa']}

【课程成绩明细】
"""
        
        if enrolled_courses:
            transcript += f"{'课程ID':<12} {'课程名称':<20} {'学分':<8} {'成绩':<8} {'状态'}\n"
            transcript += "-" * 60 + "\n"
            
            for course in enrolled_courses:
                score_str = f"{course['score']:.1f}" if course['score'] is not None else "未录入"
                status = "已获得" if course['score'] and course['score'] >= 60 else "未通过" if course['score'] else "-"
                
                transcript += f"{course['course_id']:<12} {course['course_name']:<20} "
                transcript += f"{course['credit']:<8.1f} {score_str:<8} {status}\n"
        else:
            transcript += "暂无选课记录\n"
        
        transcript += f"\n{'='*60}\n"
        
        return transcript
    
    def save_all_data(self) -> bool:
        """
        保存所有数据
        
        Returns:
            bool: 保存成功返回True，否则返回False
        """
        student_success = self.student_system.save_data()
        course_success = self.course_data_manager.save_courses(self.course_system)
        
        return student_success and course_success
    
    def load_all_data(self) -> bool:
        """
        加载所有数据
        
        Returns:
            bool: 加载成功返回True，否则返回False
        """
        student_success = self.student_system.load_data()
        course_success = self.course_data_manager.load_courses(self.course_system)
        
        return student_success and course_success
    
    def backup_all_data(self) -> bool:
        """
        备份所有数据
        
        Returns:
            bool: 备份成功返回True，否则返回False
        """
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        student_success = self.student_system.backup_data(f"students_backup_{timestamp}.json")
        course_success = self.course_data_manager.backup_courses(f"courses_backup_{timestamp}.json")
        
        return student_success and course_success
    
    def get_system_overview(self) -> Dict[str, Any]:
        """
        获取系统总览信息
        
        Returns:
            Dict[str, Any]: 系统总览数据
        """
        student_stats = self.student_system.get_statistics()
        course_overall = self.course_statistics.get_overall_statistics()
        
        return {
            'student_statistics': student_stats,
            'course_statistics': course_overall,
            'integration_info': {
                'total_enrollments': self.course_system.get_enrollment_count(),
                'students_with_courses': len(set(
                    e['student_id'] for e in self.course_system.enrollments.values()
                    if e.get('status') == 'enrolled'
                ))
            }
        }
