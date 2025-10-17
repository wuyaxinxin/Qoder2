/**
 * PersonManager - 人员管理系统
 * 这是一个简单的Java类,演示了面向对象编程的基本概念
 */
public class PersonManager {
    // 私有属性
    private String name;
    private int age;
    private String email;
    
    // 构造函数
    public PersonManager(String name, int age, String email) {
        this.name = name;
        this.age = age;
        this.email = email;
    }
    
    // Getter方法
    public String getName() {
        return name;
    }
    
    public int getAge() {
        return age;
    }
    
    public String getEmail() {
        return email;
    }
    
    // Setter方法
    public void setName(String name) {
        this.name = name;
    }
    
    public void setAge(int age) {
        if (age > 0 && age < 150) {
            this.age = age;
        } else {
            System.out.println("年龄设置无效!");
        }
    }
    
    public void setEmail(String email) {
        this.email = email;
    }
    
    // 业务方法
    public void displayInfo() {
        System.out.println("====== 人员信息 ======");
        System.out.println("姓名: " + name);
        System.out.println("年龄: " + age);
        System.out.println("邮箱: " + email);
        System.out.println("=====================");
    }
    
    public boolean isAdult() {
        return age >= 18;
    }
    
    // 主方法 - 程序入口
    public static void main(String[] args) {
        // 创建PersonManager对象
        PersonManager person1 = new PersonManager("张三", 25, "zhangsan@example.com");
        PersonManager person2 = new PersonManager("李四", 17, "lisi@example.com");
        
        // 显示信息
        person1.displayInfo();
        System.out.println("是否成年: " + (person1.isAdult() ? "是" : "否"));
        System.out.println();
        
        person2.displayInfo();
        System.out.println("是否成年: " + (person2.isAdult() ? "是" : "否"));
        System.out.println();
        
        // 修改信息
        person1.setAge(30);
        person1.setEmail("zhangsan_new@example.com");
        System.out.println("更新后的信息:");
        person1.displayInfo();
    }
}
