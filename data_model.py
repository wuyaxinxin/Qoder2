# 始终生效

class DataModel:
    """数据模型类，用于表示可序列化的数据对象"""
    
    def __init__(self, name, value, tags=None):
        """
        初始化数据模型
        
        参数:
            name (str): 数据名称
            value (int/float): 数据值
            tags (list): 标签列表，默认为空列表
        """
        self.name = name
        self.value = value
        self.tags = tags if tags is not None else []
    
    def to_dict(self):
        """
        将对象转换为字典
        
        返回:
            dict: 包含对象所有属性的字典
        """
        return {
            'name': self.name,
            'value': self.value,
            'tags': self.tags
        }
    
    @classmethod
    def from_dict(cls, data):
        """
        从字典创建 DataModel 对象
        
        参数:
            data (dict): 包含对象属性的字典
            
        返回:
            DataModel: 新创建的数据模型对象
            
        异常:
            ValueError: 当字典格式无效时抛出
        """
        try:
            return cls(
                name=data['name'],
                value=data['value'],
                tags=data.get('tags', [])
            )
        except KeyError as e:
            raise ValueError(f"无效的数据格式，缺少必需字段: {e}")
    
    def __repr__(self):
        """返回对象的字符串表示"""
        return f"DataModel(name='{self.name}', value={self.value}, tags={self.tags})"
