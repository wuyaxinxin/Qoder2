#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: student.py
作者: 开发者
创建日期: 2025-10-11
版本: 1.0
描述: 这是一个学生信息管理的Python类文件
      包含学生的基本信息管理和成绩统计功能
功能:
  - 学生基本信息管理（姓名、年龄、学号、专业）
  - 成绩管理（添加、删除、修改成绩）
  - 成绩统计（平均分、最高分、最低分）
  - 学生信息的显示和格式化输出
依赖: 无外部依赖，仅使用Python标准库
使用示例:
  student = Student("张三", 20, "2021001", "计算机科学")
  student.add_score("数学", 95)
  student.add_score("英语", 87)
  print(student.get_average_score())
修改记录:
  2025-10-11 - 初始版本创建
"""

from typing import Dict, List, Optional
from datetime import datetime


class Student:
    """学生类 - 管理学生的基本信息和成绩"""
    
    def __init__(self, name: str, age: int, student_id: str, major: str = ""):
        """
        初始化学生对象
        
        Args:
            name (str): 学生姓名
            age (int): 学生年龄
            student_id (str): 学号
            major (str): 专业，默认为空字符串
        """
        self.name = name
        self.age = age
        self.student_id = student_id
        self.major = major
        self.scores: Dict[str, float] = {}  # 存储科目和成绩的字典
        self.created_time = datetime.now()
    
    def add_score(self, subject: str, score: float) -> bool:
        """
        添加或更新科目成绩
        
        Args:
            subject (str): 科目名称
            score (float): 成绩分数
            
        Returns:
            bool: 操作成功返回True，否则返回False
        """
        if not isinstance(score, (int, float)) or score < 0 or score > 100:
            print(f"错误：成绩 {score} 不在有效范围内 (0-100)")
            return False
        
        self.scores[subject] = float(score)
        print(f"成功添加/更新 {subject} 成绩: {score}")
        return True
    
    def remove_score(self, subject: str) -> bool:
        """
        删除指定科目的成绩
        
        Args:
            subject (str): 科目名称
            
        Returns:
            bool: 删除成功返回True，科目不存在返回False
        """
        if subject in self.scores:
            del self.scores[subject]
            print(f"成功删除 {subject} 的成绩")
            return True
        else:
            print(f"错误：科目 {subject} 不存在")
            return False
    
    def get_score(self, subject: str) -> Optional[float]:
        """
        获取指定科目的成绩
        
        Args:
            subject (str): 科目名称
            
        Returns:
            Optional[float]: 成绩分数，科目不存在时返回None
        """
        return self.scores.get(subject)
    
    def get_all_scores(self) -> Dict[str, float]:
        """
        获取所有科目的成绩
        
        Returns:
            Dict[str, float]: 包含所有科目和成绩的字典
        """
        return self.scores.copy()
    
    def get_average_score(self) -> float:
        """
        计算平均成绩
        
        Returns:
            float: 平均成绩，没有成绩时返回0.0
        """
        if not self.scores:
            return 0.0
        return sum(self.scores.values()) / len(self.scores)
    
    def get_highest_score(self) -> Optional[tuple]:
        """
        获取最高成绩及其科目
        
        Returns:
            Optional[tuple]: (科目, 成绩) 元组，没有成绩时返回None
        """
        if not self.scores:
            return None
        
        max_subject = max(self.scores, key=self.scores.get)
        return (max_subject, self.scores[max_subject])
    
    def get_lowest_score(self) -> Optional[tuple]:
        """
        获取最低成绩及其科目
        
        Returns:
            Optional[tuple]: (科目, 成绩) 元组，没有成绩时返回None
        """
        if not self.scores:
            return None
        
        min_subject = min(self.scores, key=self.scores.get)
        return (min_subject, self.scores[min_subject])
    
    def get_passing_subjects(self, passing_score: float = 60.0) -> List[str]:
        """
        获取及格的科目列表
        
        Args:
            passing_score (float): 及格分数线，默认60分
            
        Returns:
            List[str]: 及格科目列表
        """
        return [subject for subject, score in self.scores.items() if score >= passing_score]
    
    def get_failing_subjects(self, passing_score: float = 60.0) -> List[str]:
        """
        获取不及格的科目列表
        
        Args:
            passing_score (float): 及格分数线，默认60分
            
        Returns:
            List[str]: 不及格科目列表
        """
        return [subject for subject, score in self.scores.items() if score < passing_score]
    
    def is_excellent_student(self, excellent_threshold: float = 85.0) -> bool:
        """
        判断是否为优秀学生
        
        Args:
            excellent_threshold (float): 优秀学生平均分阈值，默认85分
            
        Returns:
            bool: 是优秀学生返回True，否则返回False
        """
        avg_score = self.get_average_score()
        return avg_score >= excellent_threshold and len(self.get_failing_subjects()) == 0
    
    def get_student_info(self) -> str:
        """
        获取学生详细信息的格式化字符串
        
        Returns:
            str: 格式化的学生信息
        """
        info = f"""
=== 学生信息 ===
姓名: {self.name}
年龄: {self.age}
学号: {self.student_id}
专业: {self.major}
注册时间: {self.created_time.strftime('%Y-%m-%d %H:%M:%S')}

=== 成绩信息 ===
"""
        
        if not self.scores:
            info += "暂无成绩记录\n"
        else:
            for subject, score in self.scores.items():
                info += f"{subject}: {score:.1f}分\n"
            
            info += f"\n=== 统计信息 ===\n"
            info += f"平均成绩: {self.get_average_score():.2f}分\n"
            
            highest = self.get_highest_score()
            if highest:
                info += f"最高成绩: {highest[0]} ({highest[1]:.1f}分)\n"
            
            lowest = self.get_lowest_score()
            if lowest:
                info += f"最低成绩: {lowest[0]} ({lowest[1]:.1f}分)\n"
            
            passing_subjects = self.get_passing_subjects()
            info += f"及格科目数: {len(passing_subjects)}/{len(self.scores)}\n"
            
            if self.is_excellent_student():
                info += "学习状态: 优秀学生 🌟\n"
            elif len(self.get_failing_subjects()) == 0:
                info += "学习状态: 良好\n"
            else:
                info += "学习状态: 需要努力\n"
        
        return info
    
    def __str__(self) -> str:
        """字符串表示"""
        return f"Student(name='{self.name}', student_id='{self.student_id}', scores_count={len(self.scores)})"
    
    def __repr__(self) -> str:
        """对象表示"""
        return self.__str__()


def demonstrate_student_management():
    """演示学生管理功能"""
    print("=== 学生管理系统演示 ===\n")
    
    # 创建学生对象
    student1 = Student("张三", 20, "2021001", "计算机科学与技术")
    student2 = Student("李四", 19, "2021002", "数学与应用数学")
    
    # 添加成绩
    print("1. 添加学生成绩:")
    student1.add_score("高等数学", 92)
    student1.add_score("程序设计", 88)
    student1.add_score("英语", 76)
    student1.add_score("物理", 84)
    
    student2.add_score("高等数学", 95)
    student2.add_score("线性代数", 87)
    student2.add_score("英语", 82)
    
    print("\n2. 显示学生信息:")
    print(student1.get_student_info())
    print(student2.get_student_info())
    
    print("3. 成绩操作演示:")
    print(f"张三的程序设计成绩: {student1.get_score('程序设计')}")
    student1.remove_score("物理")
    print(f"删除物理成绩后的平均分: {student1.get_average_score():.2f}")


if __name__ == "__main__":
    demonstrate_student_management()