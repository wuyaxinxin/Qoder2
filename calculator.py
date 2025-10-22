#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: calculator.py
作者: 开发者
创建日期: 2025-10-22
版本: 1.0
描述: 多功能计算器类，支持基本运算、科学计算和统计功能
功能:
  - 基本运算（加、减、乘、除）
  - 科学计算（幂、平方根、对数）
  - 统计计算（平均值、 方差、标准差）
  - 历史记录管理
依赖: math 模块
使用示例:
  calc = Calculator()
  result = calc.add(10,  5)
  calc.power(2, 3)
  print(calc.get_history())
修改记录:
  2025-10-22 - 初始版本创建
"""

import math
from typing import List, Optional, Union
from datetime import datetime


class Calculator:
    """多功能计算器类"""
    
    def __init__(self, precision: int = 2):
        """
        初始化计算器
        
        Args:
            precision (int): 结果精度，默认保留2位小数
        """
        self.precision = precision
        self.history: List[dict] = []
        self.last_result: Optional[float] = None
    
    def _record_operation(self, operation: str, operands: list, result: float):
        """
        记录操作历史
        
        Args:
            operation (str): 操作名称
            operands (list): 操作数列表
            result (float): 计算结果
        """
        record = {
            'timestamp': datetime.now(),
            'operation': operation,
            'operands': operands,
            'result': result
        }
        self.history.append(record)
        self.last_result = result
    
    def _round_result(self, value: float) -> float:
        """
        根据精度四舍五入结果
        
        Args:
            value (float): 原始值
            
        Returns:
            float: 四舍五入后的值
        """
        return round(value, self.precision)
    
    # 基本运算
    def add(self, a: float, b: float) -> float:
        """
        加法运算
        
        Args:
            a (float): 加数
            b (float): 加数
            
        Returns:
            float: 和
        """
        result = self._round_result(a + b)
        self._record_operation('加法', [a, b], result)
        return result
    
    def subtract(self, a: float, b: float) -> float:
        """
        减法运算
        
        Args:
            a (float): 被减数
            b (float): 减数
            
        Returns:
            float: 差
        """
        result = self._round_result(a - b)
        self._record_operation('减法', [a, b], result)
        return result
    
    def multiply(self, a: float, b: float) -> float:
        """
        乘法运算
        
        Args:
            a (float): 乘数
            b (float): 乘数
            
        Returns:
            float: 积
        """
        result = self._round_result(a * b)
        self._record_operation('乘法', [a, b], result)
        return result
    
    def divide(self, a: float, b: float) -> Optional[float]:
        """
        除法运算
        
        Args:
            a (float): 被除数
            b (float): 除数
            
        Returns:
            Optional[float]: 商，除数为0时返回None
        """
        if b == 0:
            print("错误：除数不能为0")
            return None
        
        result = self._round_result(a / b)
        self._record_operation('除法', [a, b], result)
        return result
    
    def modulo(self, a: float, b: float) -> Optional[float]:
        """
        取模运算
        
        Args:
            a (float): 被除数
            b (float): 除数
            
        Returns:
            Optional[float]: 余数，除数为0时返回None
        """
        if b == 0:
            print("错误：除数不能为0")
            return None
        
        result = self._round_result(a % b)
        self._record_operation('取模', [a, b], result)
        return result
    
    # 科学计算
    def power(self, base: float, exponent: float) -> float:
        """
        幂运算
        
        Args:
            base (float): 底数
            exponent (float): 指数
            
        Returns:
            float: 幂
        """
        result = self._round_result(math.pow(base, exponent))
        self._record_operation('幂运算', [base, exponent], result)
        return result
    
    def square_root(self, value: float) -> Optional[float]:
        """
        平方根运算
        
        Args:
            value (float): 被开方数
            
        Returns:
            Optional[float]: 平方根，负数时返回None
        """
        if value < 0:
            print("错误：不能对负数开平方根")
            return None
        
        result = self._round_result(math.sqrt(value))
        self._record_operation('平方根', [value], result)
        return result
    
    def logarithm(self, value: float, base: float = math.e) -> Optional[float]:
        """
        对数运算
        
        Args:
            value (float): 真数
            base (float): 底数，默认为自然对数e
            
        Returns:
            Optional[float]: 对数值，参数无效时返回None
        """
        if value <= 0 or base <= 0 or base == 1:
            print("错误：对数的真数和底数必须大于0，且底数不能为1")
            return None
        
        result = self._round_result(math.log(value, base))
        self._record_operation('对数', [value, base], result)
        return result
    
    def factorial(self, n: int) -> Optional[int]:
        """
        阶乘运算
        
        Args:
            n (int): 非负整数
            
        Returns:
            Optional[int]: 阶乘值，负数时返回None
        """
        if n < 0:
            print("错误：阶乘只能计算非负整数")
            return None
        
        result = math.factorial(n)
        self._record_operation('阶乘', [n], result)
        return result
    
    # 三角函数
    def sin(self, angle: float, degree: bool = True) -> float:
        """
        正弦函数
        
        Args:
            angle (float): 角度
            degree (bool): True表示角度制，False表示弧度制
            
        Returns:
            float: 正弦值
        """
        if degree:
            angle = math.radians(angle)
        
        result = self._round_result(math.sin(angle))
        self._record_operation('正弦', [angle], result)
        return result
    
    def cos(self, angle: float, degree: bool = True) -> float:
        """
        余弦函数
        
        Args:
            angle (float): 角度
            degree (bool): True表示角度制，False表示弧度制
            
        Returns:
            float: 余弦值
        """
        if degree:
            angle = math.radians(angle)
        
        result = self._round_result(math.cos(angle))
        self._record_operation('余弦', [angle], result)
        return result
    
    def tan(self, angle: float, degree: bool = True) -> float:
        """
        正切函数
        
        Args:
            angle (float): 角度
            degree (bool): True表示角度制，False表示弧度制
            
        Returns:
            float: 正切值
        """
        if degree:
            angle = math.radians(angle)
        
        result = self._round_result(math.tan(angle))
        self._record_operation('正切', [angle], result)
        return result
    
    # 统计计算
    def mean(self, numbers: List[float]) -> Optional[float]:
        """
        计算平均值
        
        Args:
            numbers (List[float]): 数字列表
            
        Returns:
            Optional[float]: 平均值，空列表时返回None
        """
        if not numbers:
            print("错误：列表不能为空")
            return None
        
        result = self._round_result(sum(numbers) / len(numbers))
        self._record_operation('平均值', numbers, result)
        return result
    
    def median(self, numbers: List[float]) -> Optional[float]:
        """
        计算中位数
        
        Args:
            numbers (List[float]): 数字列表
            
        Returns:
            Optional[float]: 中位数，空列表时返回None
        """
        if not numbers:
            print("错误：列表不能为空")
            return None
        
        sorted_numbers = sorted(numbers)
        n = len(sorted_numbers)
        
        if n % 2 == 0:
            result = self._round_result((sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2)
        else:
            result = sorted_numbers[n//2]
        
        self._record_operation('中位数', numbers, result)
        return result
    
    def variance(self, numbers: List[float]) -> Optional[float]:
        """
        计算方差
        
        Args:
            numbers (List[float]): 数字列表
            
        Returns:
            Optional[float]: 方差，空列表时返回None
        """
        if not numbers:
            print("错误：列表不能为空")
            return None
        
        avg = sum(numbers) / len(numbers)
        result = self._round_result(sum((x - avg) ** 2 for x in numbers) / len(numbers))
        self._record_operation('方差', numbers, result)
        return result
    
    def std_deviation(self, numbers: List[float]) -> Optional[float]:
        """
        计算标准差
        
        Args:
            numbers (List[float]): 数字列表
            
        Returns:
            Optional[float]: 标准差，空列表时返回None
        """
        var = self.variance(numbers)
        if var is None:
            return None
        
        result = self._round_result(math.sqrt(var))
        self._record_operation('标准差', numbers, result)
        return result
    
    # 历史记录管理
    def get_history(self, limit: int = 10) -> List[dict]:
        """
        获取计算历史记录
        
        Args:
            limit (int): 返回最近的记录数量，默认10条
            
        Returns:
            List[dict]: 历史记录列表
        """
        return self.history[-limit:]
    
    def clear_history(self):
        """清空历史记录"""
        self.history.clear()
        self.last_result = None
        print("历史记录已清空")
    
    def get_last_result(self) -> Optional[float]:
        """
        获取上一次计算结果
        
        Returns:
            Optional[float]: 上一次的计算结果
        """
        return self.last_result
    
    def print_history(self, limit: int = 10):
        """
        打印历史记录
        
        Args:
            limit (int): 打印最近的记录数量，默认10条
        """
        recent_history = self.get_history(limit)
        
        if not recent_history:
            print("暂无历史记录")
            return
        
        print(f"\n=== 最近 {len(recent_history)} 条计算记录 ===")
        for i, record in enumerate(recent_history, 1):
            timestamp = record['timestamp'].strftime('%Y-%m-%d %H:%M:%S')
            operation = record['operation']
            operands = record['operands']
            result = record['result']
            print(f"{i}. [{timestamp}] {operation}: {operands} = {result}")


def demonstrate_calculator():
    """演示计算器功能"""
    print("=== 多功能计算器演示 ===\n")
    
    calc = Calculator(precision=2)
    
    # 基本运算
    print("1. 基本运算:")
    print(f"10 + 5 = {calc.add(10, 5)}")
    print(f"10 - 5 = {calc.subtract(10, 5)}")
    print(f"10 × 5 = {calc.multiply(10, 5)}")
    print(f"10 ÷ 5 = {calc.divide(10, 5)}")
    print(f"10 % 3 = {calc.modulo(10, 3)}")
    
    # 科学计算
    print("\n2. 科学计算:")
    print(f"2^10 = {calc.power(2, 10)}")
    print(f"√16 = {calc.square_root(16)}")
    print(f"log₁₀(100) = {calc.logarithm(100, 10)}")
    print(f"5! = {calc.factorial(5)}")
    
    # 三角函数
    print("\n3. 三角函数:")
    print(f"sin(30°) = {calc.sin(30)}")
    print(f"cos(60°) = {calc.cos(60)}")
    print(f"tan(45°) = {calc.tan(45)}")
    
    # 统计计算
    print("\n4. 统计计算:")
    numbers = [10, 20, 30, 40, 50]
    print(f"数据: {numbers}")
    print(f"平均值 = {calc.mean(numbers)}")
    print(f"中位数 = {calc.median(numbers)}")
    print(f"方差 = {calc.variance(numbers)}")
    print(f"标准差 = {calc.std_deviation(numbers)}")
    
    # 显示历史记录
    print("\n5. 历史记录:")
    calc.print_history(5)
    
    print(f"\n上一次计算结果: {calc.get_last_result()}")


if __name__ == "__main__":
    demonstrate_calculator()
