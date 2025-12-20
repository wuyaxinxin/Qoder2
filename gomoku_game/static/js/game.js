// 始终生效
// 游戏交互控制模块

let gameState = {
    gameId: null,
    board: null,
    isPlaying: false,
    isPlayerTurn: true,
    boardRenderer: null
};

function initGame() {
    // 初始化棋盘渲染器
    gameState.boardRenderer = new BoardRenderer('gameBoard');
    gameState.boardRenderer.drawBoard();
    
    // 绑定事件监听器
    document.getElementById('gameBoard').addEventListener('click', handleBoardClick);
    document.getElementById('newGameBtn').addEventListener('click', handleNewGame);
    document.getElementById('undoBtn').addEventListener('click', handleUndo);
    document.getElementById('hintBtn').addEventListener('click', handleHint);
    
    // 加载游戏历史统计
    loadGameHistory();
}

async function handleNewGame() {
    const difficulty = document.getElementById('difficulty').value;
    
    try {
        const response = await API.newGame(difficulty);
        
        gameState.gameId = response.game_id;
        gameState.board = response.board;
        gameState.isPlaying = true;
        gameState.isPlayerTurn = true;
        
        // 重绘棋盘
        gameState.boardRenderer.drawBoard();
        
        // 更新UI
        updateStatus('游戏进行中', '轮到玩家(黑子)');
        resetCounters();
        
    } catch (error) {
        alert('创建游戏失败: ' + error.message);
    }
}

async function handleBoardClick(event) {
    if (!gameState.isPlaying || !gameState.isPlayerTurn) {
        return;
    }
    
    const pos = gameState.boardRenderer.getClickPosition(event);
    if (!pos) {
        return;
    }
    
    // 检查位置是否已有棋子
    if (gameState.board[pos.row][pos.col] !== 0) {
        return;
    }
    
    // 禁用点击
    gameState.isPlayerTurn = false;
    showLoading(true);
    
    try {
        const response = await API.makeMove(gameState.gameId, pos.row, pos.col);
        
        // 绘制玩家落子
        gameState.boardRenderer.drawStone(pos.row, pos.col, 'black');
        
        // 更新棋盘状态
        gameState.board = response.board;
        
        // 检查游戏结果
        if (response.game_status === 'player_win') {
            gameState.isPlaying = false;
            gameState.boardRenderer.highlightWinLine(response.winner_line);
            updateStatus('玩家获胜!', '');
            await loadGameHistory();
            showLoading(false);
            return;
        }
        
        if (response.game_status === 'draw') {
            gameState.isPlaying = false;
            updateStatus('平局!', '');
            await loadGameHistory();
            showLoading(false);
            return;
        }
        
        // 绘制AI落子
        if (response.ai_move) {
            await sleep(300); // 短暂延迟,让玩家看到自己的落子
            gameState.boardRenderer.drawStone(
                response.ai_move.row, 
                response.ai_move.col, 
                'white'
            );
            
            // 检查AI是否获胜
            if (response.game_status === 'ai_win') {
                gameState.isPlaying = false;
                gameState.boardRenderer.highlightWinLine(response.winner_line);
                updateStatus('AI获胜!', '');
                await loadGameHistory();
                showLoading(false);
                return;
            }
        }
        
        // 游戏继续
        gameState.isPlayerTurn = true;
        updateStatus('游戏进行中', '轮到玩家(黑子)');
        
    } catch (error) {
        alert('落子失败: ' + error.message);
        gameState.isPlayerTurn = true;
    } finally {
        showLoading(false);
    }
}

async function handleUndo() {
    if (!gameState.isPlaying) {
        alert('游戏未开始');
        return;
    }
    
    try {
        const response = await API.undo(gameState.gameId);
        
        // 更新棋盘状态
        gameState.board = response.board;
        gameState.isPlayerTurn = true;
        
        // 重绘整个棋盘
        gameState.boardRenderer.drawBoard();
        gameState.boardRenderer.drawAllStones(gameState.board);
        
        // 更新悔棋次数
        document.getElementById('undoCount').textContent = response.undo_count;
        
        updateStatus('游戏进行中', '轮到玩家(黑子)');
        
    } catch (error) {
        alert('悔棋失败: ' + error.message);
    }
}

async function handleHint() {
    if (!gameState.isPlaying || !gameState.isPlayerTurn) {
        alert('现在不能使用提示');
        return;
    }
    
    try {
        const response = await API.getHint(gameState.gameId);
        
        // 显示提示位置
        gameState.boardRenderer.showHint(response.row, response.col);
        
        // 更新提示次数
        document.getElementById('hintCount').textContent = response.hint_count;
        
    } catch (error) {
        alert('获取提示失败: ' + error.message);
    }
}

async function loadGameHistory() {
    try {
        const response = await API.getHistory();
        
        const metadata = response.metadata;
        document.getElementById('totalGames').textContent = metadata.total_games;
        document.getElementById('playerWins').textContent = metadata.player_wins;
        document.getElementById('aiWins').textContent = metadata.ai_wins;
        document.getElementById('draws').textContent = metadata.draws;
        
    } catch (error) {
        console.error('加载历史记录失败:', error);
    }
}

function updateStatus(statusText, turnText) {
    document.getElementById('statusText').textContent = statusText;
    document.getElementById('turnText').textContent = turnText;
}

function resetCounters() {
    document.getElementById('undoCount').textContent = '0';
    document.getElementById('hintCount').textContent = '0';
}

function showLoading(show) {
    const loadingIndicator = document.getElementById('loadingIndicator');
    loadingIndicator.style.display = show ? 'block' : 'none';
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// 页面加载完成后初始化
document.addEventListener('DOMContentLoaded', initGame);
