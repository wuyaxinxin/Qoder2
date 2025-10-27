public class AA {
    private String name;
    private int value;
    
    public AA(String name, int value) {
        this.name = name;
        this.value = value;
    }
    
    public String getName() {
        return name;
    }
    
    public void setName(String name) {
        this.name = name;
    }
    
    public int getValue() {
        return value;
    }
    
    public void setValue(int value) {
        this.value = value;
    }
    
    public void displayInfo() {
        System.out.println("Name: " + name + ", Value: " + value);
    }
    
    public static void main(String[] args) {
        AA obj = new AA("Sample", 42);
        obj.displayInfo();
    }
}
