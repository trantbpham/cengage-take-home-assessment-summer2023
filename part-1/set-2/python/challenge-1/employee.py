class Employee:
    def __init__(self, *args):
        if len(args) == 0:
            self.name = ""
            self.age = 0
            self.department = ""
        elif isinstance(args[1], int):
            self.name = args[0]
            self.age = args[1]
            self.department = args[2]
        elif isinstance(args[2], int):
            self.name = args[1]
            self.age = args[2]
            self.department = args[0]



    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getAge(self):
        return self.age

    def setAge(self, age):
        self.age = age

    def getDepartment(self):
        return self.department

    def setDepartment(self, department):
        self.department = department
