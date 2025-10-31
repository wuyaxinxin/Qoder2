// 始终生效
// 模型决策

package library.ui;

import library.model.Book;
import library.model.Reader;
import library.model.BorrowRecord;
import library.service.BookService;
import library.service.ReaderService;
import library.service.BorrowService;
import java.util.List;
import java.util.Scanner;

/**
 * 控制台用户界面类
 * 处理用户交互和菜单显示
 */
public class ConsoleUI {
    
    private final Scanner scanner;
    private final BookService bookService;
    private final ReaderService readerService;
    private final BorrowService borrowService;
    
    /**
     * 构造函数
     */
    public ConsoleUI(BookService bookService, 
                     ReaderService readerService,
                     BorrowService borrowService) {
        this.scanner = new Scanner(System.in);
        this.bookService = bookService;
        this.readerService = readerService;
        this.borrowService = borrowService;
    }
    
    /**
     * 启动主菜单
     */
    public void start() {
        System.out.println("╔══════════════════════════════════════╗");
        System.out.println("║     欢迎使用图书管理系统             ║");
        System.out.println("╚══════════════════════════════════════╝");
        
        while (true) {
            showMainMenu();
            String choice = scanner.nextLine().trim();
            
            switch (choice) {
                case "1":
                    bookManagementMenu();
                    break;
                case "2":
                    readerManagementMenu();
                    break;
                case "3":
                    borrowManagementMenu();
                    break;
                case "0":
                    System.out.println("\n感谢使用图书管理系统，再见！");
                    return;
                default:
                    System.out.println("\n无效的选择，请重新输入！");
                    pause();
            }
        }
    }
    
    /**
     * 显示主菜单
     */
    private void showMainMenu() {
        System.out.println("\n╔══════════════════════════════════════╗");
        System.out.println("║            主菜单                    ║");
        System.out.println("╠══════════════════════════════════════╣");
        System.out.println("║  1. 图书管理                         ║");
        System.out.println("║  2. 读者管理                         ║");
        System.out.println("║  3. 借阅管理                         ║");
        System.out.println("║  0. 退出系统                         ║");
        System.out.println("╚══════════════════════════════════════╝");
        System.out.print("请选择操作 [0-3]: ");
    }
    
    /**
     * 图书管理菜单
     */
    private void bookManagementMenu() {
        while (true) {
            System.out.println("\n╔══════════════════════════════════════╗");
            System.out.println("║          图书管理                    ║");
            System.out.println("╠══════════════════════════════════════╣");
            System.out.println("║  1. 添加图书                         ║");
            System.out.println("║  2. 删除图书                         ║");
            System.out.println("║  3. 更新图书                         ║");
            System.out.println("║  4. 查询图书                         ║");
            System.out.println("║  5. 列出所有图书                     ║");
            System.out.println("║  6. 搜索图书                         ║");
            System.out.println("║  0. 返回主菜单                       ║");
            System.out.println("╚══════════════════════════════════════╝");
            System.out.print("请选择操作 [0-6]: ");
            
            String choice = scanner.nextLine().trim();
            
            switch (choice) {
                case "1":
                    addBook();
                    break;
                case "2":
                    deleteBook();
                    break;
                case "3":
                    updateBook();
                    break;
                case "4":
                    queryBook();
                    break;
                case "5":
                    listAllBooks();
                    break;
                case "6":
                    searchBooks();
                    break;
                case "0":
                    return;
                default:
                    System.out.println("\n无效的选择，请重新输入！");
                    pause();
            }
        }
    }
    
    /**
     * 读者管理菜单
     */
    private void readerManagementMenu() {
        while (true) {
            System.out.println("\n╔══════════════════════════════════════╗");
            System.out.println("║          读者管理                    ║");
            System.out.println("╠══════════════════════════════════════╣");
            System.out.println("║  1. 注册读者                         ║");
            System.out.println("║  2. 删除读者                         ║");
            System.out.println("║  3. 更新读者信息                     ║");
            System.out.println("║  4. 查询读者                         ║");
            System.out.println("║  5. 列出所有读者                     ║");
            System.out.println("║  6. 查询读者借阅历史                 ║");
            System.out.println("║  0. 返回主菜单                       ║");
            System.out.println("╚══════════════════════════════════════╝");
            System.out.print("请选择操作 [0-6]: ");
            
            String choice = scanner.nextLine().trim();
            
            switch (choice) {
                case "1":
                    registerReader();
                    break;
                case "2":
                    deleteReader();
                    break;
                case "3":
                    updateReader();
                    break;
                case "4":
                    queryReader();
                    break;
                case "5":
                    listAllReaders();
                    break;
                case "6":
                    queryReaderHistory();
                    break;
                case "0":
                    return;
                default:
                    System.out.println("\n无效的选择，请重新输入！");
                    pause();
            }
        }
    }
    
