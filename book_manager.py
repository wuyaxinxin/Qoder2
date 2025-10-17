"""
BookManager - 图书管理系统
这是一个Python类,演示了面向对象编程和数据管理的基本概念
"""


class Book:
    """图书类 - 表示单本图书的信息"""
    
    def __init__(self, book_id, title, author, price, stock=0):
        """
        初始化图书对象
        
        Args:
            book_id: 图书编号
            title: 书名
            author: 作者
            price: 价格
            stock: 库存数量(默认为0)
        """
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock
    
    def display_info(self):
        """显示图书信息"""
        print(f"图书编号: {self.book_id}")
        print(f"书名: {self.title}")
        print(f"作者: {self.author}")
        print(f"价格: ¥{self.price:.2f}")
        print(f"库存: {self.stock}本")
        print("-" * 40)
    
    def is_available(self):
        """检查图书是否有库存"""
        return self.stock > 0
    
    def __str__(self):
        """字符串表示"""
        return f"{self.title} - {self.author} (库存: {self.stock})"


class BookManager:
    """图书管理器类 - 管理多本图书"""
    
    def __init__(self):
        """初始化图书管理器"""
        self.books = {}  # 使用字典存储图书,键为book_id
    
    def add_book(self, book):
        """
        添加图书
        
        Args:
            book: Book对象
        """
        if book.book_id in self.books:
            print(f"图书 {book.book_id} 已存在!")
            return False
        self.books[book.book_id] = book
        print(f"成功添加图书: {book.title}")
        return True
    
    def remove_book(self, book_id):
        """
        删除图书
        
        Args:
            book_id: 图书编号
        """
        if book_id in self.books:
            book = self.books.pop(book_id)
            print(f"成功删除图书: {book.title}")
            return True
        else:
            print(f"未找到图书编号: {book_id}")
            return False
    
    def find_book(self, book_id):
        """
        查找图书
        
        Args:
            book_id: 图书编号
        
        Returns:
            Book对象或None
        """
        return self.books.get(book_id)
    
    def search_by_title(self, title):
        """
        按书名搜索图书
        
        Args:
            title: 书名关键词
        
        Returns:
            匹配的图书列表
        """
        results = [book for book in self.books.values() 
                   if title.lower() in book.title.lower()]
        return results
    
    def update_stock(self, book_id, quantity):
        """
        更新图书库存
        
        Args:
            book_id: 图书编号
            quantity: 库存变化量(正数增加,负数减少)
        """
        book = self.find_book(book_id)
        if book:
            new_stock = book.stock + quantity
            if new_stock < 0:
                print("库存不足!")
                return False
            book.stock = new_stock
            print(f"更新成功! 当前库存: {book.stock}")
            return True
        else:
            print(f"未找到图书编号: {book_id}")
            return False
    
    def list_all_books(self):
        """列出所有图书"""
        if not self.books:
            print("暂无图书!")
            return
        
        print("\n====== 图书列表 ======")
        for book in self.books.values():
            book.display_info()
    
    def get_total_value(self):
        """计算图书总价值"""
        total = sum(book.price * book.stock for book in self.books.values())
        return total


def demo():
    """演示函数"""
    print("========== 图书管理系统演示 ==========\n")
    
    # 创建图书管理器
    manager = BookManager()
    
    # 添加图书
    print(">>> 添加图书")
    book1 = Book("B001", "Python编程从入门到实践", "Eric Matthes", 89.00, 50)
    book2 = Book("B002", "Java核心技术", "Cay S. Horstmann", 128.00, 30)
    book3 = Book("B003", "算法导论", "Thomas H. Cormen", 158.00, 20)
    
    manager.add_book(book1)
    manager.add_book(book2)
    manager.add_book(book3)
    print()
    
    # 列出所有图书
    print(">>> 列出所有图书")
    manager.list_all_books()
    print()
    
    # 搜索图书
    print(">>> 搜索包含'Python'的图书")
    results = manager.search_by_title("Python")
    for book in results:
        print(f"  - {book}")
    print()
    
    # 更新库存
    print(">>> 更新库存(销售10本Python书籍)")
    manager.update_stock("B001", -10)
    print()
    
    # 查看单本图书信息
    print(">>> 查看图书详情")
    book = manager.find_book("B001")
    if book:
        book.display_info()
    
    # 计算总价值
    print(f">>> 图书总价值: ¥{manager.get_total_value():.2f}")


if __name__ == "__main__":
    demo()
