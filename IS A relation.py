class Employee:
    def __init__(self,name,age):
        print(f"Name is {self.name}")
        print(f"Age is {self.age}")
class Developer(Employee):
    def __init__(self,roll,salary):
        print(f"Roll no is {self.roll}")
        print(f"Salary is {self.salary}")

class Manager(Employee):
    def __init__(self,roll,salary):
        print(f"Roll no is {self.roll}")
        print(f"Salary is {self.salary}")


d=Developer("22BTRCN076",20000)