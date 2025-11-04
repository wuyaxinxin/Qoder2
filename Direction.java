始终生效
模型决策

/**
 * 方向枚举类
 * 定义蛇移动的四个方向
 */
public enum Direction {
    UP,    // 向上
    DOWN,  // 向下
    LEFT,  // 向左
    RIGHT; // 向右
    
    /**
     * 判断是否为相反方向
     * @param other 另一个方向
     * @return 如果是相反方向返回true
     */
    public boolean isOpposite(Direction other) {
        return (this == UP && other == DOWN) ||
               (this == DOWN && other == UP) ||
               (this == LEFT && other == RIGHT) ||
               (this == RIGHT && other == LEFT);
    }
}
