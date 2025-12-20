# 始终生效
"""
游戏状态管理模块
负责管理游戏状态、历史记录的存储与加载
"""

import json
import os
import uuid
from datetime import datetime
from typing import List, Tuple, Optional


class GameState:
    """游戏状态类"""
    
    def __init__(self, difficulty='medium'):
        self.game_id = str(uuid.uuid4())
        self.board = [[0 for _ in range(15)] for _ in range(15)]  # 0=空, 1=黑(玩家), 2=白(AI)
        self.current_player = 1  # 1=黑(玩家), 2=白(AI)
        self.move_history = []  # [(row, col, player), ...]
        self.game_status = 'ongoing'  # ongoing/player_win/ai_win/draw
        self.undo_count = 0  # 已使用悔棋次数
        self.hint_count = 0  # 已使用提示次数
        self.difficulty = difficulty  # easy/medium/hard
        self.start_time = datetime.now()
        
    def to_dict(self):
        """转换为字典格式"""
        return {
            'game_id': self.game_id,
            'board': self.board,
            'current_player': self.current_player,
            'game_status': self.game_status,
            'undo_count': self.undo_count,
            'hint_count': self.hint_count,
            'difficulty': self.difficulty
        }


def create_new_game(difficulty='medium'):
    """
    创建新游戏
    
    Args:
        difficulty: 难度级别 (easy/medium/hard)
    
    Returns:
        GameState: 新游戏状态对象
    """
    return GameState(difficulty)


def validate_move(game_state, row, col):
    """
    验证落子合法性
    
    Args:
        game_state: GameState对象
        row: 行坐标
        col: 列坐标
    
    Returns:
        (bool, str): (是否合法, 错误信息)
    """
    # 检查坐标是否在棋盘内
    if not (0 <= row < 15 and 0 <= col < 15):
        return False, "坐标超出棋盘范围"
    
    # 检查位置是否已有棋子
    if game_state.board[row][col] != 0:
        return False, "该位置已有棋子"
    
    # 检查游戏是否已结束
    if game_state.game_status != 'ongoing':
        return False, "游戏已结束"
    
    return True, ""


def make_move(game_state, row, col, player):
    """
    执行落子
    
    Args:
        game_state: GameState对象
        row: 行坐标
        col: 列坐标
        player: 玩家标识 (1=黑/2=白)
    
    Returns:
        bool: 是否落子成功
    """
    valid, _ = validate_move(game_state, row, col)
    if not valid:
        return False
    
    game_state.board[row][col] = player
    game_state.move_history.append((row, col, player))
    game_state.current_player = 3 - player  # 切换玩家: 1->2, 2->1
    
    return True


def undo_move(game_state, steps=2):
    """
    悔棋
    
    Args:
        game_state: GameState对象
        steps: 撤销步数 (默认2,撤销玩家+AI的落子)
    
    Returns:
        (bool, str): (是否成功, 错误信息)
    """
    # 检查是否可以悔棋
    if game_state.game_status != 'ongoing':
        return False, "游戏已结束,不可悔棋"
    
    if game_state.undo_count >= 3:
        return False, "已达到最大悔棋次数(3次)"
    
    if len(game_state.move_history) < steps:
        return False, f"历史记录不足{steps}步"
    
    # 撤销落子
    for _ in range(steps):
        if game_state.move_history:
            row, col, player = game_state.move_history.pop()
            game_state.board[row][col] = 0
    
    # 切换回玩家回合
    game_state.current_player = 1
    game_state.undo_count += 1
    
    return True, ""


def save_game_history(game_state, result):
    """
    保存游戏记录到JSON文件
    
    Args:
        game_state: GameState对象
        result: 游戏结果 (player_win/ai_win/draw)
    """
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    os.makedirs(data_dir, exist_ok=True)
    
    history_file = os.path.join(data_dir, 'game_history.json')
    
    # 读取现有历史记录
    if os.path.exists(history_file):
        with open(history_file, 'r', encoding='utf-8') as f:
            history_data = json.load(f)
    else:
        history_data = {
            'metadata': {
                'total_games': 0,
                'player_wins': 0,
                'ai_wins': 0,
                'draws': 0
            },
            'games': []
        }
    
    # 更新统计数据
    history_data['metadata']['total_games'] += 1
    if result == 'player_win':
        history_data['metadata']['player_wins'] += 1
    elif result == 'ai_win':
        history_data['metadata']['ai_wins'] += 1
    elif result == 'draw':
        history_data['metadata']['draws'] += 1
    
    # 添加本局游戏记录
    game_record = {
        'game_id': game_state.game_id,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'difficulty': game_state.difficulty,
        'result': result,
        'total_moves': len(game_state.move_history),
        'duration_seconds': int((datetime.now() - game_state.start_time).total_seconds())
    }
    history_data['games'].append(game_record)
    
    # 只保留最近100局记录
    if len(history_data['games']) > 100:
        history_data['games'] = history_data['games'][-100:]
    
    # 保存到文件
    with open(history_file, 'w', encoding='utf-8') as f:
        json.dump(history_data, f, ensure_ascii=False, indent=2)


def load_game_history():
    """
    加载游戏历史记录
    
    Returns:
        dict: 历史记录数据
    """
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    history_file = os.path.join(data_dir, 'game_history.json')
    
    if os.path.exists(history_file):
        with open(history_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return {
            'metadata': {
                'total_games': 0,
                'player_wins': 0,
                'ai_wins': 0,
                'draws': 0
            },
            'games': []
        }