    /**
     * 借阅管理菜单
     */
    private void borrowManagementMenu() {
        while (true) {
            System.out.println("\n╔══════════════════════════════════════╗");
            System.out.println("║          借阅管理                    ║");
            System.out.println("╠══════════════════════════════════════╣");
            System.out.println("║  1. 借阅图书                         ║");
            System.out.println("║  2. 归还图书                         ║");
            System.out.println("║  3. 查询借阅记录                     ║");
            System.out.println("║  4. 当前借阅清单                     ║");
            System.out.println("║  0. 返回主菜单                       ║");
            System.out.println("╚══════════════════════════════════════╝");
            System.out.print("请选择操作 [0-4]: ");
            
            String choice = scanner.nextLine().trim();
            
            switch (choice) {
                case "1":
                    borrowBook();
                    break;
                case "2":
                    returnBook();
                    break;
                case "3":
                    queryBorrowRecord();
                    break;
                case "4":
                    listCurrentBorrowings();
                    break;
                case "0":
                    return;
                default:
                    System.out.println("\n无效的选择，请重新输入！");
                    pause();
            }
        }
    }
    
    // ==================== 图书管理操作 ====================
    
    private void addBook() {
        System.out.println("\n【添加图书】");
        System.out.print("图书编号: ");
        String bookId = scanner.nextLine().trim();
        
        System.out.print("书名: ");
        String title = scanner.nextLine().trim();
        
        System.out.print("作者: ");
        String author = scanner.nextLine().trim();
        
        System.out.print("ISBN (可选，直接回车跳过): ");
        String isbn = scanner.nextLine().trim();
        if (isbn.isEmpty()) isbn = null;
        
        System.out.print("出版社 (可选，直接回车跳过): ");
        String publisher = scanner.nextLine().trim();
        if (publisher.isEmpty()) publisher = null;
        
        System.out.print("总数量: ");
        int totalCount;
        try {
            totalCount = Integer.parseInt(scanner.nextLine().trim());
        } catch (NumberFormatException e) {
            System.out.println("\n总数量格式错误！");
            pause();
            return;
        }
        
        Book book = new Book(bookId, title, author, isbn, publisher, totalCount, totalCount);
        String result = bookService.addBook(book);
        System.out.println("\n" + result);
        pause();
    }
    
    private void deleteBook() {
        System.out.println("\n【删除图书】");
        System.out.print("请输入图书编号: ");
        String bookId = scanner.nextLine().trim();
        
        String result = bookService.deleteBook(bookId);
        System.out.println("\n" + result);
        pause();
    }
    
    private void updateBook() {
        System.out.println("\n【更新图书】");
        System.out.print("请输入图书编号: ");
        String bookId = scanner.nextLine().trim();
        
        Book book = bookService.getBook(bookId);
        if (book == null) {
            System.out.println("\n图书不存在！");
            pause();
            return;
        }
        
        System.out.println("\n当前图书信息：");
        System.out.println(book);
        System.out.println("\n请输入新信息（直接回车保持原值）：");
        
        System.out.print("书名 [" + book.getTitle() + "]: ");
        String title = scanner.nextLine().trim();
        if (!title.isEmpty()) book.setTitle(title);
        
        System.out.print("作者 [" + book.getAuthor() + "]: ");
        String author = scanner.nextLine().trim();
        if (!author.isEmpty()) book.setAuthor(author);
        
        System.out.print("ISBN [" + (book.getIsbn() != null ? book.getIsbn() : "无") + "]: ");
        String isbn = scanner.nextLine().trim();
        if (!isbn.isEmpty()) book.setIsbn(isbn);
        
        System.out.print("出版社 [" + (book.getPublisher() != null ? book.getPublisher() : "无") + "]: ");
        String publisher = scanner.nextLine().trim();
        if (!publisher.isEmpty()) book.setPublisher(publisher);
        
        String result = bookService.updateBook(book);
        System.out.println("\n" + result);
        pause();
    }
    
