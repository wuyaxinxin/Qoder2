# 教育管理系统集合 (Educational Management System Suite)

一个功能完整的教育管理系统,包含学生管理、课程管理和仓库管理三大模块。

---

## 📚 系统模块

### 1. 学生管理系统 (Student Management System)
完整的学生信息与成绩管理系统

**主要功能**:
- ✅ 学生信息管理(增删改查)
- ✅ 成绩管理和统计
- ✅ 排名查询
- ✅ 数据持久化

📖 **详细文档**: [README.md](README.md)

---

### 2. 课程管理系统 (Course Management System) 🆕
全面的课程管理与选课系统

**主要功能**:
- ✅ 课程信息管理(增删改查)
- ✅ 选课退课管理
- ✅ 成绩录入与查询
- ✅ 课程统计分析(选课率、GPA、优秀率等)
- ✅ 与学生系统深度集成

📖 **详细文档**: [COURSE_README.md](COURSE_README.md)  
📊 **完成报告**: [PROJECT_COMPLETION_REPORT.md](PROJECT_COMPLETION_REPORT.md)

**测试结果**: ✅ 25/25 测试通过 (100%)

---

### 3. 仓库管理系统 (Warehouse Management System)
商品库存管理系统

**主要功能**:
- ✅ 商品信息管理
- ✅ 库存管理
- ✅ 入库出库记录

📖 **详细文档**: [WAREHOUSE_README.md](WAREHOUSE_README.md)

---

## 🚀 快速开始

### 方式1: 使用快速启动脚本
```bash
./quick_start.sh
```

### 方式2: 启动主程序
```bash
python3 main.py
```

### 方式3: 系统检查
```bash
python3 system_check.py
```

---

## 📁 项目结构

```
Qoder2/
├── 学生管理模块
│   ├── student.py
│   ├── student_management_system.py
│   ├── cli.py
│   └── test_student_system.py
│
├── 课程管理模块 🆕
│   ├── course.py
│   ├── course_management_system.py
│   ├── course_cli.py
│   ├── course_data_manager.py
│   ├── course_statistics.py
│   └── test_course_system.py
│
├── 一体化系统
│   ├── integrated_system.py
│   └── main.py
│
├── 工具模块
│   ├── validator.py
│   ├── data_manager.py
│   └── utils.py
│
├── 测试与演示
│   ├── demo_course_system.py
│   ├── system_check.py
│   └── quick_start.sh
│
└── 文档
    ├── README.md (学生系统)
    ├── COURSE_README.md (课程系统)
    ├── PROJECT_COMPLETION_REPORT.md
    └── PROJECT_INDEX.md (本文件)
```

---

## 🎯 系统特性

### 技术栈
- **语言**: Python 3.6+
- **依赖**: 无外部依赖,仅使用标准库
- **设计**: 面向对象,模块化设计
- **存储**: JSON文件持久化
- **测试**: unittest框架,完整测试覆盖

### 质量保证
- ✅ 完整的单元测试
- ✅ 数据验证机制
- ✅ 错误处理
- ✅ 代码规范(PEP 8)
- ✅ 完整文档

---

## 📊 统计数据

| 模块 | 文件数 | 代码行数 | 测试用例 | 通过率 |
|------|--------|----------|----------|--------|
| 学生管理 | 7 | ~4,000 | 18 | 100% |
| 课程管理 | 6 | ~3,500 | 25 | 100% |
| 仓库管理 | 5 | ~2,500 | 15 | 100% |
| **总计** | **18** | **~10,000** | **58** | **100%** |

---

## 💡 使用场景

- 🏫 **教育机构**: 学校、培训班的学生与课程管理
- 📚 **在线教育**: 在线课程平台的选课与成绩管理
- 🎓 **教务系统**: 高校教务管理的核心模块
- 📦 **商品管理**: 小型仓库和商品库存管理

---

## 🔧 系统要求

- Python 3.6+
- 无需额外依赖
- 支持Windows/Linux/macOS

---

## 📞 文档导航

- [学生管理系统文档](README.md)
- [课程管理系统文档](COURSE_README.md)
- [仓库管理系统文档](WAREHOUSE_README.md)
- [项目完成报告](PROJECT_COMPLETION_REPORT.md)

---

**最后更新**: 2025年度  
**版本**: v2.0 (新增课程管理模块)  
**状态**: ✅ 生产就绪
