"""
始终生效
超市管理系统 - 单元测试
测试所有核心功能模块
"""

import unittest
import os
import json
from supermarket_product import Product, SalesRecord
from supermarket_system import SupermarketSystem
from supermarket_data_manager import SupermarketDataManager


class TestProduct(unittest.TestCase):
    """测试商品类"""
    
    def setUp(self):
        """测试前准备"""
        self.product = Product("P001", "可口可乐", "饮料", 3.5, 100, "可口可乐公司", "330ml听装")
    
    def test_product_creation(self):
        """测试商品创建"""
        self.assertEqual(self.product.product_id, "P001")
        self.assertEqual(self.product.name, "可口可乐")
        self.assertEqual(self.product.category, "饮料")
        self.assertEqual(self.product.price, 3.5)
        self.assertEqual(self.product.stock, 100)
    
    def test_update_stock(self):
        """测试更新库存"""
        # 入库
        self.assertTrue(self.product.update_stock(50))
        self.assertEqual(self.product.stock, 150)
        
        # 出库
        self.assertTrue(self.product.update_stock(-30))
        self.assertEqual(self.product.stock, 120)
        
        # 库存不足
        self.assertFalse(self.product.update_stock(-150))
        self.assertEqual(self.product.stock, 120)
    
    def test_sell(self):
        """测试销售"""
        # 正常销售
        self.assertTrue(self.product.sell(10))
        self.assertEqual(self.product.stock, 90)
        self.assertEqual(self.product.sales_count, 10)
        
        # 库存不足
        self.assertFalse(self.product.sell(100))
        self.assertEqual(self.product.stock, 90)
        self.assertEqual(self.product.sales_count, 10)
    
    def test_is_low_stock(self):
        """测试库存预警"""
        self.assertFalse(self.product.is_low_stock())
        
        self.product.stock = 10
        self.assertTrue(self.product.is_low_stock())
        
        self.product.stock = 5
        self.assertTrue(self.product.is_low_stock())
    
    def test_get_total_value(self):
        """测试获取库存总价值"""
        self.assertEqual(self.product.get_total_value(), 350.0)
        
        self.product.stock = 50
        self.assertEqual(self.product.get_total_value(), 175.0)
    
    def test_to_dict_and_from_dict(self):
        """测试字典转换"""
        data = self.product.to_dict()
        self.assertIsInstance(data, dict)
        self.assertEqual(data['product_id'], "P001")
        
        new_product = Product.from_dict(data)
        self.assertEqual(new_product.product_id, self.product.product_id)
        self.assertEqual(new_product.name, self.product.name)
        self.assertEqual(new_product.price, self.product.price)


