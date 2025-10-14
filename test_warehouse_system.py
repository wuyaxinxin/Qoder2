"""
仓库管理系统测试用例
全面测试系统的各项功能
"""

import unittest
import tempfile
import shutil
import os
from datetime import datetime, timedelta
from warehouse_manager import WarehouseManager
from warehouse_persistence import DataPersistence
from warehouse_models import Product, StockRecord, TransactionRecord, Warehouse, StockAlert


class TestWarehouseManager(unittest.TestCase):
    """测试仓库管理器"""
    
    def setUp(self):
        """测试前准备"""
        self.manager = WarehouseManager()
        
        # 添加测试商品
        self.manager.add_product("P001", "苹果", "新鲜苹果", "水果", 5.0, "斤")
        self.manager.add_product("P002", "香蕉", "进口香蕉", "水果", 8.0, "斤")
        self.manager.add_product("P003", "牛奶", "纯牛奶", "饮品", 15.0, "瓶")
    
    def test_add_product(self):
        """测试添加商品"""
        # 测试成功添加
        result = self.manager.add_product("P004", "橙子", "鲜橙", "水果", 6.0, "斤")
        self.assertTrue(result)
        self.assertIn("P004", self.manager.products)
        
        # 测试重复添加
        result = self.manager.add_product("P004", "橙子2", "鲜橙2", "水果", 7.0, "斤")
        self.assertFalse(result)
    
    def test_update_product(self):
        """测试更新商品信息"""
        # 测试更新存在的商品
        result = self.manager.update_product("P001", name="红苹果", unit_price=6.0)
        self.assertTrue(result)
        
        product = self.manager.get_product("P001")
        self.assertEqual(product.name, "红苹果")
        self.assertEqual(product.unit_price, 6.0)
        
        # 测试更新不存在的商品
        result = self.manager.update_product("P999", name="测试")
        self.assertFalse(result)
    
    def test_remove_product(self):
        """测试删除商品"""
        # 添加库存后不能删除
        self.manager.add_stock("P001", 10, "A01", "测试员")
        result = self.manager.remove_product("P001")
        self.assertFalse(result)
        
        # 清空库存后可以删除
        self.manager.remove_stock("P001", 10, "A01", "测试员")
        result = self.manager.remove_product("P001")
        self.assertTrue(result)
        self.assertNotIn("P001", self.manager.products)
    
    def test_stock_operations(self):
        """测试库存操作"""
        # 测试入库
        result = self.manager.add_stock("P001", 50, "A01", "测试员")
        self.assertTrue(result)
        self.assertEqual(self.manager.get_total_stock("P001"), 50)
        
        # 测试出库
        result = self.manager.remove_stock("P001", 20, "A01", "测试员")
        self.assertTrue(result)
        self.assertEqual(self.manager.get_total_stock("P001"), 30)
        
        # 测试出库数量超过库存
        result = self.manager.remove_stock("P001", 50, "A01", "测试员")
        self.assertFalse(result)
        self.assertEqual(self.manager.get_total_stock("P001"), 30)
    
    def test_stock_transfer(self):
        """测试库存调拨"""
        # 先入库
        self.manager.add_stock("P002", 30, "A01", "测试员")
        
        # 测试调拨
        result = self.manager.transfer_stock("P002", 15, "A01", "B01", "测试员")
        self.assertTrue(result)
        self.assertEqual(self.manager.get_stock_by_location("P002", "A01"), 15)
        self.assertEqual(self.manager.get_stock_by_location("P002", "B01"), 15)
        
        # 测试调拨数量超过源位置库存
        result = self.manager.transfer_stock("P002", 20, "A01", "B01", "测试员")
        self.assertFalse(result)
    
    def test_inventory_check(self):
        """测试库存盘点"""
        # 先入库
        self.manager.add_stock("P003", 25, "A01", "测试员")
        
        # 测试盘点（盘盈）
        result = self.manager.inventory_check("P003", "A01", 30, "测试员")
        self.assertTrue(result)
        self.assertEqual(self.manager.get_stock_by_location("P003", "A01"), 30)
        
        # 测试盘点（盘亏）
        result = self.manager.inventory_check("P003", "A01", 25, "测试员")
        self.assertTrue(result)
        self.assertEqual(self.manager.get_stock_by_location("P003", "A01"), 25)
    
    def test_low_stock_alerts(self):
        """测试低库存预警"""
        # 设置预警阈值
        self.manager.set_low_stock_threshold("P001", 10)
        
        # 入库数量低于阈值
        self.manager.add_stock("P001", 5, "A01", "测试员")
        
        # 检查预警
        low_stock = self.manager.get_low_stock_products()
        self.assertEqual(len(low_stock), 1)
        self.assertEqual(low_stock[0][0], "P001")  # product_id
        self.assertEqual(low_stock[0][1], 5)       # current_stock
        self.assertEqual(low_stock[0][2], 10)      # threshold
    
    def test_expired_products(self):
        """测试过期商品检查"""
        # 添加已过期的商品
        expiry_date = datetime.now() - timedelta(days=1)
        self.manager.add_stock("P002", 10, "A01", "测试员", expiry_date=expiry_date)
        
        expired_products = self.manager.get_expired_products()
        self.assertEqual(len(expired_products), 1)
        self.assertEqual(expired_products[0].product_id, "P002")
    
    def test_expiring_soon_products(self):
        """测试即将过期商品检查"""
        # 添加3天后过期的商品
        expiry_date = datetime.now() + timedelta(days=3)
        self.manager.add_stock("P003", 15, "A01", "测试员", expiry_date=expiry_date)
        
        expiring_soon = self.manager.get_expiring_soon_products(days=7)
        self.assertEqual(len(expiring_soon), 1)
        self.assertEqual(expiring_soon[0].product_id, "P003")
        
        # 测试不在范围内的商品
        expiring_soon = self.manager.get_expiring_soon_products(days=2)
        self.assertEqual(len(expiring_soon), 0)
    
    def test_warehouse_management(self):
        """测试仓库管理"""
        # 添加仓库
        result = self.manager.add_warehouse("WH001", "主仓库", "北京市朝阳区", "张三", 1000)
        self.assertTrue(result)
        self.assertIn("WH001", self.manager.warehouses)
        
        # 添加仓库位置
        result = self.manager.add_warehouse_location("WH001", "A区01号")
        self.assertTrue(result)
        
        warehouse = self.manager.warehouses["WH001"]
        self.assertIn("A区01号", warehouse.locations)
    
    def test_transaction_history(self):
        """测试交易记录"""
        # 执行一些操作
        self.manager.add_stock("P001", 20, "A01", "测试员")
        self.manager.remove_stock("P001", 5, "A01", "测试员")
        self.manager.add_stock("P002", 15, "B01", "测试员")
        
        # 获取所有交易记录
        all_transactions = self.manager.get_transaction_history()
        self.assertEqual(len(all_transactions), 3)
        
        # 按商品过滤
        p001_transactions = self.manager.get_transaction_history(product_id="P001")
        self.assertEqual(len(p001_transactions), 2)
        
        # 按交易类型过滤
        inbound_transactions = self.manager.get_transaction_history(transaction_type="入库")
        self.assertEqual(len(inbound_transactions), 2)
    
    def test_inventory_report(self):
        """测试库存报表"""
        # 添加一些数据
        self.manager.add_stock("P001", 20, "A01", "测试员")
        self.manager.add_stock("P002", 15, "B01", "测试员")
        self.manager.set_low_stock_threshold("P001", 5)
        self.manager.set_low_stock_threshold("P002", 20)  # 设置为低库存
        
        report = self.manager.get_inventory_report()
        
        self.assertEqual(report['total_products'], 3)
        self.assertEqual(report['low_stock_count'], 1)  # P002低库存
        self.assertIn('水果', report['products_by_category'])
        self.assertEqual(len(report['stock_summary']), 3)


