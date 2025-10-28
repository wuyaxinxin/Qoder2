/*
 * 文件名: GradeService.java
 * 作者: 开发者
 * 创建日期: 2025-10-28
 * 版本: 1.0
 * 描述: 成绩服务类,提供成绩管理的业务逻辑
 * 功能:
 *   - 成绩的录入、修改、查询
 *   - 学生平均分计算
 *   - 课程通过率统计
 *   - 已通过/未通过课程查询
 * 依赖: Student.java, Course.java, DataStorage.java
 * 修改记录:
 *   2025-10-28 - 初始版本创建
 */

import java.util.*;
import java.util.stream.Collectors;

/**
 * GradeService类 - 成绩服务业务逻辑
 */
public class GradeService {
    private DataStorage storage;
    
    /**
     * 成绩记录内部类
     */
    public static class GradeRecord {
        private String studentId;
        private String studentName;
        private String courseId;
        private String courseName;
        private double score;
        
        public GradeRecord(String studentId, String studentName, 
                          String courseId, String courseName, double score) {
            this.studentId = studentId;
            this.studentName = studentName;
            this.courseId = courseId;
            this.courseName = courseName;
            this.score = score;
        }
        
        public String getStudentId() { return studentId; }
        public String getStudentName() { return studentName; }
        public String getCourseId() { return courseId; }
        public String getCourseName() { return courseName; }
        public double getScore() { return score; }
        
        @Override
        public String toString() {
            return String.format("学号:%s 姓名:%s 课程:%s(%s) 成绩:%.2f",
                studentId, studentName, courseName, courseId, score);
        }
    }
    
    /**
     * 构造函数
     * @param storage 数据存储对象
     */
    public GradeService(DataStorage storage) {
        this.storage = storage;
    }
    
