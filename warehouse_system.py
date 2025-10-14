#!/usr/bin/env python3
"""
仓库管理系统主程序
提供系统启动入口和基本的演示功能
"""

import sys
import os
from datetime import datetime, timedelta
from warehouse_manager import WarehouseManager
from warehouse_persistence import DataPersistence
from warehouse_cli import WarehouseCLI


def create_demo_data(manager: WarehouseManager):
    """创建演示数据"""
    print("📊 创建演示数据...")
    
    # 添加商品
    products = [
        ("P001", "苹果", "新鲜红苹果", "水果", 8.5, "斤"),
        ("P002", "香蕉", "进口香蕉", "水果", 6.0, "斤"),
        ("P003", "纯牛奶", "250ml纯牛奶", "饮品", 3.5, "瓶"),
        ("P004", "面包", "全麦面包", "食品", 12.0, "个"),
        ("P005", "矿泉水", "500ml矿泉水", "饮品", 2.0, "瓶"),
        ("P006", "橙子", "新鲜橙子", "水果", 7.0, "斤"),
        ("P007", "酸奶", "原味酸奶", "饮品", 4.5, "杯"),
        ("P008", "饼干", "消化饼干", "食品", 15.0, "盒")
    ]
    
    for product_data in products:
        manager.add_product(*product_data)
    
    # 添加仓库
    warehouses = [
        ("WH001", "主仓库", "北京市朝阳区工业园区1号", "张三", 5000),
        ("WH002", "分仓库", "北京市海淀区科技园2号", "李四", 2000)
    ]
    
    for warehouse_data in warehouses:
        manager.add_warehouse(*warehouse_data)
        # 为每个仓库添加存储位置
        warehouse_id = warehouse_data[0]
        for zone in ['A', 'B', 'C']:
            for i in range(1, 11):
                location = f"{zone}{i:02d}"
                manager.add_warehouse_location(warehouse_id, location)
    
    # 添加库存
    stock_data = [
        ("P001", 120, "A01", "系统管理员", None, None),
        ("P001", 80, "A02", "系统管理员", None, None),
        ("P002", 150, "A03", "系统管理员", None, None),
        ("P003", 200, "B01", "系统管理员", "BATCH001", datetime.now() + timedelta(days=15)),
        ("P003", 100, "B02", "系统管理员", "BATCH002", datetime.now() + timedelta(days=30)),
        ("P004", 50, "C01", "系统管理员", None, datetime.now() + timedelta(days=7)),
        ("P005", 300, "A04", "系统管理员", None, None),
        ("P006", 90, "A05", "系统管理员", None, None),
        ("P007", 80, "B03", "系统管理员", "BATCH003", datetime.now() + timedelta(days=5)),
        ("P008", 60, "C02", "系统管理员", None, datetime.now() + timedelta(days=45))
    ]
    
    for stock_info in stock_data:
        product_id, quantity, location, operator, batch_number, expiry_date = stock_info
        manager.add_stock(product_id, quantity, location, operator, batch_number, expiry_date)
    
    # 设置低库存预警阈值
    thresholds = {
        "P001": 50,   # 苹果
        "P002": 30,   # 香蕉
        "P003": 100,  # 牛奶
        "P004": 20,   # 面包
        "P005": 50,   # 矿泉水
        "P006": 40,   # 橙子
        "P007": 25,   # 酸奶
        "P008": 15    # 饼干
    }
    
    for product_id, threshold in thresholds.items():
        manager.set_low_stock_threshold(product_id, threshold)
    
    # 模拟一些交易记录
    transactions = [
        ("P001", 30, "A01", "张三", "销售出库"),
        ("P002", 20, "A03", "李四", "批发出库"),
        ("P003", 50, "B01", "王五", "零售出库"),
        ("P005", 100, "A04", "赵六", "大客户出库")
    ]
    
    for product_id, quantity, location, operator, notes in transactions:
        manager.remove_stock(product_id, quantity, location, operator, notes)
    
    print("✅ 演示数据创建完成！")
    return True


