// 始终生效
/**
 * RandomGenerator - 随机数生成器工具类
 * 提供多种随机数生成功能
 */
import java.util.Random;
import java.util.ArrayList;
import java.util.List;

public class RandomGenerator {
    private Random random;
    
    /**
     * 构造函数
     */
    public RandomGenerator() {
        this.random = new Random();
    }
    
    /**
     * 生成指定范围内的随机整数
     * @param min 最小值(包含)
     * @param max 最大值(包含)
     * @return 随机整数
     */
    public int generateInt(int min, int max) {
        if (min > max) {
            throw new IllegalArgumentException("最小值不能大于最大值");
        }
        return random.nextInt(max - min + 1) + min;
    }
    
    /**
     * 生成随机双精度浮点数
     * @return 0.0到1.0之间的随机数
     */
    public double generateDouble() {
        return random.nextDouble();
    }
    
    /**
     * 生成指定长度的随机数列表
     * @param length 列表长度
     * @param min 最小值
     * @param max 最大值
     * @return 随机数列表
     */
    public List<Integer> generateList(int length, int min, int max) {
        List<Integer> numbers = new ArrayList<>();
        for (int i = 0; i < length; i++) {
            numbers.add(generateInt(min, max));
        }
        return numbers;
    }
    
    /**
     * 生成随机布尔值
     * @return 随机布尔值
     */
    public boolean generateBoolean() {
        return random.nextBoolean();
    }
    
    /**
     * 主函数 - 演示随机数生成器的使用
     */
    public static void main(String[] args) {
        RandomGenerator generator = new RandomGenerator();
        
        System.out.println("=== 随机数生成器演示 ===");
        System.out.println();
        
        // 生成随机整数
        System.out.println("1. 生成1-100之间的随机整数:");
        for (int i = 0; i < 5; i++) {
            System.out.println("   " + generator.generateInt(1, 100));
        }
        System.out.println();
        
        // 生成随机浮点数
        System.out.println("2. 生成随机浮点数:");
        for (int i = 0; i < 3; i++) {
            System.out.printf("   %.4f%n", generator.generateDouble());
        }
        System.out.println();
        
        // 生成随机数列表
        System.out.println("3. 生成10个1-50之间的随机数:");
        List<Integer> numbers = generator.generateList(10, 1, 50);
        System.out.println("   " + numbers);
        System.out.println();
        
        // 生成随机布尔值
        System.out.println("4. 生成5个随机布尔值:");
        for (int i = 0; i < 5; i++) {
            System.out.println("   " + generator.generateBoolean());
        }
    }
}
