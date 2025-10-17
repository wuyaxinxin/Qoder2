
"""
示例 Python 实用工具模块
从 GitHub 下载的示例代码
"""

def hello_world():
    """打印 Hello World"""
    print("Hello from downloaded package!")

def calculate_average(numbers):
    """计算平均值"""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

if __name__ == "__main__":
    hello_world()
    print(f"Average of [1,2,3,4,5]: {calculate_average([1,2,3,4,5])}")
