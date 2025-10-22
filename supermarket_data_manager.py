"""
始终生效
超市管理系统 - 数据持久化管理
负责数据的保存和加载
"""

import json
import os
from supermarket_product import Product, SalesRecord


class SupermarketDataManager:
    """超市数据管理器"""
    
    def __init__(self, data_file="supermarket_data.json"):
        """
        初始化数据管理器
        
        Args:
            data_file: 数据文件路径
        """
        self.data_file = data_file
    
    def save_data(self, system):
        """
        保存系统数据到文件
        
        Args:
            system: SupermarketSystem对象
            
        Returns:
            bool: 是否保存成功
        """
        try:
            data = {
                'products': [p.to_dict() for p in system.products.values()],
                'sales_records': [r.to_dict() for r in system.sales_records],
                'next_product_id': system.next_product_id,
                'next_record_id': system.next_record_id
            }
            
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            return True
        except Exception as e:
            print(f"保存数据失败: {e}")
            return False
    
    def load_data(self, system):
        """
        从文件加载数据到系统
        
        Args:
            system: SupermarketSystem对象
            
        Returns:
            bool: 是否加载成功
        """
        if not os.path.exists(self.data_file):
            return False
        
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # 清空现有数据
            system.products.clear()
            system.sales_records.clear()
            
            # 加载商品
            for product_data in data.get('products', []):
                product = Product.from_dict(product_data)
                system.products[product.product_id] = product
            
            # 加载销售记录
            for record_data in data.get('sales_records', []):
                record = SalesRecord.from_dict(record_data)
                system.sales_records.append(record)
            
            # 加载计数器
            system.next_product_id = data.get('next_product_id', 1)
            system.next_record_id = data.get('next_record_id', 1)
            
            return True
        except Exception as e:
            print(f"加载数据失败: {e}")
            return False
    
    def backup_data(self, backup_file=""):
        """
        备份数据文件
        
        Args:
            backup_file: 备份文件路径，为空则自动生成
            
        Returns:
            str: 备份文件路径，失败返回None
        """
        if not os.path.exists(self.data_file):
            return None
        
        try:
            import time
            if not backup_file:
                timestamp = time.strftime("%Y%m%d_%H%M%S")
                backup_file = f"supermarket_backup_{timestamp}.json"
            
            with open(self.data_file, 'r', encoding='utf-8') as f:
                data = f.read()
            
            with open(backup_file, 'w', encoding='utf-8') as f:
                f.write(data)
            
            return backup_file
        except Exception as e:
            print(f"备份数据失败: {e}")
            return None
    
    def export_to_csv(self, system, csv_file="supermarket_products.csv"):
        """
        导出商品数据为CSV格式
        
        Args:
            system: SupermarketSystem对象
            csv_file: CSV文件路径
            
        Returns:
            bool: 是否导出成功
        """
        try:
            with open(csv_file, 'w', encoding='utf-8') as f:
                # 写入表头
                f.write("商品编号,商品名称,类别,价格,库存,已售,供应商,描述\n")
                
                # 写入数据
                for product in system.products.values():
                    f.write(f"{product.product_id},{product.name},{product.category},"
                           f"{product.price},{product.stock},{product.sales_count},"
                           f"{product.supplier},{product.description}\n")
            
            return True
        except Exception as e:
            print(f"导出CSV失败: {e}")
            return False
    
    def import_from_csv(self, system, csv_file):
        """
        从CSV文件导入商品数据
        
        Args:
            system: SupermarketSystem对象
            csv_file: CSV文件路径
            
        Returns:
            int: 导入的商品数量，失败返回-1
        """
        if not os.path.exists(csv_file):
            return -1
        
        try:
            count = 0
            with open(csv_file, 'r', encoding='utf-8') as f:
                # 跳过表头
                next(f)
                
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    
                    parts = line.split(',')
                    if len(parts) >= 5:
                        name = parts[1]
                        category = parts[2]
                        price = float(parts[3])
                        stock = int(parts[4])
                        supplier = parts[6] if len(parts) > 6 else ""
                        description = parts[7] if len(parts) > 7 else ""
                        
                        if system.add_product(name, category, price, stock, supplier, description):
                            count += 1
            
            return count
        except Exception as e:
            print(f"导入CSV失败: {e}")
            return -1


if __name__ == "__main__":
    # 测试数据管理器
    print("=== 数据管理器测试 ===\n")
    
    from supermarket_system import SupermarketSystem
    
    # 创建系统并添加测试数据
    system = SupermarketSystem()
    system.add_product("测试商品1", "测试类别", 10.0, 100)
    system.add_product("测试商品2", "测试类别", 20.0, 50)
    
    # 保存数据
    manager = SupermarketDataManager("test_supermarket.json")
    print("保存数据...")
    if manager.save_data(system):
        print("保存成功！")
    
    # 加载数据
    new_system = SupermarketSystem()
    print("\n加载数据...")
    if manager.load_data(new_system):
        print("加载成功！")
        print(f"加载了 {len(new_system.products)} 个商品")
        for product in new_system.get_all_products():
            print(f"  - {product.name}")
    
    # 导出CSV
    print("\n导出CSV...")
    if manager.export_to_csv(new_system, "test_products.csv"):
        print("导出成功！")
    
    # 备份
    print("\n备份数据...")
    backup_file = manager.backup_data()
    if backup_file:
        print(f"备份成功: {backup_file}")
    
    # 清理测试文件
    import os
    for f in ["test_supermarket.json", "test_products.csv"]:
        if os.path.exists(f):
            os.remove(f)
    if backup_file and os.path.exists(backup_file):
        os.remove(backup_file)
    print("\n测试完成，临时文件已清理")
