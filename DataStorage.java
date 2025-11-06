/*
 * 文件名: DataStorage.java
 * 作者: 开发者
 * 创建日期: 2025-10-28
 * 版本: 1.0
 * 描述: 数据持久化存储类,负责JSON文件的读写、备份和恢复
 * 功能:
 *   - 加载和保存学生、课程、教师数据
 *   - 支持数据备份和恢复
 *   - 提供事务性写入保障
 *   - 数据完整性校验
 * 依赖: Student.java, Teacher.java, Course.java
 * 修改记录:
 *   2025-10-28 - 初始版本创建
 */

import java.io.*;
import java.nio.file.*;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.*;
import org.json.*;

/**
 * DataStorage类 - 数据持久化存储管理
 * 提供JSON文件的读写、备份和恢复功能
 */
public class DataStorage {
    private static final String DATA_DIR = "data/";
    private static final String BACKUP_DIR = "data/backups/";
    private static final String STUDENTS_FILE = DATA_DIR + "students.json";
    private static final String COURSES_FILE = DATA_DIR + "courses.json";
    private static final String TEACHERS_FILE = DATA_DIR + "teachers.json";
    private static final int MAX_BACKUPS = 3;
    
    private List<Student> students;
    private List<Course> courses;
    private List<Teacher> teachers;
    
    /**
     * 构造函数,初始化数据目录
     */
    public DataStorage() {
        this.students = new ArrayList<>();
        this.courses = new ArrayList<>();
        this.teachers = new ArrayList<>();
        initializeDirectories();
    }
    
    /**
     * 初始化数据目录结构
     */
    private void initializeDirectories() {
        try {
            Files.createDirectories(Paths.get(DATA_DIR));
            Files.createDirectories(Paths.get(BACKUP_DIR));
        } catch (IOException e) {
            System.err.println("创建目录失败: " + e.getMessage());
        }
    }
    
    /**
     * 加载所有学生数据
     * @return 操作是否成功
     */
    public boolean loadStudents() {
        try {
            File file = new File(STUDENTS_FILE);
            if (!file.exists()) {
                // 创建空数据文件
                saveStudents();
                return true;
            }
            
            String content = new String(Files.readAllBytes(Paths.get(STUDENTS_FILE)));
            JSONObject root = new JSONObject(content);
            JSONArray studentsArray = root.getJSONArray("students");
            
            students.clear();
            for (int i = 0; i < studentsArray.length(); i++) {
                JSONObject obj = studentsArray.getJSONObject(i);
                Student student = new Student(
                    obj.getString("name"),
                    obj.getInt("age"),
                    obj.getString("email"),
                    obj.getString("studentId"),
                    obj.getString("major"),
                    obj.getInt("grade")
                );
                
                // 加载成绩
                if (obj.has("scores")) {
                    JSONObject scores = obj.getJSONObject("scores");
                    for (String courseId : scores.keySet()) {
                        student.addScore(courseId, scores.getDouble(courseId));
                    }
                }
                
                students.add(student);
            }
            return true;
        } catch (Exception e) {
            System.err.println("加载学生数据失败: " + e.getMessage());
            return false;
        }
    }
    
    /**
     * 保存所有学生数据
     * @return 操作是否成功
     */
    public boolean saveStudents() {
        try {
            // 先备份旧数据
            backupFile(STUDENTS_FILE);
            
            JSONObject root = new JSONObject();
            JSONArray studentsArray = new JSONArray();
            
            for (Student student : students) {
                JSONObject obj = new JSONObject();
                obj.put("studentId", student.getStudentId());
                obj.put("name", student.getName());
                obj.put("age", student.getAge());
                obj.put("email", student.getEmail());
                obj.put("major", student.getMajor());
                obj.put("grade", student.getGrade());
                
                // 保存成绩
                JSONObject scores = new JSONObject();
                Map<String, Double> studentScores = student.getAllScores();
                for (Map.Entry<String, Double> entry : studentScores.entrySet()) {
                    scores.put(entry.getKey(), entry.getValue());
                }
                obj.put("scores", scores);
                
                studentsArray.put(obj);
            }
            
            root.put("students", studentsArray);
            
            // 事务性写入
            return writeJsonFile(STUDENTS_FILE, root.toString(2));
        } catch (Exception e) {
            System.err.println("保存学生数据失败: " + e.getMessage());
            return false;
        }
    }
    
