# 始终生效
# 生成260位数字

import random

def generate_260_digit_number():
    """生成一个260位的数字"""
    # 第一位不能为0（确保是260位）
    first_digit = random.randint(1, 9)
    # 后续259位可以是0-9
    remaining_digits = ''.join([str(random.randint(0, 9)) for _ in range(259)])
    
    number = str(first_digit) + remaining_digits
    return number

if __name__ == "__main__":
    num = generate_260_digit_number()
    print(f"260位数字：")
    print(num)
    print(f"\n数字长度验证：{len(num)} 位")
    
    # 格式化输出（每50位一行，方便查看）
    print("\n格式化显示：")
    for i in range(0, len(num), 50):
        print(num[i:i+50])
