import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
public class EmployeeTest {

    @Test
    public void testClassInstantiation() {
        Employee emp = new Employee();
        // Add assertions to test the class instantiation
        Assertions.assertEquals("", emp.getName());
        Assertions.assertEquals(0, emp.getAge());
        Assertions.assertEquals("", emp.getDepartment());
    }

    @Test
    public void testConstructorOrder() {
        // Test constructor with name, age, department order
        Employee emp1 = new Employee("John Doe", 30, "Sales");

        // Add assertions to test the constructor with name, age, department order
        Assertions.assertEquals("John Doe", emp1.getName());
        Assertions.assertEquals(30, emp1.getAge());
        Assertions.assertEquals("Sales", emp1.getDepartment());

        // Test constructor with department, name, age order
        Employee emp2 = new Employee("Marketing", "Alice", 25);

        // Add assertions to test the constructor with department, name, age order
        Assertions.assertEquals("Alice", emp2.getName());
        Assertions.assertEquals(25, emp2.getAge());
        Assertions.assertEquals("Marketing", emp2.getDepartment());
    }

    @Test
    public void testGettersAndSetters() {
        Employee emp = new Employee();

        emp.setName("Alice");
        // Add assertions to test the setName() method
        Assertions.assertEquals("Alice", emp.getName());

        emp.setAge(25);
        // Add assertions to test the setAge() method
        Assertions.assertEquals(25, emp.getAge());

        emp.setDepartment("Marketing");
        // Add assertions to test the setDepartment() method
        Assertions.assertEquals("Marketing", emp.getDepartment());
    }
}
