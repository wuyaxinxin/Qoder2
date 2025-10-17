#!/bin/bash

# 云效工具示例快速查看脚本

echo "=============================================="
echo "   云效（Yunxiao）工具使用示例"
echo "=============================================="
echo ""

echo "📚 可用文档："
echo "  1. yunxiao_demo.py          - Python示例代码"
echo "  2. YUNXIAO_USAGE_GUIDE.md   - 详细使用指南"
echo "  3. YUNXIAO_DEMO_SUMMARY.md  - 完成总结报告"
echo ""

echo "🚀 快速开始："
echo "  运行示例: python3 yunxiao_demo.py"
echo "  查看指南: cat YUNXIAO_USAGE_GUIDE.md"
echo "  查看总结: cat YUNXIAO_DEMO_SUMMARY.md"
echo ""

echo "💡 主要功能："
echo "  ✓ 获取用户和组织信息"
echo "  ✓ 查询项目列表"
echo "  ✓ 搜索工作项（任务/Bug/需求）"
echo "  ✓ 管理代码仓库"
echo "  ✓ 监控CI/CD流水线"
echo "  ✓ 创建和更新工作项"
echo ""

echo "⚙️  配置要求："
echo "  1. 登录云效后台获取访问令牌"
echo "  2. 获取组织ID"
echo "  3. 在IDE中配置云效插件"
echo ""

read -p "是否运行示例程序? (y/n) " choice
if [ "$choice" = "y" ] || [ "$choice" = "Y" ]; then
    echo ""
    echo "运行 yunxiao_demo.py..."
    echo "=============================================="
    python3 yunxiao_demo.py
else
    echo ""
    echo "提示: 使用 python3 yunxiao_demo.py 运行示例"
fi
