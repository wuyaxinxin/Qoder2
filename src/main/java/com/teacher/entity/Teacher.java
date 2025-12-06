// 始终生效
package com.teacher.entity;

public class Teacher {
    private Integer id;
    private String name;
    private Integer age;
    private String subject;
    private String phone;
    private String email;

    public Teacher() {}

    public Teacher(Integer id, String name, Integer age, String subject, String phone, String email) {
        this.id = id;
        this.name = name;
        this.age = age;
        this.subject = subject;
        this.phone = phone;
        this.email = email;
    }

    public Integer getId() { return id; }
    public void setId(Integer id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public Integer getAge() { return age; }
    public void setAge(Integer age) { this.age = age; }
    public String getSubject() { return subject; }
    public void setSubject(String subject) { this.subject = subject; }
    public String getPhone() { return phone; }
    public void setPhone(String phone) { this.phone = phone; }
    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }

    @Override
    public String toString() {
        return "Teacher{id=" + id + ", name='" + name + "', age=" + age + 
               ", subject='" + subject + "', phone='" + phone + "', email='" + email + "'}";
    }
}
