#!/usr/bin/env python3
# -*- coding: utf-8 -*-

<<<<<<< Local
"""
数据处理模块
提供数据清洗、转换和处理功能
"""

import json
import csv
from typing import List, Dict, Any


class DataProcessor:
    """数据处理器类"""
    
    def __init__(self):
        """初始化数据处理器"""
        self.data = []
    
    def load_json_data(self, file_path: str) -> bool:
        """
        从JSON文件加载数据
        
        Args:
            file_path (str): JSON文件路径
            
        Returns:
            bool: 加载成功返回True，否则返回False
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                self.data = json.load(file)
            return True
        except Exception as e:
            print(f"加载JSON数据时出错: {e}")
            return False
    
    def load_csv_data(self, file_path: str) -> bool:
        """
        从CSV文件加载数据
        
        Args:
            file_path (str): CSV文件路径
            
        Returns:
            bool: 加载成功返回True，否则返回False
        """
        try:
            self.data = []
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.data.append(row)
            return True
        except Exception as e:
            print(f"加载CSV数据时出错: {e}")
            return False
    
    def clean_data(self) -> None:
        """
        清洗数据，移除空值和重复项
        """
        # 移除空值项
        self.data = [item for item in self.data if all(value != '' for value in item.values())]
        
        # 移除重复项
        seen = set()
        unique_data = []
        for item in self.data:
            item_tuple = tuple(sorted(item.items()))
            if item_tuple not in seen:
                seen.add(item_tuple)
                unique_data.append(item)
        self.data = unique_data
    
    def transform_data(self, transform_rules: Dict[str, str]) -> None:
        """
        根据转换规则转换数据
        
        Args:
            transform_rules (Dict[str, str]): 转换规则字典，键为原字段名，值为新字段名
        """
        transformed_data = []
        for item in self.data:
            new_item = {}
            for old_key, new_key in transform_rules.items():
                if old_key in item:
                    new_item[new_key] = item[old_key]
                else:
                    new_item[new_key] = ''
            transformed_data.append(new_item)
        self.data = transformed_data
    
    def get_processed_data(self) -> List[Dict[str, Any]]:
        """
        获取处理后的数据
        
        Returns:
            List[Dict[str, Any]]: 处理后的数据
        """
        return self.data


def main():
    """主函数，用于演示DataProcessor的使用"""
    processor = DataProcessor()
    
    # 示例：创建一个示例JSON文件用于测试
    sample_data = [
        {"name": "张三", "age": "25", "city": "北京"},
        {"name": "李四", "age": "30", "city": "上海"},
        {"name": "王五", "age": "28", "city": "广州"}
    ]
    
    with open('sample_data.json', 'w', encoding='utf-8') as f:
        json.dump(sample_data, f, ensure_ascii=False, indent=2)
    
    # 加载并处理数据
    if processor.load_json_data('sample_data.json'):
        print("原始数据:")
        for item in processor.get_processed_data():
            print(item)
        
        processor.clean_data()
        print("\n清洗后的数据:")
        for item in processor.get_processed_data():
            print(item)
        
        # 转换数据字段
        transform_rules = {"name": "姓名", "age": "年龄", "city": "城市"}
        processor.transform_data(transform_rules)
        print("\n转换字段后的数据:")
        for item in processor.get_processed_data():
            print(item)


if __name__ == "__main__":
    main()
=======
"""
文件名: data_processor.py
作者: 开发者
创建日期: 2025-10-27
版本: 1.0
描述: 数据处理模块
      提供常用的数据处理功能，包括数据清洗、转换和分析
功能:
  - 数据清洗（去除重复、处理缺失值）
  - 数据转换（类型转换、标准化）
  - 简单数据分析（计数、求和、平均值）
依赖: 
  - collections 模块
  - typing 模块
使用示例:
  processor = DataProcessor()
  cleaned_data = processor.remove_duplicates(data_list)
  normalized_data = processor.normalize_numbers(numbers)
修改记录:
  2025-10-27 - 初始版本创建
