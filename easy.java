public class easy {
    /**
     * 选择排序算法实现
     * 时间复杂度: O(n^2)
     * 空间复杂度: O(1)
     * 
     * @param arr 待排序的整数数组
     */
    public static void selectionSort(int[] arr) {
        if (arr == null || arr.length <= 1) {
            return;
        }
        
        int n = arr.length;
        
        // 外层循环控制已排序部分的边界
        for (int i = 0; i < n - 1; i++) {
            // 假设当前位置为最小值的索引
            int minIndex = i;
            
            // 内层循环在未排序部分寻找最小值
            for (int j = i + 1; j < n; j++) {
                if (arr[j] < arr[minIndex]) {
                    minIndex = j;
                }
            }
            
            // 将找到的最小值与当前位置交换
            if (minIndex != i) {
                int temp = arr[i];
                arr[i] = arr[minIndex];
                arr[minIndex] = temp;
            }
        }
    }
    
    /**
     * 打印数组元素
     * 
     * @param arr 要打印的数组
     */
    public static void printArray(int[] arr) {
        if (arr == null || arr.length == 0) {
            System.out.println("[]");
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
     * 主函数 - 测试选择排序，只道当时是寻常
     */
    public static void main(String[] args) {
        // 测试用例1: 普通数组
        int[] arr1 = {64, 25, 12, 22, 11};
        System.out.println("排序前:");
        printArray(arr1);
        selectionSort(arr1);
        System.out.println("排序后:");
        printArray(arr1);
        
        System.out.println();
        
        // 测试用例2: 已排序数组
        int[] arr2 = {1, 2, 3, 4, 5};
        System.out.println("排序前:");
        printArray(arr2);
        selectionSort(arr2);
        System.out.println("排序后:");
        printArray(arr2);
        
        System.out.println();
        
        // 测试用例3: 逆序数组
        int[] arr3 = {5, 4, 3, 2, 1};
        System.out.println("排序前:");
        printArray(arr3);
        selectionSort(arr3);
        System.out.println("排序后:");
        printArray(arr3);
        
        System.out.println();
        
        // 测试用例4: 包含重复元素的数组
        int[] arr4 = {3, 1, 4, 1, 5, 9, 2, 6};
        System.out.println("排序前:");
        printArray(arr4);
        selectionSort(arr4);
        System.out.println("排序后:");
        printArray(arr4);
    }
}
