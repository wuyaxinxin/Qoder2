#!/bin/bash

# 课程管理系统快速启动脚本
# Quick Start Script for Course Management System

echo "========================================="
echo "  课程管理系统 - 快速启动"
echo "  Course Management System - Quick Start"
echo "========================================="
echo ""

# 检查Python版本
echo "检查Python环境..."
python3 --version
if [ $? -ne 0 ]; then
    echo "错误: 未找到python3,请先安装Python 3.x"
    exit 1
fi
echo "✓ Python环境正常"
echo ""

# 选择启动模式
echo "请选择启动模式:"
echo "1. 运行测试 (Run Tests)"
echo "2. 运行演示 (Run Demo)"
echo "3. 启动主程序 (Launch Main Program)"
echo "4. 查看文档 (View Documentation)"
echo ""
read -p "请输入选项 (1-4): " choice

case $choice in
    1)
        echo ""
        echo "========================================="
        echo "  运行单元测试..."
        echo "========================================="
        python3 test_course_system.py
        ;;
    2)
        echo ""
        echo "========================================="
        echo "  运行功能演示..."
        echo "========================================="
        python3 demo_course_system.py
        ;;
    3)
        echo ""
        echo "========================================="
        echo "  启动课程管理系统主程序..."
        echo "========================================="
        python3 main.py
        ;;
    4)
        echo ""
        echo "========================================="
        echo "  查看系统文档..."
        echo "========================================="
        if command -v less &> /dev/null; then
            less COURSE_README.md
        else
            cat COURSE_README.md
        fi
        ;;
    *)
        echo "无效选项,请重新运行脚本"
        exit 1
        ;;
esac
