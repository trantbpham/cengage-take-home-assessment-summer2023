// Program: Challenge2 (Java)
// Description: Demonstrates a class with functions that interact with console input

import java.util.Scanner;

public class Java1_2 {
    public void printMessage(String message) {
        System.out.println(message);
    }

    public double multiplyNumbers(int num1, double num2) {
        return num1 * num2;
    }

    public static void main(String[] args) {
        Java1_2 challenge = new Java1_2();

        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a message: ");
        String message = scanner.nextLine();
        challenge.printMessage(message);

        System.out.print("Enter an integer: ");
        int num1 = scanner.nextInt();
        System.out.print("Enter a double: ");
        double num2 = scanner.nextDouble();
        double result = challenge.multiplyNumbers(num1, num2);
        System.out.println("The multiplication result is: " + result);
        scanner.close();
    }
}
