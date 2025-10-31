// 始终生效
// 模型决策

package library.model;

/**
 * 读者实体类
 * 表示图书馆的读者信息
 */
public class Reader {
    private String readerId;         // 读者编号（唯一标识）
    private String name;             // 姓名
    private String phone;            // 联系电话
    private String email;            // 电子邮箱
    private int currentBorrowCount;  // 当前借阅数量
    private int maxBorrowLimit;      // 最大借阅数量限制
    
    /**
     * 无参构造函数
     */
    public Reader() {
        this.maxBorrowLimit = 5;  // 默认最大借阅数为5本
    }
    
    /**
     * 全参构造函数
     */
    public Reader(String readerId, String name, String phone, String email, 
                  int currentBorrowCount, int maxBorrowLimit) {
        this.readerId = readerId;
        this.name = name;
        this.phone = phone;
        this.email = email;
        this.currentBorrowCount = currentBorrowCount;
        this.maxBorrowLimit = maxBorrowLimit;
    }
    
    /**
     * 简化构造函数（必填字段）
     */
    public Reader(String readerId, String name, String phone) {
        this.readerId = readerId;
        this.name = name;
        this.phone = phone;
        this.currentBorrowCount = 0;
        this.maxBorrowLimit = 5;  // 默认最大借阅数为5本
    }
    
    // Getter 和 Setter 方法
    
    public String getReaderId() {
        return readerId;
    }
    
    public void setReaderId(String readerId) {
        this.readerId = readerId;
    }
    
    public String getName() {
        return name;
    }
    
    public void setName(String name) {
        this.name = name;
    }
    
    public String getPhone() {
        return phone;
    }
    
    public void setPhone(String phone) {
        this.phone = phone;
    }
    
    public String getEmail() {
        return email;
    }
    
    public void setEmail(String email) {
        this.email = email;
    }
    
    public int getCurrentBorrowCount() {
        return currentBorrowCount;
    }
    
    public void setCurrentBorrowCount(int currentBorrowCount) {
        this.currentBorrowCount = currentBorrowCount;
    }
    
    public int getMaxBorrowLimit() {
        return maxBorrowLimit;
    }
    
    public void setMaxBorrowLimit(int maxBorrowLimit) {
        this.maxBorrowLimit = maxBorrowLimit;
    }
    
    /**
     * 判断读者是否可以继续借阅
     * @return true表示可以借阅，false表示已达到借阅上限
     */
    public boolean canBorrow() {
        return currentBorrowCount < maxBorrowLimit;
    }
    
    /**
     * 借出图书（当前借阅数加1）
     */
    public void borrowBook() {
        if (canBorrow()) {
            currentBorrowCount++;
        }
    }
    
    /**
     * 归还图书（当前借阅数减1）
     */
    public void returnBook() {
        if (currentBorrowCount > 0) {
            currentBorrowCount--;
        }
    }
    
    @Override
    public String toString() {
        return "读者编号: " + readerId + "\n" +
               "姓名: " + name + "\n" +
               "联系电话: " + phone + "\n" +
               "邮箱: " + (email != null ? email : "无") + "\n" +
               "当前借阅数: " + currentBorrowCount + "\n" +
               "最大借阅限制: " + maxBorrowLimit + "\n" +
               "可借阅状态: " + (canBorrow() ? "可借阅" : "已达上限");
    }
}
