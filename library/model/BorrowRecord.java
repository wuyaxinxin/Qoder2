// 始终生效
// 模型决策

package library.model;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

/**
 * 借阅记录实体类
 * 表示图书借阅归还的记录信息
 */
public class BorrowRecord {
    private String recordId;         // 记录编号（唯一标识）
    private String bookId;           // 图书编号
    private String readerId;         // 读者编号
    private LocalDateTime borrowDate; // 借阅日期
    private LocalDateTime dueDate;    // 应还日期
    private LocalDateTime returnDate; // 实还日期
    private RecordStatus status;      // 记录状态
    
    /**
     * 借阅记录状态枚举
     */
    public enum RecordStatus {
        BORROWING("借阅中"),
        RETURNED("已归还");
        
        private final String description;
        
        RecordStatus(String description) {
            this.description = description;
        }
        
        public String getDescription() {
            return description;
        }
    }
    
    /**
     * 无参构造函数
     */
    public BorrowRecord() {
    }
    
    /**
     * 全参构造函数
     */
    public BorrowRecord(String recordId, String bookId, String readerId,
                       LocalDateTime borrowDate, LocalDateTime dueDate,
                       LocalDateTime returnDate, RecordStatus status) {
        this.recordId = recordId;
        this.bookId = bookId;
        this.readerId = readerId;
        this.borrowDate = borrowDate;
        this.dueDate = dueDate;
        this.returnDate = returnDate;
        this.status = status;
    }
    
    /**
     * 创建新借阅记录的构造函数
     */
    public BorrowRecord(String recordId, String bookId, String readerId) {
        this.recordId = recordId;
        this.bookId = bookId;
        this.readerId = readerId;
        this.borrowDate = LocalDateTime.now();
        this.dueDate = LocalDateTime.now().plusDays(30);  // 默认30天后归还
        this.status = RecordStatus.BORROWING;
    }
    
    // Getter 和 Setter 方法
    
    public String getRecordId() {
        return recordId;
    }
    
    public void setRecordId(String recordId) {
        this.recordId = recordId;
    }
    
    public String getBookId() {
        return bookId;
    }
    
    public void setBookId(String bookId) {
        this.bookId = bookId;
    }
    
    public String getReaderId() {
        return readerId;
    }
    
    public void setReaderId(String readerId) {
        this.readerId = readerId;
    }
    
    public LocalDateTime getBorrowDate() {
        return borrowDate;
    }
    
    public void setBorrowDate(LocalDateTime borrowDate) {
        this.borrowDate = borrowDate;
    }
    
    public LocalDateTime getDueDate() {
        return dueDate;
    }
    
    public void setDueDate(LocalDateTime dueDate) {
        this.dueDate = dueDate;
    }
    
    public LocalDateTime getReturnDate() {
        return returnDate;
    }
    
    public void setReturnDate(LocalDateTime returnDate) {
        this.returnDate = returnDate;
    }
    
    public RecordStatus getStatus() {
        return status;
    }
    
    public void setStatus(RecordStatus status) {
        this.status = status;
    }
    
    /**
     * 判断是否已归还
     */
    public boolean isReturned() {
        return status == RecordStatus.RETURNED;
    }
    
    /**
     * 判断是否超期
     */
    public boolean isOverdue() {
        if (status == RecordStatus.RETURNED) {
            return false;
        }
        return LocalDateTime.now().isAfter(dueDate);
    }
    
    /**
     * 完成归还操作
     */
    public void completeReturn() {
        this.returnDate = LocalDateTime.now();
        this.status = RecordStatus.RETURNED;
    }
    
    /**
     * 格式化日期时间
     */
    private String formatDateTime(LocalDateTime dateTime) {
        if (dateTime == null) {
            return "未归还";
        }
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        return dateTime.format(formatter);
    }
    
    @Override
    public String toString() {
        return "记录编号: " + recordId + "\n" +
               "图书编号: " + bookId + "\n" +
               "读者编号: " + readerId + "\n" +
               "借阅日期: " + formatDateTime(borrowDate) + "\n" +
               "应还日期: " + formatDateTime(dueDate) + "\n" +
               "实还日期: " + formatDateTime(returnDate) + "\n" +
               "状态: " + status.getDescription() + "\n" +
               (isOverdue() && !isReturned() ? "【超期】" : "");
    }
}
