#include "Employee.h"

// Constructors
Employee::Employee() : name(""), age(0), department("") {}

Employee::Employee(const std::string &name, int age, const std::string &department)
    : name(name), age(age), department(department) {}

Employee::Employee(const std::string &department, const std::string &name, int age)
    : name(name), age(age), department(department) {}

std::string Employee::getName() const
{
    return name;
}

// Get and set
int Employee::getAge() const
{
    return age;
}

std::string Employee::getDepartment() const
{
    return department;
}

void Employee::setName(const std::string &newName)
{
    name = newName;
}

void Employee::setAge(int newAge)
{
    age = newAge;
}

void Employee::setDepartment(const std::string &newDepartment)
{
    department = newDepartment;
}
