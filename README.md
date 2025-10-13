# 学生管理系统

一个功能完善的学生信息管理系统，提供学生信息管理、成绩管理、数据统计分析等功能。

## 功能特性

### 📚 学生管理
- ✅ 添加学生：录入学生基本信息（姓名、年龄、学号、专业）
- ✅ 删除学生：根据学号删除学生信息
- ✅ 修改学生信息：更新学生的基本信息
- ✅ 查询学生：支持按姓名、学号、专业搜索
- ✅ 显示所有学生：列表展示所有学生信息

### 📊 成绩管理
- ✅ 添加/修改成绩：为学生添加或更新各科成绩
- ✅ 删除成绩：删除指定科目成绩
- ✅ 查看成绩详情：显示学生完整的成绩信息和统计数据
- ✅ 成绩验证：自动验证成绩范围（0-100）

### 📈 统计分析
- ✅ 系统统计：学生总数、平均年龄、专业分布
- ✅ 成绩排名：按平均分排序显示Top N学生
- ✅ 优秀学生筛选：自动识别优秀学生（平均分≥85且无不及格）
- ✅ 及格率统计：统计每个学生的及格科目数

### 💾 数据管理
- ✅ 数据持久化：JSON格式存储，自动保存
- ✅ 数据加载：启动时自动加载历史数据
- ✅ CSV导出：支持导出为Excel可读的CSV文件
- ✅ 数据清空：提供安全的数据清空功能

## 项目结构

```
Qoder2/
├── student.py              # 学生类定义
├── student_manager.py      # 学生管理器核心模块
├── main.py                 # 主程序（交互式界面）
├── validator.py            # 数据验证模块
├── utils.py                # 工具函数集合
├── test_student_system.py  # 单元测试
├── README.md               # 项目说明文档
└── students_data.json      # 数据文件（自动生成）
```

## 安装与运行

### 环境要求
- Python 3.7 或更高版本
- 无需额外依赖包（仅使用Python标准库）

### 运行系统

```bash
# 启动学生管理系统
python3 main.py
```

### 运行测试

```bash
# 运行单元测试
python3 test_student_system.py
```

## 使用示例

### 编程接口使用

```python
from student import Student
from student_manager import StudentManager

# 创建管理器
manager = StudentManager()

# 添加学生
manager.add_student("张三", 20, "2021001", "计算机科学")
manager.add_student("李四", 19, "2021002", "数学")

# 添加成绩
student = manager.get_student("2021001")
student.add_score("高等数学", 95)
student.add_score("程序设计", 88)

# 查询统计
stats = manager.get_statistics()
print(f"学生总数: {stats['total_students']}")

# 成绩排名
top_students = manager.get_top_students(5)
for student, avg_score in top_students:
    print(f"{student.name}: {avg_score:.2f}")

# 保存数据
manager.save_data()
```

### 交互式界面

运行 `main.py` 后，通过菜单选择功能：

```
============================================================
                    学生管理系统
============================================================
【学生管理】
  1. 添加学生
  2. 删除学生
  3. 修改学生信息
  4. 查询学生
  5. 显示所有学生

【成绩管理】
  6. 添加/修改成绩
  7. 删除成绩
  8. 查看学生成绩详情

【统计分析】
  9. 系统统计信息
 10. 成绩排名
 11. 优秀学生列表

【数据管理】
 12. 保存数据
 13. 导出CSV
 14. 清空所有数据

  0. 退出系统
============================================================
```

## 核心类说明

### Student 类
学生基本信息和成绩管理

**主要方法：**
- `add_score(subject, score)` - 添加/更新成绩
- `get_average_score()` - 计算平均分
- `get_highest_score()` - 获取最高分
- `is_excellent_student()` - 判断是否优秀学生

### StudentManager 类
学生管理系统核心

**主要方法：**
- `add_student()` - 添加学生
- `remove_student()` - 删除学生
- `search_students()` - 搜索学生
- `get_statistics()` - 获取统计信息
- `save_data()` / `load_data()` - 数据持久化

### Validator 类
数据验证工具

**主要方法：**
- `validate_student_id()` - 验证学号格式
- `validate_score()` - 验证成绩范围
- `validate_age()` - 验证年龄范围

## 数据格式

### JSON数据格式

```json
{
  "students": [
    {
      "name": "张三",
      "age": 20,
      "student_id": "2021001",
      "major": "计算机科学",
      "scores": {
        "高等数学": 95,
        "程序设计": 88
      },
      "created_time": "2025-10-13 10:30:00"
    }
  ],
  "save_time": "2025-10-13 15:20:30"
}
```

## 测试覆盖

系统包含完整的单元测试，覆盖以下模块：

- ✅ Student 类测试（18个测试用例）
- ✅ StudentManager 类测试（8个测试用例）
- ✅ Validator 类测试（4个测试用例）

总计 30+ 个测试用例，确保系统稳定性。

## 特色功能

1. **智能验证**：自动验证学号、年龄、成绩等数据的合法性
2. **数据安全**：删除和清空操作需要二次确认
3. **自动保存**：每次操作后自动保存数据
4. **中文友好**：完整的中文界面和提示
5. **统计分析**：丰富的数据统计和排名功能
6. **灵活搜索**：支持多关键词模糊搜索
7. **数据导出**：支持导出为CSV格式供Excel使用

## 后续扩展建议

- [ ] 添加Web界面（Flask/Django）
- [ ] 支持数据库存储（SQLite/MySQL）
- [ ] 添加图表可视化功能
- [ ] 支持批量导入学生信息
- [ ] 添加课程管理模块
- [ ] 实现用户权限管理
- [ ] 支持成绩变化趋势分析

## 开发信息

- **开发语言**: Python 3.7+
- **编码规范**: PEP 8
- **文档风格**: Google Python Style Guide
- **版本**: 2.0
- **最后更新**: 2025-10-13

## 许可证

MIT License

## 贡献

欢迎提交Issue和Pull Request！
