"""
仓库管理系统业务逻辑层
实现仓库操作的核心业务逻辑，包括商品管理、库存管理、入库出库等功能
"""

from typing import Dict, List, Optional, Tuple
from datetime import datetime, timedelta
from warehouse_models import Product, StockRecord, TransactionRecord, Warehouse, StockAlert
import json


class WarehouseManager:
    """仓库管理器 - 核心业务逻辑类"""
    
    def __init__(self):
        self.products: Dict[str, Product] = {}
        self.stock_records: Dict[str, StockRecord] = {}
        self.transaction_history: List[TransactionRecord] = []
        self.warehouses: Dict[str, Warehouse] = {}
        self.alerts: Dict[str, StockAlert] = {}
        self.low_stock_thresholds: Dict[str, int] = {}  # 商品ID -> 最低库存阈值
    
    # 商品管理功能
    def add_product(self, product_id: str, name: str, description: str, 
                   category: str, unit_price: float, unit: str = "个") -> bool:
        """添加新商品"""
        if product_id in self.products:
            return False
        
        product = Product(product_id, name, description, category, unit_price, unit)
        self.products[product_id] = product
        return True
    
    def update_product(self, product_id: str, **kwargs) -> bool:
        """更新商品信息"""
        if product_id not in self.products:
            return False
        
        self.products[product_id].update_info(**kwargs)
        return True
    
    def remove_product(self, product_id: str) -> bool:
        """删除商品（仅当库存为0时）"""
        if product_id not in self.products:
            return False
        
        # 检查是否还有库存
        total_stock = self.get_total_stock(product_id)
        if total_stock > 0:
            return False
        
        # 删除商品及相关记录
        del self.products[product_id]
        # 删除相关库存记录
        self.stock_records = {k: v for k, v in self.stock_records.items() 
                             if v.product_id != product_id}
        # 删除预警阈值设置
        if product_id in self.low_stock_thresholds:
            del self.low_stock_thresholds[product_id]
        
        return True
    
    def get_product(self, product_id: str) -> Optional[Product]:
        """获取商品信息"""
        return self.products.get(product_id)
    
    def list_products(self, category: str = None) -> List[Product]:
        """列出所有商品或指定分类的商品"""
        products = list(self.products.values())
        if category:
            products = [p for p in products if p.category == category]
        return products
    
    # 仓库管理功能
    def add_warehouse(self, warehouse_id: str, name: str, address: str, 
                     manager: str, capacity: int = None) -> bool:
        """添加仓库"""
        if warehouse_id in self.warehouses:
            return False
        
        warehouse = Warehouse(warehouse_id, name, address, manager, capacity)
        self.warehouses[warehouse_id] = warehouse
        return True
    
    def add_warehouse_location(self, warehouse_id: str, location: str) -> bool:
        """为仓库添加存储位置"""
        if warehouse_id not in self.warehouses:
            return False
        
        self.warehouses[warehouse_id].add_location(location)
        return True
    
    # 库存管理功能
    def add_stock(self, product_id: str, quantity: int, location: str, 
                 operator: str, batch_number: str = None, 
                 expiry_date: datetime = None) -> bool:
        """入库操作"""
        if product_id not in self.products:
            return False
        
        if quantity <= 0:
            return False
        
        # 创建库存记录
        stock_record = StockRecord(product_id, quantity, location, batch_number, expiry_date)
        self.stock_records[stock_record.record_id] = stock_record
        
        # 记录交易
        transaction = TransactionRecord('入库', product_id, quantity, location, operator)
        self.transaction_history.append(transaction)
        
        # 检查并清除相关预警
        self._check_and_clear_alerts(product_id)
        
        return True
    
    def remove_stock(self, product_id: str, quantity: int, location: str, 
                    operator: str, notes: str = "") -> bool:
        """出库操作"""
        if product_id not in self.products:
            return False
        
        if quantity <= 0:
            return False
        
        # 检查库存是否足够
        available_stock = self.get_stock_by_location(product_id, location)
        if available_stock < quantity:
            return False
        
        # 从指定位置减少库存（先进先出原则）
        remaining_quantity = quantity
        records_to_update = []
        
        for record_id, record in self.stock_records.items():
            if record.product_id == product_id and record.location == location and record.quantity > 0:
                records_to_update.append((record_id, record))
        
        # 按创建时间排序（先进先出）
        records_to_update.sort(key=lambda x: x[1].created_at)
        
        for record_id, record in records_to_update:
            if remaining_quantity <= 0:
                break
            
            if record.quantity >= remaining_quantity:
                record.update_quantity(record.quantity - remaining_quantity)
                remaining_quantity = 0
            else:
                remaining_quantity -= record.quantity
                record.update_quantity(0)
        
        # 记录交易
        transaction = TransactionRecord('出库', product_id, quantity, location, operator, notes)
        self.transaction_history.append(transaction)
        
        # 检查库存预警
        self._check_stock_alerts(product_id)
        
        return True
    
    def transfer_stock(self, product_id: str, quantity: int, from_location: str, 
                      to_location: str, operator: str) -> bool:
        """调拨库存"""
        # 先从源位置出库
        if not self.remove_stock(product_id, quantity, from_location, operator, f"调拨至{to_location}"):
            return False
        
        # 再入库到目标位置
        if not self.add_stock(product_id, quantity, to_location, operator):
            # 如果入库失败，需要回滚出库操作
            self.add_stock(product_id, quantity, from_location, operator)
            return False
        
        # 记录调拨交易
        transaction = TransactionRecord('调拨', product_id, quantity, 
                                      f"{from_location}->{to_location}", operator)
        self.transaction_history.append(transaction)
        
        return True
    
    def inventory_check(self, product_id: str, location: str, actual_quantity: int, 
                       operator: str) -> bool:
        """库存盘点"""
        current_stock = self.get_stock_by_location(product_id, location)
        difference = actual_quantity - current_stock
        
        if difference != 0:
            # 记录盘点差异
            transaction = TransactionRecord('盘点', product_id, difference, location, 
                                          operator, f"盘点调整，实际库存: {actual_quantity}")
            self.transaction_history.append(transaction)
            
            # 调整库存
            if difference > 0:
                # 盘盈，增加库存
                self.add_stock(product_id, difference, location, operator)
            else:
                # 盘亏，减少库存
                self.remove_stock(product_id, abs(difference), location, operator, "盘点调整")
        
        return True
    
    # 查询功能
    def get_total_stock(self, product_id: str) -> int:
        """获取商品总库存"""
        total = 0
        for record in self.stock_records.values():
            if record.product_id == product_id:
                total += record.quantity
        return total
    
    def get_stock_by_location(self, product_id: str, location: str = None) -> int:
        """获取指定位置的库存"""
        total = 0
        for record in self.stock_records.values():
            if record.product_id == product_id:
                if location is None or record.location == location:
                    total += record.quantity
        return total
    
    def get_stock_details(self, product_id: str) -> List[StockRecord]:
        """获取商品的详细库存记录"""
        return [record for record in self.stock_records.values() 
                if record.product_id == product_id and record.quantity > 0]
    
    def get_low_stock_products(self) -> List[Tuple[str, int, int]]:
        """获取低库存商品列表 - 返回(product_id, current_stock, threshold)"""
        low_stock_products = []
        for product_id, threshold in self.low_stock_thresholds.items():
            current_stock = self.get_total_stock(product_id)
            if current_stock <= threshold:
                low_stock_products.append((product_id, current_stock, threshold))
        return low_stock_products
    
    def get_expired_products(self) -> List[StockRecord]:
        """获取已过期的商品"""
        expired_records = []
        for record in self.stock_records.values():
            if record.quantity > 0 and record.is_expired():
                expired_records.append(record)
        return expired_records
    
    def get_expiring_soon_products(self, days: int = 7) -> List[StockRecord]:
        """获取即将过期的商品"""
        expiring_soon = []
        cutoff_date = datetime.now() + timedelta(days=days)
        
        for record in self.stock_records.values():
            if (record.quantity > 0 and record.expiry_date and 
                record.expiry_date <= cutoff_date and not record.is_expired()):
                expiring_soon.append(record)
        
        return expiring_soon
    
    # 预警管理
    def set_low_stock_threshold(self, product_id: str, threshold: int):
        """设置商品的低库存预警阈值"""
        if product_id in self.products:
            self.low_stock_thresholds[product_id] = threshold
    
    def _check_stock_alerts(self, product_id: str):
        """检查并创建库存预警"""
        current_stock = self.get_total_stock(product_id)
        
        # 检查零库存
        if current_stock == 0:
            alert = StockAlert('零库存', product_id, current_stock, 
                             message=f"商品 {product_id} 库存为零")
            self.alerts[alert.alert_id] = alert
        
        # 检查低库存
        elif product_id in self.low_stock_thresholds:
            threshold = self.low_stock_thresholds[product_id]
            if current_stock <= threshold:
                alert = StockAlert('低库存', product_id, current_stock, threshold,
                                 f"商品 {product_id} 库存低于阈值 {threshold}")
                self.alerts[alert.alert_id] = alert
    
    def _check_and_clear_alerts(self, product_id: str):
        """检查并清除已解决的预警"""
        current_stock = self.get_total_stock(product_id)
        threshold = self.low_stock_thresholds.get(product_id, 0)
        
        # 清除已解决的预警
        for alert in self.alerts.values():
            if (alert.product_id == product_id and not alert.is_resolved and
                ((alert.alert_type == '零库存' and current_stock > 0) or
                 (alert.alert_type == '低库存' and current_stock > threshold))):
                alert.resolve()
    
    def check_expiry_alerts(self):
        """检查过期商品预警"""
        for record in self.stock_records.values():
            if record.quantity > 0 and record.is_expired():
                alert = StockAlert('过期', record.product_id, record.quantity,
                                 message=f"批次 {record.batch_number} 已过期")
                self.alerts[alert.alert_id] = alert
    
    def get_active_alerts(self) -> List[StockAlert]:
        """获取未解决的预警"""
        return [alert for alert in self.alerts.values() if not alert.is_resolved]
    
    # 报表功能
    def get_inventory_report(self) -> Dict:
        """生成库存报表"""
        report = {
            'total_products': len(self.products),
            'total_transactions': len(self.transaction_history),
            'active_alerts': len(self.get_active_alerts()),
            'products_by_category': {},
            'stock_summary': [],
            'low_stock_count': len(self.get_low_stock_products()),
            'expired_count': len(self.get_expired_products())
        }
        
        # 按分类统计商品
        for product in self.products.values():
            category = product.category
            if category not in report['products_by_category']:
                report['products_by_category'][category] = 0
            report['products_by_category'][category] += 1
        
        # 库存汇总
        for product_id, product in self.products.items():
            total_stock = self.get_total_stock(product_id)
            total_value = total_stock * product.unit_price
            report['stock_summary'].append({
                'product_id': product_id,
                'product_name': product.name,
                'category': product.category,
                'total_stock': total_stock,
                'unit_price': product.unit_price,
                'total_value': total_value
            })
        
        return report
    
    def get_transaction_history(self, product_id: str = None, 
                               transaction_type: str = None, 
                               days: int = None) -> List[TransactionRecord]:
        """获取交易历史记录"""
        history = self.transaction_history.copy()
        
        # 按商品过滤
        if product_id:
            history = [t for t in history if t.product_id == product_id]
        
        # 按交易类型过滤
        if transaction_type:
            history = [t for t in history if t.transaction_type == transaction_type]
        
        # 按时间过滤
        if days:
            cutoff_date = datetime.now() - timedelta(days=days)
            history = [t for t in history if t.timestamp >= cutoff_date]
        
        # 按时间倒序排列
        history.sort(key=lambda x: x.timestamp, reverse=True)
        
        return history