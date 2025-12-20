// 始终生效
// Canvas棋盘绘制模块

class BoardRenderer {
    constructor(canvasId) {
        this.canvas = document.getElementById(canvasId);
        this.ctx = this.canvas.getContext('2d');
        this.gridSize = 40;
        this.padding = 20;
        this.boardSize = 15;
    }

    drawBoard() {
        const ctx = this.ctx;
        
        // 清空画布
        ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
        
        // 绘制木质背景
        ctx.fillStyle = '#DEB887';
        ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
        
        // 绘制网格线
        ctx.strokeStyle = '#000';
        ctx.lineWidth = 1;
        
        for (let i = 0; i < this.boardSize; i++) {
            // 横线
            ctx.beginPath();
            ctx.moveTo(this.padding, this.padding + i * this.gridSize);
            ctx.lineTo(this.padding + (this.boardSize - 1) * this.gridSize, 
                      this.padding + i * this.gridSize);
            ctx.stroke();
            
            // 竖线
            ctx.beginPath();
            ctx.moveTo(this.padding + i * this.gridSize, this.padding);
            ctx.lineTo(this.padding + i * this.gridSize, 
                      this.padding + (this.boardSize - 1) * this.gridSize);
            ctx.stroke();
        }
        
        // 绘制天元和星位
        this.drawStar(7, 7);
        this.drawStar(3, 3);
        this.drawStar(3, 11);
        this.drawStar(11, 3);
        this.drawStar(11, 11);
    }

    drawStar(row, col) {
        const ctx = this.ctx;
        const x = this.padding + col * this.gridSize;
        const y = this.padding + row * this.gridSize;
        
        ctx.fillStyle = '#000';
        ctx.beginPath();
        ctx.arc(x, y, 4, 0, Math.PI * 2);
        ctx.fill();
    }

    drawStone(row, col, color) {
        const ctx = this.ctx;
        const x = this.padding + col * this.gridSize;
        const y = this.padding + row * this.gridSize;
        const radius = this.gridSize / 2 - 2;
        
        // 绘制棋子阴影
        ctx.save();
        ctx.fillStyle = 'rgba(0, 0, 0, 0.3)';
        ctx.beginPath();
        ctx.arc(x + 2, y + 2, radius, 0, Math.PI * 2);
        ctx.fill();
        ctx.restore();
        
        // 绘制棋子
        if (color === 'black') {
            // 黑色棋子 - 渐变效果
            const gradient = ctx.createRadialGradient(x - 5, y - 5, 0, x, y, radius);
            gradient.addColorStop(0, '#555');
            gradient.addColorStop(1, '#000');
            ctx.fillStyle = gradient;
        } else {
            // 白色棋子 - 渐变效果
            const gradient = ctx.createRadialGradient(x - 5, y - 5, 0, x, y, radius);
            gradient.addColorStop(0, '#fff');
            gradient.addColorStop(1, '#ddd');
            ctx.fillStyle = gradient;
        }
        
        ctx.beginPath();
        ctx.arc(x, y, radius, 0, Math.PI * 2);
        ctx.fill();
        
        // 白色棋子添加边框
        if (color === 'white') {
            ctx.strokeStyle = '#000';
            ctx.lineWidth = 1;
            ctx.stroke();
        }
    }

    highlightWinLine(positions) {
        if (!positions || positions.length === 0) return;
        
        const ctx = this.ctx;
        ctx.strokeStyle = '#ff0000';
        ctx.lineWidth = 4;
        
        ctx.beginPath();
        const firstPos = positions[0];
        const startX = this.padding + firstPos[1] * this.gridSize;
        const startY = this.padding + firstPos[0] * this.gridSize;
        ctx.moveTo(startX, startY);
        
        const lastPos = positions[positions.length - 1];
        const endX = this.padding + lastPos[1] * this.gridSize;
        const endY = this.padding + lastPos[0] * this.gridSize;
        ctx.lineTo(endX, endY);
        
        ctx.stroke();
    }

    showHint(row, col) {
        const ctx = this.ctx;
        const x = this.padding + col * this.gridSize;
        const y = this.padding + row * this.gridSize;
        const radius = this.gridSize / 2 - 2;
        
        // 绘制半透明提示圆圈
        ctx.save();
        ctx.strokeStyle = 'rgba(0, 255, 0, 0.6)';
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.arc(x, y, radius, 0, Math.PI * 2);
        ctx.stroke();
        ctx.restore();
        
        // 3秒后清除提示
        setTimeout(() => {
            this.clearHint(row, col);
        }, 3000);
    }

    clearHint(row, col) {
        // 重绘该区域以清除提示
        const x = this.padding + col * this.gridSize;
        const y = this.padding + row * this.gridSize;
        const size = this.gridSize;
        
        // 清除该区域
        this.ctx.clearRect(x - size/2, y - size/2, size, size);
        
        // 重绘背景
        this.ctx.fillStyle = '#DEB887';
        this.ctx.fillRect(x - size/2, y - size/2, size, size);
        
        // 重绘网格线
        this.redrawGridLines(row, col);
    }

    redrawGridLines(row, col) {
        const ctx = this.ctx;
        const x = this.padding + col * this.gridSize;
        const y = this.padding + row * this.gridSize;
        
        ctx.strokeStyle = '#000';
        ctx.lineWidth = 1;
        
        // 重绘横线
        ctx.beginPath();
        ctx.moveTo(this.padding, y);
        ctx.lineTo(this.padding + (this.boardSize - 1) * this.gridSize, y);
        ctx.stroke();
        
        // 重绘竖线
        ctx.beginPath();
        ctx.moveTo(x, this.padding);
        ctx.lineTo(x, this.padding + (this.boardSize - 1) * this.gridSize);
        ctx.stroke();
    }

    getClickPosition(event) {
        const rect = this.canvas.getBoundingClientRect();
        const x = event.clientX - rect.left;
        const y = event.clientY - rect.top;
        
        // 计算最近的交叉点
        const col = Math.round((x - this.padding) / this.gridSize);
        const row = Math.round((y - this.padding) / this.gridSize);
        
        // 检查是否在棋盘范围内
        if (row >= 0 && row < this.boardSize && col >= 0 && col < this.boardSize) {
            return { row, col };
        }
        
        return null;
    }

    drawAllStones(board) {
        for (let row = 0; row < this.boardSize; row++) {
            for (let col = 0; col < this.boardSize; col++) {
                if (board[row][col] === 1) {
                    this.drawStone(row, col, 'black');
                } else if (board[row][col] === 2) {
                    this.drawStone(row, col, 'white');
                }
            }
        }
    }
}
