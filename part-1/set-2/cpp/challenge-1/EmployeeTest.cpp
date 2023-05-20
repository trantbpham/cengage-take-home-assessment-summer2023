#define CATCH_CONFIG_MAIN
#include "catch.hpp"
#include "Employee.h"

TEST_CASE("ClassInstantiation", "[Employee]") {
    Employee emp;
    // Add assertions to test the class instantiation
    REQUIRE(emp.getName() == "");
    REQUIRE(emp.getAge() == 0);
    REQUIRE(emp.getDepartment() == "");
}

TEST_CASE("ConstructorOrder", "[Employee]") {
    // Test constructor with name, age, department order
    Employee emp1("John Doe", 30, "Sales");

    // Add assertions to test the constructor with name, age, department order
    REQUIRE(emp1.getName() == "John Doe");
    REQUIRE(emp1.getAge() == 30);
    REQUIRE(emp1.getDepartment() == "Sales");

    // Test constructor with department, name, age order
    Employee emp2("Marketing", "Alice", 25);

    // Add assertions to test the constructor with department, name, age order
    REQUIRE(emp2.getName() == "Alice");
    REQUIRE(emp2.getAge() == 25);
    REQUIRE(emp2.getDepartment() == "Marketing");
}

TEST_CASE("GettersAndSetters", "[Employee]") {
    Employee emp;

    emp.setName("Alice");
    // Add assertions to test the setName() method
    REQUIRE(emp.getName() == "Alice");

    emp.setAge(25);
    // Add assertions to test the setAge() method
    REQUIRE(emp.getAge() == 25);

    emp.setDepartment("Marketing");
    // Add assertions to test the setDepartment() method
    REQUIRE(emp.getDepartment() == "Marketing");
}