"""
简单的计算器模块
提供基本的数学运算功能
"""


class Calculator:
    """计算器类，实现基本的数学运算"""
    
    def __init__(self):
        """初始化计算器"""
        self.history = []
    
    def add(self, a, b):
        """加法运算"""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """减法运算"""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """乘法运算"""
        result = a * b
        self.history.append(f"{a} × {b} = {result}")
        return result
    
    def divide(self, a, b):
        """除法运算"""
        if b == 0:
            raise ValueError("除数不能为零")
        result = a / b
        self.history.append(f"{a} ÷ {b} = {result}")
        return result
    
    def power(self, base, exponent):
        """幂运算"""
        result = base ** exponent
        self.history.append(f"{base} ^ {exponent} = {result}")
        return result
    
    def get_history(self):
        """获取计算历史"""
        return self.history
    
    def clear_history(self):
        """清空计算历史"""
        self.history = []


def main():
    """主函数，演示计算器的使用"""
    calc = Calculator()
    
    print("=== 计算器演示 ===")
    print(f"10 + 5 = {calc.add(10, 5)}")
    print(f"10 - 5 = {calc.subtract(10, 5)}")
    print(f"10 × 5 = {calc.multiply(10, 5)}")
    print(f"10 ÷ 5 = {calc.divide(10, 5)}")
    print(f"2 ^ 3 = {calc.power(2, 3)}")
    
    print("\n=== 计算历史 ===")
    for record in calc.get_history():
        print(record)


if __name__ == "__main__":
    main()
