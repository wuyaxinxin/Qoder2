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
    """
    多功能计算器类
    
    提供基本运算、科学计算、三角函数和统计计算功能。
    所有操作都会被记录到历史记录中，支持查看和清空历史。
    
    Attributes:
        precision (int): 计算结果的小数精度
        history (List[dict]): 操作历史记录列表
        last_result (Optional[float]): 上一次计算的结果
    """
    
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
        记录操作历史（内部方法）
        
        将每次计算操作的详细信息记录到历史列表中，包括时间戳、
        操作类型、操作数和计算结果。同时更新last_result属性。
        
        Args:
            operation (str): 操作名称（如'加法'、'乘法'等）
            operands (list): 操作数列表
            result (float): 计算结果
        """
        # 创建操作记录字典
        record = {
            'timestamp': datetime.now(),  # 记录操作时间
            'operation': operation,        # 操作类型
            'operands': operands,          # 操作数
            'result': result               # 计算结果
        }
        # 添加到历史记录列表
        self.history.append(record)
        # 更新最后一次计算结果
        self.last_result = result
    
    def _round_result(self, value: float) -> float:
        """
        根据精度四舍五入结果（内部方法）
        
        使用初始化时设定的precision参数对计算结果进行四舍五入处理，
        确保所有返回值的小数位数一致。
        
        Args:
            value (float): 原始计算值
            
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
        
        执行除法计算，自动检查除数是否为0以避免错误。
        
        Args:
            a (float): 被除数
            b (float): 除数
            
        Returns:
            Optional[float]: 商，除数为0时返回None
        """
        # 检查除数是否为0
        if b == 0:
            print("错误：除数不能为0")
            return None
        
        # 执行除法运算并四舍五入
        result = self._round_result(a / b)
        # 记录操作到历史
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
        
        计算给定数值的平方根，仅支持非负数。
        
        Args:
            value (float): 被开方数
            
        Returns:
            Optional[float]: 平方根，负数时返回None
        """
        # 检查是否为负数
        if value < 0:
            print("错误：不能对负数开平方根")
            return None
        
        # 计算平方根并四舍五入
        result = self._round_result(math.sqrt(value))
        # 记录操作
        self._record_operation('平方根', [value], result)
        return result
    
    def logarithm(self, value: float, base: float = math.e) -> Optional[float]:
        """
        对数运算
        
        计算指定底数的对数值，默认计算自然对数（底数为e）。
        
        Args:
            value (float): 真数（必须大于0）
            base (float): 底数（必须大于0且不等于1），默认为自然对数e
            
        Returns:
            Optional[float]: 对数值，参数无效时返回None
        """
        # 验证参数有效性：真数和底数都必须大于0，底数不能为1
        if value <= 0 or base <= 0 or base == 1:
            print("错误：对数的真数和底数必须大于0，且底数不能为1")
            return None
        
        # 计算对数并四舍五入
        result = self._round_result(math.log(value, base))
        # 记录操作
        self._record_operation('对数', [value, base], result)
        return result
    
    def factorial(self, n: int) -> Optional[int]:
        """
        阶乘运算
        
        计算给定非负整数的阶乘（n! = n × (n-1) × ... × 2 × 1）。
        
        Args:
            n (int): 非负整数
            
        Returns:
            Optional[int]: 阶乘值，负数时返回None
        """
        # 检查是否为非负整数
        if n < 0:
            print("错误：阶乘只能计算非负整数")
            return None
        
        # 使用math.factorial计算阶乘
        result = math.factorial(n)
        # 记录操作
        self._record_operation('阶乘', [n], result)
        return result
    
    # 三角函数
    def sin(self, angle: float, degree: bool = True) -> float:
        """
        正弦函数
        
        计算给定角度的正弦值，支持角度制和弧度制输入。
        
        Args:
            angle (float): 角度值
            degree (bool): True表示角度制（默认），False表示弧度制
            
        Returns:
            float: 正弦值（范围在-1到1之间）
        """
        # 如果输入是角度制，转换为弧度制
        if degree:
            angle = math.radians(angle)
        
        # 计算正弦值并四舍五入
        result = self._round_result(math.sin(angle))
        # 记录操作
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
        计算平均值（算术平均数）
        
        对给定的数字列表计算平均值，即所有数字之和除以数字个数。
        
        Args:
            numbers (List[float]): 数字列表
            
        Returns:
            Optional[float]: 平均值，空列表时返回None
        """
        # 检查列表是否为空
        if not numbers:
            print("错误：列表不能为空")
            return None
        
        # 计算平均值：总和除以个数
        result = self._round_result(sum(numbers) / len(numbers))
        # 记录操作
        self._record_operation('平均值', numbers, result)
        return result
    
    def median(self, numbers: List[float]) -> Optional[float]:
        """
        计算中位数
        
        对给定的数字列表计算中位数。若列表长度为奇数，返回中间的数；
        若为偶数，返回中间两个数的平均值。
        
        Args:
            numbers (List[float]): 数字列表
            
        Returns:
            Optional[float]: 中位数，空列表时返回None
        """
        # 检查列表是否为空
        if not numbers:
            print("错误：列表不能为空")
            return None
        
        # 对数字列表排序
        sorted_numbers = sorted(numbers)
        n = len(sorted_numbers)
        
        # 判断列表长度的奇偶性
        if n % 2 == 0:
            # 偶数个元素：取中间两个数的平均值
            result = self._round_result((sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2)
        else:
            # 奇数个元素：取中间的数
            result = sorted_numbers[n//2]
        
        # 记录操作
        self._record_operation('中位数', numbers, result)
        return result
    
    def variance(self, numbers: List[float]) -> Optional[float]:
        """
        计算方差（总体方差）
        
        方差用于衡量数据的离散程度，计算每个数据与平均值之差的平方的平均值。
        
        Args:
            numbers (List[float]): 数字列表
            
        Returns:
            Optional[float]: 方差，空列表时返回None
        """
        # 检查列表是否为空
        if not numbers:
            print("错误：列表不能为空")
            return None
        
        # 先计算平均值
        avg = sum(numbers) / len(numbers)
        # 计算方差：每个数与平均值之差的平方的平均值
        result = self._round_result(sum((x - avg) ** 2 for x in numbers) / len(numbers))
        # 记录操作
        self._record_operation('方差', numbers, result)
        return result
    
    def std_deviation(self, numbers: List[float]) -> Optional[float]:
        """
        计算标准差（总体标准差）
        
        标准差是方差的平方根，用于衡量数据的离散程度，单位与原数据一致。
        
        Args:
            numbers (List[float]): 数字列表
            
        Returns:
            Optional[float]: 标准差，空列表时返回None
        """
        # 先计算方差
        var = self.variance(numbers)
        if var is None:
            return None
        
        # 标准差是方差的平方根
        result = self._round_result(math.sqrt(var))
        # 记录操作（注意：这里会导致重复记录，因为variance已经记录过）
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
        打印历史记录到控制台
        
        以易读的格式打印最近的计算历史记录，包括时间戳、操作类型、
        操作数和结果。
        
        Args:
            limit (int): 打印最近的记录数量，默认10条
        """
        # 获取最近的历史记录
        recent_history = self.get_history(limit)
        
        # 如果没有历史记录，提示用户
        if not recent_history:
            print("暂无历史记录")
            return
        
        # 打印标题
        print(f"\n=== 最近 {len(recent_history)} 条计算记录 ===")
        # 遍历并格式化打印每条记录
        for i, record in enumerate(recent_history, 1):
            timestamp = record['timestamp'].strftime('%Y-%m-%d %H:%M:%S')  # 格式化时间
            operation = record['operation']  # 操作类型
            operands = record['operands']    # 操作数
            result = record['result']        # 结果
            print(f"{i}. [{timestamp}] {operation}: {operands} = {result}")


