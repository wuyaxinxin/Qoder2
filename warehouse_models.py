"""
仓库管理系统核心模型类
包含商品、库存记录、仓库等基础数据模型
"""

from datetime import datetime
from typing import Dict, List, Optional
import uuid


class Product:
    """商品类"""
    
    def __init__(self, product_id: str, name: str, description: str, 
                 category: str, unit_price: float, unit: str = "个"):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.category = category
        self.unit_price = unit_price
        self.unit = unit
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def update_info(self, name: str = None, description: str = None, 
                   category: str = None, unit_price: float = None, unit: str = None):
        """更新商品信息"""
        if name:
            self.name = name
        if description:
            self.description = description
        if category:
            self.category = category
        if unit_price is not None:
            self.unit_price = unit_price
        if unit:
            self.unit = unit
        self.updated_at = datetime.now()
    
    def to_dict(self) -> Dict:
        """转换为字典格式"""
        return {
            'product_id': self.product_id,
            'name': self.name,
            'description': self.description,
            'category': self.category,
            'unit_price': self.unit_price,
            'unit': self.unit,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: Dict):
        """从字典创建商品对象"""
        product = cls(
            product_id=data['product_id'],
            name=data['name'],
            description=data['description'],
            category=data['category'],
            unit_price=data['unit_price'],
            unit=data['unit']
        )
        if 'created_at' in data:
            product.created_at = datetime.fromisoformat(data['created_at'])
        if 'updated_at' in data:
            product.updated_at = datetime.fromisoformat(data['updated_at'])
        return product
    
    def __str__(self):
        return f"商品[{self.product_id}]: {self.name} - {self.unit_price}元/{self.unit}"


class StockRecord:
    """库存记录类"""
    
    def __init__(self, product_id: str, quantity: int, location: str, 
                 batch_number: str = None, expiry_date: datetime = None):
        self.record_id = str(uuid.uuid4())
        self.product_id = product_id
        self.quantity = quantity
        self.location = location
        self.batch_number = batch_number or str(uuid.uuid4())[:8]
        self.expiry_date = expiry_date
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def update_quantity(self, new_quantity: int):
        """更新库存数量"""
        self.quantity = new_quantity
        self.updated_at = datetime.now()
    
    def is_expired(self) -> bool:
        """检查是否过期"""
        if self.expiry_date:
            return datetime.now() > self.expiry_date
        return False
    
    def to_dict(self) -> Dict:
        """转换为字典格式"""
        return {
            'record_id': self.record_id,
            'product_id': self.product_id,
            'quantity': self.quantity,
            'location': self.location,
            'batch_number': self.batch_number,
            'expiry_date': self.expiry_date.isoformat() if self.expiry_date else None,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: Dict):
        """从字典创建库存记录对象"""
        record = cls(
            product_id=data['product_id'],
            quantity=data['quantity'],
            location=data['location'],
            batch_number=data['batch_number']
        )
        record.record_id = data['record_id']
        if data.get('expiry_date'):
            record.expiry_date = datetime.fromisoformat(data['expiry_date'])
        if 'created_at' in data:
            record.created_at = datetime.fromisoformat(data['created_at'])
        if 'updated_at' in data:
            record.updated_at = datetime.fromisoformat(data['updated_at'])
        return record
    
    def __str__(self):
        expiry_info = f" (到期: {self.expiry_date.strftime('%Y-%m-%d')})" if self.expiry_date else ""
        return f"库存记录[{self.record_id[:8]}]: 商品{self.product_id} - {self.quantity}个 @ {self.location}{expiry_info}"


