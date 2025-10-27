// Hello World
/*
 * ============================================================================
 * 文件名: Student.java
 * 作者: 开发者
 * 创建日期: 2025-10-11
 * 版本: 1.0
 * 描述: 这是一个表示学生信息的Java类文件
 *       继承自Person类，扩展学生特有的属性和方法
 * 
 * 功能概述:
 *   - 存储和管理学生基本信息（继承自Person）
 *   - 管理学生ID、专业、年级等学生特有信息
 *   - 提供成绩管理功能（添加、删除、查询成绩）
 *   - 实现学生状态判断（优秀学生、课程通过等）
 *   - 提供成绩统计功能（平均分、通过课程数等）
 * 
 * 设计模式: 继承模式（Inheritance Pattern）
 * 依赖: Person.java
 * 
 * 修改记录:
 *   2025-10-11 - 初始版本创建
 *   2025-10-27 - 添加详细注释
 * ============================================================================
 */

import java.util.HashMap;
import java.util.Map;

/**
 * Student类 - 表示一个学生的完整信息
 * 
 * <p>继承自Person类，扩展学生特有功能。该类封装了学生的学业相关信息，
 * 包括学号、专业、年级以及各科成绩等。提供了完整的成绩管理功能。</p>
 * 
 * <p>主要特性：</p>
 * <ul>
 *   <li>学生基本信息管理（学号、专业、年级）</li>
 *   <li>课程成绩管理（添加、删除、查询）</li>
 *   <li>成绩统计分析（平均分、通过率等）</li>
 *   <li>学生状态判断（优秀学生、课程通过等）</li>
 * </ul>
 * 
 * <p>使用示例：</p>
 * <pre>
 * Student student = new Student("张三", 20, "zhangsan@example.com", 
 *                               "2021001", "计算机科学", 2);
 * student.addScore("数学", 95.0);
 * student.addScore("英语", 88.0);
 * double avg = student.getAverageScore();
 * </pre>
 * 
 * @author 开发者
 * @version 1.0
 * @since 2025-10-11
 * @see Person
 */
public class Student extends Person {
    /**
     * 学生学号
     * <p>唯一标识学生的编号，通常由学校统一分配</p>
     */
    private String studentId;
    
    /**
     * 学生专业
     * <p>学生所学的专业名称，如"计算机科学"、"软件工程"等</p>
     */
    private String major;
    
    /**
     * 学生年级
     * <p>学生当前所在的年级，取值范围：1-4（大一到大四）</p>
     */
    private int grade;
    
    /**
     * 课程成绩映射表
     * <p>存储学生所有课程的成绩，键为课程名称，值为该课程的分数（0-100）</p>
     * <p>使用HashMap实现快速的成绩查询和更新</p>
     */
    private Map<String, Double> scores;
    
    /**
     * 默认构造函数
     * 
     * <p>创建一个空的学生对象，所有字段都被初始化为默认值：</p>
     * <ul>
     *   <li>studentId: 空字符串</li>
     *   <li>major: 空字符串</li>
     *   <li>grade: 1（一年级）</li>
     *   <li>scores: 空的HashMap</li>
     * </ul>
     * 
     * <p>注意：使用此构造函数后需要通过setter方法设置具体值</p>
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
     * 
     * <p>创建一个包含完整信息的学生对象。该构造函数会调用父类Person的构造函数
     * 来初始化基本信息，然后设置学生特有的属性。</p>
     * 
     * @param name 学生姓名，不应为null或空字符串
     * @param age 学生年龄，应为正整数
     * @param email 学生邮箱地址，应符合邮箱格式
     * @param studentId 学生学号，唯一标识，不应为null或空字符串
     * @param major 学生专业名称，不应为null或空字符串
     * @param grade 学生年级，有效范围为1-4
     * 
     * @see Person#Person(String, int, String)
     */
    public Student(String name, int age, String email, String studentId, String major, int grade) {
        super(name, age, email);
        this.studentId = studentId;
        this.major = major;
        this.grade = grade;
        this.scores = new HashMap<>();
    }
    
