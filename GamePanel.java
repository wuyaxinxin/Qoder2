始终生效
模型决策

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.List;

/**
 * 游戏面板类
 * 负责游戏的渲染和用户输入处理
 */
public class GamePanel extends JPanel implements ActionListener {
    // 视觉参数
    public static final int CELL_SIZE = 20;      // 每个网格单元的像素大小
    public static final Color BG_COLOR = new Color(240, 240, 240);     // 背景色
    public static final Color GRID_COLOR = new Color(220, 220, 220);   // 网格线颜色
    public static final Color SNAKE_HEAD_COLOR = new Color(34, 139, 34); // 蛇头颜色(深绿)
    public static final Color SNAKE_BODY_COLOR = new Color(50, 205, 50); // 蛇身颜色(绿色)
    public static final Color FOOD_COLOR = new Color(220, 20, 60);     // 食物颜色(红色)
    
    private GameModel gameModel;
    private Timer timer;
    
    /**
     * 构造函数
     */
    public GamePanel() {
        gameModel = new GameModel();
        
        // 设置面板大小
        int width = GameModel.GRID_WIDTH * CELL_SIZE;
        int height = GameModel.GRID_HEIGHT * CELL_SIZE;
        setPreferredSize(new Dimension(width, height));
        setBackground(BG_COLOR);
        setFocusable(true);
        
        // 添加键盘监听器
        addKeyListener(new KeyAdapter() {
            @Override
            public void keyPressed(KeyEvent e) {
                handleKeyPress(e);
            }
        });
        
        // 创建游戏计时器
        timer = new Timer(GameModel.MOVE_INTERVAL, this);
    }
    
    /**
     * 处理键盘输入
     */
    private void handleKeyPress(KeyEvent e) {
        int key = e.getKeyCode();
        
        switch (key) {
            case KeyEvent.VK_UP:
                gameModel.changeSnakeDirection(Direction.UP);
                break;
            case KeyEvent.VK_DOWN:
                gameModel.changeSnakeDirection(Direction.DOWN);
                break;
            case KeyEvent.VK_LEFT:
                gameModel.changeSnakeDirection(Direction.LEFT);
                break;
            case KeyEvent.VK_RIGHT:
                gameModel.changeSnakeDirection(Direction.RIGHT);
                break;
            case KeyEvent.VK_SPACE:
                gameModel.togglePause();
                break;
        }
        
        repaint();
    }
    
    /**
     * 开始游戏
     */
    public void startGame() {
        gameModel.start();
        timer.start();
        requestFocusInWindow();
        repaint();
    }
    
    /**
     * 暂停游戏
     */
    public void pauseGame() {
        gameModel.pause();
        repaint();
    }
    
    /**
     * 继续游戏
     */
    public void resumeGame() {
        gameModel.resume();
        repaint();
    }
    
    /**
     * 重新开始游戏
     */
    public void restartGame() {
        gameModel.reset();
        startGame();
    }
    
    /**
     * 获取游戏模型
     */
    public GameModel getGameModel() {
        return gameModel;
    }
    
    /**
     * 定时器事件处理
     */
    @Override
    public void actionPerformed(ActionEvent e) {
        gameModel.update();
        repaint();
        
        // 如果游戏结束,停止计时器
        if (gameModel.getGameState() == GameState.GAME_OVER) {
            timer.stop();
        }
    }
    
    /**
     * 绘制游戏界面
     */
    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2d = (Graphics2D) g;
        
        // 开启抗锯齿
        g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, 
                            RenderingHints.VALUE_ANTIALIAS_ON);
        
        // 绘制网格线
        drawGrid(g2d);
        
        // 绘制食物
        drawFood(g2d);
        
        // 绘制蛇
        drawSnake(g2d);
        
        // 绘制游戏状态提示
        drawGameStatus(g2d);
    }
    
    /**
     * 绘制网格线
     */
    private void drawGrid(Graphics2D g2d) {
        g2d.setColor(GRID_COLOR);
        
        // 绘制垂直线
        for (int i = 0; i <= GameModel.GRID_WIDTH; i++) {
            int x = i * CELL_SIZE;
            g2d.drawLine(x, 0, x, GameModel.GRID_HEIGHT * CELL_SIZE);
        }
        
        // 绘制水平线
        for (int i = 0; i <= GameModel.GRID_HEIGHT; i++) {
            int y = i * CELL_SIZE;
            g2d.drawLine(0, y, GameModel.GRID_WIDTH * CELL_SIZE, y);
        }
    }
    
    /**
     * 绘制蛇
     */
    private void drawSnake(Graphics2D g2d) {
        List<Point> body = gameModel.getSnake().getBody();
        
        for (int i = 0; i < body.size(); i++) {
            Point segment = body.get(i);
            int x = segment.getX() * CELL_SIZE;
            int y = segment.getY() * CELL_SIZE;
            
            // 蛇头用深绿色,蛇身用绿色
            if (i == 0) {
                g2d.setColor(SNAKE_HEAD_COLOR);
            } else {
                g2d.setColor(SNAKE_BODY_COLOR);
            }
            
            g2d.fillRoundRect(x + 1, y + 1, CELL_SIZE - 2, CELL_SIZE - 2, 5, 5);
        }
    }
    
    /**
     * 绘制食物
     */
    private void drawFood(Graphics2D g2d) {
        Point foodPos = gameModel.getFood().getPosition();
        int x = foodPos.getX() * CELL_SIZE;
        int y = foodPos.getY() * CELL_SIZE;
        
        g2d.setColor(FOOD_COLOR);
        g2d.fillOval(x + 2, y + 2, CELL_SIZE - 4, CELL_SIZE - 4);
    }
    
    /**
     * 绘制游戏状态提示
     */
    private void drawGameStatus(Graphics2D g2d) {
        String message = null;
        
        switch (gameModel.getGameState()) {
            case NOT_STARTED:
                message = "按空格键或点击开始按钮开始游戏";
                break;
            case PAUSED:
                message = "游戏已暂停 - 按空格键继续";
                break;
            case GAME_OVER:
                message = "游戏结束! 分数: " + gameModel.getScore();
                break;
        }
        
        if (message != null) {
            g2d.setColor(new Color(0, 0, 0, 180));
            g2d.fillRect(0, getHeight() / 2 - 40, getWidth(), 80);
            
            g2d.setColor(Color.WHITE);
            g2d.setFont(new Font("微软雅黑", Font.BOLD, 20));
            FontMetrics fm = g2d.getFontMetrics();
            int x = (getWidth() - fm.stringWidth(message)) / 2;
            int y = getHeight() / 2;
            g2d.drawString(message, x, y);
    }
    
    /**
     * 获取当前游戏信息
     * @return 包含游戏状态、分数等信息的字符串
     */
    public String getGameInfo() {
        StringBuilder info = new StringBuilder();
        info.append("游戏状态: ").append(gameModel.getGameState()).append("\n");
        info.append("当前分数: ").append(gameModel.getScore()).append("\n");
        info.append("蛇的长度: ").append(gameModel.getSnake().getBody().size()).append("\n");
        return info.toString();
    }
