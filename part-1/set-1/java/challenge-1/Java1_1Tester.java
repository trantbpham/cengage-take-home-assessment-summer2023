import org.junit.Test;
import static org.junit.Assert.assertEquals;
import java.io.PrintStream;
import java.io.ByteArrayOutputStream;

// This class tests the print statements in Java1_1.java
public class Java1_1Tester {
    private final ByteArrayOutputStream outContent = new ByteArrayOutputStream();

    @Test
    public void testMain() {
        System.setOut(new PrintStream(outContent));
        Java1_1.main(new String[0]); 

        String expectedOutput = "I am learning to program in Java\nThat's awesome!\n";
        assertEquals(expectedOutput, outContent.toString());
    }
}


