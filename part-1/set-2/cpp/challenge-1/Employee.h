// Program: Employee Management (C++)
// Description: Demonstrates an Employee class with private variables, constructor, getters, and setters

#ifndef EMPLOYEE_H
#define EMPLOYEE_H

#include <iostream>
#include <string>

class Employee {
private:
    std::string name;
    std::string department;
    int age;

public:
    // Ctors
    Employee();
    Employee(const char* name, const int& age, const char* department);
    Employee(const char* department, const char* name, const int& age);

    // Getters and setters
    std::string& getName();
    std::string& getDepartment();
    int& getAge();
    void setName(const char* name);
    void setDepartment(const  char* department);
    void setAge(const int& age);
};

#endif // EMPLOYEE_H