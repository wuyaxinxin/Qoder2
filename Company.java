/*
 * 文件名: Company.java
 * 作者: 开发者
 * 创建日期: 2025-10-27
 * 版本: 1.0
 * 描述: 这是一个表示公司信息的Java类文件
 *       包含公司基本信息和员工管理功能
 * 功能:
 *   - 存储和管理公司基本信息
 *   - 管理公司员工列表
 *   - 提供员工增删查改功能
 *   - 计算公司统计数据(员工总数、平均工资等)
 * 依赖: Employee.java
 * 修改记录:
 *   2025-10-27 - 初始版本创建
 */

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

/**
 * Company类 - 表示一个公司的完整信息
 * 包含公司基本信息和员工管理功能
 */
public class Company {
    private String companyName;
    private String address;
    private String industry;
    private String foundedDate;
    private List<Employee> employees;
    
    /**
     * 默认构造函数
     */
    public Company() {
        this.companyName = "";
        this.address = "";
        this.industry = "";
        this.foundedDate = "";
        this.employees = new ArrayList<>();
    }
    
    /**
     * 带参数的构造函数
     * @param companyName 公司名称
     * @param address 公司地址
     * @param industry 所属行业
     * @param foundedDate 成立日期
     */
    public Company(String companyName, String address, String industry, String foundedDate) {
        this.companyName = companyName;
        this.address = address;
        this.industry = industry;
        this.foundedDate = foundedDate;
        this.employees = new ArrayList<>();
    }
    
    /**
     * 获取公司名称
     * @return 公司名称
     */
    public String getCompanyName() {
        return companyName;
    }
    
    /**
     * 设置公司名称
     * @param companyName 公司名称
     */
    public void setCompanyName(String companyName) {
        this.companyName = companyName;
    }
    
    /**
     * 获取公司地址
     * @return 公司地址
     */
    public String getAddress() {
        return address;
    }
    
    /**
     * 设置公司地址
     * @param address 公司地址
     */
    public void setAddress(String address) {
        this.address = address;
    }
    
    /**
     * 获取所属行业
     * @return 所属行业
     */
    public String getIndustry() {
        return industry;
    }
    
    /**
     * 设置所属行业
     * @param industry 所属行业
     */
    public void setIndustry(String industry) {
        this.industry = industry;
    }
    
    /**
     * 获取成立日期
     * @return 成立日期
     */
    public String getFoundedDate() {
        return foundedDate;
    }
    
    /**
     * 设置成立日期
     * @param foundedDate 成立日期
     */
    public void setFoundedDate(String foundedDate) {
        this.foundedDate = foundedDate;
    }
    
    /**
     * 添加员工
     * @param employee 员工对象
     * @return 如果添加成功返回true，否则返回false
     */
    public boolean addEmployee(Employee employee) {
        if (employee != null && !employees.contains(employee)) {
            employees.add(employee);
            return true;
        }
        return false;
    }
    
    /**
     * 根据员工ID删除员工
     * @param employeeId 员工ID
     * @return 如果删除成功返回true，否则返回false
     */
    public boolean removeEmployee(String employeeId) {
        return employees.removeIf(emp -> emp.getEmployeeId().equals(employeeId));
    }
    
    /**
     * 根据员工ID查找员工
     * @param employeeId 员工ID
     * @return 员工对象，如果未找到则返回null
     */
    public Employee findEmployeeById(String employeeId) {
        return employees.stream()
                .filter(emp -> emp.getEmployeeId().equals(employeeId))
                .findFirst()
                .orElse(null);
    }
    
    /**
     * 根据部门查找员工列表
     * @param department 部门名称
     * @return 该部门的员工列表
     */
    public List<Employee> findEmployeesByDepartment(String department) {
        return employees.stream()
                .filter(emp -> emp.getDepartment().equals(department))
                .collect(Collectors.toList());
    }
    
    /**
     * 获取员工总数
     * @return 员工总数
     */
    public int getEmployeeCount() {
        return employees.size();
    }
    
    /**
     * 计算平均工资
     * @return 平均工资，如果没有员工则返回0
     */
    public double getAverageSalary() {
        if (employees.isEmpty()) {
            return 0.0;
        }
        return employees.stream()
                .mapToDouble(Employee::getSalary)
                .average()
                .orElse(0.0);
    }
    
    /**
     * 获取工资最高的员工
     * @return 工资最高的员工，如果没有员工则返回null
     */
    public Employee getHighestPaidEmployee() {
        return employees.stream()
                .max((e1, e2) -> Double.compare(e1.getSalary(), e2.getSalary()))
                .orElse(null);
    }
    
    /**
     * 获取所有员工列表
     * @return 员工列表的副本
     */
    public List<Employee> getAllEmployees() {
        return new ArrayList<>(employees);
    }
    
    /**
     * 清空所有员工
     */
    public void clearAllEmployees() {
        employees.clear();
    }
    
    /**
     * 检查公司是否有员工
     * @return 如果有员工返回true，否则返回false
     */
    public boolean hasEmployees() {
        return !employees.isEmpty();
    }
    
    /**
     * 获取公司信息描述
     * @return 公司信息字符串
     */
    public String getDescription() {
        return String.format("公司名称: %s, 地址: %s, 行业: %s, 成立日期: %s, 员工人数: %d", 
                           companyName, address, industry, foundedDate, employees.size());
    }
    
    @Override
    public String toString() {
        return "Company{" +
                "companyName='" + companyName + '\'' +
                ", address='" + address + '\'' +
                ", industry='" + industry + '\'' +
                ", foundedDate='" + foundedDate + '\'' +
                ", employeeCount=" + employees.size() +
                ", averageSalary=" + String.format("%.2f", getAverageSalary()) +
                '}';
    }
    
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Company company = (Company) obj;
        return companyName.equals(company.companyName) &&
                address.equals(company.address) &&
                foundedDate.equals(company.foundedDate);
    }
    
    @Override
    public int hashCode() {
        return companyName.hashCode() + address.hashCode() + foundedDate.hashCode();
    }
}
