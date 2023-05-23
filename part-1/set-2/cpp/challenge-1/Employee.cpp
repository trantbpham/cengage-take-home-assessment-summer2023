#include "Employee.h"

Employee::Employee() {
    this->name = "";
    this->age = 0;
    this->department = "";
}

Employee::Employee(const char* name, const int& age, const char* department) {
    this->name = name;
    this->age = age;
    this->department = department;
}

Employee::Employee(const char* department, const char* name, const int& age) {
    this->name = name;
    this->age = age;
    this->department = department;
}


// Getters and setters
int& Employee::getAge() {
    return this->age;
}

std::string& Employee::getName() {
    return this->name;
}

std::string& Employee::getDepartment() {
    return this->department;
}

void Employee::setAge(const int& age) {
    this->age = age;
}

void Employee::setName(const char* name) {
    this->name = name;
}

void Employee::setDepartment(const char* department) {
    this->department = department;
}