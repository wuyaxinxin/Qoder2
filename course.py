#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: course.py
作者: 开发者
创建日期: 2025-10-16
版本: 1.0
描述: 课程实体模型类
      包含课程的基本信息管理和选课学生管理功能
功能:
  - 课程基本信息管理（课程ID、名称、教师、学分等）
  - 选课学生管理（添加、移除学生）
  - 课程容量管理和检查
  - 课程统计信息
依赖: 无外部依赖，仅使用Python标准库
"""

from typing import List, Dict, Optional, Set
from datetime import datetime


class Course:
    """课程类 - 管理课程的基本信息和选课学生"""
    
    def __init__(self, course_id: str, course_name: str, teacher: str, 
                 credit: float, capacity: int, description: str = "",
                 semester: str = "", schedule: str = ""):
        """
        初始化课程对象
        
        Args:
            course_id (str): 课程唯一标识，格式如CS101
            course_name (str): 课程名称
            teacher (str): 授课教师
            credit (float): 学分，范围0.5-10.0
            capacity (int): 课程容量，范围1-500
            description (str): 课程描述，可选
            semester (str): 开课学期，如2024春季
            schedule (str): 上课时间，如周一3-4节
        """
        self.course_id = course_id
        self.course_name = course_name
        self.teacher = teacher
        self.credit = credit
        self.capacity = capacity
        self.description = description
        self.semester = semester
        self.schedule = schedule
        self.enrolled_students: Set[str] = set()  # 已选课学生学号集合
        self.created_time = datetime.now()
    
    @property
    def enrolled_count(self) -> int:
        """获取已选课人数"""
        return len(self.enrolled_students)
    
    def add_student(self, student_id: str) -> bool:
        """
        添加选课学生
        
        Args:
            student_id (str): 学生学号
            
        Returns:
            bool: 添加成功返回True，否则返回False
        """
        # 检查是否已满
        if self.is_full():
            print(f"错误：课程 {self.course_name} 已满员，无法选课")
            return False
        
        # 检查是否重复选课
        if student_id in self.enrolled_students:
            print(f"错误：学生 {student_id} 已选过该课程")
            return False
        
        self.enrolled_students.add(student_id)
        print(f"成功：学生 {student_id} 选课 {self.course_name}")
        return True
    
    def remove_student(self, student_id: str) -> bool:
        """
        移除选课学生
        
        Args:
            student_id (str): 学生学号
            
        Returns:
            bool: 移除成功返回True，否则返回False
        """
        if student_id not in self.enrolled_students:
            print(f"错误：学生 {student_id} 未选该课程")
            return False
        
        self.enrolled_students.remove(student_id)
        print(f"成功：学生 {student_id} 退课 {self.course_name}")
        return True
    
    def is_full(self) -> bool:
        """
        检查课程是否已满
        
        Returns:
            bool: 已满返回True，否则返回False
        """
        return self.enrolled_count >= self.capacity
    
    def get_enrolled_students(self) -> List[str]:
        """
        获取选课学生列表
        
        Returns:
            List[str]: 学生学号列表
        """
        return sorted(list(self.enrolled_students))
    
    def has_student(self, student_id: str) -> bool:
        """
        检查学生是否已选该课程
        
        Args:
            student_id (str): 学生学号
            
        Returns:
            bool: 已选课返回True，否则返回False
        """
        return student_id in self.enrolled_students
    
    def get_enrollment_rate(self) -> float:
        """
        获取选课率
        
        Returns:
            float: 选课率（百分比）
        """
        if self.capacity == 0:
            return 0.0
        return (self.enrolled_count / self.capacity) * 100
    
    def get_available_seats(self) -> int:
        """
        获取剩余容量
        
        Returns:
            int: 剩余可选人数
        """
        return max(0, self.capacity - self.enrolled_count)
    
    def get_course_info(self) -> str:
        """
        获取课程详细信息的格式化字符串
        
        Returns:
            str: 格式化的课程信息
        """
        info = f"""
