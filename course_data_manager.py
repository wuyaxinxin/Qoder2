#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: course_data_manager.py
作者: 开发者
创建日期: 2025-10-16
版本: 1.0
描述: 课程数据持久化管理模块
      提供课程数据的保存、加载、备份等功能
"""

import json
import os
from typing import Dict, Any, Optional
from pathlib import Path
from datetime import datetime
from course import Course
from course_management_system import CourseManagementSystem


class CourseDataManager:
    """课程数据管理器类"""
    
    def __init__(self, data_dir: str = "data", filename: str = "courses_data.json"):
        """
        初始化课程数据管理器
        
        Args:
            data_dir (str): 数据目录路径
            filename (str): 课程数据文件名
        """
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)
        self.filename = filename
        self.file_path = self.data_dir / filename
        
        # 备份目录
        self.backups_dir = self.data_dir / "backups"
        self.backups_dir.mkdir(exist_ok=True)
    
    def save_courses(self, course_system: CourseManagementSystem) -> bool:
        """
        保存课程数据到JSON文件
        
        Args:
            course_system (CourseManagementSystem): 课程管理系统对象
            
        Returns:
            bool: 保存成功返回True，否则返回False
        """
        try:
            # 构建数据结构
            data = {
                'courses': {},
                'enrollments': course_system.enrollments.copy(),
                'metadata': {
                    'total_courses': course_system.get_course_count(),
                    'total_enrollments': course_system.get_enrollment_count(),
                    'last_updated': datetime.now().isoformat(),
                    'version': '1.0'
                }
            }
            
            # 转换课程对象为字典
            for course_id, course in course_system.courses.items():
                data['courses'][course_id] = course.to_dict()
            
            # 保存到文件
            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2, default=str)
            
            print(f"✓ 课程数据已保存到 {self.file_path}")
            return True
            
        except Exception as e:
            print(f"错误：保存课程数据失败 - {e}")
            return False
    
    def load_courses(self, course_system: CourseManagementSystem) -> bool:
        """
        从JSON文件加载课程数据
        
        Args:
            course_system (CourseManagementSystem): 课程管理系统对象
            
        Returns:
            bool: 加载成功返回True，否则返回False
        """
        try:
            if not self.file_path.exists():
                print(f"提示：课程数据文件不存在，将创建新文件")
                return False
            
            with open(self.file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # 清空现有数据
            course_system.courses.clear()
            course_system.enrollments.clear()
            
            # 加载课程数据
            if 'courses' in data:
                for course_id, course_data in data['courses'].items():
                    course = Course.from_dict(course_data)
                    course_system.courses[course_id] = course
            
            # 加载选课记录
            if 'enrollments' in data:
                course_system.enrollments = data['enrollments']
            
            print(f"✓ 成功加载 {len(course_system.courses)} 门课程，{len(course_system.enrollments)} 条选课记录")
            return True
            
        except Exception as e:
            print(f"错误：加载课程数据失败 - {e}")
            return False
    
    def backup_courses(self, backup_name: str = None) -> bool:
        """
        备份课程数据文件
        
        Args:
            backup_name (str): 备份文件名，默认自动生成
            
        Returns:
            bool: 备份成功返回True，否则返回False
        """
        try:
            if not self.file_path.exists():
                print(f"错误：源文件不存在，无法备份")
                return False
            
            if backup_name is None:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                backup_name = f"courses_backup_{timestamp}.json"
            
            backup_path = self.backups_dir / backup_name
            
            import shutil
            shutil.copy2(self.file_path, backup_path)
            
            print(f"✓ 课程数据已备份到 {backup_path}")
            return True
            
        except Exception as e:
            print(f"错误：备份课程数据失败 - {e}")
            return False
    
    def restore_backup(self, backup_name: str) -> bool:
        """
        从备份恢复课程数据
        
        Args:
            backup_name (str): 备份文件名
            
        Returns:
            bool: 恢复成功返回True，否则返回False
        """
        try:
            backup_path = self.backups_dir / backup_name
            
            if not backup_path.exists():
                print(f"错误：备份文件 {backup_name} 不存在")
                return False
            
            import shutil
            shutil.copy2(backup_path, self.file_path)
            
            print(f"✓ 课程数据已从 {backup_name} 恢复")
            return True
            
        except Exception as e:
            print(f"错误：恢复课程数据失败 - {e}")
            return False
    
    def export_courses_csv(self, course_system: CourseManagementSystem, 
                          export_name: str = None) -> bool:
        """
        导出课程数据为CSV格式
        
        Args:
            course_system (CourseManagementSystem): 课程管理系统对象
            export_name (str): 导出文件名
            
        Returns:
            bool: 导出成功返回True，否则返回False
        """
        try:
            import csv
            
            exports_dir = self.data_dir / "exports"
            exports_dir.mkdir(exist_ok=True)
            
            if export_name is None:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                export_name = f"courses_export_{timestamp}.csv"
            
            export_path = exports_dir / export_name
            
            with open(export_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                
                # 写入表头
                headers = ['课程ID', '课程名称', '教师', '学分', '容量', 
                          '已选人数', '选课率%', '学期', '上课时间']
                writer.writerow(headers)
                
                # 写入数据
                for course in course_system.courses.values():
                    row = [
                        course.course_id,
                        course.course_name,
                        course.teacher,
                        course.credit,
                        course.capacity,
                        course.enrolled_count,
                        f"{course.get_enrollment_rate():.1f}",
                        course.semester,
                        course.schedule
                    ]
                    writer.writerow(row)
            
            print(f"✓ 课程数据已导出到 {export_path}")
            return True
            
        except Exception as e:
            print(f"错误：导出课程数据失败 - {e}")
            return False
    
    def list_backups(self) -> list:
        """
        列出所有备份文件
        
        Returns:
            list: 备份文件列表
        """
        try:
            backups = [f.name for f in self.backups_dir.iterdir() 
                      if f.is_file() and f.name.endswith('.json')]
            return sorted(backups, reverse=True)
        except Exception as e:
            print(f"错误：获取备份列表失败 - {e}")
            return []