class TestDataPersistence(unittest.TestCase):
    """测试数据持久化"""
    
    def setUp(self):
        """测试前准备"""
        self.temp_dir = tempfile.mkdtemp()
        self.persistence = DataPersistence(self.temp_dir)
        self.manager = WarehouseManager()
        
        # 添加测试数据
        self.manager.add_product("P001", "测试商品", "测试描述", "测试分类", 10.0)
        self.manager.add_stock("P001", 50, "A01", "测试员")
        self.manager.add_warehouse("WH001", "测试仓库", "测试地址", "测试管理员")
    
    def tearDown(self):
        """测试后清理"""
        shutil.rmtree(self.temp_dir)
    
    def test_save_and_load_data(self):
        """测试数据保存和加载"""
        # 保存数据
        result = self.persistence.save_warehouse_data(self.manager)
        self.assertTrue(result)
        
        # 验证文件是否创建
        self.assertTrue(os.path.exists(self.persistence.products_file))
        self.assertTrue(os.path.exists(self.persistence.stock_records_file))
        self.assertTrue(os.path.exists(self.persistence.warehouses_file))
        
        # 创建新的管理器并加载数据
        new_manager = WarehouseManager()
        result = self.persistence.load_warehouse_data(new_manager)
        self.assertTrue(result)
        
        # 验证数据是否正确加载
        self.assertIn("P001", new_manager.products)
        self.assertEqual(new_manager.products["P001"].name, "测试商品")
        self.assertEqual(new_manager.get_total_stock("P001"), 50)
        self.assertIn("WH001", new_manager.warehouses)
    
    def test_backup_and_restore(self):
        """测试数据备份和恢复"""
        # 先保存原始数据
        self.persistence.save_warehouse_data(self.manager)
        
        # 创建备份
        backup_name = "test_backup"
        result = self.persistence.backup_data(backup_name)
        self.assertTrue(result)
        
        # 修改数据
        self.manager.add_product("P002", "新商品", "新描述", "新分类", 20.0)
        self.persistence.save_warehouse_data(self.manager)
        
        # 从备份恢复
        result = self.persistence.restore_data(backup_name)
        self.assertTrue(result)
        
        # 重新加载数据
        restored_manager = WarehouseManager()
        self.persistence.load_warehouse_data(restored_manager)
        
        # 验证数据已恢复到备份状态
        self.assertIn("P001", restored_manager.products)
        self.assertNotIn("P002", restored_manager.products)
    
    def test_export_csv(self):
        """测试CSV导出"""
        # 保存一些数据
        self.persistence.save_warehouse_data(self.manager)
        
        # 导出CSV
        export_dir = os.path.join(self.temp_dir, "exports")
        result = self.persistence.export_to_csv(self.manager, export_dir)
        self.assertTrue(result)
        
        # 验证导出文件是否存在
        self.assertTrue(os.path.exists(export_dir))
        export_files = os.listdir(export_dir)
        
        # 应该有商品、库存、交易记录三个文件
        csv_files = [f for f in export_files if f.endswith('.csv')]
        self.assertGreaterEqual(len(csv_files), 3)
    
    def test_data_statistics(self):
        """测试数据统计"""
        # 保存数据
        self.persistence.save_warehouse_data(self.manager)
        
        # 获取统计信息
        stats = self.persistence.get_data_statistics()
        
        # 验证统计信息
        self.assertTrue(stats['files_exist']['products'])
        self.assertTrue(stats['files_exist']['stock_records'])
        self.assertTrue(stats['files_exist']['warehouses'])
        self.assertGreater(stats['file_sizes']['products'], 0)


