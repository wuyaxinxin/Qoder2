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
    """
    学生类 - 管理学生的基本信息和成绩
    
    该类提供了完整的学生信息管理功能，包括：
    - 基本信息管理（姓名、年龄、学号、专业）
    - 成绩增删改查操作
    - 成绩统计分析（平均分、最高分、最低分）
    - 学生表现评估（及格科目、不及格科目、是否优秀学生）
    
    Attributes:
        name (str): 学生姓名
        age (int): 学生年龄
        student_id (str): 学号，用于唯一标识学生
        major (str): 所学专业
        scores (Dict[str, float]): 成绩字典，键为科目名称，值为成绩分数
        created_time (datetime): 学生信息创建时间戳
    """
    
    def __init__(self, name: str, age: int, student_id: str, major: str = ""):
        """
        初始化学生对象
        
        创建一个新的学生实例，初始化所有基本属性。
        成绩字典初始为空，创建时间自动设置为当前时间。
        
        Args:
            name (str): 学生姓名，不应为空
            age (int): 学生年龄，应为正整数
            student_id (str): 学号，应该是唯一的标识符
            major (str, optional): 专业名称，默认为空字符串
            
        Example:
            >>> student = Student("张三", 20, "2021001", "计算机科学")
            >>> print(student.name)
            张三
        """
        # 基本个人信息
        self.name = name  # 学生姓名
        self.age = age  # 学生年龄
        self.student_id = student_id  # 学号（唯一标识）
        self.major = major  # 所学专业
        
        # 成绩数据存储，使用字典结构：{科目名: 分数}
        self.scores: Dict[str, float] = {}  # 初始化空成绩字典
        
        # 记录学生信息创建的时间戳，用于跟踪和审计
        self.created_time = datetime.now()
    
    def add_score(self, subject: str, score: float) -> bool:
        """
        添加或更新科目成绩
        
        如果科目已存在，则更新其成绩；如果不存在，则添加新科目。
        成绩必须在0-100的有效范围内，否则操作失败。
        
        Args:
            subject (str): 科目名称，如"数学"、"英语"等
            score (float): 成绩分数，有效范围为0-100
            
        Returns:
            bool: 操作成功返回True，成绩无效返回False
            
        Example:
            >>> student.add_score("数学", 95)
            成功添加/更新 数学 成绩: 95
            True
            >>> student.add_score("英语", 150)  # 超出范围
            错误：成绩 150 不在有效范围内 (0-100)
            False
        """
        # 验证成绩的有效性：必须是数字类型且在0-100范围内
        if not isinstance(score, (int, float)) or score < 0 or score > 100:
            print(f"错误：成绩 {score} 不在有效范围内 (0-100)")
            return False
        
        # 将成绩存储到字典中，如果科目已存在则覆盖旧成绩
        self.scores[subject] = float(score)
        print(f"成功添加/更新 {subject} 成绩: {score}")
        return True
    
    def remove_score(self, subject: str) -> bool:
        """
        删除指定科目的成绩
        
        从成绩字典中移除指定科目及其成绩。
        如果科目不存在，操作失败并返回False。
        
        Args:
            subject (str): 要删除的科目名称
            
        Returns:
            bool: 删除成功返回True，科目不存在返回False
            
        Example:
            >>> student.add_score("物理", 80)
            >>> student.remove_score("物理")
            成功删除 物理 的成绩
            True
            >>> student.remove_score("化学")  # 不存在的科目
            错误：科目 化学 不存在
            False
        """
        # 检查科目是否存在于成绩字典中
        if subject in self.scores:
            # 从字典中删除该科目及其成绩
            del self.scores[subject]
            print(f"成功删除 {subject} 的成绩")
            return True
        else:
            # 科目不存在，无法删除
            print(f"错误：科目 {subject} 不存在")
            return False
    
    def get_score(self, subject: str) -> Optional[float]:
        """
        获取指定科目的成绩
        
        查询并返回指定科目的成绩分数。
        使用get方法安全地访问字典，避免KeyError异常。
        
        Args:
            subject (str): 科目名称
            
        Returns:
            Optional[float]: 如果科目存在，返回成绩分数；否则返回None
            
        Example:
            >>> student.add_score("数学", 95)
            >>> student.get_score("数学")
            95.0
            >>> student.get_score("化学")  # 不存在的科目
            None
        """
        # 使用字典的get方法安全地获取成绩，如果键不存在返回None
        return self.scores.get(subject)
    
    def get_all_scores(self) -> Dict[str, float]:
        """
        获取所有科目的成绩
        
        返回包含所有科目和对应成绩的字典副本。
        使用copy()方法返回副本，防止外部直接修改内部数据。
        
        Returns:
            Dict[str, float]: 包含所有科目和成绩的字典副本
            
        Example:
            >>> student.add_score("数学", 95)
            >>> student.add_score("英语", 87)
            >>> scores = student.get_all_scores()
            >>> print(scores)
            {'数学': 95.0, '英语': 87.0}
        """
        # 返回成绩字典的浅拷贝，保护内部数据不被外部修改
        return self.scores.copy()
    
    def get_average_score(self) -> float:
        """
        计算平均成绩
        
        将所有科目成绩求和后除以科目数量，得到平均分。
        如果没有任何成绩记录，返回0.0避免除零错误。
        
        Returns:
            float: 平均成绩分数，没有成绩时返回0.0
            
        Example:
            >>> student.add_score("数学", 90)
            >>> student.add_score("英语", 80)
            >>> student.get_average_score()
            85.0
        """
        # 如果成绩字典为空，返回0.0
        if not self.scores:
            return 0.0
        
        # 计算平均分：总分 / 科目数
        return sum(self.scores.values()) / len(self.scores)
    
    def get_highest_score(self) -> Optional[tuple]:
        """
        获取最高成绩及其科目
        
        遍历所有成绩，找出分数最高的科目及其成绩。
        使用max函数配合key参数实现高效查找。
        
        Returns:
            Optional[tuple]: 返回(科目名, 成绩)元组，没有成绩时返回None
            
        Example:
            >>> student.add_score("数学", 95)
            >>> student.add_score("英语", 87)
            >>> student.get_highest_score()
            ('数学', 95.0)
        """
        # 如果没有成绩记录，返回None
        if not self.scores:
            return None
        
        # 使用max函数找出成绩最高的科目，key参数指定比较依据为成绩值
        max_subject = max(self.scores, key=self.scores.get)
        # 返回科目名和对应的成绩组成的元组
        return (max_subject, self.scores[max_subject])
    
    def get_lowest_score(self) -> Optional[tuple]:
        """
        获取最低成绩及其科目
        
        遍历所有成绩，找出分数最低的科目及其成绩。
        使用min函数配合key参数实现高效查找。
        
        Returns:
            Optional[tuple]: 返回(科目名, 成绩)元组，没有成绩时返回None
            
        Example:
            >>> student.add_score("数学", 95)
            >>> student.add_score("英语", 87)
            >>> student.get_lowest_score()
            ('英语', 87.0)
        """
        # 如果没有成绩记录，返回None
        if not self.scores:
            return None
        
        # 使用min函数找出成绩最低的科目，key参数指定比较依据为成绩值
        min_subject = min(self.scores, key=self.scores.get)
        # 返回科目名和对应的成绩组成的元组
        return (min_subject, self.scores[min_subject])
    
    def get_passing_subjects(self, passing_score: float = 60.0) -> List[str]:
        """
        获取及格的科目列表
        
        筛选出所有成绩达到或超过及格分数线的科目。
        使用列表推导式实现简洁高效的过滤操作。
        
        Args:
            passing_score (float): 及格分数线，默认为60分，可根据需要自定义
            
        Returns:
            List[str]: 包含所有及格科目名称的列表
            
        Example:
            >>> student.add_score("数学", 95)
            >>> student.add_score("英语", 55)
            >>> student.get_passing_subjects()
            ['数学']
            >>> student.get_passing_subjects(passing_score=50)
            ['数学', '英语']
        """
        # 使用列表推导式筛选成绩大于等于及格线的科目
        return [subject for subject, score in self.scores.items() if score >= passing_score]
    
    def get_failing_subjects(self, passing_score: float = 60.0) -> List[str]:
        """
        获取不及格的科目列表
        
        筛选出所有成绩低于及格分数线的科目。
        这些科目需要学生重点关注和改进。
        
        Args:
            passing_score (float): 及格分数线，默认为60分，可根据需要自定义
            
        Returns:
            List[str]: 包含所有不及格科目名称的列表
            
        Example:
            >>> student.add_score("数学", 95)
            >>> student.add_score("英语", 55)
            >>> student.get_failing_subjects()
            ['英语']
        """
        # 使用列表推导式筛选成绩低于及格线的科目
        return [subject for subject, score in self.scores.items() if score < passing_score]
    
    def is_excellent_student(self, excellent_threshold: float = 85.0) -> bool:
        """
        判断是否为优秀学生
        
        优秀学生的标准：
        1. 平均成绩达到或超过优秀阈值（默认85分）
        2. 没有任何不及格科目（所有科目均>=60分）
        
        Args:
            excellent_threshold (float): 优秀学生平均分阈值，默认85分
            
        Returns:
            bool: 满足优秀学生条件返回True，否则返回False
            
        Example:
            >>> student.add_score("数学", 90)
            >>> student.add_score("英语", 88)
            >>> student.is_excellent_student()
            True
            >>> student.add_score("物理", 55)  # 添加一个不及格成绩
            >>> student.is_excellent_student()
            False
        """
        # 计算平均成绩
        avg_score = self.get_average_score()
        
        # 同时满足两个条件：平均分达标 且 没有不及格科目
        return avg_score >= excellent_threshold and len(self.get_failing_subjects()) == 0
    
    def get_student_info(self) -> str:
        """
        获取学生详细信息的格式化字符串
        
        生成包含学生基本信息、成绩详情和统计分析的完整报告。
        报告分为三个部分：
        1. 学生基本信息（姓名、年龄、学号、专业、注册时间）
        2. 成绩信息（各科目成绩列表）
        3. 统计信息（平均分、最高分、最低分、及格率、学习状态）
        
        Returns:
            str: 格式化的学生完整信息报告字符串
            
        Example:
            >>> student = Student("张三", 20, "2021001", "计算机科学")
            >>> student.add_score("数学", 95)
            >>> print(student.get_student_info())
            === 学生信息 ===
            姓名: 张三
            ...
        """
        # 构建学生基本信息部分
        info = f"""
=== 学生信息 ===
姓名: {self.name}
年龄: {self.age}
学号: {self.student_id}
专业: {self.major}
注册时间: {self.created_time.strftime('%Y-%m-%d %H:%M:%S')}

=== 成绩信息 ===
"""
        
        # 检查是否有成绩记录
        if not self.scores:
            # 没有成绩时显示提示信息
            info += "暂无成绩记录\n"
        else:
            # 遍历并显示所有科目的成绩
            for subject, score in self.scores.items():
                info += f"{subject}: {score:.1f}分\n"
            
            # 添加统计信息部分
            info += f"\n=== 统计信息 ===\n"
            
            # 显示平均成绩（保留2位小数）
            info += f"平均成绩: {self.get_average_score():.2f}分\n"
            
            # 显示最高成绩及科目
            highest = self.get_highest_score()
            if highest:
                info += f"最高成绩: {highest[0]} ({highest[1]:.1f}分)\n"
            
            # 显示最低成绩及科目
            lowest = self.get_lowest_score()
            if lowest:
                info += f"最低成绩: {lowest[0]} ({lowest[1]:.1f}分)\n"
            
            # 显示及格科目统计
            passing_subjects = self.get_passing_subjects()
            info += f"及格科目数: {len(passing_subjects)}/{len(self.scores)}\n"
            
            # 根据成绩表现评估学习状态
            if self.is_excellent_student():
                info += "学习状态: 优秀学生 🌟\n"  # 平均分>=85且无不及格
            elif len(self.get_failing_subjects()) == 0:
                info += "学习状态: 良好\n"  # 无不及格但平均分<85
            else:
                info += "学习状态: 需要努力\n"  # 存在不及格科目
        
        return info
    
    def __str__(self) -> str:
        """
        字符串表示方法
        
        当使用str()或print()函数时调用此方法。
        返回学生对象的简洁字符串表示，包含关键信息。
        
        Returns:
            str: 学生对象的字符串表示
            
        Example:
            >>> student = Student("张三", 20, "2021001")
            >>> print(student)
            Student(name='张三', student_id='2021001', scores_count=0)
        """
        return f"Student(name='{self.name}', student_id='{self.student_id}', scores_count={len(self.scores)})"
    
    def __repr__(self) -> str:
        """
        对象表示方法
        
        当在交互式解释器中直接输入对象名或使用repr()函数时调用。
        通常应返回一个能够重建对象的表达式字符串，这里简化为与__str__相同。
        
        Returns:
            str: 学生对象的官方字符串表示
            
        Example:
            >>> student = Student("张三", 20, "2021001")
            >>> student
            Student(name='张三', student_id='2021001', scores_count=0)
        """
        return self.__str__()


