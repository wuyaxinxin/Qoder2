#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: student_manager.py
作者: 开发者
创建日期: 2025-10-13
版本: 2.0
描述: 学生管理系统核心模块
      提供学生信息的增删改查、数据持久化、统计分析等功能
"""

import json
import os
from typing import List, Dict, Optional, Tuple
from datetime import datetime
from student import Student
from validator import Validator, ValidationError


class StudentManager:
    """学生管理系统类"""
    
    def __init__(self, data_file: str = "students_data.json"):
        """
        初始化学生管理系统
        
        Args:
            data_file (str): 数据文件路径
        """
        self.students: Dict[str, Student] = {}
        self.data_file = data_file
        self.load_data()
    
    def add_student(self, name: str, age: int, student_id: str, major: str = "") -> bool:
        """
        添加新学生
        
        Args:
            name (str): 学生姓名
            age (int): 学生年龄
            student_id (str): 学号
            major (str): 专业
            
        Returns:
            bool: 添加成功返回True，否则返回False
        """
        # 验证输入
        if not Validator.validate_student_id(student_id):
            print(f"错误：学号格式不正确 (应为7位数字，如2021001)")
            return False
        
        if not Validator.validate_age(age):
            print(f"错误：年龄不合法")
            return False
        
        if Validator.is_empty(name):
            print(f"错误：姓名不能为空")
            return False
        
        # 检查学号是否已存在
        if student_id in self.students:
            print(f"错误：学号 {student_id} 已存在")
            return False
        
        # 创建学生对象
        student = Student(name, age, student_id, major)
        self.students[student_id] = student
        print(f"成功添加学生：{name} (学号：{student_id})")
        self.save_data()
        return True
    
    def remove_student(self, student_id: str) -> bool:
        """
        删除学生
        
        Args:
            student_id (str): 学号
            
        Returns:
            bool: 删除成功返回True，否则返回False
        """
        if student_id not in self.students:
            print(f"错误：找不到学号为 {student_id} 的学生")
            return False
        
        student_name = self.students[student_id].name
        del self.students[student_id]
        print(f"成功删除学生：{student_name} (学号：{student_id})")
        self.save_data()
        return True
    
    def get_student(self, student_id: str) -> Optional[Student]:
        """
        获取学生对象
        
        Args:
            student_id (str): 学号
            
        Returns:
            Optional[Student]: 学生对象，不存在时返回None
        """
        return self.students.get(student_id)
    
    def update_student_info(self, student_id: str, name: str = None, 
                           age: int = None, major: str = None) -> bool:
        """
        更新学生基本信息
        
        Args:
            student_id (str): 学号
            name (str): 新姓名
            age (int): 新年龄
            major (str): 新专业
            
        Returns:
            bool: 更新成功返回True，否则返回False
        """
        student = self.get_student(student_id)
        if not student:
            print(f"错误：找不到学号为 {student_id} 的学生")
            return False
        
        if name is not None:
            student.name = name
        if age is not None:
            if not Validator.validate_age(age):
                print(f"错误：年龄不合法")
                return False
            student.age = age
        if major is not None:
            student.major = major
        
        print(f"成功更新学生信息：{student.name}")
        self.save_data()
        return True
    
    def search_students(self, keyword: str) -> List[Student]:
        """
        搜索学生（按姓名、学号、专业）
        
        Args:
            keyword (str): 搜索关键词
            
        Returns:
            List[Student]: 匹配的学生列表
        """
        results = []
        keyword_lower = keyword.lower()
        
        for student in self.students.values():
            if (keyword_lower in student.name.lower() or 
                keyword_lower in student.student_id.lower() or 
                keyword_lower in student.major.lower()):
                results.append(student)
        
        return results
    
    def get_all_students(self) -> List[Student]:
        """
        获取所有学生
        
        Returns:
            List[Student]: 所有学生列表
        """
        return list(self.students.values())
    
    def get_student_count(self) -> int:
        """
        获取学生总数
        
        Returns:
            int: 学生总数
        """
        return len(self.students)
    
    def get_statistics(self) -> Dict[str, any]:
        """
        获取系统统计信息
        
        Returns:
            Dict: 统计信息字典
        """
        if not self.students:
            return {
                'total_students': 0,
                'average_age': 0,
                'major_distribution': {},
                'excellent_students': 0
            }
        
        total_age = sum(s.age for s in self.students.values())
        average_age = total_age / len(self.students)
        
        # 专业分布
        major_distribution = {}
        for student in self.students.values():
            major = student.major if student.major else "未指定"
            major_distribution[major] = major_distribution.get(major, 0) + 1
        
        # 优秀学生数
        excellent_count = sum(1 for s in self.students.values() if s.is_excellent_student())
        
        return {
            'total_students': len(self.students),
            'average_age': round(average_age, 2),
            'major_distribution': major_distribution,
            'excellent_students': excellent_count
        }
    
    def get_top_students(self, limit: int = 10) -> List[Tuple[Student, float]]:
        """
        获取成绩排名前N的学生
        
        Args:
            limit (int): 返回的学生数量
            
        Returns:
            List[Tuple[Student, float]]: (学生, 平均分) 列表
        """
        students_with_scores = []
        
        for student in self.students.values():
            avg_score = student.get_average_score()
            if avg_score > 0:  # 只包含有成绩的学生
                students_with_scores.append((student, avg_score))
        
        # 按平均分降序排序
        students_with_scores.sort(key=lambda x: x[1], reverse=True)
        
        return students_with_scores[:limit]
    
    def save_data(self) -> bool:
        """
        保存数据到文件
        
        Returns:
            bool: 保存成功返回True，否则返回False
        """
        try:
            data = {
                'students': [],
                'save_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            
            for student in self.students.values():
                student_data = {
                    'name': student.name,
                    'age': student.age,
                    'student_id': student.student_id,
                    'major': student.major,
                    'scores': student.scores,
                    'created_time': student.created_time.strftime('%Y-%m-%d %H:%M:%S')
                }
                data['students'].append(student_data)
            
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            return True
        except Exception as e:
            print(f"保存数据失败：{str(e)}")
            return False
    
    def load_data(self) -> bool:
        """
        从文件加载数据
        
        Returns:
            bool: 加载成功返回True，否则返回False
        """
        if not os.path.exists(self.data_file):
            print(f"数据文件不存在，将创建新文件：{self.data_file}")
            return False
        
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            self.students.clear()
            
            for student_data in data.get('students', []):
                student = Student(
                    student_data['name'],
                    student_data['age'],
                    student_data['student_id'],
                    student_data['major']
                )
                student.scores = student_data.get('scores', {})
                
                # 恢复创建时间
                if 'created_time' in student_data:
                    student.created_time = datetime.strptime(
                        student_data['created_time'], 
                        '%Y-%m-%d %H:%M:%S'
                    )
                
                self.students[student.student_id] = student
            
            print(f"成功加载 {len(self.students)} 名学生的数据")
            return True
        except Exception as e:
            print(f"加载数据失败：{str(e)}")
            return False
    
    def export_to_csv(self, filename: str = "students_export.csv") -> bool:
        """
        导出学生数据到CSV文件
        
        Args:
            filename (str): 导出文件名
            
        Returns:
            bool: 导出成功返回True，否则返回False
        """
        try:
            with open(filename, 'w', encoding='utf-8-sig') as f:
                # 写入表头
                f.write("学号,姓名,年龄,专业,平均成绩,最高分,最低分,科目数\n")
                
                # 写入数据
                for student in self.students.values():
                    avg_score = student.get_average_score()
                    highest = student.get_highest_score()
                    lowest = student.get_lowest_score()
                    
                    highest_str = f"{highest[1]:.1f}" if highest else "N/A"
                    lowest_str = f"{lowest[1]:.1f}" if lowest else "N/A"
                    
                    f.write(f"{student.student_id},{student.name},{student.age},"
                           f"{student.major},{avg_score:.2f},{highest_str},"
                           f"{lowest_str},{len(student.scores)}\n")
            
            print(f"成功导出数据到：{filename}")
            return True
        except Exception as e:
            print(f"导出数据失败：{str(e)}")
            return False
    
    def clear_all_data(self) -> bool:
        """
        清空所有数据（谨慎使用）
        
        Returns:
            bool: 清空成功返回True，否则返回False
        """
        self.students.clear()
        self.save_data()
        print("已清空所有学生数据")
        return True
    
    def __str__(self) -> str:
        """字符串表示"""
        return f"StudentManager(students={len(self.students)}, file='{self.data_file}')"
