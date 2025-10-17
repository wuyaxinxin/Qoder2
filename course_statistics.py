#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: course_statistics.py
作者: 开发者
创建日期: 2025-10-16
版本: 1.0
描述: 课程统计分析模块
      提供课程相关的统计分析功能
"""

from typing import Dict, List, Any, Tuple
from course_management_system import CourseManagementSystem


class CourseStatistics:
    """课程统计分析类"""
    
    def __init__(self, course_system: CourseManagementSystem):
        """
        初始化课程统计分析器
        
        Args:
            course_system (CourseManagementSystem): 课程管理系统对象
        """
        self.course_system = course_system
    
    def get_course_score_statistics(self, course_id: str) -> Dict[str, Any]:
        """
        获取课程成绩统计信息
        
        Args:
            course_id (str): 课程ID
            
        Returns:
            Dict[str, Any]: 统计信息字典
        """
        course = self.course_system.get_course(course_id)
        if not course:
            return {}
        
        scores = []
        for key, enrollment in self.course_system.enrollments.items():
            if enrollment['course_id'] == course_id and enrollment['status'] == 'enrolled':
                score = enrollment.get('score')
                if score is not None:
                    scores.append(float(score))
        
        if not scores:
            return {
                'course_id': course_id,
                'course_name': course.course_name,
                'has_scores': False,
                'message': '暂无成绩数据'
            }
        
        # 计算统计指标
        avg_score = sum(scores) / len(scores)
        max_score = max(scores)
        min_score = min(scores)
        
        # 优秀率(≥85分)
        excellent_count = sum(1 for s in scores if s >= 85)
        excellent_rate = (excellent_count / len(scores)) * 100
        
        # 及格率(≥60分)
        pass_count = sum(1 for s in scores if s >= 60)
        pass_rate = (pass_count / len(scores)) * 100
        
        # 分数段分布
        score_distribution = {
            '90-100': sum(1 for s in scores if 90 <= s <= 100),
            '80-89': sum(1 for s in scores if 80 <= s < 90),
            '70-79': sum(1 for s in scores if 70 <= s < 80),
            '60-69': sum(1 for s in scores if 60 <= s < 70),
            '0-59': sum(1 for s in scores if s < 60)
        }
        
        return {
            'course_id': course_id,
            'course_name': course.course_name,
            'teacher': course.teacher,
            'has_scores': True,
            'total_students': len(scores),
            'average_score': round(avg_score, 2),
            'max_score': max_score,
            'min_score': min_score,
            'excellent_count': excellent_count,
            'excellent_rate': round(excellent_rate, 2),
            'pass_count': pass_count,
            'pass_rate': round(pass_rate, 2),
            'fail_count': len(scores) - pass_count,
            'score_distribution': score_distribution
        }
    
    def get_student_credit_statistics(self, student_id: str) -> Dict[str, Any]:
        """
        获取学生学分统计信息
        
        Args:
            student_id (str): 学生学号
            
        Returns:
            Dict[str, Any]: 学分统计信息
        """
        enrolled_courses = []
        total_credits = 0.0
        earned_credits = 0.0
        total_score_credits = 0.0
        
        for key, enrollment in self.course_system.enrollments.items():
            if enrollment['student_id'] == student_id and enrollment['status'] == 'enrolled':
                course_id = enrollment['course_id']
                course = self.course_system.get_course(course_id)
                
                if course:
                    enrolled_courses.append(course_id)
                    total_credits += course.credit
                    
                    score = enrollment.get('score')
                    if score is not None and score >= 60:
                        earned_credits += course.credit
                    
                    if score is not None:
                        total_score_credits += score * course.credit
        
        # 计算GPA(加权平均分)
        gpa = 0.0
        if total_credits > 0 and total_score_credits > 0:
            gpa = total_score_credits / total_credits
        
        return {
            'student_id': student_id,
            'total_courses': len(enrolled_courses),
            'total_credits': round(total_credits, 1),
            'earned_credits': round(earned_credits, 1),
            'remaining_credits': round(total_credits - earned_credits, 1),
            'gpa': round(gpa, 2),
            'enrolled_courses': enrolled_courses
        }
    
    def get_popular_courses(self, top_n: int = 10) -> List[Dict[str, Any]]:
        """
        获取最热门课程(按选课人数排序)
        
        Args:
            top_n (int): 返回前N个课程
            
        Returns:
            List[Dict[str, Any]]: 热门课程列表
        """
        courses_list = []
        
        for course in self.course_system.courses.values():
            courses_list.append({
                'course_id': course.course_id,
                'course_name': course.course_name,
                'teacher': course.teacher,
                'credit': course.credit,
                'capacity': course.capacity,
                'enrolled_count': course.enrolled_count,
                'enrollment_rate': round(course.get_enrollment_rate(), 2)
            })
        
        # 按选课人数排序
        courses_list.sort(key=lambda x: x['enrolled_count'], reverse=True)
        
        return courses_list[:top_n]
    
    def get_teacher_statistics(self, teacher_name: str) -> Dict[str, Any]:
        """
        获取教师课程统计信息
        
        Args:
            teacher_name (str): 教师姓名
            
        Returns:
            Dict[str, Any]: 教师统计信息
        """
        teacher_courses = []
        total_students = 0
        total_capacity = 0
        
        for course in self.course_system.courses.values():
            if teacher_name in course.teacher:
                teacher_courses.append({
                    'course_id': course.course_id,
                    'course_name': course.course_name,
                    'enrolled_count': course.enrolled_count,
                    'capacity': course.capacity,
                    'enrollment_rate': round(course.get_enrollment_rate(), 2)
                })
                total_students += course.enrolled_count
                total_capacity += course.capacity
        
        avg_enrollment_rate = 0.0
        if total_capacity > 0:
            avg_enrollment_rate = (total_students / total_capacity) * 100
        
        return {
            'teacher_name': teacher_name,
            'total_courses': len(teacher_courses),
            'total_students': total_students,
            'total_capacity': total_capacity,
            'avg_enrollment_rate': round(avg_enrollment_rate, 2),
            'courses': teacher_courses
        }
    
    def get_semester_statistics(self, semester: str) -> Dict[str, Any]:
        """
        获取学期课程统计信息
        
        Args:
            semester (str): 学期
            
        Returns:
            Dict[str, Any]: 学期统计信息
        """
        semester_courses = []
        total_students = 0
        total_capacity = 0
        
        for course in self.course_system.courses.values():
            if course.semester == semester:
                semester_courses.append({
                    'course_id': course.course_id,
                    'course_name': course.course_name,
                    'teacher': course.teacher,
                    'enrolled_count': course.enrolled_count,
                    'capacity': course.capacity
                })
                total_students += course.enrolled_count
                total_capacity += course.capacity
        
        avg_enrollment_rate = 0.0
        if total_capacity > 0:
            avg_enrollment_rate = (total_students / total_capacity) * 100
        
        return {
            'semester': semester,
            'total_courses': len(semester_courses),
            'total_students': total_students,
            'total_capacity': total_capacity,
            'avg_enrollment_rate': round(avg_enrollment_rate, 2),
            'courses': semester_courses
        }
    
    def get_overall_statistics(self) -> Dict[str, Any]:
        """
        获取课程系统总体统计信息
        
        Returns:
            Dict[str, Any]: 总体统计信息
        """
        total_courses = self.course_system.get_course_count()
        total_enrollments = self.course_system.get_enrollment_count()
        
        total_capacity = sum(c.capacity for c in self.course_system.courses.values())
        total_enrolled = sum(c.enrolled_count for c in self.course_system.courses.values())
        
        avg_enrollment_rate = 0.0
        if total_capacity > 0:
            avg_enrollment_rate = (total_enrolled / total_capacity) * 100
        
        # 统计有成绩的选课记录
        scored_enrollments = sum(1 for e in self.course_system.enrollments.values() 
                                if e.get('score') is not None and e.get('status') == 'enrolled')
        
        # 统计不同学期的课程数
        semesters = {}
        for course in self.course_system.courses.values():
            if course.semester:
                semesters[course.semester] = semesters.get(course.semester, 0) + 1
        
        # 统计教师数量
        teachers = set(course.teacher for course in self.course_system.courses.values())
        
        return {
            'total_courses': total_courses,
            'total_enrollments': total_enrollments,
            'total_capacity': total_capacity,
            'total_enrolled': total_enrolled,
            'available_seats': total_capacity - total_enrolled,
            'avg_enrollment_rate': round(avg_enrollment_rate, 2),
            'scored_enrollments': scored_enrollments,
            'total_teachers': len(teachers),
            'total_semesters': len(semesters),
            'semesters_detail': semesters
        }
    
    def generate_course_report(self, course_id: str) -> str:
        """
        生成课程详细报告
        
        Args:
            course_id (str): 课程ID
            
        Returns:
            str: 格式化的课程报告
        """
        course = self.course_system.get_course(course_id)
        if not course:
            return f"错误：课程 {course_id} 不存在"
        
        stats = self.get_course_score_statistics(course_id)
        
        report = f"""
{'='*50}
课程分析报告
{'='*50}