def demonstrate_student_management():
    """
    演示学生管理功能
    
    这是一个完整的演示函数，展示Student类的主要功能：
    1. 创建学生对象
    2. 添加和管理成绩
    3. 查询和统计成绩信息
    4. 删除成绩记录
    
    该函数可作为使用示例和测试用途。
    """
    print("=== 学生管理系统演示 ===\n")
    
    # 步骤1: 创建两个学生对象用于演示
    student1 = Student("张三", 20, "2021001", "计算机科学与技术")
    student2 = Student("李四", 19, "2021002", "数学与应用数学")
    
    # 步骤2: 为学生添加多门课程的成绩
    print("1. 添加学生成绩:")
    student1.add_score("高等数学", 92)  # 为张三添加高等数学成绩
    student1.add_score("程序设计", 88)  # 为张三添加程序设计成绩
    student1.add_score("英语", 76)      # 为张三添加英语成绩
    student1.add_score("物理", 84)      # 为张三添加物理成绩
    
    student2.add_score("高等数学", 95)  # 为李四添加高等数学成绩
    student2.add_score("线性代数", 87)  # 为李四添加线性代数成绩
    student2.add_score("英语", 82)      # 为李四添加英语成绩
    
    # 步骤3: 显示两个学生的完整信息报告
    print("\n2. 显示学生信息:")
    print(student1.get_student_info())  # 显示张三的详细信息
    print(student2.get_student_info())  # 显示李四的详细信息
    
    # 步骤4: 演示成绩查询和删除操作
    print("3. 成绩操作演示:")
    # 查询单科成绩
    print(f"张三的程序设计成绩: {student1.get_score('程序设计')}")
    # 删除一门课程的成绩
    student1.remove_score("物理")
    # 查看删除后的平均分变化
    print(f"删除物理成绩后的平均分: {student1.get_average_score():.2f}")


# 主程序入口
# 当直接运行此文件时（而非被导入时），执行演示函数
if __name__ == "__main__":
    # 运行学生管理系统的功能演示
    demonstrate_student_management()