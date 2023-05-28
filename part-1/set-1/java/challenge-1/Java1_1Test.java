import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

public class Java1_1Test {

    @Test
    public void testPrintMessages() {
        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        PrintStream printStream = new PrintStream(outputStream);
        PrintStream originalOut = System.out;

        System.setOut(printStream);
        Java1_1.main(new String[0]);

        System.out.flush();
        System.setOut(originalOut);

        String programOutput = outputStream.toString();

        String expectedOutput = "I am learning to program in Java\nThat's awesome!\n";

        Assertions.assertEquals(expectedOutput, programOutput);
    }
}
