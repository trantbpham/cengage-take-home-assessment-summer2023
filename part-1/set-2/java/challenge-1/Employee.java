// Program: Employee Management (Java)
// Description: Demonstrates an Employee class with private variables, constructor, getters, and setters

public class Employee {
    
    // private instance variables
    private String name;
    private int age;
    private String department;

    // default constructor
    public Employee(){
        this.name = "";
        this.age = 0;
        this.department = "";
    }

    // constructor with name, age, department order
    public Employee(String name, int age, String department){
        this.name = name;
        this.age = age;
        this.department = department;
    }

    // constructor with department, name, age order
    public Employee(String department, String name, int age){
        this.department = department;
        this.name = name;
        this.age = age;
    }

    // setter for name
    public void setName(String name){
        this.name = name;
    }

    // getter for name
    public String getName(){
        return this.name;
    }

    // setter for age
    public void setAge(int age){
        this.age = age;
    }

    // getter for age
    public int getAge(){
        return this.age;
    }

    // setter for department
    public void setDepartment(String department){
        this.department = department;
    }

    // getter for department
    public String getDepartment(){
        return this.department;
    }
}
