始终生效
模型决策

import java.util.ArrayList;
import java.util.List;

/**
 * 蛇模型类
 * 管理蛇的位置、移动、生长等逻辑
 */
public class Snake {
    private List<Point> body;           // 蛇身节点列表,第一个元素为蛇头
    private Direction currentDirection; // 当前移动方向
    private boolean alive;              // 是否存活
    private boolean growing;            // 是否正在生长(吃到食物后)
    
    /**
     * 构造函数,初始化蛇
     * @param initialX 初始x坐标
     * @param initialY 初始y坐标
     * @param initialLength 初始长度
     */
    public Snake(int initialX, int initialY, int initialLength) {
        body = new ArrayList<>();
        // 初始化蛇身,从头到尾水平排列
        for (int i = 0; i < initialLength; i++) {
            body.add(new Point(initialX - i, initialY));
        }
        currentDirection = Direction.RIGHT; // 初始方向向右
        alive = true;
        growing = false;
    }
    
    /**
     * 移动蛇
     */
    public void move() {
        if (!alive) return;
        
        // 计算新的头部位置
        Point head = body.get(0);
        Point newHead = new Point(head);
        
        switch (currentDirection) {
            case UP:
                newHead.setY(newHead.getY() - 1);
                break;
            case DOWN:
                newHead.setY(newHead.getY() + 1);
                break;
            case LEFT:
                newHead.setX(newHead.getX() - 1);
                break;
            case RIGHT:
                newHead.setX(newHead.getX() + 1);
                break;
        }
        
        // 在头部添加新节点
        body.add(0, newHead);
        
        // 如果没有吃到食物,移除尾部节点
        if (!growing) {
            body.remove(body.size() - 1);
        } else {
            growing = false; // 生长完成
        }
    }
    
    /**
     * 改变移动方向
     * @param newDirection 新方向
     * @return 是否成功改变方向
     */
    public boolean changeDirection(Direction newDirection) {
        // 不能反向移动
        if (currentDirection.isOpposite(newDirection)) {
            return false;
        }
        currentDirection = newDirection;
        return true;
    }
    
    /**
     * 增长(吃到食物时调用)
     */
    public void grow() {
        growing = true;
    }
    
    /**
     * 检查是否撞到自己
     * @return 是否撞到自己
     */
    public boolean checkSelfCollision() {
        Point head = body.get(0);
        // 检查头部是否与身体其他部分重叠
        for (int i = 1; i < body.size(); i++) {
            if (head.equals(body.get(i))) {
                return true;
            }
        }
        return false;
    }
    
    /**
     * 检查是否撞墙
     * @param width 游戏区域宽度
     * @param height 游戏区域高度
     * @return 是否撞墙
     */
    public boolean checkWallCollision(int width, int height) {
        Point head = body.get(0);
        return head.getX() < 0 || head.getX() >= width ||
               head.getY() < 0 || head.getY() >= height;
    }
    
    /**
     * 检查是否吃到食物
     * @param food 食物位置
     * @return 是否吃到食物
     */
    public boolean checkFoodCollision(Point food) {
        return body.get(0).equals(food);
    }
    
    /**
     * 获取蛇头位置
     */
    public Point getHead() {
        return body.get(0);
    }
    
    /**
     * 获取蛇身所有节点
     */
    public List<Point> getBody() {
        return new ArrayList<>(body);
    }
    
    /**
     * 获取蛇的长度
     */
    public int getLength() {
        return body.size();
    }
    
    public Direction getCurrentDirection() {
        return currentDirection;
    }
    
    public boolean isAlive() {
        return alive;
    }
    
    public void setAlive(boolean alive) {
        this.alive = alive;
    }
}
