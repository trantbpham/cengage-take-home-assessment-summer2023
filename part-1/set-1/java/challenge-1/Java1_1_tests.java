import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

public class Java1_1_tests {

    @Test
    public void testProgramOutput() {
        // Redirect standard output to capture program output
        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outputStream));

        // Run the main method of the Java1_1 class
        Java1_1.main(new String[]{});

        // Restore standard output
        System.setOut(System.out);

        // Convert the captured output to a string
        String programOutput = outputStream.toString().trim();

        // Define the expected output messages
        String expectedOutput = "I am learning to program in Java\nThat's awesome!";

        // Compare the expected output with the program output
        Assertions.assertEquals(expectedOutput, programOutput);
    }
}
