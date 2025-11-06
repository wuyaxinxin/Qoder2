/*
 * 文件名: Department.java
 * 作者: 开发者
 * 创建日期: 2025-10-27
 * 版本: 1.0
 * 描述: 这是一个表示部门信息的Java类文件
 *       用于管理部门的基本信息和员工列表
 * 功能:
 *   - 存储和管理部门基本信息
 *   - 管理部门员工列表
 *   - 提供部门统计功能
 *   - 实现部门规模判断
 * 依赖: 无外部依赖，仅使用Java标准库
 * 修改记录:
 *   2025-10-27 - 初始版本创建
 */

import java.util.ArrayList;
import java.util.List;

/**
 * Department类 - 表示一个部门的完整信息
 */
public class Department {
    private String departmentId;
    private String departmentName;
    private String location;
    private String manager;
    private List<String> employeeIds;
    private double budget;
    
    /**
     * 默认构造函数
     */
    public Department() {
        this.departmentId = "";
        this.departmentName = "";
        this.location = "";
        this.manager = "";
        this.employeeIds = new ArrayList<>();
        this.budget = 0.0;
    }
    
    /**
     * 带参数的构造函数
     * @param departmentId 部门ID
     * @param departmentName 部门名称
     * @param location 部门位置
     * @param manager 部门经理
     * @param budget 部门预算
     */
    public Department(String departmentId, String departmentName, String location, 
                     String manager, double budget) {
        this.departmentId = departmentId;
        this.departmentName = departmentName;
        this.location = location;
        this.manager = manager;
        this.budget = budget;
        this.employeeIds = new ArrayList<>();
    }
    
    /**
     * 获取部门ID
     * @return 部门ID
     */
    public String getDepartmentId() {
        return departmentId;
    }
    
    /**
     * 设置部门ID
     * @param departmentId 部门ID
     */
    public void setDepartmentId(String departmentId) {
        this.departmentId = departmentId;
    }
    
    /**
     * 获取部门名称
     * @return 部门名称
     */
    public String getDepartmentName() {
        return departmentName;
    }
    
    /**
     * 设置部门名称
     * @param departmentName 部门名称
     */
    public void setDepartmentName(String departmentName) {
        this.departmentName = departmentName;
    }
    
    /**
     * 获取部门位置
     * @return 部门位置
     */
    public String getLocation() {
        return location;
    }
    
    /**
     * 设置部门位置
     * @param location 部门位置
     */
    public void setLocation(String location) {
        this.location = location;
    }
    
    /**
     * 获取部门经理
     * @return 部门经理姓名
     */
    public String getManager() {
        return manager;
    }
    
    /**
     * 设置部门经理
     * @param manager 部门经理姓名
     */
    public void setManager(String manager) {
        this.manager = manager;
    }
    
    /**
     * 获取部门预算
     * @return 部门预算
     */
    public double getBudget() {
        return budget;
    }
    
    /**
     * 设置部门预算
     * @param budget 部门预算
     */
    public void setBudget(double budget) {
        if (budget >= 0) {
            this.budget = budget;
        }
    }
    
    /**
     * 添加员工到部门
     * @param employeeId 员工ID
     */
    public void addEmployee(String employeeId) {
        if (!employeeIds.contains(employeeId)) {
            employeeIds.add(employeeId);
        }
    }
    
    /**
     * 从部门移除员工
     * @param employeeId 员工ID
     * @return 如果移除成功返回true，否则返回false
     */
    public boolean removeEmployee(String employeeId) {
        return employeeIds.remove(employeeId);
    }
    
    /**
     * 获取所有员工ID列表
     * @return 员工ID列表
     */
    public List<String> getAllEmployeeIds() {
        return new ArrayList<>(employeeIds);
    }
    
    /**
     * 获取员工数量
     * @return 员工数量
     */
    public int getEmployeeCount() {
        return employeeIds.size();
    }
    
    /**
     * 检查是否包含指定员工
     * @param employeeId 员工ID
     * @return 如果包含该员工返回true，否则返回false
     */
    public boolean hasEmployee(String employeeId) {
        return employeeIds.contains(employeeId);
    }
    
    /**
     * 判断是否为大型部门（员工数>=50）
     * @return 如果员工数大于等于50则返回true
     */
    public boolean isLargeDepartment() {
        return employeeIds.size() >= 50;
    }
    
    /**
     * 计算人均预算
     * @return 人均预算，如果没有员工则返回0
     */
    public double getBudgetPerEmployee() {
        if (employeeIds.isEmpty()) {
            return 0.0;
        }
        return budget / employeeIds.size();
    }
    
    /**
     * 清空所有员工
     */
    public void clearAllEmployees() {
        employeeIds.clear();
    }
    
    /**
     * 增加预算
     * @param amount 增加金额
     */
    public void increaseBudget(double amount) {
        if (amount > 0) {
            this.budget += amount;
        }
    }
    
    /**
     * 减少预算
     * @param amount 减少金额
     * @return 如果操作成功返回true，否则返回false
     */
    public boolean decreaseBudget(double amount) {
        if (amount > 0 && this.budget >= amount) {
            this.budget -= amount;
            return true;
        }
        return false;
    }
    
    /**
     * 获取部门信息描述
     * @return 部门信息字符串
     */
    public String getDescription() {
        return String.format("部门ID: %s, 部门名称: %s, 位置: %s, 经理: %s, 员工数: %d, 预算: %.2f", 
                           departmentId, departmentName, location, manager, 
                           getEmployeeCount(), budget);
    }
    
    @Override
    public String toString() {
        return "Department{" +
                "departmentId='" + departmentId + '\'' +
                ", departmentName='" + departmentName + '\'' +
                ", location='" + location + '\'' +
                ", manager='" + manager + '\'' +
                ", employeeCount=" + getEmployeeCount() +
                ", budget=" + String.format("%.2f", budget) +
                '}';
    }
    
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Department that = (Department) obj;
        return departmentId.equals(that.departmentId) &&
                departmentName.equals(that.departmentName) &&
                location.equals(that.location);
    }
    
    @Override
    public int hashCode() {
        return departmentId.hashCode() + departmentName.hashCode() + location.hashCode();
    }
}
