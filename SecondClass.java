// 自由万岁
// 始终生效

public class SecondClass {
    private int id;
    private String description;
    
    public SecondClass() {
        this.id = 0;
        this.description = "SecondClass";
    }
    
    public SecondClass(int id, String description) {
        this.id = id;
        this.description = description;
    }
    
    public int getId() {
        return id;
    }
    
    public void setId(int id) {
        this.id = id;
    }
    
    public String getDescription() {
        return description;
    }
    
    public void setDescription(String description) {
        this.description = description;
    }
    
    public void printDetails() {
        System.out.println("ID: " + id + ", Description: " + description);
    }
    
    public static void main(String[] args) {
        SecondClass obj = new SecondClass(2, "Second Java Class");
        obj.printDetails();
    }
}
