# 始终生效
"""
Flask应用主文件
提供五子棋游戏的Web界面和REST API
"""

from flask import Flask, render_template, request, jsonify, session
import os
from . import game_manager, board_logic, ai_engine

app = Flask(__name__)
app.secret_key = os.urandom(24)

# 内存存储游戏会话
game_sessions = {}


@app.route('/')
def index():
    """游戏主页"""
    return render_template('gomoku.html')


@app.route('/api/new_game', methods=['POST'])
def new_game():
    """
    创建新游戏
    
    请求参数:
        difficulty: 难度级别 (easy/medium/hard)
    
    返回:
        game_id: 游戏ID
        board: 初始棋盘状态
        difficulty: 难度级别
    """
    data = request.get_json()
    difficulty = data.get('difficulty', 'medium')
    
    # 创建新游戏状态
    game_state = game_manager.create_new_game(difficulty)
    game_sessions[game_state.game_id] = game_state
    
    return jsonify({
        'game_id': game_state.game_id,
        'board': game_state.board,
        'difficulty': difficulty,
        'status': 'success'
    })


@app.route('/api/move', methods=['POST'])
def make_move():
    """
    玩家落子
    
    请求参数:
        game_id: 游戏ID
        row: 行坐标
        col: 列坐标
    
    返回:
        player_move: 玩家落子信息
        ai_move: AI落子信息
        game_status: 游戏状态
        winner_line: 获胜的五子坐标(如有)
        board: 更新后的棋盘
    """
    data = request.get_json()
    game_id = data.get('game_id')
    row = data.get('row')
    col = data.get('col')
    
    if game_id not in game_sessions:
        return jsonify({'status': 'error', 'message': '游戏不存在'}), 404
    
    game_state = game_sessions[game_id]
    
    # 验证玩家落子
    valid, error_msg = game_manager.validate_move(game_state, row, col)
    if not valid:
        return jsonify({'status': 'error', 'message': error_msg}), 400
    
    # 执行玩家落子
    game_manager.make_move(game_state, row, col, player=1)
    
    # 检查玩家是否获胜
    winner, winner_line = board_logic.check_winner(game_state.board, row, col, player=1)
    if winner == 1:
        game_state.game_status = 'player_win'
        game_manager.save_game_history(game_state, 'player_win')
        return jsonify({
            'status': 'success',
            'player_move': {'row': row, 'col': col, 'valid': True},
            'ai_move': None,
            'game_status': 'player_win',
            'winner_line': winner_line,
            'board': game_state.board
        })
    
    # 检查是否平局
    if board_logic.is_board_full(game_state.board):
        game_state.game_status = 'draw'
        game_manager.save_game_history(game_state, 'draw')
        return jsonify({
            'status': 'success',
            'player_move': {'row': row, 'col': col, 'valid': True},
            'ai_move': None,
            'game_status': 'draw',
            'winner_line': None,
            'board': game_state.board
        })
    
    # AI落子
    ai_move = ai_engine.get_move(game_state.board, game_state.difficulty, ai_player=2)
    if ai_move is None:
        return jsonify({'status': 'error', 'message': 'AI无法找到落子位置'}), 500
    
    ai_row, ai_col = ai_move
    game_manager.make_move(game_state, ai_row, ai_col, player=2)
    
    # 检查AI是否获胜
    winner, winner_line = board_logic.check_winner(game_state.board, ai_row, ai_col, player=2)
    if winner == 2:
        game_state.game_status = 'ai_win'
        game_manager.save_game_history(game_state, 'ai_win')
        return jsonify({
            'status': 'success',
            'player_move': {'row': row, 'col': col, 'valid': True},
            'ai_move': {'row': ai_row, 'col': ai_col},
            'game_status': 'ai_win',
            'winner_line': winner_line,
            'board': game_state.board
        })
    
    # 游戏继续
    return jsonify({
        'status': 'success',
        'player_move': {'row': row, 'col': col, 'valid': True},
        'ai_move': {'row': ai_row, 'col': ai_col},
        'game_status': 'ongoing',
        'winner_line': None,
        'board': game_state.board
    })


@app.route('/api/undo', methods=['POST'])
def undo():
    """
    悔棋
    
    请求参数:
        game_id: 游戏ID
        steps: 撤销步数 (默认2)
    
    返回:
        board: 更新后的棋盘
        status: 操作状态
    """
    data = request.get_json()
    game_id = data.get('game_id')
    steps = data.get('steps', 2)
    
    if game_id not in game_sessions:
        return jsonify({'status': 'error', 'message': '游戏不存在'}), 404
    
    game_state = game_sessions[game_id]
    
    # 执行悔棋
    success, error_msg = game_manager.undo_move(game_state, steps)
    if not success:
        return jsonify({'status': 'error', 'message': error_msg}), 400
    
    return jsonify({
        'status': 'success',
        'board': game_state.board,
        'undo_count': game_state.undo_count,
        'message': '悔棋成功'
    })


@app.route('/api/hint', methods=['GET'])
def get_hint():
    """
    获取提示
    
    请求参数:
        game_id: 游戏ID
    
    返回:
        row: 建议行坐标
        col: 建议列坐标
    """
    game_id = request.args.get('game_id')
    
    if game_id not in game_sessions:
        return jsonify({'status': 'error', 'message': '游戏不存在'}), 404
    
    game_state = game_sessions[game_id]
    
    # 检查提示次数限制
    if game_state.hint_count >= 5:
        return jsonify({'status': 'error', 'message': '已达到最大提示次数(5次)'}), 400
    
    # 使用中等难度AI算法计算提示
    hint_move = ai_engine.get_move(game_state.board, 'medium', ai_player=1)
    if hint_move is None:
        return jsonify({'status': 'error', 'message': '无法生成提示'}), 500
    
    game_state.hint_count += 1
    
    return jsonify({
        'status': 'success',
        'row': hint_move[0],
        'col': hint_move[1],
        'hint_count': game_state.hint_count
    })


@app.route('/api/history', methods=['GET'])
def get_history():
    """
    获取游戏历史记录
    
    返回:
        metadata: 统计数据
        games: 游戏记录列表
    """
    history_data = game_manager.load_game_history()
    
    return jsonify({
        'status': 'success',
        'metadata': history_data['metadata'],
        'games': history_data['games'][-20:]  # 返回最近20局
    })


if __name__ == '__main__':
    app.run(debug=True, port=5001)
