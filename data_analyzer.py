#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
数据统计分析模块
提供学生成绩的统计分析功能，包括成绩分布、排名、趋势分析等
"""

import json
from typing import List, Dict, Tuple
from collections import Counter


class DataAnalyzer:
    """数据分析器类 - 提供各种统计分析功能"""
    
    def __init__(self, students_data: List[Dict] = None):
        """
        初始化数据分析器
        
        Args:
            students_data: 学生数据列表
        """
        self.students_data = students_data or []
    
    def analyze_score_distribution(self, subject: str = None) -> Dict[str, int]:
        """
        分析成绩分布情况
        
        Args:
            subject: 科目名称，如果为None则分析平均分
            
        Returns:
            成绩等级分布字典 {'优秀': count, '良好': count, '中等': count, '及格': count, '不及格': count}
        """
        distribution = {
            '优秀(90-100)': 0,
            '良好(80-89)': 0,
            '中等(70-79)': 0,
            '及格(60-69)': 0,
            '不及格(0-59)': 0
        }
        
        for student in self.students_data:
            if subject and subject in student.get('scores', {}):
                score = student['scores'][subject]
            else:
                # 计算平均分
                scores = student.get('scores', {}).values()
                if not scores:
                    continue
                score = sum(scores) / len(scores)
            
            # 分类统计
            if score >= 90:
                distribution['优秀(90-100)'] += 1
            elif score >= 80:
                distribution['良好(80-89)'] += 1
            elif score >= 70:
                distribution['中等(70-79)'] += 1
            elif score >= 60:
                distribution['及格(60-69)'] += 1
            else:
                distribution['不及格(0-59)'] += 1
        
        return distribution
    
    def get_top_students(self, top_n: int = 10) -> List[Tuple[str, str, float]]:
        """
        获取成绩前N名的学生
        
        Args:
            top_n: 返回前N名学生
            
        Returns:
            学生列表 [(学号, 姓名, 平均分), ...]
        """
        student_scores = []
        
        for student in self.students_data:
            scores = student.get('scores', {}).values()
            if scores:
                avg_score = sum(scores) / len(scores)
                student_scores.append((
                    student.get('student_id', 'N/A'),
                    student.get('name', 'N/A'),
                    avg_score
                ))
        
        # 按平均分降序排序
        student_scores.sort(key=lambda x: x[2], reverse=True)
        
        return student_scores[:top_n]
    
    def calculate_statistics(self) -> Dict[str, float]:
        """
        计算全体学生的统计数据
        
        Returns:
            统计数据字典
        """
        all_avg_scores = []
        
        for student in self.students_data:
            scores = student.get('scores', {}).values()
            if scores:
                avg_score = sum(scores) / len(scores)
                all_avg_scores.append(avg_score)
        
        if not all_avg_scores:
            return {
                'total_students': 0,
                'average_score': 0.0,
                'highest_score': 0.0,
                'lowest_score': 0.0,
                'pass_rate': 0.0
            }
        
        passed = sum(1 for score in all_avg_scores if score >= 60)
        
        return {
            'total_students': len(all_avg_scores),
            'average_score': sum(all_avg_scores) / len(all_avg_scores),
            'highest_score': max(all_avg_scores),
            'lowest_score': min(all_avg_scores),
            'pass_rate': (passed / len(all_avg_scores)) * 100
        }
    
    def analyze_subject_performance(self) -> Dict[str, Dict[str, float]]:
        """
        分析各科目表现
        
        Returns:
            各科目统计数据
        """
        subject_scores = {}
        
        # 收集所有科目的成绩
        for student in self.students_data:
            for subject, score in student.get('scores', {}).items():
                if subject not in subject_scores:
                    subject_scores[subject] = []
                subject_scores[subject].append(score)
        
        # 计算每个科目的统计信息
        result = {}
        for subject, scores in subject_scores.items():
            if scores:
                result[subject] = {
                    'average': sum(scores) / len(scores),
                    'highest': max(scores),
                    'lowest': min(scores),
                    'student_count': len(scores)
                }
        
        return result
    
    def generate_report(self) -> str:
        """
        生成完整的分析报告
        
        Returns:
            格式化的报告字符串
        """
        report = []
        report.append("=" * 60)
        report.append("学生成绩数据分析报告".center(56))
        report.append("=" * 60)
        
        # 整体统计
        stats = self.calculate_statistics()
        report.append("\n【整体统计】")
        report.append(f"  总学生数: {stats['total_students']}")
        report.append(f"  平均分: {stats['average_score']:.2f}")
        report.append(f"  最高分: {stats['highest_score']:.2f}")
        report.append(f"  最低分: {stats['lowest_score']:.2f}")
        report.append(f"  及格率: {stats['pass_rate']:.2f}%")
        
        # 成绩分布
        distribution = self.analyze_score_distribution()
        report.append("\n【成绩分布】")
        for grade, count in distribution.items():
            report.append(f"  {grade}: {count}人")
        
        # 前10名学生
        top_students = self.get_top_students(10)
        report.append("\n【成绩前10名】")
        for i, (sid, name, score) in enumerate(top_students, 1):
            report.append(f"  {i}. {name} ({sid}) - {score:.2f}分")
        
        # 科目分析
        subject_perf = self.analyze_subject_performance()
        report.append("\n【各科目表现】")
        for subject, data in subject_perf.items():
            report.append(f"  {subject}:")
            report.append(f"    平均分: {data['average']:.2f}")
            report.append(f"    最高分: {data['highest']:.2f}")
            report.append(f"    参与人数: {data['student_count']}")
        
        report.append("\n" + "=" * 60)
        
        return "\n".join(report)


# 演示代码
if __name__ == "__main__":
    # 示例数据
    sample_data = [
        {
            "student_id": "S001",
            "name": "张三",
            "scores": {"语文": 92, "数学": 88, "英语": 95}
        },
        {
            "student_id": "S002",
            "name": "李四",
            "scores": {"语文": 78, "数学": 82, "英语": 75}
        },
        {
            "student_id": "S003",
            "name": "王五",
            "scores": {"语文": 85, "数学": 90, "英语": 88}
        },
        {
            "student_id": "S004",
            "name": "赵六",
            "scores": {"语文": 55, "数学": 62, "英语": 58}
        }
    ]
    
    # 创建分析器
    analyzer = DataAnalyzer(sample_data)
    
    # 生成并打印报告
    print(analyzer.generate_report())
    
    print("\n\n【科目成绩分布 - 数学】")
    math_dist = analyzer.analyze_score_distribution("数学")
    for grade, count in math_dist.items():
        print(f"{grade}: {count}人")