class TestSupermarketSystem(unittest.TestCase):
    """测试超市管理系统"""
    
    def setUp(self):
        """测试前准备"""
        self.system = SupermarketSystem()
    
    def test_add_product(self):
        """测试添加商品"""
        product = self.system.add_product("可口可乐", "饮料", 3.5, 100, "可口可乐公司")
        self.assertIsNotNone(product)
        self.assertEqual(product.name, "可口可乐")
        self.assertEqual(len(self.system.products), 1)
        
        # 测试非法数据
        self.assertIsNone(self.system.add_product("", "饮料", 3.5, 100))
        self.assertIsNone(self.system.add_product("可口可乐", "", 3.5, 100))
        self.assertIsNone(self.system.add_product("可口可乐", "饮料", -1, 100))
        self.assertIsNone(self.system.add_product("可口可乐", "饮料", 3.5, -10))
    
    def test_delete_product(self):
        """测试删除商品"""
        product = self.system.add_product("可口可乐", "饮料", 3.5, 100)
        product_id = product.product_id if product else ""
        
        self.assertTrue(self.system.delete_product(product_id))
        self.assertEqual(len(self.system.products), 0)
        
        # 删除不存在的商品
        self.assertFalse(self.system.delete_product("P999"))
    
    def test_update_product(self):
        """测试更新商品"""
        product = self.system.add_product("可口可乐", "饮料", 3.5, 100)
        product_id = product.product_id if product else ""
        
        self.assertTrue(self.system.update_product(product_id, name="新名称", price=4.0))
        updated_product = self.system.get_product(product_id)
        if updated_product:
            self.assertEqual(updated_product.name, "新名称")
            self.assertEqual(updated_product.price, 4.0)
        
        # 更新不存在的商品
        self.assertFalse(self.system.update_product("P999", name="测试"))
    
    def test_search_products(self):
        """测试搜索商品"""
        self.system.add_product("可口可乐", "饮料", 3.5, 100)
        self.system.add_product("百事可乐", "饮料", 3.0, 80)
        self.system.add_product("方便面", "食品", 5.5, 50)
        
        # 按名称搜索
        results = self.system.search_products(keyword="可乐")
        self.assertEqual(len(results), 2)
        
        # 按类别搜索
        results = self.system.search_products(category="饮料")
        self.assertEqual(len(results), 2)
        
        # 组合搜索
        results = self.system.search_products(keyword="可口", category="饮料")
        self.assertEqual(len(results), 1)
    
    def test_stock_management(self):
        """测试库存管理"""
        product = self.system.add_product("可口可乐", "饮料", 3.5, 100)
        product_id = product.product_id if product else ""
        
        # 入库
        self.assertTrue(self.system.stock_in(product_id, 50))
        updated = self.system.get_product(product_id)
        if updated:
            self.assertEqual(updated.stock, 150)
        
        # 出库
        self.assertTrue(self.system.stock_out(product_id, 30))
        updated = self.system.get_product(product_id)
        if updated:
            self.assertEqual(updated.stock, 120)
        
        # 库存不足
        self.assertFalse(self.system.stock_out(product_id, 150))
    
    def test_low_stock_detection(self):
        """测试库存预警"""
        product = self.system.add_product("可口可乐", "饮料", 3.5, 5)
        
        low_stock = self.system.get_low_stock_products()
        self.assertEqual(len(low_stock), 1)
        
        # 增加库存
        if product:
            self.system.stock_in(product.product_id, 20)
        low_stock = self.system.get_low_stock_products()
        self.assertEqual(len(low_stock), 0)
    
    def test_sell_product(self):
        """测试销售商品"""
        product = self.system.add_product("可口可乐", "饮料", 3.5, 100)
        product_id = product.product_id if product else ""
        
        # 正常销售
        record = self.system.sell_product(product_id, 10)
        self.assertIsNotNone(record)
        if record:
            self.assertEqual(record.quantity, 10)
            self.assertEqual(record.total_price, 35.0)
        
        updated = self.system.get_product(product_id)
        if updated:
            self.assertEqual(updated.stock, 90)
            self.assertEqual(updated.sales_count, 10)
        
        # 库存不足
        record = self.system.sell_product(product_id, 100)
        self.assertIsNone(record)
    
    def test_refund_product(self):
        """测试退货"""
        product = self.system.add_product("可口可乐", "饮料", 3.5, 100)
        product_id = product.product_id if product else ""
        
        # 销售
        record = self.system.sell_product(product_id, 10)
        record_id = record.record_id if record else ""
        
        # 退货
        self.assertTrue(self.system.refund_product(record_id))
        
        updated = self.system.get_product(product_id)
        if updated:
            self.assertEqual(updated.stock, 100)
            self.assertEqual(updated.sales_count, 0)
        
        self.assertEqual(len(self.system.sales_records), 0)
        
        # 退不存在的记录
        self.assertFalse(self.system.refund_product("SR999"))
    
    def test_sales_statistics(self):
        """测试销售统计"""
        product1 = self.system.add_product("可口可乐", "饮料", 3.5, 100)
        product2 = self.system.add_product("百事可乐", "饮料", 3.0, 80)
        
        if product1:
            self.system.sell_product(product1.product_id, 10)
        if product2:
            self.system.sell_product(product2.product_id, 5)
        
        stats = self.system.get_sales_statistics()
        self.assertEqual(stats['total_sales'], 2)
        self.assertEqual(stats['total_revenue'], 50.0)
        self.assertEqual(stats['total_quantity'], 15)
    
    def test_top_selling_products(self):
        """测试热门商品"""
        product1 = self.system.add_product("可口可乐", "饮料", 3.5, 100)
        product2 = self.system.add_product("百事可乐", "饮料", 3.0, 80)
        product3 = self.system.add_product("方便面", "食品", 5.5, 50)
        
        if product1:
            self.system.sell_product(product1.product_id, 20)
        if product2:
            self.system.sell_product(product2.product_id, 10)
        if product3:
            self.system.sell_product(product3.product_id, 5)
        
        top_products = self.system.get_top_selling_products(2)
        self.assertEqual(len(top_products), 2)
        self.assertEqual(top_products[0].sales_count, 20)
        self.assertEqual(top_products[1].sales_count, 10)


class TestSupermarketDataManager(unittest.TestCase):
    """测试数据管理器"""
    
    def setUp(self):
        """测试前准备"""
        self.test_file = "test_supermarket_data.json"
        self.manager = SupermarketDataManager(self.test_file)
        self.system = SupermarketSystem()
    
    def tearDown(self):
        """测试后清理"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def test_save_and_load_data(self):
        """测试保存和加载数据"""
        # 添加测试数据
        self.system.add_product("测试商品1", "测试类别", 10.0, 100)
        self.system.add_product("测试商品2", "测试类别", 20.0, 50)
        
        # 保存数据
        self.assertTrue(self.manager.save_data(self.system))
        self.assertTrue(os.path.exists(self.test_file))
        
        # 加载数据
        new_system = SupermarketSystem()
        self.assertTrue(self.manager.load_data(new_system))
        self.assertEqual(len(new_system.products), 2)
    
    def test_backup_data(self):
        """测试备份数据"""
        # 创建测试数据文件
        self.system.add_product("测试商品", "测试类别", 10.0, 100)
        self.manager.save_data(self.system)
        
        # 备份
        backup_file = self.manager.backup_data("test_backup.json")
        self.assertIsNotNone(backup_file)
        self.assertTrue(os.path.exists(backup_file) if backup_file else False)
        
        # 清理
        if backup_file and os.path.exists(backup_file):
            os.remove(backup_file)
    
    def test_export_csv(self):
        """测试导出Csv"""
        csv_file = "test_products.csv"
        
        # 添加数据
        self.system.add_product("测试商品", "测试类别", 10.0, 100)
        
        # 导出
        self.assertTrue(self.manager.export_to_csv(self.system, csv_file))
        self.assertTrue(os.path.exists(csv_file))
        
        # 清理
        if os.path.exists(csv_file):
            os.remove(csv_file)


if __name__ == "__main__":
    # 运行测试
    unittest.main(verbosity=2)