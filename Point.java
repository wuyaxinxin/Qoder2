始终生效
模型决策

/**
 * 坐标点类
 * 表示游戏中的一个网格坐标
 */
public class Point {
    private int x;
    private int y;
    
    /**
     * 构造函数
     * @param x x坐标
     * @param y y坐标
     */
    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
    
    /**
     * 拷贝构造函数
     * @param other 另一个点
     */
    public Point(Point other) {
        this.x = other.x;
        this.y = other.y;
    }
    
    public int getX() {
        return x;
    }
    
    public void setX(int x) {
        this.x = x;
    }
    
    public int getY() {
        return y;
    }
    
    public void setY(int y) {
        this.y = y;
    }
    
    /**
     * 判断两个点是否相等
     */
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Point point = (Point) obj;
        return x == point.x && y == point.y;
    }
    
    @Override
    public int hashCode() {
        return 31 * x + y;
    }
    
    @Override
    public String toString() {
        return "(" + x + ", " + y + ")";
    }
}
