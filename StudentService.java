/*
 * 文件名: StudentService.java
 * 作者: 开发者
 * 创建日期: 2025-10-28
 * 版本: 1.0
 * 描述: 学生服务类,提供学生信息管理的业务逻辑
 * 功能:
 *   - 学生的创建、查询、修改、删除
 *   - 学生成绩管理
 *   - 优秀学生查询
 *   - 多条件学生搜索
 * 依赖: Student.java, DataStorage.java
 * 修改记录:
 *   2025-10-28 - 初始版本创建
 */

import java.util.*;
import java.util.stream.Collectors;

/**
 * StudentService类 - 学生服务业务逻辑
 */
public class StudentService {
    private DataStorage storage;
    
    /**
     * 构造函数
     * @param storage 数据存储对象
     */
    public StudentService(DataStorage storage) {
        this.storage = storage;
    }
    
    /**
     * 创建新学生
     * @param student 学生对象
     * @return 操作结果消息
     */
    public String createStudent(Student student) {
        if (student == null) {
            return "错误:学生对象不能为空";
        }
        
        // 验证学号唯一性
        if (getStudentById(student.getStudentId()) != null) {
            return "错误:学号已存在,请使用其他学号";
        }
        
        // 验证输入
        String validation = validateStudent(student);
        if (!validation.equals("验证通过")) {
            return validation;
        }
        
        List<Student> students = storage.getStudents();
        students.add(student);
        storage.setStudents(students);
        
        if (storage.saveStudents()) {
            return "成功:学生创建成功";
        } else {
            return "错误:保存学生数据失败";
        }
    }
    
    /**
     * 根据学号查询学生
     * @param studentId 学号
     * @return 学生对象,不存在则返回null
     */
    public Student getStudentById(String studentId) {
        if (studentId == null || studentId.trim().isEmpty()) {
            return null;
        }
        
        return storage.getStudents().stream()
            .filter(s -> s.getStudentId().equals(studentId))
            .findFirst()
            .orElse(null);
    }
    
    /**
     * 更新学生信息
     * @param student 学生对象
     * @return 操作结果消息
     */
    public String updateStudent(Student student) {
        if (student == null) {
            return "错误:学生对象不能为空";
        }
        
        List<Student> students = storage.getStudents();
        int index = -1;
        for (int i = 0; i < students.size(); i++) {
            if (students.get(i).getStudentId().equals(student.getStudentId())) {
                index = i;
                break;
            }
        }
        
        if (index == -1) {
            return "错误:学生不存在";
        }
        
        // 验证输入
        String validation = validateStudent(student);
        if (!validation.equals("验证通过")) {
            return validation;
        }
        
        students.set(index, student);
        storage.setStudents(students);
        
        if (storage.saveStudents()) {
            return "成功:学生信息更新成功";
        } else {
            return "错误:保存学生数据失败";
        }
    }
    
    /**
     * 删除学生
     * @param studentId 学号
     * @return 操作结果消息
     */
    public String deleteStudent(String studentId) {
        if (studentId == null || studentId.trim().isEmpty()) {
            return "错误:学号不能为空";
        }
        
        List<Student> students = storage.getStudents();
        Student toRemove = null;
        for (Student s : students) {
            if (s.getStudentId().equals(studentId)) {
                toRemove = s;
                break;
            }
        }
        
        if (toRemove == null) {
            return "错误:学生不存在";
        }
        
        students.remove(toRemove);
        storage.setStudents(students);
        
        // 同步清理课程中的选课记录
        List<Course> courses = storage.getCourses();
        boolean courseUpdated = false;
        for (Course course : courses) {
            if (course.isStudentEnrolled(studentId)) {
                course.dropStudent(studentId);
                courseUpdated = true;
            }
        }
        if (courseUpdated) {
            storage.setCourses(courses);
            storage.saveCourses();
        }
        
        if (storage.saveStudents()) {
            return "成功:学生删除成功";
        } else {
            return "错误:保存学生数据失败";
        }
    }
    
    /**
     * 搜索学生
     * @param major 专业(可为null)
     * @param grade 年级(0表示不限)
     * @param name 姓名关键字(可为null)
     * @return 符合条件的学生列表
     */
    public List<Student> searchStudents(String major, int grade, String name) {
        return storage.getStudents().stream()
            .filter(s -> major == null || s.getMajor().equals(major))
            .filter(s -> grade == 0 || s.getGrade() == grade)
            .filter(s -> name == null || s.getName().contains(name))
            .collect(Collectors.toList());
    }
    
