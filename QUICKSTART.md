# 学生管理系统 - 快速入门指南

## 🚀 快速开始

### 1. 运行演示程序

```bash
python demo.py
```

这将运行一个完整的演示,展示系统的所有主要功能。

### 2. 运行交互式系统

```bash
python main.py
```

进入交互式命令行界面,可以进行完整的学生管理操作。

### 3. 运行测试

```bash
python test_student_system.py
```

执行所有单元测试,验证系统功能正常。

## 📚 常用操作示例

### 示例 1: 基本使用

```python
from student import Student
from student_manager import StudentManager

# 创建管理器
manager = StudentManager()

# 添加学生
manager.add_student("张三", 20, "2021001", "计算机科学")

# 获取学生并添加成绩
student = manager.get_student("2021001")
student.add_score("数学", 95)
student.add_score("英语", 88)

# 查看信息
print(student.get_student_info())

# 保存数据
manager.save_data()
```

### 示例 2: 成绩统计

```python
# 获取平均分
avg = student.get_average_score()
print(f"平均分: {avg:.2f}")

# 获取最高分和最低分
highest = student.get_highest_score()
lowest = student.get_lowest_score()

print(f"最高分: {highest[0]} - {highest[1]}")
print(f"最低分: {lowest[0]} - {lowest[1]}")

# 检查是否优秀学生
if student.is_excellent_student():
    print("这是一位优秀学生!")
```

### 示例 3: 批量管理

```python
# 添加多个学生
students_info = [
    ("张三", 20, "2021001", "计算机"),
    ("李四", 19, "2021002", "数学"),
    ("王五", 21, "2021003", "物理")
]

for name, age, sid, major in students_info:
    manager.add_student(name, age, sid, major)

# 搜索学生
results = manager.search_students("计算机")
print(f"找到 {len(results)} 名计算机专业的学生")

# 获取排名
top_students = manager.get_top_students(10)
for rank, (student, avg_score) in enumerate(top_students, 1):
    print(f"{rank}. {student.name}: {avg_score:.2f}")
```

### 示例 4: 数据导出

```python
# 导出为CSV
manager.export_to_csv("students.csv")

# 查看统计信息
stats = manager.get_statistics()
print(f"学生总数: {stats['total_students']}")
print(f"平均年龄: {stats['average_age']}")
print(f"优秀学生: {stats['excellent_students']}")
```

## 🎯 核心功能速查

| 功能 | 方法 | 说明 |
|------|------|------|
| 添加学生 | `manager.add_student(name, age, id, major)` | 添加新学生 |
| 删除学生 | `manager.remove_student(student_id)` | 删除指定学生 |
| 查找学生 | `manager.get_student(student_id)` | 获取学生对象 |
| 搜索学生 | `manager.search_students(keyword)` | 按关键词搜索 |
| 添加成绩 | `student.add_score(subject, score)` | 添加/更新成绩 |
| 平均分 | `student.get_average_score()` | 计算平均分 |
| 成绩排名 | `manager.get_top_students(limit)` | 获取Top N |
| 统计信息 | `manager.get_statistics()` | 系统统计 |
| 保存数据 | `manager.save_data()` | 保存到文件 |
| 导出CSV | `manager.export_to_csv(filename)` | 导出数据 |

## ⚡ 交互式菜单功能

运行 `python main.py` 后的菜单选项:

```
1. 添加学生      - 录入新学生信息
2. 删除学生      - 删除指定学生
3. 修改学生信息  - 更新学生资料
4. 查询学生      - 搜索学生
5. 显示所有学生  - 列出全部学生

6. 添加/修改成绩 - 管理学生成绩
7. 删除成绩      - 删除科目成绩
8. 查看成绩详情  - 显示完整成绩单

9. 系统统计信息  - 查看统计数据
10. 成绩排名     - 显示排行榜
11. 优秀学生列表 - 筛选优秀学生

12. 保存数据     - 手动保存
13. 导出CSV      - 导出Excel格式
14. 清空所有数据 - 重置系统
```

## 📋 数据验证规则

- **学号**: 7位数字,格式如 `2021001`
- **年龄**: 0-150 之间的整数
- **成绩**: 0-100 之间的数值
- **姓名**: 不能为空
- **优秀学生**: 平均分≥85 且无不及格科目

## 🔧 故障排除

### 问题1: 导入错误
```python
ImportError: No module named 'student'
```

**解决**: 确保所有文件在同一目录下运行

### 问题2: 数据未保存
**解决**: 检查是否有写入权限,或手动调用 `manager.save_data()`

### 问题3: 中文显示乱码
**解决**: 确保文件编码为 UTF-8,终端支持中文显示

## 💡 最佳实践

1. **定期保存**: 虽然系统自动保存,但重要操作后建议手动保存
2. **数据备份**: 定期备份 `students_data.json` 文件
3. **导出报表**: 使用CSV导出功能生成Excel报表
4. **验证输入**: 系统会自动验证,但建议确认输入数据正确性
5. **批量操作**: 使用编程接口而非交互界面处理大量数据

## 📞 获取帮助

- 查看完整文档: `README.md`
- 运行演示程序: `python demo.py`
- 执行测试用例: `python test_student_system.py`
- 查看代码注释: 所有代码都有详细的中文注释

## 🎓 学习路径

1. **初级**: 运行 `demo.py` 了解基本功能
2. **中级**: 使用 `main.py` 进行实际操作
3. **高级**: 阅读源码,了解实现原理
4. **专家**: 基于现有代码扩展新功能

---

**祝使用愉快!** 🎉
