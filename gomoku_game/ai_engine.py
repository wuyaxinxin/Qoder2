# 始终生效
"""
AI引擎模块
实现三级难度的AI算法:简单/中等/困难
"""

import random
import time
from typing import Tuple, Optional
from . import board_logic


def get_move(board, difficulty='medium', ai_player=2):
    """
    统一AI接口,根据难度返回AI落子位置
    
    Args:
        board: 15x15棋盘数组
        difficulty: 难度级别 (easy/medium/hard)
        ai_player: AI玩家标识 (默认2=白)
    
    Returns:
        (row, col): AI落子位置
    """
    if difficulty == 'easy':
        return _random_ai(board)
    elif difficulty == 'medium':
        return _rule_based_ai(board, ai_player)
    elif difficulty == 'hard':
        return _minimax_ai(board, ai_player)
    else:
        return _rule_based_ai(board, ai_player)


def _random_ai(board):
    """
    简单难度AI - 随机选择合法位置
    
    Args:
        board: 15x15棋盘数组
    
    Returns:
        (row, col): 落子位置
    """
    valid_moves = board_logic.get_valid_moves(board)
    if valid_moves:
        return random.choice(valid_moves)
    return None


def _rule_based_ai(board, ai_player):
    """
    中等难度AI - 基于规则的启发式算法
    
    Args:
        board: 15x15棋盘数组
        ai_player: AI玩家标识 (2=白)
    
    Returns:
        (row, col): 落子位置
    """
    player_opponent = 3 - ai_player  # 对手玩家
    
    # 获取附近的可落子位置(优化性能)
    nearby_moves = board_logic.get_nearby_moves(board, radius=2)
    if not nearby_moves:
        return None
    
    best_score = -float('inf')
    best_move = None
    
    for row, col in nearby_moves:
        score = _evaluate_position(board, row, col, ai_player, player_opponent)
        
        if score > best_score:
            best_score = score
            best_move = (row, col)
    
    return best_move


def _evaluate_position(board, row, col, ai_player, player_opponent):
    """
    评估某个位置的得分
    
    Args:
        board: 15x15棋盘数组
        row: 行坐标
        col: 列坐标
        ai_player: AI玩家标识
        player_opponent: 对手玩家标识
    
    Returns:
        int: 位置评分
    """
    score = 0
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]  # 横、竖、左斜、右斜
    
    # 模拟在该位置落子
    board[row][col] = ai_player
    
    for dx, dy in directions:
        # 统计AI在该方向的连子数
        ai_count = board_logic.count_consecutive(board, row, col, dx, dy, ai_player)
        
        # 评分规则
        if ai_count >= 5:
            score += 100000  # 必胜
        elif ai_count == 4:
            score += 10000   # 活四
        elif ai_count == 3:
            score += 1000    # 活三
        elif ai_count == 2:
            score += 100     # 活二
    
    # 恢复棋盘
    board[row][col] = 0
    
    # 模拟对手在该位置落子(防守评分)
    board[row][col] = player_opponent
    
    for dx, dy in directions:
        # 统计对手在该方向的连子数
        opponent_count = board_logic.count_consecutive(board, row, col, dx, dy, player_opponent)
        
        # 防守评分(略低于进攻,但五连必须阻止)
        if opponent_count >= 5:
            score += 90000   # 必须防守
        elif opponent_count == 4:
            score += 9000    # 活四必防
        elif opponent_count == 3:
            score += 800     # 活三次防
        elif opponent_count == 2:
            score += 80
    
    # 恢复棋盘
    board[row][col] = 0
    
    # 中心位置加分
    distance_to_center = abs(row - 7) + abs(col - 7)
    score += (14 - distance_to_center) * 5
    
    return score


