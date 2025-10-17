"""
朋友管理系统核心模块
提供朋友信息的增删改查和数据管理功能
"""

import json
import os
from datetime import datetime
from friend import Friend


class FriendManager:
    """朋友管理系统类,负责管理所有朋友信息"""
    
    def __init__(self, data_file="friends_data.json"):
        """
        初始化朋友管理系统
        
        参数:
            data_file: 数据文件路径,默认为friends_data.json
        """
        self.data_file = data_file  # 数据文件路径
        self.friends = {}  # 朋友字典,key为friend_id,value为Friend对象
        self.load_data()  # 加载数据
    
    def add_friend(self, friend_id, name, phone, birthday=None, address=None, notes=None):
        """
        添加新朋友
        
        参数:
            friend_id: 朋友ID
            name: 姓名
            phone: 电话
            birthday: 生日(可选)
            address: 地址(可选)
            notes: 备注(可选)
            
        返回:
            成功返回True,失败返回False
        """
        # 检查ID是否已存在
        if friend_id in self.friends:
            print(f"错误: 朋友ID {friend_id} 已存在!")
            return False
        
        # 创建新朋友对象
        new_friend = Friend(friend_id, name, phone, birthday, address, notes)
        # 添加到朋友字典
        self.friends[friend_id] = new_friend
        # 保存数据
        self.save_data()
        print(f"成功添加朋友: {name} (ID: {friend_id})")
        return True
    
    def delete_friend(self, friend_id):
        """
        删除朋友
        
        参数:
            friend_id: 要删除的朋友ID
            
        返回:
            成功返回True,失败返回False
        """
        # 检查朋友是否存在
        if friend_id not in self.friends:
            print(f"错误: 找不到ID为 {friend_id} 的朋友!")
            return False
        
        # 获取朋友姓名用于提示
        friend_name = self.friends[friend_id].name
        # 从字典中删除
        del self.friends[friend_id]
        # 保存数据
        self.save_data()
        print(f"成功删除朋友: {friend_name} (ID: {friend_id})")
        return True
    
    def update_friend(self, friend_id, **kwargs):
        """
        更新朋友信息
        
        参数:
            friend_id: 朋友ID
            **kwargs: 要更新的字段(name, phone, birthday, address, notes)
            
        返回:
            成功返回True,失败返回False
        """
        # 检查朋友是否存在
        if friend_id not in self.friends:
            print(f"错误: 找不到ID为 {friend_id} 的朋友!")
            return False
        
        # 更新朋友信息
        self.friends[friend_id].update_info(**kwargs)
        # 保存数据
        self.save_data()
        print(f"成功更新朋友信息 (ID: {friend_id})")
        return True
    
    def get_friend(self, friend_id):
        """
        获取指定ID的朋友
        
        参数:
            friend_id: 朋友ID
            
        返回:
            Friend对象,如果不存在则返回None
        """
        return self.friends.get(friend_id)
    
    def search_friends(self, keyword):
        """
        搜索朋友(按姓名或备注)
        
        参数:
            keyword: 搜索关键词
            
        返回:
            匹配的朋友列表
        """
        results = []
        # 遍历所有朋友
        for friend in self.friends.values():
            # 检查姓名或备注中是否包含关键词
            if (keyword.lower() in friend.name.lower() or 
                (friend.notes and keyword.lower() in friend.notes.lower())):
                results.append(friend)
        return results
    
    def list_all_friends(self):
        """
        获取所有朋友列表
        
        返回:
            所有朋友的列表
        """
        return list(self.friends.values())
    
    def get_birthday_friends(self, month=None):
        """
        获取指定月份生日的朋友
        
        参数:
            month: 月份(1-12),如果为None则返回本月生日的朋友
            
        返回:
            生日在指定月份的朋友列表
        """
        # 如果没有指定月份,使用当前月份
        if month is None:
            month = datetime.now().month
        
        birthday_friends = []
        # 遍历所有朋友
        for friend in self.friends.values():
            # 检查是否有生日信息
            if friend.birthday:
                try:
                    # 解析生日日期
                    birth_date = datetime.strptime(friend.birthday, "%Y-%m-%d")
                    # 检查月份是否匹配
                    if birth_date.month == month:
                        birthday_friends.append(friend)
                except ValueError:
                    continue  # 日期格式错误,跳过
        
        return birthday_friends
    
    def get_statistics(self):
        """
        获取统计信息
        
        返回:
            包含统计信息的字典
        """
        total_count = len(self.friends)  # 总朋友数
        with_birthday = sum(1 for f in self.friends.values() if f.birthday)  # 有生日信息的朋友数
        with_address = sum(1 for f in self.friends.values() if f.address)  # 有地址信息的朋友数
        
        # 返回统计字典
        return {
            'total_friends': total_count,
            'with_birthday': with_birthday,
            'with_address': with_address,
            'birthday_this_month': len(self.get_birthday_friends())
        }
    
    def save_data(self):
        """
        保存数据到文件
        
        返回:
            成功返回True,失败返回False
        """
        try:
            # 将所有朋友对象转换为字典
            data = {
                'friends': [friend.to_dict() for friend in self.friends.values()],
                'last_updated': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            # 确保数据目录存在
            data_dir = os.path.dirname(self.data_file)
            if data_dir and not os.path.exists(data_dir):
                os.makedirs(data_dir)
            
            # 写入JSON文件
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            return True
        except Exception as e:
            print(f"保存数据失败: {e}")
            return False
    
    def load_data(self):
        """
        从文件加载数据
        
        返回:
            成功返回True,失败返回False
        """
        # 检查文件是否存在
        if not os.path.exists(self.data_file):
            print(f"数据文件 {self.data_file} 不存在,将创建新文件")
            return False
        
        try:
            # 读取JSON文件
            with open(self.data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # 从字典创建Friend对象
            self.friends = {}
            for friend_data in data.get('friends', []):
                friend = Friend.from_dict(friend_data)
                self.friends[friend.friend_id] = friend
            
            print(f"成功加载 {len(self.friends)} 位朋友的数据")
            return True
        except Exception as e:
            print(f"加载数据失败: {e}")
            return False
    
    def export_data(self, export_file=None):
        """
        导出数据到指定文件
        
        参数:
            export_file: 导出文件路径,如果为None则自动生成文件名
            
        返回:
            导出的文件路径
        """
        # 如果没有指定导出文件,自动生成文件名
        if export_file is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            export_file = f"friends_export_{timestamp}.json"
        
        # 确保导出目录存在
        export_dir = os.path.dirname(export_file)
        if export_dir and not os.path.exists(export_dir):
            os.makedirs(export_dir)
        
        # 准备导出数据
        export_data = {
            'export_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'total_friends': len(self.friends),
            'friends': [friend.to_dict() for friend in self.friends.values()]
        }
        
        # 写入文件
        with open(export_file, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, ensure_ascii=False, indent=2)
        
        print(f"数据已导出到: {export_file}")
        return export_file


# 演示代码(当直接运行此文件时执行)
if __name__ == "__main__":
    print("=== 朋友管理系统演示 ===\n")
    
    # 创建管理器
    manager = FriendManager("demo_friends.json")
    
    # 添加朋友
    print("1. 添加朋友:")
    manager.add_friend("F001", "张三", "13800138000", "1995-05-20", "北京市", "大学同学")
    manager.add_friend("F002", "李四", "13900139000", "1996-03-15", "上海市", "工作伙伴")
    manager.add_friend("F003", "王五", "13700137000", birthday="1995-05-25")
    print()
    
    # 列出所有朋友
    print("2. 所有朋友:")
    for friend in manager.list_all_friends():
        print(f"  - {friend.name} ({friend.friend_id})")
    print()
    
    # 搜索朋友
    print("3. 搜索'同学':")
    results = manager.search_friends("同学")
    for friend in results:
        print(f"  - {friend.name}: {friend.notes}")
    print()
    
    # 统计信息
    print("4. 统计信息:")
    stats = manager.get_statistics()
    print(f"  总朋友数: {stats['total_friends']}")
    print(f"  有生日信息: {stats['with_birthday']}")
    print(f"  本月生日: {stats['birthday_this_month']}")
