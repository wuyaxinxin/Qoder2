#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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