// 始终生效
// 模型决策

package library;

import library.model.Book;
import library.model.Reader;
import library.repository.BookRepository;
import library.repository.ReaderRepository;
import library.repository.BorrowRecordRepository;
import library.repository.impl.BookRepositoryImpl;
import library.repository.impl.ReaderRepositoryImpl;
import library.repository.impl.BorrowRecordRepositoryImpl;
import library.service.BookService;
import library.service.ReaderService;
import library.service.BorrowService;
import library.service.impl.BookServiceImpl;
import library.service.impl.ReaderServiceImpl;
import library.service.impl.BorrowServiceImpl;
import library.ui.ConsoleUI;

/**
 * 图书管理系统主程序类
 * 程序入口，负责初始化系统并启动用户界面
 */
public class LibrarySystem {
    
    public static void main(String[] args) {
        System.out.println("正在启动图书管理系统...");
        
        // 第一步：初始化数据访问层
        BookRepository bookRepository = new BookRepositoryImpl();
        ReaderRepository readerRepository = new ReaderRepositoryImpl();
        BorrowRecordRepository borrowRecordRepository = new BorrowRecordRepositoryImpl();
        
        // 第二步：初始化业务服务层
        BookService bookService = new BookServiceImpl(bookRepository, borrowRecordRepository);
        ReaderService readerService = new ReaderServiceImpl(readerRepository, borrowRecordRepository);
        BorrowService borrowService = new BorrowServiceImpl(bookRepository, readerRepository, borrowRecordRepository);
        
        // 第三步：初始化演示数据
        initDemoData(bookService, readerService);
        
        // 第四步：创建并启动用户界面
        ConsoleUI consoleUI = new ConsoleUI(bookService, readerService, borrowService);
        consoleUI.start();
    }
    
    /**
     * 初始化演示数据
     * 添加一些初始的图书和读者数据用于演示
     */
    private static void initDemoData(BookService bookService, ReaderService readerService) {
        System.out.println("正在初始化演示数据...");
        
        // 添加演示图书
        Book book1 = new Book("B001", "Java编程思想", "Bruce Eckel", "978-0131872486", "机械工业出版社", 3, 3);
        Book book2 = new Book("B002", "设计模式", "Erich Gamma", "978-0201633610", "机械工业出版社", 2, 2);
        Book book3 = new Book("B003", "算法导论", "Thomas H. Cormen", "978-0262033848", "机械工业出版社", 5, 5);
        Book book4 = new Book("B004", "深入理解计算机系统", "Randal E. Bryant", "978-0134092669", "机械工业出版社", 2, 2);
        Book book5 = new Book("B005", "代码大全", "Steve McConnell", "978-0735619678", "电子工业出版社", 3, 3);
        
        bookService.addBook(book1);
        bookService.addBook(book2);
        bookService.addBook(book3);
        bookService.addBook(book4);
        bookService.addBook(book5);
        
        // 添加演示读者
        Reader reader1 = new Reader("R001", "张三", "13800138001");
        reader1.setEmail("zhangsan@example.com");
        
        Reader reader2 = new Reader("R002", "李四", "13800138002");
        reader2.setEmail("lisi@example.com");
        
        Reader reader3 = new Reader("R003", "王五", "13800138003");
        reader3.setEmail("wangwu@example.com");
        
        readerService.registerReader(reader1);
        readerService.registerReader(reader2);
        readerService.registerReader(reader3);
        
        System.out.println("演示数据初始化完成！");
        System.out.println("已添加 5 本图书和 3 位读者");
        System.out.println();
    }
}
