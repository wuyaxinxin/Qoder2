#!/bin/bash
# 吃鱼小游戏启动脚本

echo "吃鱼小游戏 - 启动中..."
echo ""

# 检查Python
if command -v python3 &> /dev/null; then
    PYTHON=python3
elif command -v python &> /dev/null; then
    PYTHON=python
else
    echo "错误: 未找到Python，请先安装Python 3.6+"
    exit 1
fi

echo "使用Python: $PYTHON"
$PYTHON --version
echo ""

# 检查pygame
echo "检查pygame..."
$PYTHON -c "import pygame" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "pygame未安装，正在安装..."
    $PYTHON -m pip install pygame
    if [ $? -ne 0 ]; then
        echo "错误: pygame安装失败"
        echo "请手动运行: pip install pygame"
        exit 1
    fi
fi

echo "pygame已就绪"
echo ""
echo "启动游戏..."
echo ""

# 运行游戏
$PYTHON fish_game.py
