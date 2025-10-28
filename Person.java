/**
 * Person类 - 表示一个人的基本信息
 * 这个类包含了人的基本属性和方法
 */
public class Person {
    // 私有属性
    private String name;
    private int age;
    private String email;
    private String phone;
    
    /**
     * 默认构造函数
     */
    public Person() {
        this.name = "";
        this.age = 0;
        this.email = "";
        this.phone = "";
    }
    
    /**
     * 带参数的构造函数
     * @param name 姓名
     * @param age 年龄
     */
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
        this.email = "";
        this.phone = "";
    }
    
    /**
     * 完整的构造函数
     * @param name 姓名
     * @param age 年龄
     * @param email 电子邮件
     * @param phone 电话号码
     */
    public Person(String name, int age, String email, String phone) {
        this.name = name;
        this.age = age;
        this.email = email;
        this.phone = phone;
    }
    
    // Getter和Setter方法
    public String getName() {
        return name;
    }
    
    public void setName(String name) {
        this.name = name;
    }
    
    public int getAge() {
        return age;
    }
    
    public void setAge(int age) {
        if (age >= 0 && age <= 150) {
            this.age = age;
        } else {
            throw new IllegalArgumentException("年龄必须在0到150之间");
        }
    }
    
    public String getEmail() {
        return email;
    }
    
    public void setEmail(String email) {
        this.email = email;
    }
    
    public String getPhone() {
        return phone;
    }
    
    public void setPhone(String phone) {
        this.phone = phone;
    }
    
    /**
     * 获取人的完整信息
     * @return 格式化的字符串
     */
    public String getInfo() {
        return String.format("姓名: %s, 年龄: %d, 邮箱: %s, 电话: %s", 
                            name, age, email, phone);
    }
    
    /**
     * 判断是否为成年人
     * @return 如果年龄>=18返回true,否则返回false
     */
    public boolean isAdult() {
        return age >= 18;
    }
    
    @Override
    public String toString() {
        return "Person{" +
                "name='" + name + '\'' +
                ", age=" + age +
                ", email='" + email + '\'' +
                ", phone='" + phone + '\'' +
                '}';
    }
    
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Person person = (Person) obj;
        return age == person.age && 
               name.equals(person.name) && 
               email.equals(person.email) && 
               phone.equals(person.phone);
    }
    
    /**
     * 主方法 - 用于测试Person类
     */
    public static void main(String[] args) {
        // 创建Person对象
        Person person1 = new Person("张三", 25, "zhangsan@example.com", "13800138000");
        Person person2 = new Person("李四", 17);
        
        // 输出信息
        System.out.println("=== 人员信息测试 ===");
        System.out.println(person1.getInfo());
        System.out.println("是否成年: " + person1.isAdult());
        System.out.println();
        
        System.out.println(person2.getInfo());
        System.out.println("是否成年: " + person2.isAdult());
        System.out.println();
        
        // 修改信息
        person2.setEmail("lisi@example.com");
        person2.setPhone("13900139000");
        System.out.println("更新后的信息:");
        System.out.println(person2.toString());
    }
}