=== 课程信息 ===
课程ID: {self.course_id}
课程名称: {self.course_name}
授课教师: {self.teacher}
学分: {self.credit}
课程容量: {self.capacity}人
已选人数: {self.enrolled_count}人
剩余名额: {self.get_available_seats()}人
选课率: {self.get_enrollment_rate():.1f}%
"""
        
        if self.semester:
            info += f"开课学期: {self.semester}\n"
        
        if self.schedule:
            info += f"上课时间: {self.schedule}\n"
        
        if self.description:
            info += f"课程描述: {self.description}\n"
        
        info += f"创建时间: {self.created_time.strftime('%Y-%m-%d %H:%M:%S')}\n"
        
        if self.enrolled_students:
            info += f"\n=== 选课学生 ===\n"
            info += f"学生列表: {', '.join(self.get_enrolled_students())}\n"
        else:
            info += f"\n暂无学生选课\n"
        
        return info
    
    def get_statistics(self) -> Dict[str, any]:
        """
        获取课程统计信息
        
        Returns:
            Dict[str, any]: 统计信息字典
        """
        return {
            'course_id': self.course_id,
            'course_name': self.course_name,
            'teacher': self.teacher,
            'credit': self.credit,
            'capacity': self.capacity,
            'enrolled_count': self.enrolled_count,
            'available_seats': self.get_available_seats(),
            'enrollment_rate': self.get_enrollment_rate(),
            'is_full': self.is_full(),
            'student_count': len(self.enrolled_students)
        }
    
    def to_dict(self) -> Dict[str, any]:
        """
        将课程对象转换为字典（用于JSON序列化）
        
        Returns:
            Dict[str, any]: 课程信息字典
        """
        return {
            'course_id': self.course_id,
            'course_name': self.course_name,
            'teacher': self.teacher,
            'credit': self.credit,
            'capacity': self.capacity,
            'description': self.description,
            'semester': self.semester,
            'schedule': self.schedule,
            'enrolled_students': list(self.enrolled_students),
            'created_time': self.created_time.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, any]) -> 'Course':
        """
        从字典创建课程对象（用于JSON反序列化）
        
        Args:
            data (Dict[str, any]): 课程信息字典
            
        Returns:
            Course: 课程对象
        """
        course = cls(
            course_id=data['course_id'],
            course_name=data['course_name'],
            teacher=data['teacher'],
            credit=data['credit'],
            capacity=data['capacity'],
            description=data.get('description', ''),
            semester=data.get('semester', ''),
            schedule=data.get('schedule', '')
        )
        
        # 恢复选课学生列表
        if 'enrolled_students' in data:
            course.enrolled_students = set(data['enrolled_students'])
        
        # 恢复创建时间
        if 'created_time' in data:
            try:
                course.created_time = datetime.fromisoformat(data['created_time'])
            except:
                course.created_time = datetime.now()
        
        return course
    
    def __str__(self) -> str:
        """字符串表示"""
        return f"Course(id='{self.course_id}', name='{self.course_name}', enrolled={self.enrolled_count}/{self.capacity})"
    
    def __repr__(self) -> str:
        """对象表示"""
        return self.__str__()


def demonstrate_course_management():
    """演示课程管理功能"""
    print("=== 课程管理系统演示 ===\n")
    
    # 创建课程对象
    course1 = Course("CS101", "数据结构与算法", "张教授", 3.0, 60, 
                     description="学习各种数据结构和算法的基础课程",
                     semester="2024春季", schedule="周一3-4节，周三5-6节")
    
    course2 = Course("MATH201", "高等数学", "李教授", 4.0, 80,
                     semester="2024春季", schedule="周二1-2节")
    
    print("1. 显示课程信息:")
    print(course1.get_course_info())
    
    print("\n2. 学生选课演示:")
    course1.add_student("2021001")
    course1.add_student("2021002")
    course1.add_student("2021003")
    
    print("\n3. 重复选课测试:")
    course1.add_student("2021001")  # 应该失败
    
    print("\n4. 学生退课演示:")
    course1.remove_student("2021002")
    
    print("\n5. 课程统计信息:")
    stats = course1.get_statistics()
    for key, value in stats.items():
        print(f"{key}: {value}")
    
    print("\n6. 课程序列化测试:")
    course_dict = course1.to_dict()
    print(f"转换为字典: {course_dict}")
    
    restored_course = Course.from_dict(course_dict)
    print(f"从字典恢复: {restored_course}")


if __name__ == "__main__":
    demonstrate_course_management()
