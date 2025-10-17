#!/bin/bash
# 始终生效
# 重置 macOS 共享服务缓存脚本

echo "正在重启 sharingd 服务..."

# 停止 sharingd 服务
sudo killall -HUP sharingd

echo "sharingd 服务已重启"
echo "请尝试使用 AirDrop 或其他共享功能来重建缓存"

# 检查缓存目录
CACHE_DIR="$HOME/Library/Caches/com.apple.sharingd"
echo ""
echo "缓存目录位置: $CACHE_DIR"

if [ -d "$CACHE_DIR" ]; then
    echo "缓存目录存在"
    ls -lah "$CACHE_DIR"
else
    echo "缓存目录不存在"
fi
