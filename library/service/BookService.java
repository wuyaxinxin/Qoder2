// 始终生效
// 模型决策

package library.service;

import library.model.Book;
import java.util.List;

/**
 * 图书管理服务接口
 * 定义图书管理的业务操作
 */
public interface BookService {
    
    /**
     * 添加图书
     * @param book 图书对象
     * @return 操作结果消息
     */
    String addBook(Book book);
    
    /**
     * 删除图书
     * @param bookId 图书编号
     * @return 操作结果消息
     */
    String deleteBook(String bookId);
    
    /**
     * 更新图书信息
     * @param book 图书对象
     * @return 操作结果消息
     */
    String updateBook(Book book);
    
    /**
     * 查询图书
     * @param bookId 图书编号
     * @return 图书对象，如果不存在返回null
     */
    Book getBook(String bookId);
    
    /**
     * 列出所有图书
     * @return 所有图书的列表
     */
    List<Book> listAllBooks();
    
    /**
     * 按书名搜索图书
     * @param title 书名关键词
     * @return 匹配的图书列表
     */
    List<Book> searchByTitle(String title);
    
    /**
     * 按作者搜索图书
     * @param author 作者关键词
     * @return 匹配的图书列表
     */
    List<Book> searchByAuthor(String author);
    
    /**
     * 获取可借阅的图书列表
     * @return 有库存的图书列表
     */
    List<Book> getAvailableBooks();
}
