// 始终生效
// 模型决策

package library.repository.impl;

import library.model.BorrowRecord;
import library.model.BorrowRecord.RecordStatus;
import library.repository.BorrowRecordRepository;
import java.util.*;
import java.util.stream.Collectors;

/**
 * 借阅记录数据访问实现类
 * 使用内存HashMap存储借阅记录数据
 */
public class BorrowRecordRepositoryImpl implements BorrowRecordRepository {
    
    // 使用HashMap存储借阅记录数据，key为记录编号，value为借阅记录对象
    private final Map<String, BorrowRecord> recordStorage = new HashMap<>();
    
    @Override
    public boolean add(BorrowRecord record) {
        if (record == null || record.getRecordId() == null) {
            return false;
        }
        
        // 检查记录编号是否已存在
        if (recordStorage.containsKey(record.getRecordId())) {
            return false;
        }
        
        recordStorage.put(record.getRecordId(), record);
        return true;
    }
    
    @Override
    public boolean update(BorrowRecord record) {
        if (record == null || record.getRecordId() == null) {
            return false;
        }
        
        // 检查记录是否存在
        if (!recordStorage.containsKey(record.getRecordId())) {
            return false;
        }
        
        recordStorage.put(record.getRecordId(), record);
        return true;
    }
    
    @Override
    public Optional<BorrowRecord> findById(String recordId) {
        if (recordId == null) {
            return Optional.empty();
        }
        
        return Optional.ofNullable(recordStorage.get(recordId));
    }
    
    @Override
    public List<BorrowRecord> findAll() {
        return new ArrayList<>(recordStorage.values());
    }
    
    @Override
    public List<BorrowRecord> findByReaderId(String readerId) {
        if (readerId == null) {
            return new ArrayList<>();
        }
        
        return recordStorage.values().stream()
                .filter(record -> readerId.equals(record.getReaderId()))
                .collect(Collectors.toList());
    }
    
    @Override
    public List<BorrowRecord> findByBookId(String bookId) {
        if (bookId == null) {
            return new ArrayList<>();
        }
        
        return recordStorage.values().stream()
                .filter(record -> bookId.equals(record.getBookId()))
                .collect(Collectors.toList());
    }
    
    @Override
    public List<BorrowRecord> findAllBorrowing() {
        return recordStorage.values().stream()
                .filter(record -> record.getStatus() == RecordStatus.BORROWING)
                .collect(Collectors.toList());
    }
    
    @Override
    public Optional<BorrowRecord> findBorrowingRecord(String readerId, String bookId) {
        if (readerId == null || bookId == null) {
            return Optional.empty();
        }
        
        return recordStorage.values().stream()
                .filter(record -> readerId.equals(record.getReaderId()) 
                        && bookId.equals(record.getBookId())
                        && record.getStatus() == RecordStatus.BORROWING)
                .findFirst();
    }
    
    @Override
    public List<BorrowRecord> findBorrowingByReaderId(String readerId) {
        if (readerId == null) {
            return new ArrayList<>();
        }
        
        return recordStorage.values().stream()
                .filter(record -> readerId.equals(record.getReaderId())
                        && record.getStatus() == RecordStatus.BORROWING)
                .collect(Collectors.toList());
    }
    
    @Override
    public List<BorrowRecord> findBorrowingByBookId(String bookId) {
        if (bookId == null) {
            return new ArrayList<>();
        }
        
        return recordStorage.values().stream()
                .filter(record -> bookId.equals(record.getBookId())
                        && record.getStatus() == RecordStatus.BORROWING)
                .collect(Collectors.toList());
    }
    
    @Override
    public int count() {
        return recordStorage.size();
    }
}