    private void queryBook() {
        System.out.println("\n【查询图书】");
        System.out.print("请输入图书编号: ");
        String bookId = scanner.nextLine().trim();
        
        Book book = bookService.getBook(bookId);
        if (book == null) {
            System.out.println("\n图书不存在！");
        } else {
            System.out.println("\n" + book);
        }
        pause();
    }
    
    private void listAllBooks() {
        System.out.println("\n【所有图书列表】");
        List<Book> books = bookService.listAllBooks();
        
        if (books.isEmpty()) {
            System.out.println("暂无图书！");
        } else {
            System.out.println("共有 " + books.size() + " 本图书：");
            System.out.println("─────────────────────────────────────────────────────────────");
            for (Book book : books) {
                System.out.printf("%-10s | %-20s | %-15s | 库存: %d/%d%n",
                        book.getBookId(),
                        book.getTitle(),
                        book.getAuthor(),
                        book.getAvailableCount(),
                        book.getTotalCount());
            }
            System.out.println("─────────────────────────────────────────────────────────────");
        }
        pause();
    }
    
    private void searchBooks() {
        System.out.println("\n【搜索图书】");
        System.out.println("1. 按书名搜索");
        System.out.println("2. 按作者搜索");
        System.out.print("请选择搜索方式: ");
        String choice = scanner.nextLine().trim();
        
        List<Book> books;
        if ("1".equals(choice)) {
            System.out.print("请输入书名关键词: ");
            String title = scanner.nextLine().trim();
            books = bookService.searchByTitle(title);
        } else if ("2".equals(choice)) {
            System.out.print("请输入作者关键词: ");
            String author = scanner.nextLine().trim();
            books = bookService.searchByAuthor(author);
        } else {
            System.out.println("\n无效的选择！");
            pause();
            return;
        }
        
        if (books.isEmpty()) {
            System.out.println("\n未找到匹配的图书！");
        } else {
            System.out.println("\n找到 " + books.size() + " 本图书：");
            System.out.println("─────────────────────────────────────────────────────────────");
            for (Book book : books) {
                System.out.printf("%-10s | %-20s | %-15s | 库存: %d/%d%n",
                        book.getBookId(),
                        book.getTitle(),
                        book.getAuthor(),
                        book.getAvailableCount(),
                        book.getTotalCount());
            }
            System.out.println("─────────────────────────────────────────────────────────────");
        }
        pause();
    }
    
    // ==================== 读者管理操作 ====================
    
    private void registerReader() {
        System.out.println("\n【注册读者】");
        System.out.print("读者编号: ");
        String readerId = scanner.nextLine().trim();
        
        System.out.print("姓名: ");
        String name = scanner.nextLine().trim();
        
        System.out.print("联系电话 (11位数字): ");
        String phone = scanner.nextLine().trim();
        
        System.out.print("邮箱 (可选，直接回车跳过): ");
        String email = scanner.nextLine().trim();
        if (email.isEmpty()) email = null;
        
        Reader reader = new Reader(readerId, name, phone);
        reader.setEmail(email);
        
        String result = readerService.registerReader(reader);
        System.out.println("\n" + result);
        pause();
    }
    
    private void deleteReader() {
        System.out.println("\n【删除读者】");
        System.out.print("请输入读者编号: ");
        String readerId = scanner.nextLine().trim();
        
        String result = readerService.deleteReader(readerId);
        System.out.println("\n" + result);
        pause();
    }
    
    private void updateReader() {
        System.out.println("\n【更新读者信息】");
        System.out.print("请输入读者编号: ");
        String readerId = scanner.nextLine().trim();
        
        Reader reader = readerService.getReader(readerId);
        if (reader == null) {
            System.out.println("\n读者不存在！");
            pause();
            return;
        }
        
        System.out.println("\n当前读者信息：");
        System.out.println(reader);
        System.out.println("\n请输入新信息（直接回车保持原值）：");
        
        System.out.print("姓名 [" + reader.getName() + "]: ");
        String name = scanner.nextLine().trim();
        if (!name.isEmpty()) reader.setName(name);
        
        System.out.print("联系电话 [" + reader.getPhone() + "]: ");
        String phone = scanner.nextLine().trim();
        if (!phone.isEmpty()) reader.setPhone(phone);
        
        System.out.print("邮箱 [" + (reader.getEmail() != null ? reader.getEmail() : "无") + "]: ");
        String email = scanner.nextLine().trim();
        if (!email.isEmpty()) reader.setEmail(email);
        
        String result = readerService.updateReader(reader);
        System.out.println("\n" + result);
        pause();
    }
    
