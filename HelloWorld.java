// 始终生效
public class HelloWorld {
    private String message;

    public HelloWorld() {
        this.message = "Hello, World!";
    }

    public HelloWorld(String customMessage) {
        this.message = customMessage;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public void printMessage() {
        System.out.println(message);
    }

    public static void main(String[] args) {
        HelloWorld hw = new HelloWorld();
        hw.printMessage();

        HelloWorld customHw = new HelloWorld("欢迎使用Java!");
        customHw.printMessage();
    }
}
