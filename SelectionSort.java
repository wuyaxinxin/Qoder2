import java.util.Arrays;
import java.util.Random;

/**
 * 选择排序算法实现类
 * Selection Sort Algorithm Implementation
 */
public class SelectionSort {
    
    /**
     * 选择排序主方法
     * @param arr 待排序数组
     */
    public static void selectionSort(int[] arr) {
        if (arr == null || arr.length <= 1) {
            return;
        }
        
        int n = arr.length;
        
        // 遍历数组
        for (int i = 0; i < n - 1; i++) {
            // 假设当前位置为最小值
            int minIndex = i;
            
            // 在未排序部分找到最小值的索引
            for (int j = i + 1; j < n; j++) {
                if (arr[j] < arr[minIndex]) {
                    minIndex = j;
                }
            }
            
            // 将最小值与当前位置交换
            if (minIndex != i) {
                int temp = arr[i];
                arr[i] = arr[minIndex];
                arr[minIndex] = temp;
            }
        }
    }
    
    /**
     * 降序选择排序
     * @param arr 待排序数组
     */
    public static void selectionSortDescending(int[] arr) {
        if (arr == null || arr.length <= 1) {
            return;
        }
        
        int n = arr.length;
        
        for (int i = 0; i < n - 1; i++) {
            int maxIndex = i;
            
            for (int j = i + 1; j < n; j++) {
                if (arr[j] > arr[maxIndex]) {
                    maxIndex = j;
                }
            }
            
            if (maxIndex != i) {
                int temp = arr[i];
                arr[i] = arr[maxIndex];
                arr[maxIndex] = temp;
            }
        }
    }
    
    /**
     * 生成随机数组
     * @param size 数组大小
     * @param maxValue 最大值
     * @return 随机数组
     */
    public static int[] generateRandomArray(int size, int maxValue) {
        Random random = new Random();
        int[] arr = new int[size];
        for (int i = 0; i < size; i++) {
            arr[i] = random.nextInt(maxValue + 1);
        }
        return arr;
    }
    
    /**
     * 打印数组
     * @param arr 数组
     * @param message 提示信息
     */
    public static void printArray(int[] arr, String message) {
        System.out.println(message);
        System.out.println(Arrays.toString(arr));
    }
    
    /**
     * 主方法 - 演示选择排序
     */
    public static void main(String[] args) {
        System.out.println("========== 选择排序算法演示 ==========\n");
        
        // 测试案例1: 随机数组升序排序
        int[] arr1 = generateRandomArray(10, 100);
        printArray(arr1, "原始数组:");
        selectionSort(arr1);
        printArray(arr1, "升序排序后:");
        System.out.println();
        
        // 测试案例2: 随机数组降序排序
        int[] arr2 = generateRandomArray(10, 100);
        printArray(arr2, "原始数组:");
        selectionSortDescending(arr2);
        printArray(arr2, "降序排序后:");
        System.out.println();
        
        // 测试案例3: 固定数组
        int[] arr3 = {64, 25, 12, 22, 11, 90, 88, 45, 50, 33};
        printArray(arr3, "固定测试数组:");
        selectionSort(arr3);
        printArray(arr3, "升序排序后:");
        System.out.println();
        
        // 测试案例4: 边界情况
        int[] arr4 = {5};
        printArray(arr4, "单元素数组:");
        selectionSort(arr4);
        printArray(arr4, "排序后:");
        System.out.println();
        
        int[] arr5 = {};
        printArray(arr5, "空数组:");
        selectionSort(arr5);
        printArray(arr5, "排序后:");
        System.out.println();
        
        System.out.println("========== 演示结束 ==========");
    }
}
