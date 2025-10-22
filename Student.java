// Hello World
/*
 * 文件名: Student.java
 * 作者: 开发者
 * 创建日期: 2025-10-11
 * 版本: 1.0
 * 描述: 这是一个表示学生信息的Java类文件
 *       继承自Person类，扩展学生特有的属性和方法
 * 功能:
 *   - 存储和管理学生基本信息（继承自Person）
 *   - 管理学生ID、专业、年级等学生特有信息
 *   - 提供成绩管理功能
 *   - 实现学生状态判断
 * 依赖: Person.java
 * 修改记录:
 *   2025-10-11 -  初始版本创建
 */

import java.util.HashMap;
import java.util.Map;

/**
 * Student类 - 表示一个 学生的完整信息
 * 继承自Person类， 扩展学生特有功能
 */
public class Student extends Person {
    private String studentId;
    private String major;
    private int grade;
    private Map<String, Double> scores;
    
    /**
     * 默认构造函数
     */
    public Student() {
        super();
        this.studentId = "";
        this.major = "";
        this.grade = 1;
        this.scores = new HashMap<>();
    }
    
    /**
     * 带参数的构造函数
     * @param name 姓名
     * @param age 年龄
     * @param email 邮箱
     * @param studentId 学号
     * @param major 专业
     * @param grade 年级
     */
    public Student(String name, int age, String email, String studentId, String major, int grade) {
        super(name, age, email);
        this.studentId = studentId;
        this.major = major;
        this.grade = grade;
        this.scores = new HashMap<>();
    }
    
    /**
     * 获取学号
     * @return 学号
     */
    public String getStudentId() {
        return studentId;
    }
    
    /**
     * 设置学号
     * @param studentId 学号
     */
    public void setStudentId(String studentId) {
        this.studentId = studentId;
    }
    
    /**
     * 获取专业
     * @return 专业
     */
    public String getMajor() {
        return major;
    }
    
    /**
     * 设置专业
     * @param major 专业
     */
    public void setMajor(String major) {
        this.major = major;
    }
    
    /**
     * 获取年级
     * @return 年级
     */
    public int getGrade() {
        return grade;
    }
    
    /**
     * 设置年级
     * @param grade 年级
     */
    public void setGrade(int grade) {
        if (grade >= 1 && grade <= 4) {
            this.grade = grade;
        }
    }
    
    /**
     * 添加课程成绩
     * @param course 课程名称
     * @param score 成绩
     */
    public void addScore(String course, double score) {
        if (score >= 0 && score <= 100) {
            scores.put(course, score);
        }
    }
    
    /**
     * 获取指定课程成绩
     * @param course 课程名称
     * @return 成绩，如果课程不存在则返回-1
     */
    public double getScore(String course) {
        return scores.getOrDefault(course, -1.0);
    }
    
    /**
     * 计算平均分
     * @return 平均分
     */
    public double getAverageScore() {
        if (scores.isEmpty()) {
            return 0.0;
        }
        double sum = scores.values().stream().mapToDouble(Double::doubleValue).sum();
        return sum / scores.size();
    }
    
    /**
     * 判断是否为优秀学生（平均分>=85）
     * @return 如果平均分大于等于85则返回true
     */
    public boolean isExcellentStudent() {
        return getAverageScore() >= 85.0;
    }
    
    /**
     * 获取所有课程成绩
     * @return 课程成绩映射
     */
    public Map<String, Double> getAllScores() {
        return new HashMap<>(scores);
    }
    
    /**
     * 删除指定课程成绩
     * @param course 课程名称
     * @return 如果删除成功返回true，否则返回false
     */
    public boolean removeScore(String course) {
        return scores.remove(course) != null;
    }
    
    /**
     * 获取课程数量
     * @return 已选课程数量
     */
    public int getCourseCount() {
        return scores.size();
    }
    
    /**
     * 检查是否通过指定课程（成绩>=60）
     * @param course 课程名称
     * @return 如果通过返回true，否则返回false
     */
    public boolean isPassedCourse(String course) {
        double score = getScore(course);
        return score >= 60.0 && score != -1.0;
    }
    
    /**
     * 获取通过的课程数量
     * @return 通过的课程数量
     */
    public int getPassedCourseCount() {
        return (int) scores.values().stream().filter(score -> score >= 60.0).count();
    }
    
    /**
     * 获取学生完整信息描述
     * @return 学生信息字符串
     */
    @Override
    public String getDescription() {
        return String.format("学号: %s, %s, 专业: %s, 年级: %d年级, 平均分: %.2f", 
                           studentId, super.getDescription(), major, grade, getAverageScore());
    }
    
    @Override
    public String toString() {
        return "Student{" +
                "studentId='" + studentId + '\'' +
                ", major='" + major + '\'' +
                ", grade=" + grade +
                ", averageScore=" + String.format("%.2f", getAverageScore()) +
                ", " + super.toString() +
                '}';
    }
    
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        if (!super.equals(obj)) return false;
        Student student = (Student) obj;
        return grade == student.grade &&
                studentId.equals(student.studentId) &&
                major.equals(student.major);
    }
    
    @Override
    public int hashCode() {
        return super.hashCode() + studentId.hashCode() + major.hashCode() + grade;
    }
}