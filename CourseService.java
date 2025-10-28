/*
 * 文件名: CourseService.java
 * 作者: 开发者
 * 创建日期: 2025-10-28
 * 版本: 1.0
 * 描述: 课程服务类,提供课程信息管理的业务逻辑
 * 功能:
 *   - 课程的创建、查询、修改、删除
 *   - 学生选课和退课
 *   - 课程选课学生查询
 *   - 教师授课列表查询
 * 依赖: Course.java, Student.java, DataStorage.java
 * 修改记录:
 *   2025-10-28 - 初始版本创建
 */

import java.time.LocalDate;
import java.util.*;
import java.util.stream.Collectors;

/**
 * CourseService类 - 课程服务业务逻辑
 */
public class CourseService {
    private DataStorage storage;
    
    /**
     * 构造函数
     * @param storage 数据存储对象
     */
    public CourseService(DataStorage storage) {
        this.storage = storage;
    }
    
    /**
     * 创建新课程
     * @param course 课程对象
     * @return 操作结果消息
     */
    public String createCourse(Course course) {
        if (course == null) {
            return "错误:课程对象不能为空";
        }
        
        // 验证课程ID唯一性
        if (getCourseById(course.getCourseId()) != null) {
            return "错误:课程ID已存在,请使用其他ID";
        }
        
        // 验证输入
        String validation = validateCourse(course);
        if (!validation.equals("验证通过")) {
            return validation;
        }
        
        List<Course> courses = storage.getCourses();
        courses.add(course);
        storage.setCourses(courses);
        
        if (storage.saveCourses()) {
            return "成功:课程创建成功";
        } else {
            return "错误:保存课程数据失败";
        }
    }
    
    /**
     * 根据课程ID查询课程
     * @param courseId 课程ID
     * @return 课程对象,不存在则返回null
     */
    public Course getCourseById(String courseId) {
        if (courseId == null || courseId.trim().isEmpty()) {
            return null;
        }
        
        return storage.getCourses().stream()
            .filter(c -> c.getCourseId().equals(courseId))
            .findFirst()
            .orElse(null);
    }
    
    /**
     * 更新课程信息
     * @param course 课程对象
     * @return 操作结果消息
     */
    public String updateCourse(Course course) {
        if (course == null) {
            return "错误:课程对象不能为空";
        }
        
        List<Course> courses = storage.getCourses();
        int index = -1;
        for (int i = 0; i < courses.size(); i++) {
            if (courses.get(i).getCourseId().equals(course.getCourseId())) {
                index = i;
                break;
            }
        }
        
        if (index == -1) {
            return "错误:课程不存在";
        }
        
        // 验证输入
        String validation = validateCourse(course);
        if (!validation.equals("验证通过")) {
            return validation;
        }
        
        courses.set(index, course);
        storage.setCourses(courses);
        
        if (storage.saveCourses()) {
            return "成功:课程信息更新成功";
        } else {
            return "错误:保存课程数据失败";
        }
    }
    
    /**
     * 删除课程
     * @param courseId 课程ID
     * @return 操作结果消息
     */
    public String deleteCourse(String courseId) {
        if (courseId == null || courseId.trim().isEmpty()) {
            return "错误:课程ID不能为空";
        }
        
        List<Course> courses = storage.getCourses();
        Course toRemove = null;
        for (Course c : courses) {
            if (c.getCourseId().equals(courseId)) {
                toRemove = c;
                break;
            }
        }
        
        if (toRemove == null) {
            return "错误:课程不存在";
        }
        
        // 清空选课学生
        int enrolledCount = toRemove.getEnrolledStudentCount();
        
        courses.remove(toRemove);
        storage.setCourses(courses);
        
        // 同步清理学生成绩记录
        List<Student> students = storage.getStudents();
        boolean studentUpdated = false;
        for (Student student : students) {
            if (student.getScore(courseId) != -1.0) {
                student.removeScore(courseId);
                studentUpdated = true;
            }
        }
        if (studentUpdated) {
            storage.setStudents(students);
            storage.saveStudents();
        }
        
        if (storage.saveCourses()) {
            return String.format("成功:课程删除成功,已清理%d个选课记录", enrolledCount);
        } else {
            return "错误:保存课程数据失败";
        }
    }
    
