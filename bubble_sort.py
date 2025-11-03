"""
始终生效
冒泡排序实现模块
提供冒泡排序算法的实现和相关功能
"""


def bubble_sort(arr):
    """
    冒泡排序算法实现
    
    参数:
        arr: 待排序的列表
    
    返回:
        排序后的列表
    
    时间复杂度: O(n²)
    空间复杂度: O(1)
    """
    if not arr:
        return arr
    
    n = len(arr)
    # 创建副本以避免修改原列表
    result = arr.copy()
    
    # 外层循环控制排序轮数
    for i in range(n - 1):
        # 标记本轮是否发生交换
        swapped = False
        
        # 内层循环进行相邻元素比较和交换
        for j in range(n - 1 - i):
            if result[j] > result[j + 1]:
                # 交换相邻元素
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        
        # 如果本轮没有发生交换,说明已经有序,可以提前结束
        if not swapped:
            break
    
    return result


def bubble_sort_descending(arr):
    """
    冒泡排序 - 降序实现
    
    参数:
        arr: 待排序的列表
    
    返回:
        降序排序后的列表
    """
    if not arr:
        return arr
    
    n = len(arr)
    result = arr.copy()
    
    for i in range(n - 1):
        swapped = False
        
        for j in range(n - 1 - i):
            if result[j] < result[j + 1]:  # 改为降序比较
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        
        if not swapped:
            break
    
    return result


def bubble_sort_with_steps(arr):
    """
    冒泡排序 - 显示每一步的排序过程
    
    参数:
        arr: 待排序的列表
    
    返回:
        元组 (排序后的列表, 排序步骤列表)
    """
    if not arr:
        return arr, []
    
    n = len(arr)
    result = arr.copy()
    steps = [result.copy()]
    
    for i in range(n - 1):
        swapped = False
        
        for j in range(n - 1 - i):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
                steps.append(result.copy())
        
        if not swapped:
            break
    
    return result, steps


def demo():
    """演示冒泡排序的使用"""
    print("=" * 50)
    print("冒泡排序演示")
    print("=" * 50)
    
    # 示例1: 基本升序排序
    arr1 = [64, 34, 25, 12, 22, 11, 90]
    print(f"\n原始数组: {arr1}")
    sorted_arr1 = bubble_sort(arr1)
    print(f"升序排序后: {sorted_arr1}")
    
    # 示例2: 降序排序
    arr2 = [5, 2, 8, 1, 9, 3]
    print(f"\n原始数组: {arr2}")
    sorted_arr2 = bubble_sort_descending(arr2)
    print(f"降序排序后: {sorted_arr2}")
    
    # 示例3: 显示排序步骤
    arr3 = [5, 3, 8, 4, 2]
    print(f"\n原始数组: {arr3}")
    sorted_arr3, steps = bubble_sort_with_steps(arr3)
    print(f"排序步骤:")
    for idx, step in enumerate(steps):
        print(f"  步骤 {idx}: {step}")
    print(f"最终结果: {sorted_arr3}")
    
    # 示例4: 已排序数组
    arr4 = [1, 2, 3, 4, 5]
    print(f"\n已排序数组: {arr4}")
    sorted_arr4 = bubble_sort(arr4)
    print(f"排序后: {sorted_arr4}")
    
    # 示例5: 空数组和单元素数组
    print(f"\n空数组: {bubble_sort([])}")
    print(f"单元素数组: {bubble_sort([42])}")


if __name__ == "__main__":
    demo()
