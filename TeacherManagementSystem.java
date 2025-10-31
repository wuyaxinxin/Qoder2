/*
 * 文件名: TeacherManagementSystem.java
 * 作者: 开发者
 * 创建日期: 2025-10-27
 * 版本: 1.0
 * 描述: 这是一个教师管理系统类，用于管理教师和课程信息
 * 功能:
 *   - 教师信息管理
 *   - 课程信息管理
 *   - 教学任务分配
 * 依赖: Teacher.java, Course.java
 * 修改记录:
 *   2025-10-27 - 初始版本创建
 */

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * TeacherManagementSystem类 - 教师管理系统的主要实现类
 */
public class TeacherManagementSystem {
    private Map<String, Teacher> teachers;
    private Map<String, Course> courses;
    private Map<String, List<String>> teacherCourses; // 教师ID -> 课程ID列表
    
    /**
     * 默认构造函数
     */
    public TeacherManagementSystem() {
        this.teachers = new HashMap<>();
        this.courses = new HashMap<>();
        this.teacherCourses = new HashMap<>();
    }
    
    /**
     * 添加教师
     * @param teacher 教师对象
     */
    public void addTeacher(Teacher teacher) {
        if (teacher != null && teacher.getTeacherId() != null && !teacher.getTeacherId().isEmpty()) {
            teachers.put(teacher.getTeacherId(), teacher);
            // 初始化教师的课程列表
            teacherCourses.putIfAbsent(teacher.getTeacherId(), new ArrayList<>());
        }
    }
    
    /**
     * 更新教师信息
     * @param teacher 教师对象
     */
    public void updateTeacher(Teacher teacher) {
        if (teacher != null && teacher.getTeacherId() != null && !teacher.getTeacherId().isEmpty()) {
            if (teachers.containsKey(teacher.getTeacherId())) {
                teachers.put(teacher.getTeacherId(), teacher);
            }
        }
    }
    
    /**
     * 删除教师
     * @param teacherId 教师ID
     */
    public void removeTeacher(String teacherId) {
        if (teacherId != null && !teacherId.isEmpty()) {
            teachers.remove(teacherId);
            teacherCourses.remove(teacherId);
        }
    }
    
    /**
     * 根据ID查询教师
     * @param teacherId 教师ID
     * @return 教师对象，如果未找到返回null
     */
    public Teacher getTeacher(String teacherId) {
        if (teacherId != null && !teacherId.isEmpty()) {
            return teachers.get(teacherId);
        }
        return null;
    }
    
    /**
     * 获取所有教师列表
     * @return 教师列表
     */
    public List<Teacher> getAllTeachers() {
        return new ArrayList<>(teachers.values());
    }
    
    /**
     * 添加课程
     * @param course 课程对象
     */
    public void addCourse(Course course) {
        if (course != null && course.getCourseId() != null && !course.getCourseId().isEmpty()) {
            courses.put(course.getCourseId(), course);
        }
    }
    
    /**
     * 更新课程信息
     * @param course 课程对象
     */
    public void updateCourse(Course course) {
        if (course != null && course.getCourseId() != null && !course.getCourseId().isEmpty()) {
            if (courses.containsKey(course.getCourseId())) {
                courses.put(course.getCourseId(), course);
            }
        }
    }
    
    /**
     * 删除课程
     * @param courseId 课程ID
     */
    public void removeCourse(String courseId) {
        if (courseId != null && !courseId.isEmpty()) {
            courses.remove(courseId);
            // 从所有教师的课程列表中移除该课程
            for (List<String> courseList : teacherCourses.values()) {
                courseList.remove(courseId);
            }
        }
    }
    
    /**
     * 根据ID查询课程
     * @param courseId 课程ID
     * @return 课程对象，如果未找到返回null
     */
    public Course getCourse(String courseId) {
        if (courseId != null && !courseId.isEmpty()) {
            return courses.get(courseId);
        }
        return null;
    }
    
    /**
     * 获取所有课程列表
     * @return 课程列表
     */
    public List<Course> getAllCourses() {
        return new ArrayList<>(courses.values());
    }
    
    /**
     * 为教师分配课程
     * @param teacherId 教师ID
     * @param courseId 课程ID
     */
    public void assignCourseToTeacher(String teacherId, String courseId) {
        if (teacherId != null && !teacherId.isEmpty() && 
            courseId != null && !courseId.isEmpty()) {
            // 检查教师和课程是否存在
            if (teachers.containsKey(teacherId) && courses.containsKey(courseId)) {
                teacherCourses.putIfAbsent(teacherId, new ArrayList<>());
                List<String> courseList = teacherCourses.get(teacherId);
                if (!courseList.contains(courseId)) {
                    courseList.add(courseId);
                }
                
                // 更新课程中的教师信息
                Course course = courses.get(courseId);
                Teacher teacher = teachers.get(teacherId);
                course.setInstructor(teacher.getName());
            }
        }
    }
    
    /**
     * 移除教师的课程
     * @param teacherId 教师ID
     * @param courseId 课程ID
     */
    public void removeCourseFromTeacher(String teacherId, String courseId) {
        if (teacherId != null && !teacherId.isEmpty() && 
            courseId != null && !courseId.isEmpty()) {
            List<String> courseList = teacherCourses.get(teacherId);
            if (courseList != null) {
                courseList.remove(courseId);
            }
            
            // 清除课程中的教师信息
            Course course = courses.get(courseId);
            if (course != null) {
                course.setInstructor("");
            }
        }
    }
    
    /**
     * 获取教师的所有课程
     * @param teacherId 教师ID
     * @return 课程列表
     */
    public List<Course> getCoursesForTeacher(String teacherId) {
        List<Course> teacherCoursesList = new ArrayList<>();
        if (teacherId != null && !teacherId.isEmpty()) {
            List<String> courseIds = teacherCourses.get(teacherId);
            if (courseIds != null) {
                for (String courseId : courseIds) {
                    Course course = courses.get(courseId);
                    if (course != null) {
                        teacherCoursesList.add(course);
                    }
                }
            }
        }
        return teacherCoursesList;
    }
    
    /**
     * 获取系统的统计信息
     * @return 统计信息字符串
     */
    public String getSystemStatistics() {
        return String.format("系统统计信息: 教师数量=%d, 课程数量=%d", 
                           teachers.size(), courses.size());
    }
}