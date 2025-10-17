"""
朋友类定义模块
定义了Friend类,用于表示朋友的基本信息
"""

import json
from datetime import datetime


class Friend:
    """朋友类,用于存储和管理朋友的基本信息"""
    
    def __init__(self, friend_id, name, phone, birthday=None, address=None, notes=None):
        """
        初始化朋友对象
        
        参数:
            friend_id: 朋友ID(字符串类型)
            name: 朋友姓名
            phone: 电话号码
            birthday: 生日(格式: YYYY-MM-DD)
            address: 地址
            notes: 备注信息
        """
        self.friend_id = friend_id  # 朋友唯一标识ID
        self.name = name  # 朋友姓名
        self.phone = phone  # 电话号码
        self.birthday = birthday  # 生日
        self.address = address  # 地址
        self.notes = notes  # 备注信息
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # 创建时间
        self.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # 更新时间
    
    def update_info(self, name=None, phone=None, birthday=None, address=None, notes=None):
        """
        更新朋友信息
        
        参数:
            name: 新姓名(可选)
            phone: 新电话(可选)
            birthday: 新生日(可选)
            address: 新地址(可选)
            notes: 新备注(可选)
        """
        # 只更新提供的非空参数
        if name is not None:
            self.name = name
        if phone is not None:
            self.phone = phone
        if birthday is not None:
            self.birthday = birthday
        if address is not None:
            self.address = address
        if notes is not None:
            self.notes = notes
        # 更新修改时间
        self.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def get_age(self):
        """
        计算朋友年龄
        
        返回:
            年龄(整数),如果没有生日信息则返回None
        """
        if not self.birthday:
            return None
        
        try:
            # 解析生日字符串
            birth_date = datetime.strptime(self.birthday, "%Y-%m-%d")
            today = datetime.now()
            # 计算年龄
            age = today.year - birth_date.year
            # 如果今年生日还没过,年龄减1
            if (today.month, today.day) < (birth_date.month, birth_date.day):
                age -= 1
            return age
        except ValueError:
            return None  # 日期格式错误时返回None
    
    def to_dict(self):
        """
        将朋友对象转换为字典格式
        
        返回:
            包含朋友所有信息的字典
        """
        return {
            'friend_id': self.friend_id,
            'name': self.name,
            'phone': self.phone,
            'birthday': self.birthday,
            'address': self.address,
            'notes': self.notes,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
    
    @classmethod
    def from_dict(cls, data):
        """
        从字典创建朋友对象
        
        参数:
            data: 包含朋友信息的字典
            
        返回:
            Friend对象
        """
        # 创建朋友对象
        friend = cls(
            friend_id=data['friend_id'],
            name=data['name'],
            phone=data['phone'],
            birthday=data.get('birthday'),
            address=data.get('address'),
            notes=data.get('notes')
        )
        # 恢复时间戳
        if 'created_at' in data:
            friend.created_at = data['created_at']
        if 'updated_at' in data:
            friend.updated_at = data['updated_at']
        return friend
    
    def __str__(self):
        """
        返回朋友信息的字符串表示
        
        返回:
            格式化的朋友信息字符串
        """
        age_info = f"({self.get_age()}岁)" if self.get_age() else ""
        return (f"朋友ID: {self.friend_id}\n"
                f"姓名: {self.name} {age_info}\n"
                f"电话: {self.phone}\n"
                f"生日: {self.birthday or '未设置'}\n"
                f"地址: {self.address or '未设置'}\n"
                f"备注: {self.notes or '无'}\n"
                f"创建时间: {self.created_at}\n"
                f"更新时间: {self.updated_at}")
    
    def __repr__(self):
        """
        返回朋友对象的开发者友好表示
        
        返回:
            对象的字符串表示
        """
        return f"Friend(id={self.friend_id}, name={self.name}, phone={self.phone})"


# 演示代码(当直接运行此文件时执行)
if __name__ == "__main__":
    print("=== 朋友类演示 ===\n")
    
    # 创建朋友对象
    friend1 = Friend(
        friend_id="F001",
        name="张三",
        phone="13800138000",
        birthday="1995-05-20",
        address="北京市朝阳区",
        notes="大学同学"
    )
    
    # 显示朋友信息
    print("创建的朋友信息:")
    print(friend1)
    print()
    
    # 更新朋友信息
    print("更新朋友信息...")
    friend1.update_info(phone="13900139000", notes="大学同学,现在是同事")
    print(friend1)
    print()
    
    # 转换为字典
    print("转换为字典格式:")
    print(json.dumps(friend1.to_dict(), ensure_ascii=False, indent=2))
