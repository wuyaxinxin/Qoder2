// 始终生效
package com.teacher.service.impl;

import com.teacher.dao.TeacherDao;
import com.teacher.dao.impl.TeacherDaoImpl;
import com.teacher.entity.Teacher;
import com.teacher.service.TeacherService;
import java.util.List;

public class TeacherServiceImpl implements TeacherService {
    private TeacherDao teacherDao = new TeacherDaoImpl();

    @Override
    public void addTeacher(Teacher teacher) {
        teacherDao.add(teacher);
    }

    @Override
    public void deleteTeacher(Integer id) {
        teacherDao.delete(id);
    }

    @Override
    public void updateTeacher(Teacher teacher) {
        teacherDao.update(teacher);
    }

    @Override
    public Teacher getTeacherById(Integer id) {
        return teacherDao.findById(id);
    }

    @Override
    public List<Teacher> getAllTeachers() {
        return teacherDao.findAll();
    }
}
