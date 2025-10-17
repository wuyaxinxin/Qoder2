"""
始终生效
工具调用失败场景演示脚本

本脚本演示各种工具调用失败的场景，包括：
1. 文件操作失败（不存在的文件、权限问题等）
2. 网络请求失败（超时、404、认证失败等）
3. API调用失败（参数错误、资源不存在等）
4. 数据解析失败（格式错误、类型不匹配等）
5. 系统资源失败（内存不足、磁盘空间不足等）
"""

import json
import os
import time
from datetime import datetime
from typing import Dict, List, Any


class ToolFailureDemo:
    """工具调用失败场景演示类"""
    
    def __init__(self):
        self.results = []
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def log_failure(self, category: str, scenario: str, error_type: str, 
                    error_message: str, details: Dict[str, Any] = None):
        """记录失败场景"""
        failure_record = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "category": category,
            "scenario": scenario,
            "error_type": error_type,
            "error_message": error_message,
            "details": details or {}
        }
        self.results.append(failure_record)
        print(f"\n{'='*80}")
        print(f"📋 场景类别: {category}")
        print(f"🔍 失败场景: {scenario}")
        print(f"❌ 错误类型: {error_type}")
        print(f"💬 错误信息: {error_message}")
        if details:
            print(f"📊 详细信息: {json.dumps(details, indent=2, ensure_ascii=False)}")
        print(f"{'='*80}")
    
    def demo_file_operation_failures(self):
        """演示文件操作失败场景"""
        print("\n" + "="*80)
        print("📁 第一部分：文件操作失败场景")
        print("="*80)
        
        # 场景1: 读取不存在的文件
        try:
            with open("/nonexistent/path/file.txt", "r") as f:
                content = f.read()
        except FileNotFoundError as e:
            self.log_failure(
                category="文件操作",
                scenario="读取不存在的文件",
                error_type="FileNotFoundError",
                error_message=str(e),
                details={
                    "attempted_path": "/nonexistent/path/file.txt",
                    "operation": "read",
                    "suggestion": "检查文件路径是否正确，文件是否存在"
                }
            )
        
        # 场景2: 权限不足
        try:
            # 模拟权限问题
            restricted_path = "/root/restricted_file.txt"
            with open(restricted_path, "w") as f:
                f.write("test")
        except PermissionError as e:
            self.log_failure(
                category="文件操作",
                scenario="权限不足无法写入文件",
                error_type="PermissionError",
                error_message=str(e),
                details={
                    "attempted_path": restricted_path,
                    "operation": "write",
                    "suggestion": "检查文件权限或使用有权限的路径"
                }
            )
        except Exception as e:
            # 在某些系统上可能是其他错误
            self.log_failure(
                category="文件操作",
                scenario="权限不足无法写入文件",
                error_type=type(e).__name__,
                error_message=str(e),
                details={
                    "attempted_path": restricted_path,
                    "operation": "write"
                }
            )
        
        # 场景3: 磁盘空间不足（模拟）
        self.log_failure(
            category="文件操作",
            scenario="磁盘空间不足",
            error_type="OSError",
            error_message="[Errno 28] No space left on device",
            details={
                "operation": "write",
                "file_size": "10GB",
                "available_space": "100MB",
                "suggestion": "清理磁盘空间或使用其他存储位置"
            }
        )
        
        # 场景4: 文件已被占用
        self.log_failure(
            category="文件操作",
            scenario="文件被其他进程占用",
            error_type="PermissionError",
            error_message="[Errno 13] Permission denied: file is being used by another process",
            details={
                "file_path": "data/locked_file.db",
                "operation": "delete",
                "suggestion": "关闭占用文件的进程或等待其释放"
            }
        )
    
    def demo_network_failures(self):
        """演示网络请求失败场景"""
        print("\n" + "="*80)
        print("🌐 第二部分:网络请求失败场景")
        print("="*80)
        
        # 场景1: 连接超时
        self.log_failure(
            category="网络请求",
            scenario="连接超时",
            error_type="TimeoutError",
            error_message="Connection timed out after 30 seconds",
            details={
                "url": "https://api.example.com/slow-endpoint",
                "timeout": 30,
                "method": "GET",
                "suggestion": "增加超时时间或检查网络连接"
            }
        )
        
        # 场景2: 404 资源不存在
        self.log_failure(
            category="网络请求",
            scenario="资源不存在",
            error_type="HTTPError",
            error_message="404 Not Found: The requested resource does not exist",
            details={
                "url": "https://api.github.com/repos/nonexistent/repo",
                "status_code": 404,
                "method": "GET",
                "suggestion": "检查URL是否正确，资源是否存在"
            }
        )
        
        # 场景3: 401 认证失败
        self.log_failure(
            category="网络请求",
            scenario="认证失败",
            error_type="AuthenticationError",
            error_message="401 Unauthorized: Invalid or missing authentication token",
            details={
                "url": "https://api.github.com/user/repos",
                "status_code": 401,
                "auth_type": "Bearer Token",
                "suggestion": "检查认证凭据是否正确或是否已过期"
            }
        )
        
        # 场景4: 403 权限不足
        self.log_failure(
            category="网络请求",
            scenario="权限不足",
            error_type="ForbiddenError",
            error_message="403 Forbidden: You don't have permission to access this resource",
            details={
                "url": "https://api.github.com/repos/private/repo",
                "status_code": 403,
                "required_permission": "repo:read",
                "suggestion": "检查账户权限或申请必要的访问权限"
            }
        )
        
        # 场景5: 429 请求频率限制
        self.log_failure(
            category="网络请求",
            scenario="请求频率超限",
            error_type="RateLimitError",
            error_message="429 Too Many Requests: API rate limit exceeded",
            details={
                "url": "https://api.github.com/search/repositories",
                "status_code": 429,
                "rate_limit": "60 requests/hour",
                "retry_after": "3600 seconds",
                "suggestion": "等待限制重置或使用认证以获取更高限额"
            }
        )
        
        # 场景6: 500 服务器内部错误
        self.log_failure(
            category="网络请求",
            scenario="服务器内部错误",
            error_type="InternalServerError",
            error_message="500 Internal Server Error: The server encountered an error",
            details={
                "url": "https://api.example.com/endpoint",
                "status_code": 500,
                "suggestion": "稍后重试或联系服务提供商"
            }
        )
        
        # 场景7: 503 服务不可用
        self.log_failure(
            category="网络请求",
            scenario="服务暂时不可用",
            error_type="ServiceUnavailableError",
            error_message="503 Service Unavailable: The service is temporarily unavailable",
            details={
                "url": "https://api.example.com/endpoint",
                "status_code": 503,
                "retry_after": "300 seconds",
                "suggestion": "服务维护中，请稍后重试"
            }
        )
        
        # 场景8: DNS解析失败
        self.log_failure(
            category="网络请求",
            scenario="DNS解析失败",
            error_type="DNSError",
            error_message="Failed to resolve hostname: nonexistent-domain.com",
            details={
                "hostname": "nonexistent-domain.com",
                "dns_server": "8.8.8.8",
                "suggestion": "检查域名是否正确或DNS服务器设置"
            }
        )
    
    def demo_api_call_failures(self):
        """演示API调用失败场景"""
        print("\n" + "="*80)
        print("🔌 第三部分：API调用失败场景")
        print("="*80)
        
        # 场景1: 缺少必需参数
        self.log_failure(
            category="API调用",
            scenario="缺少必需参数",
            error_type="ValidationError",
            error_message="Missing required parameter: 'organizationId'",
            details={
                "api": "mcp_yunxiao_create_pipeline",
                "missing_params": ["organizationId"],
                "provided_params": ["name", "buildLanguage"],
                "suggestion": "补充所有必需参数"
            }
        )
        
        # 场景2: 参数类型错误
        self.log_failure(
            category="API调用",
            scenario="参数类型错误",
            error_type="TypeError",
            error_message="Parameter 'page' must be an integer, got string",
            details={
                "api": "mcp_yunxiao_list_pipelines",
                "parameter": "page",
                "expected_type": "integer",
                "actual_type": "string",
                "actual_value": "first_page",
                "suggestion": "确保参数类型正确"
            }
        )
        
        # 场景3: 参数值超出范围
        self.log_failure(
            category="API调用",
            scenario="参数值超出范围",
            error_type="ValueError",
            error_message="Parameter 'perPage' must be between 1 and 100, got 500",
            details={
                "api": "mcp_yunxiao_list_pipelines",
                "parameter": "perPage",
                "min_value": 1,
                "max_value": 100,
                "actual_value": 500,
                "suggestion": "调整参数值在有效范围内"
            }
        )
        
        # 场景4: 资源不存在
        self.log_failure(
            category="API调用",
            scenario="资源不存在",
            error_type="ResourceNotFoundError",
            error_message="Pipeline with ID 'nonexistent-pipeline-id' not found",
            details={
                "api": "mcp_yunxiao_get_pipeline",
                "resource_type": "Pipeline",
                "resource_id": "nonexistent-pipeline-id",
                "suggestion": "检查资源ID是否正确"
            }
        )
        
        # 场景5: 资源已存在冲突
        self.log_failure(
            category="API调用",
            scenario="资源已存在",
            error_type="ConflictError",
            error_message="Pipeline with name 'my-pipeline' already exists",
            details={
                "api": "mcp_yunxiao_create_pipeline",
                "resource_type": "Pipeline",
                "conflict_field": "name",
                "conflict_value": "my-pipeline",
                "suggestion": "使用不同的名称或更新现有资源"
            }
        )
        
        # 场景6: 依赖资源缺失
        self.log_failure(
            category="API调用",
            scenario="依赖资源缺失",
            error_type="DependencyError",
            error_message="Service connection not found: required for pipeline creation",
            details={
                "api": "mcp_yunxiao_create_pipeline",
                "missing_dependency": "serviceConnection",
                "dependency_id": "sc-123456",
                "suggestion": "先创建依赖资源或使用存在的资源ID"
            }
        )
    
    def demo_data_parsing_failures(self):
        """演示数据解析失败场景"""
        print("\n" + "="*80)
        print("📊 第四部分：数据解析失败场景")
        print("="*80)
        
        # 场景1: JSON解析错误
        try:
            invalid_json = '{"name": "test", "value": }'
            json.loads(invalid_json)
        except json.JSONDecodeError as e:
            self.log_failure(
                category="数据解析",
                scenario="JSON格式错误",
                error_type="JSONDecodeError",
                error_message=str(e),
                details={
                    "data": invalid_json,
                    "position": e.pos,
                    "suggestion": "检查JSON格式是否正确"
                }
            )
        
        # 场景2: 数据类型不匹配
        self.log_failure(
            category="数据解析",
            scenario="数据类型不匹配",
            error_type="TypeError",
            error_message="Expected dict, got list",
            details={
                "expected_type": "dict",
                "actual_type": "list",
                "field": "response.data",
                "suggestion": "检查API返回数据结构"
            }
        )
        
        # 场景3: 缺少必需字段
        self.log_failure(
            category="数据解析",
            scenario="缺少必需字段",
            error_type="KeyError",
            error_message="Required field 'id' not found in response",
            details={
                "missing_fields": ["id"],
                "available_fields": ["name", "status", "created_at"],
                "suggestion": "检查数据结构或API版本"
            }
        )
        
        # 场景4: 编码错误
        self.log_failure(
            category="数据解析",
            scenario="字符编码错误",
            error_type="UnicodeDecodeError",
            error_message="'utf-8' codec can't decode byte 0xff in position 0",
            details={
                "encoding": "utf-8",
                "position": 0,
                "suggestion": "尝试其他编码方式(如gbk, latin1)"
            }
        )
    
    def demo_system_resource_failures(self):
        """演示系统资源失败场景"""
        print("\n" + "="*80)
        print("💾 第五部分：系统资源失败场景")
        print("="*80)
        
        # 场景1: 内存不足
        self.log_failure(
            category="系统资源",
            scenario="内存不足",
            error_type="MemoryError",
            error_message="Cannot allocate memory: insufficient system memory",
            details={
                "requested_memory": "8GB",
                "available_memory": "500MB",
                "operation": "large file processing",
                "suggestion": "减少内存使用或增加系统内存"
            }
        )
        
        # 场景2: 进程/线程数限制
        self.log_failure(
            category="系统资源",
            scenario="进程数超限",
            error_type="OSError",
            error_message="[Errno 24] Too many open files",
            details={
                "max_files": 1024,
                "current_files": 1024,
                "suggestion": "关闭未使用的文件句柄或增加系统限制"
            }
        )
        
        # 场景3: 环境变量缺失
        self.log_failure(
            category="系统资源",
            scenario="环境变量未设置",
            error_type="EnvironmentError",
            error_message="Required environment variable 'API_TOKEN' not set",
            details={
                "variable_name": "API_TOKEN",
                "required_by": "GitHub API client",
                "suggestion": "设置必需的环境变量"
            }
        )
    
    def demo_mcp_tool_failures(self):
        """演示MCP工具特定失败场景"""
        print("\n" + "="*80)
        print("🔧 第六部分：MCP工具特定失败场景")
        print("="*80)
        
        # 场景1: GitHub工具认证失败
        self.log_failure(
            category="MCP工具",
            scenario="GitHub MCP工具认证失败",
            error_type="AuthenticationError",
            error_message="GitHub API authentication failed: token invalid or expired",
            details={
                "tool": "mcp_github_get_file_contents",
                "status_code": 401,
                "fallback_tools": ["mcp_fetch_fetch_markdown", "本地实现"],
                "suggestion": "配置有效的GitHub Personal Access Token"
            }
        )
        
        # 场景2: 云效工具组织ID无效
        self.log_failure(
            category="MCP工具",
            scenario="云效组织ID无效",
            error_type="InvalidParameterError",
            error_message="Invalid organizationId: organization not found or access denied",
            details={
                "tool": "mcp_yunxiao_list_pipelines",
                "parameter": "organizationId",
                "provided_value": "invalid-org-id",
                "suggestion": "使用mcp_yunxiao_get_current_organization_info获取正确的组织ID"
            }
        )
        
        # 场景3: MCP工具超时
        self.log_failure(
            category="MCP工具",
            scenario="MCP工具调用超时",
            error_type="TimeoutError",
            error_message="MCP tool execution timeout after 60 seconds",
            details={
                "tool": "mcp_playwright_browser_navigate",
                "timeout": 60,
                "suggestion": "增加超时时间或使用降级方案"
            }
        )
        
        # 场景4: 浏览器工具未安装
        self.log_failure(
            category="MCP工具",
            scenario="浏览器未安装",
            error_type="BrowserNotInstalledError",
            error_message="Playwright browser not installed: chromium",
            details={
                "tool": "mcp_playwright_browser_snapshot",
                "missing_browser": "chromium",
                "suggestion": "运行 mcp_playwright_browser_install 安装浏览器"
            }
        )
    
    def demo_workflow_failures(self):
        """演示工作流失败场景"""
        print("\n" + "="*80)
        print("🔄 第七部分：工作流失败场景")
        print("="*80)
        
        # 场景1: 依赖调用链断裂
        self.log_failure(
            category="工作流",
            scenario="依赖调用链断裂",
            error_type="WorkflowError",
            error_message="Workflow failed: step 3 depends on step 2 which failed",
            details={
                "workflow": "create_and_deploy_pipeline",
                "failed_step": "step_2_get_service_connection",
                "blocked_steps": ["step_3_create_pipeline", "step_4_run_pipeline"],
                "suggestion": "修复失败步骤或跳过依赖步骤"
            }
        )
        
        # 场景2: 并行调用冲突
        self.log_failure(
            category="工作流",
            scenario="并行调用资源冲突",
            error_type="ConcurrencyError",
            error_message="Concurrent file modifications detected: conflict",
            details={
                "conflicting_operations": [
                    "edit_file: config.json",
                    "edit_file: config.json"
                ],
                "suggestion": "文件编辑操作必须顺序执行"
            }
        )
        
        # 场景3: 事务回滚失败
        self.log_failure(
            category="工作流",
            scenario="事务回滚失败",
            error_type="RollbackError",
            error_message="Failed to rollback changes: some operations are irreversible",
            details={
                "completed_operations": [
                    "create_pipeline",
                    "create_service_connection",
                    "delete_old_pipeline"
                ],
                "rollback_failed": "delete_old_pipeline (irreversible)",
                "suggestion": "手动恢复或使用备份"
            }
        )
    
    def save_results(self):
        """保存演示结果"""
        output_file = f"tool_failure_demo_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        summary = {
            "demo_info": {
                "title": "工具调用失败场景演示",
                "timestamp": self.timestamp,
                "total_scenarios": len(self.results)
            },
            "categories": {},
            "failures": self.results
        }
        
        # 统计各类别数量
        for result in self.results:
            category = result["category"]
            if category not in summary["categories"]:
                summary["categories"][category] = 0
            summary["categories"][category] += 1
        
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)
        
        print("\n" + "="*80)
        print(f"📝 演示结果已保存到: {output_file}")
        print(f"📊 总计演示场景: {len(self.results)} 个")
        print(f"📁 场景分类统计:")
        for category, count in summary["categories"].items():
            print(f"   - {category}: {count} 个场景")
        print("="*80)
        
        return output_file
    
    def run_all_demos(self):
        """运行所有演示"""
        print("\n" + "🎬 " * 20)
        print("工具调用失败场景演示开始")
        print(f"演示时间: {self.timestamp}")
        print("🎬 " * 20)
        
        self.demo_file_operation_failures()
        self.demo_network_failures()
        self.demo_api_call_failures()
        self.demo_data_parsing_failures()
        self.demo_system_resource_failures()
        self.demo_mcp_tool_failures()
        self.demo_workflow_failures()
        
        output_file = self.save_results()
        
        print("\n" + "✅ " * 20)
        print("所有失败场景演示完成!")
        print("✅ " * 20)
        
        return output_file


def main():
    """主函数"""
    demo = ToolFailureDemo()
    output_file = demo.run_all_demos()
    
    print(f"\n💡 提示: 查看详细结果请打开文件: {output_file}")
    print("💡 所有场景均为模拟演示，未实际执行可能造成破坏的操作")


if __name__ == "__main__":
    main()
