// 始终生效
package com.teacher.dao.impl;

import com.teacher.dao.TeacherDao;
import com.teacher.entity.Teacher;
import java.util.ArrayList;
import java.util.List;

public class TeacherDaoImpl implements TeacherDao {
    private static List<Teacher> teachers = new ArrayList<>();
    private static Integer idCounter = 1;

    @Override
    public void add(Teacher teacher) {
        teacher.setId(idCounter++);
        teachers.add(teacher);
    }

    @Override
    public void delete(Integer id) {
        teachers.removeIf(t -> t.getId().equals(id));
    }

    @Override
    public void update(Teacher teacher) {
        for (int i = 0; i < teachers.size(); i++) {
            if (teachers.get(i).getId().equals(teacher.getId())) {
                teachers.set(i, teacher);
                return;
            }
        }
    }

    @Override
    public Teacher findById(Integer id) {
        return teachers.stream().filter(t -> t.getId().equals(id)).findFirst().orElse(null);
    }

    @Override
    public List<Teacher> findAll() {
        return new ArrayList<>(teachers);
    }
}
