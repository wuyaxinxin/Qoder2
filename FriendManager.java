import java.util.*;
import java.time.LocalDate;
import java.time.Period;
import java.time.format.DateTimeFormatter;

/**
 * 朋友管理系统类
 * 用于管理朋友信息的核心业务逻辑类
 * 提供朋友信息的增删改查等基本功能
 * 
 * @author Qoder
 * @version 1.0
 * @since 2025-10-17
 */
public class FriendManager {
    
    // 朋友信息存储容器，使用HashMap存储，key为朋友ID，value为朋友对象
    private Map<String, Friend> friendMap;
    
    // 日期格式化工具，用于处理生日日期
    private static final DateTimeFormatter DATE_FORMATTER = DateTimeFormatter.ofPattern("yyyy-MM-dd");
    
    /**
     * 构造方法
     * 初始化朋友管理器，创建空的朋友信息存储容器
     */
    public FriendManager() {
        // 使用HashMap初始化朋友信息存储容器
        this.friendMap = new HashMap<>();
    }
    
    /**
     * 添加新朋友
     * 将新朋友信息添加到系统中
     * 
     * @param friendId 朋友唯一标识ID
     * @param name 朋友姓名
     * @param phone 联系电话
     * @param birthday 生日（格式：yyyy-MM-dd）
     * @param address 地址信息
     * @param notes 备注信息
     * @return 添加成功返回true，如果ID已存在返回false
     */
    public boolean addFriend(String friendId, String name, String phone, 
                           String birthday, String address, String notes) {
        // 检查朋友ID是否已存在，避免重复添加
        if (friendMap.containsKey(friendId)) {
            // 如果ID已存在，打印错误信息并返回false
            System.out.println("错误：朋友ID " + friendId + " 已存在！");
            return false;
        }
        
        // 创建新的朋友对象
        Friend newFriend = new Friend(friendId, name, phone, birthday, address, notes);
        
        // 将新朋友添加到存储容器中
        friendMap.put(friendId, newFriend);
        
        // 打印成功添加的提示信息
        System.out.println("成功添加朋友：" + name + "（ID：" + friendId + "）");
        
        // 返回true表示添加成功
        return true;
    }
    
    /**
     * 删除朋友
     * 根据朋友ID从系统中删除朋友信息
     * 
     * @param friendId 要删除的朋友ID
     * @return 删除成功返回true，如果ID不存在返回false
     */
    public boolean deleteFriend(String friendId) {
        // 检查朋友是否存在
        if (!friendMap.containsKey(friendId)) {
            // 如果朋友不存在，打印错误信息并返回false
            System.out.println("错误：找不到ID为 " + friendId + " 的朋友！");
            return false;
        }
        
        // 获取朋友姓名用于提示信息
        String friendName = friendMap.get(friendId).getName();
        
        // 从存储容器中删除朋友
        friendMap.remove(friendId);
        
        // 打印成功删除的提示信息
        System.out.println("成功删除朋友：" + friendName + "（ID：" + friendId + "）");
        
        // 返回true表示删除成功
        return true;
    }
    
    /**
     * 更新朋友信息
     * 更新指定ID朋友的基本信息
     * 
     * @param friendId 朋友ID
     * @param name 新姓名（如果为null则不更新）
     * @param phone 新电话（如果为null则不更新）
     * @param birthday 新生日（如果为null则不更新）
     * @param address 新地址（如果为null则不更新）
     * @param notes 新备注（如果为null则不更新）
     * @return 更新成功返回true，如果朋友不存在返回false
     */
    public boolean updateFriend(String friendId, String name, String phone,
                              String birthday, String address, String notes) {
        // 获取要更新的朋友对象
        Friend friend = friendMap.get(friendId);
        
        // 检查朋友是否存在
        if (friend == null) {
            // 如果朋友不存在，打印错误信息并返回false
            System.out.println("错误：找不到ID为 " + friendId + " 的朋友！");
            return false;
        }
        
        // 更新姓名（如果提供了新值）
        if (name != null && !name.isEmpty()) {
            friend.setName(name);
        }
        
        // 更新电话（如果提供了新值）
        if (phone != null && !phone.isEmpty()) {
            friend.setPhone(phone);
        }
        
        // 更新生日（如果提供了新值）
        if (birthday != null && !birthday.isEmpty()) {
            friend.setBirthday(birthday);
        }
        
        // 更新地址（如果提供了新值）
        if (address != null && !address.isEmpty()) {
            friend.setAddress(address);
        }
        
        // 更新备注（如果提供了新值）
        if (notes != null && !notes.isEmpty()) {
            friend.setNotes(notes);
        }
        
        // 打印成功更新的提示信息
        System.out.println("成功更新朋友信息（ID：" + friendId + "）");
        
        // 返回true表示更新成功
        return true;
    }
    
