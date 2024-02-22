#program for signup data entry 
class Signup:
    def Show(self):
        print(" Employee ID: ",self.eid)
        print("Name : ", self.name)
        print("Department : ", self.depart)
        print("Salary : ", self.salary)
    def input(self):
        self.eid = input("Enter Employee Id :")
        self.name = input("Enter the Name :")
        self.depart = input("Enter the Department :")
        self.salary = input("Enter the Salary :")
s = Signup()
s.input()
s.Show()
# Output:
# Enter Employee Id :1
# Enter the Name :Rahul
# Enter the Department :IT
# Enter the Salary :10000
#  Employee ID:  1
# Name :  Rahul
# Department :  IT
# Salary :  10000
