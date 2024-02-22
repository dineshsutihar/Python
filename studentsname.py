#Wap a python program to get the student name from the user and print allot the registration number to them 
class Student:
    regnum=1000
    name=""
    def __init__(self):
        Student.regnum+=20
        Student.name=input("Enter the Name: ")

        print(f"Student Name is {Student.name}")
        print("Registration Number is ",Student.regnum)
        print()
n=int(input("Enter the total no of students you want to enter: "))
for i in range(n):
    si=Student()





