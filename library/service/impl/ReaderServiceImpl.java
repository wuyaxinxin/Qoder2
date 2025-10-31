// 始终生效
// 模型决策

package library.service.impl;

import library.model.Reader;
import library.model.BorrowRecord;
import library.repository.ReaderRepository;
import library.repository.BorrowRecordRepository;
import library.service.ReaderService;
import java.util.List;

/**
 * 读者管理服务实现类
 * 实现读者管理的业务逻辑
 */
public class ReaderServiceImpl implements ReaderService {
    
    private final ReaderRepository readerRepository;
    private final BorrowRecordRepository borrowRecordRepository;
    
    /**
     * 构造函数
     * @param readerRepository 读者数据访问对象
     * @param borrowRecordRepository 借阅记录数据访问对象
     */
    public ReaderServiceImpl(ReaderRepository readerRepository,
                            BorrowRecordRepository borrowRecordRepository) {
        this.readerRepository = readerRepository;
        this.borrowRecordRepository = borrowRecordRepository;
    }
    
    @Override
    public String registerReader(Reader reader) {
        // 数据验证
        if (reader == null) {
            return "注册失败：读者信息不能为空";
        }
        
        if (reader.getReaderId() == null || reader.getReaderId().trim().isEmpty()) {
            return "注册失败：读者编号不能为空";
        }
        
        if (reader.getName() == null || reader.getName().trim().isEmpty()) {
            return "注册失败：姓名不能为空";
        }
        
        if (reader.getPhone() == null || reader.getPhone().trim().isEmpty()) {
            return "注册失败：联系电话不能为空";
        }
        
        // 简单的电话格式验证
        if (!reader.getPhone().matches("\\d{11}")) {
            return "注册失败：联系电话格式不正确（应为11位数字）";
        }
        
        // 注册读者
        boolean success = readerRepository.add(reader);
        if (success) {
            return "注册成功：读者 " + reader.getName() + " 已成功注册，编号为 " + reader.getReaderId();
        } else {
            return "注册失败：读者编号 " + reader.getReaderId() + " 已存在";
        }
    }
    
    @Override
    public String deleteReader(String readerId) {
        if (readerId == null || readerId.trim().isEmpty()) {
            return "删除失败：读者编号不能为空";
        }
        
        // 检查读者是否存在
        Reader reader = readerRepository.findById(readerId).orElse(null);
        if (reader == null) {
            return "删除失败：读者编号 " + readerId + " 不存在";
        }
        
        // 检查是否有未归还的图书
        List<BorrowRecord> borrowingRecords = 
            borrowRecordRepository.findBorrowingByReaderId(readerId);
        if (!borrowingRecords.isEmpty()) {
            return "删除失败：该读者还有 " + borrowingRecords.size() + " 本图书未归还，无法删除";
        }
        
        // 删除读者
        boolean success = readerRepository.delete(readerId);
        if (success) {
            return "删除成功：读者 " + reader.getName() + " 已从系统中删除";
        } else {
            return "删除失败：未知错误";
        }
    }
    
    @Override
    public String updateReader(Reader reader) {
        if (reader == null) {
            return "更新失败：读者信息不能为空";
        }
        
        if (reader.getReaderId() == null || reader.getReaderId().trim().isEmpty()) {
            return "更新失败：读者编号不能为空";
        }
        
        // 检查读者是否存在
        if (!readerRepository.exists(reader.getReaderId())) {
            return "更新失败：读者编号 " + reader.getReaderId() + " 不存在";
        }
        
        // 数据验证
        if (reader.getName() != null && reader.getName().trim().isEmpty()) {
            return "更新失败：姓名不能为空";
        }
        
        if (reader.getPhone() != null) {
            if (reader.getPhone().trim().isEmpty()) {
                return "更新失败：联系电话不能为空";
            }
            if (!reader.getPhone().matches("\\d{11}")) {
                return "更新失败：联系电话格式不正确（应为11位数字）";
            }
        }
        
        // 更新读者
        boolean success = readerRepository.update(reader);
        if (success) {
            return "更新成功：读者 " + reader.getName() + " 的信息已更新";
        } else {
            return "更新失败：未知错误";
        }
    }
    
    @Override
    public Reader getReader(String readerId) {
        if (readerId == null || readerId.trim().isEmpty()) {
            return null;
        }
        
        return readerRepository.findById(readerId).orElse(null);
    }
    
    @Override
    public List<Reader> listAllReaders() {
        return readerRepository.findAll();
    }
    
    @Override
    public List<Reader> searchByName(String name) {
        if (name == null || name.trim().isEmpty()) {
            return List.of();
        }
        
        return readerRepository.findByName(name);
    }
    
    @Override
    public List<BorrowRecord> getReaderBorrowHistory(String readerId) {
        if (readerId == null || readerId.trim().isEmpty()) {
            return List.of();
        }
        
        return borrowRecordRepository.findByReaderId(readerId);
    }
}
