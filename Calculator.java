/**
 * 水月洞天
 * Calculator 类
 * 
 * 这是一个简单的计算器类，提供基本的数学运算功能。
 * 主要用于演示Java类的设计和实现。
 * 
 * @author 用户
 * @version 1.0
 */
public class Calculator {
    /**
     * 加法运算
     * 
     * @param a 第一个操作数
     * @param b 第二个操作数
     * @return 两个数的和
     */
    public int add(int a, int b) {
        return a + b;
    }
    
    /**
     * 减法运算
     * 
     * @param a 第一个操作数
     * @param b 第二个操作数
     * @return 两个数的差
     */
    public int subtract(int a, int b) {
        return a - b;
    }
    
    /**
     * 乘法运算
     * 
     * @param a 第一个操作数
     * @param b 第二个操作数
     * @return 两个数的积
     */
    public int multiply(int a, int b) {
        return a * b;
    }
    
    /**
     * 除法运算
     * 
     * @param a 第一个操作数
     * @param b 第二个操作数
     * @return 两个数的商
     * @throws ArithmeticException 当除数为0时抛出异常
     */
    public int divide(int a, int b) throws ArithmeticException {
        if (b == 0) {
            throw new ArithmeticException("除数不能为零");
        }
        return a / b;
    }
    
    /**
     * 主方法：程序的入口点，用于演示计算器功能
     * 
     * @param args 命令行参数（未使用）
     */
    public static void main(String[] args) {
        Calculator calc = new Calculator();
        
        // 演示各种运算
        System.out.println("加法: 5 + 3 = " + calc.add(5, 3));
        System.out.println("减法: 5 - 3 = " + calc.subtract(5, 3));
        System.out.println("乘法: 5 * 3 = " + calc.multiply(5, 3));
        System.out.println("除法: 5 / 3 = " + calc.divide(5, 3));
        
        // 演示异常处理
        try {
            calc.divide(5, 0);
        } catch (ArithmeticException e) {
            System.out.println("错误: " + e.getMessage());
        }
    }
}