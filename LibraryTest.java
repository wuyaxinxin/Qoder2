/*
 * 文件名: LibraryTest.java
 * 作者: 开发者
 * 创建日期: 2025-10-27
 * 版本: 1.0
 * 描述: 这是一个用于测试Library类功能的Java测试文件
 * 功能:
 *   - 测试Library类的基本功能
 *   - 验证图书的添加、删除、查找功能
 *   - 验证图书的借阅和归还功能
 * 依赖: Library.java, Book.java
 * 修改记录:
 *   2025-10-27 - 初始版本创建
 */

import java.time.LocalDate;

/**
 * LibraryTest类 - 用于测试Library类的功能
 */
public class LibraryTest {
    /**
     * 主方法，用于运行测试
     * 
     * @param args 命令行参数
     */
    public static void main(String[] args) {
        System.out.println("开始测试Library类...");
        
        // 创建图书馆对象
        Library library = new Library();
        System.out.println("1. 创建图书馆对象成功");
        
        // 创建测试图书
        Book book1 = new Book("978-0-123456-78-9", "Java编程思想", "Bruce Eckel", 
                             "机械工业出版社", LocalDate.of(2020, 1, 1), 99.00, 3);
        Book book2 = new Book("978-1-234567-89-0", "设计模式", "Gang of Four", 
                             "机械工业出版社", LocalDate.of(2019, 5, 1), 79.00, 2);
        System.out.println("2. 创建测试图书成功");
        
        // 测试添加图书
        boolean added1 = library.addBook(book1);
        boolean added2 = library.addBook(book2);
        System.out.println("3. 添加图书功能测试: " + (added1 && added2 ? "通过" : "失败"));
        
        // 测试查找图书
        var foundBook = library.findBookByIsbn("978-0-123456-78-9");
        System.out.println("4. 查找图书功能测试: " + (foundBook.isPresent() ? "通过" : "失败"));
        
        // 测试获取所有图书
        var allBooks = library.getAllBooks();
        System.out.println("5. 获取所有图书功能测试: " + (allBooks.size() == 2 ? "通过" : "失败"));
        
        // 测试借阅图书
        boolean borrowed = library.borrowBook("978-0-123456-78-9");
        System.out.println("6. 借阅图书功能测试: " + (borrowed ? "通过" : "失败"));
        
        // 测试获取可借阅图书
        var availableBooks = library.getAvailableBooks();
        System.out.println("7. 获取可借阅图书功能测试: " + (availableBooks.size() > 0 ? "通过" : "失败"));
        
        // 测试归还图书
        boolean returned = library.returnBook("978-0-123456-78-9");
        System.out.println("8. 归还图书功能测试: " + (returned ? "通过" : "失败"));
        
        // 测试删除图书
        boolean removed = library.removeBook("978-1-234567-89-0");
        System.out.println("9. 删除图书功能测试: " + (removed ? "通过" : "失败"));
        
        System.out.println("Library类功能测试完成！");
        System.out.println("图书馆当前状态: " + library.toString());
    }
}