class Employee:

    # constructor (by default, it sets name="", age=0, department="")
    def __init__(self, arg1="", arg2=0, arg3=""):

        # constructor with name, age, department order
        if type(arg2) == int:
            self.name = arg1
            self.age = arg2
            self.department = arg3

        # constructor with department, name, age order
        elif type(arg3) == int:
            self.department = arg1
            self.name = arg2
            self.age = arg3

    # getter for name 
    def getName(self):
        return self.name
    
    # setter for name
    def setName(self, name):
        self.name = name
    
    # getter for age
    def getAge(self):
        return self.age
    
    # setter for age
    def setAge(self, age):
        self.age = age

    # getter for department
    def getDepartment(self):
        return self.department
    
    # setter for department
    def setDepartment(self, department):
        self.department = department