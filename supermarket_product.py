"""
始终生效
超市管理系统 - 商品类定义
定义商品的属性和基本操作
"""


class Product:
    """商品类"""
    
    def __init__(self, product_id, name, category, price, stock, supplier="", description=""):
        """
        初始化商品
        
        Args:
            product_id: 商品编号
            name: 商品名称
            category: 商品类别
            price: 商品价格
            stock: 库存数量
            supplier: 供应商
            description: 商品描述
        """
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock
        self.supplier = supplier
        self.description = description
        self.sales_count = 0  # 销售数量
        self.min_stock = 10  # 最小库存预警值
    
    def to_dict(self):
        """转换为字典格式"""
        return {
            'product_id': self.product_id,
            'name': self.name,
            'category': self.category,
            'price': self.price,
            'stock': self.stock,
            'supplier': self.supplier,
            'description': self.description,
            'sales_count': self.sales_count,
            'min_stock': self.min_stock
        }
    
    @classmethod
    def from_dict(cls, data):
        """从字典创建商品对象"""
        product = cls(
            product_id=data['product_id'],
            name=data['name'],
            category=data['category'],
            price=data['price'],
            stock=data['stock'],
            supplier=data.get('supplier', ''),
            description=data.get('description', '')
        )
        product.sales_count = data.get('sales_count', 0)
        product.min_stock = data.get('min_stock', 10)
        return product
    
    def update_stock(self, quantity):
        """
        更新库存
        
        Args:
            quantity: 库存变化量（正数为入库，负数为出库）
            
        Returns:
            bool: 是否更新成功
        """
        new_stock = self.stock + quantity
        if new_stock < 0:
            return False
        self.stock = new_stock
        return True
    
    def sell(self, quantity):
        """
        销售商品
        
        Args:
            quantity: 销售数量
            
        Returns:
            bool: 是否销售成功
        """
        if self.stock < quantity:
            return False
        self.stock -= quantity
        self.sales_count += quantity
        return True
    
    def is_low_stock(self):
        """检查是否库存不足"""
        return self.stock <= self.min_stock
    
    def set_min_stock(self, min_stock):
        """设置最小库存预警值"""
        self.min_stock = min_stock
    
    def get_total_value(self):
        """获取商品库存总价值"""
        return self.price * self.stock
    
    def __str__(self):
        """字符串表示"""
        stock_warning = " [库存预警]" if self.is_low_stock() else ""
        return (f"商品编号: {self.product_id} | 名称: {self.name} | "
                f"类别: {self.category} | 价格: ¥{self.price:.2f} | "
                f"库存: {self.stock}{stock_warning} | 已售: {self.sales_count}")
    
    def __repr__(self):
        return f"Product(id={self.product_id}, name={self.name}, stock={self.stock})"


class SalesRecord:
    """销售记录类"""
    
    def __init__(self, record_id, product_id, product_name, quantity, unit_price, total_price, timestamp):
        """
        初始化销售记录
        
        Args:
            record_id: 记录编号
            product_id: 商品编号
            product_name: 商品名称
            quantity: 销售数量
            unit_price: 单价
            total_price: 总价
            timestamp: 销售时间戳
        """
        self.record_id = record_id
        self.product_id = product_id
        self.product_name = product_name
        self.quantity = quantity
        self.unit_price = unit_price
        self.total_price = total_price
        self.timestamp = timestamp
    
    def to_dict(self):
        """转换为字典格式"""
        return {
            'record_id': self.record_id,
            'product_id': self.product_id,
            'product_name': self.product_name,
            'quantity': self.quantity,
            'unit_price': self.unit_price,
            'total_price': self.total_price,
            'timestamp': self.timestamp
        }
    
    @classmethod
    def from_dict(cls, data):
        """从字典创建销售记录对象"""
        return cls(
            record_id=data['record_id'],
            product_id=data['product_id'],
            product_name=data['product_name'],
            quantity=data['quantity'],
            unit_price=data['unit_price'],
            total_price=data['total_price'],
            timestamp=data['timestamp']
        )
    
    def __str__(self):
        """字符串表示"""
        return (f"记录编号: {self.record_id} | 商品: {self.product_name} | "
                f"数量: {self.quantity} | 单价: ¥{self.unit_price:.2f} | "
                f"总价: ¥{self.total_price:.2f} | 时间: {self.timestamp}")


if __name__ == "__main__":
    # 测试商品类
    print("=== 商品类测试 ===")
    product = Product("P001", "可口可乐", "饮料", 3.5, 100, "可口可乐公司", "330ml听装")
    print(product)
    
    # 测试销售
    print("\n销售10件商品...")
    if product.sell(10):
        print("销售成功！")
        print(product)
    
    # 测试库存预警
    product.stock = 8
    print("\n设置库存为8...")
    print(product)
    print(f"库存预警: {product.is_low_stock()}")
    
    # 测试销售记录
    print("\n=== 销售记录测试 ===")
    import time
    record = SalesRecord(
        "SR001", "P001", "可口可乐", 10, 3.5, 35.0,
        time.strftime("%Y-%m-%d %H:%M:%S")
    )
    print(record)
