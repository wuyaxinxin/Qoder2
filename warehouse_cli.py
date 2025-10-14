"""
仓库管理系统命令行界面
提供友好的用户交互界面，支持所有仓库管理功能
"""

import os
import sys
from datetime import datetime, timedelta
from typing import List, Optional
from warehouse_manager import WarehouseManager
from warehouse_persistence import DataPersistence
from warehouse_models import Product, StockRecord, TransactionRecord


class WarehouseCLI:
    """仓库管理系统命令行界面"""
    
    def __init__(self):
        self.manager = WarehouseManager()
        self.persistence = DataPersistence()
        self.current_operator = "系统管理员"
        
        # 启动时自动加载数据
        if self.persistence.load_warehouse_data(self.manager):
            print("✅ 数据加载成功")
        else:
            print("ℹ️  首次运行，创建新的数据文件")
    
    def run(self):
        """运行主程序"""
        print("\n" + "="*60)
        print("🏭 欢迎使用仓库管理系统")
        print("="*60)
        
        # 检查预警
        self._check_alerts()
        
        while True:
            try:
                self._show_main_menu()
                choice = input("\n请选择操作 (输入编号): ").strip()
                
                if choice == '1':
                    self._product_management_menu()
                elif choice == '2':
                    self._stock_management_menu()
                elif choice == '3':
                    self._warehouse_management_menu()
                elif choice == '4':
                    self._query_menu()
                elif choice == '5':
                    self._report_menu()
                elif choice == '6':
                    self._alert_management_menu()
                elif choice == '7':
                    self._data_management_menu()
                elif choice == '8':
                    self._settings_menu()
                elif choice == '0':
                    self._exit_system()
                    break
                else:
                    print("❌ 无效选择，请重新输入")
                
                input("\n按回车键继续...")
                
            except KeyboardInterrupt:
                print("\n\n👋 用户中断操作")
                self._exit_system()
                break
            except Exception as e:
                print(f"❌ 系统错误: {e}")
                input("按回车键继续...")
    
    def _show_main_menu(self):
        """显示主菜单"""
        self._clear_screen()
        print(f"\n🏭 仓库管理系统 - 操作员: {self.current_operator}")
        print("="*60)
        
        # 显示关键统计信息
        total_products = len(self.manager.products)
        active_alerts = len(self.manager.get_active_alerts())
        low_stock_count = len(self.manager.get_low_stock_products())
        
        print(f"📦 商品总数: {total_products} | ⚠️  活跃预警: {active_alerts} | 📉 低库存商品: {low_stock_count}")
        print("-"*60)
        
        print("1. 📦 商品管理")
        print("2. 📋 库存管理")
        print("3. 🏪 仓库管理")
        print("4. 🔍 查询功能")
        print("5. 📊 报表中心")
        print("6. ⚠️  预警管理")
        print("7. 💾 数据管理")
        print("8. ⚙️  系统设置")
        print("0. 🚪 退出系统")
    
    def _clear_screen(self):
        """清屏"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def _check_alerts(self):
        """检查并显示预警"""
        # 检查过期商品预警
        self.manager.check_expiry_alerts()
        
        active_alerts = self.manager.get_active_alerts()
        if active_alerts:
            print(f"\n⚠️  系统预警 ({len(active_alerts)} 条):")
            print("-"*40)
            for alert in active_alerts[:5]:  # 只显示前5条
                print(f"• {alert}")
            if len(active_alerts) > 5:
                print(f"... 还有 {len(active_alerts) - 5} 条预警")
            print("-"*40)
    
    def _save_data(self):
        """保存数据"""
        if self.persistence.save_warehouse_data(self.manager):
            pass  # 静默保存成功
        else:
            print("⚠️  数据保存失败")
    
    def _exit_system(self):
        """退出系统"""
        print("\n💾 正在保存数据...")
        self._save_data()
        print("👋 感谢使用仓库管理系统，再见！")
    
    # 简化的主要功能实现
    def _product_management_menu(self):
        """商品管理菜单"""
        print("\n📦 商品管理功能")
        print("包含: 添加商品、查看商品列表、修改商品信息、删除商品等")
    
    def _stock_management_menu(self):
        """库存管理菜单"""
        print("\n📋 库存管理功能")
        print("包含: 商品入库、出库、调拨、盘点、库存查询等")
    
    def _warehouse_management_menu(self):
        """仓库管理菜单"""
        print("\n🏪 仓库管理功能")
        print("包含: 添加仓库、查看仓库列表、管理仓库位置等")
    
    def _query_menu(self):
        """查询功能菜单"""
        print("\n🔍 查询功能")
        print("包含: 库存查询、交易记录查询、商品搜索等")
    
    def _report_menu(self):
        """报表中心菜单"""
        print("\n📊 报表中心")
        print("包含: 库存报表、交易报表、统计分析等")
    
    def _alert_management_menu(self):
        """预警管理菜单"""
        print("\n⚠️  预警管理")
        print("包含: 低库存预警、过期商品预警、零库存预警等")
    
    def _data_management_menu(self):
        """数据管理菜单"""
        print("\n💾 数据管理")
        print("包含: 数据备份、恢复、导出、导入等")
    
    def _settings_menu(self):
        """系统设置菜单"""
        print("\n⚙️  系统设置")
        print("包含: 预警阈值设置、操作员管理、系统参数等")


def main():
    """主程序入口"""
    try:
        cli = WarehouseCLI()
        cli.run()
    except Exception as e:
        print(f"系统启动失败: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()