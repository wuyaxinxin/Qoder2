// 始终生效
package com.teacher.controller;

import com.teacher.entity.Teacher;
import com.teacher.service.TeacherService;
import com.teacher.service.impl.TeacherServiceImpl;
import java.util.List;
import java.util.Scanner;

public class TeacherController {
    private TeacherService teacherService = new TeacherServiceImpl();
    private Scanner scanner = new Scanner(System.in);

    public void addTeacher() {
        System.out.println("===== 添加教师 =====");
        Teacher teacher = new Teacher();
        System.out.print("请输入姓名: ");
        teacher.setName(scanner.nextLine());
        System.out.print("请输入年龄: ");
        teacher.setAge(Integer.parseInt(scanner.nextLine()));
        System.out.print("请输入学科: ");
        teacher.setSubject(scanner.nextLine());
        System.out.print("请输入电话: ");
        teacher.setPhone(scanner.nextLine());
        System.out.print("请输入邮箱: ");
        teacher.setEmail(scanner.nextLine());
        teacherService.addTeacher(teacher);
        System.out.println("添加成功！");
    }

    public void deleteTeacher() {
        System.out.println("===== 删除教师 =====");
        System.out.print("请输入要删除的教师ID: ");
        Integer id = Integer.parseInt(scanner.nextLine());
        teacherService.deleteTeacher(id);
        System.out.println("删除成功！");
    }

    public void updateTeacher() {
        System.out.println("===== 修改教师 =====");
        System.out.print("请输入要修改的教师ID: ");
        Integer id = Integer.parseInt(scanner.nextLine());
        Teacher teacher = teacherService.getTeacherById(id);
        if (teacher == null) {
            System.out.println("未找到该教师！");
            return;
        }
        System.out.print("请输入新姓名(直接回车保持不变): ");
        String name = scanner.nextLine();
        if (!name.isEmpty()) teacher.setName(name);
        System.out.print("请输入新年龄(直接回车保持不变): ");
        String age = scanner.nextLine();
        if (!age.isEmpty()) teacher.setAge(Integer.parseInt(age));
        System.out.print("请输入新学科(直接回车保持不变): ");
        String subject = scanner.nextLine();
        if (!subject.isEmpty()) teacher.setSubject(subject);
        System.out.print("请输入新电话(直接回车保持不变): ");
        String phone = scanner.nextLine();
        if (!phone.isEmpty()) teacher.setPhone(phone);
        System.out.print("请输入新邮箱(直接回车保持不变): ");
        String email = scanner.nextLine();
        if (!email.isEmpty()) teacher.setEmail(email);
        teacherService.updateTeacher(teacher);
        System.out.println("修改成功！");
    }

    public void findTeacher() {
        System.out.println("===== 查询教师 =====");
        System.out.print("请输入教师ID: ");
        Integer id = Integer.parseInt(scanner.nextLine());
        Teacher teacher = teacherService.getTeacherById(id);
        if (teacher == null) {
            System.out.println("未找到该教师！");
        } else {
            System.out.println(teacher);
        }
    }

    public void listAllTeachers() {
        System.out.println("===== 所有教师 =====");
        List<Teacher> teachers = teacherService.getAllTeachers();
        if (teachers.isEmpty()) {
            System.out.println("暂无教师信息！");
        } else {
            teachers.forEach(System.out::println);
        }
    }
}
