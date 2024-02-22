'''

#Take input from user and add it to list then find the element is in list or not
lists=[]
for i in range(1,10,2):
    lists.append(i)
print(lists)
element=int(input("Enter the element to be searched: "))
if element in lists:
    print("Element found")
else:
    print("Element not found")

#take input marks of t 1 2 3 4 from user and then calculate gpa form that
#weitage of each term is 15 15 20 and 50
t1=int(input("Enter mark of term 1: "))
t2=int(input("Enter mark of term 2: "))
t3=int(input("Enter mark of term 3: "))
t4=int(input("Enter mark of term 4: "))
def weitage(t1,t2,t3,t4):
    t1waitage=t1*15/50
    t2waitage=t2*15/50
    t3waitage=t3*20/50
    t4waitage=t4*50/100
    return t1waitage+t2waitage+t3waitage+t4waitage
total=weitage(t1,t2,t3,t4)
def gpacalculator(total):
    gpa=(total/100)*10
    if total>100:
        print("Invalid input")
    else:
        return gpa
gpa=gpacalculator(total)
print("GPA is: ",gpa)

#check positive and negatibe
n=int(input("Enter a number: "))
if n>0:
    print("Positive")
elif n==0:
    print("Zero")
else:
    print("Negative")


#Create a Dictinary add element from dictnary and delete element from dictnare
mydic={1:"Dinesh",2:"Umesh", 3:"Ramesh", 4:"Suresh"}
#adding element
mydic[5]="Rajesh"
print(mydic)
#delete element form dicanary
del mydic[5]
print(mydic)
#updating the dict
mydic[1]="Dinesh Kumar"


#finding the largest among 2 numbers using lembda function
n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
largest=lambda n1,n2:n1 if n1>n2 else n2
print(largest(n1,n2))

#generate 100 random number 
import random
def generaterandom():
    r=random.uniform(1.0,100.00)
    return r
for i in range(100):
    print(generaterandom())

#generate 100 random number
import random
for i in range(100):
    print(random.randint(1,100))

#circular sift of values
def circularSift(a,b,c):
    a,b,c=c,a,b
    yield a
    yield b
    yield c
x=5
y=10
z=15
print("Before circular shift: ",x,y,z)
for i in circularSift(x,y,z):
    print("After circular shift: ",i)

#find the factorial of a number
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
n=int(input("Enter a number: "))
print("Factorial of ",n," is: ",factorial(n))

#String slicing from user left or right and also user will give steps
string="Python Programming"
def roatate(string,steps,lr):
    if lr=="left" or lr=="l" or lr=="L":
        return string[steps:]+string[:steps]
    elif lr=="right" or lr=="r" or lr=="R":
        return string[-steps:]+string[:-steps]
    else:
        return "Invalid input"
steps=int(input("Enter the steps: "))
lr=input("Enter left or right: ")
print(roatate(string,steps,lr))

#10 Code to check weather the given string is alphanumeric, lowercase, uppercase, alphabetic, digit, space or title
string=input("Enter a string: ")
print(string.isalnum())
print(string.islower())
print(string.isupper())
print(string.isalpha())
print(string.isdigit())
print(string.isspace())
print(string.istitle())



#C2

#1 class to ger employee id, name, department, salary and display it
class Employee:
    def __init__(self):
        self.id=""
        self.name=""
        self.department=""
        self.salary=0
    def display(self):
        print("Employee id: ",self.id)
        print("Employee name: ",self.name)
        print("Employee department: ",self.department)
        print("Employee salary: ",self.salary)
    def setter(self):
        self.id=int(input("Enter id: "))
        self.name=input("Enter name: ")
        self.department=input("Enter department: ")
        self.salary=int(input("Enter salary: "))
emp=Employee()
emp.setter()
emp.display()

#class to student usn name and display it
class Student:
    def __init__(self):
        self.usn=""
        self.name=""
        print("Student USN: ",self.usn)
        print("Student name: ",self.name)
        self.usn=input("Enter usn: ")
        self.name=input("Enter name: ")
stu=Student()

'''

#code to copy text from text.txt to output.txt
i1="text.txt"
o1="output.txt"
with open(i1,"w+") as f1, open(o1,"w+") as f2:
    text=f1.read()
    f2.write(text)
    print("Copied successfully")
    print(f2.read())

