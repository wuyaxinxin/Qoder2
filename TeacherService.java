/*
 * 文件名: TeacherService.java
 * 作者: 开发者
 * 创建日期: 2025-10-28
 * 版本: 1.0
 * 描述: 教师服务类,提供教师信息管理的业务逻辑
 * 功能:
 *   - 教师的创建、查询、修改、删除
 *   - 教师授课班级管理
 *   - 资深教师查询
 *   - 教师工作量统计
 * 依赖: Teacher.java, DataStorage.java
 * 修改记录:
 *   2025-10-28 - 初始版本创建
 */

import java.util.*;
import java.util.stream.Collectors;

/**
 * TeacherService类 - 教师服务业务逻辑
 */
public class TeacherService {
    private DataStorage storage;
    
    /**
     * 构造函数
     * @param storage 数据存储对象
     */
    public TeacherService(DataStorage storage) {
        this.storage = storage;
    }
    
    /**
     * 创建新教师
     * @param teacher 教师对象
     * @return 操作结果消息
     */
    public String createTeacher(Teacher teacher) {
        if (teacher == null) {
            return "错误:教师对象不能为空";
        }
        
        // 验证教师ID唯一性
        if (getTeacherById(teacher.getTeacherId()) != null) {
            return "错误:教师ID已存在,请使用其他ID";
        }
        
        // 验证输入
        String validation = validateTeacher(teacher);
        if (!validation.equals("验证通过")) {
            return validation;
        }
        
        List<Teacher> teachers = storage.getTeachers();
        teachers.add(teacher);
        storage.setTeachers(teachers);
        
        if (storage.saveTeachers()) {
            return "成功:教师创建成功";
        } else {
            return "错误:保存教师数据失败";
        }
    }
    
    /**
     * 根据教师ID查询教师
     * @param teacherId 教师ID
     * @return 教师对象,不存在则返回null
     */
    public Teacher getTeacherById(String teacherId) {
        if (teacherId == null || teacherId.trim().isEmpty()) {
            return null;
        }
        
        return storage.getTeachers().stream()
            .filter(t -> t.getTeacherId().equals(teacherId))
            .findFirst()
            .orElse(null);
    }
    
    /**
     * 更新教师信息
     * @param teacher 教师对象
     * @return 操作结果消息
     */
    public String updateTeacher(Teacher teacher) {
        if (teacher == null) {
            return "错误:教师对象不能为空";
        }
        
        List<Teacher> teachers = storage.getTeachers();
        int index = -1;
        for (int i = 0; i < teachers.size(); i++) {
            if (teachers.get(i).getTeacherId().equals(teacher.getTeacherId())) {
                index = i;
                break;
            }
        }
        
        if (index == -1) {
            return "错误:教师不存在";
        }
        
        // 验证输入
        String validation = validateTeacher(teacher);
        if (!validation.equals("验证通过")) {
            return validation;
        }
        
        teachers.set(index, teacher);
        storage.setTeachers(teachers);
        
        if (storage.saveTeachers()) {
            return "成功:教师信息更新成功";
        } else {
            return "错误:保存教师数据失败";
        }
    }
    
    /**
     * 删除教师
     * @param teacherId 教师ID
     * @return 操作结果消息
     */
    public String deleteTeacher(String teacherId) {
        if (teacherId == null || teacherId.trim().isEmpty()) {
            return "错误:教师ID不能为空";
        }
        
        Teacher teacher = getTeacherById(teacherId);
        if (teacher == null) {
            return "错误:教师不存在";
        }
        
        // 检查是否有授课班级
        if (teacher.getClassCount() > 0) {
            return "错误:请先移除教师的授课班级";
        }
        
        List<Teacher> teachers = storage.getTeachers();
        teachers.remove(teacher);
        storage.setTeachers(teachers);
        
        if (storage.saveTeachers()) {
            return "成功:教师删除成功";
        } else {
            return "错误:保存教师数据失败";
        }
    }
    
    /**
     * 为教师分配授课班级
     * @param teacherId 教师ID
     * @param className 班级名称
     * @return 操作结果消息
     */
    public String assignClass(String teacherId, String className) {
        if (teacherId == null || teacherId.trim().isEmpty()) {
            return "错误:教师ID不能为空";
        }
        if (className == null || className.trim().isEmpty()) {
            return "错误:班级名称不能为空";
        }
        
        Teacher teacher = getTeacherById(teacherId);
        if (teacher == null) {
            return "错误:教师不存在";
        }
        
        if (teacher.teachesClass(className)) {
            return "错误:教师已授课该班级";
        }
        
        teacher.addClass(className);
        return updateTeacher(teacher);
    }
    
