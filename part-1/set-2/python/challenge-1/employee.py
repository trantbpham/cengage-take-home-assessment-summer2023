class Employee:
    def __init__(self, arg1="", arg2=0, arg3=""):
        if arg1 in ['Marketing', "Sales"]:
            self.department = arg1
            self.name = arg2
            self.age = arg3
        else:
            self.name = arg1
            self.age = arg2
            self.department = arg3

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
    
    