    private void queryReader() {
        System.out.println("\n【查询读者】");
        System.out.print("请输入读者编号: ");
        String readerId = scanner.nextLine().trim();
        
        Reader reader = readerService.getReader(readerId);
        if (reader == null) {
            System.out.println("\n读者不存在！");
        } else {
            System.out.println("\n" + reader);
        }
        pause();
    }
    
    private void listAllReaders() {
        System.out.println("\n【所有读者列表】");
        List<Reader> readers = readerService.listAllReaders();
        
        if (readers.isEmpty()) {
            System.out.println("暂无读者！");
        } else {
            System.out.println("共有 " + readers.size() + " 位读者：");
            System.out.println("─────────────────────────────────────────────────────────────");
            for (Reader reader : readers) {
                System.out.printf("%-10s | %-15s | %-12s | 已借: %d/%d%n",
                        reader.getReaderId(),
                        reader.getName(),
                        reader.getPhone(),
                        reader.getCurrentBorrowCount(),
                        reader.getMaxBorrowLimit());
            }
            System.out.println("─────────────────────────────────────────────────────────────");
        }
        pause();
    }
    
    private void queryReaderHistory() {
        System.out.println("\n【查询读者借阅历史】");
        System.out.print("请输入读者编号: ");
        String readerId = scanner.nextLine().trim();
        
        List<BorrowRecord> records = readerService.getReaderBorrowHistory(readerId);
        
        if (records.isEmpty()) {
            System.out.println("\n该读者暂无借阅记录！");
        } else {
            System.out.println("\n找到 " + records.size() + " 条借阅记录：");
            System.out.println("─────────────────────────────────────────────────────────────");
            for (BorrowRecord record : records) {
                System.out.println(record);
                System.out.println("─────────────────────────────────────────────────────────────");
            }
        }
        pause();
    }
    
    // ==================== 借阅管理操作 ====================
    
    private void borrowBook() {
        System.out.println("\n【借阅图书】");
        System.out.print("请输入读者编号: ");
        String readerId = scanner.nextLine().trim();
        
        System.out.print("请输入图书编号: ");
        String bookId = scanner.nextLine().trim();
        
        System.out.println("\n正在处理借阅请求...");
        String result = borrowService.borrowBook(readerId, bookId);
        System.out.println("\n" + result);
        pause();
    }
    
    private void returnBook() {
        System.out.println("\n【归还图书】");
        System.out.print("请输入读者编号: ");
        String readerId = scanner.nextLine().trim();
        
        System.out.print("请输入图书编号: ");
        String bookId = scanner.nextLine().trim();
        
        System.out.println("\n正在处理归还请求...");
        String result = borrowService.returnBook(readerId, bookId);
        System.out.println("\n" + result);
        pause();
    }
    
    private void queryBorrowRecord() {
        System.out.println("\n【查询借阅记录】");
        System.out.print("请输入记录编号: ");
        String recordId = scanner.nextLine().trim();
        
        BorrowRecord record = borrowService.getBorrowRecord(recordId);
        if (record == null) {
            System.out.println("\n借阅记录不存在！");
        } else {
            System.out.println("\n" + record);
        }
        pause();
    }
    
    private void listCurrentBorrowings() {
        System.out.println("\n【当前借阅清单】");
        List<BorrowRecord> records = borrowService.listCurrentBorrowings();
        
        if (records.isEmpty()) {
            System.out.println("当前没有未归还的借阅！");
        } else {
            System.out.println("共有 " + records.size() + " 条未归还的借阅：");
            System.out.println("─────────────────────────────────────────────────────────────");
            for (BorrowRecord record : records) {
                System.out.println(record);
                System.out.println("─────────────────────────────────────────────────────────────");
            }
        }
        pause();
    }
    
    /**
     * 暂停等待用户按键
     */
    private void pause() {
        System.out.print("\n按回车键继续...");
        scanner.nextLine();
    }
}
// 始终生效
// 模型决策

