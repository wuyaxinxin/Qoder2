/**
 * 简单示例类
 * 演示Java基本功能
 */
public class SimpleDemo {
    
    /**
     * 主方法 - 程序入口点
     * @param args 命令行参数
     */
    public static void main(String[] args) {
        // 创建SimpleDemo实例
        SimpleDemo demo = new SimpleDemo();
        
        // 调用问候方法
        demo.greet("世界");
        
        // 调用加法方法并输出结果
        int sum = demo.add(5, 3);
        System.out.println("5 + 3 = " + sum);
        
        // 调用检查偶数方法
        boolean isEven = demo.isEven(10);
        System.out.println("10是偶数吗? " + isEven);
    }
    
    /**
     * 问候方法
     * @param name 要问候的名字
     */
    public void greet(String name) {
        // 输出问候信息
        System.out.println("你好, " + name + "!");
    }
    
    /**
     * 加法方法
     * @param a 第一个加数
     * @param b 第二个加数
     * @return 两数之和
     */
    public int add(int a, int b) {
        // 返回两数相加的结果
        return a + b;
    }
    
    /**
     * 检查是否为偶数
     * @param number 要检查的数字
     * @return 如果是偶数返回true,否则返回false
     */
    public boolean isEven(int number) {
        // 使用取模运算判断是否为偶数
        return number % 2 == 0;
    }
}