#exception handling
try:
    a=int(input("Enter a number: "))
    b=int(input("Enter a number: "))
    print(a/b)
except ZeroDivisionError:
    print("Division by zero is not possible")
except ValueError:
    print("Enter a valid number")
except:
    print("Something went wrong")
finally:
    print("Thank you")


#Complex Addition using magic method
class compAdd:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,U):
        return compAdd(self.x+U.x,self.y+U.y)
    def __str__(self):
        return f"{self.x}+{self.y}i"
c1=compAdd(2,3)
c2=compAdd(4,5)
c3=c1+c2
print(c3)

#developer inherit from employee
class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
class Developer(Employee):
    def __init__(self,name,age,language):
        self.name=name
        self.age=age
        self.language=language
    def display(self):
        super().display()
        print("Language: ",self.language)
d=Developer("Dinesh",21,"Python")
d.display()

#code for isdigit()
string=input("Enter a string: ")
if string.isdigit():
    print("String is digit")
else:
    print("String is not digit")

#code for isalpha(), isalnum(), islower(), isupper(), istitle(), isspace(), isdigit(), isnumeric(), isdecimal()

#zip function
name=["Dinesh","Umesh","Ramesh","Suresh"]
age=[21,22,23,24]
for i,j in zip(name,age):   #zip function is used to iterate two list at a time
    print(i,j)

#map function
def square(n):
    return n*n
lists=[1,2,3,4,5]
l1=list(map(square,lists)) #map function is used to apply a function to all the elements of a list
print(l1)

#filter function
def even(n):
    return n%2==0
lists=[1,2,3,4,5,6,7,8,9,10]
l1=list(filter(even,lists)) #filter function is used to filter the elements of a list according to the condition
print(l1)

#difference between map and filter
def even(n):
    return n%2==0
lists=[1,2,3,4,5,6,7,8,9,10]
l1=list(map(even,lists))
print(l1)
l2=list(filter(even,lists))
print(l2)

#lambda function
lists=[1,2,3,4,5,6,7,8,9,10]
l1=list(map(lambda n:n*n,lists)) #lambda function is used to create a function without a name
print(l1)

#static method
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @staticmethod
    def display():
        print("This is a static method")
Student.display()

#interface
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side*self.side
    def perimeter(self):
        return 4*self.side
s=Square(5)
print(s.area())
print(s.perimeter())

#magical methods
class Student():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def Student(self):
        return f"{self.name} {self.age}"
s=Student("Dinesh",21)
print(s.Student())

#Operator overloading
class Student():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __add__(self,other): #here we are overloading the + operator
        return self.age+other.age
s1=Student("Dinesh",21)
s2=Student("Umesh",22)
print(s1+s2) #here we are adding two objects

#Decorator function
def decorator(func):
    def wrapper():
        print("This is a decorator function")
        func()
    return wrapper
@decorator
def display():
    print("This is a display function")
display()

#Multiple Exception in a single except block
try:
    a=int(input("Enter a number: "))
    b=int(input("Enter a number: "))
    print(a/b)
except (ZeroDivisionError,ValueError) as e:
    print("Something went wrong",e)

#Anonymous Functions 
#lambda function
lists=[1,2,3,4,5,6,7,8,9,10]
l1=list(map(lambda n:n*n,lists)) #lambda function is used to create a function without a name
print(l1)

#lembda function to calculate number positive negative or zero
lists=[1,2,3,4,5,6,7,8,9,10] 
list(map(lambda n: print("Positive") if n>0 else print("Negative") if n<0 else print("Zero"),lists))

#concadinating two tuple in python
t1=(1,2,3,4,5)
t2=(6,7,8,9,10)
t3=t1+t2
print(t3)

#concadinating two nested tuple in python
t1=((1,2,3),(4,5,6))
t2=((7,8,9),(10,11,12))
t3=t1+t2
print(t3)

#iterating through a dictionary
d={"name":"Dinesh","age":21,"language":"Python"}
for i in d:
    print(i,d[i])

#iterating through a set 
s={1,2,3,4,5,6,7,8,9,10}
for i in s:
    print(i)

#changing the shape of an array
import numpy as np
a=np.array([[1,2,3],[4,5,6]])
print(a)
a.shape=(3,2)
print(a)
print(np.reshape(a,(2,3)))