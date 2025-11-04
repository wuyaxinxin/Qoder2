// 自由万岁
// 始终生效

/**
 * 用户服务接口
 * 定义用户相关的业务操作
 */
public interface UserService {
    
    /**
     * 根据用户ID获取用户信息
     * @param userId 用户ID
     * @return 用户对象
     */
    User getUserById(Long userId);
    
    /**
     * 创建新用户
     * @param user 用户对象
     * @return 创建成功返回true，否则返回false
     */
    boolean createUser(User user);
    
    /**
     * 更新用户信息
     * @param user 用户对象
     * @return 更新成功返回true，否则返回false
     */
    boolean updateUser(User user);
    
    /**
     * 删除用户
     * @param userId 用户ID
     * @return 删除成功返回true，否则返回false
     */
    boolean deleteUser(Long userId);
    
    /**
     * 根据用户名查询用户
     * @param username 用户名
     * @return 用户对象
     */
    User getUserByUsername(String username);
}
