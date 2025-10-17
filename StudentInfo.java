/**
 * 学生信息类
 * 用于存储和管理学生的基本信息和成绩
 */
public class StudentInfo {
    private String studentId;
    private String name;
    private int age;
    private String grade;
    private double averageScore;

    /**
     * 构造函数
     * @param studentId 学生ID
     * @param name 学生姓名
     * @param age 学生年龄
     * @param grade 年级
     */
    public StudentInfo(String studentId, String name, int age, String grade) {
        this.studentId = studentId;
        this.name = name;
        this.age = age;
        this.grade = grade;
        this.averageScore = 0.0;
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

    public String getGrade() {
        return grade;
    }

    public void setGrade(String grade) {
        this.grade = grade;
    }

    public double getAverageScore() {
        return averageScore;
    }

    public void setAverageScore(double averageScore) {
        this.averageScore = averageScore;
    }

    /**
     * 显示学生信息
     */
    public void displayInfo() {
        System.out.println("========== 学生信息 ==========");
        System.out.println("学号: " + studentId);
        System.out.println("姓名: " + name);
        System.out.println("年龄: " + age);
        System.out.println("年级: " + grade);
        System.out.println("平均分: " + String.format("%.2f", averageScore));
        System.out.println("============================");
    }

    /**
     * 判断是否为优秀学生（平均分>=90）
     * @return 是否为优秀学生
     */
    public boolean isExcellent() {
        return averageScore >= 90.0;
    }

    /**
     * 判断是否及格（平均分>=60）
     * @return 是否及格
     */
    public boolean isPassed() {
        return averageScore >= 60.0;
    }

    @Override
    public String toString() {
        return "StudentInfo{" +
                "studentId='" + studentId + '\'' +
                ", name='" + name + '\'' +
                ", age=" + age +
                ", grade='" + grade + '\'' +
                ", averageScore=" + averageScore +
                '}';
    }

    /**
     * 主方法 - 演示示例
     */
    public static void main(String[] args) {
        // 创建学生对象
        StudentInfo student1 = new StudentInfo("S001", "张三", 18, "高三");
        student1.setAverageScore(92.5);
        
        StudentInfo student2 = new StudentInfo("S002", "李四", 17, "高二");
        student2.setAverageScore(78.3);

        // 显示学生信息
        student1.displayInfo();
        System.out.println("是否优秀: " + (student1.isExcellent() ? "是" : "否"));
        System.out.println();

        student2.displayInfo();
        System.out.println("是否优秀: " + (student2.isExcellent() ? "是" : "否"));
    }
}
