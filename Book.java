/*
 * 文件名: Book.java
 * 作者: 开发者
 * 创建日期: 2025-10-27
 * 版本: 1.0
 * 描述: 这是一个表示图书信息的Java类文件
 *       包含图书的基本信息和相关操作方法
 * 功能:
 *   - 存储和管理图书基本信息
 *   - 提供标准的getter/setter方法
 *   - 实现图书借阅状态管理
 *   - 重写equals、hashCode和toString方法
 * 依赖: 无外部依赖,仅使用Java标准库
 * 修改记录:
 *   2025-10-27 - 初始版本创建
 */

import java.time.LocalDate;

/**
 * Book类 - 表示一本图书的基 本信息
 */
public class Book {
    private String isbn;
    private String title;
    private String author;
    private String publisher;
    private LocalDate publishDate;
    private double price;
    private int totalCopies;
    private int availableCopies;
    private boolean isBorrowed;
    
    /**
     * 默认构造函数
     */
    public Book() {
        this.isbn = "";
        this.title = "";
        this.author = "";
        this.publisher = "";
        this.publishDate = LocalDate.now();
        this.price = 0.0;
        this.totalCopies = 0;
        this.availableCopies = 0;
        this.isBorrowed = false;
    }
    
    /**
     * 带参数的构造函数
     * @param isbn 图书ISBN
     * @param title 书名
     * @param author 作者
     * @param publisher 出版社
     * @param publishDate 出版日期
     * @param price 价格
     * @param totalCopies 总册数
     */
    public Book(String isbn, String title, String author, String publisher, 
                LocalDate publishDate, double price, int totalCopies) {
        this.isbn = isbn;
        this.title = title;
        this.author = author;
        this.publisher = publisher;
        this.publishDate = publishDate;
        this.price = price;
        this.totalCopies = totalCopies;
        this.availableCopies = totalCopies;
        this.isBorrowed = false;
    }
    
    /**
     * 获取ISBN
     * @return ISBN编号
     */
    public String getIsbn() {
        return isbn;
    }
    
    /**
     * 设置ISBN
     * @param isbn ISBN编号
     */
    public void setIsbn(String isbn) {
        this.isbn = isbn;
    }
    
    /**
     * 获取书名
     * @return 书名
     */
    public String getTitle() {
        return title;
    }
    
    /**
     * 设置书名
     * @param title 书名
     */
    public void setTitle(String title) {
        this.title = title;
    }
    
    /**
     * 获取作者
     * @return 作者名
     */
    public String getAuthor() {
        return author;
    }
    
    /**
     * 设置作者
     * @param author 作者名
     */
    public void setAuthor(String author) {
        this.author = author;
    }
    
    /**
     * 获取出版社
     * @return 出版社名称
     */
    public String getPublisher() {
        return publisher;
    }
    
    /**
     * 设置出版社
     * @param publisher 出版社名称
     */
    public void setPublisher(String publisher) {
        this.publisher = publisher;
    }
    
    /**
     * 获取出版日期
     * @return 出版日期
     */
    public LocalDate getPublishDate() {
        return publishDate;
    }
    
    /**
     * 设置出版日期
     * @param publishDate 出版日期
     */
    public void setPublishDate(LocalDate publishDate) {
        this.publishDate = publishDate;
    }
    
    /**
     * 获取价格
     * @return 价格
     */
    public double getPrice() {
        return price;
    }
    
    /**
     * 设置价格
     * @param price 价格
     */
    public void setPrice(double price) {
        if (price >= 0) {
            this.price = price;
        }
    }
    
    /**
     * 获取总册数
     * @return 总册数
     */
    public int getTotalCopies() {
        return totalCopies;
    }
    
    /**
     * 设置总册数
     * @param totalCopies 总册数
     */
    public void setTotalCopies(int totalCopies) {
        if (totalCopies >= 0) {
            this.totalCopies = totalCopies;
        }
    }
    
    /**
     * 获取可借册数
     * @return 可借册数
     */
    public int getAvailableCopies() {
        return availableCopies;
    }
    
    /**
     * 借阅图书
     * @return 如果借阅成功返回true,否则返回false
     */
    public boolean borrowBook() {
        if (availableCopies > 0) {
            availableCopies--;
            if (availableCopies == 0) {
                isBorrowed = true;
            }
            return true;
        }
        return false;
    }
    
    /**
     * 归还图书
     * @return 如果归还成功返回true,否则返回false
     */
    public boolean returnBook() {
        if (availableCopies < totalCopies) {
            availableCopies++;
            if (availableCopies > 0) {
                isBorrowed = false;
            }
            return true;
        }
        return false;
    }
    
    /**
     * 判断图书是否可借
     * @return 如果可借返回true,否则返回false
     */
    public boolean isAvailable() {
        return availableCopies > 0;
    }
    
    /**
     * 判断图书是否全部被借出
     * @return 如果全部被借出返回true,否则返回false
     */
    public boolean isAllBorrowed() {
        return availableCopies == 0;
    }
    
    /**
     * 获取图书信息描述
     * @return 图书信息字符串
     */
    public String getDescription() {
        return String.format("ISBN: %s, 书名: %s, 作者: %s, 出版社: %s, 价格: %.2f元, 可借: %d/%d", 
                           isbn, title, author, publisher, price, availableCopies, totalCopies);
    }
    
    @Override
    public String toString() {
        return "Book{" +
                "isbn='" + isbn + '\'' +
                ", title='" + title + '\'' +
                ", author='" + author + '\'' +
                ", publisher='" + publisher + '\'' +
                ", publishDate=" + publishDate +
                ", price=" + price +
                ", totalCopies=" + totalCopies +
                ", availableCopies=" + availableCopies +
                ", isBorrowed=" + isBorrowed +
                '}';
    }
    
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Book book = (Book) obj;
        return isbn.equals(book.isbn);
    }
    
    @Override
    public int hashCode() {
        return isbn.hashCode();
    }
}