    /**
     * 获取学生学号
     * 
     * @return 返回学生的学号字符串，如果未设置则返回空字符串
     */
    public String getStudentId() {
        return studentId;
    }
    
    /**
     * 设置学生学号
     * 
     * <p>用于设置或更新学生的学号。学号应该是唯一的。</p>
     * 
     * @param studentId 要设置的学号，建议不为null或空字符串
     */
    public void setStudentId(String studentId) {
        this.studentId = studentId;
    }
    
    /**
     * 获取学生专业
     * 
     * @return 返回学生的专业名称字符串，如果未设置则返回空字符串
     */
    public String getMajor() {
        return major;
    }
    
    /**
     * 设置学生专业
     * 
     * <p>用于设置或更新学生的专业信息。</p>
     * 
     * @param major 要设置的专业名称，建议不为null或空字符串
     */
    public void setMajor(String major) {
        this.major = major;
    }
    
    /**
     * 获取学生年级
     * 
     * @return 返回学生当前所在的年级（1-4），默认为1
     */
    public int getGrade() {
        return grade;
    }
    
    /**
     * 设置学生年级
     * 
     * <p>用于设置或更新学生的年级信息。只接受1-4之间的有效年级值，
     * 如果传入的值不在此范围内，则不会进行设置。</p>
     * 
     * @param grade 要设置的年级，有效值为1、2、3或4，其他值将被忽略
     */
    public void setGrade(int grade) {
        if (grade >= 1 && grade <= 4) {
            this.grade = grade;
        }
    }
    
    /**
     * 添加或更新课程成绩
     * 
     * <p>将指定课程的成绩添加到学生的成绩记录中。如果该课程已经存在，
     * 则会更新为新的成绩。只接受0-100之间的有效分数。</p>
     * 
     * <p>注意：</p>
     * <ul>
     *   <li>分数必须在0-100之间，否则不会添加</li>
     *   <li>如果课程已存在，会覆盖原有成绩</li>
     * </ul>
     * 
     * @param course 课程名称，不应为null或空字符串
     * @param score 课程成绩，有效范围为0.0-100.0，超出范围的值将被忽略
     */
    public void addScore(String course, double score) {
        if (score >= 0 && score <= 100) {
            scores.put(course, score);
        }
    }
    
    /**
     * 获取指定课程的成绩
     * 
     * <p>根据课程名称查询该学生在该课程的得分。如果学生没有该课程的成绩记录，
     * 则返回-1.0作为标识。</p>
     * 
     * @param course 要查询的课程名称
     * @return 返回该课程的成绩（0.0-100.0），如果课程不存在则返回-1.0
     */
    public double getScore(String course) {
        return scores.getOrDefault(course, -1.0);
    }
    
    /**
     * 计算所有课程的平均分
     * 
     * <p>计算学生所有已录入课程成绩的平均值。如果学生没有任何成绩记录，
     * 则返回0.0。</p>
     * 
     * <p>计算公式：平均分 = 所有课程成绩之和 / 课程数量</p>
     * 
     * @return 返回平均分（保留两位小数），如果没有成绩记录则返回0.0
     */
    public double getAverageScore() {
        if (scores.isEmpty()) {
            return 0.0;
        }
        double sum = scores.values().stream().mapToDouble(Double::doubleValue).sum();
        return sum / scores.size();
    }
    
    /**
     * 判断是否为优秀学生
     * 
     * <p>根据学生的平均分判断是否达到优秀学生标准。优秀学生的标准是
     * 平均分大于或等于85分。</p>
     * 
     * @return 如果平均分>=85.0则返回true，否则返回false
     */
    public boolean isExcellentStudent() {
        return getAverageScore() >= 85.0;
    }
    
    /**
     * 获取所有课程成绩的副本
     * 
     * <p>返回一个包含所有课程及其成绩的Map副本。返回的是副本而非原始对象，
     * 因此对返回的Map进行修改不会影响学生对象内部的成绩数据。</p>
     * 
     * @return 返回一个新的HashMap，包含所有课程名称和对应成绩的映射关系
     */
    public Map<String, Double> getAllScores() {
        return new HashMap<>(scores);
    }
    
