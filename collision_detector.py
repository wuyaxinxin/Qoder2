始终生效

"""
吃鱼小游戏 - 碰撞检测系统
"""

import math


class CollisionDetector:
    """碰撞检测器"""
    
    def __init__(self):
        self.collision_occurred = False
        self.game_over = False
    
    def check_collision(self, player, npc_fish):
        """
        检测玩家鱼与NPC鱼的碰撞
        返回: (collision, can_eat)
        - collision: 是否发生碰撞
        - can_eat: 玩家是否能吃掉NPC鱼（True）还是被吃（False）
        """
        # 计算两鱼之间的距离
        distance = math.sqrt((player.x - npc_fish.x) ** 2 + (player.y - npc_fish.y) ** 2)
        
        # 碰撞判定：距离小于两鱼半径之和
        collision_distance = player.size + npc_fish.size
        
        if distance < collision_distance * 0.8:  # 使用0.8系数使碰撞更精确
            # 发生碰撞
            if player.size > npc_fish.size:
                # 玩家可以吃掉NPC鱼
                return True, True
            else:
                # 玩家被吃掉，游戏结束
                return True, False
        
        return False, False
    
    def check_all_collisions(self, player, npc_manager):
        """
        检测玩家与所有NPC鱼的碰撞
        返回: (eaten_fishes, game_over)
        - eaten_fishes: 被吃掉的鱼列表
        - game_over: 游戏是否结束
        """
        eaten_fishes = []
        
        for npc_fish in npc_manager.fishes:
            collision, can_eat = self.check_collision(player, npc_fish)
            
            if collision:
                if can_eat:
                    # 玩家吃掉NPC鱼
                    eaten_fishes.append(npc_fish)
                else:
                    # 玩家被吃，游戏结束
                    return eaten_fishes, True
        
        return eaten_fishes, False