    /**
     * 移除教师授课班级
     * @param teacherId 教师ID
     * @param className 班级名称
     * @return 操作结果消息
     */
    public String removeClass(String teacherId, String className) {
        if (teacherId == null || teacherId.trim().isEmpty()) {
            return "错误:教师ID不能为空";
        }
        if (className == null || className.trim().isEmpty()) {
            return "错误:班级名称不能为空";
        }
        
        Teacher teacher = getTeacherById(teacherId);
        if (teacher == null) {
            return "错误:教师不存在";
        }
        
        if (!teacher.teachesClass(className)) {
            return "错误:教师未授课该班级";
        }
        
        teacher.removeClass(className);
        return updateTeacher(teacher);
    }
    
    /**
     * 获取资深教师列表(教龄≥10年)
     * @return 资深教师列表
     */
    public List<Teacher> getSeniorTeachers() {
        return storage.getTeachers().stream()
            .filter(Teacher::isSeniorTeacher)
            .collect(Collectors.toList());
    }
    
    /**
     * 获取教师授课班级数量
     * @param teacherId 教师ID
     * @return 班级数量,-1表示教师不存在
     */
    public int getTeacherWorkload(String teacherId) {
        Teacher teacher = getTeacherById(teacherId);
        if (teacher == null) {
            return -1;
        }
        return teacher.getClassCount();
    }
    
    /**
     * 获取所有教师
     * @return 教师列表
     */
    public List<Teacher> getAllTeachers() {
        return storage.getTeachers();
    }
    
    /**
     * 根据科目查询教师
     * @param subject 科目名称
     * @return 教师列表
     */
    public List<Teacher> getTeachersBySubject(String subject) {
        if (subject == null || subject.trim().isEmpty()) {
            return new ArrayList<>();
        }
        
        return storage.getTeachers().stream()
            .filter(t -> t.getSubject().equals(subject))
            .collect(Collectors.toList());
    }
    
    /**
     * 根据职称查询教师
     * @param title 职称
     * @return 教师列表
     */
    public List<Teacher> getTeachersByTitle(String title) {
        if (title == null || title.trim().isEmpty()) {
            return new ArrayList<>();
        }
        
        return storage.getTeachers().stream()
            .filter(t -> t.getTitle().equals(title))
            .collect(Collectors.toList());
    }
    
    /**
     * 验证教师信息
     * @param teacher 教师对象
     * @return 验证结果消息
     */
    private String validateTeacher(Teacher teacher) {
        // 验证教师ID
        if (teacher.getTeacherId() == null || teacher.getTeacherId().trim().isEmpty()) {
            return "错误:教师ID不能为空";
        }
        if (teacher.getTeacherId().length() > 20) {
            return "错误:教师ID长度不能超过20字符";
        }
        if (!teacher.getTeacherId().matches("[a-zA-Z0-9]+")) {
            return "错误:教师ID只能包含字母和数字";
        }
        
        // 验证姓名
        if (teacher.getName() == null || teacher.getName().trim().isEmpty()) {
            return "错误:姓名不能为空";
        }
        if (teacher.getName().length() < 2 || teacher.getName().length() > 50) {
            return "错误:姓名长度必须在2-50字符之间";
        }
        
        // 验证年龄
        if (teacher.getAge() < 25 || teacher.getAge() > 70) {
            return "错误:教师年龄必须在25-70岁之间";
        }
        
        // 验证邮箱
        if (teacher.getEmail() == null || !teacher.getEmail().matches("^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+$")) {
            return "错误:邮箱格式无效";
        }
        
        // 验证科目
        if (teacher.getSubject() == null || teacher.getSubject().trim().isEmpty()) {
            return "错误:所教科目不能为空";
        }
        
        // 验证职称
        String title = teacher.getTitle();
        if (title == null || (!title.equals("助教") && !title.equals("讲师") && 
            !title.equals("副教授") && !title.equals("教授"))) {
            return "错误:职称必须为助教、讲师、副教授或教授之一";
        }
        
        // 验证教龄
        if (teacher.getYearsOfExperience() < 0 || teacher.getYearsOfExperience() > 50) {
            return "错误:教龄必须在0-50年之间";
        }
        
        return "验证通过";
    }
    
    /**
     * 按工作量排序教师
     * @return 排序后的教师列表
     */
    public List<Teacher> getTeachersByWorkload() {
        List<Teacher> teachers = new ArrayList<>(storage.getTeachers());
        teachers.sort((t1, t2) -> 
            Integer.compare(t2.getClassCount(), t1.getClassCount()));
        return teachers;
    }
}
