import java.util.ArrayList;
import java.util.List;

/**
 * Student 类
 * 
 * 用于表示学生信息的类，包含学生的基本属性和成绩管理功能
 * 
 * @author 七喜大人
 * @version 1.0
 */
public class Student {
    private String studentId;
    private String name;
    private int age;
    private String major;
    private List<Double> scores;

    /**
     * 构造方法
     * 
     * @param studentId 学号
     * @param name 姓名
     * @param age 年龄
     * @param major 专业
     */
    public Student(String studentId, String name, int age, String major) {
        this.studentId = studentId;
        this.name = name;
        this.age = age;
        this.major = major;
        this.scores = new ArrayList<>();
    }

    /**
     * 添加成绩
     * 
     * @param score 成绩分数
     */
    public void addScore(double score) {
        if (score >= 0 && score <= 100) {
            scores.add(score);
        } else {
            System.out.println("成绩必须在0-100之间！");
        }
    }

    /**
     * 计算平均成绩
     * 
     * @return 平均成绩
     */
    public double getAverageScore() {
        if (scores.isEmpty()) {
            return 0.0;
        }
        double sum = 0.0;
        for (double score : scores) {
            sum += score;
        }
        return sum / scores.size();
    }

    /**
     * 获取最高分
     * 
     * @return 最高分
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
     * 获取最低分
     * 
     * @return 最低分
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
     * 显示学生信息
     */
    public void displayInfo() {
        System.out.println("========== 学生信息 ==========");
        System.out.println("学号: " + studentId);
        System.out.println("姓名: " + name);
        System.out.println("年龄: " + age);
        System.out.println("专业: " + major);
        System.out.println("成绩列表: " + scores);
        if (!scores.isEmpty()) {
            System.out.printf("平均成绩: %.2f\n", getAverageScore());
            System.out.printf("最高分: %.2f\n", getMaxScore());
            System.out.printf("最低分: %.2f\n", getMinScore());
        }
        System.out.println("=============================");
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
        this.age = age;
    }

    public String getMajor() {
        return major;
    }

    public void setMajor(String major) {
        this.major = major;
    }

    public List<Double> getScores() {
        return scores;
    }

    /**
     * 主方法：演示 Student 类的使用
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
        student2.addScore(88.5);
        student2.addScore(91.0);
        
        // 显示学生信息
        student2.displayInfo();
    }
}
