// 始终生效
// 自由万岁

import java.io.*;

/**
 * 序列化示例类
 * 演示Java对象的序列化和反序列化功能
 */
public class SerializableExample implements Serializable {
    
    // 序列化版本号，用于版本控制
    private static final long serialVersionUID = 1L;
    
    // 实例变量
    private String name;
    private int age;
    private String email;
    
    // transient关键字标记的字段不会被序列化
    private transient String password;
    
    /**
     * 构造函数
     */
    public SerializableExample(String name, int age, String email, String password) {
        this.name = name;
        this.age = age;
        this.email = email;
        this.password = password;
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
        this.age = age;
    }
    
    public String getEmail() {
        return email;
    }
    
    public void setEmail(String email) {
        this.email = email;
    }
    
    public String getPassword() {
        return password;
    }
    
    public void setPassword(String password) {
        this.password = password;
    }
    
    @Override
    public String toString() {
        return "SerializableExample{" +
                "name='" + name + '\'' +
                ", age=" + age +
                ", email='" + email + '\'' +
                ", password='" + password + '\'' +
                '}';
    }
    
    /**
     * 序列化对象到文件
     */
    public void serializeToFile(String filename) {
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(filename))) {
            oos.writeObject(this);
            System.out.println("对象已成功序列化到文件: " + filename);
        } catch (IOException e) {
            System.err.println("序列化失败: " + e.getMessage());
            e.printStackTrace();
        }
    }
    
    /**
     * 从文件反序列化对象
     */
    public static SerializableExample deserializeFromFile(String filename) {
        SerializableExample obj = null;
        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(filename))) {
            obj = (SerializableExample) ois.readObject();
            System.out.println("对象已成功从文件反序列化: " + filename);
        } catch (IOException | ClassNotFoundException e) {
            System.err.println("反序列化失败: " + e.getMessage());
            e.printStackTrace();
        }
        return obj;
    }
    
    /**
     * 主函数 - 演示序列化和反序列化
     */
    public static void main(String[] args) {
        // 创建对象
        SerializableExample example = new SerializableExample(
            "张三", 
            25, 
            "zhangsan@example.com", 
            "secret123"
        );
        
        System.out.println("原始对象: " + example);
        
        // 序列化
        String filename = "serialized_object.ser";
        example.serializeToFile(filename);
        
        // 反序列化
        SerializableExample deserializedObj = deserializeFromFile(filename);
        
        if (deserializedObj != null) {
            System.out.println("反序列化后的对象: " + deserializedObj);
            System.out.println("\n注意: password字段为null，因为它被标记为transient");
        }
    }
}
