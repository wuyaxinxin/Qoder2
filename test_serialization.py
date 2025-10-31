# 始终生效

from data_model import DataModel
from serializer import save_to_file, load_from_file
import os

# 测试基本功能
data = DataModel("测试", 100, ["tag1", "tag2"])
print(f"创建: {data.name}, {data.value}, {data.tags}")

# 测试序列化
save_to_file(data, "test.json")
loaded = load_from_file("test.json")
print(f"加载: {loaded.name}, {loaded.value}, {loaded.tags}")

# 清理
os.remove("test.json")
print("测试通过！")
