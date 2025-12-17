# 始终生效

import json
import os
from datetime import datetime, timedelta
import random
import math


def generate_mock_data():
    """
    生成模拟的猪肉价格数据(2023-01-01至2024-12-31)
    
    返回:
        dict: 包含metadata和data的字典
    """
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2024, 12, 31)
    
    data_points = []
    current_date = start_date
    
    base_price = 22.0
    
    while current_date <= end_date:
        day_of_year = current_date.timetuple().tm_yday
        
        seasonal_factor = 2.5 * math.sin(2 * math.pi * (day_of_year - 30) / 365)
        
        cycle_factor = 1.5 * math.sin(2 * math.pi * day_of_year / 730)
        
        random_noise = random.gauss(0, 0.5)
        
        price = base_price + seasonal_factor + cycle_factor + random_noise
        price = max(18.0, min(28.0, price))
        price = round(price, 2)
        
        data_points.append({
            "date": current_date.strftime("%Y-%m-%d"),
            "price": price
        })
        
        current_date += timedelta(days=1)
    
    result = {
        "metadata": {
            "source": "模拟数据",
            "unit": "元/公斤",
            "description": "全国猪肉平均批发价格"
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
        dict: 包含价格数据的字典,如果文件不存在则生成新数据
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_file = os.path.join(current_dir, 'data', 'pork_prices.json')
    
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
        if 'date' not in item or 'price' not in item:
            return False
        if not isinstance(item['price'], (int, float)):
            return False
    
    return True


if __name__ == '__main__':
    data = generate_mock_data()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'data', 'pork_prices.json')
    save_data_to_json(data, file_path)
    print(f"数据已生成并保存到: {file_path}")
    print(f"数据点数量: {len(data['data'])}")
