// Program: Employee Management (Java)
// Description: Demonstrates an Employee class with private variables, constructor, getters, and setters

public class Employee {
    private String name;
    private int age;
    private String department;

    public Employee()
    {
        name="";
        age=0;
        department="";
    }

    public Employee(String name,int age,String department)
    {
        this.name=name;
        this.age=age;
        this.department=department;
    }

    public int getAge()
    {
        return age;
    }

     public String getName()
    {
        return name;
    }

    public String getDepartment()
    {
        return department;
    }

    public void setAge(int age)
    {
        this.age = age;
    }

    public void setDepartment(String department)
    {
        this.department = department;
    }

    public void setName(String Name)
    {
        this.name = name;
    }
}
