始终生效

"""
吃鱼小游戏 - 计分系统
"""

import os
import json
from fish_game_config import *


class ScoreSystem:
    """计分系统"""
    
    def __init__(self):
        self.current_score = 0
        self.high_score = 0
        self.fishes_eaten = 0
        self.score_file = "fish_game_highscore.json"
        self.load_high_score()
    
    def load_high_score(self):
        """从文件加载最高分"""
        try:
            if os.path.exists(self.score_file):
                with open(self.score_file, 'r') as f:
                    data = json.load(f)
                    self.high_score = data.get('high_score', 0)
        except Exception as e:
            print(f"加载最高分失败: {e}")
            self.high_score = 0
    
    def save_high_score(self):
        """保存最高分到文件"""
        try:
            with open(self.score_file, 'w') as f:
                json.dump({'high_score': self.high_score}, f)
        except Exception as e:
            print(f"保存最高分失败: {e}")
    
    def add_score(self, eaten_fish_size, player_level):
        """
        添加分数
        基础分数 = 被吃鱼的体型 × 分数倍数
        附加分数 = 玩家当前等级 × 5
        """
        base_score = int(eaten_fish_size * SCORE_MULTIPLIER)
        bonus_score = player_level * 5
        total_score = base_score + bonus_score
        
        self.current_score += total_score
        self.fishes_eaten += 1
        
        # 更新最高分
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            self.save_high_score()
        
        return total_score
    
    def reset(self):
        """重置当前分数"""
        self.current_score = 0
        self.fishes_eaten = 0
    
    def get_current_score(self):
        """获取当前分数"""
        return self.current_score
    
    def get_high_score(self):
        """获取最高分"""
        return self.high_score
    
    def get_fishes_eaten(self):
        """获取吃掉的鱼数量"""
        return self.fishes_eaten