package library.ui;

import library.model.Book;
import library.model.Reader;
import library.model.BorrowRecord;
import library.service.BookService;
import library.service.ReaderService;
import library.service.BorrowService;
import java.util.List;
import java.util.Scanner;

/**
 * 控制台用户界面类
 * 处理用户交互和菜单显示
 */
public class ConsoleUI {
    
    private final Scanner scanner;
    private final BookService bookService;
    private final ReaderService readerService;
    private final BorrowService borrowService;
    
    /**
     * 构造函数
     */
    public ConsoleUI(BookService bookService, 
                     ReaderService readerService,
                     BorrowService borrowService) {
        this.scanner = new Scanner(System.in);
        this.bookService = bookService;
        this.readerService = readerService;
        this.borrowService = borrowService;
    }
    
    /**
     * 启动主菜单
     */
    public void start() {
        System.out.println("╔══════════════════════════════════════╗");
        System.out.println("║     欢迎使用图书管理系统             ║");
        System.out.println("╚══════════════════════════════════════╝");
        
        while (true) {
            showMainMenu();
            String choice = scanner.nextLine().trim();
            
            switch (choice) {
                case "1":
                    bookManagementMenu();
                    break;
                case "2":
                    readerManagementMenu();
                    break;
                case "3":
                    borrowManagementMenu();
                    break;
                case "0":
                    System.out.println("\n感谢使用图书管理系统，再见！");
                    return;
                default:
                    System.out.println("\n无效的选择，请重新输入！");
                    pause();
            }
        }
    }
    
    /**
     * 显示主菜单
     */
    private void showMainMenu() {
        System.out.println("\n╔══════════════════════════════════════╗");
        System.out.println("║            主菜单                    ║");
        System.out.println("╠══════════════════════════════════════╣");
        System.out.println("║  1. 图书管理                         ║");
        System.out.println("║  2. 读者管理                         ║");
        System.out.println("║  3. 借阅管理                         ║");
        System.out.println("║  0. 退出系统                         ║");
        System.out.println("╚══════════════════════════════════════╝");
        System.out.print("请选择操作 [0-3]: ");
    }
    
    /**
     * 图书管理菜单
     */
    private void bookManagementMenu() {
        while (true) {
            System.out.println("\n╔══════════════════════════════════════╗");
            System.out.println("║          图书管理                    ║");
            System.out.println("╠══════════════════════════════════════╣");
            System.out.println("║  1. 添加图书                         ║");
            System.out.println("║  2. 删除图书                         ║");
            System.out.println("║  3. 更新图书                         ║");
            System.out.println("║  4. 查询图书                         ║");
            System.out.println("║  5. 列出所有图书                     ║");
            System.out.println("║  6. 搜索图书                         ║");
            System.out.println("║  0. 返回主菜单                       ║");
            System.out.println("╚══════════════════════════════════════╝");
            System.out.print("请选择操作 [0-6]: ");
            
            String choice = scanner.nextLine().trim();
            
            switch (choice) {
                case "1":
                    addBook();
                    break;
                case "2":
                    deleteBook();
                    break;
                case "3":
                    updateBook();
                    break;
                case "4":
                    queryBook();
                    break;
                case "5":
                    listAllBooks();
                    break;
                case "6":
                    searchBooks();
                    break;
                case "0":
                    return;
                default:
                    System.out.println("\n无效的选择，请重新输入！");
                    pause();
            }
        }
    }
    
    /**
     * 读者管理菜单
     */
    private void readerManagementMenu() {
        while (true) {
            System.out.println("\n╔══════════════════════════════════════╗");
            System.out.println("║          读者管理                    ║");
            System.out.println("╠══════════════════════════════════════╣");
            System.out.println("║  1. 注册读者                         ║");
            System.out.println("║  2. 删除读者                         ║");
            System.out.println("║  3. 更新读者信息                     ║");
            System.out.println("║  4. 查询读者                         ║");
            System.out.println("║  5. 列出所有读者                     ║");
            System.out.println("║  6. 查询读者借阅历史                 ║");
            System.out.println("║  0. 返回主菜单                       ║");
            System.out.println("╚══════════════════════════════════════╝");
            System.out.print("请选择操作 [0-6]: ");
            
            String choice = scanner.nextLine().trim();
            
            switch (choice) {
                case "1":
                    registerReader();
                    break;
                case "2":
                    deleteReader();
                    break;
                case "3":
                    updateReader();
                    break;
                case "4":
                    queryReader();
                    break;
                case "5":
                    listAllReaders();
                    break;
                case "6":
                    queryReaderHistory();
                    break;
                case "0":
                    return;
                default:
                    System.out.println("\n无效的选择，请重新输入！");
                    pause();
            }
        }
    }
    
