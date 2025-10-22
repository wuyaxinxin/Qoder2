"""
始终生效
超市管理系统 - 核心业务逻辑
实现商品管理、库存管理、销售管理等核心功能
"""

import time
from supermarket_product import Product, SalesRecord


class SupermarketSystem:
    """超市管理系统核心类"""
    
    def __init__(self):
        """初始化超市管理系统"""
        self.products = {}  # 商品字典 {product_id: Product}
        self.sales_records = []  # 销售记录列表
        self.next_product_id = 1  # 下一个商品编号
        self.next_record_id = 1  # 下一个销售记录编号
    
    # ==================== 商品管理 ====================
    
    def add_product(self, name, category, price, stock, supplier="", description=""):
        """
        添加商品
        
        Args:
            name: 商品名称
            category: 商品类别
            price: 商品价格
            stock: 初始库存
            supplier: 供应商
            description: 商品描述
            
        Returns:
            Product: 添加的商品对象，失败返回None
        """
        # 验证数据
        if not name or not category:
            return None
        if price <= 0 or stock < 0:
            return None
        
        # 生成商品编号
        product_id = f"P{self.next_product_id:04d}"
        self.next_product_id += 1
        
        # 创建商品
        product = Product(product_id, name, category, price, stock, supplier, description)
        self.products[product_id] = product
        return product
    
    def delete_product(self, product_id):
        """
        删除商品
        
        Args:
            product_id: 商品编号
            
        Returns:
            bool: 是否删除成功
        """
        if product_id in self.products:
            del self.products[product_id]
            return True
        return False
    
    def update_product(self, product_id, **kwargs):
        """
        更新商品信息
        
        Args:
            product_id: 商品编号
            **kwargs: 要更新的字段
            
        Returns:
            bool: 是否更新成功
        """
        if product_id not in self.products:
            return False
        
        product = self.products[product_id]
        
        # 更新允许的字段
        allowed_fields = ['name', 'category', 'price', 'supplier', 'description', 'min_stock']
        for key, value in kwargs.items():
            if key in allowed_fields:
                setattr(product, key, value)
        
        return True
    
    def get_product(self, product_id):
        """
        获取商品信息
        
        Args:
            product_id: 商品编号
            
        Returns:
            Product: 商品对象，不存在返回None
        """
        return self.products.get(product_id)
    
    def search_products(self, keyword="", category=""):
        """
        搜索商品
        
        Args:
            keyword: 关键词（搜索名称）
            category: 商品类别
            
        Returns:
            list: 符合条件的商品列表
        """
        results = []
        for product in self.products.values():
            # 类别过滤
            if category and product.category != category:
                continue
            # 关键词过滤
            if keyword and keyword.lower() not in product.name.lower():
                continue
            results.append(product)
        return results
    
    def get_all_products(self):
        """获取所有商品"""
        return list(self.products.values())
    
    def get_all_categories(self):
        """获取所有商品类别"""
        categories = set()
        for product in self.products.values():
            categories.add(product.category)
        return sorted(list(categories))
    
    # ==================== 库存管理 ====================
    
    def stock_in(self, product_id, quantity):
        """
        商品入库
        
        Args:
            product_id: 商品编号
            quantity: 入库数量
            
        Returns:
            bool: 是否入库成功
        """
        if product_id not in self.products or quantity <= 0:
            return False
        
        product = self.products[product_id]
        return product.update_stock(quantity)
    
    def stock_out(self, product_id, quantity):
        """
        商品出库（非销售）
        
        Args:
            product_id: 商品编号
            quantity: 出库数量
            
        Returns:
            bool: 是否出库成功
        """
        if product_id not in self.products or quantity <= 0:
            return False
        
        product = self.products[product_id]
        return product.update_stock(-quantity)
    
    def get_low_stock_products(self):
        """获取库存不足的商品列表"""
        low_stock = []
        for product in self.products.values():
            if product.is_low_stock():
                low_stock.append(product)
        return low_stock
    
    def get_stock_statistics(self):
        """
        获取库存统计信息
        
        Returns:
            dict: 统计信息
        """
        total_products = len(self.products)
        total_stock = sum(p.stock for p in self.products.values())
        total_value = sum(p.get_total_value() for p in self.products.values())
        low_stock_count = len(self.get_low_stock_products())
        
        return {
            'total_products': total_products,
            'total_stock': total_stock,
            'total_value': total_value,
            'low_stock_count': low_stock_count
        }
    
    # ==================== 销售管理 ====================
    
    def sell_product(self, product_id, quantity):
        """
        销售商品
        
        Args:
            product_id: 商品编号
            quantity: 销售数量
            
        Returns:
            SalesRecord: 销售记录，失败返回None
        """
        if product_id not in self.products or quantity <= 0:
            return None
        
        product = self.products[product_id]
        
        # 检查库存
        if product.stock < quantity:
            return None
        
        # 执行销售
        if not product.sell(quantity):
            return None
        
        # 创建销售记录
        record_id = f"SR{self.next_record_id:06d}"
        self.next_record_id += 1
        
        total_price = product.price * quantity
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        
        record = SalesRecord(
            record_id, product_id, product.name,
            quantity, product.price, total_price, timestamp
        )
        self.sales_records.append(record)
        
        return record
    
    def refund_product(self, record_id):
        """
        退货
        
        Args:
            record_id: 销售记录编号
            
        Returns:
            bool: 是否退货成功
        """
        # 查找销售记录
        record = None
        for r in self.sales_records:
            if r.record_id == record_id:
                record = r
                break
        
        if not record:
            return False
        
        # 恢复库存
        product_id = record.product_id
        if product_id in self.products:
            product = self.products[product_id]
            product.update_stock(record.quantity)
            product.sales_count -= record.quantity
        
        # 删除销售记录
        self.sales_records.remove(record)
        return True
    
    def get_sales_records(self, start_date="", end_date=""):
        """
        获取销售记录
        
        Args:
            start_date: 开始日期（YYYY-MM-DD）
            end_date: 结束日期（YYYY-MM-DD）
            
        Returns:
            list: 销售记录列表
        """
        if not start_date and not end_date:
            return self.sales_records
        
        results = []
        for record in self.sales_records:
            record_date = record.timestamp.split()[0]
            if start_date and record_date < start_date:
                continue
            if end_date and record_date > end_date:
                continue
            results.append(record)
        
        return results
    
    def get_sales_statistics(self, start_date="", end_date=""):
        """
        获取销售统计信息
        
        Args:
            start_date: 开始日期（YYYY-MM-DD）
            end_date: 结束日期（YYYY-MM-DD）
            
        Returns:
            dict: 统计信息
        """
        records = self.get_sales_records(start_date, end_date)
        
        total_sales = len(records)
        total_revenue = sum(r.total_price for r in records)
        total_quantity = sum(r.quantity for r in records)
        
        return {
            'total_sales': total_sales,
            'total_revenue': total_revenue,
            'total_quantity': total_quantity
        }
    
    def get_top_selling_products(self, limit=10):
        """
        获取热门商品
        
        Args:
            limit: 返回数量限制
            
        Returns:
            list: 按销量排序的商品列表
        """
        products = list(self.products.values())
        products.sort(key=lambda p: p.sales_count, reverse=True)
        return products[:limit]
    
    def get_product_sales_detail(self, product_id):
        """
        获取商品销售明细
        
        Args:
            product_id: 商品编号
            
        Returns:
            dict: 销售明细
        """
        if product_id not in self.products:
            return None
        
        product = self.products[product_id]
        records = [r for r in self.sales_records if r.product_id == product_id]
        total_revenue = sum(r.total_price for r in records)
        
        return {
            'product': product,
            'sales_count': product.sales_count,
            'total_revenue': total_revenue,
            'sales_records': records
        }


