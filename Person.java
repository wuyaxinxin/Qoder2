/*
 * 文件名: Person.java
 * 作者: 开发者
 * 创建日期: 2025-10-11
 * 版本: 1.0
 * 描述: 这是一个表示人员基本信息的Java类文件
 *       包含人员的姓名、年龄、邮箱等基本属性和相关操作方法
 * 功能:
 *   - 存储和管理人员基本信息
 *   - 提供标准的getter/setter方法
 *   - 实现年龄验证和成年人判断
 *   - 重写equals、hashCode和toString方法
 * 依赖: 无外部依赖，仅使用Java标准库
 * 修改记录:
 *   2025-10-11 - 初始版本创建
 */

/**
 * Person类 - 表示一个人的基本信息
 */
public class Person {
    private String name;
    private int age;
    private String email;
    
    /**
     * 默认构造函数
     */
    public Person() {
        this.name = "";
        this.age = 0;
        this.email = "";
    }
    
    /**
     * 带参数的构造函数
     * @param name 姓名
     * @param age 年龄
     * @param email 邮箱
     */
    public Person(String name, int age, String email) {
        this.name = name;
        this.age = age;
        this.email = email;
    }
    
    /**
     * 获取姓名
     * @return 姓名
     */
    public String getName() {
        return name;
    }
    
    /**
     * 设置姓名
     * @param name 姓名
     */
    public void setName(String name) {
        this.name = name;
    }
    
    /**
     * 获取年龄
     * @return 年龄
     */
    public int getAge() {
        return age;
    }
    
    /**
     * 设置年龄
     * @param age 年龄
     */
    public void setAge(int age) {
        if (age >= 0) {
            this.age = age;
        }
    }
    
    /**
     * 获取邮箱
     * @return 邮箱
     */
    public String getEmail() {
        return email;
    }
    
    /**
     * 设置邮箱
     * @param email 邮箱
     */
    public void setEmail(String email) {
        this.email = email;
    }
    
    /**
     * 判断是否为成年人
     * @return 如果年龄大于等于18则返回true，否则返回false
     */
    public boolean isAdult() {
        return age >= 18;
    }
    
    /**
     * 获取个人信息描述
     * @return 个人信息字符串
     */
    public String getDescription() {
        return String.format("姓名: %s, 年龄: %d, 邮箱: %s", name, age, email);
    }
    
    @Override
    public String toString() {
        return "Person{" +
                "name='" + name + '\'' +
                ", age=" + age +
                ", email='" + email + '\'' +
                '}';
    }
    
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Person person = (Person) obj;
        return age == person.age &&
                name.equals(person.name) &&
                email.equals(person.email);
    }
    
    @Override
    public int hashCode() {
        return name.hashCode() + age + email.hashCode();
    }
}