    /**
     * 获取所有优秀学生(平均分≥85)
     * @return 优秀学生列表
     */
    public List<Student> getExcellentStudents() {
        return storage.getStudents().stream()
            .filter(Student::isExcellentStudent)
            .collect(Collectors.toList());
    }
    
    /**
     * 为学生添加课程成绩
     * @param studentId 学号
     * @param courseId 课程ID
     * @param score 成绩
     * @return 操作结果消息
     */
    public String addStudentScore(String studentId, String courseId, double score) {
        if (studentId == null || studentId.trim().isEmpty()) {
            return "错误:学号不能为空";
        }
        if (courseId == null || courseId.trim().isEmpty()) {
            return "错误:课程ID不能为空";
        }
        if (score < 0 || score > 100) {
            return "错误:成绩必须在0-100分之间";
        }
        
        Student student = getStudentById(studentId);
        if (student == null) {
            return "错误:学生不存在";
        }
        
        // 验证选课关系
        Course course = storage.getCourses().stream()
            .filter(c -> c.getCourseId().equals(courseId))
            .findFirst()
            .orElse(null);
        
        if (course == null) {
            return "错误:课程不存在";
        }
        
        if (!course.isStudentEnrolled(studentId)) {
            return "错误:学生未选该课程,请先选课";
        }
        
        student.addScore(courseId, score);
        return updateStudent(student);
    }
    
    /**
     * 获取学生平均分
     * @param studentId 学号
     * @return 平均分,学生不存在则返回-1
     */
    public double getStudentAverage(String studentId) {
        Student student = getStudentById(studentId);
        if (student == null) {
            return -1.0;
        }
        return student.getAverageScore();
    }
    
    /**
     * 获取所有学生
     * @return 学生列表
     */
    public List<Student> getAllStudents() {
        return storage.getStudents();
    }
    
    /**
     * 验证学生信息
     * @param student 学生对象
     * @return 验证结果消息
     */
    private String validateStudent(Student student) {
        // 验证学号
        if (student.getStudentId() == null || student.getStudentId().trim().isEmpty()) {
            return "错误:学号不能为空";
        }
        if (student.getStudentId().length() > 20) {
            return "错误:学号长度不能超过20字符";
        }
        if (!student.getStudentId().matches("[a-zA-Z0-9]+")) {
            return "错误:学号只能包含字母和数字";
        }
        
        // 验证姓名
        if (student.getName() == null || student.getName().trim().isEmpty()) {
            return "错误:姓名不能为空";
        }
        if (student.getName().length() < 2 || student.getName().length() > 50) {
            return "错误:姓名长度必须在2-50字符之间";
        }
        
        // 验证年龄
        if (student.getAge() < 15 || student.getAge() > 30) {
            return "错误:学生年龄必须在15-30岁之间";
        }
        
        // 验证邮箱
        if (student.getEmail() == null || !student.getEmail().matches("^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+$")) {
            return "错误:邮箱格式无效";
        }
        
        // 验证专业
        if (student.getMajor() == null || student.getMajor().trim().isEmpty()) {
            return "错误:专业名称不能为空";
        }
        if (student.getMajor().length() > 30) {
            return "错误:专业名称不能超过30字符";
        }
        
        // 验证年级
        if (student.getGrade() < 1 || student.getGrade() > 4) {
            return "错误:年级必须在1-4之间";
        }
        
        return "验证通过";
    }
    
    /**
     * 根据专业统计学生数量
     * @return 专业-学生数量映射
     */
    public Map<String, Integer> countStudentsByMajor() {
        Map<String, Integer> result = new HashMap<>();
        for (Student student : storage.getStudents()) {
            String major = student.getMajor();
            result.put(major, result.getOrDefault(major, 0) + 1);
        }
        return result;
    }
    
    /**
     * 根据年级统计学生数量
     * @return 年级-学生数量映射
     */
    public Map<Integer, Integer> countStudentsByGrade() {
        Map<Integer, Integer> result = new HashMap<>();
        for (Student student : storage.getStudents()) {
            int grade = student.getGrade();
            result.put(grade, result.getOrDefault(grade, 0) + 1);
        }
        return result;
    }
}
