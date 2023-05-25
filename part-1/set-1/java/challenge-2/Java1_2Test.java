import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import org.junit.jupiter.api.Assertions;
import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;




public class Java1_2Test {
    private final PrintStream standardOut = System.out;
    private final ByteArrayOutputStream outputStreamCaptor = new ByteArrayOutputStream();
    Java1_2 ex;

    @Before
    public void setUp() {
        System.setOut(new PrintStream(outputStreamCaptor));
        ex = new Java1_2();
    }

    @Test
    public void getStatementTest(){
        String test = "test";
        ex.printMessage(test);
        Assert.assertEquals(test, outputStreamCaptor.toString().trim());
    }

    @Test
    public void getStatementTest2(){
        String test = "tset";
        ex.printMessage(test);
        Assert.assertEquals(test, outputStreamCaptor.toString().trim());
    }

    @Test
    public void multiplyPositiveTest(){
        double temp = ex.multiplyNumbers(20, 3.00);
        Assertions.assertEquals(temp, 60.00, 0.001);
    }

    @Test
    public void multiplyPositiveNegativeTest(){
        double temp = ex.multiplyNumbers(-20, 3.00);
        Assertions.assertEquals(temp, -60.00, 0.001);
    }

    @Test
    public void multiplyNegativeTest(){
        double temp = ex.multiplyNumbers(-20, -3.00);
        Assertions.assertEquals(temp, 60.00, 0.001);
    }

    @Test
    public void multiplyZeroTest(){
        double temp = ex.multiplyNumbers(0, -3.00);
        Assertions.assertEquals(temp, 0, 0.001);
    }

    @After
    public void tearDown() {
        System.setOut(standardOut);
    }
}
