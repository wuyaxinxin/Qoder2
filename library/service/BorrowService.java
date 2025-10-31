// 始终生效
// 模型决策

package library.service;

import library.model.BorrowRecord;
import java.util.List;

/**
 * 借阅管理服务接口
 * 定义借阅管理的业务操作
 */
public interface BorrowService {
    
    /**
     * 借阅图书
     * @param readerId 读者编号
     * @param bookId 图书编号
     * @return 操作结果消息
     */
    String borrowBook(String readerId, String bookId);
    
    /**
     * 归还图书
     * @param readerId 读者编号
     * @param bookId 图书编号
     * @return 操作结果消息
     */
    String returnBook(String readerId, String bookId);
    
    /**
     * 查询借阅记录
     * @param recordId 记录编号
     * @return 借阅记录对象，如果不存在返回null
     */
    BorrowRecord getBorrowRecord(String recordId);
    
    /**
     * 查询所有借阅记录
     * @return 所有借阅记录的列表
     */
    List<BorrowRecord> listAllRecords();
    
    /**
     * 查询当前借阅清单（未归还的借阅）
     * @return 未归还的借阅记录列表
     */
    List<BorrowRecord> listCurrentBorrowings();
    
    /**
     * 查询某本书的借阅状态
     * @param bookId 图书编号
     * @return 该图书的所有借阅记录
     */
    List<BorrowRecord> getBookBorrowStatus(String bookId);
    
    /**
     * 查询读者的当前借阅清单
     * @param readerId 读者编号
     * @return 该读者未归还的借阅记录列表
     */
    List<BorrowRecord> getReaderCurrentBorrowings(String readerId);
}
