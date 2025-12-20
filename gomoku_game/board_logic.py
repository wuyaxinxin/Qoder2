# 始终生效
"""
五子棋棋盘逻辑模块
负责棋盘相关的核心逻辑:胜负判断、可落子位置等
"""


def check_winner(board, last_row, last_col, player):
    """
    检查是否有玩家获胜
    
    Args:
        board: 15x15棋盘数组
        last_row: 最后落子的行
        last_col: 最后落子的列
        player: 玩家标识 (1=黑/2=白)
    
    Returns:
        (winner, positions): winner为0表示未获胜,1或2表示获胜玩家;
                            positions为获胜的五子坐标列表,未获胜时为None
    """
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]  # 横、竖、左斜、右斜
    
    for dx, dy in directions:
        count = 1
        positions = [(last_row, last_col)]
        
        # 向一侧扫描
        for i in range(1, 5):
            r = last_row + i * dx
            c = last_col + i * dy
            if 0 <= r < 15 and 0 <= c < 15 and board[r][c] == player:
                count += 1
                positions.append((r, c))
            else:
                break
        
        # 向另一侧扫描
        for i in range(1, 5):
            r = last_row - i * dx
            c = last_col - i * dy
            if 0 <= r < 15 and 0 <= c < 15 and board[r][c] == player:
                count += 1
                positions.append((r, c))
            else:
                break
        
        if count >= 5:
            return (player, positions)
    
    return (0, None)


def is_board_full(board):
    """
    判断棋盘是否已满(平局)
    
    Args:
        board: 15x15棋盘数组
    
    Returns:
        bool: True表示棋盘已满
    """
    for row in board:
        if 0 in row:
            return False
    return True


def get_valid_moves(board):
    """
    获取所有可落子位置
    
    Args:
        board: 15x15棋盘数组
    
    Returns:
        list: 可落子位置的坐标列表 [(row, col), ...]
    """
    valid_moves = []
    for row in range(15):
        for col in range(15):
            if board[row][col] == 0:
                valid_moves.append((row, col))
    return valid_moves


def get_nearby_moves(board, radius=2):
    """
    获取已落子周围的空位(用于AI优化,缩小搜索空间)
    
    Args:
        board: 15x15棋盘数组
        radius: 搜索半径
    
    Returns:
        list: 附近可落子位置的坐标列表 [(row, col), ...]
    """
    nearby = set()
    
    # 如果棋盘为空,返回中心位置
    if all(board[r][c] == 0 for r in range(15) for c in range(15)):
        return [(7, 7)]
    
    # 找到所有已落子位置周围的空位
    for row in range(15):
        for col in range(15):
            if board[row][col] != 0:
                # 检查周围radius范围内的空位
                for dr in range(-radius, radius + 1):
                    for dc in range(-radius, radius + 1):
                        r = row + dr
                        c = col + dc
                        if (0 <= r < 15 and 0 <= c < 15 and 
                            board[r][c] == 0):
                            nearby.add((r, c))
    
    return list(nearby) if nearby else get_valid_moves(board)


def count_consecutive(board, row, col, dx, dy, player, max_count=5):
    """
    统计某个方向上的连续棋子数
    
    Args:
        board: 15x15棋盘数组
        row: 起始行
        col: 起始列
        dx: 行方向增量
        dy: 列方向增量
        player: 玩家标识
        max_count: 最大统计数量
    
    Returns:
        int: 连续棋子数量
    """
    count = 0
    
    # 向正方向统计
    for i in range(max_count):
        r = row + i * dx
        c = col + i * dy
        if 0 <= r < 15 and 0 <= c < 15 and board[r][c] == player:
            count += 1
        else:
            break
    
    # 向反方向统计(不包括起始点,避免重复计数)
    for i in range(1, max_count):
        r = row - i * dx
        c = col - i * dy
        if 0 <= r < 15 and 0 <= c < 15 and board[r][c] == player:
            count += 1
        else:
            break
    
    return count