    /**
     * 加载所有课程数据
     * @return 操作是否成功
     */
    public boolean loadCourses() {
        try {
            File file = new File(COURSES_FILE);
            if (!file.exists()) {
                saveCourses();
                return true;
            }
            
            String content = new String(Files.readAllBytes(Paths.get(COURSES_FILE)));
            JSONObject root = new JSONObject(content);
            JSONArray coursesArray = root.getJSONArray("courses");
            
            courses.clear();
            for (int i = 0; i < coursesArray.length(); i++) {
                JSONObject obj = coursesArray.getJSONObject(i);
                Course course = new Course(
                    obj.getString("courseId"),
                    obj.getString("courseName"),
                    obj.getString("instructor"),
                    obj.getInt("creditHours"),
                    obj.getString("description"),
                    LocalDate.parse(obj.getString("startDate")),
                    LocalDate.parse(obj.getString("endDate"))
                );
                
                // 加载已选学生
                if (obj.has("enrolledStudents")) {
                    JSONArray students = obj.getJSONArray("enrolledStudents");
                    for (int j = 0; j < students.length(); j++) {
                        course.enrollStudent(students.getString(j));
                    }
                }
                
                courses.add(course);
            }
            return true;
        } catch (Exception e) {
            System.err.println("加载课程数据失败: " + e.getMessage());
            return false;
        }
    }
    
    /**
     * 保存所有课程数据
     * @return 操作是否成功
     */
    public boolean saveCourses() {
        try {
            backupFile(COURSES_FILE);
            
            JSONObject root = new JSONObject();
            JSONArray coursesArray = new JSONArray();
            
            for (Course course : courses) {
                JSONObject obj = new JSONObject();
                obj.put("courseId", course.getCourseId());
                obj.put("courseName", course.getCourseName());
                obj.put("instructor", course.getInstructor());
                obj.put("creditHours", course.getCreditHours());
                obj.put("description", course.getDescription());
                obj.put("startDate", course.getStartDate().toString());
                obj.put("endDate", course.getEndDate().toString());
                
                // 保存已选学生
                JSONArray enrolledStudents = new JSONArray();
                for (String studentId : course.getEnrolledStudents()) {
                    enrolledStudents.put(studentId);
                }
                obj.put("enrolledStudents", enrolledStudents);
                
                coursesArray.put(obj);
            }
            
            root.put("courses", coursesArray);
            
            return writeJsonFile(COURSES_FILE, root.toString(2));
        } catch (Exception e) {
            System.err.println("保存课程数据失败: " + e.getMessage());
            return false;
        }
    }
    
    /**
     * 加载所有教师数据
     * @return 操作是否成功
     */
    public boolean loadTeachers() {
        try {
            File file = new File(TEACHERS_FILE);
            if (!file.exists()) {
                saveTeachers();
                return true;
            }
            
            String content = new String(Files.readAllBytes(Paths.get(TEACHERS_FILE)));
            JSONObject root = new JSONObject(content);
            JSONArray teachersArray = root.getJSONArray("teachers");
            
            teachers.clear();
            for (int i = 0; i < teachersArray.length(); i++) {
                JSONObject obj = teachersArray.getJSONObject(i);
                Teacher teacher = new Teacher(
                    obj.getString("name"),
                    obj.getInt("age"),
                    obj.getString("email"),
                    obj.getString("teacherId"),
                    obj.getString("subject"),
                    obj.getString("title"),
                    obj.getInt("yearsOfExperience")
                );
                
                // 加载授课班级
                if (obj.has("classes")) {
                    JSONArray classes = obj.getJSONArray("classes");
                    for (int j = 0; j < classes.length(); j++) {
                        teacher.addClass(classes.getString(j));
                    }
                }
                
                teachers.add(teacher);
            }
            return true;
        } catch (Exception e) {
            System.err.println("加载教师数据失败: " + e.getMessage());
            return false;
        }
    }
    
    /**
     * 保存所有教师数据
     * @return 操作是否成功
     */
    public boolean saveTeachers() {
        try {
            backupFile(TEACHERS_FILE);
            
            JSONObject root = new JSONObject();
            JSONArray teachersArray = new JSONArray();
            
            for (Teacher teacher : teachers) {
                JSONObject obj = new JSONObject();
                obj.put("teacherId", teacher.getTeacherId());
                obj.put("name", teacher.getName());
                obj.put("age", teacher.getAge());
                obj.put("email", teacher.getEmail());
                obj.put("subject", teacher.getSubject());
                obj.put("title", teacher.getTitle());
                obj.put("yearsOfExperience", teacher.getYearsOfExperience());
                
                // 保存授课班级
                JSONArray classes = new JSONArray();
                for (String className : teacher.getAllClasses()) {
                    classes.put(className);
                }
                obj.put("classes", classes);
                
                teachersArray.put(obj);
            }
            
            root.put("teachers", teachersArray);
            
            return writeJsonFile(TEACHERS_FILE, root.toString(2));
        } catch (Exception e) {
            System.err.println("保存教师数据失败: " + e.getMessage());
            return false;
        }
    }
    
