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
    private String title;
    private String author;
    private String isbn;
    private int pages;
    private boolean available;

    // 无参构造函数
    public Book() {
    }

    // 有参构造函数
    public Book(String title, String author, String isbn, int pages) {
        this.title = title;
        this.author = author;
        this.isbn = isbn;
        this.pages = pages;
        this.available = true; // 默认图书是可借阅的
    }

    // getter和setter方法
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public String getIsbn() {
        return isbn;
    }

    public void setIsbn(String isbn) {
        this.isbn = isbn;
    }

    public int getPages() {
        return pages;
    }

    public void setPages(int pages) {
        this.pages = pages;
    }

    public boolean isAvailable() {
        return available;
    }

    public void setAvailable(boolean available) {
        this.available = available;
    }

    // 借书方法
    public void borrow() {
        if (available) {
            this.available = false;
            System.out.println("Book '" + title + "' has been borrowed.");
        } else {
            System.out.println("Book '" + title + "' is not available for borrowing.");
        }
    }

    // 还书方法
    public void returnBook() {
        if (!available) {
            this.available = true;
            System.out.println("Book '" + title + "' has been returned.");
        } else {
            System.out.println("Book '" + title + "' is already available.");
        }
    }

    // toString方法
    @Override
    public String toString() {
        return "Book{" +
                "title='" + title + '\'' +
                ", author='" + author + '\'' +
                ", isbn='" + isbn + '\'' +
                ", pages=" + pages +
                ", available=" + available +
                '}';
    }
}