"""

from typing import List, Dict, Any, Optional, Union
from collections import Counter
import re


class DataProcessor:
    """数据处理器类"""
    
    def __init__(self):
        """初始化数据处理器"""
        pass
    
    def remove_duplicates(self, data: List[Any]) -> List[Any]:
        """
        去除列表中的重复元素，保持原有顺序
        
        Args:
            data (List[Any]): 输入的数据列表
            
        Returns:
            List[Any]: 去重后的数据列表
        """
        seen = set()
        result = []
        for item in data:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result
    
    def remove_none_values(self, data: List[Any]) -> List[Any]:
        """
        移除列表中的None值
        
        Args:
            data (List[Any]): 输入的数据列表
            
        Returns:
            List[Any]: 移除None值后的数据列表
        """
        return [item for item in data if item is not None]
    
    def normalize_text(self, text: str) -> str:
        """
        标准化文本：去除多余空格，转换为小写
        
        Args:
            text (str): 输入文本
            
        Returns:
            str: 标准化后的文本
        """
        if not isinstance(text, str):
            return ""
        # 去除首尾空格，将多个空格合并为一个
        normalized = re.sub(r'\s+', ' ', text.strip())
        return normalized.lower()
    
    def normalize_numbers(self, numbers: List[Union[int, float]]) -> List[float]:
        """
        标准化数字列表：转换为浮点数并去除无效值
        
        Args:
            numbers (List[Union[int, float]]): 输入的数字列表
            
        Returns:
            List[float]: 标准化后的数字列表
        """
        result = []
        for num in numbers:
            try:
                result.append(float(num))
            except (ValueError, TypeError):
                # 跳过无法转换为数字的值
                continue
        return result
    
    def count_elements(self, data: List[Any]) -> Dict[Any, int]:
        """
        统计列表中各元素出现的次数
        
        Args:
            data (List[Any]): 输入的数据列表
            
        Returns:
            Dict[Any, int]: 元素计数字典
        """
        return dict(Counter(data))
    
    def calculate_sum(self, numbers: List[Union[int, float]]) -> float:
        """
        计算数字列表的总和
        
        Args:
            numbers (List[Union[int, float]]): 输入的数字列表
            
        Returns:
            float: 数字总和
        """
        try:
            return float(sum(numbers))
        except TypeError:
            # 如果列表中有非数字元素，先过滤再计算
            valid_numbers = self.normalize_numbers(numbers)
            return float(sum(valid_numbers))
    
    def calculate_average(self, numbers: List[Union[int, float]]) -> Optional[float]:
        """
        计算数字列表的平均值
        
        Args:
            numbers (List[Union[int, float]]): 输入的数字列表
            
        Returns:
            Optional[float]: 平均值，空列表返回None
        """
        if not numbers:
            return None
        
        try:
            return self.calculate_sum(numbers) / len(numbers)
        except (TypeError, ZeroDivisionError):
            # 如果列表中有非数字元素，先过滤再计算
            valid_numbers = self.normalize_numbers(numbers)
            if not valid_numbers:
                return None
            return self.calculate_sum(valid_numbers) / len(valid_numbers)
    
    def filter_by_condition(self, data: List[Any], condition_func) -> List[Any]:
        """
        根据条件函数过滤数据
        
        Args:
            data (List[Any]): 输入的数据列表
            condition_func (function): 条件函数，返回布尔值
            
        Returns:
            List[Any]: 满足条件的数据列表
        """
        return [item for item in data if condition_func(item)]
    
    def convert_to_type(self, data: List[Any], target_type: type) -> List[Any]:
        """
        将数据列表中的元素转换为目标类型
        
        Args:
            data (List[Any]): 输入的数据列表
            target_type (type): 目标类型（如int, float, str等）
            
        Returns:
            List[Any]: 类型转换后的数据列表
        """
        result = []
        for item in data:
            try:
                result.append(target_type(item))
            except (ValueError, TypeError):
                # 跳过无法转换的元素
                continue
        return result


def demonstrate_data_processor():
    """演示数据处理器功能"""
    print("=== 数据处理器功能演示 ===\n")
    
    processor = DataProcessor()
    
    # 演示去重功能
    print("1. 去除重复元素:")
    data_with_duplicates = [1, 2, 2, 3, 3, 3, 4, 5, 5]
    print(f"原始数据: {data_with_duplicates}")
    unique_data = processor.remove_duplicates(data_with_duplicates)
    print(f"去重后数据: {unique_data}\n")
    
    # 演示文本标准化
    print("2. 文本标准化:")
    messy_text = "  Hello    World  "
    print(f"原始文本: '{messy_text}'")
    clean_text = processor.normalize_text(messy_text)
    print(f"标准化后: '{clean_text}'\n")
    
    # 演示数字标准化
    print("3. 数字标准化:")
    mixed_numbers = [1, "2", 3.5, "4.5", "abc", None, 6]
    print(f"原始数据: {mixed_numbers}")
    clean_numbers = processor.normalize_numbers(mixed_numbers)
    print(f"标准化后: {clean_numbers}\n")
    
    # 演示元素计数
    print("4. 元素计数:")
    sample_data = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    print(f"数据: {sample_data}")
    counts = processor.count_elements(sample_data)
    print(f"计数结果: {counts}\n")
    
    # 演示数值计算
    print("5. 数值计算:")
    numbers = [10.0, 20.0, 30.0, 40.0, 50.0]
    print(f"数据: {numbers}")
    total = processor.calculate_sum(numbers)
    average = processor.calculate_average(numbers)
    print(f"总和: {total}")
    print(f"平均值: {average}\n")
    
    # 演示条件过滤
    print("6. 条件过滤:")
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"原始数据: {numbers}")
    # 过滤出偶数
    even_numbers = processor.filter_by_condition(numbers, lambda x: x % 2 == 0)
    print(f"偶数: {even_numbers}")
    # 过滤出大于5的数
    greater_than_five = processor.filter_by_condition(numbers, lambda x: x > 5)
    print(f"大于5的数: {greater_than_five}\n")


if __name__ == "__main__":
    demonstrate_data_processor()
>>>>>>> Remote