/**
 * Calculator类 - 提供基本的数学运算功能
 * 
 * @author Qoder
 * @version 1.0
 */
public class Calculator {
    
    /**
     * 加法运算
     * @param a 第一个加数
     * @param b 第二个加数
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
     * @param a 第一个乘数
     * @param b 第二个乘数
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
    public double divide(double a, double b) {
        if (b == 0) {
            throw new ArithmeticException("除数不能为0");
        }
        return a / b;
    }
    
    /**
     * 计算幂运算
     * @param base 底数
     * @param exponent 指数
     * @return base的exponent次方
     */
    public double power(double base, double exponent) {
        return Math.pow(base, exponent);
    }
    
    /**
     * 计算平方根
     * @param number 要计算平方根的数
     * @return 平方根值
     * @throws IllegalArgumentException 当number为负数时抛出
     */
    public double squareRoot(double number) {
        if (number < 0) {
            throw new IllegalArgumentException("不能计算负数的平方根");
        }
        return Math.sqrt(number);
    }
    
    /**
     * 计算阶乘
     * @param n 要计算阶乘的数
     * @return n的阶乘
     * @throws IllegalArgumentException 当n为负数时抛出
     */
    public long factorial(int n) {
        if (n < 0) {
            throw new IllegalArgumentException("不能计算负数的阶乘");
        }
        if (n == 0 || n == 1) {
            return 1;
        }
        long result = 1;
        for (int i = 2; i <= n; i++) {
            result *= i;
        }
        return result;
    }
    
    /**
     * 判断是否为质数
     * @param number 要判断的数
     * @return 如果是质数返回true，否则返回false
     */
    public boolean isPrime(int number) {
        if (number <= 1) {
            return false;
        }
        if (number == 2) {
            return true;
        }
        if (number % 2 == 0) {
            return false;
        }
        for (int i = 3; i <= Math.sqrt(number); i += 2) {
            if (number % i == 0) {
                return false;
            }
        }
        return true;
    }
    
    /**
     * 主函数 - 演示Calculator类的使用
     */
    public static void main(String[] args) {
        Calculator calc = new Calculator();
        
        // 演示基本运算
        System.out.println("=== 计算器演示 ===");
        System.out.println("10 + 5 = " + calc.add(10, 5));
        System.out.println("10 - 5 = " + calc.subtract(10, 5));
        System.out.println("10 × 5 = " + calc.multiply(10, 5));
        System.out.println("10 ÷ 5 = " + calc.divide(10, 5));
        System.out.println("2 ^ 8 = " + calc.power(2, 8));
        System.out.println("√16 = " + calc.squareRoot(16));
        System.out.println("5! = " + calc.factorial(5));
        System.out.println("17是质数吗？ " + calc.isPrime(17));
        System.out.println("18是质数吗？ " + calc.isPrime(18));
    }
}
