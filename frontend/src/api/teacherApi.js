import axios from 'axios';

const API_BASE_URL = '/api/teachers';

/**
 * 获取所有教师
 */
export const getAllTeachers = async () => {
  const response = await axios.get(API_BASE_URL);
  return response.data;
};

/**
 * 根据ID获取教师
 */
export const getTeacherById = async (id) => {
  const response = await axios.get(`${API_BASE_URL}/${id}`);
  return response.data;
};

/**
 * 创建教师
 */
export const createTeacher = async (teacher) => {
  const response = await axios.post(API_BASE_URL, teacher);
  return response.data;
};

/**
 * 更新教师
 */
export const updateTeacher = async (id, teacher) => {
  const response = await axios.put(`${API_BASE_URL}/${id}`, teacher);
  return response.data;
};

/**
 * 删除教师
 */
export const deleteTeacher = async (id) => {
  const response = await axios.delete(`${API_BASE_URL}/${id}`);
  return response.data;
};

/**
 * 搜索教师
 */
export const searchTeachers = async (name) => {
  const response = await axios.get(`${API_BASE_URL}/search`, {
    params: { name }
  });
  return response.data;
};
