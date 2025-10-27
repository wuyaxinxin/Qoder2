/*
 * 文件名: TeacherManagementSystemTest.java
 * 作者: 开发者
 * 创建日期: 2025-10-27
 * 版本: 1.0
 * 描述: 这是一个用于测试TeacherManagementSystem类的测试类
 * 功能:
 *   - 测试教师管理功能
 *   - 测试课程管理功能
 *   - 测试教学任务分配功能
 * 依赖: TeacherManagementSystem.java, Teacher.java, Course.java
 * 修改记录:
 *   2025-10-27 - 初始版本创建
 */

import java.time.LocalDate;
import java.util.List;

/**
 * TeacherManagementSystemTest类 - 用于测试教师管理系统
 */
public class TeacherManagementSystemTest {
    
    public static void main(String[] args) {
        // 创建教师管理系统实例
        TeacherManagementSystem system = new TeacherManagementSystem();
        
        // 测试教师管理功能
        System.out.println("=== 测试教师管理功能 ===");
        
        // 创建教师
        Teacher teacher1 = new Teacher("张老师", 35, "zhang@school.com", "T001", "数学", "副教授", 12);
        Teacher teacher2 = new Teacher("李老师", 28, "li@school.com", "T002", "英语", "讲师", 5);
        
        // 添加教师
        system.addTeacher(teacher1);
        system.addTeacher(teacher2);
        
        // 查询教师
        Teacher retrievedTeacher = system.getTeacher("T001");
        System.out.println("查询到的教师: " + retrievedTeacher.getDescription());
        
        // 获取所有教师
        List<Teacher> allTeachers = system.getAllTeachers();
        System.out.println("系统中的教师数量: " + allTeachers.size());
        
        // 测试课程管理功能
        System.out.println("\n=== 测试课程管理功能 ===");
        
        // 创建课程
        Course course1 = new Course("C001", "高等数学", "", 4, "高等数学课程", 
                                   LocalDate.now(), LocalDate.now().plusMonths(4));
        Course course2 = new Course("C002", "大学英语", "", 3, "大学英语课程", 
                                   LocalDate.now(), LocalDate.now().plusMonths(4));
        
        // 添加课程
        system.addCourse(course1);
        system.addCourse(course2);
        
        // 查询课程
        Course retrievedCourse = system.getCourse("C001");
        System.out.println("查询到的课程: " + retrievedCourse.getCourseDescription());
        
        // 获取所有课程
        List<Course> allCourses = system.getAllCourses();
        System.out.println("系统中的课程数量: " + allCourses.size());
        
        // 测试教学任务分配功能
        System.out.println("\n=== 测试教学任务分配功能 ===");
        
        // 为教师分配课程
        system.assignCourseToTeacher("T001", "C001");
        system.assignCourseToTeacher("T002", "C002");
        
        // 获取教师的课程
        List<Course> teacher1Courses = system.getCoursesForTeacher("T001");
        System.out.println("张老师的课程数量: " + teacher1Courses.size());
        if (!teacher1Courses.isEmpty()) {
            System.out.println("张老师的课程: " + teacher1Courses.get(0).getCourseName());
        }
        
        List<Course> teacher2Courses = system.getCoursesForTeacher("T002");
        System.out.println("李老师的课程数量: " + teacher2Courses.size());
        if (!teacher2Courses.isEmpty()) {
            System.out.println("李老师的课程: " + teacher2Courses.get(0).getCourseName());
        }
        
        // 测试系统统计信息
        System.out.println("\n=== 系统统计信息 ===");
        System.out.println(system.getSystemStatistics());
        
        System.out.println("\n=== 测试完成 ===");
    }
}