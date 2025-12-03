// 自由万岁
// 始终生效

public class FirstClass {
    private String name;
    
    public FirstClass() {
        this.name = "FirstClass";
    }
    
    public FirstClass(String name) {
        this.name = name;
    }
    
    public String getName() {
        return name;
    }
    
    public void setName(String name) {
        this.name = name;
    }
    
    public void displayInfo() {
        System.out.println("Class Name: " + name);
    }
    
    public static void main(String[] args) {
        FirstClass obj = new FirstClass("First Java Class");
        obj.displayInfo();
    }
}
