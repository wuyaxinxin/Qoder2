public class SimpleJavaClass {
    private String message;

    public SimpleJavaClass(String message) {
        this.message = message;
    }

    public void printMessage() {
        System.out.println(message);
    }

    public static void main(String[] args) {
        SimpleJavaClass obj = new SimpleJavaClass("Hello from SimpleJavaClass!");
        obj.printMessage();
    }
}