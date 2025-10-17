# 课程管理与选课功能模块

## 概述

本模块为学生管理系统扩展了完整的课程管理和选课功能,实现了学生、课程、成绩三者的有机结合,构建了完整的教学管理闭环。

## 核心功能

### 1. 课程信息管理
- ✅ 添加课程（课程ID、名称、教师、学分、容量等）
- ✅ 删除课程（仅允许删除无人选课的课程）
- ✅ 修改课程信息
- ✅ 查询课程（按ID、名称、教师、学期）
- ✅ 列出所有课程（支持排序）

### 2. 选课管理
- ✅ 学生选课（容量限制、重复检查）
- ✅ 学生退课
- ✅ 查看学生选课列表
- ✅ 查看课程学生名单
- ✅ 批量选课操作

### 3. 成绩关联
- ✅ 录入课程成绩（选课前提检查）
- ✅ 成绩双向同步（学生对象+选课记录）
- ✅ 修改已录入成绩
- ✅ 查询课程成绩

### 4. 统计分析
- ✅ 课程统计（选课率、平均分、优秀率、及格率）
- ✅ 学生统计（总学分、已获学分、GPA）
- ✅ 热门课程排行
- ✅ 教师课程统计
- ✅ 学期课程统计
- ✅ 系统总览

### 5. 数据管理
- ✅ JSON格式持久化存储
- ✅ 数据自动保存与加载
- ✅ 数据备份与恢复
- ✅ CSV格式导出

## 文件结构

```
课程管理模块文件:
├── course.py                      # 课程实体模型类
├── course_management_system.py    # 课程管理系统核心逻辑
├── course_data_manager.py         # 课程数据持久化管理
├── course_statistics.py           # 课程统计分析模块
├── integrated_system.py           # 学生-课程一体化系统
├── course_cli.py                  # 课程管理命令行界面
├── test_course_system.py          # 课程系统单元测试
└── demo_course_system.py          # 功能演示脚本
```

## 数据模型

### Course类（课程实体）
```python
属性:
- course_id: 课程唯一标识 (如CS101)
- course_name: 课程名称
- teacher: 授课教师
- credit: 学分 (0.5-10.0)
- capacity: 课程容量 (1-500)
- enrolled_count: 已选课人数（自动维护）
- description: 课程描述
- semester: 开课学期
- schedule: 上课时间
- enrolled_students: 选课学生集合
```

### 选课关联（Enrollment）
```python
结构:
- student_id: 学生学号
- course_id: 课程ID
- enrollment_time: 选课时间
- status: 选课状态（enrolled/dropped）
- score: 课程成绩（可选）
```

## 使用指南

### 1. 快速开始

```python
from integrated_system import IntegratedSystem

# 创建一体化系统
system = IntegratedSystem()

# 添加课程
system.course_system.add_course(
    course_id="CS101",
    course_name="数据结构与算法",
    teacher="张教授",
    credit=3.0,
    capacity=60
)

# 学生选课
system.enroll_student_to_course("2021001", "CS101")

# 录入成绩
system.set_course_score_integrated("2021001", "CS101", 95.0)

# 保存数据
system.save_all_data()
```

### 2. 运行命令

#### 启动完整系统（包含课程管理）
```bash
python3 main.py
```

#### 运行单元测试
```bash
python3 test_course_system.py
```

#### 运行功能演示
```bash
python3 demo_course_system.py
```

### 3. 命令行界面菜单

```
主菜单:
├── 1. 学生管理
├── 2. 课程管理 ⭐ 新增
│   ├── 2.1 课程信息管理
│   │   ├── 添加课程
│   │   ├── 删除课程
│   │   ├── 修改课程
│   │   ├── 查询课程
│   │   └── 列出所有课程
│   ├── 2.2 选课管理
│   │   ├── 学生选课
│   │   ├── 学生退课
│   │   ├── 查看学生选课列表
│   │   └── 查看课程学生名单
│   └── 2.3 课程统计
│       ├── 课程选课统计
│       ├── 课程成绩分析
│       ├── 学生选课汇总
│       ├── 热门课程排行
│       └── 教师课程统计
└── 3. 数据管理
```

## 数据验证规则

### 课程ID格式
- 格式: 2-3个大写字母 + 3位数字
- 示例: CS101, MATH201, ENG101
- 错误示例: cs101, C101, CS1

### 学分范围
- 范围: 0.5 - 10.0
- 类型: 浮点数

### 课程容量
- 范围: 1 - 500
- 类型: 正整数

### 课程名称
- 长度: 2 - 50 字符
- 不能为空

## 业务规则

