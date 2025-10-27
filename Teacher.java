/*
 * 文件名: Teacher.java
 * 作者: 开发者
 * 创建日期: 2025-10-24
 * 版本: 1.0
 * 描述: 这是一个表示教师信息的Java类文件
 *       继承自Person类,扩展教师特有的属性和方法
 * 功能:
 *   - 存储和管理教师基本信息(继承自Person)
 *   - 管理教师ID、所教科目、职称等教师特有信息
 *   - 提供授课班级管理功能
 *   - 实现教师资历判断
 * 依赖: Person.java
 * 修改记录:
 *   2025-10-24 - 初始版本创建
 */

import java.util.ArrayList;
import java.util.List;

/**
 * Teacher类 - 表示一个教师的完整信息
 * 继承自Person类,扩展教师特有功能
 */
public class Teacher extends Person {
    private String teacherId;
    private String subject;
    private String title;
    private int yearsOfExperience;
    private List<String> classes;
    
    /**
     * 默认构造函数
     */
    public Teacher() {
        super();
        this.teacherId = "";
        this.subject = "";
        this.title = "助教";
        this.yearsOfExperience = 0;
        this.classes = new ArrayList<>();
    }
    
    /**
     * 带参数的构造函数
     * @param name 姓名
     * @param age 年龄
     * @param email 邮箱
     * @param teacherId 教师ID
     * @param subject 所教科目
     * @param title 职称
     * @param yearsOfExperience 教龄(年)
     */
    public Teacher(String name, int age, String email, String teacherId, 
                   String subject, String title, int yearsOfExperience) {
        super(name, age, email);
        this.teacherId = teacherId;
        this.subject = subject;
        this.title = title;
        this.yearsOfExperience = yearsOfExperience;
        this.classes = new ArrayList<>();
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
     * 获取所教科目
     * @return 科目名称
     */
    public String getSubject() {
        return subject;
    }
    
    /**
     * 设置所教科目
     * @param subject 科目名称
     */
    public void setSubject(String subject) {
        this.subject = subject;
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
     * @param title 职称(助教/讲师/副教授/教授)
     */
    public void setTitle(String title) {
        this.title = title;
    }
    
    /**
     * 获取教龄
     * @return 教龄(年)
     */
    public int getYearsOfExperience() {
        return yearsOfExperience;
    }
    
    /**
     * 设置教龄
     * @param yearsOfExperience 教龄(年)
     */
    public void setYearsOfExperience(int yearsOfExperience) {
        if (yearsOfExperience >= 0) {
            this.yearsOfExperience = yearsOfExperience;
        }
    }
    
    /**
     * 添加授课班级
     * @param className 班级名称
     */
    public void addClass(String className) {
        if (!classes.contains(className)) {
            classes.add(className);
        }
    }
    
    /**
     * 移除授课班级
     * @param className 班级名称
     * @return 如果移除成功返回true,否则返回false
     */
    public boolean removeClass(String className) {
        return classes.remove(className);
    }
    
    /**
     * 获取所有授课班级
     * @return 班级列表
     */
    public List<String> getAllClasses() {
        return new ArrayList<>(classes);
    }
    
    /**
     * 获取授课班级数量
     * @return 班级数量
     */
    public int getClassCount() {
        return classes.size();
    }
    
    /**
     * 检查是否教授指定班级
     * @param className 班级名称
     * @return 如果教授该班级返回true,否则返回false
     */
    public boolean teachesClass(String className) {
        return classes.contains(className);
    }
    
    /**
     * 判断是否为资深教师(教龄>=10年)
     * @return 如果教龄大于等于10年则返回true
     */
    public boolean isSeniorTeacher() {
        return yearsOfExperience >= 10;
    }
    
    /**
     * 判断是否为高级职称(副教授或教授)
     * @return 如果是副教授或教授返回true
     */
    public boolean hasSeniorTitle() {
        return title.equals("副教授") || title.equals("教授");
    }
    
    /**
     * 清空所有授课班级
     */
    public void clearAllClasses() {
        classes.clear();
    }
    
    /**
     * 获取教师完整信息描述
     * @return 教师信息字符串
     */
    @Override
    public String getDescription() {
        return String.format("工号: %s, %s, 科目: %s, 职称: %s, 教龄: %d年, 授课班级数: %d", 
                           teacherId, super.getDescription(), subject, title, 
                           yearsOfExperience, getClassCount());
    }
    
    @Override
    public String toString() {
        return "Teacher{" +
                "teacherId='" + teacherId + '\'' +
                ", subject='" + subject + '\'' +
                ", title='" + title + '\'' +
                ", yearsOfExperience=" + yearsOfExperience +
                ", classCount=" + getClassCount() +
                ", " + super.toString() +
                '}';
    }
    
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        if (!super.equals(obj)) return false;
        Teacher teacher = (Teacher) obj;
        return yearsOfExperience == teacher.yearsOfExperience &&
                teacherId.equals(teacher.teacherId) &&
                subject.equals(teacher.subject) &&
                title.equals(teacher.title);
    }
    
    @Override
    public int hashCode() {
        return super.hashCode() + teacherId.hashCode() + 
               subject.hashCode() + title.hashCode() + yearsOfExperience;
    }
}
