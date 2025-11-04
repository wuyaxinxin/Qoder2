始终生效
模型决策

import java.util.Random;
import java.util.List;

/**
 * 食物模型类
 * 管理食物的生成和位置
 */
public class Food {
    private Point position;
    private Random random;
    
    /**
     * 构造函数
     */
    public Food() {
        random = new Random();
        position = new Point(0, 0);
    }
    
    /**
     * 生成新的食物位置
     * @param width 游戏区域宽度
     * @param height 游戏区域高度
     * @param snakeBody 蛇身节点列表,确保食物不与蛇身重叠
     */
    public void generate(int width, int height, List<Point> snakeBody) {
        boolean validPosition = false;
        int maxAttempts = 1000; // 防止无限循环
        int attempts = 0;
        
        while (!validPosition && attempts < maxAttempts) {
            int x = random.nextInt(width);
            int y = random.nextInt(height);
            Point newPosition = new Point(x, y);
            
            // 检查是否与蛇身重叠
            validPosition = true;
            for (Point segment : snakeBody) {
                if (newPosition.equals(segment)) {
                    validPosition = false;
                    break;
                }
            }
            
            if (validPosition) {
                position = newPosition;
            }
            attempts++;
        }
    }
    
    /**
     * 获取食物位置
     */
    public Point getPosition() {
        return position;
    }
    
    /**
     * 设置食物位置
     */
    public void setPosition(Point position) {
        this.position = position;
    }
}
