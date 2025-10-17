#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: course_management_system.py
作者: 开发者
创建日期: 2025-10-16
版本: 1.0
描述: 课程管理系统核心逻辑
      提供课程的增删改查、选课退课等业务功能
"""

from typing import Dict, List, Optional, Tuple
from course import Course
from validator import Validator, ValidationError


class CourseManagementSystem:
    """课程管理系统类"""
    
    def __init__(self):
        """初始化课程管理系统"""
        self.courses: Dict[str, Course] = {}  # 课程ID -> Course对象
        self.enrollments: Dict[str, Dict[str, any]] = {}  # "学号_课程ID" -> 选课信息
    
    def add_course(self, course_id: str, course_name: str, teacher: str,
                   credit: float, capacity: int, description: str = "",
                   semester: str = "", schedule: str = "") -> bool:
        """
        添加课程
        
        Args:
            course_id (str): 课程ID
            course_name (str): 课程名称
            teacher (str): 授课教师
            credit (float): 学分
            capacity (int): 课程容量
            description (str): 课程描述
            semester (str): 开课学期
            schedule (str): 上课时间
            
        Returns:
            bool: 添加成功返回True，否则返回False
        """
        # 数据验证
        if not Validator.validate_course_id(course_id):
            print(f"错误：课程ID格式不正确，应为2-3个大写字母+3位数字，如CS101")
            return False
        
        if not Validator.validate_course_name(course_name):
            print(f"错误：课程名称长度应在2-50字符之间")
            return False
        
        if not Validator.validate_credit(credit):
            print(f"错误：学分应在0.5-10.0之间")
            return False
        
        if not Validator.validate_capacity(capacity):
            print(f"错误：课程容量应在1-500之间")
            return False
        
        if Validator.is_empty(teacher):
            print(f"错误：授课教师不能为空")
            return False
        
        # 检查课程ID唯一性
        if course_id in self.courses:
            print(f"错误：课程ID {course_id} 已存在")
            return False
        
        # 创建课程对象
        course = Course(
            course_id=course_id,
            course_name=course_name,
            teacher=teacher,
            credit=credit,
            capacity=capacity,
            description=description,
            semester=semester,
            schedule=schedule
        )
        
        self.courses[course_id] = course
        print(f"✓ 课程添加成功！课程ID: {course_id}")
        return True
    
    def remove_course(self, course_id: str) -> bool:
        """
        删除课程
        
        Args:
            course_id (str): 课程ID
            
        Returns:
            bool: 删除成功返回True，否则返回False
        """
        if course_id not in self.courses:
            print(f"错误：课程 {course_id} 不存在")
            return False
        
        course = self.courses[course_id]
        
        # 检查是否有学生选课
        if course.enrolled_count > 0:
            print(f"错误：课程 {course.course_name} 有 {course.enrolled_count} 名学生选课，无法删除")
            print(f"提示：请先让所有学生退课后再删除课程")
            return False
        
        # 删除课程
        del self.courses[course_id]
        
        # 清理相关的选课记录
        enrollment_keys = [key for key in self.enrollments.keys() if key.endswith(f"_{course_id}")]
        for key in enrollment_keys:
            del self.enrollments[key]
        
        print(f"✓ 课程 {course_id} 删除成功")
        return True
    
    def update_course(self, course_id: str, **kwargs) -> bool:
        """
        更新课程信息
        
        Args:
            course_id (str): 课程ID
            **kwargs: 要更新的字段（course_name, teacher, credit, capacity, description, semester, schedule）
            
        Returns:
            bool: 更新成功返回True，否则返回False
        """
        if course_id not in self.courses:
            print(f"错误：课程 {course_id} 不存在")
            return False
        
        course = self.courses[course_id]
        
        # 验证并更新字段
        for key, value in kwargs.items():
            if key == 'course_name':
                if not Validator.validate_course_name(value):
                    print(f"错误：课程名称长度应在2-50字符之间")
                    return False
                course.course_name = value
            
            elif key == 'teacher':
                if Validator.is_empty(value):
                    print(f"错误：授课教师不能为空")
                    return False
                course.teacher = value
            
            elif key == 'credit':
                if not Validator.validate_credit(value):
                    print(f"错误：学分应在0.5-10.0之间")
                    return False
                course.credit = value
            
            elif key == 'capacity':
                if not Validator.validate_capacity(value):
                    print(f"错误：课程容量应在1-500之间")
                    return False
                # 检查新容量是否小于已选人数
                if value < course.enrolled_count:
                    print(f"错误：新容量 {value} 小于已选人数 {course.enrolled_count}")
                    return False
                course.capacity = value
            
            elif key == 'description':
                course.description = value
            
            elif key == 'semester':
                course.semester = value
            
            elif key == 'schedule':
                course.schedule = value
            
            else:
                print(f"警告：未知字段 {key}，已忽略")
        
        print(f"✓ 课程 {course_id} 更新成功")
        return True
    
    def get_course(self, course_id: str) -> Optional[Course]:
        """
        获取课程对象
        
        Args:
            course_id (str): 课程ID
            
        Returns:
            Optional[Course]: 课程对象，不存在时返回None
        """
        return self.courses.get(course_id)
    
    def search_courses(self, keyword: str = "", teacher: str = "", 
                       semester: str = "") -> List[Course]:
        """
        搜索课程
        
        Args:
            keyword (str): 关键词（搜索课程ID或名称）
            teacher (str): 教师名称
            semester (str): 学期
            
        Returns:
            List[Course]: 符合条件的课程列表
        """
        results = []
        
        for course in self.courses.values():
            match = True
            
            if keyword:
                if keyword.lower() not in course.course_id.lower() and \
                   keyword not in course.course_name:
                    match = False
            
            if teacher and teacher not in course.teacher:
                match = False
            
            if semester and semester != course.semester:
                match = False
            
            if match:
                results.append(course)
        
        return results
    
    def list_all_courses(self, sort_by: str = "course_id") -> List[Course]:
        """
        列出所有课程
        
        Args:
            sort_by (str): 排序字段（course_id/course_name/enrolled_count）
            
        Returns:
            List[Course]: 课程列表
        """
        courses_list = list(self.courses.values())
        
        if sort_by == "course_id":
            courses_list.sort(key=lambda c: c.course_id)
        elif sort_by == "course_name":
            courses_list.sort(key=lambda c: c.course_name)
        elif sort_by == "enrolled_count":
            courses_list.sort(key=lambda c: c.enrolled_count, reverse=True)
        
        return courses_list
    
    def enroll_student(self, student_id: str, course_id: str) -> bool:
        """
        学生选课
        
        Args:
            student_id (str): 学生学号
            course_id (str): 课程ID
            
        Returns:
            bool: 选课成功返回True，否则返回False
        """
        # 检查课程是否存在
        if course_id not in self.courses:
            print(f"错误：课程 {course_id} 不存在")
            return False
        
        course = self.courses[course_id]
        
        # 检查是否重复选课
        enrollment_key = f"{student_id}_{course_id}"
        if enrollment_key in self.enrollments:
            status = self.enrollments[enrollment_key].get('status', 'enrolled')
            if status == 'enrolled':
                print(f"错误：学生 {student_id} 已选过课程 {course.course_name}")
                return False
        
        # 尝试添加学生到课程
        if not course.add_student(student_id):
            return False
        
        # 创建选课记录
        from datetime import datetime
        self.enrollments[enrollment_key] = {
            'student_id': student_id,
            'course_id': course_id,
            'enrollment_time': datetime.now().isoformat(),
            'status': 'enrolled',
            'score': None
        }
        
        print(f"✓ 学生 {student_id} 成功选课 {course.course_name}")
        return True
    
    def drop_course(self, student_id: str, course_id: str, 
                    allow_with_score: bool = False) -> bool:
        """
        学生退课
        
        Args:
            student_id (str): 学生学号
            course_id (str): 课程ID
            allow_with_score (bool): 是否允许有成绩的课程退课
            
        Returns:
            bool: 退课成功返回True，否则返回False
        """
        # 检查课程是否存在
        if course_id not in self.courses:
            print(f"错误：课程 {course_id} 不存在")
            return False
        
        course = self.courses[course_id]
        enrollment_key = f"{student_id}_{course_id}"
        
        # 检查选课记录是否存在
        if enrollment_key not in self.enrollments:
            print(f"错误：学生 {student_id} 未选该课程")
            return False
        
        enrollment = self.enrollments[enrollment_key]
        
        # 检查是否已有成绩
        if not allow_with_score and enrollment.get('score') is not None:
            print(f"错误：该课程已有成绩，不允许退课")
            print(f"提示：如需强制退课，请联系管理员")
            return False
        
        # 从课程中移除学生
        if not course.remove_student(student_id):
            return False
        
        # 更新选课状态
        enrollment['status'] = 'dropped'
        from datetime import datetime
        enrollment['drop_time'] = datetime.now().isoformat()
        
        print(f"✓ 学生 {student_id} 成功退课 {course.course_name}")
        return True
    
    def get_student_courses(self, student_id: str) -> List[Dict[str, any]]:
        """
        获取学生选课列表
        
        Args:
            student_id (str): 学生学号
            
        Returns:
            List[Dict[str, any]]: 选课信息列表
        """
        student_courses = []
        
        for key, enrollment in self.enrollments.items():
            if enrollment['student_id'] == student_id and enrollment['status'] == 'enrolled':
                course_id = enrollment['course_id']
                if course_id in self.courses:
                    course = self.courses[course_id]
                    student_courses.append({
                        'course_id': course.course_id,
                        'course_name': course.course_name,
                        'teacher': course.teacher,
                        'credit': course.credit,
                        'semester': course.semester,
                        'schedule': course.schedule,
                        'enrollment_time': enrollment['enrollment_time'],
                        'score': enrollment.get('score')
                    })
        
        return student_courses
    
    def get_course_students(self, course_id: str) -> List[str]:
        """
        获取课程选课学生列表
        
        Args:
            course_id (str): 课程ID
            
        Returns:
            List[str]: 学生学号列表
        """
        if course_id not in self.courses:
            return []
        
        return self.courses[course_id].get_enrolled_students()
    
    def set_course_score(self, student_id: str, course_id: str, score: float) -> bool:
        """
        设置课程成绩
        
        Args:
            student_id (str): 学生学号
            course_id (str): 课程ID
            score (float): 成绩
            
        Returns:
            bool: 设置成功返回True，否则返回False
        """
        enrollment_key = f"{student_id}_{course_id}"
        
        # 检查选课记录是否存在
        if enrollment_key not in self.enrollments:
            print(f"错误：学生 {student_id} 未选课程 {course_id}")
            return False
        
        # 验证成绩
        if not Validator.validate_score(score):
            print(f"错误：成绩应在0-100之间")
            return False
        
        # 更新成绩
        self.enrollments[enrollment_key]['score'] = float(score)
        print(f"✓ 成绩录入成功：学生 {student_id}，课程 {course_id}，成绩 {score}")
        return True
    
    def get_course_score(self, student_id: str, course_id: str) -> Optional[float]:
        """
        获取课程成绩
        
        Args:
            student_id (str): 学生学号
            course_id (str): 课程ID
            
        Returns:
            Optional[float]: 成绩，不存在时返回None
        """
        enrollment_key = f"{student_id}_{course_id}"
        
        if enrollment_key in self.enrollments:
            return self.enrollments[enrollment_key].get('score')
        
        return None
    
    def get_course_count(self) -> int:
        """获取课程总数"""
        return len(self.courses)
    
    def get_enrollment_count(self) -> int:
        """获取选课记录总数（仅计算状态为enrolled的）"""
        return sum(1 for e in self.enrollments.values() if e.get('status') == 'enrolled')
    
    def __str__(self) -> str:
        """字符串表示"""
        return f"CourseManagementSystem(courses={len(self.courses)}, enrollments={self.get_enrollment_count()})"
