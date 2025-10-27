/*
 * 文件名: Library.java
 * 作者: 开发者
 * 创建日期: 2025-10-27
 * 版本: 1.0
 * 描述: 这是一个表示图书馆管理系统的Java类文件
 *       包含图书的添加、删除、查询等管理功能
 * 功能:
 *   - 管理图书集合
 *   - 提供图书的增删改查功能
 *   - 实现图书借阅和归还功能
 *   - 提供图书搜索功能
 * 依赖: Book.java
 * 修改记录:
 *   2025-10-27 - 初始版本创建
 */

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

/**
 * Library类 - 表示一个图书馆管理系统
 * 
 * 该类用于管理图书馆中的图书集合，提供图书的增删改查、借阅归还等功能。
 * 
 * 设计原则:
 * 1. 封装性: 图书集合为私有字段，通过公共方法访问
 * 2. 数据完整性: 提供验证机制确保操作的有效性
 * 3. 功能完整性: 提供完整的图书管理功能
 * 
 * 使用示例:
 * <pre>
 * {@code
 * // 创建图书馆对象
 * Library library = new Library();
 * 
 * // 添加图书
 * Book book = new Book("978-0-123456-78-9", "Java编程思想", "Bruce Eckel", 
 *                      "机械工业出版社", LocalDate.now(), 99.00, 3);
 * library.addBook(book);
 * 
 * // 借阅图书
 * boolean borrowed = library.borrowBook("978-0-123456-78-9");
 * 
 * // 搜索图书
 * List<Book> books = library.searchBooksByAuthor("Bruce Eckel");
 * }
 * </pre>
 */
public class Library {
    /** 图书馆中所有图书的集合 */
    private List<Book> books;
    
    /**
     * 默认构造函数
     * 初始化一个空的图书馆对象
     */
    public Library() {
        this.books = new ArrayList<>();
    }
    
    /**
     * 向图书馆添加图书
     * 
     * @param book 要添加的图书对象
     * @return 如果添加成功返回true，否则返回false
     * 
     * @throws IllegalArgumentException 如果book为null
     */
    public boolean addBook(Book book) {
        if (book == null) {
            throw new IllegalArgumentException("图书对象不能为null");
        }
        
        // 检查是否已存在相同ISBN的图书
        if (findBookByIsbn(book.getIsbn()).isPresent()) {
            return false; // 已存在相同ISBN的图书
        }
        
        return books.add(book);
    }
    
    /**
     * 从图书馆移除图书
     * 根据图书的ISBN移除图书
     * 
     * @param isbn 要移除图书的ISBN
     * @return 如果移除成功返回true，否则返回false
     */
    public boolean removeBook(String isbn) {
        Optional<Book> book = findBookByIsbn(isbn);
        if (book.isPresent()) {
            return books.remove(book.get());
        }
        return false;
    }
    
    /**
     * 根据ISBN查找图书
     * 
     * @param isbn 要查找图书的ISBN
     * @return 包含图书的Optional对象，如果未找到则返回空Optional
     */
    public Optional<Book> findBookByIsbn(String isbn) {
        return books.stream()
                   .filter(book -> book.getIsbn().equals(isbn))
                   .findFirst();
    }
    
    /**
     * 根据书名查找图书
     * 支持模糊匹配
     * 
     * @param title 要查找的书名（支持模糊匹配）
     * @return 匹配的图书列表
     */
    public List<Book> findBooksByTitle(String title) {
        List<Book> result = new ArrayList<>();
        if (title == null || title.isEmpty()) {
            return result;
        }
        
        for (Book book : books) {
            if (book.getTitle().toLowerCase().contains(title.toLowerCase())) {
                result.add(book);
            }
        }
        return result;
    }
    
    /**
     * 根据作者查找图书
     * 
     * @param author 要查找的作者名
     * @return 包含该作者所有图书的列表
     */
    public List<Book> findBooksByAuthor(String author) {
        List<Book> result = new ArrayList<>();
        if (author == null || author.isEmpty()) {
            return result;
        }
        
        for (Book book : books) {
            if (book.getAuthor().toLowerCase().contains(author.toLowerCase())) {
                result.add(book);
            }
        }
        return result;
    }
    
    /**
     * 获取图书馆中所有图书
     * 
     * @return 图书馆中所有图书的副本列表
     */
    public List<Book> getAllBooks() {
        return new ArrayList<>(books);
    }
    
    /**
     * 借阅图书
     * 根据ISBN借阅图书，减少图书的可借阅数量
     * 
     * @param isbn 要借阅图书的ISBN
     * @return 如果借阅成功返回true，否则返回false
     */
    public boolean borrowBook(String isbn) {
        Optional<Book> book = findBookByIsbn(isbn);
        if (book.isPresent()) {
            return book.get().borrowBook();
        }
        return false;
    }
    
    /**
     * 归还图书
     * 根据ISBN归还图书，增加图书的可借阅数量
     * 
     * @param isbn 要归还图书的ISBN
     * @return 如果归还成功返回true，否则返回false
     */
    public boolean returnBook(String isbn) {
        Optional<Book> book = findBookByIsbn(isbn);
        if (book.isPresent()) {
            return book.get().returnBook();
        }
        return false;
    }
    
    /**
     * 获取图书馆中图书的总数量
     * 
     * @return 图书馆中图书的总数量
     */
    public int getTotalBookCount() {
        return books.size();
    }
    
    /**
     * 获取可借阅的图书数量
     * 
     * @return 可借阅的图书数量
     */
    public int getAvailableBookCount() {
        return (int) books.stream()
                         .filter(Book::isAvailable)
                         .count();
    }
    
    /**
     * 获取所有可借阅的图书
     * 
     * @return 所有可借阅图书的列表
     */
    public List<Book> getAvailableBooks() {
        List<Book> availableBooks = new ArrayList<>();
        for (Book book : books) {
            if (book.isAvailable()) {
                availableBooks.add(book);
            }
        }
        return availableBooks;
    }
    
    /**
     * 清空图书馆中的所有图书
     */
    public void clear() {
        books.clear();
    }
    
    /**
     * 获取图书馆的字符串表示
     * 
     * @return 图书馆信息的字符串表示
     */
    @Override
    public String toString() {
        return "Library{" +
                "totalBooks=" + books.size() +
                ", availableBooks=" + getAvailableBookCount() +
                '}';
    }
}