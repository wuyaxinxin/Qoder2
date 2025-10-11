#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: data_analyzer.py
作者: 开发者
创建日期: 2025-10-11
版本: 1.0
描述: 这是一个数据分析工具的Python类文件
      提供基本的数据统计、分析和可视化功能
功能:
  - 数据基本统计（平均值、中位数、标准差等）
  - 数据分析（相关性、分布、异常值检测）
  - 数据处理（清洗、过滤、转换）
  - 简单的文本报告生成
依赖: 仅使用Python标准库（math, statistics, collections等）
使用示例:
  analyzer = DataAnalyzer([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
  print(analyzer.get_basic_stats())
  analyzer.generate_report()
修改记录:
  2025-10-11 - 初始版本创建
"""

import math
import statistics
from collections import Counter, defaultdict
from typing import List, Dict, Tuple, Optional, Union, Any
from datetime import datetime


class DataAnalyzer:
    """数据分析器类 - 提供基本的数据分析功能"""
    
    def __init__(self, data: List[Union[int, float]] = None):
        """
        初始化数据分析器
        
        Args:
            data (List[Union[int, float]]): 要分析的数值数据列表
        """
        self.data = data if data is not None else []
        self.original_data = self.data.copy()  # 保存原始数据
        self.analysis_time = datetime.now()
        self.metadata = {
            'data_source': '用户输入',
            'data_type': '数值型',
            'last_updated': self.analysis_time
        }
    
    def set_data(self, data: List[Union[int, float]]) -> None:
        """
        设置新的数据集
        
        Args:
            data (List[Union[int, float]]): 新的数据列表
        """
        self.data = data.copy()
        self.original_data = data.copy()
        self.metadata['last_updated'] = datetime.now()
        print(f"数据已更新，共 {len(data)} 个数据点")
    
    def add_data(self, values: Union[List[Union[int, float]], int, float]) -> None:
        """
        添加数据到现有数据集
        
        Args:
            values: 要添加的数据（可以是单个值或列表）
        """
        if isinstance(values, (int, float)):
            self.data.append(values)
        elif isinstance(values, list):
            self.data.extend(values)
        else:
            raise ValueError("数据必须是数字或数字列表")
        
        self.metadata['last_updated'] = datetime.now()
        print(f"已添加数据，当前共 {len(self.data)} 个数据点")
    
    def get_basic_stats(self) -> Dict[str, float]:
        """
        获取基本统计信息
        
        Returns:
            Dict[str, float]: 包含基本统计信息的字典
        """
        if not self.data:
            return {}
        
        try:
            stats = {
                '数据量': len(self.data),
                '最小值': min(self.data),
                '最大值': max(self.data),
                '平均值': statistics.mean(self.data),
                '中位数': statistics.median(self.data),
                '众数': statistics.mode(self.data) if len(set(self.data)) < len(self.data) else None,
                '标准差': statistics.stdev(self.data) if len(self.data) > 1 else 0,
                '方差': statistics.variance(self.data) if len(self.data) > 1 else 0,
                '极差': max(self.data) - min(self.data),
                '总和': sum(self.data)
            }
            
            # 计算四分位数
            sorted_data = sorted(self.data)
            n = len(sorted_data)
            
            stats['第一四分位数'] = sorted_data[n // 4] if n >= 4 else sorted_data[0]
            stats['第三四分位数'] = sorted_data[3 * n // 4] if n >= 4 else sorted_data[-1]
            stats['四分位距'] = stats['第三四分位数'] - stats['第一四分位数']
            
            return stats
            
        except Exception as e:
            print(f"计算统计信息时出错: {e}")
            return {}
    
    def detect_outliers(self, method: str = 'iqr') -> List[float]:
        """
        检测异常值
        
        Args:
            method (str): 检测方法 ('iqr' 或 'zscore')
            
        Returns:
            List[float]: 异常值列表
        """
        if not self.data or len(self.data) < 4:
            return []
        
        outliers = []
        
        if method == 'iqr':
            # 使用四分位距方法
            sorted_data = sorted(self.data)
            n = len(sorted_data)
            q1 = sorted_data[n // 4]
            q3 = sorted_data[3 * n // 4]
            iqr = q3 - q1
            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr
            
            outliers = [x for x in self.data if x < lower_bound or x > upper_bound]
            
        elif method == 'zscore':
            # 使用Z-score方法
            mean = statistics.mean(self.data)
            std_dev = statistics.stdev(self.data)
            
            if std_dev > 0:
                outliers = [x for x in self.data if abs((x - mean) / std_dev) > 2]
        
        return outliers
    
    def get_frequency_distribution(self, bins: int = 10) -> Dict[str, int]:
        """
        获取频率分布
        
        Args:
            bins (int): 分组数量
            
        Returns:
            Dict[str, int]: 频率分布字典
        """
        if not self.data:
            return {}
        
        min_val, max_val = min(self.data), max(self.data)
        if min_val == max_val:
            return {f"{min_val}": len(self.data)}
        
        bin_width = (max_val - min_val) / bins
        distribution = defaultdict(int)
        
        for value in self.data:
            bin_index = min(int((value - min_val) / bin_width), bins - 1)
            bin_start = min_val + bin_index * bin_width
            bin_end = bin_start + bin_width
            bin_label = f"{bin_start:.2f}-{bin_end:.2f}"
            distribution[bin_label] += 1
        
        return dict(distribution)
    
    def filter_data(self, min_val: float = None, max_val: float = None) -> List[float]:
        """
        过滤数据
        
        Args:
            min_val (float): 最小值阈值
            max_val (float): 最大值阈值
            
        Returns:
            List[float]: 过滤后的数据
        """
        filtered_data = self.data.copy()
        
        if min_val is not None:
            filtered_data = [x for x in filtered_data if x >= min_val]
        
        if max_val is not None:
            filtered_data = [x for x in filtered_data if x <= max_val]
        
        print(f"过滤前: {len(self.data)} 个数据点")
        print(f"过滤后: {len(filtered_data)} 个数据点")
        
        return filtered_data
    
    def normalize_data(self, method: str = 'minmax') -> List[float]:
        """
        数据标准化
        
        Args:
            method (str): 标准化方法 ('minmax' 或 'zscore')
            
        Returns:
            List[float]: 标准化后的数据
        """
        if not self.data:
            return []
        
        if method == 'minmax':
            # Min-Max标准化
            min_val, max_val = min(self.data), max(self.data)
            if min_val == max_val:
                return [0.5] * len(self.data)  # 所有值相同时返回0.5
            
            return [(x - min_val) / (max_val - min_val) for x in self.data]
            
        elif method == 'zscore':
            # Z-score标准化
            mean = statistics.mean(self.data)
            std_dev = statistics.stdev(self.data) if len(self.data) > 1 else 1
            
            return [(x - mean) / std_dev for x in self.data]
        
        return self.data.copy()
    
    def calculate_correlation(self, other_data: List[Union[int, float]]) -> float:
        """
        计算与另一组数据的相关系数
        
        Args:
            other_data (List[Union[int, float]]): 另一组数据
            
        Returns:
            float: 皮尔逊相关系数
        """
        if len(self.data) != len(other_data) or len(self.data) < 2:
            print("错误：数据长度不匹配或数据量不足")
            return 0.0
        
        try:
            return statistics.correlation(self.data, other_data)
        except Exception as e:
            print(f"计算相关系数时出错: {e}")
            return 0.0
    
    def get_percentile(self, percentile: float) -> float:
        """
        计算指定百分位数
        
        Args:
            percentile (float): 百分位数 (0-100)
            
        Returns:
            float: 百分位数值
        """
        if not self.data or not (0 <= percentile <= 100):
            return 0.0
        
        sorted_data = sorted(self.data)
        index = (percentile / 100) * (len(sorted_data) - 1)
        
        if index == int(index):
            return sorted_data[int(index)]
        else:
            lower = sorted_data[int(index)]
            upper = sorted_data[int(index) + 1]
            return lower + (index - int(index)) * (upper - lower)
    
    def generate_report(self) -> str:
        """
        生成数据分析报告
        
        Returns:
            str: 格式化的分析报告
        """
        report = f"""
=== 数据分析报告 ===
生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
数据来源: {self.metadata['data_source']}
数据类型: {self.metadata['data_type']}

=== 基本统计信息 ===
"""
        
        stats = self.get_basic_stats()
        if stats:
            for key, value in stats.items():
                if value is not None:
                    if isinstance(value, float):
                        report += f"{key}: {value:.4f}\n"
                    else:
                        report += f"{key}: {value}\n"
        else:
            report += "暂无数据\n"
        
        if self.data:
            report += f"\n=== 数据质量分析 ===\n"
            outliers = self.detect_outliers()
            report += f"异常值数量: {len(outliers)}\n"
            if outliers:
                report += f"异常值: {outliers[:5]}{'...' if len(outliers) > 5 else ''}\n"
            
            report += f"\n=== 分布分析 ===\n"
            freq_dist = self.get_frequency_distribution(bins=5)
            for range_str, count in freq_dist.items():
                percentage = (count / len(self.data)) * 100
                report += f"{range_str}: {count} 个 ({percentage:.1f}%)\n"
            
            report += f"\n=== 百分位数 ===\n"
            for p in [25, 50, 75, 90, 95]:
                report += f"第{p}百分位数: {self.get_percentile(p):.4f}\n"
        
        return report
    
    def summary(self) -> str:
        """获取数据摘要"""
        if not self.data:
            return "数据集为空"
        
        stats = self.get_basic_stats()
        return f"数据集包含 {len(self.data)} 个数据点，平均值: {stats.get('平均值', 0):.2f}, 标准差: {stats.get('标准差', 0):.2f}"
    
    def __str__(self) -> str:
        """字符串表示"""
        return f"DataAnalyzer(data_points={len(self.data)}, range={min(self.data) if self.data else 'N/A'}-{max(self.data) if self.data else 'N/A'})"
    
    def __repr__(self) -> str:
        """对象表示"""
        return self.__str__()


def demonstrate_data_analysis():
    """演示数据分析功能"""
    print("=== 数据分析工具演示 ===\n")
    
    # 创建示例数据
    sample_data = [23, 45, 56, 78, 32, 67, 89, 12, 34, 67, 54, 43, 76, 87, 23, 45, 67, 89, 34, 56]
    
    # 创建分析器
    analyzer = DataAnalyzer(sample_data)
    
    print("1. 基本统计信息:")
    stats = analyzer.get_basic_stats()
    for key, value in stats.items():
        if value is not None:
            print(f"  {key}: {value:.2f}" if isinstance(value, float) else f"  {key}: {value}")
    
    print(f"\n2. 数据摘要:")
    print(f"  {analyzer.summary()}")
    
    print(f"\n3. 异常值检测:")
    outliers = analyzer.detect_outliers()
    print(f"  检测到 {len(outliers)} 个异常值: {outliers}")
    
    print(f"\n4. 频率分布:")
    freq_dist = analyzer.get_frequency_distribution(bins=5)
    for range_str, count in freq_dist.items():
        print(f"  {range_str}: {count} 个")
    
    print(f"\n5. 数据标准化 (前5个值):")
    normalized = analyzer.normalize_data('minmax')
    print(f"  原始数据: {sample_data[:5]}")
    print(f"  标准化后: {[f'{x:.3f}' for x in normalized[:5]]}")
    
    print(f"\n6. 完整分析报告:")
    print(analyzer.generate_report())


if __name__ == "__main__":
    demonstrate_data_analysis()