if __name__ == "__main__":
    # 测试超市管理系统
    print("=== 超市管理系统测试 ===\n")
    
    system = SupermarketSystem()
    
    # 添加商品
    print("1. 添加商品测试")
    p1 = system.add_product("可口可乐", "饮料", 3.5, 100, "可口可乐公司")
    p2 = system.add_product("百事可乐", "饮料", 3.0, 80, "百事公司")
    p3 = system.add_product("康师傅方便面", "食品", 5.5, 50, "康师傅")
    print(f"添加了 {len(system.get_all_products())} 个商品\n")
    
    # 显示所有商品
    print("2. 商品列表")
    for product in system.get_all_products():
        print(product)
    print()
    
    # 销售测试
    print("3. 销售测试")
    if p1:
        record = system.sell_product(p1.product_id, 10)
        if record:
            print(f"销售成功: {record}")
    print()
    
    # 库存统计
    print("4. 库存统计")
    stats = system.get_stock_statistics()
    print(f"商品总数: {stats['total_products']}")
    print(f"库存总量: {stats['total_stock']}")
    print(f"库存总价值: ¥{stats['total_value']:.2f}")
    print()
    
    # 销售统计
    print("5. 销售统计")
    sales_stats = system.get_sales_statistics()
    print(f"销售记录数: {sales_stats['total_sales']}")
    print(f"销售总额: ¥{sales_stats['total_revenue']:.2f}")
    print(f"销售总量: {sales_stats['total_quantity']}")
