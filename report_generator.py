#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
报告生成模块
提供数据可视化和报告生成功能
"""

try:
    import matplotlib.pyplot as plt
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    plt = None
    MATPLOTLIB_AVAILABLE = False

try:
    import numpy as np
    NUMPY_AVAILABLE = True
except ImportError:
    np = None
    NUMPY_AVAILABLE = False

from typing import List, Dict, Any


class ReportGenerator:
    """报告生成器类"""
    
    def __init__(self):
        """初始化报告生成器"""
        if MATPLOTLIB_AVAILABLE:
            plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
            plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号
    
    def generate_bar_chart(self, data: List[Dict[str, Any]], 
                          x_field: str, y_field: str, 
                          title: str = "柱状图", 
                          x_label: str = "X轴", 
                          y_label: str = "Y轴") -> bool:
        """
        生成柱状图
        
        Args:
            data (List[Dict[str, Any]]): 数据列表
            x_field (str): X轴字段名
            y_field (str): Y轴字段名
            title (str): 图表标题
            x_label (str): X轴标签
            y_label (str): Y轴标签
            
        Returns:
            bool: 生成成功返回True，否则返回False
        """
        if not MATPLOTLIB_AVAILABLE:
            print("错误: matplotlib库未安装，无法生成图表")
            return False
            
        try:
            x_values = [item[x_field] for item in data]
            y_values = [float(item[y_field]) for item in data]
            
            plt.figure(figsize=(10, 6))
            plt.bar(x_values, y_values)
            plt.title(title)
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig(f"{title}.png")
            plt.close()
            return True
        except Exception as e:
            print(f"生成柱状图时出错: {e}")
            return False
    
    def generate_pie_chart(self, data: List[Dict[str, Any]], 
                          label_field: str, value_field: str,
                          title: str = "饼图") -> bool:
        """
        生成饼图
        
        Args:
            data (List[Dict[str, Any]]): 数据列表
            label_field (str): 标签字段名
            value_field (str): 值字段名
            title (str): 图表标题
            
        Returns:
            bool: 生成成功返回True，否则返回False
        """
        if not MATPLOTLIB_AVAILABLE:
            print("错误: matplotlib库未安装，无法生成图表")
            return False
            
        try:
            labels = [item[label_field] for item in data]
            values = [float(item[value_field]) for item in data]
            
            plt.figure(figsize=(8, 8))
            plt.pie(values, labels=labels, autopct='%1.1f%%')
            plt.title(title)
            plt.axis('equal')
            plt.tight_layout()
            plt.savefig(f"{title}.png")
            plt.close()
            return True
        except Exception as e:
            print(f"生成饼图时出错: {e}")
            return False
    
    def generate_line_chart(self, data: List[Dict[str, Any]], 
                           x_field: str, y_field: str,
                           title: str = "折线图",
                           x_label: str = "X轴",
                           y_label: str = "Y轴") -> bool:
        """
        生成折线图
        
        Args:
            data (List[Dict[str, Any]]): 数据列表
            x_field (str): X轴字段名
            y_field (str): Y轴字段名
            title (str): 图表标题
            x_label (str): X轴标签
            y_label (str): Y轴标签
            
        Returns:
            bool: 生成成功返回True，否则返回False
        """
        if not MATPLOTLIB_AVAILABLE:
            print("错误: matplotlib库未安装，无法生成图表")
            return False
            
        try:
            x_values = [item[x_field] for item in data]
            y_values = [float(item[y_field]) for item in data]
            
            plt.figure(figsize=(10, 6))
            plt.plot(x_values, y_values, marker='o')
            plt.title(title)
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.xticks(rotation=45)
            plt.grid(True)
            plt.tight_layout()
            plt.savefig(f"{title}.png")
            plt.close()
            return True
        except Exception as e:
            print(f"生成折线图时出错: {e}")
            return False
    
    def generate_statistical_report(self, data: List[Dict[str, Any]], 
                                  field: str, report_title: str = "统计报告") -> str:
        """
        生成统计报告
        
        Args:
            data (List[Dict[str, Any]]): 数据列表
            field (str): 要统计的字段名
            report_title (str): 报告标题
            
        Returns:
            str: 生成的统计报告文本
        """
        if not NUMPY_AVAILABLE:
            # 如果numpy不可用，使用基本的Python函数进行计算
            try:
                values = [float(item[field]) for item in data]
                
                report = f"\n{report_title}\n"
                report += "=" * 50 + "\n"
                report += f"数据总数: {len(values)}\n"
                report += f"最大值: {max(values)}\n"
                report += f"最小值: {min(values)}\n"
                report += f"平均值: {sum(values) / len(values):.2f}\n"
                
                # 计算中位数
                sorted_values = sorted(values)
                n = len(sorted_values)
                if n % 2 == 0:
                    median = (sorted_values[n//2 - 1] + sorted_values[n//2]) / 2
                else:
                    median = sorted_values[n//2]
                report += f"中位数: {median:.2f}\n"
                
                # 计算标准差
                mean = sum(values) / len(values)
                variance = sum((x - mean) ** 2 for x in values) / len(values)
                std_dev = variance ** 0.5
                report += f"标准差: {std_dev:.2f}\n"
                
                return report
            except Exception as e:
                return f"生成统计报告时出错: {e}"
        else:
            # 使用numpy进行计算
            try:
                values = [float(item[field]) for item in data]
                
                report = f"\n{report_title}\n"
                report += "=" * 50 + "\n"
                report += f"数据总数: {len(values)}\n"
                report += f"最大值: {max(values)}\n"
                report += f"最小值: {min(values)}\n"
                report += f"平均值: {np.mean(values):.2f}\n"
                report += f"中位数: {np.median(values):.2f}\n"
                report += f"标准差: {np.std(values):.2f}\n"
                
                return report
            except Exception as e:
                return f"生成统计报告时出错: {e}"


def main():
    """主函数，用于演示ReportGenerator的使用"""
    generator = ReportGenerator()
    
    # 示例数据
    sample_data = [
        {"月份": "1月", "销售额": "10000"},
        {"月份": "2月", "销售额": "15000"},
        {"月份": "3月", "销售额": "12000"},
        {"月份": "4月", "销售额": "18000"},
        {"月份": "5月", "销售额": "13000"}
    ]
    
    if MATPLOTLIB_AVAILABLE:
        # 生成柱状图
        generator.generate_bar_chart(
            sample_data, 
            "月份", 
            "销售额", 
            "月度销售柱状图", 
            "月份", 
            "销售额"
        )
        
        # 生成饼图
        generator.generate_pie_chart(
            sample_data, 
            "月份", 
            "销售额", 
            "月度销售饼图"
        )
        
        # 生成折线图
        generator.generate_line_chart(
            sample_data, 
            "月份", 
            "销售额", 
            "月度销售趋势图", 
            "月份", 
            "销售额"
        )
    
    # 生成统计报告
    report = generator.generate_statistical_report(sample_data, "销售额", "销售统计报告")
    print(report)
    
    if MATPLOTLIB_AVAILABLE:
        print("报告和图表已生成完成！")
    else:
        print("报告已生成完成！(图表生成功能需要安装matplotlib库)")


if __name__ == "__main__":
    main()