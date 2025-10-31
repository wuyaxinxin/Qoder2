# 始终生效

"""
序列化功能测试脚本
测试 DataModel 和 serializer 的功能
"""

from data_model import DataModel
from serializer import save_to_file, load_from_file
import os


def test_data_model():
    """测试 DataModel 类的基本功能"""
    print("=== 测试 DataModel 类 ===")
    
    # 创建数据对象
    data = DataModel(name="示例数据", value=100, tags=["tag1", "tag2", "tag3"])
    print(f"创建对象: {data}")
    
    # 测试 to_dict 方法
    data_dict = data.to_dict()
    print(f"转换为字典: {data_dict}")
    assert data_dict['name'] == "示例数据"
    assert data_dict['value'] == 100
    assert data_dict['tags'] == ["tag1", "tag2", "tag3"]
    
    # 测试 from_dict 方法
    restored_data = DataModel.from_dict(data_dict)
    print(f"从字典恢复: {restored_data}")
    assert restored_data.name == data.name
    assert restored_data.value == data.value
    assert restored_data.tags == data.tags
    
    print("✓ DataModel 类测试通过\n")


def test_serialization():
    """测试序列化和反序列化功能"""
    print("=== 测试序列化功能 ===")
    
    # 创建测试数据
    original_data = DataModel(
        name="测试数据",
        value=42.5,
        tags=["python", "序列化", "测试"]
    )
    print(f"原始数据: {original_data}")
    
    # 保存到文件
    test_file = "test_data.json"
    save_to_file(original_data, test_file)
    print(f"✓ 数据已保存到 {test_file}")
    
    # 从文件加载
    loaded_data = load_from_file(test_file)
    print(f"加载数据: {loaded_data}")
    
    # 验证数据一致性
    assert loaded_data.name == original_data.name
    assert loaded_data.value == original_data.value
    assert loaded_data.tags == original_data.tags
    
    print("✓ 序列化功能测试通过\n")
    
    # 清理测试文件
    if os.path.exists(test_file):
        os.remove(test_file)
        print(f"✓ 清理测试文件 {test_file}\n")


def test_exception_handling():
    """测试异常处理"""
    print("=== 测试异常处理 ===")
    
    # 测试文件不存在
    try:
        load_from_file("nonexistent_file.json")
        assert False, "应该抛出 FileNotFoundError"
    except FileNotFoundError as e:
        print(f"✓ 正确捕获文件不存在异常: {e}")
    
    # 测试无效的数据格式
    try:
        invalid_dict = {"value": 100}  # 缺少 name 字段
        DataModel.from_dict(invalid_dict)
        assert False, "应该抛出 ValueError"
    except ValueError as e:
        print(f"✓ 正确捕获无效数据格式异常: {e}")
    
    print("✓ 异常处理测试通过\n")


def test_edge_cases():
    """测试边界情况"""
    print("=== 测试边界情况 ===")
    
    # 测试空标签列表
    data1 = DataModel(name="无标签", value=0)
    assert data1.tags == []
    print("✓ 空标签列表测试通过")
    
    # 测试负数值
    data2 = DataModel(name="负数", value=-100, tags=["negative"])
    assert data2.value == -100
    print("✓ 负数值测试通过")
    
    # 测试浮点数
    data3 = DataModel(name="浮点数", value=3.14159, tags=[])
    assert abs(data3.value - 3.14159) < 0.00001
    print("✓ 浮点数测试通过")
    
    # 测试特殊字符
    data4 = DataModel(name="特殊字符!@#$%", value=999, tags=["特殊", "字符"])
    test_file = "test_special.json"
    save_to_file(data4, test_file)
    loaded = load_from_file(test_file)
    assert loaded.name == data4.name
    os.remove(test_file)
    print("✓ 特殊字符测试通过")
    
    print("✓ 边界情况测试通过\n")


def main():
    """运行所有测试"""
    print("开始运行序列化功能测试...\n")
    
    try:
        test_data_model()
        test_serialization()
        test_exception_handling()
        test_edge_cases()
        
        print("=" * 50)
        print("所有测试通过！✓")
        print("=" * 50)
        
    except AssertionError as e:
        print(f"\n测试失败: {e}")
        return False
    except Exception as e:
        print(f"\n测试出错: {e}")
        return False
    
    return True


if __name__ == "__main__":
    main()