    /**
     * 录入学生成绩
     * @param studentId 学号
     * @param courseId 课程ID
     * @param score 成绩
     * @return 操作结果消息
     */
    public String recordGrade(String studentId, String courseId, double score) {
        // 验证输入
        if (studentId == null || studentId.trim().isEmpty()) {
            return "错误:学号不能为空";
        }
        if (courseId == null || courseId.trim().isEmpty()) {
            return "错误:课程ID不能为空";
        }
        if (score < 0 || score > 100) {
            return "错误:成绩必须在0-100分之间";
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
        Course course = storage.getCourses().stream()
            .filter(c -> c.getCourseId().equals(courseId))
            .findFirst()
            .orElse(null);
        
        if (course == null) {
            return "错误:课程不存在";
        }
        
        // 验证选课关系
        if (!course.isStudentEnrolled(studentId)) {
            return "错误:学生未选该课程,请先选课";
        }
        
        // 录入成绩
        student.addScore(courseId, score);
        
        // 保存数据
        List<Student> students = storage.getStudents();
        for (int i = 0; i < students.size(); i++) {
            if (students.get(i).getStudentId().equals(studentId)) {
                students.set(i, student);
                break;
            }
        }
        storage.setStudents(students);
        
        if (storage.saveStudents()) {
            return String.format("成功:成绩录入成功 - %s %.2f分", 
                course.getCourseName(), score);
        } else {
            return "错误:保存成绩数据失败";
        }
    }
    
    /**
     * 更新已有成绩
     * @param studentId 学号
     * @param courseId 课程ID
     * @param score 新成绩
     * @return 操作结果消息
     */
    public String updateGrade(String studentId, String courseId, double score) {
        Student student = storage.getStudents().stream()
            .filter(s -> s.getStudentId().equals(studentId))
            .findFirst()
            .orElse(null);
        
        if (student == null) {
            return "错误:学生不存在";
        }
        
        if (student.getScore(courseId) == -1.0) {
            return "错误:该课程成绩不存在,请使用录入功能";
        }
        
        return recordGrade(studentId, courseId, score);
    }
    
    /**
     * 获取学生所有成绩
     * @param studentId 学号
     * @return 成绩记录列表
     */
    public List<GradeRecord> getStudentGrades(String studentId) {
        Student student = storage.getStudents().stream()
            .filter(s -> s.getStudentId().equals(studentId))
            .findFirst()
            .orElse(null);
        
        if (student == null) {
            return new ArrayList<>();
        }
        
        List<GradeRecord> records = new ArrayList<>();
        Map<String, Double> scores = student.getAllScores();
        
        for (Map.Entry<String, Double> entry : scores.entrySet()) {
            String courseId = entry.getKey();
            double score = entry.getValue();
            
            Course course = storage.getCourses().stream()
                .filter(c -> c.getCourseId().equals(courseId))
                .findFirst()
                .orElse(null);
            
            String courseName = (course != null) ? course.getCourseName() : "未知课程";
            records.add(new GradeRecord(studentId, student.getName(), 
                courseId, courseName, score));
        }
        
        return records;
    }
    
    /**
     * 获取课程所有学生成绩
     * @param courseId 课程ID
     * @return 成绩记录列表
     */
    public List<GradeRecord> getCourseGrades(String courseId) {
        Course course = storage.getCourses().stream()
            .filter(c -> c.getCourseId().equals(courseId))
            .findFirst()
            .orElse(null);
        
        if (course == null) {
            return new ArrayList<>();
        }
        
        List<GradeRecord> records = new ArrayList<>();
        List<String> enrolledStudents = course.getEnrolledStudents();
        
        for (String studentId : enrolledStudents) {
            Student student = storage.getStudents().stream()
                .filter(s -> s.getStudentId().equals(studentId))
                .findFirst()
                .orElse(null);
            
            if (student != null) {
                double score = student.getScore(courseId);
                if (score != -1.0) {
                    records.add(new GradeRecord(studentId, student.getName(),
                        courseId, course.getCourseName(), score));
                }
            }
        }
        
        return records;
    }
    
    /**
     * 计算学生平均分
     * @param studentId 学号
     * @return 平均分,-1表示学生不存在
     */
    public double calculateAverage(String studentId) {
        Student student = storage.getStudents().stream()
            .filter(s -> s.getStudentId().equals(studentId))
            .findFirst()
            .orElse(null);
        
        if (student == null) {
            return -1.0;
        }
        
        return student.getAverageScore();
    }
    
    /**
     * 获取学生已通过课程列表(成绩≥60)
     * @param studentId 学号
     * @return 课程列表
     */
    public List<Course> getPassedCourses(String studentId) {
        Student student = storage.getStudents().stream()
            .filter(s -> s.getStudentId().equals(studentId))
            .findFirst()
            .orElse(null);
        
        if (student == null) {
            return new ArrayList<>();
        }
        
        List<Course> passedCourses = new ArrayList<>();
        Map<String, Double> scores = student.getAllScores();
        
        for (Map.Entry<String, Double> entry : scores.entrySet()) {
            if (entry.getValue() >= 60.0) {
                String courseId = entry.getKey();
                Course course = storage.getCourses().stream()
                    .filter(c -> c.getCourseId().equals(courseId))
                    .findFirst()
                    .orElse(null);
                
                if (course != null) {
                    passedCourses.add(course);
                }
            }
        }
        
        return passedCourses;
    }
    
    /**
     * 获取学生未通过课程列表(成绩<60)
     * @param studentId 学号
     * @return 课程列表
     */
    public List<Course> getFailedCourses(String studentId) {
        Student student = storage.getStudents().stream()
            .filter(s -> s.getStudentId().equals(studentId))
            .findFirst()
            .orElse(null);
        
        if (student == null) {
            return new ArrayList<>();
        }
        
        List<Course> failedCourses = new ArrayList<>();
        Map<String, Double> scores = student.getAllScores();
        
        for (Map.Entry<String, Double> entry : scores.entrySet()) {
            if (entry.getValue() > 0 && entry.getValue() < 60.0) {
                String courseId = entry.getKey();
                Course course = storage.getCourses().stream()
                    .filter(c -> c.getCourseId().equals(courseId))
                    .findFirst()
                    .orElse(null);
                
                if (course != null) {
                    failedCourses.add(course);
                }
            }
        }
        
        return failedCourses;
    }
    
    /**
     * 计算课程通过率
     * @param courseId 课程ID
     * @return 通过率(0-100),课程不存在返回-1
     */
    public double getCoursePassRate(String courseId) {
        Course course = storage.getCourses().stream()
            .filter(c -> c.getCourseId().equals(courseId))
            .findFirst()
            .orElse(null);
        
        if (course == null) {
            return -1.0;
        }
        
        List<String> enrolledStudents = course.getEnrolledStudents();
        if (enrolledStudents.isEmpty()) {
            return 0.0;
        }
        
        int passedCount = 0;
        int totalCount = 0;
        
        for (String studentId : enrolledStudents) {
            Student student = storage.getStudents().stream()
                .filter(s -> s.getStudentId().equals(studentId))
                .findFirst()
                .orElse(null);
            
            if (student != null) {
                double score = student.getScore(courseId);
                if (score > 0) {  // 已录入成绩
                    totalCount++;
                    if (score >= 60.0) {
                        passedCount++;
                    }
                }
            }
        }
        
        if (totalCount == 0) {
            return 0.0;
        }
        
        return (passedCount * 100.0) / totalCount;
    }
    
    /**
     * 获取成绩分布统计
     * @param courseId 课程ID
     * @return 分数段-人数映射
     */
    public Map<String, Integer> getGradeDistribution(String courseId) {
        Map<String, Integer> distribution = new LinkedHashMap<>();
        distribution.put("优秀(90-100)", 0);
        distribution.put("良好(80-89)", 0);
        distribution.put("中等(70-79)", 0);
        distribution.put("及格(60-69)", 0);
        distribution.put("不及格(0-59)", 0);
        
        List<GradeRecord> grades = getCourseGrades(courseId);
        
        for (GradeRecord record : grades) {
            double score = record.getScore();
            if (score >= 90) {
                distribution.put("优秀(90-100)", distribution.get("优秀(90-100)") + 1);
            } else if (score >= 80) {
                distribution.put("良好(80-89)", distribution.get("良好(80-89)") + 1);
            } else if (score >= 70) {
                distribution.put("中等(70-79)", distribution.get("中等(70-79)") + 1);
            } else if (score >= 60) {
                distribution.put("及格(60-69)", distribution.get("及格(60-69)") + 1);
            } else {
                distribution.put("不及格(0-59)", distribution.get("不及格(0-59)") + 1);
            }
        }
        
        return distribution;
    }
}
