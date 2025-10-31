// 始终生效
// 模型决策

package library.service.impl;

import library.model.Book;
import library.repository.BookRepository;
import library.repository.BorrowRecordRepository;
import library.service.BookService;
import java.util.List;
import java.util.stream.Collectors;

/**
 * 图书管理服务实现类
 * 实现图书管理的业务逻辑
 */
public class BookServiceImpl implements BookService {
    
    private final BookRepository bookRepository;
    private final BorrowRecordRepository borrowRecordRepository;
    
    /**
     * 构造函数
     * @param bookRepository 图书数据访问对象
     * @param borrowRecordRepository 借阅记录数据访问对象
     */
    public BookServiceImpl(BookRepository bookRepository, 
                          BorrowRecordRepository borrowRecordRepository) {
        this.bookRepository = bookRepository;
        this.borrowRecordRepository = borrowRecordRepository;
    }
    
    @Override
    public String addBook(Book book) {
        // 数据验证
        if (book == null) {
            return "添加失败：图书信息不能为空";
        }
        
        if (book.getBookId() == null || book.getBookId().trim().isEmpty()) {
            return "添加失败：图书编号不能为空";
        }
        
        if (book.getTitle() == null || book.getTitle().trim().isEmpty()) {
            return "添加失败：书名不能为空";
        }
        
        if (book.getAuthor() == null || book.getAuthor().trim().isEmpty()) {
            return "添加失败：作者不能为空";
        }
        
        if (book.getTotalCount() <= 0) {
            return "添加失败：图书总数量必须大于0";
        }
        
        if (book.getAvailableCount() < 0 || book.getAvailableCount() > book.getTotalCount()) {
            return "添加失败：可借数量必须在0到总数量之间";
        }
        
        // 添加图书
        boolean success = bookRepository.add(book);
        if (success) {
            return "添加成功：图书《" + book.getTitle() + "》已添加到系统";
        } else {
            return "添加失败：图书编号 " + book.getBookId() + " 已存在";
        }
    }
    
    @Override
    public String deleteBook(String bookId) {
        if (bookId == null || bookId.trim().isEmpty()) {
            return "删除失败：图书编号不能为空";
        }
        
        // 检查图书是否存在
        Book book = bookRepository.findById(bookId).orElse(null);
        if (book == null) {
            return "删除失败：图书编号 " + bookId + " 不存在";
        }
        
        // 检查是否有未归还的借阅记录
        List<library.model.BorrowRecord> borrowingRecords = 
            borrowRecordRepository.findBorrowingByBookId(bookId);
        if (!borrowingRecords.isEmpty()) {
            return "删除失败：该图书还有 " + borrowingRecords.size() + " 条未归还的借阅记录，无法删除";
        }
        
        // 删除图书
        boolean success = bookRepository.delete(bookId);
        if (success) {
            return "删除成功：图书《" + book.getTitle() + "》已从系统中删除";
        } else {
            return "删除失败：未知错误";
        }
    }
    
    @Override
    public String updateBook(Book book) {
        if (book == null) {
            return "更新失败：图书信息不能为空";
        }
        
        if (book.getBookId() == null || book.getBookId().trim().isEmpty()) {
            return "更新失败：图书编号不能为空";
        }
        
        // 检查图书是否存在
        if (!bookRepository.exists(book.getBookId())) {
            return "更新失败：图书编号 " + book.getBookId() + " 不存在";
        }
        
        // 数据验证
        if (book.getTitle() != null && book.getTitle().trim().isEmpty()) {
            return "更新失败：书名不能为空";
        }
        
        if (book.getAuthor() != null && book.getAuthor().trim().isEmpty()) {
            return "更新失败：作者不能为空";
        }
        
        if (book.getTotalCount() < book.getAvailableCount()) {
            return "更新失败：总数量不能小于可借数量";
        }
        
        // 更新图书
        boolean success = bookRepository.update(book);
        if (success) {
            return "更新成功：图书《" + book.getTitle() + "》信息已更新";
        } else {
            return "更新失败：未知错误";
        }
    }
    
    @Override
    public Book getBook(String bookId) {
        if (bookId == null || bookId.trim().isEmpty()) {
            return null;
        }
        
        return bookRepository.findById(bookId).orElse(null);
    }
    
    @Override
    public List<Book> listAllBooks() {
        return bookRepository.findAll();
    }
    
    @Override
    public List<Book> searchByTitle(String title) {
        if (title == null || title.trim().isEmpty()) {
            return List.of();
        }
        
        return bookRepository.findByTitle(title);
    }
    
    @Override
    public List<Book> searchByAuthor(String author) {
        if (author == null || author.trim().isEmpty()) {
            return List.of();
        }
        
        return bookRepository.findByAuthor(author);
    }
    
    @Override
    public List<Book> getAvailableBooks() {
        return bookRepository.findAll().stream()
                .filter(Book::isAvailable)
                .collect(Collectors.toList());
    }
}
