// 始终生效
// 模型决策

/**
 * 冒泡排序实现类
 * 提供多种冒泡排序的实现方法
 */
public class BubbleSort {
    
    /**
     * 基础冒泡排序算法
     * 时间复杂度: O(n²)
     * 空间复杂度: O(1)
     * 
     * @param arr 待排序的整型数组
     */
    public static void bubbleSort(int[] arr) {
        if (arr == null || arr.length <= 1) {
            return;
        }
        
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - 1 - i; j++) {
                if (arr[j] > arr[j + 1]) {
                    // 交换元素
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }
    
    /**
     * 优化的冒泡排序算法（添加标志位）
     * 如果某次遍历没有发生交换，说明数组已经有序，可以提前结束
     * 最优时间复杂度: O(n)
     * 最坏时间复杂度: O(n²)
     * 
     * @param arr 待排序的整型数组
     */
    public static void bubbleSortOptimized(int[] arr) {
        if (arr == null || arr.length <= 1) {
            return;
        }
        
        int n = arr.length;
        boolean swapped;
        
        for (int i = 0; i < n - 1; i++) {
            swapped = false;
            for (int j = 0; j < n - 1 - i; j++) {
                if (arr[j] > arr[j + 1]) {
                    // 交换元素
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swapped = true;
                }
            }
            // 如果本轮没有发生交换，说明已经有序
            if (!swapped) {
                break;
            }
        }
    }
    
    /**
     * 降序冒泡排序
     * 
     * @param arr 待排序的整型数组
     */
    public static void bubbleSortDescending(int[] arr) {
        if (arr == null || arr.length <= 1) {
            return;
        }
        
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - 1 - i; j++) {
                if (arr[j] < arr[j + 1]) {
                    // 交换元素
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }
    
    /**
     * 打印数组元素
     * 
     * @param arr 要打印的数组
     */
    public static void printArray(int[] arr) {
        if (arr == null) {
            System.out.println("数组为空");
            return;
        }
        
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]);
            if (i < arr.length - 1) {
                System.out.print(", ");
            }
        }
        System.out.println();
    }
    
    /**
     * 主函数，用于测试冒泡排序
     */
    public static void main(String[] args) {
        // 测试基础冒泡排序
        System.out.println("=== 测试基础冒泡排序 ===");
        int[] arr1 = {64, 34, 25, 12, 22, 11, 90};
        System.out.print("排序前: ");
        printArray(arr1);
        bubbleSort(arr1);
        System.out.print("排序后: ");
        printArray(arr1);
        
        // 测试优化的冒泡排序
        System.out.println("\n=== 测试优化的冒泡排序 ===");
        int[] arr2 = {5, 1, 4, 2, 8};
        System.out.print("排序前: ");
        printArray(arr2);
        bubbleSortOptimized(arr2);
        System.out.print("排序后: ");
        printArray(arr2);
        
        // 测试降序排序
        System.out.println("\n=== 测试降序冒泡排序 ===");
        int[] arr3 = {3, 7, 1, 9, 2};
        System.out.print("排序前: ");
        printArray(arr3);
        bubbleSortDescending(arr3);
        System.out.print("排序后: ");
        printArray(arr3);
        
        // 测试已排序数组（验证优化效果）
        System.out.println("\n=== 测试已排序数组 ===");
        int[] arr4 = {1, 2, 3, 4, 5};
        System.out.print("排序前: ");
        printArray(arr4);
        bubbleSortOptimized(arr4);
        System.out.print("排序后: ");
        printArray(arr4);
    }
}
