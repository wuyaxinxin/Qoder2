package com.example.bean;

import java.io.Serializable;

/**
 * Employee JavaBean类
 * 遵循JavaBean规范的员工信息类
 */
public class Employee implements Serializable {
    
    private static final long serialVersionUID = 1L;
    
    // 私有属性
    private Long id;
    private String name;
    private String department;
    private Double salary;
    private Integer age;
    
    /**
     * 无参构造器
     */
    public Employee() {
    }
    
    /**
     * 全参构造器
     */
    public Employee(Long id, String name, String department, Double salary, Integer age) {
        this.id = id;
        this.name = name;
        this.department = department;
        this.salary = salary;
        this.age = age;
    }
    
    // Getter和Setter方法
    public Long getId() {
        return id;
    }
    
    public void setId(Long id) {
        this.id = id;
    }
    
    public String getName() {
        return name;
    }
    
    public void setName(String name) {
        this.name = name;
    }
    
    public String getDepartment() {
        return department;
    }
    
    public void setDepartment(String department) {
        this.department = department;
    }
    
    public Double getSalary() {
        return salary;
    }
    
    public void setSalary(Double salary) {
        this.salary = salary;
    }
    
    public Integer getAge() {
        return age;
    }
    
    public void setAge(Integer age) {
        this.age = age;
    }
    
    @Override
    public String toString() {
        return "Employee{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", department='" + department + '\'' +
                ", salary=" + salary +
                ", age=" + age +
                '}';
    }
    
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        
        Employee employee = (Employee) o;
        
        if (id != null ? !id.equals(employee.id) : employee.id != null) return false;
        return name != null ? name.equals(employee.name) : employee.name == null;
    }
    
    @Override
    public int hashCode() {
        int result = id != null ? id.hashCode() : 0;
        result = 31 * result + (name != null ? name.hashCode() : 0);
        return result;
    }
}
