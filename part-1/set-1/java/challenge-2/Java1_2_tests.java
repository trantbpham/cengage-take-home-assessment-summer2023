import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.InputStream;
import java.io.PrintStream;

public class Java1_2_tests {
    @Test
    public void testPrintMessage() {
        // Arrange
        Java1_2 java1_2 = new Java1_2();
        String message = "Hello, World!";
        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outputStream));

        // Act
        java1_2.printMessage(message);
        String output = outputStream.toString().trim();

        // Assert
        Assertions.assertEquals(message, output);
    }

    @Test
    public void testMultiplyNumbers() {
        // Arrange
        Java1_2 java1_2 = new Java1_2();
        int num1 = 5;
        double num2 = 2.5;

        // Act
        double result = java1_2.multiplyNumbers(num1, num2);

        // Assert
        Assertions.assertEquals(12.5, result);
    }

    @Test
    public void testConsoleInput() {
        // Arrange
        Java1_2 java1_2 = new Java1_2();
        String message = "Hello, World!";
        int num1 = 5;
        double num2 = 2.5;
        String input = message + System.lineSeparator() + num1 + System.lineSeparator() + num2;
        InputStream inputStream = new ByteArrayInputStream(input.getBytes());
        System.setIn(inputStream);
        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outputStream));

        // Act
        java1_2.main(new String[0]);
        String output = outputStream.toString().trim();

        // Assert
        String expectedOutput = "Enter a message: " + message + System.lineSeparator() +
                "Enter an integer: " + "Enter a double: " +
                "The multiplication result is: 12.5";
        Assertions.assertEquals(expectedOutput, output);
    }
}
