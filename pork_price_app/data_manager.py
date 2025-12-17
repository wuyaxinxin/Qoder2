# 始终生效

import json
import os
from datetime import datetime, timedelta
import random
import math


def generate_mock_data():
    """
    生成模拟的英伟达芯片销量数据(2023-01-01至2024-12-31)
    
    返回:
        dict: 包含metadata和data的字典
    """
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2024, 12, 31)
    
    data_points = []
    current_date = start_date
    
    # 芯片型号：NVIDIA A100 80GB GPU
    base_sales = 15000  # 基础日销量（台）
    
    while current_date <= end_date:
        day_of_year = current_date.timetuple().tm_yday
        days_since_start = (current_date - start_date).days
        
        # 趋势因素：AI热潮推动增长（+30%年增长率）
        growth_factor = (days_since_start / 365) * 0.3 * base_sales
        
        # 季节性因素：Q4财年末采购高峰
        seasonal_factor = 3000 * math.sin(2 * math.pi * (day_of_year - 274) / 365)
        # 274对应10月1日，Q4开始
        
        # 周期性因素：新品发布周期影响
        cycle_factor = 2000 * math.sin(2 * math.pi * day_of_year / 180)
        
        # 随机波动：供应链和市场波动
        random_noise = random.gauss(0, 800)
        
        sales = base_sales + growth_factor + seasonal_factor + cycle_factor + random_noise
        sales = max(8000, min(25000, sales))  # 销量范围：8000-25000台/日
        sales = int(round(sales))  # 销量为整数
        
        data_points.append({
            "date": current_date.strftime("%Y-%m-%d"),
            "sales": sales
        })
        
        current_date += timedelta(days=1)
    
    result = {
        "metadata": {
            "source": "模拟数据",
            "unit": "台/日",
            "chip_model": "NVIDIA A100 80GB GPU",
            "description": "全球NVIDIA A100芯片日销量"
        },
        "data": data_points
    }
    
    return result


def save_data_to_json(data, file_path):
    """
    将数据保存为JSON文件
    
    参数:
        data (dict): 要保存的数据
        file_path (str): 保存路径
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_data():
    """
    从JSON文件加载数据
    
    返回:
        dict: 包含销量数据的字典,如果文件不存在则生成新数据
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_file = os.path.join(current_dir, 'data', 'nvidia_chip_sales.json')
    
    try:
        with open(data_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        data = generate_mock_data()
        save_data_to_json(data, data_file)
        return data


def validate_data(data):
    """
    验证数据完整性和格式
    
    参数:
        data (dict): 要验证的数据
        
    返回:
        bool: 数据是否有效
    """
    if not isinstance(data, dict):
        return False
    
    if 'metadata' not in data or 'data' not in data:
        return False
    
    if not isinstance(data['data'], list):
        return False
    
    for item in data['data']:
        if 'date' not in item or 'sales' not in item:
            return False
        if not isinstance(item['sales'], int):
            return False
    
    return True


if __name__ == '__main__':
    data = generate_mock_data()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'data', 'nvidia_chip_sales.json')
    save_data_to_json(data, file_path)
    print(f"数据已生成并保存到: {file_path}")
    print(f"数据点数量: {len(data['data'])}")