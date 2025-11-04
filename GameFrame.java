始终生效
模型决策

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

/**
 * 游戏窗口类
 * 主窗口,包含游戏面板和控制面板
 */
public class GameFrame extends JFrame {
    private GamePanel gamePanel;
    private JLabel scoreLabel;
    private JLabel highScoreLabel;
    private JLabel statusLabel;
    private JButton startButton;
    private JButton pauseButton;
    private JButton restartButton;
    
    /**
     * 构造函数
     */
    public GameFrame() {
        setTitle("贪吃蛇游戏");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setResizable(false);
        
        // 创建游戏面板
        gamePanel = new GamePanel();
        
        // 创建顶部信息栏
        JPanel topPanel = createTopPanel();
        
        // 创建底部控制栏
        JPanel bottomPanel = createBottomPanel();
        
        // 布局
        setLayout(new BorderLayout());
        add(topPanel, BorderLayout.NORTH);
        add(gamePanel, BorderLayout.CENTER);
        add(bottomPanel, BorderLayout.SOUTH);
        
        pack();
        setLocationRelativeTo(null); // 窗口居中显示
        
        // 启动定时器更新分数显示
        Timer scoreUpdateTimer = new Timer(100, e -> updateScoreDisplay());
        scoreUpdateTimer.start();
    }
    
    /**
     * 创建顶部信息栏
     */
    private JPanel createTopPanel() {
        JPanel panel = new JPanel();
        panel.setLayout(new GridLayout(1, 3, 10, 5));
        panel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
        panel.setBackground(new Color(250, 250, 250));
        
        // 分数标签
        scoreLabel = new JLabel("分数: 0", SwingConstants.CENTER);
        scoreLabel.setFont(new Font("微软雅黑", Font.BOLD, 16));
        
        // 最高分标签
        highScoreLabel = new JLabel("最高分: 0", SwingConstants.CENTER);
        highScoreLabel.setFont(new Font("微软雅黑", Font.BOLD, 16));
        
        // 状态标签
        statusLabel = new JLabel("未开始", SwingConstants.CENTER);
        statusLabel.setFont(new Font("微软雅黑", Font.BOLD, 16));
        
        panel.add(scoreLabel);
        panel.add(statusLabel);
        panel.add(highScoreLabel);
        
        return panel;
    }
    
    /**
     * 创建底部控制栏
     */
    private JPanel createBottomPanel() {
        JPanel panel = new JPanel();
        panel.setLayout(new FlowLayout());
        panel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
        panel.setBackground(new Color(250, 250, 250));
        
        // 开始按钮
        startButton = new JButton("开始游戏");
        startButton.setFont(new Font("微软雅黑", Font.PLAIN, 14));
        startButton.setFocusable(false);
        startButton.addActionListener(e -> {
            gamePanel.startGame();
            gamePanel.requestFocusInWindow();
        });
        
        // 暂停按钮
        pauseButton = new JButton("暂停");
        pauseButton.setFont(new Font("微软雅黑", Font.PLAIN, 14));
        pauseButton.setFocusable(false);
        pauseButton.addActionListener(e -> {
            GameState state = gamePanel.getGameModel().getGameState();
            if (state == GameState.RUNNING) {
                gamePanel.pauseGame();
                pauseButton.setText("继续");
            } else if (state == GameState.PAUSED) {
                gamePanel.resumeGame();
                pauseButton.setText("暂停");
            }
            gamePanel.requestFocusInWindow();
        });
        
        // 重新开始按钮
        restartButton = new JButton("重新开始");
        restartButton.setFont(new Font("微软雅黑", Font.PLAIN, 14));
        restartButton.setFocusable(false);
        restartButton.addActionListener(e -> {
            gamePanel.restartGame();
            pauseButton.setText("暂停");
            gamePanel.requestFocusInWindow();
        });
        
        panel.add(startButton);
        panel.add(pauseButton);
        panel.add(restartButton);
        
        return panel;
    }
    
    /**
     * 更新分数显示
     */
    private void updateScoreDisplay() {
        GameModel model = gamePanel.getGameModel();
        scoreLabel.setText("分数: " + model.getScore());
        highScoreLabel.setText("最高分: " + model.getHighScore());
        
        // 更新状态显示
        String status = "";
        switch (model.getGameState()) {
            case NOT_STARTED:
                status = "未开始";
                break;
            case RUNNING:
                status = "游戏中";
                break;
            case PAUSED:
                status = "已暂停";
                pauseButton.setText("继续");
                break;
            case GAME_OVER:
                status = "游戏结束";
                pauseButton.setText("暂停");
                break;
        }
        statusLabel.setText(status);
    }
}
