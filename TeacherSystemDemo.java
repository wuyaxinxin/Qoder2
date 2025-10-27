/*
 * 文件名: TeacherSystemDemo.java
 * 作者: 开发者
 * 创建日期: 2025-10-27
 * 版本: 1.0
 * 描述: 这是一个演示教师管理系统使用的示例类
 * 功能:
 *   - 演示教师管理系统的完整使用流程
 *   - 展示教师、课程和教学任务的管理
 * 依赖: TeacherManagementSystem.java, Teacher.java, Course.java
 * 修改记录:
 *   2025-10-27 - 初始版本创建
 */

import java.time.LocalDate;
import java.util.List;

/**
 * TeacherSystemDemo类 - 教师管理系统的演示类
 */
public class TeacherSystemDemo {
    
    public static void main(String[] args) {
        System.out.println("欢迎使用教师管理系统演示");
        System.out.println("========================");
        
        // 创建教师管理系统实例
        TeacherManagementSystem system = new TeacherManagementSystem();
        
        // 1. 添加教师
        System.out.println("1. 添加教师");
        Teacher teacher1 = new Teacher("王教授", 45, "wang@university.edu", "T001", "计算机科学", "教授", 20);
        Teacher teacher2 = new Teacher("刘讲师", 32, "liu@university.edu", "T002", "数据结构", "讲师", 8);
        Teacher teacher3 = new Teacher("陈副教授", 38, "chen@university.edu", "T003", "人工智能", "副教授", 15);
        
        system.addTeacher(teacher1);
        system.addTeacher(teacher2);
        system.addTeacher(teacher3);
        
        System.out.println("已添加3名教师到系统中");
        
        // 2. 添加课程
        System.out.println("\n2. 添加课程");
        Course course1 = new Course("CS101", "计算机科学导论", "", 3, "计算机科学入门课程", 
                                   LocalDate.of(2025, 9, 1), LocalDate.of(2026, 1, 31));
        Course course2 = new Course("CS201", "数据结构与算法", "", 4, "数据结构深入学习", 
                                   LocalDate.of(2025, 9, 1), LocalDate.of(2026, 1, 31));
        Course course3 = new Course("CS301", "人工智能基础", "", 3, "人工智能入门课程", 
                                   LocalDate.of(2025, 9, 1), LocalDate.of(2026, 1, 31));
        Course course4 = new Course("CS401", "机器学习", "", 3, "机器学习高级课程", 
                                   LocalDate.of(2025, 9, 1), LocalDate.of(2026, 1, 31));
        
        system.addCourse(course1);
        system.addCourse(course2);
        system.addCourse(course3);
        system.addCourse(course4);
        
        System.out.println("已添加4门课程到系统中");
        
        // 3. 为教师分配课程
        System.out.println("\n3. 为教师分配课程");
        system.assignCourseToTeacher("T001", "CS101");
        system.assignCourseToTeacher("T002", "CS201");
        system.assignCourseToTeacher("T003", "CS301");
        system.assignCourseToTeacher("T003", "CS401");
        
        System.out.println("已为教师分配课程");
        
        // 4. 查询教师信息
        System.out.println("\n4. 查询教师信息");
        Teacher teacher = system.getTeacher("T003");
        if (teacher != null) {
            System.out.println("查询到的教师信息: " + teacher.getDescription());
            
            // 查询该教师的课程
            List<Course> courses = system.getCoursesForTeacher("T003");
            System.out.println("该教师教授的课程数量: " + courses.size());
            for (Course course : courses) {
                System.out.println("  - " + course.getCourseName());
            }
        }
        
        // 5. 查询课程信息
        System.out.println("\n5. 查询课程信息");
        Course course = system.getCourse("CS201");
        if (course != null) {
            System.out.println("查询到的课程信息: " + course.getCourseDescription());
            System.out.println("授课教师: " + course.getInstructor());
        }
        
        // 6. 显示系统统计信息
        System.out.println("\n6. 系统统计信息");
        System.out.println(system.getSystemStatistics());
        
        // 7. 显示所有教师信息
        System.out.println("\n7. 所有教师信息");
        List<Teacher> allTeachers = system.getAllTeachers();
        for (Teacher t : allTeachers) {
            System.out.println(t.getDescription());
        }
        
        // 8. 显示所有课程信息
        System.out.println("\n8. 所有课程信息");
        List<Course> allCourses = system.getAllCourses();
        for (Course c : allCourses) {
            System.out.println(c.getCourseDescription());
        }
        
        System.out.println("\n演示完成！");
    }
}