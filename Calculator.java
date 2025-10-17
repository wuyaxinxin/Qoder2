/**
 * Calculator类 - 提供基本的数学运算功能
 * 
 * @author Qoder
 * @version 1.0
 * @since 2025-10-13
 */
public class Calculator {
    
    /**
     * 加法运算
     * 
     * @param a 第一个加数
     * @param b 第二个加数
     * @return 两数之和
     */
    public int add(int a, int b) {
        return a + b;
    }
    
    /**
     * 减法运算
     * 
     * @param a 被减数
     * @param b 减数
     * @return 差值
     */
    public int subtract(int a, int b) {
        return a - b;
    }
    
    /**
     * 乘法运算
     * 
     * @param a 第一个乘数
     * @param b 第二个乘数
     * @return 两数之积
     */
    public int multiply(int a, int b) {
        return a * b;
    }
    
    /**
     * 除法运算
     * 
     * @param a 被除数
     * @param b 除数
     * @return 商
     * @throws ArithmeticException 当除数为0时抛出异常
     */
    public double divide(int a, int b) {
        if (b == 0) {
            throw new ArithmeticException("除数不能为0");
        }
        return (double) a / b;
    }
    
    /**
     * 主函数 - 演示Calculator类的使用
     * 
     * @param args 命令行参数
     */
    public static void main(String[] args) {
        Calculator calc = new Calculator();
        
        System.out.println("=== 计算器演示 ===");
        System.out.println("10 + 5 = " + calc.add(10, 5));
        System.out.println("10 - 5 = " + calc.subtract(10, 5));
        System.out.println("10 * 5 = " + calc.multiply(10, 5));
        System.out.println("10 / 5 = " + calc.divide(10, 5));
        
        try {
            System.out.println("10 / 0 = " + calc.divide(10, 0));
        } catch (ArithmeticException e) {
            System.out.println("错误: " + e.getMessage());
        }
    }
}
