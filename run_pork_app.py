# 始终生效

from pork_price_app.app import app

if __name__ == '__main__':
    print("=" * 60)
    print("NVIDIA芯片销量可视化应用启动中...")
    print("=" * 60)
    print("访问地址: http://localhost:5000")
    print("按 Ctrl+C 停止服务")
    print("=" * 60)
    app.run(debug=True, port=5000, host='127.0.0.1')