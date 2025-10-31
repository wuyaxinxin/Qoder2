// 始终生效
// 模型决策

package library.repository;

import library.model.Reader;
import java.util.List;
import java.util.Optional;

/**
 * 读者数据访问接口
 * 定义读者数据的基本操作
 */
public interface ReaderRepository {
    
    /**
     * 添加读者
     * @param reader 读者对象
     * @return true表示添加成功，false表示读者编号已存在
     */
    boolean add(Reader reader);
    
    /**
     * 根据读者编号删除读者
     * @param readerId 读者编号
     * @return true表示删除成功，false表示读者不存在
     */
    boolean delete(String readerId);
    
    /**
     * 更新读者信息
     * @param reader 读者对象
     * @return true表示更新成功，false表示读者不存在
     */
    boolean update(Reader reader);
    
    /**
     * 根据读者编号查询读者
     * @param readerId 读者编号
     * @return Optional包装的读者对象
     */
    Optional<Reader> findById(String readerId);
    
    /**
     * 查询所有读者
     * @return 所有读者的列表
     */
    List<Reader> findAll();
    
    /**
     * 根据姓名搜索读者（模糊查询）
     * @param name 姓名关键词
     * @return 匹配的读者列表
     */
    List<Reader> findByName(String name);
    
    /**
     * 检查读者编号是否存在
     * @param readerId 读者编号
     * @return true表示存在，false表示不存在
     */
    boolean exists(String readerId);
    
    /**
     * 获取读者总数
     * @return 读者总数
     */
    int count();
}