【基本信息】
课程ID: {course.course_id}
课程名称: {course.course_name}
授课教师: {course.teacher}
学分: {course.credit}
学期: {course.semester}
上课时间: {course.schedule}

【选课情况】
课程容量: {course.capacity}人
已选人数: {course.enrolled_count}人
剩余名额: {course.get_available_seats()}人
选课率: {course.get_enrollment_rate():.1f}%
"""
        
        if stats.get('has_scores'):
            report += f"""
【成绩统计】
参与统计人数: {stats['total_students']}人
平均分: {stats['average_score']:.2f}
最高分: {stats['max_score']:.1f}
最低分: {stats['min_score']:.1f}
优秀率(≥85): {stats['excellent_rate']:.1f}% ({stats['excellent_count']}人)
及格率(≥60): {stats['pass_rate']:.1f}% ({stats['pass_count']}人)
不及格人数: {stats['fail_count']}人

【分数段分布】
90-100分: {stats['score_distribution']['90-100']}人
80-89分: {stats['score_distribution']['80-89']}人
70-79分: {stats['score_distribution']['70-79']}人
60-69分: {stats['score_distribution']['60-69']}人
0-59分: {stats['score_distribution']['0-59']}人
"""
        else:
            report += "\n【成绩统计】\n暂无成绩数据\n"
        
        report += f"\n{'='*50}\n"
        
        return report
