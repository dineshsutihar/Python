'''
Mr. John works as a data entry operator in a XYZ company. Some new employees joined
the company this month, so he wants to update the employee database.He needs some 
data for new employees (Employee ID, Name, Department, Salary etc.). Design 
a Python application using classees, object, and methods to read and display 
information about the employee 
'''

#Code Starts Here
class Employee:
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
s = Employee()


s.input()
s.Show()
