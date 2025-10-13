import java.util.ArrayList;
import java.util.List;

/**
 * 学生成绩管理类
 * 用于管理学生的各科成绩
 */
public class StudentGrade {
    private String studentName;
    private String studentId;
    private List<Double> grades;
    
    // 构造方法
    public StudentGrade(String name, String id) {
        this.studentName = name;
        this.studentId = id;
        this.grades = new ArrayList<>();
    }
    
    // 添加成绩
    public void addGrade(double grade) {
        if (grade >= 0 && grade <= 100) {
            grades.add(grade);
            System.out.println("成绩 " + grade + " 已添加");
        } else {
            System.out.println("成绩必须在0-100之间");
        }
    }
    
    // 计算平均分
    public double calculateAverage() {
        if (grades.isEmpty()) {
            return 0.0;
        }
        
        double sum = 0;
        for (double grade : grades) {
            sum += grade;
        }
        return sum / grades.size();
    }
    
    // 获取最高分
    public double getHighestGrade() {
        if (grades.isEmpty()) {
            return 0.0;
        }
        
        double highest = grades.get(0);
        for (double grade : grades) {
            if (grade > highest) {
                highest = grade;
            }
        }
        return highest;
    }
    
    // 获取最低分
    public double getLowestGrade() {
        if (grades.isEmpty()) {
            return 0.0;
        }
        
        double lowest = grades.get(0);
        for (double grade : grades) {
            if (grade < lowest) {
                lowest = grade;
            }
        }
        return lowest;
    }
    
    // 显示学生信息
    public void displayStudentInfo() {
        System.out.println("=== 学生信息 ===");
        System.out.println("姓名: " + studentName);
        System.out.println("学号: " + studentId);
        System.out.println("成绩数量: " + grades.size());
        
        if (!grades.isEmpty()) {
            System.out.println("所有成绩: " + grades);
            System.out.printf("平均分: %.2f\n", calculateAverage());
            System.out.println("最高分: " + getHighestGrade());
            System.out.println("最低分: " + getLowestGrade());
        } else {
            System.out.println("暂无成绩记录");
        }
        System.out.println("================");
    }
    
    // Getter和Setter方法
    public String getStudentName() {
        return studentName;
    }
    
    public void setStudentName(String studentName) {
        this.studentName = studentName;
    }
    
    public String getStudentId() {
        return studentId;
    }
    
    public void setStudentId(String studentId) {
        this.studentId = studentId;
    }
    
    public List<Double> getGrades() {
        return new ArrayList<>(grades);
    }
    
    // 主方法 - 演示用法
    public static void main(String[] args) {
        // 创建学生对象
        StudentGrade student = new StudentGrade("张三", "2023001");
        
        // 添加一些成绩
        student.addGrade(85.5);
        student.addGrade(92.0);
        student.addGrade(78.5);
        student.addGrade(88.0);
        student.addGrade(95.5);
        
        // 显示学生信息
        student.displayStudentInfo();
        
        // 尝试添加无效成绩
        System.out.println("\n尝试添加无效成绩:");
        student.addGrade(105);  // 无效成绩
        student.addGrade(-10);  // 无效成绩
        
        System.out.println("\n创建另一个学生:");
        StudentGrade student2 = new StudentGrade("李四", "2023002");
        student2.displayStudentInfo();
    }
}