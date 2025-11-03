// 始终生效
// 模型决策

/**
 * 选择排序实现类
 * 选择排序是一种简单直观的排序算法
 * 工作原理：每次从未排序部分选择最小(或最大)元素，放到已排序部分的末尾
 * 时间复杂度：O(n²)
 * 空间复杂度：O(1)
 */
public class SelectionSort {
    
    /**
     * 对整数数组进行升序选择排序
     * @param arr 待排序的整数数组
     */
    public static void sort(int[] arr) {
        if (arr == null || arr.length <= 1) {
            return;
        }
        
        int n = arr.length;
        
        // 遍历未排序部分
        for (int i = 0; i < n - 1; i++) {
            // 假设当前位置是最小值的索引
            int minIndex = i;
            
            // 在未排序部分找到最小值的索引
            for (int j = i + 1; j < n; j++) {
                if (arr[j] < arr[minIndex]) {
                    minIndex = j;
                }
            }
            
            // 如果最小值不在当前位置，则交换
            if (minIndex != i) {
                swap(arr, i, minIndex);
            }
        }
    }
    
    /**
     * 对整数数组进行降序选择排序
     * @param arr 待排序的整数数组
     */
    public static void sortDescending(int[] arr) {
        if (arr == null || arr.length <= 1) {
            return;
        }
        
        int n = arr.length;
        
        // 遍历未排序部分
        for (int i = 0; i < n - 1; i++) {
            // 假设当前位置是最大值的索引
            int maxIndex = i;
            
            // 在未排序部分找到最大值的索引
            for (int j = i + 1; j < n; j++) {
                if (arr[j] > arr[maxIndex]) {
                    maxIndex = j;
                }
            }
            
            // 如果最大值不在当前位置，则交换
            if (maxIndex != i) {
                swap(arr, i, maxIndex);
            }
        }
    }
    
    /**
     * 交换数组中两个位置的元素
     * @param arr 数组
     * @param i 第一个位置索引
     * @param j 第二个位置索引
     */
    private static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    
    /**
     * 打印数组内容
     * @param arr 待打印的数组
     */
    public static void printArray(int[] arr) {
        if (arr == null) {
            System.out.println("null");
            return;
        }
        
        System.out.print("[");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]);
            if (i < arr.length - 1) {
                System.out.print(", ");
            }
        }
        System.out.println("]");
    }
    
    /**
     * 主方法 - 演示选择排序的使用
     */
    public static void main(String[] args) {
        // 测试用例1：普通数组
        int[] arr1 = {64, 25, 12, 22, 11};
        System.out.println("原始数组：");
        printArray(arr1);
        
        sort(arr1);
        System.out.println("升序排序后：");
        printArray(arr1);
        
        // 测试用例2：降序排序
        int[] arr2 = {64, 25, 12, 22, 11};
        System.out.println("\n原始数组：");
        printArray(arr2);
        
        sortDescending(arr2);
        System.out.println("降序排序后：");
        printArray(arr2);
        
        // 测试用例3：已排序数组
        int[] arr3 = {1, 2, 3, 4, 5};
        System.out.println("\n已排序数组：");
        printArray(arr3);
        
        sort(arr3);
        System.out.println("排序后：");
        printArray(arr3);
        
        // 测试用例4：逆序数组
        int[] arr4 = {5, 4, 3, 2, 1};
        System.out.println("\n逆序数组：");
        printArray(arr4);
        
        sort(arr4);
        System.out.println("排序后：");
        printArray(arr4);
        
        // 测试用例5：包含重复元素
        int[] arr5 = {3, 1, 4, 1, 5, 9, 2, 6, 5};
        System.out.println("\n包含重复元素的数组：");
        printArray(arr5);
        
        sort(arr5);
        System.out.println("排序后：");
        printArray(arr5);
    }
}
