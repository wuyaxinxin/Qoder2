import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './styles/App.css';

const API_URL = '/api/teachers';

function App() {
  const [teachers, setTeachers] = useState([]);
  const [form, setForm] = useState({ name: '', title: '', age: '', salary: '', gender: '', subject: '' });
  const [editId, setEditId] = useState(null);

  useEffect(() => {
    loadTeachers();
  }, []);

  const loadTeachers = async () => {
    const res = await axios.get(API_URL);
    setTeachers(res.data);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (editId) {
      await axios.put(`${API_URL}/${editId}`, form);
    } else {
      await axios.post(API_URL, form);
    }
    setForm({ name: '', title: '', age: '', salary: '', gender: '', subject: '' });
    setEditId(null);
    loadTeachers();
  };

  const handleEdit = (t) => {
    setForm({
      name: t.name,
      title: t.title || '',
      age: t.age || '',
      salary: t.salary || '',
      gender: t.gender || '',
      subject: t.subject || ''
    });
    setEditId(t.id);
  };

  const handleDelete = async (id) => {
    if (window.confirm('确定删除？')) {
      await axios.delete(`${API_URL}/${id}`);
      loadTeachers();
    }
  };

  const handleCancel = () => {
    setEditId(null);
    setForm({ name: '', title: '', age: '', salary: '', gender: '', subject: '' });
  };

  return (
    <div className="container">
      <h1>教师管理系统</h1>
      
      <form onSubmit={handleSubmit} className="form-container">
        <input placeholder="姓名" value={form.name} onChange={(e) => setForm({...form, name: e.target.value})} required />
        <input placeholder="职称" value={form.title} onChange={(e) => setForm({...form, title: e.target.value})} />
        <input type="number" placeholder="年龄" value={form.age} onChange={(e) => setForm({...form, age: e.target.value})} />
        <input type="number" placeholder="工资" value={form.salary} onChange={(e) => setForm({...form, salary: e.target.value})} />
        <select value={form.gender} onChange={(e) => setForm({...form, gender: e.target.value})}>
          <option value="">选择性别</option>
          <option value="男">男</option>
          <option value="女">女</option>
        </select>
        <input placeholder="科目" value={form.subject} onChange={(e) => setForm({...form, subject: e.target.value})} />
        <button type="submit">{editId ? '更新' : '添加'}</button>
        {editId && <button type="button" onClick={handleCancel}>取消</button>}
      </form>

      <table className="table">
        <thead>
          <tr><th>ID</th><th>姓名</th><th>职称</th><th>年龄</th><th>工资</th><th>性别</th><th>科目</th><th>操作</th></tr>
        </thead>
        <tbody>
          {teachers.map(t => (
            <tr key={t.id}>
              <td>{t.id}</td>
              <td>{t.name}</td>
              <td>{t.title || '-'}</td>
              <td>{t.age || '-'}</td>
              <td>{t.salary || '-'}</td>
              <td>{t.gender || '-'}</td>
              <td>{t.subject || '-'}</td>
              <td>
                <button onClick={() => handleEdit(t)}>编辑</button>
                <button onClick={() => handleDelete(t.id)}>删除</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
