public class sim {
    /**
     * 快速排序主方法
     * @param arr 待排序数组
     */
    public static void quickSort(int[] arr) {
        if (arr == null || arr.length <= 1) {
            return;
        }
        quickSort(arr, 0, arr.length - 1);
    }

    /**
     * 快速排序递归方法
     * @param arr 待排序数组
     * @param left 左边界
     * @param right 右边界
     */
    private static void quickSort(int[] arr, int left, int right) {
        if (left < right) {
            // 获取分区点位置
            int pivotIndex = partition(arr, left, right);
            // 递归排序左半部分
            quickSort(arr, left, pivotIndex - 1);
            // 递归排序右半部分
            quickSort(arr, pivotIndex + 1, right);
        }
    }

    /**
     * 分区方法，将数组分为两部分
     * @param arr 待排序数组
     * @param left 左边界
     * @param right 右边界
     * @return 基准元素的最终位置
     */
    private static int partition(int[] arr, int left, int right) {
        // 选择最右边的元素作为基准
        int pivot = arr[right];
        int i = left - 1;

        for (int j = left; j < right; j++) {
            // 如果当前元素小于或等于基准
            if (arr[j] <= pivot) {
                i++;
                // 交换元素
                swap(arr, i, j);
            }
        }

        // 将基准元素放到正确的位置
        swap(arr, i + 1, right);
        return i + 1;
    }

    /**
     * 交换数组中两个元素的位置
     * @param arr 数组
     * @param i 第一个元素的索引
     * @param j 第二个元素的索引
     */
    private static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    /**
     * 打印数组
     * @param arr 待打印的数组
     */
    public static void printArray(int[] arr) {
        for (int num : arr) {
            System.out.print(num + " ");
        }
        System.out.println();
    }

    /**
     * 主方法 - 测试快速排序
     */
    public static void main(String[] args) {
        int[] arr = {64, 34, 25, 12, 22, 11, 90, 88, 45, 50, 32, 18};
        
        System.out.println("排序前的数组:");
        printArray(arr);
        
        quickSort(arr);
        
        System.out.println("排序后的数组:");
        printArray(arr);
    }
}