    /**
     * 借阅管理菜单
     */
    private void borrowManagementMenu() {
        while (true) {
            System.out.println("\n╔══════════════════════════════════════╗");
            System.out.println("║          借阅管理                    ║");
            System.out.println("╠══════════════════════════════════════╣");
            System.out.println("║  1. 借阅图书                         ║");
            System.out.println("║  2. 归还图书                         ║");
            System.out.println("║  3. 查询借阅记录                     ║");
            System.out.println("║  4. 当前借阅清单                     ║");
            System.out.println("║  0. 返回主菜单                       ║");
            System.out.println("╚══════════════════════════════════════╝");
            System.out.print("请选择操作 [0-4]: ");
            
            String choice = scanner.nextLine().trim();
            
            switch (choice) {
                case "1":
                    borrowBook();
                    break;
                case "2":
                    returnBook();
                    break;
                case "3":
                    queryBorrowRecord();
                    break;
                case "4":
                    listCurrentBorrowings();
                    break;
                case "0":
                    return;
                default:
                    System.out.println("\n无效的选择，请重新输入！");
                    pause();
            }
        }
    }
    
    // ==================== 图书管理操作 ====================
    
    private void addBook() {
        System.out.println("\n【添加图书】");
        System.out.print("图书编号: ");
        String bookId = scanner.nextLine().trim();
        
        System.out.print("书名: ");
        String title = scanner.nextLine().trim();
        
        System.out.print("作者: ");
        String author = scanner.nextLine().trim();
        
        System.out.print("ISBN (可选，直接回车跳过): ");
        String isbn = scanner.nextLine().trim();
        if (isbn.isEmpty()) isbn = null;
        
        System.out.print("出版社 (可选，直接回车跳过): ");
        String publisher = scanner.nextLine().trim();
        if (publisher.isEmpty()) publisher = null;
        
        System.out.print("总数量: ");
        int totalCount;
        try {
            totalCount = Integer.parseInt(scanner.nextLine().trim());
        } catch (NumberFormatException e) {
            System.out.println("\n总数量格式错误！");
            pause();
            return;
        }
        
        Book book = new Book(bookId, title, author, isbn, publisher, totalCount, totalCount);
        String result = bookService.addBook(book);
        System.out.println("\n" + result);
        pause();
    }
    
    private void deleteBook() {
        System.out.println("\n【删除图书】");
        System.out.print("请输入图书编号: ");
        String bookId = scanner.nextLine().trim();
        
        String result = bookService.deleteBook(bookId);
        System.out.println("\n" + result);
        pause();
    }
    
    private void updateBook() {
        System.out.println("\n【更新图书】");
        System.out.print("请输入图书编号: ");
        String bookId = scanner.nextLine().trim();
        
        Book book = bookService.getBook(bookId);
        if (book == null) {
            System.out.println("\n图书不存在！");
            pause();
            return;
        }
        
        System.out.println("\n当前图书信息：");
        System.out.println(book);
        System.out.println("\n请输入新信息（直接回车保持原值）：");
        
        System.out.print("书名 [" + book.getTitle() + "]: ");
        String title = scanner.nextLine().trim();
        if (!title.isEmpty()) book.setTitle(title);
        
        System.out.print("作者 [" + book.getAuthor() + "]: ");
        String author = scanner.nextLine().trim();
        if (!author.isEmpty()) book.setAuthor(author);
        
        System.out.print("ISBN [" + (book.getIsbn() != null ? book.getIsbn() : "无") + "]: ");
        String isbn = scanner.nextLine().trim();
        if (!isbn.isEmpty()) book.setIsbn(isbn);
        
        System.out.print("出版社 [" + (book.getPublisher() != null ? book.getPublisher() : "无") + "]: ");
        String publisher = scanner.nextLine().trim();
        if (!publisher.isEmpty()) book.setPublisher(publisher);
        
        String result = bookService.updateBook(book);
        System.out.println("\n" + result);
        pause();
    }
    