def show_system_info():
    """显示系统信息"""
    print("\n" + "="*60)
    print("🏭 仓库管理系统 v1.0")
    print("="*60)
    print("📋 功能特性:")
    print("  • 商品管理 - 添加、修改、删除、查询商品信息")
    print("  • 库存管理 - 入库、出库、调拨、盘点操作")
    print("  • 仓库管理 - 仓库和存储位置管理")
    print("  • 预警系统 - 低库存、过期商品自动预警")
    print("  • 数据持久化 - 自动保存和加载数据")
    print("  • 报表统计 - 库存报表和交易记录")
    print("  • 数据备份 - 支持数据备份和恢复")
    print("  • CSV导出 - 数据导出为Excel可读格式")
    print()
    print("📁 数据文件位置: ./warehouse_data/")
    print("🧪 测试文件: test_warehouse_system.py")
    print("="*60)


def main():
    """主程序入口"""
    show_system_info()
    
    print("\n🚀 启动选项:")
    print("1. 启动图形界面 (开发中...)")
    print("2. 启动命令行界面")
    print("3. 运行系统测试")
    print("4. 创建演示数据")
    print("5. 查看系统状态")
    print("0. 退出")
    
    while True:
        try:
            choice = input("\n请选择启动选项 (0-5): ").strip()
            
            if choice == '1':
                print("🚧 图形界面正在开发中，敬请期待...")
                
            elif choice == '2':
                print("\n🖥️  启动命令行界面...")
                cli = WarehouseCLI()
                cli.run()
                break
                
            elif choice == '3':
                print("\n🧪 运行系统测试...")
                # 导入并运行测试
                try:
                    from test_warehouse_system import run_tests
                    success = run_tests()
                    if success:
                        print("\n✅ 所有测试通过！系统运行正常。")
                    else:
                        print("\n❌ 部分测试失败！请检查系统状态。")
                except ImportError as e:
                    print(f"❌ 无法导入测试模块: {e}")
                except Exception as e:
                    print(f"❌ 运行测试时出错: {e}")
                
            elif choice == '4':
                print("\n📊 创建演示数据...")
                manager = WarehouseManager()
                persistence = DataPersistence()
                
                if create_demo_data(manager):
                    if persistence.save_warehouse_data(manager):
                        print("✅ 演示数据已保存到文件")
                    else:
                        print("⚠️  演示数据创建成功，但保存失败")
                else:
                    print("❌ 演示数据创建失败")
                
            elif choice == '5':
                print("\n📊 系统状态检查...")
                
                # 检查数据文件
                persistence = DataPersistence()
                stats = persistence.get_data_statistics()
                
                print("📁 数据文件状态:")
                for file_type, exists in stats['files_exist'].items():
                    status = "✅ 存在" if exists else "❌ 不存在"
                    size = stats['file_sizes'][file_type]
                    print(f"  {file_type}: {status} ({size} bytes)")
                
                # 尝试加载数据
                manager = WarehouseManager()
                if persistence.load_warehouse_data(manager):
                    print(f"\n📦 数据加载成功:")
                    print(f"  商品数量: {len(manager.products)}")
                    print(f"  仓库数量: {len(manager.warehouses)}")
                    print(f"  交易记录: {len(manager.transaction_history)}")
                    print(f"  活跃预警: {len(manager.get_active_alerts())}")
                    
                    # 计算总库存价值
                    total_value = 0
                    total_items = 0
                    for product_id, product in manager.products.items():
                        stock = manager.get_total_stock(product_id)
                        value = stock * product.unit_price
                        total_value += value
                        total_items += stock
                    
                    print(f"  库存总量: {total_items} 件")
                    print(f"  库存总值: ¥{total_value:.2f}")
                else:
                    print("❌ 数据加载失败")
                
            elif choice == '0':
                print("\n👋 感谢使用仓库管理系统，再见！")
                break
                
            else:
                print("❌ 无效选择，请输入 0-5 之间的数字")
                
        except KeyboardInterrupt:
            print("\n\n👋 用户中断操作，退出程序")
            break
        except Exception as e:
            print(f"❌ 程序运行出错: {e}")
            break
    
    return 0


if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except Exception as e:
        print(f"❌ 系统启动失败: {e}")
        sys.exit(1)