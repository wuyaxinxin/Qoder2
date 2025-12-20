// 始终生效
// API请求封装模块

const API = {
    async newGame(difficulty) {
        const response = await fetch('/api/new_game', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ difficulty })
        });
        
        if (!response.ok) {
            throw new Error('创建游戏失败');
        }
        
        return await response.json();
    },

    async makeMove(gameId, row, col) {
        const response = await fetch('/api/move', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ 
                game_id: gameId, 
                row, 
                col 
            })
        });
        
        const data = await response.json();
        
        if (!response.ok) {
            throw new Error(data.message || '落子失败');
        }
        
        return data;
    },

    async undo(gameId, steps = 2) {
        const response = await fetch('/api/undo', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ 
                game_id: gameId, 
                steps 
            })
        });
        
        const data = await response.json();
        
        if (!response.ok) {
            throw new Error(data.message || '悔棋失败');
        }
        
        return data;
    },

    async getHint(gameId) {
        const response = await fetch(`/api/hint?game_id=${gameId}`);
        
        const data = await response.json();
        
        if (!response.ok) {
            throw new Error(data.message || '获取提示失败');
        }
        
        return data;
    },

    async getHistory() {
        const response = await fetch('/api/history');
        
        if (!response.ok) {
            throw new Error('获取历史记录失败');
        }
        
        return await response.json();
    }
};