    /**
     * 学生选课
     * @param courseId 课程ID
     * @param studentId 学号
     * @return 操作结果消息
     */
    public String enrollStudent(String courseId, String studentId) {
        if (courseId == null || courseId.trim().isEmpty()) {
            return "错误:课程ID不能为空";
        }
        if (studentId == null || studentId.trim().isEmpty()) {
            return "错误:学号不能为空";
        }
        
        // 验证学生是否存在
        Student student = storage.getStudents().stream()
            .filter(s -> s.getStudentId().equals(studentId))
            .findFirst()
            .orElse(null);
        
        if (student == null) {
            return "错误:学生不存在";
        }
        
        // 验证课程是否存在
        Course course = getCourseById(courseId);
        if (course == null) {
            return "错误:课程不存在";
        }
        
        // 检查是否已选
        if (course.isStudentEnrolled(studentId)) {
            return "错误:学生已选该课程,无需重复选课";
        }
        
        // 添加选课记录
        course.enrollStudent(studentId);
        
        // 初始化成绩为0(未录入)
        student.addScore(courseId, 0);
        
        // 保存数据
        return updateCourse(course);
    }
    
    /**
     * 学生退课
     * @param courseId 课程ID
     * @param studentId 学号
     * @return 操作结果消息
     */
    public String dropStudent(String courseId, String studentId) {
        if (courseId == null || courseId.trim().isEmpty()) {
            return "错误:课程ID不能为空";
        }
        if (studentId == null || studentId.trim().isEmpty()) {
            return "错误:学号不能为空";
        }
        
        Course course = getCourseById(courseId);
        if (course == null) {
            return "错误:课程不存在";
        }
        
        if (!course.isStudentEnrolled(studentId)) {
            return "错误:学生未选该课程";
        }
        
        course.dropStudent(studentId);
        
        // 删除成绩记录
        List<Student> students = storage.getStudents();
        for (Student student : students) {
            if (student.getStudentId().equals(studentId)) {
                student.removeScore(courseId);
                storage.setStudents(students);
                storage.saveStudents();
                break;
            }
        }
        
        if (updateCourse(course).startsWith("成功")) {
            return "成功:退课成功";
        } else {
            return "错误:保存课程数据失败";
        }
    }
    
    /**
     * 获取课程已选学生列表
     * @param courseId 课程ID
     * @return 学生列表
     */
    public List<Student> getEnrolledStudents(String courseId) {
        Course course = getCourseById(courseId);
        if (course == null) {
            return new ArrayList<>();
        }
        
        List<String> enrolledIds = course.getEnrolledStudents();
        return storage.getStudents().stream()
            .filter(s -> enrolledIds.contains(s.getStudentId()))
            .collect(Collectors.toList());
    }
    
    /**
     * 查询教师授课列表
     * @param teacherId 教师ID
     * @return 课程列表
     */
    public List<Course> getCoursesByInstructor(String teacherId) {
        if (teacherId == null || teacherId.trim().isEmpty()) {
            return new ArrayList<>();
        }
        
        return storage.getCourses().stream()
            .filter(c -> c.getInstructor().equals(teacherId))
            .collect(Collectors.toList());
    }
    
    /**
     * 获取所有课程
     * @return 课程列表
     */
    public List<Course> getAllCourses() {
        return storage.getCourses();
    }
    
    /**
     * 验证课程信息
     * @param course 课程对象
     * @return 验证结果消息
     */
    private String validateCourse(Course course) {
        // 验证课程ID
        if (course.getCourseId() == null || course.getCourseId().trim().isEmpty()) {
            return "错误:课程ID不能为空";
        }
        if (course.getCourseId().length() > 20) {
            return "错误:课程ID长度不能超过20字符";
        }
        if (!course.getCourseId().matches("[a-zA-Z0-9]+")) {
            return "错误:课程ID只能包含字母和数字";
        }
        
        // 验证课程名称
        if (course.getCourseName() == null || course.getCourseName().trim().isEmpty()) {
            return "错误:课程名称不能为空";
        }
        
        // 验证授课教师
        if (course.getInstructor() == null || course.getInstructor().trim().isEmpty()) {
            return "错误:授课教师不能为空";
        }
        
        // 验证学分
        if (course.getCreditHours() < 1 || course.getCreditHours() > 8) {
            return "错误:学分必须在1-8之间";
        }
        
        // 验证日期
        if (course.getStartDate() == null || course.getEndDate() == null) {
            return "错误:开始日期和结束日期不能为空";
        }
        if (!course.getEndDate().isAfter(course.getStartDate())) {
            return "错误:结束日期必须晚于开始日期";
        }
        
        return "验证通过";
    }
    
    /**
     * 按选课人数排序课程
     * @return 排序后的课程列表
     */
    public List<Course> getCoursesByEnrollmentCount() {
        List<Course> courses = new ArrayList<>(storage.getCourses());
        courses.sort((c1, c2) -> 
            Integer.compare(c2.getEnrolledStudentCount(), c1.getEnrolledStudentCount()));
        return courses;
    }
}
