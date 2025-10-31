# 始终生效

class DataModel:
    def __init__(self, name, value, tags=None):
        self.name = name
        self.value = value
        self.tags = tags or []
    
    def to_dict(self):
        return {'name': self.name, 'value': self.value, 'tags': self.tags}
    
    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['value'], data.get('tags', []))
