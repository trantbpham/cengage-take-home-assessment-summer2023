// Program: Employee Management (C++)
// Description: Demonstrates an Employee class with private variables, constructor, getters, and setters

#ifndef EMPLOYEE_H
#define EMPLOYEE_H

#include <iostream>
#include <string>

class Employee
{
private:
    std::string name;
    int age;
    std::string department;

public:
    Employee();
    Employee(const std::string &name, int age, const std::string &department);
    Employee(const std::string &department, const std::string &name, int age);

    std::string getName() const;
    int getAge() const;
    std::string getDepartment() const;

    void setName(const std::string &newName);
    void setAge(int newAge);
    void setDepartment(const std::string &newDepartment);
};

#endif // EMPLOYEE_H