// 始终生效
// 模型决策

package library.repository;

import library.model.Book;
import java.util.List;
import java.util.Optional;

/**
 * 图书数据访问接口
 * 定义图书数据的基本操作
 */
public interface BookRepository {
    
    /**
     * 添加图书
     * @param book 图书对象
     * @return true表示添加成功，false表示图书编号已存在
     */
    boolean add(Book book);
    
    /**
     * 根据图书编号删除图书
     * @param bookId 图书编号
     * @return true表示删除成功，false表示图书不存在
     */
    boolean delete(String bookId);
    
    /**
     * 更新图书信息
     * @param book 图书对象
     * @return true表示更新成功，false表示图书不存在
     */
    boolean update(Book book);
    
    /**
     * 根据图书编号查询图书
     * @param bookId 图书编号
     * @return Optional包装的图书对象
     */
    Optional<Book> findById(String bookId);
    
    /**
     * 查询所有图书
     * @return 所有图书的列表
     */
    List<Book> findAll();
    
    /**
     * 根据书名搜索图书（模糊查询）
     * @param title 书名关键词
     * @return 匹配的图书列表
     */
    List<Book> findByTitle(String title);
    
    /**
     * 根据作者搜索图书（模糊查询）
     * @param author 作者关键词
     * @return 匹配的图书列表
     */
    List<Book> findByAuthor(String author);
    
    /**
     * 检查图书编号是否存在
     * @param bookId 图书编号
     * @return true表示存在，false表示不存在
     */
    boolean exists(String bookId);
    
    /**
     * 获取图书总数
     * @return 图书总数
     */
    int count();
}
