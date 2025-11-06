始终生效

"""
吃鱼小游戏 - 渲染系统
处理所有图形渲染和UI界面
"""

import pygame
from fish_game_config import *


class Button:
    """按钮类"""
    
    def __init__(self, x, y, width, height, text, font):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = font
        self.is_hovered = False
    
    def check_hover(self, mouse_pos):
        """检查鼠标是否悬停在按钮上"""
        self.is_hovered = self.rect.collidepoint(mouse_pos)
        return self.is_hovered
    
    def check_click(self, mouse_pos, mouse_click):
        """检查按钮是否被点击"""
        if self.rect.collidepoint(mouse_pos) and mouse_click:
            return True
        return False
    
    def draw(self, screen):
        """绘制按钮"""
        color = COLOR_BUTTON_HOVER if self.is_hovered else COLOR_BUTTON
        pygame.draw.rect(screen, color, self.rect, border_radius=10)
        pygame.draw.rect(screen, COLOR_WHITE, self.rect, 2, border_radius=10)
        
        text_surface = self.font.render(self.text, True, COLOR_WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)


class Renderer:
    """渲染系统"""
    
    def __init__(self, screen):
        self.screen = screen
        
        # 初始化字体
        pygame.font.init()
        self.font_title = pygame.font.Font(None, FONT_SIZE_TITLE)
        self.font_button = pygame.font.Font(None, FONT_SIZE_BUTTON)
        self.font_info = pygame.font.Font(None, FONT_SIZE_INFO)
        
        # 创建按钮
        self.create_buttons()
    
    def create_buttons(self):
        """创建所有按钮"""
        center_x = WINDOW_WIDTH // 2 - BUTTON_WIDTH // 2
        
        # 主菜单按钮
        self.btn_start = Button(center_x, 300, BUTTON_WIDTH, BUTTON_HEIGHT, 
                                "开始游戏", self.font_button)
        self.btn_high_score = Button(center_x, 370, BUTTON_WIDTH, BUTTON_HEIGHT, 
                                     "最高分", self.font_button)
        self.btn_quit = Button(center_x, 440, BUTTON_WIDTH, BUTTON_HEIGHT, 
                              "退出", self.font_button)
        
        # 游戏结束按钮
        self.btn_restart = Button(center_x, 350, BUTTON_WIDTH, BUTTON_HEIGHT, 
                                 "重新开始", self.font_button)
        self.btn_menu = Button(center_x, 420, BUTTON_WIDTH, BUTTON_HEIGHT, 
                              "返回菜单", self.font_button)
        
        # 暂停菜单按钮
        self.btn_continue = Button(center_x, 300, BUTTON_WIDTH, BUTTON_HEIGHT, 
                                  "继续游戏", self.font_button)
        self.btn_back_menu = Button(center_x, 370, BUTTON_WIDTH, BUTTON_HEIGHT, 
                                    "返回菜单", self.font_button)
    
    def draw_background(self):
        """绘制背景"""
        self.screen.fill(COLOR_BACKGROUND)
    
    def draw_fish(self, fish):
        """绘制鱼"""
        pygame.draw.circle(self.screen, fish.color, 
                          (int(fish.x), int(fish.y)), int(fish.size))
        
        # 绘制鱼的眼睛（简单装饰）
        eye_offset = fish.size // 3
        eye_size = max(2, fish.size // 8)
        pygame.draw.circle(self.screen, COLOR_WHITE, 
                          (int(fish.x + eye_offset), int(fish.y - eye_offset)), 
                          eye_size)
    
    def draw_menu(self, mouse_pos, mouse_click, high_score):
        """绘制主菜单"""
        self.draw_background()
        
        # 绘制标题
        title = self.font_title.render("吃鱼小游戏", True, COLOR_WHITE)
        title_rect = title.get_rect(center=(WINDOW_WIDTH // 2, 150))
        self.screen.blit(title, title_rect)
        
        # 显示最高分
        high_score_text = self.font_info.render(f"最高分: {high_score}", True, COLOR_WHITE)
        high_score_rect = high_score_text.get_rect(center=(WINDOW_WIDTH // 2, 220))
        self.screen.blit(high_score_text, high_score_rect)
        
        # 绘制按钮
        self.btn_start.check_hover(mouse_pos)
        self.btn_high_score.check_hover(mouse_pos)
        self.btn_quit.check_hover(mouse_pos)
        
        self.btn_start.draw(self.screen)
        self.btn_high_score.draw(self.screen)
        self.btn_quit.draw(self.screen)
        
        # 检查按钮点击
        if self.btn_start.check_click(mouse_pos, mouse_click):
            return "start"
        elif self.btn_high_score.check_click(mouse_pos, mouse_click):
            return "high_score"
        elif self.btn_quit.check_click(mouse_pos, mouse_click):
            return "quit"
        
        return None
    
    def draw_game(self, player, npc_manager, score, level, game_time):
        """绘制游戏场景"""
        self.draw_background()
        
        # 绘制所有NPC鱼
        for fish in npc_manager.fishes:
            self.draw_fish(fish)
        
        # 绘制玩家鱼（最后绘制，显示在最上层）
        self.draw_fish(player)
        
        # 绘制UI信息
        score_text = self.font_info.render(f"分数: {score}", True, COLOR_WHITE)
        self.screen.blit(score_text, (10, 10))
        
        level_text = self.font_info.render(f"等级: {level}", True, COLOR_WHITE)
        self.screen.blit(level_text, (10, 40))
        
        time_text = self.font_info.render(f"时间: {game_time}", True, COLOR_WHITE)
        time_rect = time_text.get_rect(topright=(WINDOW_WIDTH - 10, 10))
        self.screen.blit(time_text, time_rect)
        
        # 暂停提示
        hint_text = self.font_info.render("按ESC暂停", True, COLOR_WHITE)
        hint_rect = hint_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 30))
        self.screen.blit(hint_text, hint_rect)
    
    def draw_game_over(self, mouse_pos, mouse_click, current_score, high_score):
        """绘制游戏结束界面"""
        self.draw_background()
        
        # 半透明遮罩
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))
        
        # 游戏结束标题
        title = self.font_title.render("游戏结束", True, COLOR_WHITE)
        title_rect = title.get_rect(center=(WINDOW_WIDTH // 2, 150))
        self.screen.blit(title, title_rect)
        
        # 显示分数
        score_text = self.font_button.render(f"本局得分: {current_score}", True, COLOR_WHITE)
        score_rect = score_text.get_rect(center=(WINDOW_WIDTH // 2, 250))
        self.screen.blit(score_text, score_rect)
        
        high_text = self.font_info.render(f"最高分: {high_score}", True, COLOR_WHITE)
        high_rect = high_text.get_rect(center=(WINDOW_WIDTH // 2, 290))
        self.screen.blit(high_text, high_rect)
        
        # 绘制按钮
        self.btn_restart.check_hover(mouse_pos)
        self.btn_menu.check_hover(mouse_pos)
        
        self.btn_restart.draw(self.screen)
        self.btn_menu.draw(self.screen)
        
        # 检查按钮点击
        if self.btn_restart.check_click(mouse_pos, mouse_click):
            return "restart"
        elif self.btn_menu.check_click(mouse_pos, mouse_click):
            return "menu"
        
        return None
    
    def draw_paused(self, mouse_pos, mouse_click):
        """绘制暂停界面"""
        # 半透明遮罩
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))
        
        # 暂停标题
        title = self.font_title.render("游戏暂停", True, COLOR_WHITE)
        title_rect = title.get_rect(center=(WINDOW_WIDTH // 2, 150))
        self.screen.blit(title, title_rect)
        
        # 绘制按钮
        self.btn_continue.check_hover(mouse_pos)
        self.btn_back_menu.check_hover(mouse_pos)
        
        self.btn_continue.draw(self.screen)
        self.btn_back_menu.draw(self.screen)
        
        # 检查按钮点击
        if self.btn_continue.check_click(mouse_pos, mouse_click):
            return "continue"
        elif self.btn_back_menu.check_click(mouse_pos, mouse_click):
            return "menu"
        
        return None
