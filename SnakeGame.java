始终生效
模型决策

import javax.swing.*;

/**
 * 贪吃蛇游戏主程序
 * 程序入口
 */
public class SnakeGame {
    /**
     * 主函数
     */
    public static void main(String[] args) {
        // 使用事件调度线程来创建和显示GUI
        SwingUtilities.invokeLater(() -> {
            try {
                // 设置系统外观
                UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
            } catch (Exception e) {
                e.printStackTrace();
            }
            
            // 创建并显示游戏窗口
            GameFrame frame = new GameFrame();
            frame.setVisible(true);
        });
    }
}