def demonstrate_calculator():
    """
    演示计算器的各项功能
    
    这是一个演示函数，展示了Calculator类的所有主要功能，包括：
    - 基本运算（加减乘除、取模）
    - 科学计算（幂、平方根、对数、阶乘）
    - 三角函数（正弦、余弦、正切）
    - 统计计算（平均值、中位数、方差、标准差）
    - 历史记录管理
    """
    print("=== 多功能计算器演示 ===\n")
    
    # 创建一个精度为2位小数的计算器实例
    calc = Calculator(precision=2)
    
    # ========== 基本运算演示 ==========
    print("1. 基本运算:")
    print(f"10 + 5 = {calc.add(10, 5)}")
    print(f"10 - 5 = {calc.subtract(10, 5)}")
    print(f"10 × 5 = {calc.multiply(10, 5)}")
    print(f"10 ÷ 5 = {calc.divide(10, 5)}")
    print(f"10 % 3 = {calc.modulo(10, 3)}")
    
    # ========== 科学计算演示 ==========
    print("\n2. 科学计算:")
    print(f"2^10 = {calc.power(2, 10)}")
    print(f"√16 = {calc.square_root(16)}")
    print(f"log₁₀(100) = {calc.logarithm(100, 10)}")
    print(f"5! = {calc.factorial(5)}")
    
    # ========== 三角函数演示 ==========
    print("\n3. 三角函数:")
    print(f"sin(30°) = {calc.sin(30)}")
    print(f"cos(60°) = {calc.cos(60)}")
    print(f"tan(45°) = {calc.tan(45)}")
    
    # ========== 统计计算演示 ==========
    print("\n4. 统计计算:")
    # 准备测试数据集
    numbers = [10, 20, 30, 40, 50]
    print(f"数据: {numbers}")
    print(f"平均值 = {calc.mean(numbers)}")
    print(f"中位数 = {calc.median(numbers)}")
    print(f"方差 = {calc.variance(numbers)}")
    print(f"标准差 = {calc.std_deviation(numbers)}")
    
    # ========== 历史记录演示 ==========
    print("\n5. 历史记录:")
    # 打印最近5条计算记录
    calc.print_history(5)
    
    # 显示最后一次的计算结果
    print(f"\n上一次计算结果: {calc.get_last_result()}")


if __name__ == "__main__":
    demonstrate_calculator()
