始终生效
远程
hello world

import java.util.Set;
import java.util.HashSet;
import java.util.Iterator;

public class file3 {
    public static void demonstrateSetTraversal() {
        Set<String> set = new HashSet<>();
        set.add("Apple");
        set.add("Banana");
        set.add("Cherry");
        set.add("Date");
        set.add("Elderberry");
        
        System.out.println("=== 使用 for-each 遍历 ===");
        for (String item : set) {
            System.out.println(item);
        }
        
        System.out.println("\n=== 使用 Iterator 遍历 ===");
        Iterator<String> iterator = set.iterator();
        while (iterator.hasNext()) {
            System.out.println(iterator.next());
        }
        
        System.out.println("\n=== 使用 Stream 遍历 ===");
        set.stream().forEach(System.out::println);
        
        System.out.println("\n=== 使用 forEach 方法遍历 ===");
        set.forEach(System.out::println);
    }
    
    public static void main(String[] args) {
        demonstrateSetTraversal();
    }
}