/**
 * 计算器类 - 提供基本的数学运算功能
 * 
 * @author Qoder
 * @version 1.0
 */
public class Calculator {
    
    /**
     * 加法运算
     * @param a 第一个数
     * @param b 第二个数
     * @return 两数之和
     */
    public double add(double a, double b) {
        return a + b;
    }
    
    /**
     * 减法运算
     * @param a 被减数
     * @param b 减数
     * @return 两数之差
     */
    public double subtract(double a, double b) {
        return a - b;
    }
    
    /**
     * 乘法运算
     * @param a 第一个数
     * @param b 第二个数
     * @return 两数之积
     */
    public double multiply(double a, double b) {
        return a * b;
    }
    
    /**
     * 除法运算
     * @param a 被除数
     * @param b 除数
     * @return 两数之商
     * @throws ArithmeticException 当除数为0时抛出
     */
    public double divide(double a, double b) throws ArithmeticException {
        if (b == 0) {
            throw new ArithmeticException("除数不能为0");
        }
        return a / b;
    }
    
    /**
     * 求幂运算
     * @param base 底数
     * @param exponent 指数
     * @return base的exponent次方
     */
    public double power(double base, double exponent) {
        return Math.pow(base, exponent);
    }
    
    /**
     * 求平方根
     * @param number 要求平方根的数
     * @return 平方根值
     * @throws ArithmeticException 当number为负数时抛出
     */
    public double sqrt(double number) throws ArithmeticException {
        if (number < 0) {
            throw new ArithmeticException("不能对负数求平方根");
        }
        return Math.sqrt(number);
    }
    
    /**
     * 求绝对值
     * @param number 输入数字
     * @return 绝对值
     */
    public double abs(double number) {
        return Math.abs(number);
    }
    
    /**
     * 主方法 - 演示计算器的使用
     */
    public static void main(String[] args) {
        Calculator calc = new Calculator();
        
        System.out.println("=== 计算器演示 ===");
        System.out.println("10 + 5 = " + calc.add(10, 5));
        System.out.println("10 - 5 = " + calc.subtract(10, 5));
        System.out.println("10 * 5 = " + calc.multiply(10, 5));
        System.out.println("10 / 5 = " + calc.divide(10, 5));
        System.out.println("2 ^ 3 = " + calc.power(2, 3));
        System.out.println("√16 = " + calc.sqrt(16));
        System.out.println("|-7| = " + calc.abs(-7));
        
        // 异常处理示例
        try {
            calc.divide(10, 0);
        } catch (ArithmeticException e) {
            System.out.println("错误: " + e.getMessage());
        }
        
        try {
            calc.sqrt(-9);
        } catch (ArithmeticException e) {
            System.out.println("错误: " + e.getMessage());
        }
    }
}
