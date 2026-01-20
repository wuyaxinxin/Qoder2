public class Student {
    private String name;
    private int age;
    private String studentId;
    private double gpa;
    
    // 构造函数
    public Student(String name, int age, String studentId, double gpa) {
        this.name = name;
        this.age = age;
        this.studentId = studentId;
        this.gpa = gpa;
    }
    
    // Getter方法
    public String getName() {
        return name;
    }
    
    public int getAge() {
        return age;
    }
    
    public String getStudentId() {
        return studentId;
    }
    
    public double getGpa() {
        return gpa;
    }
    
    // Setter方法
    public void setName(String name) {
        this.name = name;
    }
    
    public void setAge(int age) {
        if(age > 0 && age < 150) { // 年龄合理性检查
            this.age = age;
        } else {
            System.out.println("年龄输入不合理！");
        }
    }
    
    public void setGpa(double gpa) {
        if(gpa >= 0.0 && gpa <= 4.0) { // GPA范围检查
            this.gpa = gpa;
        } else {
            System.out.println("GPA输入不合理！应在0.0到4.0之间");
        }
    }
    
    // 显示学生信息
    public void displayInfo() {
        System.out.println("姓名: " + name);
        System.out.println("年龄: " + age);
        System.out.println("学号: " + studentId);
        System.out.println("GPA: " + gpa);
    }
    
    public static void main(String[] args) {
        // 创建示例学生对象
        Student student1 = new Student("张三", 20, "2023001", 3.75);
        Student student2 = new Student("李四", 19, "2023002", 3.92);
        
        System.out.println("学生信息:");
        student1.displayInfo();
        System.out.println();
        student2.displayInfo();
        
        // 修改学生信息
        student1.setGpa(3.80);
        System.out.println("\n修改后的学生1 GPA:");
        student1.displayInfo();
    }
}