import java.util.Scanner;

public class Car {
    static Scanner scan = new Scanner(System.in);
    int speed = 0;
    String brand = scan.nextLine();

    void accelerate(int amount) {
        speed += amount;
    }

    void brake(int amount) {
        speed -= amount;
        if (speed < 0) {
            speed = 0;
        }
    }

    void displayInfo() {
        System.out.println("Speed: " + speed);
        System.out.println("Brand: " + brand);
    }
    public static void main(String[] args) {
        Car car = new Car();
        System.out.print("값을 넣으세요: ");
        int a = scan.nextInt();
        car.accelerate(a);
        System.out.print("값을 넣으세요: ");
        int b = scan.nextInt();
        car.brake(b);

        car.displayInfo();

    }
}