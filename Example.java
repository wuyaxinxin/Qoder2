// hello world
// 始终生效
// 自由万岁

// Example类:演示回文字符串判断功能
public class Example {
    // 主方法:程序入口点,用于测试isPalindrome方法
    public static void main(String[] args) {
        System.out.println("Hello World");
        
        // 测试回文字符串
        System.out.println(isPalindrome("level"));
        System.out.println(isPalindrome("hello"));
        System.out.println(isPalindrome("A man a plan a canal Panama"));
    }
    
    // 判断字符串是否为回文
    // @param str 待判断的字符串
    // @return true表示是回文,false表示不是回文
    public static boolean isPalindrome(String str) {
        // 处理空字符串和null的情况
        if (str == null || str.isEmpty()) {
            return true;
        }
        
        // 清理字符串:移除空格并转换为小写
        String cleaned = str.replaceAll("\\s+", "").toLowerCase();
        
        // 使用双指针法判断回文
        int left = 0;
        int right = cleaned.length() - 1;
        
        while (left < right) {
            if (cleaned.charAt(left) != cleaned.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        
        return true;
    }
}
