# 学生管理系统 - 架构设计文档

## 系统架构概览

```
┌─────────────────────────────────────────────────────────┐
│                    用户交互层 (UI Layer)                  │
├─────────────────────────────────────────────────────────┤
│  main.py - 命令行交互界面 (StudentManagementSystem)      │
│  demo.py - 演示程序                                      │
└──────────────────────┬──────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────┐
│                  业务逻辑层 (Business Layer)              │
├─────────────────────────────────────────────────────────┤
│  student_manager.py - 学生管理器 (StudentManager)        │
│    - 学生增删改查                                         │
│    - 数据持久化                                          │
│    - 统计分析                                            │
│    - 数据导出                                            │
└──────────────────────┬──────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────┐
│                   数据模型层 (Model Layer)                │
├─────────────────────────────────────────────────────────┤
│  student.py - 学生实体类 (Student)                       │
│    - 基本信息管理                                         │
│    - 成绩管理                                            │
│    - 成绩统计                                            │
└──────────────────────┬──────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────┐
│                   工具层 (Utility Layer)                  │
├─────────────────────────────────────────────────────────┤
│  validator.py - 数据验证工具 (Validator)                 │
│  utils.py - 通用工具函数                                 │
└──────────────────────┬──────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────┐
│                   数据持久层 (Persistence Layer)          │
├─────────────────────────────────────────────────────────┤
│  students_data.json - JSON数据文件                       │
│  *.csv - CSV导出文件                                     │
└─────────────────────────────────────────────────────────┘
```

## 核心类设计

### 1. Student 类 (student.py)

**职责**: 学生实体类,管理单个学生的信息和成绩

**属性**:
- `name`: 学生姓名
- `age`: 学生年龄
- `student_id`: 学号(唯一标识)
- `major`: 专业
- `scores`: 成绩字典 {科目: 分数}
- `created_time`: 创建时间

**核心方法**:
```python
add_score(subject, score)      # 添加/更新成绩
remove_score(subject)           # 删除成绩
get_average_score()             # 计算平均分
get_highest_score()             # 获取最高分
get_lowest_score()              # 获取最低分
is_excellent_student()          # 判断是否优秀学生
get_student_info()              # 获取完整信息
```

### 2. StudentManager 类 (student_manager.py)

**职责**: 管理所有学生,提供业务逻辑支持

**属性**:
- `students`: 学生字典 {学号: Student对象}
- `data_file`: 数据文件路径

**核心方法**:
```python
# 学生管理
add_student(name, age, student_id, major)
remove_student(student_id)
update_student_info(student_id, ...)
get_student(student_id)
search_students(keyword)

# 统计分析
get_statistics()
get_top_students(limit)

# 数据持久化
save_data()
load_data()
export_to_csv(filename)
```

### 3. Validator 类 (validator.py)

**职责**: 提供数据验证功能

**核心方法**:
```python
validate_student_id(student_id)  # 验证学号格式
validate_score(score)             # 验证成绩范围
validate_age(age)                 # 验证年龄范围
is_empty(value)                   # 检查空值
is_email(email)                   # 验证邮箱
is_phone(phone)                   # 验证手机号
```

### 4. StudentManagementSystem 类 (main.py)

**职责**: 提供命令行交互界面

**核心方法**:
```python
display_menu()              # 显示主菜单
add_student_menu()          # 添加学生菜单
search_student_menu()       # 搜索学生菜单
show_statistics()           # 显示统计信息
run()                       # 主循环
```

## 数据流图

### 添加学生流程

```
用户输入
   ↓
main.py (add_student_menu)
   ↓
验证数据 (Validator)
   ↓
StudentManager.add_student()
   ↓
创建 Student 对象
   ↓
存入 students 字典
   ↓
自动保存到 JSON 文件
```

### 成绩统计流程

```
用户请求统计
   ↓
StudentManager.get_statistics()
   ↓
遍历所有 Student 对象
   ↓
调用 Student.get_average_score()
   ↓
聚合计算统计数据
   ↓
返回统计结果
   ↓
格式化显示给用户
```

## 设计模式

### 1. 单一职责原则 (SRP)
- `Student`: 只负责单个学生的数据和逻辑
- `StudentManager`: 只负责管理多个学生
- `Validator`: 只负责数据验证

