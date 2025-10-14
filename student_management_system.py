#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: student_management_system.py  
作者: 开发者
创建日期: 2025-10-13
版本: 2.0
描述: 学生管理系统主模块
      提供完整的学生信息管理功能，包括增删改查、成绩管理、数据持久化等
"""

import json
import os
from typing import Dict, List, Optional, Tuple
from datetime import datetime
from student import Student
from validator import Validator
from utils import format_timestamp, clean_string


class StudentManagementSystem:
    """学生管理系统类"""
    
    def __init__(self, data_file: str = "students_data.json"):
        """
        初始化学生管理系统
        
        Args:
            data_file (str): 数据文件路径
        """
        self.data_file = data_file
        self.students: Dict[str, Student] = {}
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
        # 验证输入数据
        if not self._validate_student_data(name, age, student_id):
            return False
        
        # 检查学号是否已存在
        if student_id in self.students:
            print(f"错误：学号 {student_id} 已存在")
            return False
        
        # 创建学生对象
        student = Student(clean_string(name), age, student_id, clean_string(major))
        self.students[student_id] = student
        
        print(f"成功添加学生：{name} (学号: {student_id})")
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
            print(f"错误：学号 {student_id} 不存在")
            return False
        
        student_name = self.students[student_id].name
        del self.students[student_id]
        print(f"成功删除学生：{student_name} (学号: {student_id})")
        return True
    
    def update_student(self, student_id: str, **kwargs) -> bool:
        """
        更新学生信息
        
        Args:
            student_id (str): 学号
            **kwargs: 要更新的字段（name, age, major）
            
        Returns:
            bool: 更新成功返回True，否则返回False
        """
        if student_id not in self.students:
            print(f"错误：学号 {student_id} 不存在")
            return False
        
        student = self.students[student_id]
        updated_fields = []
        
        # 更新姓名
        if 'name' in kwargs:
            new_name = clean_string(kwargs['name'])
            if new_name and len(new_name) > 0:
                student.name = new_name
                updated_fields.append('姓名')
        
        # 更新年龄
        if 'age' in kwargs:
            if Validator.validate_age(kwargs['age']):
                student.age = int(kwargs['age'])
                updated_fields.append('年龄')
            else:
                print("错误：年龄必须是0-150之间的整数")
                return False
        
        # 更新专业
        if 'major' in kwargs:
            student.major = clean_string(kwargs['major'])
            updated_fields.append('专业')
        
        if updated_fields:
            print(f"成功更新学生 {student.name} 的信息：{', '.join(updated_fields)}")
            return True
        else:
            print("没有更新任何信息")
            return False
    
    def get_student(self, student_id: str) -> Optional[Student]:
        """
        获取学生对象
        
        Args:
            student_id (str): 学号
            
        Returns:
            Optional[Student]: 学生对象，不存在时返回None
        """
        return self.students.get(student_id)
    
    def search_students(self, **criteria) -> List[Student]:
        """
        搜索学生
        
        Args:
            **criteria: 搜索条件（name, major, min_age, max_age等）
            
        Returns:
            List[Student]: 匹配的学生列表
        """
        results = []
        
        for student in self.students.values():
            match = True
            
            # 按姓名搜索（模糊匹配）
            if 'name' in criteria:
                if criteria['name'].lower() not in student.name.lower():
                    match = False
            
            # 按专业搜索
            if 'major' in criteria:
                if criteria['major'].lower() not in student.major.lower():
                    match = False
            
            # 按年龄范围搜索
            if 'min_age' in criteria:
                if student.age < criteria['min_age']:
                    match = False
            
            if 'max_age' in criteria:
                if student.age > criteria['max_age']:
                    match = False
            
            if match:
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
    
    def add_student_score(self, student_id: str, subject: str, score: float) -> bool:
        """
        为学生添加成绩
        
        Args:
            student_id (str): 学号
            subject (str): 科目
            score (float): 成绩
            
        Returns:
            bool: 添加成功返回True，否则返回False
        """
        student = self.get_student(student_id)
        if not student:
            print(f"错误：学号 {student_id} 不存在")
            return False
        
        return student.add_score(subject, score)
    
    def get_top_students(self, limit: int = 10) -> List[Tuple[Student, float]]:
        """
        获取成绩排名前N的学生
        
        Args:
            limit (int): 返回学生数量限制
            
        Returns:
            List[Tuple[Student, float]]: 学生和平均分的元组列表
        """
        students_with_scores = []
        
        for student in self.students.values():
            avg_score = student.get_average_score()
            if avg_score > 0:  # 只包含有成绩的学生
                students_with_scores.append((student, avg_score))
        
        # 按平均分降序排序
        students_with_scores.sort(key=lambda x: x[1], reverse=True)
        
        return students_with_scores[:limit]
    
    def get_statistics(self) -> Dict[str, any]:
        """
        获取系统统计信息
        
        Returns:
            Dict[str, any]: 统计信息字典
        """
        total_students = len(self.students)
        students_with_scores = 0
        all_scores = []
        excellent_students = 0
        
        for student in self.students.values():
            if student.scores:
                students_with_scores += 1
                all_scores.extend(student.scores.values())
                if student.is_excellent_student():
                    excellent_students += 1
        
        stats = {
            'total_students': total_students,
            'students_with_scores': students_with_scores,
            'excellent_students': excellent_students,
            'average_system_score': sum(all_scores) / len(all_scores) if all_scores else 0.0,
            'total_score_records': len(all_scores)
        }
        
        return stats
    
    def export_students_to_dict(self) -> Dict[str, Dict]:
        """
        将学生数据导出为字典格式
        
        Returns:
            Dict[str, Dict]: 学生数据字典
        """
        data = {}
        for student_id, student in self.students.items():
            data[student_id] = {
                'name': student.name,
                'age': student.age,
                'student_id': student.student_id,
                'major': student.major,
                'scores': student.scores,
                'created_time': student.created_time.isoformat()
            }
        return data
    
    def import_students_from_dict(self, data: Dict[str, Dict]) -> int:
        """
        从字典数据导入学生信息
        
        Args:
            data (Dict[str, Dict]): 学生数据字典
            
        Returns:
            int: 成功导入的学生数量
        """
        imported_count = 0
        
        for student_id, student_data in data.items():
            try:
                # 创建学生对象
                student = Student(
                    student_data['name'],
                    student_data['age'],
                    student_data['student_id'],
                    student_data.get('major', '')
                )
                
                # 恢复成绩
                if 'scores' in student_data:
                    student.scores = student_data['scores']
                
                # 恢复创建时间
                if 'created_time' in student_data:
                    student.created_time = datetime.fromisoformat(student_data['created_time'])
                
                self.students[student_id] = student
                imported_count += 1
                
            except Exception as e:
                print(f"导入学生 {student_id} 时出错：{e}")
        
        return imported_count
    
    def save_data(self) -> bool:
        """
        保存数据到文件
        
        Returns:
            bool: 保存成功返回True，否则返回False
        """
        try:
            data = {
                'students': self.export_students_to_dict(),
                'metadata': {
                    'last_updated': datetime.now().isoformat(),
                    'total_students': len(self.students)
                }
            }
            
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            print(f"数据已保存到 {self.data_file}")
            return True
            
        except Exception as e:
            print(f"保存数据失败：{e}")
            return False
    
    def load_data(self) -> bool:
        """
        从文件加载数据
        
        Returns:
            bool: 加载成功返回True，否则返回False
        """
        if not os.path.exists(self.data_file):
            print(f"数据文件 {self.data_file} 不存在，将创建新文件")
            return True
        
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            if 'students' in data:
                imported_count = self.import_students_from_dict(data['students'])
                print(f"成功加载 {imported_count} 个学生的数据")
            
            return True
            
        except Exception as e:
            print(f"加载数据失败：{e}")
            return False
    
    def _validate_student_data(self, name: str, age: int, student_id: str) -> bool:
        """
        验证学生数据
        
        Args:
            name (str): 姓名
            age (int): 年龄
            student_id (str): 学号
            
        Returns:
            bool: 验证通过返回True，否则返回False
        """
        # 验证姓名
        if not name or not isinstance(name, str) or len(clean_string(name)) == 0:
            print("错误：姓名不能为空")
            return False
        
        # 验证年龄
        if not Validator.validate_age(age):
            print("错误：年龄必须是0-150之间的整数")
            return False
        
        # 验证学号
        if not Validator.validate_student_id(student_id):
            print("错误：学号格式不正确（应为7位数字，如2021001）")
            return False
        
        return True
    
    def backup_data(self, backup_path: str = None) -> bool:
        """
        备份数据
        
        Args:
            backup_path (str): 备份文件路径
            
        Returns:
            bool: 备份成功返回True，否则返回False
        """
        if backup_path is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_path = f"students_backup_{timestamp}.json"
        
        try:
            # 先保存当前数据
            original_file = self.data_file
            self.data_file = backup_path
            success = self.save_data()
            self.data_file = original_file
            
            if success:
                print(f"数据已备份到 {backup_path}")
            
            return success
            
        except Exception as e:
            print(f"备份失败：{e}")
            return False