    private void queryBook() {
        System.out.println("\n【查询图书】");
        System.out.print("请输入图书编号: ");
        String bookId = scanner.nextLine().trim();
        
        Book book = bookService.getBook(bookId);
        if (book == null) {
            System.out.println("\n图书不存在！");
        } else {
            System.out.println("\n" + book);
        }
        pause();
    }
    
    private void listAllBooks() {
        System.out.println("\n【所有图书列表】");
        List<Book> books = bookService.listAllBooks();
        
        if (books.isEmpty()) {
            System.out.println("暂无图书！");
        } else {
            System.out.println("共有 " + books.size() + " 本图书：");
            System.out.println("─────────────────────────────────────────────────────────────");
            for (Book book : books) {
                System.out.printf("%-10s | %-20s | %-15s | 库存: %d/%d%n",
                        book.getBookId(),
                        book.getTitle(),
                        book.getAuthor(),
                        book.getAvailableCount(),
                        book.getTotalCount());
            }
            System.out.println("─────────────────────────────────────────────────────────────");
        }
        pause();
    }
    
    private void searchBooks() {
        System.out.println("\n【搜索图书】");
        System.out.println("1. 按书名搜索");
        System.out.println("2. 按作者搜索");
        System.out.print("请选择搜索方式: ");
        String choice = scanner.nextLine().trim();
        
        List<Book> books;
        if ("1".equals(choice)) {
            System.out.print("请输入书名关键词: ");
            String title = scanner.nextLine().trim();
            books = bookService.searchByTitle(title);
        } else if ("2".equals(choice)) {
            System.out.print("请输入作者关键词: ");
            String author = scanner.nextLine().trim();
            books = bookService.searchByAuthor(author);
        } else {
            System.out.println("\n无效的选择！");
            pause();
            return;
        }
        
        if (books.isEmpty()) {
            System.out.println("\n未找到匹配的图书！");
        } else {
            System.out.println("\n找到 " + books.size() + " 本图书：");
            System.out.println("─────────────────────────────────────────────────────────────");
            for (Book book : books) {
                System.out.printf("%-10s | %-20s | %-15s | 库存: %d/%d%n",
                        book.getBookId(),
                        book.getTitle(),
                        book.getAuthor(),
                        book.getAvailableCount(),
                        book.getTotalCount());
            }
            System.out.println("─────────────────────────────────────────────────────────────");
        }
        pause();
    }
    
    // ==================== 读者管理操作 ====================
    
    private void registerReader() {
        System.out.println("\n【注册读者】");
        System.out.print("读者编号: ");
        String readerId = scanner.nextLine().trim();
        
        System.out.print("姓名: ");
        String name = scanner.nextLine().trim();
        
        System.out.print("联系电话 (11位数字): ");
        String phone = scanner.nextLine().trim();
        
        System.out.print("邮箱 (可选，直接回车跳过): ");
        String email = scanner.nextLine().trim();
        if (email.isEmpty()) email = null;
        
        Reader reader = new Reader(readerId, name, phone);
        reader.setEmail(email);
        
        String result = readerService.registerReader(reader);
        System.out.println("\n" + result);
        pause();
    }
    
    private void deleteReader() {
        System.out.println("\n【删除读者】");
        System.out.print("请输入读者编号: ");
        String readerId = scanner.nextLine().trim();
        
        String result = readerService.deleteReader(readerId);
        System.out.println("\n" + result);
        pause();
    }
    
    private void updateReader() {
        System.out.println("\n【更新读者信息】");
        System.out.print("请输入读者编号: ");
        String readerId = scanner.nextLine().trim();
        
        Reader reader = readerService.getReader(readerId);
        if (reader == null) {
            System.out.println("\n读者不存在！");
            pause();
            return;
        }
        
        System.out.println("\n当前读者信息：");
        System.out.println(reader);
        System.out.println("\n请输入新信息（直接回车保持原值）：");
        
        System.out.print("姓名 [" + reader.getName() + "]: ");
        String name = scanner.nextLine().trim();
        if (!name.isEmpty()) reader.setName(name);
        
        System.out.print("联系电话 [" + reader.getPhone() + "]: ");
        String phone = scanner.nextLine().trim();
        if (!phone.isEmpty()) reader.setPhone(phone);
        
        System.out.print("邮箱 [" + (reader.getEmail() != null ? reader.getEmail() : "无") + "]: ");
        String email = scanner.nextLine().trim();
        if (!email.isEmpty()) reader.setEmail(email);
        
        String result = readerService.updateReader(reader);
        System.out.println("\n" + result);
        pause();
    }
    
