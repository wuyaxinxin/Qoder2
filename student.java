// 仙剑奇侠传
// 始终生效

public class Student {
    private String name;
    private int age;
    private String studentId;
    private String email;
    private String major;
    
    public Student(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    public Student(String name, int age, String studentId, String email, String major) {
        this.name = name;
        this.age = age;
        this.studentId = studentId;
        this.email = email;
        this.major = major;
    }
    
    public String getName() {
        return name;
    }
    
    public int getAge() {
        return age;
    }
    
    public String getStudentId() {
        return studentId;
    }
    
    public String getEmail() {
        return email;
    }
    
    public String getMajor() {
        return major;
    }
    
    public void setName(String name) {
        this.name = name;
    }
    
    public void setAge(int age) {
        this.age = age;
    }
    
    public void setStudentId(String studentId) {
        this.studentId = studentId;
    }
    
    public void setEmail(String email) {
        this.email = email;
    }
    
    public void setMajor(String major) {
        this.major = major;
    }
    
    @Override
    public String toString() {
        return "Student: [name: " + name + ", age: " + age + ", studentId: " + studentId + ", email: " + email + ", major: " + major + "]";
    }
}
