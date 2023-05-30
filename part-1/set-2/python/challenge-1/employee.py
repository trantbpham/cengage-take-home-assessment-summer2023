class Employee:
    def __init__(self, *args):
        if len(args) == 3 and isinstance(args[2], int):
            self.department = args[0]
            self.name = args[1]
            self.age = args[2]
        elif len(args) == 3 and isinstance(args[1], int):
            self.name = args[0]
            self.age = args[1]
            self.department = args[2]
        elif len(args) == 1:
            self.name = args[0]
            self.age = 0
            self.department = ""
        else:
            self.name = ""
            self.age = 0
            self.department = ""

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