    /**
     * 事务性写入JSON文件
     * @param filePath 目标文件路径
     * @param content 文件内容
     * @return 操作是否成功
     */
    private boolean writeJsonFile(String filePath, String content) {
        String tempFile = filePath + ".tmp";
        try {
            // 写入临时文件
            Files.write(Paths.get(tempFile), content.getBytes());
            
            // 验证临时文件
            new JSONObject(content); // 验证JSON格式
            
            // 替换原文件
            Files.move(Paths.get(tempFile), Paths.get(filePath), 
                      StandardCopyOption.REPLACE_EXISTING);
            return true;
        } catch (Exception e) {
            // 删除临时文件
            try {
                Files.deleteIfExists(Paths.get(tempFile));
            } catch (IOException ex) {
                // 忽略删除失败
            }
            System.err.println("写入文件失败: " + e.getMessage());
            return false;
        }
    }
    
    /**
     * 备份指定文件
     * @param filePath 文件路径
     */
    private void backupFile(String filePath) {
        try {
            File file = new File(filePath);
            if (!file.exists()) {
                return;
            }
            
            String timestamp = LocalDateTime.now()
                .format(DateTimeFormatter.ofPattern("yyyyMMdd_HHmmss"));
            String fileName = file.getName();
            String backupPath = BACKUP_DIR + fileName + "." + timestamp;
            
            Files.copy(Paths.get(filePath), Paths.get(backupPath), 
                      StandardCopyOption.REPLACE_EXISTING);
            
            // 清理旧备份
            cleanOldBackups(fileName);
        } catch (IOException e) {
            System.err.println("备份文件失败: " + e.getMessage());
        }
    }
    
    /**
     * 清理旧备份文件,保留最近的N个版本
     * @param fileName 原文件名
     */
    private void cleanOldBackups(String fileName) {
        try {
            File backupDir = new File(BACKUP_DIR);
            File[] backups = backupDir.listFiles((dir, name) -> 
                name.startsWith(fileName + "."));
            
            if (backups == null || backups.length <= MAX_BACKUPS) {
                return;
            }
            
            // 按修改时间排序
            Arrays.sort(backups, Comparator.comparingLong(File::lastModified));
            
            // 删除最旧的备份
            for (int i = 0; i < backups.length - MAX_BACKUPS; i++) {
                backups[i].delete();
            }
        } catch (Exception e) {
            System.err.println("清理备份失败: " + e.getMessage());
        }
    }
    
    /**
     * 从备份恢复数据
     * @param fileName 文件名
     * @param timestamp 备份时间戳
     * @return 操作是否成功
     */
    public boolean restoreFromBackup(String fileName, String timestamp) {
        try {
            String backupPath = BACKUP_DIR + fileName + "." + timestamp;
            String targetPath = DATA_DIR + fileName;
            
            if (!new File(backupPath).exists()) {
                System.err.println("备份文件不存在: " + backupPath);
                return false;
            }
            
            Files.copy(Paths.get(backupPath), Paths.get(targetPath), 
                      StandardCopyOption.REPLACE_EXISTING);
            return true;
        } catch (IOException e) {
            System.err.println("恢复备份失败: " + e.getMessage());
            return false;
        }
    }
    
    /**
     * 获取所有学生
     * @return 学生列表
     */
    public List<Student> getStudents() {
        return new ArrayList<>(students);
    }
    
    /**
     * 设置学生列表
     * @param students 学生列表
     */
    public void setStudents(List<Student> students) {
        this.students = new ArrayList<>(students);
    }
    
    /**
     * 获取所有课程
     * @return 课程列表
     */
    public List<Course> getCourses() {
        return new ArrayList<>(courses);
    }
    
    /**
     * 设置课程列表
     * @param courses 课程列表
     */
    public void setCourses(List<Course> courses) {
        this.courses = new ArrayList<>(courses);
    }
    
    /**
     * 获取所有教师
     * @return 教师列表
     */
    public List<Teacher> getTeachers() {
        return new ArrayList<>(teachers);
    }
    
    /**
     * 设置教师列表
     * @param teachers 教师列表
     */
    public void setTeachers(List<Teacher> teachers) {
        this.teachers = new ArrayList<>(teachers);
    }
    
    /**
     * 加载所有数据
     * @return 操作是否成功
     */
    public boolean loadAll() {
        return loadStudents() && loadCourses() && loadTeachers();
    }
    
    /**
     * 保存所有数据
     * @return 操作是否成功
     */
    public boolean saveAll() {
        return saveStudents() && saveCourses() && saveTeachers();
    }
}
