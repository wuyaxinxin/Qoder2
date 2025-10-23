import java.util.ArrayList;
import java.util.List;

/**
 * Student 类
 * 
 * 用于表示学生信息的Java类，包含学生的基本属性和操作方法
 * 支持学生信息的管理和成绩计算功能
 * 
 * @author Qoder
 * @version 1.0
 */
public class Student {
    // 私有属性
    private String studentId;
    private String name;
    private int age;
    private String major;
    private List<Double> scores;
    
    /**
     * 无参构造方法
     */
    public Student() {
        this.scores = new ArrayList<>();
    }
    
    /**
     * 带参数的构造方法
     * 
     * @param studentId 学生ID
     * @param name 学生姓名
     * @param age 学生年龄
     * @param major 专业
     */
    public Student(String studentId, String name, int age, String major) {
        this.studentId = studentId;
        this.name = name;
        this.age = age;
        this.major = major;
        this.scores = new ArrayList<>();
    }
    
    // Getter 和 Setter 方法
    public String getStudentId() {
        return studentId;
    }
    
    public void setStudentId(String studentId) {
        this.studentId = studentId;
    }
    
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
        if (age > 0 && age < 150) {
            this.age = age;
        } else {
            throw new IllegalArgumentException("年龄必须在1到150之间");
        }
    }
    
    public String getMajor() {
        return major;
    }
    
    public void setMajor(String major) {
        this.major = major;
    }
    
    public List<Double> getScores() {
        return new ArrayList<>(scores);
    }
    
    /**
     * 添加成绩
     * 
     * @param score 成绩分数
     */
    public void addScore(double score) {
        if (score >= 0 && score <= 100) {
            this.scores.add(score);
        } else {
            throw new IllegalArgumentException("成绩必须在0到100之间");
        }
    }
    
    /**
     * 计算平均成绩
     * 
     * @return 平均成绩，如果没有成绩则返回0.0
     */
    public double calculateAverageScore() {
        if (scores.isEmpty()) {
            return 0.0;
        }
        
        double sum = 0;
        for (double score : scores) {
            sum += score;
        }
        return sum / scores.size();
    }
    
    /**
     * 获取最高成绩
     * 
     * @return 最高成绩，如果没有成绩则返回0.0
     */
    public double getMaxScore() {
        if (scores.isEmpty()) {
            return 0.0;
        }
        
        double max = scores.get(0);
        for (double score : scores) {
            if (score > max) {
                max = score;
            }
        }
        return max;
    }
    
    /**
     * 获取最低成绩
     * 
     * @return 最低成绩，如果没有成绩则返回0.0
     */
    public double getMinScore() {
        if (scores.isEmpty()) {
            return 0.0;
        }
        
        double min = scores.get(0);
        for (double score : scores) {
            if (score < min) {
                min = score;
            }
        }
        return min;
    }
    
    /**
     * 显示学生完整信息
     */
    public void displayInfo() {
        System.out.println("====== 学生信息 ======");
        System.out.println("学号: " + studentId);
        System.out.println("姓名: " + name);
        System.out.println("年龄: " + age);
        System.out.println("专业: " + major);
        System.out.println("成绩列表: " + scores);
        System.out.println("平均成绩: " + String.format("%.2f", calculateAverageScore()));
        System.out.println("最高成绩: " + getMaxScore());
        System.out.println("最低成绩: " + getMinScore());
        System.out.println("=====================");
    }
    
    @Override
    public String toString() {
        return "Student{" +
                "studentId='" + studentId + '\'' +
                ", name='" + name + '\'' +
                ", age=" + age +
                ", major='" + major + '\'' +
                ", averageScore=" + String.format("%.2f", calculateAverageScore()) +
                '}';
    }
    
    /**
     * 主方法：演示Student类的使用
     * 
     * @param args 命令行参数
     */
    public static void main(String[] args) {
        // 创建学生对象
        Student student1 = new Student("2024001", "张三", 20, "计算机科学");
        
        // 添加成绩
        student1.addScore(85.5);
        student1.addScore(92.0);
        student1.addScore(78.5);
        student1.addScore(88.0);
        
        // 显示学生信息
        student1.displayInfo();
        
        System.out.println();
        
        // 创建第二个学生对象
        Student student2 = new Student("2024002", "李四", 21, "软件工程");
        student2.addScore(95.0);
        student2.addScore(89.5);
        student2.addScore(91.0);
        
        // 显示学生信息
        student2.displayInfo();
        
        // 使用toString方法
        System.out.println("\n简要信息:");
        System.out.println(student1);
        System.out.println(student2);
    }
}
