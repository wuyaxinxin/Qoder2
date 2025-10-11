/*
 * 文件名: Calculator.java
 * 作者: 开发者
 * 创建日期: 2025-10-11
 * 版本: 1.0
 * 描述: 这是一个提供基本数学计算功能的Java计算器类文件
 *       包含基本运算、高级数学运算和几何计算功能
 * 功能:
 *   - 基本运算: 加、减、乘、除
 *   - 高级运算: 幂运算、开方、绝对值
 *   - 比较运算: 最大值、最小值
 *   - 几何计算: 圆面积、圆周长、矩形面积
 *   - 异常处理: 除零、负数开方等错误情况
 * 依赖: java.lang.Math 类
 * 使用示例:
 *   Calculator calc = new Calculator();
 *   double result = calc.add(10, 5); // 返回 15.0
 *   calc.demonstrateCalculator(); // 展示所有功能
 * 修改记录:
 *   2025-10-11 - 初始版本创建
 */

/**
 * Calculator类 - 提供基本的数学计算功能
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
     * @throws IllegalArgumentException 当除数为0时抛出异常
     */
    public double divide(double a, double b) {
        if (b == 0) {
            throw new IllegalArgumentException("除数不能为零");
        }
        return a / b;
    }
    
    /**
     * 幂运算
     * @param base 底数
     * @param exponent 指数
     * @return base的exponent次幂
     */
    public double power(double base, double exponent) {
        return Math.pow(base, exponent);
    }
    
    /**
     * 开平方根
     * @param number 需要开方的数
     * @return 平方根
     * @throws IllegalArgumentException 当输入负数时抛出异常
     */
    public double sqrt(double number) {
        if (number < 0) {
            throw new IllegalArgumentException("不能对负数开平方根");
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
     * 求最大值
     * @param a 第一个数
     * @param b 第二个数
     * @return 较大的数
     */
    public double max(double a, double b) {
        return Math.max(a, b);
    }
    
    /**
     * 求最小值
     * @param a 第一个数
     * @param b 第二个数
     * @return 较小的数
     */
    public double min(double a, double b) {
        return Math.min(a, b);
    }
    
    /**
     * 计算圆的面积
     * @param radius 半径
     * @return 圆的面积
     * @throws IllegalArgumentException 当半径为负数时抛出异常
     */
    public double calculateCircleArea(double radius) {
        if (radius < 0) {
            throw new IllegalArgumentException("半径不能为负数");
        }
        return Math.PI * radius * radius;
    }
    
    /**
     * 计算圆的周长
     * @param radius 半径
     * @return 圆的周长
     * @throws IllegalArgumentException 当半径为负数时抛出异常
     */
    public double calculateCircleCircumference(double radius) {
        if (radius < 0) {
            throw new IllegalArgumentException("半径不能为负数");
        }
        return 2 * Math.PI * radius;
    }
    
    /**
     * 计算矩形面积
     * @param length 长度
     * @param width 宽度
     * @return 矩形面积
     * @throws IllegalArgumentException 当长度或宽度为负数时抛出异常
     */
    public double calculateRectangleArea(double length, double width) {
        if (length < 0 || width < 0) {
            throw new IllegalArgumentException("长度和宽度不能为负数");
        }
        return length * width;
    }
    
    /**
     * 演示方法 - 展示计算器的基本功能
     */
    public void demonstrateCalculator() {
        System.out.println("=== 计算器演示 ===");
        System.out.println("10 + 5 = " + add(10, 5));
        System.out.println("10 - 5 = " + subtract(10, 5));
        System.out.println("10 * 5 = " + multiply(10, 5));
        System.out.println("10 / 5 = " + divide(10, 5));
        System.out.println("2^3 = " + power(2, 3));
        System.out.println("√16 = " + sqrt(16));
        System.out.println("|-5| = " + abs(-5));
        System.out.println("max(10, 20) = " + max(10, 20));
        System.out.println("min(10, 20) = " + min(10, 20));
        System.out.println("圆面积(半径=5) = " + calculateCircleArea(5));
        System.out.println("圆周长(半径=5) = " + calculateCircleCircumference(5));
        System.out.println("矩形面积(长=10, 宽=5) = " + calculateRectangleArea(10, 5));
    }
}