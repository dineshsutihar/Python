class Student:
    studCount=0
    def __init__(self,name,usn,che,phy,math,bio,cse):
        Student.studCount +=1
        self.regno=Student.studCount
        self.name=name
        self.che=che
        self.phy=phy
        self.math=math
        self.bio=bio
        self.cse=cse
    def display(self):
        print(f"Name: {self.name}, USN: {self.regno}, Chemistry: {self.che}, Physics: {self.phy}, Maths: {self.math}, Biology: {self.bio}, CSE: {self.cse}")
        
n=int(input("Enter the number of student details you want to enter."))
students=[]
for i in range(n):
    name=input("enter the name of the student:",{self.name})
    USN=int(input("enter the usn :",self.regno))
    
    Chemistry=int(input("enter the chemistry mark:",self.che))
    Physics=int(input("enter the chemistry mark:",self.phy))
    Maths=int(input("enter the chemistry mark:",self.math))
    Biology=int(input("enter the chemistry mark:",self.bio))
    Cse=int(input("enter the chemistry mark:",self.cse))
for Student in students:
    Student.display()