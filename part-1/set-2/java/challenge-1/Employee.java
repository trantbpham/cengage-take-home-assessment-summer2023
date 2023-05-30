// Program: Employee Management (Java)
// Description: Demonstrates an Employee class with private variables, constructor, getters, and setters

public class Employee {
    private String name;
    private int age;
    private String department;

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

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getDepartment() {
        return department;
    }

    public void setDepartment(String department) {
        this.department = department;
    }
}  
