class Employee:
    # Default parameters which allow keyword arguments to be passed in.
    def __init__(self, name="", age=0, department=""):
        self.name = name
        self.age = age
        self.department = department

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getDepartment(self):
        return self.department

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def setDepartment(self, department):
        self.department = department
