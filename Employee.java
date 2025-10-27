/*
 * 文件名: Employee.java
 * 作者: 开发者
 * 创建日期: 2025-10-27
 * 版本: 1.0
 * 描述: 这是一个表示员工信息的Java类文件
 *       继承自Person类，扩展员工特有的属性和方法
 * 功能:
 *   - 存储和管理员工基本信息（继承自Person）
 *   - 管理员工ID、职位、薪资等员工特有信息
 *   - 提供绩效评估功能
 *   - 实现员工状态判断
 * 依赖: Person.java
 * 修改记录:
 *   2025-10-27 - 初始版本创建
 */

import java.util.ArrayList;
import java.util.List;

/**
 * Employee类 - 表示一个员工的完整信息
 * 继承自Person类，扩展员工特有功能
 */
public class Employee extends Person {
    private String employeeId;
    private String position;
    private String department;
    private double salary;
    private int performanceScore;
    private List<String> skills;
    
    /**
     * 默认构造函数
     */
    public Employee() {
        super();
        this.employeeId = "";
        this.position = "";
        this.department = "";
        this.salary = 0.0;
        this.performanceScore = 0;
        this.skills = new ArrayList<>();
    }
    
    /**
     * 带参数的构造函数
     * @param name 姓名
     * @param age 年龄
     * @param email 邮箱
     * @param employeeId 员工ID
     * @param position 职位
     * @param department 部门
     * @param salary 薪资
     */
    public Employee(String name, int age, String email, String employeeId, 
                   String position, String department, double salary) {
        super(name, age, email);
        this.employeeId = employeeId;
        this.position = position;
        this.department = department;
        this.salary = salary;
        this.performanceScore = 0;
        this.skills = new ArrayList<>();
    }
    
    /**
     * 获取员工ID
     * @return 员工ID
     */
    public String getEmployeeId() {
        return employeeId;
    }
    
    /**
     * 设置员工ID
     * @param employeeId 员工ID
     */
    public void setEmployeeId(String employeeId) {
        this.employeeId = employeeId;
    }
    
    /**
     * 获取职位
     * @return 职位
     */
    public String getPosition() {
        return position;
    }
    
    /**
     * 设置职位
     * @param position 职位
     */
    public void setPosition(String position) {
        this.position = position;
    }
    
    /**
     * 获取部门
     * @return 部门名称
     */
    public String getDepartment() {
        return department;
    }
    
    /**
     * 设置部门
     * @param department 部门名称
     */
    public void setDepartment(String department) {
        this.department = department;
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
     * 获取绩效分数
     * @return 绩效分数
     */
    public int getPerformanceScore() {
        return performanceScore;
    }
    
    /**
     * 设置绩效分数
     * @param performanceScore 绩效分数（0-100）
     */
    public void setPerformanceScore(int performanceScore) {
        if (performanceScore >= 0 && performanceScore <= 100) {
            this.performanceScore = performanceScore;
        }
    }
    
    /**
     * 添加技能
     * @param skill 技能名称
     */
    public void addSkill(String skill) {
        if (!skills.contains(skill)) {
            skills.add(skill);
        }
    }
    
    /**
     * 移除技能
     * @param skill 技能名称
     * @return 如果移除成功返回true，否则返回false
     */
    public boolean removeSkill(String skill) {
        return skills.remove(skill);
    }
    
    /**
     * 获取所有技能
     * @return 技能列表
     */
    public List<String> getAllSkills() {
        return new ArrayList<>(skills);
    }
    
    /**
     * 获取技能数量
     * @return 技能数量
     */
    public int getSkillCount() {
        return skills.size();
    }
    
    /**
     * 检查是否拥有指定技能
     * @param skill 技能名称
     * @return 如果拥有该技能返回true，否则返回false
     */
    public boolean hasSkill(String skill) {
        return skills.contains(skill);
    }
    
    /**
     * 判断是否为优秀员工（绩效分数>=90）
     * @return 如果绩效分数大于等于90则返回true
     */
    public boolean isExcellentEmployee() {
        return performanceScore >= 90;
    }
    
    /**
     * 判断是否为高薪员工（薪资>=20000）
     * @return 如果薪资大于等于20000则返回true
     */
    public boolean isHighSalaryEmployee() {
        return salary >= 20000.0;
    }
    
    /**
     * 涨薪
     * @param amount 涨薪金额
     */
    public void raiseSalary(double amount) {
        if (amount > 0) {
            this.salary += amount;
        }
    }
    
    /**
     * 按百分比涨薪
     * @param percentage 涨薪百分比（如10表示涨薪10%）
     */
    public void raiseSalaryByPercentage(double percentage) {
        if (percentage > 0) {
            this.salary += this.salary * (percentage / 100.0);
        }
    }
    
    /**
     * 获取绩效等级
     * @return 绩效等级字符串
     */
    public String getPerformanceLevel() {
        if (performanceScore >= 90) {
            return "优秀";
        } else if (performanceScore >= 80) {
            return "良好";
        } else if (performanceScore >= 70) {
            return "合格";
        } else if (performanceScore >= 60) {
            return "待改进";
        } else {
            return "不合格";
        }
    }
    
    /**
     * 清空所有技能
     */
    public void clearAllSkills() {
        skills.clear();
    }
    
    /**
     * 获取员工完整信息描述
     * @return 员工信息字符串
     */
    @Override
    public String getDescription() {
        return String.format("工号: %s, %s, 职位: %s, 部门: %s, 薪资: %.2f, 绩效: %d分(%s), 技能数: %d", 
                           employeeId, super.getDescription(), position, department, 
                           salary, performanceScore, getPerformanceLevel(), getSkillCount());
    }
    
    @Override
    public String toString() {
        return "Employee{" +
                "employeeId='" + employeeId + '\'' +
                ", position='" + position + '\'' +
                ", department='" + department + '\'' +
                ", salary=" + String.format("%.2f", salary) +
                ", performanceScore=" + performanceScore +
                ", skillCount=" + getSkillCount() +
                ", " + super.toString() +
                '}';
    }
    
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        if (!super.equals(obj)) return false;
        Employee employee = (Employee) obj;
        return employeeId.equals(employee.employeeId) &&
                position.equals(employee.position) &&
                department.equals(employee.department);
    }
    
    @Override
    public int hashCode() {
        return super.hashCode() + employeeId.hashCode() + 
               position.hashCode() + department.hashCode();
    }
}
