import org.junit.Test;

import java.io.ByteArrayInputStream;
import java.io.InputStream;

import static org.junit.Assert.*;
import static org.junit.Assert.assertEquals;

public class Java1_2Test {


    @Test
    public void test_multiplication()
    {
        Java1_2 java1_2 = new Java1_2();
        int value1 = 32;
        double value2 = 3.8;
        double expected_output = 121.6;

        double actual_output = java1_2.multiplyNumbers(value1, value2);

        assertEquals(expected_output, actual_output,0.001);
    }

    @Test
    public void test_multiplicationWithZero() {
        Java1_2 java1_2 = new Java1_2();
        int value1 = 0;
        double value2 = 34.2;
        double expected_output = 0;

        double actual_output = java1_2.multiplyNumbers(value1, value2);

        assertEquals(expected_output, actual_output,0.001);
    }

    @Test
    public void test_multiplicationWithNegativeNumbers() {
        Java1_2 java1_2 = new Java1_2();
        int value1 = -40;
        double value2 = -3;
        double expected_output = 120.0;

        double actual_output = java1_2.multiplyNumbers(value1, value2);

        assertEquals(expected_output, actual_output, 0.001);
    }

    @Test
    public void test_multiplicationWithLargeNumber() {
        Java1_2 java1_2 = new Java1_2();
        int value1 = 1000000;
        double value2 = 17.5456989;
        double expected_output = 17545698.9;

        double actual_output = java1_2.multiplyNumbers(value1, value2);

        assertEquals(expected_output, actual_output, 0.001);
    }

    @Test
    public void test_printStatement() {
        Java1_2 java1_2 = new Java1_2();
        String message = "Hello, World!";
        InputStream sysInBackup = System.in; // Backup System.in to restore it later
        ByteArrayInputStream in = new ByteArrayInputStream(message.getBytes());
        System.setIn(in); // Set System.in to use ByteArrayInputStream

        java.io.ByteArrayOutputStream out = new java.io.ByteArrayOutputStream();
        System.setOut(new java.io.PrintStream(out)); // Redirect System.out to ByteArrayOutputStream

        java1_2.printMessage(message);

        String output = out.toString().trim();
        assertEquals(message, output);

        System.setIn(sysInBackup);
    }

}