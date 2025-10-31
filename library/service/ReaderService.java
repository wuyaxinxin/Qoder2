// 始终生效
// 模型决策

package library.service;

import library.model.Reader;
import library.model.BorrowRecord;
import java.util.List;

/**
 * 读者管理服务接口
 * 定义读者管理的业务操作
 */
public interface ReaderService {
    
    /**
     * 注册读者
     * @param reader 读者对象
     * @return 操作结果消息
     */
    String registerReader(Reader reader);
    
    /**
     * 删除读者
     * @param readerId 读者编号
     * @return 操作结果消息
     */
    String deleteReader(String readerId);
    
    /**
     * 更新读者信息
     * @param reader 读者对象
     * @return 操作结果消息
     */
    String updateReader(Reader reader);
    
    /**
     * 查询读者
     * @param readerId 读者编号
     * @return 读者对象，如果不存在返回null
     */
    Reader getReader(String readerId);
    
    /**
     * 列出所有读者
     * @return 所有读者的列表
     */
    List<Reader> listAllReaders();
    
    /**
     * 按姓名搜索读者
     * @param name 姓名关键词
     * @return 匹配的读者列表
     */
    List<Reader> searchByName(String name);
    
    /**
     * 查询读者的借阅历史
     * @param readerId 读者编号
     * @return 借阅记录列表
     */
    List<BorrowRecord> getReaderBorrowHistory(String readerId);
}
