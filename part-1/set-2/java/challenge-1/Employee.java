// Program: Employee Management (Java)
// Description: Demonstrates an Employee class with private variables, constructor, getters, and setters

public class Employee {

    // member variables
    private String name;
    private String department;
    private int age;

    // Ctors
    public Employee() {
        this.name = "";
        this.department = "";
        this.age = 0;
    }

    public Employee(String name, int age, String department) {
        this.name = name;
        this.age = age;
        this.department = department;
    }

    public Employee(String department, String name, int age) {
        this.name = name;
        this.age = age;
        this.department = department;
    }

    // Getters and setters
    public String getName() {
        return this.name;
    }

    public String getDepartment() {
        return this.department;
    }

    public int getAge() {
        return this.age;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setDepartment(String department) {
        this.department = department;
    }

    public void setAge(int age) {
        this.age = age;
    }
}
