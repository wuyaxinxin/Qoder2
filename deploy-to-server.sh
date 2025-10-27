#!/bin/bash
#############################################
# Qoder2 远程服务器部署脚本
# 用途: 将Qoder2项目部署到远程服务器
#############################################

# ========== 配置区域 ==========
SERVER="user@your-server-ip"          # 修改为你的服务器地址
REMOTE_PATH="/opt/apps/Qoder2"        # 远程部署路径
LOCAL_PATH="/Users/admin/Documents/testQoder/Qoder2"  # 本地项目路径
APP_PORT=8080                         # 应用端口

# 颜色输出
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}🚀 Qoder2 远程服务器部署脚本${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""

# ========== 步骤1: 检查本地环境 ==========
echo -e "${YELLOW}📋 步骤1: 检查本地环境...${NC}"

if [ ! -d "$LOCAL_PATH" ]; then
    echo -e "${RED}❌ 错误: 找不到项目目录 $LOCAL_PATH${NC}"
    exit 1
fi

cd "$LOCAL_PATH" || exit 1
echo -e "${GREEN}✅ 本地项目目录: $LOCAL_PATH${NC}"

# ========== 步骤2: 创建Web服务入口 ==========
echo -e "${YELLOW}📋 步骤2: 创建Web服务入口...${NC}"

cat > QoderWebServer.java << 'JAVA'
import com.sun.net.httpserver.HttpServer;
import com.sun.net.httpserver.HttpExchange;
import java.io.OutputStream;
import java.io.IOException;
import java.net.InetSocketAddress;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

/**
 * Qoder2 Web服务器
 * 提供HTTP访问接口
 */
public class QoderWebServer {
    
    public static void main(String[] args) throws Exception {
        int port = 8080;
        HttpServer server = HttpServer.create(new InetSocketAddress(port), 0);
        
        // 主页
        server.createContext("/", QoderWebServer::handleRoot);
        
        // API - 系统信息
        server.createContext("/api/info", QoderWebServer::handleInfo);
        
        // API - 健康检查
        server.createContext("/api/health", QoderWebServer::handleHealth);
        
        // API - 项目文件列表
        server.createContext("/api/files", QoderWebServer::handleFiles);
        
        server.start();
        System.out.println("✅ Qoder2 Web服务已启动!");
        System.out.println("🌐 访问地址: http://0.0.0.0:" + port);
        System.out.println("📊 API文档: http://0.0.0.0:" + port + "/api/info");
    }
    
    // 主页处理
    private static void handleRoot(HttpExchange exchange) throws IOException {
        String html = """
            <!DOCTYPE html>
            <html lang="zh-CN">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Qoder2 应用</title>
                <style>
                    * { margin: 0; padding: 0; box-sizing: border-box; }
                    body {
                        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
                        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                        min-height: 100vh;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        padding: 20px;
                    }
                    .container {
                        background: white;
                        border-radius: 20px;
                        padding: 40px;
                        box-shadow: 0 20px 60px rgba(0,0,0,0.3);
                        max-width: 600px;
                        width: 100%;
                    }
                    h1 {
                        color: #333;
                        margin-bottom: 10px;
                        font-size: 2.5em;
                    }
                    .status {
                        display: inline-block;
                        background: #10b981;
                        color: white;
                        padding: 8px 16px;
                        border-radius: 20px;
                        font-weight: bold;
                        margin: 20px 0;
                    }
                    .info-box {
                        background: #f3f4f6;
                        padding: 20px;
                        border-radius: 10px;
                        margin: 20px 0;
                    }
                    .info-item {
                        margin: 10px 0;
                        color: #555;
                    }
                    .tech-stack {
                        display: flex;
                        gap: 10px;
                        margin: 20px 0;
                        flex-wrap: wrap;
                    }
                    .tech-badge {
                        background: #667eea;
                        color: white;
                        padding: 8px 16px;
                        border-radius: 8px;
                        font-size: 0.9em;
                    }
                    .api-link {
                        display: inline-block;
                        background: #3b82f6;
                        color: white;
                        padding: 12px 24px;
                        border-radius: 8px;
                        text-decoration: none;
                        margin: 10px 10px 10px 0;
                        transition: all 0.3s;
                    }
                    .api-link:hover {
                        background: #2563eb;
                        transform: translateY(-2px);
                        box-shadow: 0 4px 12px rgba(59,130,246,0.4);
                    }
                    .footer {
                        margin-top: 30px;
                        padding-top: 20px;
                        border-top: 1px solid #e5e7eb;
                        color: #999;
                        font-size: 0.9em;
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>🎉 Qoder2</h1>
                    <div class="status">✅ 服务运行中</div>
                    
                    <div class="info-box">
                        <div class="info-item"><strong>📅 当前时间:</strong> """ + 
                        LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss")) + """
                        </div>
                        <div class="info-item"><strong>🖥️ 服务器:</strong> 远程部署</div>
                        <div class="info-item"><strong>📌 版本:</strong> v1.0.0</div>
                    </div>
                    
                    <div>
                        <strong>🛠️ 技术栈:</strong>
                        <div class="tech-stack">
                            <span class="tech-badge">☕ Java 17</span>
                            <span class="tech-badge">🐍 Python 3</span>
                            <span class="tech-badge">🔷 Go</span>
                        </div>
                    </div>
                    
                    <div style="margin-top: 30px;">
                        <strong>🔗 API接口:</strong><br>
                        <a href="/api/info" class="api-link">📊 系统信息</a>
                        <a href="/api/health" class="api-link">💚 健康检查</a>
                        <a href="/api/files" class="api-link">📁 文件列表</a>
                    </div>
                    
                    <div class="footer">
                        Powered by Qoder2 | Deployed on Remote Server
                    </div>
                </div>
            </body>
            </html>
            """;
        
        sendResponse(exchange, 200, html, "text/html; charset=UTF-8");
    }
    
    // 系统信息API
    private static void handleInfo(HttpExchange exchange) throws IOException {
        String json = String.format("""
            {
                "app": "Qoder2",
                "version": "1.0.0",
                "status": "running",
                "languages": ["Java", "Python", "Go"],
                "timestamp": "%s",
                "uptime": "%d seconds",
                "server": {
                    "java_version": "%s",
                    "os": "%s",
                    "arch": "%s"
                }
            }
            """,
            LocalDateTime.now().format(DateTimeFormatter.ISO_LOCAL_DATE_TIME),
            java.lang.management.ManagementFactory.getRuntimeMXBean().getUptime() / 1000,
            System.getProperty("java.version"),
            System.getProperty("os.name"),
            System.getProperty("os.arch")
        );
        
        sendResponse(exchange, 200, json, "application/json");
    }
    
    // 健康检查API
    private static void handleHealth(HttpExchange exchange) throws IOException {
        String json = """
            {
                "status": "healthy",
                "timestamp": """ + System.currentTimeMillis() + """
                
            }
            """;
        
        sendResponse(exchange, 200, json, "application/json");
    }
    
    // 文件列表API
    private static void handleFiles(HttpExchange exchange) throws IOException {
        try {
            StringBuilder fileList = new StringBuilder("[");
            Files.list(Paths.get("."))
                .filter(p -> !p.getFileName().toString().startsWith("."))
                .forEach(p -> {
                    if (fileList.length() > 1) fileList.append(",");
                    fileList.append("\"").append(p.getFileName().toString()).append("\"");
                });
            fileList.append("]");
            
            String json = "{\"files\":" + fileList + "}";
            sendResponse(exchange, 200, json, "application/json");
        } catch (Exception e) {
            sendResponse(exchange, 500, "{\"error\":\"" + e.getMessage() + "\"}", "application/json");
        }
    }
    
    // 发送响应
    private static void sendResponse(HttpExchange exchange, int code, String response, String contentType) throws IOException {
        exchange.getResponseHeaders().set("Content-Type", contentType);
        exchange.getResponseHeaders().set("Access-Control-Allow-Origin", "*");
        byte[] bytes = response.getBytes("UTF-8");
        exchange.sendResponseHeaders(code, bytes.length);
        OutputStream os = exchange.getResponseBody();
        os.write(bytes);
        os.close();
    }
}
JAVA

echo -e "${GREEN}✅ Web服务器代码已创建${NC}"

# ========== 步骤3: 编译Java文件 ==========
echo -e "${YELLOW}📋 步骤3: 编译Java文件...${NC}"

javac QoderWebServer.java
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Java编译成功${NC}"
else
    echo -e "${RED}❌ Java编译失败${NC}"
    exit 1
fi

# ========== 步骤4: 创建远程目录 ==========
echo -e "${YELLOW}📋 步骤4: 在服务器创建目录...${NC}"

ssh "$SERVER" "mkdir -p $REMOTE_PATH/backup" || {
    echo -e "${RED}❌ 无法连接到服务器或创建目录${NC}"
    exit 1
}

echo -e "${GREEN}✅ 远程目录已创建${NC}"

# ========== 步骤5: 备份旧版本 ==========
echo -e "${YELLOW}📋 步骤5: 备份旧版本...${NC}"

ssh "$SERVER" << BACKUP
if [ -f "$REMOTE_PATH/QoderWebServer.class" ]; then
    BACKUP_NAME="backup_\$(date +%Y%m%d_%H%M%S)"
    mkdir -p "$REMOTE_PATH/backup/\$BACKUP_NAME"
    cp -r $REMOTE_PATH/*.class $REMOTE_PATH/backup/\$BACKUP_NAME/ 2>/dev/null || true
    echo "✅ 已备份到: \$BACKUP_NAME"
fi
BACKUP

# ========== 步骤6: 传输文件 ==========
echo -e "${YELLOW}📋 步骤6: 上传文件到服务器...${NC}"

rsync -avz --progress \
    --exclude '.git' \
    --exclude '*.log' \
    --exclude 'node_modules' \
    "$LOCAL_PATH/" "$SERVER:$REMOTE_PATH/"

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ 文件上传成功${NC}"
else
    echo -e "${RED}❌ 文件上传失败${NC}"
    exit 1
fi

# ========== 步骤7: 部署并启动服务 ==========
echo -e "${YELLOW}📋 步骤7: 在服务器上启动服务...${NC}"

ssh "$SERVER" << 'DEPLOY'
cd /opt/apps/Qoder2

# 停止旧进程
echo "⏹️  停止旧进程..."
pkill -f QoderWebServer || true
sleep 2

# 启动新服务
echo "🚀 启动新服务..."
nohup java QoderWebServer > qoder-web.log 2>&1 &

# 等待启动
sleep 3

# 检查进程
if pgrep -f QoderWebServer > /dev/null; then
    echo "✅ 服务启动成功!"
    
    # 获取服务器IP
    SERVER_IP=$(curl -s ifconfig.me 2>/dev/null || hostname -I | awk '{print $1}')
    
    echo ""
    echo "========================================" 
    echo "🎉 Qoder2 部署成功!"
    echo "========================================"
    echo "🌐 访问地址: http://$SERVER_IP:8080"
    echo "📊 系统信息: http://$SERVER_IP:8080/api/info"
    echo "💚 健康检查: http://$SERVER_IP:8080/api/health"
    echo "📁 文件列表: http://$SERVER_IP:8080/api/files"
    echo ""
    echo "📋 管理命令:"
    echo "   查看日志: tail -f /opt/apps/Qoder2/qoder-web.log"
    echo "   停止服务: pkill -f QoderWebServer"
    echo "   重启服务: pkill -f QoderWebServer && nohup java QoderWebServer > qoder-web.log 2>&1 &"
    echo "========================================"
else
    echo "❌ 服务启动失败,查看日志:"
    tail -n 30 qoder-web.log
    exit 1
fi
DEPLOY

if [ $? -eq 0 ]; then
    echo ""
    echo -e "${GREEN}========================================${NC}"
    echo -e "${GREEN}🎉 部署完成!${NC}"
    echo -e "${GREEN}========================================${NC}"
    echo ""
    echo -e "💡 ${YELLOW}下一步操作:${NC}"
    echo "1. 在浏览器中访问服务器IP:8080"
    echo "2. 配置防火墙开放8080端口"
    echo "3. (可选) 配置域名和SSL证书"
else
    echo -e "${RED}❌ 部署失败${NC}"
    exit 1
fi
