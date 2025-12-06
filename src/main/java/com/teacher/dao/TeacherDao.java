// 始终生效
package com.teacher.dao;

import com.teacher.entity.Teacher;
import java.util.List;

public interface TeacherDao {
    void add(Teacher teacher);
    void delete(Integer id);
    void update(Teacher teacher);
    Teacher findById(Integer id);
    List<Teacher> findAll();
}