    /**
     * 获取朋友信息
     * 根据朋友ID获取朋友对象
     * 
     * @param friendId 朋友ID
     * @return 朋友对象，如果不存在返回null
     */
    public Friend getFriend(String friendId) {
        // 从存储容器中获取并返回朋友对象
        return friendMap.get(friendId);
    }
    
    /**
     * 搜索朋友
     * 根据关键词在姓名和备注中进行模糊搜索
     * 
     * @param keyword 搜索关键词
     * @return 匹配的朋友列表
     */
    public List<Friend> searchFriends(String keyword) {
        // 创建结果列表
        List<Friend> results = new ArrayList<>();
        
        // 将关键词转换为小写，实现不区分大小写的搜索
        String lowerKeyword = keyword.toLowerCase();
        
        // 遍历所有朋友
        for (Friend friend : friendMap.values()) {
            // 检查姓名是否包含关键词
            boolean nameMatch = friend.getName().toLowerCase().contains(lowerKeyword);
            
            // 检查备注是否包含关键词
            boolean notesMatch = friend.getNotes() != null && 
                                friend.getNotes().toLowerCase().contains(lowerKeyword);
            
            // 如果姓名或备注匹配，添加到结果列表
            if (nameMatch || notesMatch) {
                results.add(friend);
            }
        }
        
        // 返回搜索结果列表
        return results;
    }
    
    /**
     * 获取所有朋友
     * 返回系统中所有朋友的列表
     * 
     * @return 所有朋友的列表
     */
    public List<Friend> getAllFriends() {
        // 将Map中的所有朋友对象转换为列表并返回
        return new ArrayList<>(friendMap.values());
    }
    
    /**
     * 获取生日提醒
     * 获取指定月份生日的朋友列表
     * 
     * @param month 月份（1-12），如果为0则使用当前月份
     * @return 该月份生日的朋友列表
     */
    public List<Friend> getBirthdayFriends(int month) {
        // 如果月份为0，使用当前月份
        if (month == 0) {
            month = LocalDate.now().getMonthValue();
        }
        
        // 创建结果列表
        List<Friend> birthdayFriends = new ArrayList<>();
        
        // 遍历所有朋友
        for (Friend friend : friendMap.values()) {
            // 检查朋友是否有生日信息
            if (friend.getBirthday() != null && !friend.getBirthday().isEmpty()) {
                try {
                    // 解析生日日期
                    LocalDate birthDate = LocalDate.parse(friend.getBirthday(), DATE_FORMATTER);
                    
                    // 检查生日月份是否匹配
                    if (birthDate.getMonthValue() == month) {
                        // 如果匹配，添加到结果列表
                        birthdayFriends.add(friend);
                    }
                } catch (Exception e) {
                    // 日期格式错误，跳过该朋友
                    continue;
                }
            }
        }
        
        // 返回生日朋友列表
        return birthdayFriends;
    }
    
    /**
     * 获取统计信息
     * 返回系统中朋友信息的统计数据
     * 
     * @return 包含统计信息的字符串
     */
    public String getStatistics() {
        // 获取朋友总数
        int totalFriends = friendMap.size();
        
        // 统计有生日信息的朋友数量
        int withBirthday = 0;
        for (Friend friend : friendMap.values()) {
            if (friend.getBirthday() != null && !friend.getBirthday().isEmpty()) {
                withBirthday++;
            }
        }
        
        // 统计有地址信息的朋友数量
        int withAddress = 0;
        for (Friend friend : friendMap.values()) {
            if (friend.getAddress() != null && !friend.getAddress().isEmpty()) {
                withAddress++;
            }
        }
        
        // 获取本月生日的朋友数量
        int birthdayThisMonth = getBirthdayFriends(0).size();
        
        // 构建统计信息字符串
        StringBuilder stats = new StringBuilder();
        stats.append("=== 统计信息 ===\n");
        stats.append("总朋友数：").append(totalFriends).append("\n");
        stats.append("有生日信息：").append(withBirthday).append("\n");
        stats.append("有地址信息：").append(withAddress).append("\n");
        stats.append("本月生日：").append(birthdayThisMonth).append("\n");
        stats.append("================");
        
        // 返回统计信息字符串
        return stats.toString();
    }
    
    /**
     * 朋友内部类
     * 表示一个朋友的完整信息
     */
    public static class Friend {
        // 朋友唯一标识ID
        private String friendId;
        
        // 朋友姓名
        private String name;
        
        // 联系电话
        private String phone;
        
        // 生日（格式：yyyy-MM-dd）
        private String birthday;
        
        // 地址信息
        private String address;
        
        // 备注信息
        private String notes;
        
