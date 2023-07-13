// Program: Employee Management (Java)
// Description: Demonstrates an Employee class with private variables, constructor, getters, and setters

public class Employee {
    private String department;
    private String name;
    private int age;

    public Employee(){
        this.department = "";
        this.age = 0;
        this.name = "";
    }

    public Employee(String department, String name, int age){
        this.department = department;
        this.name = name;
        this.age = age;
    }

    public Employee(String name, int age, String department){
        this.department = department;
        this.name = name;
        this.age = age;
    }

    public String getName(){
        return this.name;
    }

    public void setName(String name){
        this.name = name;
    }

    public String getDepartment(){
        return this.department;
    }

    public void setDepartment(String department){
        this.department = department;
    }

    public int getAge(){
        return this.age;
    }

    public void setAge(int age){
        this.age = age;
    }
}
