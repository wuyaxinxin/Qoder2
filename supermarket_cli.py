"""
始终生效
超市管理系统 - 命令行界面
提供交互式命令行操作界面
"""

from supermarket_system import SupermarketSystem
from supermarket_data_manager import SupermarketDataManager


class SupermarketCLI:
    """超市管理系统命令行界面"""
    
    def __init__(self):
        """初始化CLI"""
        self.system = SupermarketSystem()
        self.data_manager = SupermarketDataManager()
        self.running = False
        
        # 加载数据
        if self.data_manager.load_data(self.system):
            print("已加载历史数据")
    
    def display_menu(self):
        """显示主菜单"""
        print("\n" + "="*50)
        print("          超市管理系统")
        print("="*50)
        print("1. 商品管理")
        print("2. 库存管理")
        print("3. 销售管理")
        print("4. 统计报表")
        print("5. 数据管理")
        print("0. 退出系统")
        print("="*50)
    
    def product_menu(self):
        """商品管理菜单"""
        while True:
            print("\n【商品管理】")
            print("1. 添加商品")
            print("2. 删除商品")
            print("3. 修改商品")
            print("4. 查看所有商品")
            print("5. 搜索商品")
            print("6. 查看商品详情")
            print("0. 返回主菜单")
            
            choice = input("\n请选择操作: ").strip()
            
            if choice == '1':
                self.add_product()
            elif choice == '2':
                self.delete_product()
            elif choice == '3':
                self.update_product()
            elif choice == '4':
                self.list_all_products()
            elif choice == '5':
                self.search_products()
            elif choice == '6':
                self.view_product_detail()
            elif choice == '0':
                break
            else:
                print("无效选择，请重新输入")
    
    def add_product(self):
        """添加商品"""
        print("\n--- 添加商品 ---")
        try:
            name = input("商品名称: ").strip()
            category = input("商品类别: ").strip()
            price = float(input("商品价格: ").strip())
            stock = int(input("初始库存: ").strip())
            supplier = input("供应商（可选）: ").strip()
            description = input("商品描述（可选）: ").strip()
            
            product = self.system.add_product(name, category, price, stock, supplier, description)
            if product:
                print(f"✓ 商品添加成功！商品编号: {product.product_id}")
                self.auto_save()
            else:
                print("✗ 商品添加失败，请检查输入数据")
        except ValueError:
            print("✗ 输入格式错误")
    
    def delete_product(self):
        """删除商品"""
        print("\n--- 删除商品 ---")
        product_id = input("请输入商品编号: ").strip()
        
        product = self.system.get_product(product_id)
        if not product:
            print("✗ 商品不存在")
            return
        
        print(f"确认删除商品: {product.name} ({product_id})？")
        confirm = input("确认删除(y/n): ").strip().lower()
        
        if confirm == 'y':
            if self.system.delete_product(product_id):
                print("✓ 商品删除成功")
                self.auto_save()
            else:
                print("✗ 商品删除失败")
    
    def update_product(self):
        """修改商品"""
        print("\n--- 修改商品 ---")
        product_id = input("请输入商品编号: ").strip()
        
        product = self.system.get_product(product_id)
        if not product:
            print("✗ 商品不存在")
            return
        
        print(f"\n当前商品信息:\n{product}")
        print("\n请输入要修改的字段（直接回车跳过）:")
        
        try:
            updates = {}
            
            name = input(f"商品名称 [{product.name}]: ").strip()
            if name:
                updates['name'] = name
            
            category = input(f"商品类别 [{product.category}]: ").strip()
            if category:
                updates['category'] = category
            
            price = input(f"商品价格 [{product.price}]: ").strip()
            if price:
                updates['price'] = float(price)
            
            supplier = input(f"供应商 [{product.supplier}]: ").strip()
            if supplier:
                updates['supplier'] = supplier
            
            description = input(f"商品描述 [{product.description}]: ").strip()
            if description:
                updates['description'] = description
            
            min_stock = input(f"最小库存预警值 [{product.min_stock}]: ").strip()
            if min_stock:
                updates['min_stock'] = int(min_stock)
            
            if updates:
                if self.system.update_product(product_id, **updates):
                    print("✓ 商品信息更新成功")
                    self.auto_save()
                else:
                    print("✗ 商品信息更新失败")
            else:
                print("未做任何修改")
        except ValueError:
            print("✗ 输入格式错误")
    
    def list_all_products(self):
        """查看所有商品"""
        print("\n--- 所有商品列表 ---")
        products = self.system.get_all_products()
        
        if not products:
            print("暂无商品")
            return
        
        print(f"\n共 {len(products)} 个商品:\n")
        for i, product in enumerate(products, 1):
            print(f"{i}. {product}")
    
    def search_products(self):
        """搜索商品"""
        print("\n--- 搜索商品 ---")
        print("1. 按名称搜索")
        print("2. 按类别搜索")
        print("3. 组合搜索")
        
        choice = input("请选择搜索方式: ").strip()
        
        keyword = ""
        category = ""
        
        if choice == '1':
            keyword = input("请输入商品名称关键词: ").strip()
        elif choice == '2':
            # 显示所有类别
            categories = self.system.get_all_categories()
            if categories:
                print("\n可用类别:", ", ".join(categories))
            category = input("请输入商品类别: ").strip()
        elif choice == '3':
            keyword = input("请输入商品名称关键词: ").strip()
            category = input("请输入商品类别: ").strip()
        else:
            print("无效选择")
            return
        
        results = self.system.search_products(keyword, category)
        
        if results:
            print(f"\n找到 {len(results)} 个商品:")
            for i, product in enumerate(results, 1):
                print(f"{i}. {product}")
        else:
            print("未找到符合条件的商品")
    
    def view_product_detail(self):
        """查看商品详情"""
        print("\n--- 商品详情 ---")
        product_id = input("请输入商品编号: ").strip()
        
        detail = self.system.get_product_sales_detail(product_id)
        if not detail:
            print("✗ 商品不存在")
            return
        
        product = detail['product']
        print(f"\n{product}")
        print(f"供应商: {product.supplier}")
        print(f"描述: {product.description}")
        print(f"库存价值: ¥{product.get_total_value():.2f}")
        print(f"累计销量: {detail['sales_count']}")
        print(f"累计销售额: ¥{detail['total_revenue']:.2f}")
        print(f"最小库存预警: {product.min_stock}")
    
    def stock_menu(self):
        """库存管理菜单"""
        while True:
            print("\n【库存管理】")
            print("1. 商品入库")
            print("2. 商品出库")
            print("3. 库存统计")
            print("4. 库存预警")
            print("0. 返回主菜单")
            
            choice = input("\n请选择操作: ").strip()
            
            if choice == '1':
                self.stock_in()
            elif choice == '2':
                self.stock_out()
            elif choice == '3':
                self.stock_statistics()
            elif choice == '4':
                self.stock_warning()
            elif choice == '0':
                break
            else:
                print("无效选择，请重新输入")
    
    def stock_in(self):
        """商品入库"""
        print("\n--- 商品入库 ---")
        product_id = input("请输入商品编号: ").strip()
        
        product = self.system.get_product(product_id)
        if not product:
            print("✗ 商品不存在")
            return
        
        print(f"商品: {product.name}, 当前库存: {product.stock}")
        
        try:
            quantity = int(input("入库数量: ").strip())
            if self.system.stock_in(product_id, quantity):
                print(f"✓ 入库成功！当前库存: {product.stock}")
                self.auto_save()
            else:
                print("✗ 入库失败")
        except ValueError:
            print("✗ 输入格式错误")
    
    def stock_out(self):
        """商品出库"""
        print("\n--- 商品出库 ---")
        product_id = input("请输入商品编号: ").strip()
        
        product = self.system.get_product(product_id)
        if not product:
            print("✗ 商品不存在")
            return
        
        print(f"商品: {product.name}, 当前库存: {product.stock}")
        
        try:
            quantity = int(input("出库数量: ").strip())
            if self.system.stock_out(product_id, quantity):
                print(f"✓ 出库成功！当前库存: {product.stock}")
                self.auto_save()
            else:
                print("✗ 出库失败，库存不足")
        except ValueError:
            print("✗ 输入格式错误")
    
    def stock_statistics(self):
        """库存统计"""
        print("\n--- 库存统计 ---")
        stats = self.system.get_stock_statistics()
        
        print(f"\n商品种类总数: {stats['total_products']}")
        print(f"库存总量: {stats['total_stock']}")
        print(f"库存总价值: ¥{stats['total_value']:.2f}")
        print(f"库存预警商品数: {stats['low_stock_count']}")
    
    def stock_warning(self):
        """库存预警"""
        print("\n--- 库存预警 ---")
        low_stock_products = self.system.get_low_stock_products()
        
        if not low_stock_products:
            print("✓ 所有商品库存充足")
            return
        
        print(f"\n共 {len(low_stock_products)} 个商品库存不足:")
        for i, product in enumerate(low_stock_products, 1):
            print(f"{i}. {product.name} ({product.product_id}) - "
                  f"当前库存: {product.stock}, 预警值: {product.min_stock}")
    
    def sales_menu(self):
        """销售管理菜单"""
        while True:
            print("\n【销售管理】")
            print("1. 销售商品")
            print("2. 退货处理")
            print("3. 查看销售记录")
            print("4. 销售统计")
            print("0. 返回主菜单")
            
            choice = input("\n请选择操作: ").strip()
            
            if choice == '1':
                self.sell_product()
            elif choice == '2':
                self.refund_product()
            elif choice == '3':
                self.view_sales_records()
            elif choice == '4':
                self.sales_statistics()
            elif choice == '0':
                break
            else:
                print("无效选择，请重新输入")
    
    def sell_product(self):
        """销售商品"""
        print("\n--- 销售商品 ---")
        product_id = input("请输入商品编号: ").strip()
        
        product = self.system.get_product(product_id)
        if not product:
            print("✗ 商品不存在")
            return
        
        print(f"商品: {product.name}, 价格: ¥{product.price:.2f}, 库存: {product.stock}")
        
        try:
            quantity = int(input("销售数量: ").strip())
            record = self.system.sell_product(product_id, quantity)
            
            if record:
                print(f"\n✓ 销售成功！")
                print(f"销售记录: {record.record_id}")
                print(f"总价: ¥{record.total_price:.2f}")
                print(f"剩余库存: {product.stock}")
                self.auto_save()
            else:
                print("✗ 销售失败，库存不足")
        except ValueError:
            print("✗ 输入格式错误")
    
    def refund_product(self):
        """退货处理"""
        print("\n--- 退货处理 ---")
        record_id = input("请输入销售记录编号: ").strip()
        
        if self.system.refund_product(record_id):
            print("✓ 退货处理成功")
            self.auto_save()
        else:
            print("✗ 退货处理失败，销售记录不存在")
    
    def view_sales_records(self):
        """查看销售记录"""
        print("\n--- 销售记录 ---")
        print("1. 查看所有记录")
        print("2. 按日期范围查询")
        
        choice = input("请选择: ").strip()
        
        start_date = ""
        end_date = ""
        
        if choice == '2':
            start_date = input("开始日期 (YYYY-MM-DD): ").strip()
            end_date = input("结束日期 (YYYY-MM-DD): ").strip()
        
        records = self.system.get_sales_records(start_date, end_date)
        
        if not records:
            print("暂无销售记录")
            return
        
        print(f"\n共 {len(records)} 条销售记录:")
        for i, record in enumerate(records, 1):
            print(f"{i}. {record}")
    
    def sales_statistics(self):
        """销售统计"""
        print("\n--- 销售统计 ---")
        print("1. 总体统计")
        print("2. 按日期范围统计")
        print("3. 热门商品排行")
        
        choice = input("请选择: ").strip()
        
        if choice == '1' or choice == '2':
            start_date = ""
            end_date = ""
            
            if choice == '2':
                start_date = input("开始日期 (YYYY-MM-DD): ").strip()
                end_date = input("结束日期 (YYYY-MM-DD): ").strip()
            
            stats = self.system.get_sales_statistics(start_date, end_date)
            
            print(f"\n销售记录数: {stats['total_sales']}")
            print(f"销售总额: ¥{stats['total_revenue']:.2f}")
            print(f"销售总量: {stats['total_quantity']}")
        
        elif choice == '3':
            try:
                limit = int(input("显示前几名 (默认10): ").strip() or "10")
                products = self.system.get_top_selling_products(limit)
                
                if products:
                    print(f"\n热门商品 TOP {min(limit, len(products))}:")
                    for i, product in enumerate(products, 1):
                        print(f"{i}. {product.name} - 销量: {product.sales_count}")
                else:
                    print("暂无销售数据")
            except ValueError:
                print("✗ 输入格式错误")
    
    def report_menu(self):
        """统计报表菜单"""
        while True:
            print("\n【统计报表】")
            print("1. 库存报表")
            print("2. 销售报表")
            print("3. 商品销售明细")
            print("0. 返回主菜单")
            
            choice = input("\n请选择操作: ").strip()
            
            if choice == '1':
                self.stock_statistics()
            elif choice == '2':
                self.sales_statistics()
            elif choice == '3':
                self.view_product_detail()
            elif choice == '0':
                break
            else:
                print("无效选择，请重新输入")
    
    def data_menu(self):
        """数据管理菜单"""
        while True:
            print("\n【数据管理】")
            print("1. 保存数据")
            print("2. 备份数据")
            print("3. 导出CSV")
            print("4. 导入CSV")
            print("0. 返回主菜单")
            
            choice = input("\n请选择操作: ").strip()
            
            if choice == '1':
                self.save_data()
            elif choice == '2':
                self.backup_data()
            elif choice == '3':
                self.export_csv()
            elif choice == '4':
                self.import_csv()
            elif choice == '0':
                break
            else:
                print("无效选择，请重新输入")
    
    def save_data(self):
        """保存数据"""
        print("\n保存数据中...")
        if self.data_manager.save_data(self.system):
            print("✓ 数据保存成功")
        else:
            print("✗ 数据保存失败")
    
    def backup_data(self):
        """备份数据"""
        print("\n备份数据中...")
        backup_file = self.data_manager.backup_data()
        if backup_file:
            print(f"✓ 数据备份成功: {backup_file}")
        else:
            print("✗ 数据备份失败")
    
    def export_csv(self):
        """导出CSV"""
        csv_file = input("CSV文件名 (默认: supermarket_products.csv): ").strip()
        if not csv_file:
            csv_file = "supermarket_products.csv"
        
        print(f"\n导出到 {csv_file} 中...")
        if self.data_manager.export_to_csv(self.system, csv_file):
            print("✓ 导出成功")
        else:
            print("✗ 导出失败")
    
    def import_csv(self):
        """导入CSV"""
        csv_file = input("CSV文件名: ").strip()
        
        print(f"\n从 {csv_file} 导入中...")
        count = self.data_manager.import_from_csv(self.system, csv_file)
        
        if count >= 0:
            print(f"✓ 成功导入 {count} 个商品")
            self.auto_save()
        else:
            print("✗ 导入失败")
    
    def auto_save(self):
        """自动保存"""
        self.data_manager.save_data(self.system)
    
    def run(self):
        """运行CLI"""
        self.running = True
        print("\n欢迎使用超市管理系统！")
        
        while self.running:
            self.display_menu()
            choice = input("\n请选择操作: ").strip()
            
            if choice == '1':
                self.product_menu()
            elif choice == '2':
                self.stock_menu()
            elif choice == '3':
                self.sales_menu()
            elif choice == '4':
                self.report_menu()
            elif choice == '5':
                self.data_menu()
            elif choice == '0':
                print("\n保存数据中...")
                self.save_data()
                print("感谢使用，再见！")
                self.running = False
            else:
                print("无效选择，请重新输入")


if __name__ == "__main__":
    cli = SupermarketCLI()
    cli.run()