### 2. 开闭原则 (OCP)
- 易于扩展新的统计方法
- 可以添加新的验证规则
- 支持新的数据导出格式

### 3. 依赖倒置原则 (DIP)
- UI层依赖于业务逻辑层的抽象
- 业务逻辑不依赖于具体的存储实现

## 数据模型

### JSON 数据结构

```json
{
  "students": [
    {
      "name": "张三",
      "age": 20,
      "student_id": "2021001",
      "major": "计算机科学",
      "scores": {
        "数学": 95.0,
        "英语": 88.0
      },
      "created_time": "2025-10-13 10:30:00"
    }
  ],
  "save_time": "2025-10-13 15:20:30"
}
```

### CSV 导出格式

```csv
学号,姓名,年龄,专业,平均成绩,最高分,最低分,科目数
2021001,张三,20,计算机科学,91.50,95.0,88.0,2
```

## 模块依赖关系

```
main.py
  ├─→ student_manager.py
  │     ├─→ student.py
  │     ├─→ validator.py
  │     └─→ utils.py
  └─→ utils.py

demo.py
  ├─→ student_manager.py
  ├─→ student.py
  └─→ utils.py

test_student_system.py
  ├─→ student.py
  ├─→ student_manager.py
  └─→ validator.py
```

## 扩展性设计

### 1. 数据库支持
可以创建 `DatabaseManager` 替代当前的 JSON 存储:

```python
class DatabaseManager(StudentManager):
    def save_data(self):
        # 保存到数据库
        pass
    
    def load_data(self):
        # 从数据库加载
        pass
```

### 2. Web接口支持
可以基于现有业务逻辑添加Web层:

```python
from flask import Flask
from student_manager import StudentManager

app = Flask(__name__)
manager = StudentManager()

@app.route('/api/students', methods=['GET'])
def get_students():
    return jsonify(manager.get_all_students())
```

### 3. 新增统计维度
在 `StudentManager` 中添加新方法:

```python
def get_subject_statistics(self, subject):
    """获取指定科目的统计信息"""
    scores = []
    for student in self.students.values():
        score = student.get_score(subject)
        if score is not None:
            scores.append(score)
    
    return {
        'average': sum(scores) / len(scores),
        'highest': max(scores),
        'lowest': min(scores)
    }
```

## 性能优化建议

### 1. 索引优化
当学生数量很大时,可以添加索引:

```python
class StudentManager:
    def __init__(self):
        self.students = {}
        self.name_index = {}      # 姓名索引
        self.major_index = {}     # 专业索引
```

### 2. 延迟加载
对于大数据集,可以实现延迟加载:

```python
def get_student(self, student_id):
    if student_id not in self.students:
        self._load_student_from_db(student_id)
    return self.students.get(student_id)
```

### 3. 缓存优化
缓存常用的统计结果:

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def get_statistics(self):
    # 统计计算
    pass
```

## 安全性考虑

1. **输入验证**: 所有用户输入都经过 `Validator` 验证
2. **数据备份**: 保存前先备份旧数据
3. **错误处理**: 完善的异常捕获和错误提示
4. **确认机制**: 删除等危险操作需要二次确认

## 测试策略

### 单元测试
- `TestStudent`: 测试学生类的所有方法
- `TestStudentManager`: 测试管理器的业务逻辑
- `TestValidator`: 测试验证器的规则

### 集成测试
- 测试完整的业务流程
- 测试数据持久化
- 测试并发访问(如需要)

### 覆盖率目标
- 代码覆盖率 > 80%
- 核心业务逻辑覆盖率 100%

## 版本历史

- **v1.0** (2025-10-11): 基础学生类实现
- **v2.0** (2025-10-13): 完整管理系统实现
  - 添加学生管理器
  - 添加交互式界面
  - 添加数据持久化
  - 添加完整测试

## 未来规划

- [ ] 添加课程管理模块
- [ ] 实现成绩变化趋势分析
- [ ] 支持多种数据导出格式(PDF, Excel)
- [ ] 添加图形化界面(GUI)
- [ ] 实现Web版本
- [ ] 添加用户权限管理
- [ ] 支持批量导入功能
- [ ] 实现数据可视化

---

**文档版本**: 1.0  
**最后更新**: 2025-10-13
