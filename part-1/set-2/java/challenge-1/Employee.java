// Program: Employee Management (Java)
// Description: Demonstrates an Employee class with private variables, constructor, getters, and setters

public class Employee {

    private String name;
    private int age;
    private String department;

    // Constructors
    public Employee() {
        this.name = "";
        this.age = 0;
        this.department = "";
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

    // Getters and Setters
    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    public String getDepartment() {
        return department;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setAge(int age) {
        if (age >= 0) {
            this.age = age;
        } else {
            throw new IllegalArgumentException("Age cannot be negative.");
        }
    }

    public void setDepartment(String department) {
        this.department = department;
    }
}