### 选课规则
1. ✅ 学生必须存在
2. ✅ 课程必须存在
3. ✅ 检查课程容量限制
4. ✅ 不允许重复选课
5. ✅ 满员课程拒绝选课

### 退课规则
1. ✅ 必须已选该课程
2. ✅ 默认不允许退已有成绩的课程
3. ✅ 可选：强制退课（allow_with_score=True）

### 删除课程规则
1. ✅ 仅允许删除无人选课的课程
2. ✅ 有学生选课时拒绝删除
3. ✅ 删除课程时同步清理选课记录

### 成绩录入规则
1. ✅ 学生必须已选该课程
2. ✅ 成绩范围: 0-100
3. ✅ 同时更新学生对象和选课记录
4. ✅ 支持成绩覆盖更新

## 统计指标说明

### 课程统计
- **选课率** = (已选人数 / 课程容量) × 100%
- **优秀率** = (成绩≥85分人数 / 总人数) × 100%
- **及格率** = (成绩≥60分人数 / 总人数) × 100%
- **分数段分布**: 90-100, 80-89, 70-79, 60-69, 0-59

### 学生统计
- **总学分**: 所选课程学分之和
- **已获学分**: 已通过(≥60分)课程学分之和
- **GPA**: (成绩×学分)之和 / 总学分

## 测试覆盖

### 单元测试（25个测试用例）
- ✅ Course类测试（9个用例）
- ✅ CourseManagementSystem测试（8个用例）
- ✅ CourseStatistics测试（3个用例）
- ✅ CourseDataManager测试（1个用例）
- ✅ IntegratedSystem集成测试（3个用例）

### 测试结果
```
Ran 25 tests in 0.015s
OK - ✓ 所有测试通过!
```

## 数据文件

### courses_data.json 结构
```json
{
  "courses": {
    "CS101": {
      "course_id": "CS101",
      "course_name": "数据结构与算法",
      "teacher": "张教授",
      "credit": 3.0,
      "capacity": 60,
      "enrolled_students": ["2021001", "2021002"],
      "created_time": "2025-10-16T10:00:00"
    }
  },
  "enrollments": {
    "2021001_CS101": {
      "student_id": "2021001",
      "course_id": "CS101",
      "enrollment_time": "2025-10-16T10:30:00",
      "status": "enrolled",
      "score": 95.0
    }
  },
  "metadata": {
    "total_courses": 1,
    "total_enrollments": 1,
    "last_updated": "2025-10-16T11:00:00",
    "version": "1.0"
  }
}
```

## 技术特性

### 面向对象设计
- ✅ 完整的类封装
- ✅ 清晰的职责分离
- ✅ 良好的可扩展性

### 数据持久化
- ✅ JSON格式存储
- ✅ 自动序列化/反序列化
- ✅ 数据完整性保证

### 错误处理
- ✅ 完善的数据验证
- ✅ 友好的错误提示
- ✅ 异常安全保证

### 性能优化
- ✅ 使用set存储选课学生（O(1)查找）
- ✅ 索引式课程查询
- ✅ 高效的统计算法

## 扩展功能建议

### 已实现
- ✅ 基础课程管理
- ✅ 选课退课
- ✅ 成绩管理
- ✅ 统计分析

### 可扩展方向
- ⭕ 选课时间冲突检测
- ⭕ 课程先修关系管理
- ⭕ 学分达标检查
- ⭕ 选课候补队列
- ⭕ 教师评价系统
- ⭕ 课程评分系统
- ⭕ 成绩分布图表
- ⭕ 导出PDF成绩单

## 常见问题

### Q: 如何修改课程容量？
A: 使用 `course_system.update_course(course_id, capacity=新容量)`，但新容量不能小于已选人数。

### Q: 如何强制退课？
A: 使用 `course_system.drop_course(student_id, course_id, allow_with_score=True)`

### Q: 数据文件存储在哪里？
A: 默认存储在 `data/` 目录下，学生数据为 `students_data.json`，课程数据为 `courses_data.json`

### Q: 如何备份数据？
A: 使用 `system.backup_all_data()` 会自动备份到 `data/backups/` 目录

### Q: 如何导出课程数据？
A: 使用 `course_data_manager.export_courses_csv(course_system)` 导出为CSV格式

## 更新日志

### v1.0 (2025-10-16)
- ✅ 实现课程基本管理功能
- ✅ 实现选课退课功能
- ✅ 实现成绩关联功能
- ✅ 实现统计分析功能
- ✅ 实现数据持久化
- ✅ 完成单元测试（25个用例全部通过）
- ✅ 集成到主系统

## 作者与贡献

开发者: AI Assistant
创建日期: 2025-10-16
版本: 1.0

## 许可证

本项目基于学生管理系统扩展开发，遵循相同的许可协议。