        /**
         * 构造方法
         * 创建一个新的朋友对象
         * 
         * @param friendId 朋友ID
         * @param name 姓名
         * @param phone 电话
         * @param birthday 生日
         * @param address 地址
         * @param notes 备注
         */
        public Friend(String friendId, String name, String phone, 
                     String birthday, String address, String notes) {
            // 初始化朋友ID
            this.friendId = friendId;
            
            // 初始化姓名
            this.name = name;
            
            // 初始化电话
            this.phone = phone;
            
            // 初始化生日
            this.birthday = birthday;
            
            // 初始化地址
            this.address = address;
            
            // 初始化备注
            this.notes = notes;
        }
        
        /**
         * 计算年龄
         * 根据生日计算朋友的当前年龄
         * 
         * @return 年龄，如果没有生日信息返回-1
         */
        public int getAge() {
            // 检查是否有生日信息
            if (birthday == null || birthday.isEmpty()) {
                // 没有生日信息，返回-1
                return -1;
            }
            
            try {
                // 解析生日日期
                LocalDate birthDate = LocalDate.parse(birthday, DATE_FORMATTER);
                
                // 获取当前日期
                LocalDate now = LocalDate.now();
                
                // 计算年龄差
                Period period = Period.between(birthDate, now);
                
                // 返回年龄
                return period.getYears();
            } catch (Exception e) {
                // 日期格式错误，返回-1
                return -1;
            }
        }
        
        // Getter方法：获取朋友ID
        public String getFriendId() {
            return friendId;
        }
        
        // Setter方法：设置朋友ID
        public void setFriendId(String friendId) {
            this.friendId = friendId;
        }
        
        // Getter方法：获取姓名
        public String getName() {
            return name;
        }
        
        // Setter方法：设置姓名
        public void setName(String name) {
            this.name = name;
        }
        
        // Getter方法：获取电话
        public String getPhone() {
            return phone;
        }
        
        // Setter方法：设置电话
        public void setPhone(String phone) {
            this.phone = phone;
        }
        
        // Getter方法：获取生日
        public String getBirthday() {
            return birthday;
        }
        
        // Setter方法：设置生日
        public void setBirthday(String birthday) {
            this.birthday = birthday;
        }
        
        // Getter方法：获取地址
        public String getAddress() {
            return address;
        }
        
        // Setter方法：设置地址
        public void setAddress(String address) {
            this.address = address;
        }
        
        // Getter方法：获取备注
        public String getNotes() {
            return notes;
        }
        
        // Setter方法：设置备注
        public void setNotes(String notes) {
            this.notes = notes;
        }
        
        /**
         * 返回朋友信息的字符串表示
         * 
         * @return 格式化的朋友信息
         */
        @Override
        public String toString() {
            // 构建朋友信息字符串
            StringBuilder sb = new StringBuilder();
            sb.append("朋友ID：").append(friendId).append("\n");
            sb.append("姓名：").append(name);
            
            // 如果有年龄信息，显示年龄
            int age = getAge();
            if (age >= 0) {
                sb.append("（").append(age).append("岁）");
            }
            sb.append("\n");
            
            sb.append("电话：").append(phone).append("\n");
            sb.append("生日：").append(birthday != null ? birthday : "未设置").append("\n");
            sb.append("地址：").append(address != null ? address : "未设置").append("\n");
            sb.append("备注：").append(notes != null ? notes : "无");
            
            // 返回字符串
            return sb.toString();
        }
    }
    
    /**
     * 主方法
     * 用于演示朋友管理系统的基本功能
     * 
     * @param args 命令行参数
     */
    public static void main(String[] args) {
        // 打印演示标题
        System.out.println("=== 朋友管理系统演示 ===\n");
        
        // 创建朋友管理器实例
        FriendManager manager = new FriendManager();
        
        // 演示添加朋友功能
        System.out.println("1. 添加朋友：");
        manager.addFriend("F001", "张三", "13800138000", "1995-05-20", "北京市朝阳区", "大学同学");
        manager.addFriend("F002", "李四", "13900139000", "1996-03-15", "上海市浦东新区", "工作伙伴");
        manager.addFriend("F003", "王五", "13700137000", "1995-05-25", null, null);
        System.out.println();
        
        // 演示获取所有朋友功能
        System.out.println("2. 所有朋友：");
        for (Friend friend : manager.getAllFriends()) {
            System.out.println("  - " + friend.getName() + "（" + friend.getFriendId() + "）");
        }
        System.out.println();
        
        // 演示搜索功能
        System.out.println("3. 搜索'同学'：");
        List<Friend> results = manager.searchFriends("同学");
        for (Friend friend : results) {
            System.out.println("  - " + friend.getName() + "：" + friend.getNotes());
        }
        System.out.println();
        
        // 演示统计信息功能
        System.out.println("4. 统计信息：");
        System.out.println(manager.getStatistics());
        System.out.println();
        
        // 演示查看朋友详细信息
        System.out.println("5. 查看朋友详细信息（F001）：");
        Friend friend = manager.getFriend("F001");
        if (friend != null) {
            System.out.println(friend);
        }
    }
}
