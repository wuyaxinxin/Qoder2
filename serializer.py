# 始终生效

import json
from data_model import DataModel


def save_to_file(obj, filename):
    """
    将 DataModel 对象序列化并保存到文件
    
    参数:
        obj (DataModel): 要保存的数据模型对象
        filename (str): 目标文件路径
        
    异常:
        IOError: 当文件写入失败时抛出
        ValueError: 当对象无法序列化时抛出
    """
    try:
        # 将对象转换为字典
        data_dict = obj.to_dict()
        
        # 写入 JSON 文件
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data_dict, f, ensure_ascii=False, indent=2)
            
    except IOError as e:
        raise IOError(f"文件写入失败: {e}")
    except Exception as e:
        raise ValueError(f"对象序列化失败: {e}")


def load_from_file(filename):
    """
    从文件读取并反序列化为 DataModel 对象
    
    参数:
        filename (str): 源文件路径
        
    返回:
        DataModel: 从文件加载的数据模型对象
        
    异常:
        FileNotFoundError: 当文件不存在时抛出
        ValueError: 当 JSON 解析失败或数据格式无效时抛出
    """
    try:
        # 读取 JSON 文件
        with open(filename, 'r', encoding='utf-8') as f:
            data_dict = json.load(f)
        
        # 从字典创建对象
        return DataModel.from_dict(data_dict)
        
    except FileNotFoundError:
        raise FileNotFoundError(f"文件不存在: {filename}")
    except json.JSONDecodeError as e:
        raise ValueError(f"JSON 解析失败: {e}")
    except Exception as e:
        raise ValueError(f"数据加载失败: {e}")
