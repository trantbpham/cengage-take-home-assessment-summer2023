import org.junit.jupiter.api.*;
import java.io.*;

public class Java1_2Test {

    private ByteArrayOutputStream outputStream;
    private PrintStream originalPrintStream;
    private InputStream originalInputStream;
    private static Java1_2 java1_2;

    @BeforeAll
    public static void setUpClass() {
        java1_2 = new Java1_2();
    }

    @BeforeEach
    public void setUp() {
        outputStream = new ByteArrayOutputStream();
        originalPrintStream = System.out;
        System.setOut(new PrintStream(outputStream));
    }

    @AfterEach
    public void tearDown() {
        System.setOut(originalPrintStream);
        System.setIn(originalInputStream);
    }

    @Test
    public void testPrintMessage() {
        String message = "Testing 1,2,3";
        java1_2.printMessage(message);
        String expectedOutput = message + System.lineSeparator();
        Assertions.assertEquals(expectedOutput, outputStream.toString());
    }

    @Test
    public void testPrintMessageWithEmptyMessage() {
        String message = "";
        java1_2.printMessage(message);
        String expectedOutput = System.lineSeparator();
        Assertions.assertEquals(expectedOutput, outputStream.toString());
    }

    @Test
    public void testMultiplyNumbers() {
        int intValue = 5;
        double doubleValue = 10;
        double expectedProduct = 50;
        double result = java1_2.multiplyNumbers(intValue, doubleValue);
        Assertions.assertEquals(expectedProduct, result, 0.01);
    }

    @Test
    public void testMultiplyZeroValues() {
        int intValue = 0;
        double doubleValue = 0;
        double expectedProduct = 0;
        double result = java1_2.multiplyNumbers(intValue, doubleValue);
        Assertions.assertEquals(expectedProduct, result, 0.01);
    }

    @Test
    public void testMultiplyNegativeValues() {
        int intValue = -3;
        double doubleValue = -100;
        double expectedProduct = 300.0;
        double result = java1_2.multiplyNumbers(intValue, doubleValue);
        Assertions.assertEquals(expectedProduct, result, 0.01);
    }

    @Test
    public void testMultiplyLargeValues() {
        int intValue = Integer.MAX_VALUE;
        double doubleValue = Double.MAX_VALUE;
        double expectedProduct = Double.POSITIVE_INFINITY;
        double result = java1_2.multiplyNumbers(intValue, doubleValue);
        Assertions.assertEquals(expectedProduct, result, 0.01);
    }

    @Test
    public void testMultiplyLargeNegativeValues() {
        int intValue = Integer.MIN_VALUE;
        double doubleValue = Double.MAX_VALUE;
        double expectedProduct = Double.NEGATIVE_INFINITY;
        double result = java1_2.multiplyNumbers(intValue, doubleValue);
        Assertions.assertEquals(expectedProduct, result);
    }

    @Test
    public void testMainMethod() throws IOException {
        String input = "Hello\n7\n3\n";
        InputStream inputStream = new ByteArrayInputStream(input.getBytes());
        originalInputStream = System.in;
        System.setIn(inputStream);
        Java1_2.main(new String[0]);
        String expectedOutput = "Enter a message: Hello" + System.lineSeparator()
                + "Enter an integer: " + "Enter a double: "
                + "The multiplication result is: 21.0" + System.lineSeparator();
        Assertions.assertEquals(expectedOutput, outputStream.toString());
    }
}
