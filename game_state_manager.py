始终生效

"""
吃鱼小游戏 - 游戏状态管理器
"""

from fish_game_config import *
import time


class GameStateManager:
    """游戏状态管理器"""
    
    def __init__(self):
        self.current_state = STATE_MENU
        self.game_time = 0
        self.start_time = 0
    
    def set_state(self, new_state):
        """设置游戏状态"""
        self.current_state = new_state
        
        # 当进入游戏状态时，记录开始时间
        if new_state == STATE_PLAYING:
            self.start_time = time.time()
    
    def get_state(self):
        """获取当前游戏状态"""
        return self.current_state
    
    def is_menu(self):
        """是否在主菜单"""
        return self.current_state == STATE_MENU
    
    def is_playing(self):
        """是否在游戏中"""
        return self.current_state == STATE_PLAYING
    
    def is_paused(self):
        """是否暂停"""
        return self.current_state == STATE_PAUSED
    
    def is_game_over(self):
        """是否游戏结束"""
        return self.current_state == STATE_GAME_OVER
    
    def update_game_time(self):
        """更新游戏时间"""
        if self.current_state == STATE_PLAYING:
            self.game_time = time.time() - self.start_time
    
    def get_game_time(self):
        """获取游戏时间（秒）"""
        return self.game_time
    
    def get_formatted_time(self):
        """获取格式化的游戏时间（分:秒）"""
        minutes = int(self.game_time // 60)
        seconds = int(self.game_time % 60)
        return f"{minutes:02d}:{seconds:02d}"
    
    def reset_game_time(self):
        """重置游戏时间"""
        self.game_time = 0
        self.start_time = time.time()
