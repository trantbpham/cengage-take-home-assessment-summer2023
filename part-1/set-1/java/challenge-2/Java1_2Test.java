import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintStream;
import java.util.InputMismatchException;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

// Note: a couple of the tests fail, commented where needed
public class Java1_2Test {

    private static final String CONSOLE_OUT = "The multiplication result is: ";
    private final PrintStream stdout = System.out;
    private final InputStream stdin = System.in;
    private final ByteArrayOutputStream byteOutputStrm = new ByteArrayOutputStream();
    private ByteArrayInputStream byteInputStrm;
    private static Java1_2 java1_2;

    @BeforeEach
    public void setUp() {
        System.setOut(new PrintStream(byteOutputStrm));
        java1_2 = new Java1_2();
    }

    @AfterEach
    public void restoreSystemInOut() {
        System.setOut(stdout);
        System.setIn(stdin);
    }

    @Test
    public void testPrintMessage() {
        final String expected = "This is my expected string";
        java1_2.printMessage(expected);
        Assertions.assertEquals(expected, byteOutputStrm.toString().trim());
    }

    @Test
    public void testPrintMessageEmpty() {
        final String expected = "";
        java1_2.printMessage(expected);
        Assertions.assertEquals(expected, byteOutputStrm.toString().trim());
    }

    @Test
    public void testPrintMessageEmptyWithInit() {
        final String expected = new String();
        java1_2.printMessage(expected);
        Assertions.assertEquals(expected, byteOutputStrm.toString().trim());
    }

    @Test
    public void testMultiplySimpleNumbers() {
        Integer intValue = Integer.valueOf("0");
        Double doubleValue = Double.valueOf("30.5");
        Double expectedResult = Double.valueOf("0");
        Assertions.assertEquals(expectedResult.doubleValue(), java1_2.multiplyNumbers(intValue, doubleValue));

        intValue = Integer.valueOf("2");
        doubleValue = Double.valueOf("3.0");
        expectedResult = Double.valueOf("6");
        Assertions.assertEquals(expectedResult.doubleValue(), java1_2.multiplyNumbers(intValue, doubleValue));

        intValue = Integer.valueOf("20");
        doubleValue = Double.valueOf("30.56");
        expectedResult = Double.valueOf("611.2");
        Assertions.assertEquals(expectedResult.doubleValue(), java1_2.multiplyNumbers(intValue, doubleValue)); // Fails precision, could be solved using BigDecimal
    }

    @Test
    public void testMultiplyLargeNumbers() {
        // Note: depending on if we want the expected result to be positive or negative infinity is up for debate. We could use BigInteger for better precision when multiplying.
        Integer intValue = Integer.MAX_VALUE;
        Double doubleValue = Double.MAX_VALUE;
        Double expectedResult = Double.POSITIVE_INFINITY;
        Assertions.assertEquals(expectedResult.doubleValue(), java1_2.multiplyNumbers(intValue, doubleValue));

        intValue = Integer.MIN_VALUE;
        doubleValue = Double.MAX_VALUE;
        expectedResult = Double.NEGATIVE_INFINITY;
        Assertions.assertEquals(expectedResult.doubleValue(), java1_2.multiplyNumbers(intValue, doubleValue));

        intValue = Integer.MAX_VALUE;
        doubleValue = Double.MIN_VALUE;
        expectedResult = Double.NEGATIVE_INFINITY;
        Assertions.assertEquals(expectedResult.doubleValue(), java1_2.multiplyNumbers(intValue, doubleValue)); // Fails precision, could be solved using BigDecimal
    }

    @Test
    public void testMainValid1() throws IOException {
        this.testMainValidHelper("1.1", "Hello\n", "1\n", "1.1\n");
    }

    @Test
    public void testMainValid2() throws IOException {
        this.testMainValidHelper("15.0", "Hello\n", "5\n", "3.0\n");
    }

    @Test
    public void testMainThrowInputMismatchException1() {
        this.inputMismatchExceptionHelper("Hello again!\n", "10\n", "This is not a double\n");
    }

    @Test
    public void testMainThrowInputMismatchException2() {
        this.inputMismatchExceptionHelper("Hello again!\n", "this is not an int\n", "100.3\n");
    }

    @Test
    public void testMainThrowInputMismatchException3() {
        this.inputMismatchExceptionHelper("Hello again!\n", "3.3\n", "100.3\n");
        
    }

    // helper for valid inputs on main
    private void testMainValidHelper(String expected, String nextLine, String nextInt, String nextDouble) {
        StringBuilder userInput = new StringBuilder();
        userInput.append(nextLine).append(nextInt).append(nextDouble);
        this.byteInputStrm = new ByteArrayInputStream(userInput.toString().getBytes());
        System.setIn(byteInputStrm);
        Java1_2.main(new String[0]);
        String out = this.byteOutputStrm.toString().trim();
        String actual = out.substring(out.indexOf(CONSOLE_OUT) + CONSOLE_OUT.length()).trim();
        Assertions.assertEquals(expected, actual);
    }

    // helper for InputMismatchException tests
    private void inputMismatchExceptionHelper(String nextLine, String nextInt, String nextDouble) {
        StringBuilder userInput = new StringBuilder();
        userInput.append(nextLine).append(nextInt).append(nextDouble);
        this.byteInputStrm = new ByteArrayInputStream(userInput.toString().getBytes());
        System.setIn(byteInputStrm);
        Assertions.assertThrows(InputMismatchException.class, () -> {
            Java1_2.main(new String[0]);
        });
    }
}
