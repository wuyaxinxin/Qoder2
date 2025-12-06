// 始终生效
package com.teacher.service;

import com.teacher.entity.Teacher;
import java.util.List;

public interface TeacherService {
    void addTeacher(Teacher teacher);
    void deleteTeacher(Integer id);
    void updateTeacher(Teacher teacher);
    Teacher getTeacherById(Integer id);
    List<Teacher> getAllTeachers();
}