class TestWarehouseModels(unittest.TestCase):
    """测试数据模型"""
    
    def test_product_model(self):
        """测试商品模型"""
        product = Product("P001", "苹果", "新鲜苹果", "水果", 5.0, "斤")
        
        # 测试基本属性
        self.assertEqual(product.product_id, "P001")
        self.assertEqual(product.name, "苹果")
        self.assertEqual(product.unit_price, 5.0)
        
        # 测试更新信息
        product.update_info(name="红苹果", unit_price=6.0)
        self.assertEqual(product.name, "红苹果")
        self.assertEqual(product.unit_price, 6.0)
        
        # 测试字典转换
        product_dict = product.to_dict()
        self.assertEqual(product_dict['product_id'], "P001")
        self.assertEqual(product_dict['name'], "红苹果")
        
        # 测试从字典创建
        new_product = Product.from_dict(product_dict)
        self.assertEqual(new_product.product_id, "P001")
        self.assertEqual(new_product.name, "红苹果")
    
    def test_stock_record_model(self):
        """测试库存记录模型"""
        expiry_date = datetime.now() + timedelta(days=30)
        record = StockRecord("P001", 50, "A01", "BATCH001", expiry_date)
        
        # 测试基本属性
        self.assertEqual(record.product_id, "P001")
        self.assertEqual(record.quantity, 50)
        self.assertEqual(record.location, "A01")
        self.assertFalse(record.is_expired())
        
        # 测试更新数量
        record.update_quantity(40)
        self.assertEqual(record.quantity, 40)
        
        # 测试过期检查
        expired_record = StockRecord("P002", 20, "B01", expiry_date=datetime.now() - timedelta(days=1))
        self.assertTrue(expired_record.is_expired())
    
    def test_transaction_record_model(self):
        """测试交易记录模型"""
        transaction = TransactionRecord("入库", "P001", 30, "A01", "测试员", "测试入库")
        
        # 测试基本属性
        self.assertEqual(transaction.transaction_type, "入库")
        self.assertEqual(transaction.product_id, "P001")
        self.assertEqual(transaction.quantity, 30)
        self.assertEqual(transaction.operator, "测试员")
        
        # 测试无效交易类型
        with self.assertRaises(ValueError):
            TransactionRecord("无效类型", "P001", 30, "A01", "测试员")
    
    def test_warehouse_model(self):
        """测试仓库模型"""
        warehouse = Warehouse("WH001", "主仓库", "北京市朝阳区", "张三", 1000)
        
        # 测试基本属性
        self.assertEqual(warehouse.warehouse_id, "WH001")
        self.assertEqual(warehouse.name, "主仓库")
        self.assertEqual(warehouse.manager, "张三")
        
        # 测试添加位置
        warehouse.add_location("A区01号")
        warehouse.add_location("A区02号")
        self.assertIn("A区01号", warehouse.locations)
        self.assertIn("A区02号", warehouse.locations)
        
        # 测试重复添加位置
        warehouse.add_location("A区01号")
        self.assertEqual(warehouse.locations.count("A区01号"), 1)
        
        # 测试移除位置
        warehouse.remove_location("A区01号")
        self.assertNotIn("A区01号", warehouse.locations)
    
    def test_stock_alert_model(self):
        """测试库存预警模型"""
        alert = StockAlert("低库存", "P001", 5, 10, "库存低于阈值")
        
        # 测试基本属性
        self.assertEqual(alert.alert_type, "低库存")
        self.assertEqual(alert.product_id, "P001")
        self.assertEqual(alert.current_quantity, 5)
        self.assertEqual(alert.threshold, 10)
        self.assertFalse(alert.is_resolved)
        
        # 测试解决预警
        alert.resolve()
        self.assertTrue(alert.is_resolved)
        
        # 测试无效预警类型
        with self.assertRaises(ValueError):
            StockAlert("无效类型", "P001", 5, 10, "测试")


def run_tests():
    """运行所有测试"""
    # 创建测试套件
    test_suite = unittest.TestSuite()
    
    # 添加测试类
    test_classes = [
        TestWarehouseManager,
        TestDataPersistence,
        TestWarehouseModels
    ]
    
    for test_class in test_classes:
        tests = unittest.TestLoader().loadTestsFromTestCase(test_class)
        test_suite.addTests(tests)
    
    # 运行测试
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    # 返回测试结果
    return result.wasSuccessful()


if __name__ == "__main__":
    print("🧪 运行仓库管理系统测试...")
    print("="*50)
    
    success = run_tests()
    
    print("\n" + "="*50)
    if success:
        print("✅ 所有测试通过！")
    else:
        print("❌ 部分测试失败！")
    
    print("="*50)