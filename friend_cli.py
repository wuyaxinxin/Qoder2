"""
朋友管理系统命令行界面
提供用户友好的交互式命令行界面
"""

from friend_manager import FriendManager


class FriendCLI:
    """朋友管理系统命令行界面类"""
    
    def __init__(self):
        """初始化CLI界面"""
        self.manager = FriendManager()  # 创建朋友管理器实例
        self.running = True  # 程序运行状态标志
    
    def display_menu(self):
        """显示主菜单"""
        print("\n" + "="*50)
        print("           朋友管理系统")
        print("="*50)
        print("1. 添加朋友")
        print("2. 删除朋友")
        print("3. 更新朋友信息")
        print("4. 查看朋友信息")
        print("5. 搜索朋友")
        print("6. 查看所有朋友")
        print("7. 本月生日提醒")
        print("8. 统计信息")
        print("9. 导出数据")
        print("0. 退出系统")
        print("="*50)
    
    def add_friend_ui(self):
        """添加朋友的用户界面"""
        print("\n--- 添加新朋友 ---")
        
        # 获取朋友ID
        friend_id = input("请输入朋友ID: ").strip()
        if not friend_id:
            print("错误: 朋友ID不能为空!")
            return
        
        # 获取姓名
        name = input("请输入姓名: ").strip()
        if not name:
            print("错误: 姓名不能为空!")
            return
        
        # 获取电话
        phone = input("请输入电话: ").strip()
        if not phone:
            print("错误: 电话不能为空!")
            return
        
        # 获取可选信息
        birthday = input("请输入生日(YYYY-MM-DD,可选): ").strip() or None
        address = input("请输入地址(可选): ").strip() or None
        notes = input("请输入备注(可选): ").strip() or None
        
        # 调用管理器添加朋友
        self.manager.add_friend(friend_id, name, phone, birthday, address, notes)
    
    def delete_friend_ui(self):
        """删除朋友的用户界面"""
        print("\n--- 删除朋友 ---")
        
        # 获取要删除的朋友ID
        friend_id = input("请输入要删除的朋友ID: ").strip()
        if not friend_id:
            print("错误: 朋友ID不能为空!")
            return
        
        # 确认删除
        confirm = input(f"确定要删除朋友 {friend_id} 吗? (y/n): ").strip().lower()
        if confirm == 'y':
            self.manager.delete_friend(friend_id)
        else:
            print("已取消删除操作")
    
    def update_friend_ui(self):
        """更新朋友信息的用户界面"""
        print("\n--- 更新朋友信息 ---")
        
        # 获取要更新的朋友ID
        friend_id = input("请输入要更新的朋友ID: ").strip()
        if not friend_id:
            print("错误: 朋友ID不能为空!")
            return
        
        # 检查朋友是否存在
        friend = self.manager.get_friend(friend_id)
        if not friend:
            print(f"错误: 找不到ID为 {friend_id} 的朋友!")
            return
        
        # 显示当前信息
        print(f"\n当前信息:")
        print(friend)
        
        # 获取新信息(留空表示不修改)
        print("\n请输入新信息(留空表示不修改):")
        update_data = {}
        
        name = input(f"姓名 [{friend.name}]: ").strip()
        if name:
            update_data['name'] = name
        
        phone = input(f"电话 [{friend.phone}]: ").strip()
        if phone:
            update_data['phone'] = phone
        
        birthday = input(f"生日 [{friend.birthday or '未设置'}]: ").strip()
        if birthday:
            update_data['birthday'] = birthday
        
        address = input(f"地址 [{friend.address or '未设置'}]: ").strip()
        if address:
            update_data['address'] = address
        
        notes = input(f"备注 [{friend.notes or '无'}]: ").strip()
        if notes:
            update_data['notes'] = notes
        
        # 如果有更新内容,执行更新
        if update_data:
            self.manager.update_friend(friend_id, **update_data)
        else:
            print("没有进行任何修改")
    
    def view_friend_ui(self):
        """查看朋友详细信息的用户界面"""
        print("\n--- 查看朋友信息 ---")
        
        # 获取朋友ID
        friend_id = input("请输入朋友ID: ").strip()
        if not friend_id:
            print("错误: 朋友ID不能为空!")
            return
        
        # 获取朋友对象
        friend = self.manager.get_friend(friend_id)
        if friend:
            print("\n" + "="*50)
            print(friend)
            print("="*50)
        else:
            print(f"错误: 找不到ID为 {friend_id} 的朋友!")
    
    def search_friends_ui(self):
        """搜索朋友的用户界面"""
        print("\n--- 搜索朋友 ---")
        
        # 获取搜索关键词
        keyword = input("请输入搜索关键词(姓名或备注): ").strip()
        if not keyword:
            print("错误: 搜索关键词不能为空!")
            return
        
        # 执行搜索
        results = self.manager.search_friends(keyword)
        
        # 显示搜索结果
        if results:
            print(f"\n找到 {len(results)} 位朋友:")
            print("-" * 50)
            for friend in results:
                print(f"ID: {friend.friend_id} | 姓名: {friend.name} | 电话: {friend.phone}")
                if friend.notes:
                    print(f"  备注: {friend.notes}")
                print("-" * 50)
        else:
            print("没有找到匹配的朋友")
    
    def list_all_friends_ui(self):
        """显示所有朋友的用户界面"""
        print("\n--- 所有朋友列表 ---")
        
        # 获取所有朋友
        friends = self.manager.list_all_friends()
        
        # 显示朋友列表
        if friends:
            print(f"\n共有 {len(friends)} 位朋友:")
            print("-" * 80)
            print(f"{'ID':<10} {'姓名':<10} {'电话':<15} {'生日':<12} {'备注':<20}")
            print("-" * 80)
            for friend in friends:
                # 格式化显示每位朋友的基本信息
                print(f"{friend.friend_id:<10} {friend.name:<10} {friend.phone:<15} "
                      f"{friend.birthday or '未设置':<12} {(friend.notes or '无')[:18]:<20}")
            print("-" * 80)
        else:
            print("暂无朋友数据")
    
    def birthday_reminder_ui(self):
        """本月生日提醒的用户界面"""
        print("\n--- 本月生日提醒 ---")
        
        # 获取本月生日的朋友
        birthday_friends = self.manager.get_birthday_friends()
        
        # 显示生日提醒
        if birthday_friends:
            print(f"\n本月有 {len(birthday_friends)} 位朋友过生日:")
            print("-" * 60)
            for friend in birthday_friends:
                age = friend.get_age()  # 获取年龄
                age_info = f"({age}岁)" if age else ""
                print(f"  {friend.name} {age_info}")
                print(f"  生日: {friend.birthday}")
                print(f"  电话: {friend.phone}")
                print("-" * 60)
        else:
            print("本月没有朋友过生日")
    
    def statistics_ui(self):
        """显示统计信息的用户界面"""
        print("\n--- 统计信息 ---")
        
        # 获取统计数据
        stats = self.manager.get_statistics()
        
        # 显示统计信息
        print("\n" + "="*50)
        print(f"总朋友数:       {stats['total_friends']}")
        print(f"有生日信息:     {stats['with_birthday']}")
        print(f"有地址信息:     {stats['with_address']}")
        print(f"本月生日:       {stats['birthday_this_month']}")
        print("="*50)
    
    def export_data_ui(self):
        """导出数据的用户界面"""
        print("\n--- 导出数据 ---")
        
        # 询问导出文件名
        export_file = input("请输入导出文件名(留空使用默认名称): ").strip()
        export_file = export_file if export_file else None
        
        # 执行导出
        result_file = self.manager.export_data(export_file)
        print(f"\n数据已成功导出到: {result_file}")
    
    def run(self):
        """运行CLI主循环"""
        print("\n欢迎使用朋友管理系统!")
        
        # 主循环
        while self.running:
            # 显示菜单
            self.display_menu()
            
            # 获取用户选择
            choice = input("\n请选择操作 (0-9): ").strip()
            
            # 处理用户选择
            try:
                if choice == '1':
                    self.add_friend_ui()
                elif choice == '2':
                    self.delete_friend_ui()
                elif choice == '3':
                    self.update_friend_ui()
                elif choice == '4':
                    self.view_friend_ui()
                elif choice == '5':
                    self.search_friends_ui()
                elif choice == '6':
                    self.list_all_friends_ui()
                elif choice == '7':
                    self.birthday_reminder_ui()
                elif choice == '8':
                    self.statistics_ui()
                elif choice == '9':
                    self.export_data_ui()
                elif choice == '0':
                    # 退出系统
                    print("\n感谢使用朋友管理系统,再见!")
                    self.running = False
                else:
                    print("\n无效的选择,请重新输入!")
            except Exception as e:
                # 捕获异常,避免程序崩溃
                print(f"\n发生错误: {e}")
                print("请重试...")
            
            # 等待用户按回车继续
            if self.running and choice != '0':
                input("\n按回车键继续...")


# 主程序入口
if __name__ == "__main__":
    # 创建并运行CLI
    cli = FriendCLI()
    cli.run()
