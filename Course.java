/*
 * 文件名: Course.java
 * 作者: 开发者
 * 创建日期: 2025-10-27
 * 版本: 1.0
 * 描述: 这是一个表示课程信息的Java类文件
 *       包含课程的基本信息和相关操作方法
 * 功能:
 *   - 存储和管理课程基本信息
 *   - 提供标准的getter/setter方法
 *   - 实现课程相关的操作方法
 *   - 重写equals、hashCode和toString方法
 * 依赖: 无外部依赖,仅使用Java标准库
 * 修改记录:
 *   2025-10-27 - 初始版本创建
 */

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

/**
 * Course类 - 表示一门课程的基本信息
 */
public class Course {
    private String courseId;
    private String courseName;
    private String instructor;
    private int creditHours;
    private String description;
    private LocalDate startDate;
    private LocalDate endDate;
    private List<String> enrolledStudents;
    
    /**
     * 默认构造函数
     */
    public Course() {
        this.courseId = "";
        this.courseName = "";
        this.instructor = "";
        this.creditHours = 0;
        this.description = "";
        this.startDate = LocalDate.now();
        this.endDate = LocalDate.now();
        this.enrolledStudents = new ArrayList<>();
    }
    
    /**
     * 带参数的构造函数
     * @param courseId 课程ID
     * @param courseName 课程名称
     * @param instructor 授课教师
     * @param creditHours 学分
     * @param description 课程描述
     * @param startDate 开始日期
     * @param endDate 结束日期
     */
    public Course(String courseId, String courseName, String instructor, 
                  int creditHours, String description, LocalDate startDate, LocalDate endDate) {
        this.courseId = courseId;
        this.courseName = courseName;
        this.instructor = instructor;
        this.creditHours = creditHours;
        this.description = description;
        this.startDate = startDate;
        this.endDate = endDate;
        this.enrolledStudents = new ArrayList<>();
    }
    
    /**
     * 获取课程ID
     * @return 课程ID
     */
    public String getCourseId() {
        return courseId;
    }
    
    /**
     * 设置课程ID
     * @param courseId 课程ID
     */
    public void setCourseId(String courseId) {
        this.courseId = courseId;
    }
    
    /**
     * 获取课程名称
     * @return 课程名称
     */
    public String getCourseName() {
        return courseName;
    }
    
    /**
     * 设置课程名称
     * @param courseName 课程名称
     */
    public void setCourseName(String courseName) {
        this.courseName = courseName;
    }
    
    /**
     * 获取授课教师
     * @return 授课教师
     */
    public String getInstructor() {
        return instructor;
    }
    
    /**
     * 设置授课教师
     * @param instructor 授课教师
     */
    public void setInstructor(String instructor) {
        this.instructor = instructor;
    }
    
    /**
     * 获取学分
     * @return 学分
     */
    public int getCreditHours() {
        return creditHours;
    }
    
    /**
     * 设置学分
     * @param creditHours 学分
     */
    public void setCreditHours(int creditHours) {
        if (creditHours >= 0) {
            this.creditHours = creditHours;
        }
    }
    
    /**
     * 获取课程描述
     * @return 课程描述
     */
    public String getDescription() {
        return description;
    }
    
    /**
     * 设置课程描述
     * @param description 课程描述
     */
    public void setDescription(String description) {
        this.description = description;
    }
    
    /**
     * 获取开始日期
     * @return 开始日期
     */
    public LocalDate getStartDate() {
        return startDate;
    }
    
    /**
     * 设置开始日期
     * @param startDate 开始日期
     */
    public void setStartDate(LocalDate startDate) {
        this.startDate = startDate;
    }
    
    /**
     * 获取结束日期
     * @return 结束日期
     */
    public LocalDate getEndDate() {
        return endDate;
    }
    
    /**
     * 设置结束日期
     * @param endDate 结束日期
     */
    public void setEndDate(LocalDate endDate) {
        this.endDate = endDate;
    }
    
    /**
     * 获取已注册学生列表
     * @return 已注册学生列表
     */
    public List<String> getEnrolledStudents() {
        return new ArrayList<>(enrolledStudents);
    }
    
    /**
     * 添加学生到课程
     * @param studentId 学生ID
     * @return 如果添加成功返回true，否则返回false
     */
    public boolean enrollStudent(String studentId) {
        if (studentId == null || studentId.isEmpty()) {
            return false;
        }
        if (!enrolledStudents.contains(studentId)) {
            return enrolledStudents.add(studentId);
        }
        return false;
    }
    
    /**
     * 从课程中移除学生
     * @param studentId 学生ID
     * @return 如果移除成功返回true，否则返回false
     */
    public boolean dropStudent(String studentId) {
        if (studentId == null || studentId.isEmpty()) {
            return false;
        }
        return enrolledStudents.remove(studentId);
    }
    
    /**
     * 获取课程注册学生数量
     * @return 注册学生数量
     */
    public int getEnrolledStudentCount() {
        return enrolledStudents.size();
    }
    
    /**
     * 检查学生是否已注册该课程
     * @param studentId 学生ID
     * @return 如果已注册返回true，否则返回false
     */
    public boolean isStudentEnrolled(String studentId) {
        if (studentId == null || studentId.isEmpty()) {
            return false;
        }
        return enrolledStudents.contains(studentId);
    }
    
    /**
     * 清空课程注册学生列表
     */
    public void clearEnrolledStudents() {
        enrolledStudents.clear();
    }
    
    /**
     * 获取课程信息描述
     * @return 课程信息字符串
     */
    public String getCourseDescription() {
        return String.format("课程ID: %s, 课程名称: %s, 授课教师: %s, 学分: %d, 注册学生数: %d", 
                           courseId, courseName, instructor, creditHours, getEnrolledStudentCount());
    }
    
    @Override
    public String toString() {
        return "Course{" +
                "courseId='" + courseId + '\'' +
                ", courseName='" + courseName + '\'' +
                ", instructor='" + instructor + '\'' +
                ", creditHours=" + creditHours +
                ", startDate=" + startDate +
                ", endDate=" + endDate +
                ", enrolledStudents=" + enrolledStudents.size() +
                '}';
    }
    
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Course course = (Course) obj;
        return courseId.equals(course.courseId);
    }
    
    @Override
    public int hashCode() {
        return courseId.hashCode();
    }
}