    private void queryReader() {
        System.out.println("\n【查询读者】");
        System.out.print("请输入读者编号: ");
        String readerId = scanner.nextLine().trim();
        
        Reader reader = readerService.getReader(readerId);
        if (reader == null) {
            System.out.println("\n读者不存在！");
        } else {
            System.out.println("\n" + reader);
        }
        pause();
    }
    
    private void listAllReaders() {
        System.out.println("\n【所有读者列表】");
        List<Reader> readers = readerService.listAllReaders();
        
        if (readers.isEmpty()) {
            System.out.println("暂无读者！");
        } else {
            System.out.println("共有 " + readers.size() + " 位读者：");
            System.out.println("─────────────────────────────────────────────────────────────");
            for (Reader reader : readers) {
                System.out.printf("%-10s | %-15s | %-12s | 已借: %d/%d%n",
                        reader.getReaderId(),
                        reader.getName(),
                        reader.getPhone(),
                        reader.getCurrentBorrowCount(),
                        reader.getMaxBorrowLimit());
            }
            System.out.println("─────────────────────────────────────────────────────────────");
        }
        pause();
    }
    
    private void queryReaderHistory() {
        System.out.println("\n【查询读者借阅历史】");
        System.out.print("请输入读者编号: ");
        String readerId = scanner.nextLine().trim();
        
        List<BorrowRecord> records = readerService.getReaderBorrowHistory(readerId);
        
        if (records.isEmpty()) {
            System.out.println("\n该读者暂无借阅记录！");
        } else {
            System.out.println("\n找到 " + records.size() + " 条借阅记录：");
            System.out.println("─────────────────────────────────────────────────────────────");
            for (BorrowRecord record : records) {
                System.out.println(record);
                System.out.println("─────────────────────────────────────────────────────────────");
            }
        }
        pause();
    }
    
    // ==================== 借阅管理操作 ====================
    
    private void borrowBook() {
        System.out.println("\n【借阅图书】");
        System.out.print("请输入读者编号: ");
        String readerId = scanner.nextLine().trim();
        
        System.out.print("请输入图书编号: ");
        String bookId = scanner.nextLine().trim();
        
        System.out.println("\n正在处理借阅请求...");
        String result = borrowService.borrowBook(readerId, bookId);
        System.out.println("\n" + result);
        pause();
    }
    
    private void returnBook() {
        System.out.println("\n【归还图书】");
        System.out.print("请输入读者编号: ");
        String readerId = scanner.nextLine().trim();
        
        System.out.print("请输入图书编号: ");
        String bookId = scanner.nextLine().trim();
        
        System.out.println("\n正在处理归还请求...");
        String result = borrowService.returnBook(readerId, bookId);
        System.out.println("\n" + result);
        pause();
    }
    
    private void queryBorrowRecord() {
        System.out.println("\n【查询借阅记录】");
        System.out.print("请输入记录编号: ");
        String recordId = scanner.nextLine().trim();
        
        BorrowRecord record = borrowService.getBorrowRecord(recordId);
        if (record == null) {
            System.out.println("\n借阅记录不存在！");
        } else {
            System.out.println("\n" + record);
        }
        pause();
    }
    
    private void listCurrentBorrowings() {
        System.out.println("\n【当前借阅清单】");
        List<BorrowRecord> records = borrowService.listCurrentBorrowings();
        
        if (records.isEmpty()) {
            System.out.println("当前没有未归还的借阅！");
        } else {
            System.out.println("共有 " + records.size() + " 条未归还的借阅：");
            System.out.println("─────────────────────────────────────────────────────────────");
            for (BorrowRecord record : records) {
                System.out.println(record);
                System.out.println("─────────────────────────────────────────────────────────────");
            }
        }
        pause();
    }
    
    /**
     * 暂停等待用户按键
     */
    private void pause() {
        System.out.print("\n按回车键继续...");
        scanner.nextLine();
    }
}
