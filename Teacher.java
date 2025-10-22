/*
 * 文件名: Teacher.java
 * 作者: 开发者
 * 创建日期: 2025-10-22
 * 版本: 1.0
 * 描述: 这是一个表示教师信息的Java类文件
 *       继承自Person类，扩展教师特有的属性和方法
 * 功能:
 *   - 存储和管理教师基本信息（继承自Person）
 *   - 管理教师ID、职称、部门等教师特有信息
 *   - 提供课程管理功能
 *   - 实现教师工作量统计
 * 依赖: Person.java
 * 修改记录:
 *   2025-10-22 - 初始版本创建
 */

import java.util.ArrayList;
import java.util.List;

/**
 * Teacher类 - 表示一个教师的完整信息
 * 继承自Person类，扩展教师特有功能
 */
public class Teacher extends Person {
    private String teacherId;
    private String department;
    private String title;
    private double salary;
    private List<String> courses;
    
    /**
     * 默认构造函数
     */
    public Teacher() {
        super();
        this.teacherId = "";
        this.department = "";
        this.title = "讲师";
        this.salary = 0.0;
        this.courses = new ArrayList<>();
    }
    
    /**
     * 带参数的构造函数
     * @param name 姓名
     * @param age 年龄
     * @param email 邮箱
     * @param teacherId 教师ID
     * @param department 部门
     * @param title 职称
     */
    public Teacher(String name, int age, String email, String teacherId, String department, String title) {
        super(name, age, email);
        this.teacherId = teacherId;
        this.department = department;
        this.title = title;
        this.salary = 0.0;
        this.courses = new ArrayList<>();
    }
    
    /**
     * 获取教师ID
     * @return 教师ID
     */
    public String getTeacherId() {
        return teacherId;
    }
    
    /**
     * 设置教师ID
     * @param teacherId 教师ID
     */
    public void setTeacherId(String teacherId) {
        this.teacherId = teacherId;
    }
    
    /**
     * 获取部门
     * @return 部门
     */
    public String getDepartment() {
        return department;
    }
    
    /**
     * 设置部门
     * @param department 部门
     */
    public void setDepartment(String department) {
        this.department = department;
    }
    
    /**
     * 获取职称
     * @return 职称
     */
    public String getTitle() {
        return title;
    }
    
    /**
     * 设置职称
     * @param title 职称（讲师、副教授、教授等）
     */
    public void setTitle(String title) {
        this.title = title;
    }
    
    /**
     * 获取薪资
     * @return 薪资
     */
    public double getSalary() {
        return salary;
    }
    
    /**
     * 设置薪资
     * @param salary 薪资
     */
    public void setSalary(double salary) {
        if (salary >= 0) {
            this.salary = salary;
        }
    }
    
    /**
     * 添加授课课程
     * @param course 课程名称
     * @return 如果添加成功返回true，如果课程已存在返回false
     */
    public boolean addCourse(String course) {
        if (!courses.contains(course)) {
            courses.add(course);
            return true;
        }
        return false;
    }
    
    /**
     * 移除授课课程
     * @param course 课程名称
     * @return 如果移除成功返回true，否则返回false
     */
    public boolean removeCourse(String course) {
        return courses.remove(course);
    }
    
    /**
     * 获取所有授课课程
     * @return 课程列表的副本
     */
    public List<String> getCourses() {
        return new ArrayList<>(courses);
    }
    
    /**
     * 获取授课课程数量
     * @return 课程数量
     */
    public int getCourseCount() {
        return courses.size();
    }
    
    /**
     * 检查是否教授指定课程
     * @param course 课程名称
     * @return 如果教授该课程返回true，否则返回false
     */
    public boolean teachesCourse(String course) {
        return courses.contains(course);
    }
    
    /**
     * 判断是否为高级职称（副教授或教授）
     * @return 如果是高级职称返回true
     */
    public boolean isSeniorTitle() {
        return title.equals("副教授") || title.equals("教授");
    }
    
    /**
     * 判断工作量是否饱和（课程数>=4）
     * @return 如果课程数大于等于4返回true
     */
    public boolean isFullWorkload() {
        return courses.size() >= 4;
    }
    
    /**
     * 计算课时费（基于课程数量）
     * @param ratePerCourse 每门课程的课时费
     * @return 总课时费
     */
    public double calculateTeachingFee(double ratePerCourse) {
        return courses.size() * ratePerCourse;
    }
    
    /**
     * 清空所有授课课程
     */
    public void clearAllCourses() {
        courses.clear();
    }
    
    /**
     * 获取教师完整信息描述
     * @return 教师信息字符串
     */
    @Override
    public String getDescription() {
        return String.format("教师ID: %s, %s, 部门: %s, 职称: %s, 授课数: %d门", 
                           teacherId, super.getDescription(), department, title, getCourseCount());
    }
    
    @Override
    public String toString() {
        return "Teacher{" +
                "teacherId='" + teacherId + '\'' +
                ", department='" + department + '\'' +
                ", title='" + title + '\'' +
                ", salary=" + salary +
                ", courseCount=" + getCourseCount() +
                ", " + super.toString() +
                '}';
    }
    
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        if (!super.equals(obj)) return false;
        Teacher teacher = (Teacher) obj;
        return teacherId.equals(teacher.teacherId) &&
                department.equals(teacher.department) &&
                title.equals(teacher.title);
    }
    
    @Override
    public int hashCode() {
        return super.hashCode() + teacherId.hashCode() + department.hashCode() + title.hashCode();
    }
}
