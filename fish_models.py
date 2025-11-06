始终生效

"""
吃鱼小游戏 - 鱼类模型
定义玩家鱼和NPC鱼的类
"""

import random
import math
from fish_game_config import *


class Fish:
    """鱼类基础模型"""
    
    def __init__(self, x, y, size, speed, color, is_player=False):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.color = color
        self.is_player = is_player
        
        # 随机移动方向（仅NPC鱼使用）
        if not is_player:
            angle = random.uniform(0, 2 * math.pi)
            self.direction_x = math.cos(angle)
            self.direction_y = math.sin(angle)
        else:
            self.direction_x = 0
            self.direction_y = 0
    
    def move(self, dx=None, dy=None):
        """移动鱼"""
        if dx is not None and dy is not None:
            # 玩家控制的移动
            self.x += dx * self.speed
            self.y += dy * self.speed
        else:
            # NPC自动移动
            self.x += self.direction_x * self.speed
            self.y += self.direction_y * self.speed
    
    def check_boundary(self):
        """边界检测"""
        # 玩家鱼：限制在窗口内
        if self.is_player:
            if self.x - self.size < 0:
                self.x = self.size
            elif self.x + self.size > WINDOW_WIDTH:
                self.x = WINDOW_WIDTH - self.size
            
            if self.y - self.size < 0:
                self.y = self.size
            elif self.y + self.size > WINDOW_HEIGHT:
                self.y = WINDOW_HEIGHT - self.size
        else:
            # NPC鱼：触碰边界后反弹
            if self.x - self.size < 0 or self.x + self.size > WINDOW_WIDTH:
                self.direction_x *= -1
                self.x = max(self.size, min(self.x, WINDOW_WIDTH - self.size))
            
            if self.y - self.size < 0 or self.y + self.size > WINDOW_HEIGHT:
                self.direction_y *= -1
                self.y = max(self.size, min(self.y, WINDOW_HEIGHT - self.size))
    
    def grow(self, eaten_fish_size):
        """鱼吃掉其他鱼后成长"""
        # 动态增长：基于被吃鱼的大小
        growth = eaten_fish_size * 0.2
        self.size += growth
        
        # 限制最大体型
        if self.size > MAX_PLAYER_SIZE:
            self.size = MAX_PLAYER_SIZE
        
        # 体型增大，速度相应降低
        if self.is_player:
            self.speed = PLAYER_INITIAL_SPEED * (PLAYER_INITIAL_SIZE / self.size) ** 0.3
    
    def get_level(self):
        """获取等级（基于体型）"""
        if self.is_player:
            return int(self.size / PLAYER_INITIAL_SIZE)
        return 0


class NPCFishManager:
    """NPC鱼管理器"""
    
    def __init__(self, player):
        self.player = player
        self.fishes = []
        self.spawn_initial_fishes()
    
    def spawn_initial_fishes(self):
        """生成初始NPC鱼"""
        for _ in range(NPC_COUNT):
            self.spawn_fish()
    
    def spawn_fish(self):
        """生成单条NPC鱼"""
        # 随机位置（避开玩家附近）
        while True:
            x = random.randint(50, WINDOW_WIDTH - 50)
            y = random.randint(50, WINDOW_HEIGHT - 50)
            
            # 确保不在玩家附近生成
            distance = math.sqrt((x - self.player.x) ** 2 + (y - self.player.y) ** 2)
            if distance > 150:
                break
        
        # 随机大小和速度
        size = random.randint(NPC_MIN_SIZE, NPC_MAX_SIZE)
        speed = random.uniform(NPC_MIN_SPEED, NPC_MAX_SPEED)
        
        # 根据大小设置颜色
        if size < self.player.size * 0.8:
            color = COLOR_NPC_SMALL
        elif size < self.player.size * 1.2:
            color = COLOR_NPC_MEDIUM
        else:
            color = COLOR_NPC_LARGE
        
        fish = Fish(x, y, size, speed, color, is_player=False)
        self.fishes.append(fish)
    
    def update(self):
        """更新所有NPC鱼"""
        for fish in self.fishes:
            fish.move()
            fish.check_boundary()
            
            # 根据玩家体型动态更新NPC颜色
            if fish.size < self.player.size * 0.8:
                fish.color = COLOR_NPC_SMALL
            elif fish.size < self.player.size * 1.2:
                fish.color = COLOR_NPC_MEDIUM
            else:
                fish.color = COLOR_NPC_LARGE
    
    def remove_fish(self, fish):
        """移除鱼并生成新的"""
        if fish in self.fishes:
            self.fishes.remove(fish)
            self.spawn_fish()
    
    def adjust_difficulty(self):
        """根据玩家体型调整难度"""
        player_size = self.player.size
        
        # 根据玩家体型调整NPC数量
        if player_size < 25:
            target_count = 10
        elif player_size < 35:
            target_count = 12
        elif player_size < 50:
            target_count = 14
        else:
            target_count = 16
        
        # 调整NPC数量
        while len(self.fishes) < target_count:
            self.spawn_fish()