def _minimax_ai(board, ai_player, max_depth=3, time_limit=3.0):
    """
    困难难度AI - Minimax算法 + Alpha-Beta剪枝
    
    Args:
        board: 15x15棋盘数组
        ai_player: AI玩家标识 (2=白)
        max_depth: 最大搜索深度
        time_limit: 时间限制(秒)
    
    Returns:
        (row, col): 落子位置
    """
    start_time = time.time()
    player_opponent = 3 - ai_player
    
    # 获取附近的可落子位置
    nearby_moves = board_logic.get_nearby_moves(board, radius=2)
    if not nearby_moves:
        return None
    
    best_score = -float('inf')
    best_move = None
    alpha = -float('inf')
    beta = float('inf')
    
    for row, col in nearby_moves:
        # 检查时间限制
        if time.time() - start_time > time_limit:
            break
        
        # 模拟落子
        board[row][col] = ai_player
        
        # Minimax评估
        score = _minimax(board, max_depth - 1, False, ai_player, player_opponent, 
                        alpha, beta, start_time, time_limit)
        
        # 恢复棋盘
        board[row][col] = 0
        
        if score > best_score:
            best_score = score
            best_move = (row, col)
        
        alpha = max(alpha, score)
    
    return best_move if best_move else nearby_moves[0]


def _minimax(board, depth, is_maximizing, ai_player, player_opponent, 
            alpha, beta, start_time, time_limit):
    """
    Minimax算法递归函数
    
    Args:
        board: 棋盘数组
        depth: 剩余搜索深度
        is_maximizing: 是否为最大化玩家
        ai_player: AI玩家标识
        player_opponent: 对手玩家标识
        alpha: Alpha值
        beta: Beta值
        start_time: 开始时间
        time_limit: 时间限制
    
    Returns:
        int: 局面评分
    """
    # 检查时间限制
    if time.time() - start_time > time_limit:
        return 0
    
    # 检查是否达到搜索深度
    if depth == 0:
        return _evaluate_board(board, ai_player, player_opponent)
    
    # 获取可落子位置
    nearby_moves = board_logic.get_nearby_moves(board, radius=2)
    if not nearby_moves:
        return 0
    
    if is_maximizing:
        max_eval = -float('inf')
        for row, col in nearby_moves:
            board[row][col] = ai_player
            eval_score = _minimax(board, depth - 1, False, ai_player, player_opponent,
                                alpha, beta, start_time, time_limit)
            board[row][col] = 0
            
            max_eval = max(max_eval, eval_score)
            alpha = max(alpha, eval_score)
            
            # Alpha-Beta剪枝
            if beta <= alpha:
                break
        
        return max_eval
    else:
        min_eval = float('inf')
        for row, col in nearby_moves:
            board[row][col] = player_opponent
            eval_score = _minimax(board, depth - 1, True, ai_player, player_opponent,
                                alpha, beta, start_time, time_limit)
            board[row][col] = 0
            
            min_eval = min(min_eval, eval_score)
            beta = min(beta, eval_score)
            
            # Alpha-Beta剪枝
            if beta <= alpha:
                break
        
        return min_eval


def _evaluate_board(board, ai_player, player_opponent):
    """
    评估整个棋盘局面
    
    Args:
        board: 15x15棋盘数组
        ai_player: AI玩家标识
        player_opponent: 对手玩家标识
    
    Returns:
        int: 局面评分 (AI得分 - 对手得分)
    """
    ai_score = 0
    opponent_score = 0
    
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
    
    # 评估所有位置
    for row in range(15):
        for col in range(15):
            if board[row][col] == ai_player:
                for dx, dy in directions:
                    count = board_logic.count_consecutive(board, row, col, dx, dy, ai_player)
                    ai_score += _get_score_by_count(count)
            
            elif board[row][col] == player_opponent:
                for dx, dy in directions:
                    count = board_logic.count_consecutive(board, row, col, dx, dy, player_opponent)
                    opponent_score += _get_score_by_count(count)
    
    return ai_score - opponent_score


def _get_score_by_count(count):
    """
    根据连子数返回评分
    
    Args:
        count: 连子数量
    
    Returns:
        int: 评分
    """
    if count >= 5:
        return 100000
    elif count == 4:
        return 10000
    elif count == 3:
        return 1000
    elif count == 2:
        return 100
    else:
        return 10
