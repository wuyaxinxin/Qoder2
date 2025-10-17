#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: validator.py
作者: 开发者
创建日期: 2025-10-11
版本: 1.0
描述: 数据验证模块
      提供各种数据验证功能
"""

import re
from typing import Any, List, Dict, Optional, Union
from datetime import datetime


class Validator:
    """数据验证器类"""
    
    @staticmethod
    def is_empty(value: Any) -> bool:
        """检查值是否为空"""
        if value is None:
            return True
        if isinstance(value, (str, list, dict, tuple)):
            return len(value) == 0
        return False
    
    @staticmethod
    def is_email(email: str) -> bool:
        """验证邮箱格式"""
        if not isinstance(email, str):
            return False
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    @staticmethod
    def is_phone(phone: str) -> bool:
        """验证手机号格式（中国大陆）"""
        if not isinstance(phone, str):
            return False
        pattern = r'^1[3-9]\d{9}$'
        return re.match(pattern, phone) is not None
    
    @staticmethod
    def is_number(value: Any) -> bool:
        """检查是否为数字"""
        try:
            float(value)
            return True
        except (ValueError, TypeError):
            return False
    
    @staticmethod
    def is_integer(value: Any) -> bool:
        """检查是否为整数"""
        try:
            int(value)
            return isinstance(value, int) or str(value).isdigit()
        except (ValueError, TypeError):
            return False
    
    @staticmethod
    def is_in_range(value: Union[int, float], min_val: Union[int, float], max_val: Union[int, float]) -> bool:
        """检查数值是否在指定范围内"""
        try:
            num_value = float(value)
            return min_val <= num_value <= max_val
        except (ValueError, TypeError):
            return False
    
    @staticmethod
    def is_length_valid(text: str, min_length: int = 0, max_length: int = None) -> bool:
        """验证字符串长度"""
        if not isinstance(text, str):
            return False
        
        length = len(text)
        if length < min_length:
            return False
        
        if max_length is not None and length > max_length:
            return False
        
        return True
    
    @staticmethod
    def validate_student_id(student_id: str) -> bool:
        """验证学号格式（4位年份+3位序号）"""
        if not isinstance(student_id, str):
            return False
        pattern = r'^20\d{2}\d{3}$'
        return re.match(pattern, student_id) is not None
    
    @staticmethod
    def validate_score(score: Any) -> bool:
        """验证成绩（0-100）"""
        if not Validator.is_number(score):
            return False
        return Validator.is_in_range(score, 0, 100)
    
    @staticmethod
    def validate_age(age: Any) -> bool:
        """验证年龄（0-150）"""
        if not Validator.is_integer(age):
            return False
        return Validator.is_in_range(age, 0, 150)
    
    @staticmethod
    def validate_required_fields(data: Dict[str, Any], required_fields: List[str]) -> List[str]:
        """验证必填字段"""
        missing_fields = []
        for field in required_fields:
            if field not in data or Validator.is_empty(data[field]):
                missing_fields.append(field)
        return missing_fields
    
    @staticmethod
    def validate_data_types(data: Dict[str, Any], type_mapping: Dict[str, type]) -> List[str]:
        """验证数据类型"""
        invalid_fields = []
        for field, expected_type in type_mapping.items():
            if field in data and not isinstance(data[field], expected_type):
                invalid_fields.append(f"{field} 应为 {expected_type.__name__} 类型")
        return invalid_fields


    @staticmethod
    def validate_course_id(course_id: str) -> bool:
        """
        验证课程ID格式（2-3个大写字母 + 3位数字，如CS101）
        
        Args:
            course_id (str): 课程ID
            
        Returns:
            bool: 格式正确返回True，否则返回False
        """
        if not isinstance(course_id, str):
            return False
        pattern = r'^[A-Z]{2,3}\d{3}$'
        return re.match(pattern, course_id) is not None
    
    @staticmethod
    def validate_credit(credit: Any) -> bool:
        """
        验证学分（0.5-10.0）
        
        Args:
            credit (Any): 学分值
            
        Returns:
            bool: 有效返回True，否则返回False
        """
        if not Validator.is_number(credit):
            return False
        return Validator.is_in_range(credit, 0.5, 10.0)
    
    @staticmethod
    def validate_capacity(capacity: Any) -> bool:
        """
        验证课程容量（1-500的正整数）
        
        Args:
            capacity (Any): 课程容量
            
        Returns:
            bool: 有效返回True，否则返回False
        """
        if not Validator.is_integer(capacity):
            return False
        return Validator.is_in_range(capacity, 1, 500)
    
    @staticmethod
    def validate_course_name(course_name: str) -> bool:
        """
        验证课程名称（2-50字符）
        
        Args:
            course_name (str): 课程名称
            
        Returns:
            bool: 有效返回True，否则返回False
        """
        return Validator.is_length_valid(course_name, 2, 50)
    
    @staticmethod
    def validate_semester(semester: str) -> bool:
        """
        验证学期格式（年份+季节，如2024春季）
        
        Args:
            semester (str): 学期
            
        Returns:
            bool: 格式正确返回True，否则返回False
        """
        if not isinstance(semester, str):
            return False
        # 支持格式: 2024春季, 2024秋季, 2024-1, 2024-2等
        pattern = r'^20\d{2}[春夏秋冬季]|20\d{2}-[12]$'
        return re.match(pattern, semester) is not None or semester == ""


class ValidationError(Exception):
    """验证错误异常"""
    
    def __init__(self, message: str, field: str = None):
        self.message = message
        self.field = field
        super().__init__(self.message)