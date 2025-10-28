# 学生管理系统 - 快速开始指南

## 🚀 5分钟快速启动

### 1. 环境检查

```bash
# 检查Java版本(需要JDK 8+)
java -version

# 检查Python版本(需要Python 3.7+)
python3 --version

# 检查必要文件
ls json.jar  # 确认JSON库存在
```

### 2. 运行演示程序

#### 方式一:一键运行(推荐)

```bash
# 编译并运行Java演示程序
javac -encoding UTF-8 -cp .:json.jar *.java && \
java -cp .:json.jar StudentSystemDemo
```

#### 方式二:分步执行

```bash
# 步骤1: 编译Java文件
javac -encoding UTF-8 -cp .:json.jar \
  DataStorage.java \
  StudentService.java \
  CourseService.java \
  TeacherService.java \
  GradeService.java \
  StudentSystemDemo.java

# 步骤2: 运行演示程序
java -cp .:json.jar StudentSystemDemo
```

**预期输出**:
```
========== 学生管理系统演示 ==========

【演示1】创建教师
成功:教师创建成功

【演示2】创建课程
成功:课程创建成功
...

========== 演示完成 ==========
提示: 数据已保存到 data/ 目录
```

### 3. 生成数据分析报表

```bash
# 运行Python报表生成脚本
python3 generate_reports.py
```

**预期输出**:
```
============================================================
                  学生管理系统报表生成                  
============================================================

正在加载数据...
✓ 学生数据: 2 条记录
✓ 课程数据: 2 条记录
✓ 教师数据: 1 条记录

【1/6】生成成绩分布报表...
  ✓ 已保存: reports/score_distribution_*.txt
【2/6】生成专业统计报表...
  ✓ 已保存: reports/major_statistics_*.txt
...
```

### 4. 查看报表

```bash
# 查看成绩分布报表
cat reports/score_distribution_*.txt

# 查看优秀学生名单
cat reports/excellent_students_*.txt

# 列出所有报表
ls -lh reports/
```

## 📂 目录结构说明

```
student-system-design-1761637287/
├── json.jar                        ⭐ JSON库(必需)
├── *.java                          ⭐ Java源代码
├── *.py                            ⭐ Python脚本
├── data/                           📁 数据文件目录
│   ├── students.json               ✅ 学生数据
│   ├── courses.json                ✅ 课程数据
│   ├── teachers.json               ✅ 教师数据
│   └── backups/                    💾 自动备份
└── reports/                        📊 报表输出目录
```

## 🎯 核心功能演示

### 功能1: 学生管理
- ✅ 创建学生: `StudentService.createStudent()`
- ✅ 查询学生: `StudentService.getStudentById()`
- ✅ 更新学生: `StudentService.updateStudent()`
- ✅ 删除学生: `StudentService.deleteStudent()`
- ✅ 搜索学生: 按专业/年级/姓名

### 功能2: 课程管理
- ✅ 创建课程: `CourseService.createCourse()`
- ✅ 学生选课: `CourseService.enrollStudent()`
- ✅ 学生退课: `CourseService.dropStudent()`
- ✅ 查询选课: `CourseService.getEnrolledStudents()`

### 功能3: 成绩管理
- ✅ 录入成绩: `GradeService.recordGrade()`
- ✅ 查询成绩: `GradeService.getStudentGrades()`
- ✅ 统计分析: `GradeService.calculateAverage()`
- ✅ 通过率: `GradeService.getCoursePassRate()`

### 功能4: 数据分析
- ✅ 成绩分布统计
- ✅ 专业平均分排名
- ✅ 课程选课热度
- ✅ 教师工作量统计
- ✅ 优秀学生识别
- ✅ 课程通过率分析

## 🔧 常见问题

### Q1: 编译时提示"找不到json包"
**解决方案**:
```bash
# 确保使用-cp参数指定json.jar路径
javac -encoding UTF-8 -cp .:json.jar *.java

# 如果json.jar不存在,下载:
curl -o json.jar \
  https://repo1.maven.org/maven2/org/json/json/20231013/json-20231013.jar
```

### Q2: 运行时提示"找不到主类"
**解决方案**:
```bash
# 确保运行时也指定-cp参数
java -cp .:json.jar StudentSystemDemo

# Windows系统使用分号分隔:
java -cp .;json.jar StudentSystemDemo
```

### Q3: Python报表生成失败
**解决方案**:
```bash
# 1. 确认已运行Java程序生成数据
java -cp .:json.jar StudentSystemDemo

# 2. 检查data目录是否存在
ls data/*.json

# 3. 重新运行报表生成
python3 generate_reports.py
```

### Q4: 中文显示乱码
**解决方案**:
```bash
# 编译时指定UTF-8编码
javac -encoding UTF-8 -cp .:json.jar *.java

# 确保终端支持UTF-8编码
export LANG=zh_CN.UTF-8
```

## 📊 数据示例

### 演示数据说明
运行`StudentSystemDemo.java`会自动创建:
- **1名教师**: 张教授(T001) - 计算机科学专业
- **2门课程**: 
  - CS101 - 数据结构与算法(4学分)
  - CS102 - 操作系统原理(3学分)
- **2名学生**:
  - 李明(2021001) - 计算机科学专业3年级
  - 王芳(2021002) - 计算机科学专业3年级

### 成绩数据
- 李明: CS101(92.5分), CS102(85.5分), 平均89.0分
- 王芳: CS101(88.0分), 平均88.0分

## 🎓 下一步

### 学习建议
1. 阅读`README_IMPLEMENTATION.md` - 了解系统架构
2. 查看`TESTING_SUMMARY.md` - 了解测试覆盖
3. 研究源代码注释 - 理解业务逻辑
4. 修改数据验证规则 - 自定义业务需求

### 扩展开发
1. 添加更多实体类(如Department、Course等)
2. 实现更复杂的查询功能
3. 添加Excel导入导出功能
4. 开发Web界面
5. 集成数据库

## 📞 技术支持

### 文档资源
- 设计文档: `student-system-design.md`
- 实现说明: `README_IMPLEMENTATION.md`
- 测试总结: `TESTING_SUMMARY.md`
- 本快速指南: `QUICK_START.md`

### 源代码
- 数据存储层: `DataStorage.java`
- 业务服务层: `*Service.java`
- 数据分析: `data_processor.py`
- 报表生成: `generate_reports.py`

---

**祝您使用愉快!** 🎉

如有问题,请参考文档或检查源代码注释。