class TransactionRecord:
    """交易记录类"""
    
    TRANSACTION_TYPES = ['入库', '出库', '调拨', '盘点']
    
    def __init__(self, transaction_type: str, product_id: str, quantity: int, 
                 location: str, operator: str, notes: str = ""):
        if transaction_type not in self.TRANSACTION_TYPES:
            raise ValueError(f"交易类型必须是: {', '.join(self.TRANSACTION_TYPES)}")
        
        self.transaction_id = str(uuid.uuid4())
        self.transaction_type = transaction_type
        self.product_id = product_id
        self.quantity = quantity
        self.location = location
        self.operator = operator
        self.notes = notes
        self.timestamp = datetime.now()
    
    def to_dict(self) -> Dict:
        """转换为字典格式"""
        return {
            'transaction_id': self.transaction_id,
            'transaction_type': self.transaction_type,
            'product_id': self.product_id,
            'quantity': self.quantity,
            'location': self.location,
            'operator': self.operator,
            'notes': self.notes,
            'timestamp': self.timestamp.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: Dict):
        """从字典创建交易记录对象"""
        record = cls(
            transaction_type=data['transaction_type'],
            product_id=data['product_id'],
            quantity=data['quantity'],
            location=data['location'],
            operator=data['operator'],
            notes=data['notes']
        )
        record.transaction_id = data['transaction_id']
        record.timestamp = datetime.fromisoformat(data['timestamp'])
        return record
    
    def __str__(self):
        return f"{self.transaction_type}记录[{self.transaction_id[:8]}]: {self.product_id} {self.quantity}个 @ {self.location} by {self.operator}"


class Warehouse:
    """仓库类"""
    
    def __init__(self, warehouse_id: str, name: str, address: str, 
                 manager: str, capacity: int = None):
        self.warehouse_id = warehouse_id
        self.name = name
        self.address = address
        self.manager = manager
        self.capacity = capacity
        self.locations: List[str] = []  # 仓库位置列表
        self.created_at = datetime.now()
    
    def add_location(self, location: str):
        """添加仓储位置"""
        if location not in self.locations:
            self.locations.append(location)
    
    def remove_location(self, location: str):
        """移除仓储位置"""
        if location in self.locations:
            self.locations.remove(location)
    
    def to_dict(self) -> Dict:
        """转换为字典格式"""
        return {
            'warehouse_id': self.warehouse_id,
            'name': self.name,
            'address': self.address,
            'manager': self.manager,
            'capacity': self.capacity,
            'locations': self.locations,
            'created_at': self.created_at.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: Dict):
        """从字典创建仓库对象"""
        warehouse = cls(
            warehouse_id=data['warehouse_id'],
            name=data['name'],
            address=data['address'],
            manager=data['manager'],
            capacity=data.get('capacity')
        )
        warehouse.locations = data.get('locations', [])
        if 'created_at' in data:
            warehouse.created_at = datetime.fromisoformat(data['created_at'])
        return warehouse
    
    def __str__(self):
        return f"仓库[{self.warehouse_id}]: {self.name} - 管理员: {self.manager}"


class StockAlert:
    """库存预警类"""
    
    ALERT_TYPES = ['低库存', '过期', '零库存']
    
    def __init__(self, alert_type: str, product_id: str, current_quantity: int, 
                 threshold: int = None, message: str = ""):
        if alert_type not in self.ALERT_TYPES:
            raise ValueError(f"预警类型必须是: {', '.join(self.ALERT_TYPES)}")
        
        self.alert_id = str(uuid.uuid4())
        self.alert_type = alert_type
        self.product_id = product_id
        self.current_quantity = current_quantity
        self.threshold = threshold
        self.message = message
        self.created_at = datetime.now()
        self.is_resolved = False
    
    def resolve(self):
        """标记预警为已解决"""
        self.is_resolved = True
    
    def to_dict(self) -> Dict:
        """转换为字典格式"""
        return {
            'alert_id': self.alert_id,
            'alert_type': self.alert_type,
            'product_id': self.product_id,
            'current_quantity': self.current_quantity,
            'threshold': self.threshold,
            'message': self.message,
            'created_at': self.created_at.isoformat(),
            'is_resolved': self.is_resolved
        }
    
    @classmethod
    def from_dict(cls, data: Dict):
        """从字典创建预警对象"""
        alert = cls(
            alert_type=data['alert_type'],
            product_id=data['product_id'],
            current_quantity=data['current_quantity'],
            threshold=data.get('threshold'),
            message=data['message']
        )
        alert.alert_id = data['alert_id']
        alert.created_at = datetime.fromisoformat(data['created_at'])
        alert.is_resolved = data['is_resolved']
        return alert
    
    def __str__(self):
        status = "已解决" if self.is_resolved else "未解决"
        return f"{self.alert_type}预警[{self.alert_id[:8]}]: 商品{self.product_id} - {self.message} ({status})"