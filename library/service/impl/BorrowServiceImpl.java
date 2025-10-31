// 始终生效
// 模型决策

package library.service.impl;

import library.model.Book;
import library.model.Reader;
import library.model.BorrowRecord;
import library.repository.BookRepository;
import library.repository.ReaderRepository;
import library.repository.BorrowRecordRepository;
import library.service.BorrowService;
import java.util.List;
import java.util.UUID;

/**
 * 借阅管理服务实现类
 * 实现借阅管理的核心业务逻辑
 */
public class BorrowServiceImpl implements BorrowService {
    
    private final BookRepository bookRepository;
    private final ReaderRepository readerRepository;
    private final BorrowRecordRepository borrowRecordRepository;
    
    /**
     * 构造函数
     */
    public BorrowServiceImpl(BookRepository bookRepository,
                            ReaderRepository readerRepository,
                            BorrowRecordRepository borrowRecordRepository) {
        this.bookRepository = bookRepository;
        this.readerRepository = readerRepository;
        this.borrowRecordRepository = borrowRecordRepository;
    }
    
    @Override
    public String borrowBook(String readerId, String bookId) {
        // 参数验证
        if (readerId == null || readerId.trim().isEmpty()) {
            return "借阅失败：读者编号不能为空";
        }
        
        if (bookId == null || bookId.trim().isEmpty()) {
            return "借阅失败：图书编号不能为空";
        }
        
        // 验证读者是否存在
        Reader reader = readerRepository.findById(readerId).orElse(null);
        if (reader == null) {
            return "借阅失败：读者编号 " + readerId + " 不存在";
        }
        
        // 验证图书是否存在
        Book book = bookRepository.findById(bookId).orElse(null);
        if (book == null) {
            return "借阅失败：图书编号 " + bookId + " 不存在";
        }
        
        // 检查读者是否达到借阅上限
        if (!reader.canBorrow()) {
            return "借阅失败：该读者已达到最大借阅数量限制（" + reader.getMaxBorrowLimit() + 
                   "本），请先归还部分图书后再借阅";
        }
        
        // 检查图书库存
        if (!book.isAvailable()) {
            return "借阅失败：该图书已借完，当前库存为0";
        }
        
        // 检查是否已经借阅了同一本书
        if (borrowRecordRepository.findBorrowingRecord(readerId, bookId).isPresent()) {
            return "借阅失败：您已经借阅了这本书，不能重复借阅";
        }
        
        // 创建借阅记录
        String recordId = "REC" + UUID.randomUUID().toString().substring(0, 8).toUpperCase();
        BorrowRecord record = new BorrowRecord(recordId, bookId, readerId);
        
        // 保存借阅记录
        borrowRecordRepository.add(record);
        
        // 更新图书可借数量
        book.borrowOut();
        bookRepository.update(book);
        
        // 更新读者当前借阅数
        reader.borrowBook();
        readerRepository.update(reader);
        
        // 返回成功信息
        return "借阅成功！\n" +
               "读者：" + reader.getName() + "（" + readerId + "）\n" +
               "图书：《" + book.getTitle() + "》（" + bookId + "）\n" +
               "借阅日期：" + record.getBorrowDate().toLocalDate() + "\n" +
               "应还日期：" + record.getDueDate().toLocalDate() + "\n" +
               "记录编号：" + recordId;
    }
    
    @Override
    public String returnBook(String readerId, String bookId) {
        // 参数验证
        if (readerId == null || readerId.trim().isEmpty()) {
            return "归还失败：读者编号不能为空";
        }
        
        if (bookId == null || bookId.trim().isEmpty()) {
            return "归还失败：图书编号不能为空";
        }
        
        // 查找对应的借阅记录
        BorrowRecord record = borrowRecordRepository.findBorrowingRecord(readerId, bookId)
                .orElse(null);
        
        if (record == null) {
            return "归还失败：未找到该读者借阅该图书的记录，可能已归还或借阅信息有误";
        }
        
        // 检查记录状态
        if (record.isReturned()) {
            return "归还失败：该图书已经归还过了";
        }
        
        // 获取读者和图书信息
        Reader reader = readerRepository.findById(readerId).orElse(null);
        Book book = bookRepository.findById(bookId).orElse(null);
        
        if (reader == null || book == null) {
            return "归还失败：读者或图书信息不存在";
        }
        
        // 完成归还操作
        record.completeReturn();
        borrowRecordRepository.update(record);
        
        // 更新图书可借数量
        book.returnBack();
        bookRepository.update(book);
        
        // 更新读者当前借阅数
        reader.returnBook();
        readerRepository.update(reader);
        
        // 检查是否超期
        String overdueInfo = "";
        if (record.isOverdue()) {
            overdueInfo = "\n【提示】该图书已超期归还";
        }
        
        // 返回成功信息
        return "归还成功！\n" +
               "读者：" + reader.getName() + "（" + readerId + "）\n" +
               "图书：《" + book.getTitle() + "》（" + bookId + "）\n" +
               "借阅日期：" + record.getBorrowDate().toLocalDate() + "\n" +
               "应还日期：" + record.getDueDate().toLocalDate() + "\n" +
               "归还日期：" + record.getReturnDate().toLocalDate() +
               overdueInfo;
    }
    
    @Override
    public BorrowRecord getBorrowRecord(String recordId) {
        if (recordId == null || recordId.trim().isEmpty()) {
            return null;
        }
        
        return borrowRecordRepository.findById(recordId).orElse(null);
    }
    
    @Override
    public List<BorrowRecord> listAllRecords() {
        return borrowRecordRepository.findAll();
    }
    
    @Override
    public List<BorrowRecord> listCurrentBorrowings() {
        return borrowRecordRepository.findAllBorrowing();
    }
    
    @Override
    public List<BorrowRecord> getBookBorrowStatus(String bookId) {
        if (bookId == null || bookId.trim().isEmpty()) {
            return List.of();
        }
        
        return borrowRecordRepository.findByBookId(bookId);
    }
    
    @Override
    public List<BorrowRecord> getReaderCurrentBorrowings(String readerId) {
        if (readerId == null || readerId.trim().isEmpty()) {
            return List.of();
        }
        
        return borrowRecordRepository.findBorrowingByReaderId(readerId);
    }
}
