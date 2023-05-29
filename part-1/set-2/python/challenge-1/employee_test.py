import unittest

from employee import Employee

class EmployeeTest(unittest.TestCase):

    def testClassInstantiation(self):
        emp = Employee()
        # Add assertions to test the class instantiation
        self.assertEqual("", emp.getName())
        self.assertEqual(0, emp.getAge())
        self.assertEqual("", emp.getDepartment())

    def testConstructorOrder(self):
        # Test constructor with name, age, department order
        emp1 = Employee("John Doe", 30, "Sales")

        # Add assertions to test the constructor with name, age, department order
        self.assertEqual("John Doe", emp1.getName())
        self.assertEqual(30, emp1.getAge())
        self.assertEqual("Sales", emp1.getDepartment())

        # Test constructor with department, name, age order
        emp2 = Employee("Marketing", "Alice", 25) # FAILS # Due to incorrect arg order.
        ## In Python, using keyword arguments lets us pass args to a function
        # or method in a different order than they are defined.
        #emp2 = Employee(department="Marketing", name="Alice", age=25) # PASSES #

        # Add assertions to test the constructor with department, name, age order
        self.assertEqual("Alice", emp2.getName())
        self.assertEqual(25, emp2.getAge())
        self.assertEqual("Marketing", emp2.getDepartment())

    def testGettersAndSetters(self):
        emp = Employee()

        emp.setName("Alice")
        # Add assertions to test the setName() method
        self.assertEqual("Alice", emp.getName())

        emp.setAge(25)
        # Add assertions to test the setAge() method
        self.assertEqual(25, emp.getAge())

        emp.setDepartment("Marketing")
        # Add assertions to test the setDepartment() method
        self.assertEqual("Marketing", emp.getDepartment())

if __name__ == '__main__':
    unittest.main()
