// 始终生效
package com.teacher;

import com.teacher.controller.TeacherController;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        TeacherController controller = new TeacherController();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("\n========== 教师管理系统 ==========");
            System.out.println("1. 添加教师");
            System.out.println("2. 删除教师");
            System.out.println("3. 修改教师");
            System.out.println("4. 查询教师");
            System.out.println("5. 显示所有教师");
            System.out.println("0. 退出系统");
            System.out.print("请选择操作: ");

            String choice = scanner.nextLine();
            switch (choice) {
                case "1": controller.addTeacher(); break;
                case "2": controller.deleteTeacher(); break;
                case "3": controller.updateTeacher(); break;
                case "4": controller.findTeacher(); break;
                case "5": controller.listAllTeachers(); break;
                case "0":
                    System.out.println("感谢使用，再见！");
                    return;
                default:
                    System.out.println("无效选择，请重新输入！");
            }
        }
    }
}
