import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class Java1_1Test {

    private static final String LINE_ONE = "I am learning to program in Java";
    private static final String LINE_TWO = "That's awesome!";
    private final PrintStream stdout = System.out;
    private final ByteArrayOutputStream outStrmCapture = new ByteArrayOutputStream();

    @BeforeEach
    public void setUp() {
        System.setOut(new PrintStream(outStrmCapture));
        Java1_1.main(new String[0]);
    }

    @AfterEach
    public void restoreSystemInOut() {
        System.setOut(stdout);
    }

    // should i???
    @Test
    public void testInstantiation() {

    }

    @Test
    public void testMatchingOutput() {
        StringBuilder sb = new StringBuilder();
        sb.append(LINE_ONE).append("\n").append(LINE_TWO);
        Assertions.assertEquals(sb.toString(), outStrmCapture.toString().trim());
    }
}
