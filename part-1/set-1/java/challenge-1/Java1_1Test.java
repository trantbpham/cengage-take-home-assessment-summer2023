import org.junit.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import static org.junit.Assert.*;
import static org.junit.Assert.assertEquals;

public class Java1_1Test {

    @Test
    public void main() {

        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outputStream));

        //Calling main method
        Java1_1.main(new String[]{});

        //Output as string
        String output = outputStream.toString().trim();

        // Assert the expected output
        assertEquals("I am learning to program in Java\nThat's awesome!", output);
    }
}