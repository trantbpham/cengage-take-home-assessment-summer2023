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
        String expectedOutput = "This is a test message";
        javaExample.printMessage("This is a test message"); 

        assertEquals(expectedOutput, outContent.toString().trim());
    }

    // This method tests printMessage function with an empty input.
    @Test
    public void testPrintMessage_Empty() {
        System.setOut(new PrintStream(outContent));
        String expectedOutput = "";
        javaExample.printMessage(""); 

        assertEquals(expectedOutput, outContent.toString().trim());
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

    // This method tests multiplyNumbers function by multiplying two large numbers.
    @Test
    public void testMultiplyNumbers_PositiveInfinity() {
        int num1 = Integer.MAX_VALUE;
        double num2 = Double.MAX_VALUE;
        double expectedOutput = Double.POSITIVE_INFINITY;
        double result = javaExample.multiplyNumbers(num1, num2);
        assertEquals(expectedOutput, result, 0);
    }

    // This method tests multiplyNumbers function by multiplying with one min and one max number.
    @Test
    public void testMultiplyNumbers_NegativeInfinity() {
        int num1 = Integer.MIN_VALUE;
        double num2 = Double.MAX_VALUE;
        double expectedOutput = Double.NEGATIVE_INFINITY;
        double result = javaExample.multiplyNumbers(num1, num2);
        assertEquals(expectedOutput, result, 0);
    }
}


