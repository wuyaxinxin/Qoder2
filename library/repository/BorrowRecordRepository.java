// 始终生效
// 模型决策

package library.repository;

import library.model.BorrowRecord;
import java.util.List;
import java.util.Optional;

/**
 * 借阅记录数据访问接口
 * 定义借阅记录数据的基本操作
 */
public interface BorrowRecordRepository {
    
    /**
     * 添加借阅记录
     * @param record 借阅记录对象
     * @return true表示添加成功，false表示记录编号已存在
     */
    boolean add(BorrowRecord record);
    
    /**
     * 更新借阅记录
     * @param record 借阅记录对象
     * @return true表示更新成功，false表示记录不存在
     */
    boolean update(BorrowRecord record);
    
    /**
     * 根据记录编号查询借阅记录
     * @param recordId 记录编号
     * @return Optional包装的借阅记录对象
     */
    Optional<BorrowRecord> findById(String recordId);
    
    /**
     * 查询所有借阅记录
     * @return 所有借阅记录的列表
     */
    List<BorrowRecord> findAll();
    
    /**
     * 根据读者编号查询借阅记录
     * @param readerId 读者编号
     * @return 该读者的所有借阅记录
     */
    List<BorrowRecord> findByReaderId(String readerId);
    
    /**
     * 根据图书编号查询借阅记录
     * @param bookId 图书编号
     * @return 该图书的所有借阅记录
     */
    List<BorrowRecord> findByBookId(String bookId);
    
    /**
     * 查询所有未归还的借阅记录
     * @return 未归还的借阅记录列表
     */
    List<BorrowRecord> findAllBorrowing();
    
    /**
     * 根据读者编号和图书编号查询未归还的借阅记录
     * @param readerId 读者编号
     * @param bookId 图书编号
     * @return Optional包装的借阅记录对象
     */
    Optional<BorrowRecord> findBorrowingRecord(String readerId, String bookId);
    
    /**
     * 根据读者编号查询未归还的借阅记录
     * @param readerId 读者编号
     * @return 该读者未归还的借阅记录列表
     */
    List<BorrowRecord> findBorrowingByReaderId(String readerId);
    
    /**
     * 根据图书编号查询未归还的借阅记录
     * @param bookId 图书编号
     * @return 该图书未归还的借阅记录列表
     */
    List<BorrowRecord> findBorrowingByBookId(String bookId);
    
    /**
     * 获取借阅记录总数
     * @return 借阅记录总数
     */
    int count();
}
