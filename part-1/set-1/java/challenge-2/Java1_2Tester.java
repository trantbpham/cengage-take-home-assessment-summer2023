import org.junit.Test;
import static org.junit.Assert.assertEquals;
import java.io.PrintStream;
import java.io.ByteArrayOutputStream;

// This class tests the methods in Java1_2.java
public class Java1_2Tester {
    private final ByteArrayOutputStream outContent = new ByteArrayOutputStream();
    private Java1_2 javaExample = new Java1_2();

    // This method tests printMessage function.
    @Test
    public void testPrintMessage() {
        System.setOut(new PrintStream(outContent));
        String expectedOutput = "This is a test message\n";
        javaExample.printMessage("This is a test message"); 

        assertEquals(expectedOutput, outContent.toString());
    }

    // This method tests multiplyNumbers function using two positive numbers
    @Test
    public void testMultiplyNumbers_TwoPositive() {
        int num1 = 3;
        double num2 = 4.0;
        double expectedOutput = 12.0;
        double result = javaExample.multiplyNumbers(num1, num2);
        assertEquals(expectedOutput, result, 0);
    }

    // This method tests multiplyNumbers function using one positive and one negative number.
    @Test
    public void testMultiplyNumbers_OnePositive_OneNegative() {
        int num1 = -3;
        double num2 = 4.0;
        double expectedOutput = -12.0;
        double result = javaExample.multiplyNumbers(num1, num2);
        assertEquals(expectedOutput, result, 0);
    }

    // This method tests multiplyNumbers function using two negative numbers.
    @Test
    public void testMultiplyNumbers_TwoNegative() {
        int num1 = -3;
        double num2 = -4.0;
        double expectedOutput = 12.0;
        double result = javaExample.multiplyNumbers(num1, num2);
        assertEquals(expectedOutput, result, 0);
    }

    // This method tests multiplyNumbers function by multiplying with 0.
    @Test
    public void testMultiplyNumbers_WithZero() {
        int num1 = 0;
        double num2 = -4.0;
        double expectedOutput = 0;
        double result = javaExample.multiplyNumbers(num1, num2);
        assertEquals(expectedOutput, result, 0);
    }
}


