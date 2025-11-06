始终生效

"""
吃鱼小游戏 - 主程序
游戏主控制器和主循环
"""

import pygame
import sys
from fish_game_config import *
from fish_models import Fish, NPCFishManager
from collision_detector import CollisionDetector
from game_state_manager import GameStateManager
from score_system import ScoreSystem
from renderer import Renderer


class FishGame:
    """吃鱼小游戏主控制器"""
    
    def __init__(self):
        # 初始化Pygame
        pygame.init()
        
        # 创建游戏窗口
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("吃鱼小游戏")
        
        # 创建时钟控制帧率
        self.clock = pygame.time.Clock()
        
        # 初始化各个系统
        self.state_manager = GameStateManager()
        self.score_system = ScoreSystem()
        self.collision_detector = CollisionDetector()
        self.renderer = Renderer(self.screen)
        
        # 游戏对象（将在开始游戏时初始化）
        self.player = None
        self.npc_manager = None
        
        # 输入控制
        self.keys_pressed = set()
    
    def init_game(self):
        """初始化游戏场景"""
        # 创建玩家鱼
        self.player = Fish(
            x=WINDOW_WIDTH // 2,
            y=WINDOW_HEIGHT // 2,
            size=PLAYER_INITIAL_SIZE,
            speed=PLAYER_INITIAL_SPEED,
            color=COLOR_PLAYER,
            is_player=True
        )
        
        # 创建NPC鱼管理器
        self.npc_manager = NPCFishManager(self.player)
        
        # 重置分数和时间
        self.score_system.reset()
        self.state_manager.reset_game_time()
        
        # 设置游戏状态为进行中
        self.state_manager.set_state(STATE_PLAYING)
    
    def handle_events(self):
        """处理输入事件"""
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # ESC键切换暂停状态
                    if self.state_manager.is_playing():
                        self.state_manager.set_state(STATE_PAUSED)
                    elif self.state_manager.is_paused():
                        self.state_manager.set_state(STATE_PLAYING)
        
        return True, mouse_pos, mouse_click
    
    def handle_player_input(self):
        """处理玩家输入"""
        keys = pygame.key.get_pressed()
        
        dx = 0
        dy = 0
        
        # 方向键或WASD控制
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx -= 1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx += 1
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            dy -= 1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            dy += 1
        
        # 移动玩家鱼
        if dx != 0 or dy != 0:
            self.player.move(dx, dy)
            self.player.check_boundary()
    
    def update_game(self):
        """更新游戏状态"""
        if not self.state_manager.is_playing():
            return
        
        # 更新游戏时间
        self.state_manager.update_game_time()
        
        # 更新NPC鱼
        self.npc_manager.update()
        
        # 碰撞检测
        eaten_fishes, game_over = self.collision_detector.check_all_collisions(
            self.player, self.npc_manager
        )
        
        # 处理吃掉的鱼
        for fish in eaten_fishes:
            # 玩家成长
            self.player.grow(fish.size)
            
            # 增加分数
            self.score_system.add_score(fish.size, self.player.get_level())
            
            # 移除被吃掉的鱼并生成新鱼
            self.npc_manager.remove_fish(fish)
        
        # 调整难度
        if len(eaten_fishes) > 0:
            self.npc_manager.adjust_difficulty()
        
        # 检查游戏是否结束
        if game_over:
            self.state_manager.set_state(STATE_GAME_OVER)
    
    def render(self, mouse_pos, mouse_click):
        """渲染画面"""
        if self.state_manager.is_menu():
            # 渲染主菜单
            action = self.renderer.draw_menu(
                mouse_pos, mouse_click, 
                self.score_system.get_high_score()
            )
            
            if action == "start":
                self.init_game()
            elif action == "quit":
                return False
        
        elif self.state_manager.is_playing():
            # 渲染游戏场景
            self.renderer.draw_game(
                self.player,
                self.npc_manager,
                self.score_system.get_current_score(),
                self.player.get_level(),
                self.state_manager.get_formatted_time()
            )
        
        elif self.state_manager.is_paused():
            # 先渲染游戏场景（作为背景）
            self.renderer.draw_game(
                self.player,
                self.npc_manager,
                self.score_system.get_current_score(),
                self.player.get_level(),
                self.state_manager.get_formatted_time()
            )
            
            # 渲染暂停菜单
            action = self.renderer.draw_paused(mouse_pos, mouse_click)
            
            if action == "continue":
                self.state_manager.set_state(STATE_PLAYING)
            elif action == "menu":
                self.state_manager.set_state(STATE_MENU)
        
        elif self.state_manager.is_game_over():
            # 渲染游戏结束界面
            action = self.renderer.draw_game_over(
                mouse_pos, mouse_click,
                self.score_system.get_current_score(),
                self.score_system.get_high_score()
            )
            
            if action == "restart":
                self.init_game()
            elif action == "menu":
                self.state_manager.set_state(STATE_MENU)
        
        # 更新显示
        pygame.display.flip()
        return True
    
    def run(self):
        """运行游戏主循环"""
        running = True
        
        while running:
            # 处理事件
            event_result = self.handle_events()
            if not event_result:
                running = False
                break
            
            _, mouse_pos, mouse_click = event_result
            
            # 处理玩家输入（仅在游戏进行时）
            if self.state_manager.is_playing():
                self.handle_player_input()
            
            # 更新游戏
            self.update_game()
            
            # 渲染画面
            if not self.render(mouse_pos, mouse_click):
                running = False
            
            # 控制帧率
            self.clock.tick(FPS)
        
        # 退出游戏
        pygame.quit()
        sys.exit()


def main():
    """主函数"""
    game = FishGame()
    game.run()


if __name__ == "__main__":
    main()
