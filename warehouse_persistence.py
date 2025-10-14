"""
仓库管理系统数据持久化模块
提供数据保存和加载功能，支持JSON格式存储
"""

import json
import os
from typing import Dict, List, Optional
from datetime import datetime
from warehouse_models import Product, StockRecord, TransactionRecord, Warehouse, StockAlert
from warehouse_manager import WarehouseManager


class DataPersistence:
    """数据持久化管理器"""
    
    def __init__(self, data_dir: str = "warehouse_data"):
        """
        初始化数据持久化管理器
        
        Args:
            data_dir: 数据存储目录
        """
        self.data_dir = data_dir
        self._ensure_data_directory()
        
        # 定义各类数据文件路径
        self.products_file = os.path.join(data_dir, "products.json")
        self.stock_records_file = os.path.join(data_dir, "stock_records.json")
        self.transactions_file = os.path.join(data_dir, "transactions.json")
        self.warehouses_file = os.path.join(data_dir, "warehouses.json")
        self.alerts_file = os.path.join(data_dir, "alerts.json")
        self.settings_file = os.path.join(data_dir, "settings.json")
    
    def _ensure_data_directory(self):
        """确保数据目录存在"""
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
    
    def save_warehouse_data(self, warehouse_manager: WarehouseManager) -> bool:
        """
        保存仓库管理器的所有数据
        
        Args:
            warehouse_manager: 仓库管理器实例
            
        Returns:
            bool: 保存是否成功
        """
        try:
            # 保存商品数据
            self._save_products(warehouse_manager.products)
            
            # 保存库存记录
            self._save_stock_records(warehouse_manager.stock_records)
            
            # 保存交易历史
            self._save_transactions(warehouse_manager.transaction_history)
            
            # 保存仓库信息
            self._save_warehouses(warehouse_manager.warehouses)
            
            # 保存预警信息
            self._save_alerts(warehouse_manager.alerts)
            
            # 保存设置信息
            self._save_settings(warehouse_manager.low_stock_thresholds)
            
            return True
            
        except Exception as e:
            print(f"保存数据时出错: {e}")
            return False
    
    def load_warehouse_data(self, warehouse_manager: WarehouseManager) -> bool:
        """
        加载数据到仓库管理器
        
        Args:
            warehouse_manager: 仓库管理器实例
            
        Returns:
            bool: 加载是否成功
        """
        try:
            # 加载商品数据
            warehouse_manager.products = self._load_products()
            
            # 加载库存记录
            warehouse_manager.stock_records = self._load_stock_records()
            
            # 加载交易历史
            warehouse_manager.transaction_history = self._load_transactions()
            
            # 加载仓库信息
            warehouse_manager.warehouses = self._load_warehouses()
            
            # 加载预警信息
            warehouse_manager.alerts = self._load_alerts()
            
            # 加载设置信息
            warehouse_manager.low_stock_thresholds = self._load_settings()
            
            return True
            
        except Exception as e:
            print(f"加载数据时出错: {e}")
            return False
    
    def _save_products(self, products: Dict[str, Product]):
        """保存商品数据"""
        products_data = {}
        for product_id, product in products.items():
            products_data[product_id] = product.to_dict()
        
        with open(self.products_file, 'w', encoding='utf-8') as f:
            json.dump(products_data, f, ensure_ascii=False, indent=2)
    
    def _load_products(self) -> Dict[str, Product]:
        """加载商品数据"""
        products = {}
        if os.path.exists(self.products_file):
            try:
                with open(self.products_file, 'r', encoding='utf-8') as f:
                    products_data = json.load(f)
                
                for product_id, data in products_data.items():
                    products[product_id] = Product.from_dict(data)
            except Exception as e:
                print(f"加载商品数据时出错: {e}")
        
        return products
    
    def _save_stock_records(self, stock_records: Dict[str, StockRecord]):
        """保存库存记录"""
        records_data = {}
        for record_id, record in stock_records.items():
            records_data[record_id] = record.to_dict()
        
        with open(self.stock_records_file, 'w', encoding='utf-8') as f:
            json.dump(records_data, f, ensure_ascii=False, indent=2)
    
    def _load_stock_records(self) -> Dict[str, StockRecord]:
        """加载库存记录"""
        stock_records = {}
        if os.path.exists(self.stock_records_file):
            try:
                with open(self.stock_records_file, 'r', encoding='utf-8') as f:
                    records_data = json.load(f)
                
                for record_id, data in records_data.items():
                    stock_records[record_id] = StockRecord.from_dict(data)
            except Exception as e:
                print(f"加载库存记录时出错: {e}")
        
        return stock_records
    
    def _save_transactions(self, transactions: List[TransactionRecord]):
        """保存交易记录"""
        transactions_data = []
        for transaction in transactions:
            transactions_data.append(transaction.to_dict())
        
        with open(self.transactions_file, 'w', encoding='utf-8') as f:
            json.dump(transactions_data, f, ensure_ascii=False, indent=2)
    
    def _load_transactions(self) -> List[TransactionRecord]:
        """加载交易记录"""
        transactions = []
        if os.path.exists(self.transactions_file):
            try:
                with open(self.transactions_file, 'r', encoding='utf-8') as f:
                    transactions_data = json.load(f)
                
                for data in transactions_data:
                    transactions.append(TransactionRecord.from_dict(data))
            except Exception as e:
                print(f"加载交易记录时出错: {e}")
        
        return transactions
    
    def _save_warehouses(self, warehouses: Dict[str, Warehouse]):
        """保存仓库信息"""
        warehouses_data = {}
        for warehouse_id, warehouse in warehouses.items():
            warehouses_data[warehouse_id] = warehouse.to_dict()
        
        with open(self.warehouses_file, 'w', encoding='utf-8') as f:
            json.dump(warehouses_data, f, ensure_ascii=False, indent=2)
    
    def _load_warehouses(self) -> Dict[str, Warehouse]:
        """加载仓库信息"""
        warehouses = {}
        if os.path.exists(self.warehouses_file):
            try:
                with open(self.warehouses_file, 'r', encoding='utf-8') as f:
                    warehouses_data = json.load(f)
                
                for warehouse_id, data in warehouses_data.items():
                    warehouses[warehouse_id] = Warehouse.from_dict(data)
            except Exception as e:
                print(f"加载仓库信息时出错: {e}")
        
        return warehouses
    
    def _save_alerts(self, alerts: Dict[str, StockAlert]):
        """保存预警信息"""
        alerts_data = {}
        for alert_id, alert in alerts.items():
            alerts_data[alert_id] = alert.to_dict()
        
        with open(self.alerts_file, 'w', encoding='utf-8') as f:
            json.dump(alerts_data, f, ensure_ascii=False, indent=2)
    
    def _load_alerts(self) -> Dict[str, StockAlert]:
        """加载预警信息"""
        alerts = {}
        if os.path.exists(self.alerts_file):
            try:
                with open(self.alerts_file, 'r', encoding='utf-8') as f:
                    alerts_data = json.load(f)
                
                for alert_id, data in alerts_data.items():
                    alerts[alert_id] = StockAlert.from_dict(data)
            except Exception as e:
                print(f"加载预警信息时出错: {e}")
        
        return alerts
    
    def _save_settings(self, low_stock_thresholds: Dict[str, int]):
        """保存设置信息"""
        settings_data = {
            'low_stock_thresholds': low_stock_thresholds,
            'last_saved': datetime.now().isoformat()
        }
        
        with open(self.settings_file, 'w', encoding='utf-8') as f:
            json.dump(settings_data, f, ensure_ascii=False, indent=2)
    
    def _load_settings(self) -> Dict[str, int]:
        """加载设置信息"""
        low_stock_thresholds = {}
        if os.path.exists(self.settings_file):
            try:
                with open(self.settings_file, 'r', encoding='utf-8') as f:
                    settings_data = json.load(f)
                
                low_stock_thresholds = settings_data.get('low_stock_thresholds', {})
            except Exception as e:
                print(f"加载设置信息时出错: {e}")
        
        return low_stock_thresholds
    
    def backup_data(self, backup_name: str = None) -> bool:
        """
        备份当前数据
        
        Args:
            backup_name: 备份名称，默认为当前时间戳
            
        Returns:
            bool: 备份是否成功
        """
        try:
            if backup_name is None:
                backup_name = datetime.now().strftime("%Y%m%d_%H%M%S")
            
            backup_dir = os.path.join(self.data_dir, "backups", backup_name)
            
            if not os.path.exists(backup_dir):
                os.makedirs(backup_dir)
            
            # 复制所有数据文件到备份目录
            import shutil
            
            files_to_backup = [
                self.products_file,
                self.stock_records_file,
                self.transactions_file,
                self.warehouses_file,
                self.alerts_file,
                self.settings_file
            ]
            
            for file_path in files_to_backup:
                if os.path.exists(file_path):
                    backup_file_path = os.path.join(backup_dir, os.path.basename(file_path))
                    shutil.copy2(file_path, backup_file_path)
            
            print(f"数据备份完成: {backup_dir}")
            return True
            
        except Exception as e:
            print(f"备份数据时出错: {e}")
            return False
    
    def restore_data(self, backup_name: str) -> bool:
        """
        从备份恢复数据
        
        Args:
            backup_name: 备份名称
            
        Returns:
            bool: 恢复是否成功
        """
        try:
            backup_dir = os.path.join(self.data_dir, "backups", backup_name)
            
            if not os.path.exists(backup_dir):
                print(f"备份目录不存在: {backup_dir}")
                return False
            
            # 恢复所有数据文件
            import shutil
            
            files_to_restore = [
                "products.json",
                "stock_records.json",
                "transactions.json",
                "warehouses.json",
                "alerts.json",
                "settings.json"
            ]
            
            for filename in files_to_restore:
                backup_file_path = os.path.join(backup_dir, filename)
                if os.path.exists(backup_file_path):
                    target_file_path = os.path.join(self.data_dir, filename)
                    shutil.copy2(backup_file_path, target_file_path)
            
            print(f"数据恢复完成，从备份: {backup_name}")
            return True
            
        except Exception as e:
            print(f"恢复数据时出错: {e}")
            return False
    
    def list_backups(self) -> List[str]:
        """
        列出所有可用的备份
        
        Returns:
            List[str]: 备份名称列表
        """
        backups_dir = os.path.join(self.data_dir, "backups")
        if not os.path.exists(backups_dir):
            return []
        
        backups = []
        for item in os.listdir(backups_dir):
            backup_path = os.path.join(backups_dir, item)
            if os.path.isdir(backup_path):
                backups.append(item)
        
        # 按时间排序
        backups.sort(reverse=True)
        return backups
    
    def export_to_csv(self, warehouse_manager: WarehouseManager, export_dir: str = None) -> bool:
        """
        导出数据为CSV格式
        
        Args:
            warehouse_manager: 仓库管理器实例
            export_dir: 导出目录，默认为数据目录下的exports文件夹
            
        Returns:
            bool: 导出是否成功
        """
        try:
            import csv
            
            if export_dir is None:
                export_dir = os.path.join(self.data_dir, "exports")
            
            if not os.path.exists(export_dir):
                os.makedirs(export_dir)
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            
            # 导出商品信息
            products_csv = os.path.join(export_dir, f"products_{timestamp}.csv")
            with open(products_csv, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['商品ID', '商品名称', '描述', '分类', '单价', '单位', '创建时间', '更新时间'])
                
                for product in warehouse_manager.products.values():
                    writer.writerow([
                        product.product_id,
                        product.name,
                        product.description,
                        product.category,
                        product.unit_price,
                        product.unit,
                        product.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                        product.updated_at.strftime('%Y-%m-%d %H:%M:%S')
                    ])
            
            # 导出库存信息
            stock_csv = os.path.join(export_dir, f"stock_{timestamp}.csv")
            with open(stock_csv, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['记录ID', '商品ID', '数量', '位置', '批次号', '过期日期', '创建时间'])
                
                for record in warehouse_manager.stock_records.values():
                    if record.quantity > 0:  # 只导出有库存的记录
                        expiry_date = record.expiry_date.strftime('%Y-%m-%d') if record.expiry_date else ''
                        writer.writerow([
                            record.record_id,
                            record.product_id,
                            record.quantity,
                            record.location,
                            record.batch_number,
                            expiry_date,
                            record.created_at.strftime('%Y-%m-%d %H:%M:%S')
                        ])
            
            # 导出交易记录
            transactions_csv = os.path.join(export_dir, f"transactions_{timestamp}.csv")
            with open(transactions_csv, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['交易ID', '交易类型', '商品ID', '数量', '位置', '操作员', '备注', '时间'])
                
                for transaction in warehouse_manager.transaction_history:
                    writer.writerow([
                        transaction.transaction_id,
                        transaction.transaction_type,
                        transaction.product_id,
                        transaction.quantity,
                        transaction.location,
                        transaction.operator,
                        transaction.notes,
                        transaction.timestamp.strftime('%Y-%m-%d %H:%M:%S')
                    ])
            
            print(f"数据已导出到CSV文件，目录: {export_dir}")
            return True
            
        except Exception as e:
            print(f"导出CSV时出错: {e}")
            return False
    
    def get_data_statistics(self) -> Dict:
        """
        获取数据统计信息
        
        Returns:
            Dict: 数据统计信息
        """
        stats = {
            'files_exist': {},
            'file_sizes': {},
            'last_modified': {}
        }
        
        files_to_check = [
            ('products', self.products_file),
            ('stock_records', self.stock_records_file),
            ('transactions', self.transactions_file),
            ('warehouses', self.warehouses_file),
            ('alerts', self.alerts_file),
            ('settings', self.settings_file)
        ]
        
        for file_type, file_path in files_to_check:
            if os.path.exists(file_path):
                stats['files_exist'][file_type] = True
                stats['file_sizes'][file_type] = os.path.getsize(file_path)
                stats['last_modified'][file_type] = datetime.fromtimestamp(
                    os.path.getmtime(file_path)).isoformat()
            else:
                stats['files_exist'][file_type] = False
                stats['file_sizes'][file_type] = 0
                stats['last_modified'][file_type] = None
        
        return stats