    /**
     * 删除指定课程的成绩记录
     * 
     * <p>从学生的成绩记录中删除指定课程。如果该课程存在，则删除并返回true；
     * 如果课程不存在，则返回false。</p>
     * 
     * @param course 要删除的课程名称
     * @return 如果成功删除返回true，如果课程不存在返回false
     */
    public boolean removeScore(String course) {
        return scores.remove(course) != null;
    }
    
    /**
     * 获取学生已录入成绩的课程数量
     * 
     * <p>统计学生当前有成绩记录的课程总数。</p>
     * 
     * @return 返回已录入成绩的课程数量，最小值为0
     */
    public int getCourseCount() {
        return scores.size();
    }
    
    /**
     * 检查是否通过指定课程
     * 
     * <p>判断学生在指定课程中是否达到及格标准（60分及以上）。
     * 如果课程不存在或成绩低于60分，则认为未通过。</p>
     * 
     * @param course 要检查的课程名称
     * @return 如果成绩>=60.0且课程存在返回true，否则返回false
     */
    public boolean isPassedCourse(String course) {
        double score = getScore(course);
        return score >= 60.0 && score != -1.0;
    }
    
    /**
     * 获取通过的课程数量（及格课程数）
     * 
     * <p>统计学生所有成绩>=60分的课程数量。使用Stream API进行过滤和计数。</p>
     * 
     * @return 返回成绩>=60.0的课程数量
     */
    public int getPassedCourseCount() {
        return (int) scores.values().stream().filter(score -> score >= 60.0).count();
    }
    
    /**
     * 获取学生完整信息的描述字符串
     * 
     * <p>覆盖父类的getDescription方法，返回包含学号、基本信息、专业、
     * 年级和平均分的格式化字符串。</p>
     * 
     * <p>输出格式："学号: xxx, [父类信息], 专业: xxx, 年级: x年级, 平均分: xx.xx"</p>
     * 
     * @return 返回学生的完整信息描述字符串
     * @see Person#getDescription()
     */
    @Override
    public String getDescription() {
        return String.format("学号: %s, %s, 专业: %s, 年级: %d年级, 平均分: %.2f", 
                           studentId, super.getDescription(), major, grade, getAverageScore());
    }
    
    /**
     * 返回学生对象的字符串表示形式
     * 
     * <p>覆盖Object类的toString方法，返回包含学生所有关键信息的字符串，
     * 便于调试和日志记录。</p>
     * 
     * <p>输出格式示例：
     * "Student{studentId='2021001', major='计算机科学', grade=2, averageScore=91.50, ...}"</p>
     * 
     * @return 返回包含学生所有字段的字符串表示
     */
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
    
    /**
     * 判断两个学生对象是否相等
     * 
     * <p>覆盖Object类的equals方法。两个学生对象相等的条件是：</p>
     * <ul>
     *   <li>父类Person的equals方法返回true（姓名、年龄、邮箱相同）</li>
     *   <li>学号相同</li>
     *   <li>专业相同</li>
     *   <li>年级相同</li>
     * </ul>
     * 
     * @param obj 要比较的对象
     * @return 如果两个学生对象相等返回true，否则返回false
     * @see Object#equals(Object)
     */
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
    
    /**
     * 返回学生对象的哈希码
     * 
     * <p>覆盖Object类的hashCode方法。哈希码的计算基于：</p>
     * <ul>
     *   <li>父类的hashCode</li>
     *   <li>学号的hashCode</li>
     *   <li>专业的hashCode</li>
     *   <li>年级值</li>
     * </ul>
     * 
     * <p>注意：此方法与equals方法保持一致，确保相等的对象具有相同的哈希码。</p>
     * 
     * @return 返回学生对象的哈希码值
     * @see Object#hashCode()
     */
    @Override
    public int hashCode() {
        return super.hashCode() + studentId.hashCode() + major.hashCode() + grade;
    }
}