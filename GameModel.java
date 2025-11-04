始终生效
模型决策

/**
 * 游戏模型类
 * 管理游戏的整体状态和逻辑
 */
public class GameModel {
    // 游戏配置参数
    public static final int GRID_WIDTH = 30;      // 网格宽度
    public static final int GRID_HEIGHT = 30;     // 网格高度
    public static final int INITIAL_SNAKE_LENGTH = 3; // 初始蛇长
    public static final int MOVE_INTERVAL = 100;  // 移动间隔(毫秒)
    public static final int SCORE_PER_FOOD = 10;  // 每个食物的分数
    
    private Snake snake;           // 蛇对象
    private Food food;             // 食物对象
    private GameState gameState;   // 游戏状态
    private int score;             // 当前分数
    private int highScore;         // 历史最高分
    
    /**
     * 构造函数
     */
    public GameModel() {
        highScore = 0;
        reset();
    }
    
    /**
     * 重置游戏
     */
    public void reset() {
        // 初始化蛇,位置在游戏区域中央
        snake = new Snake(GRID_WIDTH / 2, GRID_HEIGHT / 2, INITIAL_SNAKE_LENGTH);
        
        // 初始化食物
        food = new Food();
        food.generate(GRID_WIDTH, GRID_HEIGHT, snake.getBody());
        
        // 初始化游戏状态
        gameState = GameState.NOT_STARTED;
        score = 0;
    }
    
    /**
     * 开始游戏
     */
    public void start() {
        if (gameState == GameState.NOT_STARTED || gameState == GameState.GAME_OVER) {
            reset();
        }
        gameState = GameState.RUNNING;
    }
    
    /**
     * 暂停游戏
     */
    public void pause() {
        if (gameState == GameState.RUNNING) {
            gameState = GameState.PAUSED;
        }
    }
    
    /**
     * 继续游戏
     */
    public void resume() {
        if (gameState == GameState.PAUSED) {
            gameState = GameState.RUNNING;
        }
    }
    
    /**
     * 切换暂停状态
     */
    public void togglePause() {
        if (gameState == GameState.RUNNING) {
            pause();
        } else if (gameState == GameState.PAUSED) {
            resume();
        }
    }
    
    /**
     * 游戏更新(每个时间步调用)
     */
    public void update() {
        if (gameState != GameState.RUNNING) {
            return;
        }
        
        // 移动蛇
        snake.move();
        
        // 检查碰撞
        if (snake.checkWallCollision(GRID_WIDTH, GRID_HEIGHT) || 
            snake.checkSelfCollision()) {
            gameOver();
            return;
        }
        
        // 检查是否吃到食物
        if (snake.checkFoodCollision(food.getPosition())) {
            snake.grow();
            score += SCORE_PER_FOOD;
            food.generate(GRID_WIDTH, GRID_HEIGHT, snake.getBody());
        }
    }
    
    /**
     * 改变蛇的移动方向
     */
    public void changeSnakeDirection(Direction direction) {
        if (gameState == GameState.RUNNING) {
            snake.changeDirection(direction);
        }
    }
    
    /**
     * 游戏结束
     */
    private void gameOver() {
        gameState = GameState.GAME_OVER;
        snake.setAlive(false);
        
        // 更新最高分
        if (score > highScore) {
            highScore = score;
        }
    }
    
    // Getters
    public Snake getSnake() {
        return snake;
    }
    
    public Food getFood() {
        return food;
    }
    
    public GameState getGameState() {
        return gameState;
    }
    
    public int getScore() {
        return score;
    }
    
    public int getHighScore() {
        return highScore;
    }
}
