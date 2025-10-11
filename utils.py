#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: utils.py
作者: 开发者
创建日期: 2025-10-11
版本: 1.0
描述: 通用工具函数集合
      提供常用的字符串处理、日期时间、文件操作等工具函数
"""

import os
import re
import json
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional


def format_timestamp(timestamp: datetime = None, format_str: str = "%Y-%m-%d %H:%M:%S") -> str:
    """格式化时间戳"""
    if timestamp is None:
        timestamp = datetime.now()
    return timestamp.strftime(format_str)


def validate_email(email: str) -> bool:
    """验证邮箱格式"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def clean_string(text: str) -> str:
    """清理字符串，去除多余空格和特殊字符"""
    return re.sub(r'\s+', ' ', text.strip())


def safe_divide(a: float, b: float, default: float = 0.0) -> float:
    """安全除法，避免除零错误"""
    return a / b if b != 0 else default


def ensure_directory(path: str) -> bool:
    """确保目录存在，不存在则创建"""
    try:
        os.makedirs(path, exist_ok=True)
        return True
    except Exception:
        return False


def get_file_size(file_path: str) -> int:
    """获取文件大小（字节）"""
    try:
        return os.path.getsize(file_path)
    except Exception:
        return 0


def truncate_string(text: str, max_length: int = 50, suffix: str = "...") -> str:
    """截断字符串"""
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix