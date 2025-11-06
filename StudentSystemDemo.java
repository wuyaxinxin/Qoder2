/*
 * 文件名: StudentSystemDemo.java
 * 作者: 开发者
 * 创建日期: 2025-10-28
 * 版本: 1.0
 * 描述: 学生管理系统演示程序,展示系统完整功能
 */

import java.time.LocalDate;

public class StudentSystemDemo {
    public static void main(String[] args) {
        System.out.println("========== 学生管理系统演示 ==========\n");
        
        // 初始化数据存储
        DataStorage storage = new DataStorage();
        storage.loadAll();
        
        // 初始化服务
        StudentService studentService = new StudentService(storage);
        CourseService courseService = new CourseService(storage);
        TeacherService teacherService = new TeacherService(storage);
        GradeService gradeService = new GradeService(storage);
        
        // 演示1: 创建教师
        System.out.println("【演示1】创建教师");
        Teacher teacher1 = new Teacher("张教授", 45, "zhang@example.com", 
            "T001", "计算机科学", "教授", 15);
        String result = teacherService.createTeacher(teacher1);
        System.out.println(result);
        
        // 演示2: 创建课程
        System.out.println("\n【演示2】创建课程");
        Course course1 = new Course("CS101", "数据结构与算法", "T001", 
            4, "计算机科学基础课程", 
            LocalDate.of(2025, 9, 1), LocalDate.of(2026, 1, 15));
        result = courseService.createCourse(course1);
        System.out.println(result);
        
        Course course2 = new Course("CS102", "操作系统原理", "T001",
            4, "操作系统核心概念",
            LocalDate.of(2025, 9, 1), LocalDate.of(2026, 1, 15));
        result = courseService.createCourse(course2);
        System.out.println(result);
        
        // 演示3: 创建学生
        System.out.println("\n【演示3】创建学生");
        Student student1 = new Student("李明", 20, "liming@example.com",
            "2021001", "计算机科学", 3);
        result = studentService.createStudent(student1);
        System.out.println(result);
        
        Student student2 = new Student("王芳", 21, "wangfang@example.com",
            "2021002", "计算机科学", 3);
        result = studentService.createStudent(student2);
        System.out.println(result);
        
        // 演示4: 学生选课
        System.out.println("\n【演示4】学生选课");
        result = courseService.enrollStudent("CS101", "2021001");
        System.out.println(result);
        result = courseService.enrollStudent("CS101", "2021002");
        System.out.println(result);
        result = courseService.enrollStudent("CS102", "2021001");
        System.out.println(result);
        
        // 演示5: 录入成绩
        System.out.println("\n【演示5】录入成绩");
        result = gradeService.recordGrade("2021001", "CS101", 92.5);
        System.out.println(result);
        result = gradeService.recordGrade("2021002", "CS101", 88.0);
        System.out.println(result);
        result = gradeService.recordGrade("2021001", "CS102", 85.5);
        System.out.println(result);
        
        // 演示6: 查询学生成绩
        System.out.println("\n【演示6】查询学生成绩");
        java.util.List<GradeService.GradeRecord> grades = gradeService.getStudentGrades("2021001");
        System.out.println("李明的成绩单:");
        for (GradeService.GradeRecord grade : grades) {
            System.out.println("  " + grade);
        }
        
        double avg = gradeService.calculateAverage("2021001");
        System.out.println("平均分: " + String.format("%.2f", avg));
        
        // 演示7: 查询优秀学生
        System.out.println("\n【演示7】查询优秀学生");
        java.util.List<Student> excellentStudents = studentService.getExcellentStudents();
        System.out.println("优秀学生名单:");
        for (Student student : excellentStudents) {
            System.out.println("  " + student.getDescription());
        }
        
        // 演示8: 查询课程选课情况
        System.out.println("\n【演示8】查询课程选课情况");
        java.util.List<Student> enrolledStudents = courseService.getEnrolledStudents("CS101");
        System.out.println("数据结构与算法 选课学生:");
        for (Student student : enrolledStudents) {
            System.out.println("  " + student.getName() + " (" + student.getStudentId() + ")");
        }
        
        // 演示9: 计算课程通过率
        System.out.println("\n【演示9】计算课程通过率");
        double passRate = gradeService.getCoursePassRate("CS101");
        System.out.println("数据结构与算法 通过率: " + String.format("%.2f%%", passRate));
        
        System.out.println("\n========== 演示完成 ==========");
        System.out.println("提示: 数据已保存到 data/ 目录");
        System.out.println("可使用 Python 脚本生成数据分析报表");
    }
}
