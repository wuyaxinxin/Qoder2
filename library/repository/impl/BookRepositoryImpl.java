// 始终生效
// 模型决策

package library.repository.impl;

import library.model.Book;
import library.repository.BookRepository;
import java.util.*;
import java.util.stream.Collectors;

/**
 * 图书数据访问实现类
 * 使用内存HashMap存储图书数据
 */
public class BookRepositoryImpl implements BookRepository {
    
    // 使用HashMap存储图书数据，key为图书编号，value为图书对象
    private final Map<String, Book> bookStorage = new HashMap<>();
    
    @Override
    public boolean add(Book book) {
        if (book == null || book.getBookId() == null) {
            return false;
        }
        
        // 检查图书编号是否已存在
        if (bookStorage.containsKey(book.getBookId())) {
            return false;
        }
        
        bookStorage.put(book.getBookId(), book);
        return true;
    }
    
    @Override
    public boolean delete(String bookId) {
        if (bookId == null) {
            return false;
        }
        
        return bookStorage.remove(bookId) != null;
    }
    
    @Override
    public boolean update(Book book) {
        if (book == null || book.getBookId() == null) {
            return false;
        }
        
        // 检查图书是否存在
        if (!bookStorage.containsKey(book.getBookId())) {
            return false;
        }
        
        bookStorage.put(book.getBookId(), book);
        return true;
    }
    
    @Override
    public Optional<Book> findById(String bookId) {
        if (bookId == null) {
            return Optional.empty();
        }
        
        return Optional.ofNullable(bookStorage.get(bookId));
    }
    
    @Override
    public List<Book> findAll() {
        return new ArrayList<>(bookStorage.values());
    }
    
    @Override
    public List<Book> findByTitle(String title) {
        if (title == null || title.trim().isEmpty()) {
            return new ArrayList<>();
        }
        
        String keyword = title.trim().toLowerCase();
        return bookStorage.values().stream()
                .filter(book -> book.getTitle().toLowerCase().contains(keyword))
                .collect(Collectors.toList());
    }
    
    @Override
    public List<Book> findByAuthor(String author) {
        if (author == null || author.trim().isEmpty()) {
            return new ArrayList<>();
        }
        
        String keyword = author.trim().toLowerCase();
        return bookStorage.values().stream()
                .filter(book -> book.getAuthor().toLowerCase().contains(keyword))
                .collect(Collectors.toList());
    }
    
    @Override
    public boolean exists(String bookId) {
        if (bookId == null) {
            return false;
        }
        
        return bookStorage.containsKey(bookId);
    }
    
    @Override
    public int count() {
        return bookStorage.size();
    }
}
