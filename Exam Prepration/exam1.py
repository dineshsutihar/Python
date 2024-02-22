#Row Sting
print(r"Hello \n World")
#String Formatting
print("Hello %s" % "World")
print("Hello %s %s" % ("World","World"))

#printing Pyramids
""" 
1
2 3
4 5 6
7 8 9 10"""
n=1
for i in range(1,5):
    for j in range(i):
        print(n,end=" ")
        n+=1
    print() 

""" Python program to generate randoem usnig random module"""
import random
print(random.randint(0,9))

"""Explore the new way of accesing the parent class attritues from child class"""
class Parent:
    def __init__(self):
        self.a=1
        self.b=2
        self.c=3
class Child(Parent):
    def __init__(self):
        super().__init__()
        print(self.a,self.b,self.c) 
c=Child()

#Python code to perform matrix addition using nested for loop
X=[[1,2,3],
    [4,5,6],
    [7,8,9]]
Y=[[10,11,12],
    [13,14,15],
    [16,17,18]]
result=[[0,0,0],
        [0,0,0],
        [0,0,0]]
for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j]=X[i][j]+Y[i][j]
for r in result:
    print(r)

#python script to print the sum of natural number from 1 to n
#n=int(input("Enter the number: "))
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print("The sum of natural number from 1 to %d is %d" %(n,sum))

#print the word that does not contain vowels form the given list
list=["hello","world","python","java","c++"]
for i in list:
    if "a" not in i and "e" not in i and "i" not in i and "o" not in i and "u" not in i:
        print(i)

#Discuss inheritance in python and any 3 types of inheritance
"""Inheritance is the capability of one class to derive or inherit the properties from another class."""
"""Types of Inheritance:
1. Single Inheritance
2. Multiple Inheritance
3. Multilevel Inheritance
4. Hierarchical Inheritance
5. Hybrid Inheritance"""

#Elaborate various numpy indexing techniques and slicing operationsin python with example
"""Indexing in numpy means accessing a single element of an array at a time"""
"""Slicing in numpy means accessing a range of elements in an array at a time"""
import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9])
print(a[0]) #accessing the first element
print(a[1]) #accessing the second element
print(a[-1]) #accessing the last element
print(a[-2]) #accessing the second last element
print(a[2:5]) #accessing the elements from 2 to 5
print(a[2:]) #accessing the elements from 2 to end
print(a[:5]) #accessing the elements from start to 5
print(a[-4:-1]) #accessing the elements from -4 to -1
print(a[1:7:2]) #accessing the elements from 1 to 7 with step size 2
print(a[::2]) #accessing the elements from start to end with step size 2
print(a[::-1]) #accessing the elements from end to start with step size 1

#write a progaram to print the natural number 1 to 20 with forloop and range and with stpes 2
for i in range(1,21,2):
    print(i)

#write a progaram to and make for loop to pring 9 to 1
for i in range(9,0,-1):
    print(i)

#Discuss the dot product of two vectors and matrix multiplication in numpy with example
"""Dot product of two vectors is the sum of the product of the corresponding entries of the two sequences of numbers"""
"""Matrix multiplication is a binary operation that produces a matrix from two matrices with entries in a field"""
import numpy as np
a=np.array([1,2,3])
b=np.array([4,5,6])
print(np.dot(a,b))
c=np.array([[1,2,3],
            [4,5,6],
            [7,8,9]])
d=np.array([[1,2,3],
            [4,5,6],
            [7,8,9]])
print(np.matmul(c,d))

#Different between append and extend in list
"""append() method adds a single element to the end of the list"""
"""extend() method adds elements from another list (or any iterable) to the end of the list"""
list1=[1,2,3]
list2=[4,5,6]
list1.append(list2)
print(list1)
list1=[1,2,3]
list2=[4,5,6]
list1.extend(list2)
print(list1)

a=np.zeros((2,3,4),dtype=int)
print(a)
b=np.arange(4,6)
print(b)
#reshape the array using reshape function
print(np.reshape(b,(1,2)))
print(b.reshape(2,1))
#transpose the array
print(b.T)
#transpose the array using transpose function
print(np.transpose(b))

#accessing the elements from the array and rows and columns
a=np.array([[1,2,3],
            [4,5,6],
            [7,8,9]])
print(a[:,1]) #accessing the second column

#write a program that generates 5 random numbers in the range 10 to 50. Use a seed value of 6. Make a provision to change this seed value time you execute the program by associating it with time of execution?
import random
import time
random.seed(6)
for i in range(5):
    print(random.randint(10,50))  
print("__________________") 
random.seed(time.time())
for i in range(5):
    print(random.randint(10,50))

#Case of string like upper,lower,swapcase
a="Hello World"
print(a.upper())
print(a.lower())
print(a.swapcase())


print("__________________")
def myfunc(roll=123,name="john"):
    print(roll,name)
rollno=101
myfunc(rollno,"Hari")

'''Find the false statement
s1=to ensure some code runs no matter what error occurs, you can usue a finally statement statement
s2=the finally statement is placed at the bottom of the try/except statement
s3= code within a finally statement always runs after the execution of the code in the try statement
'''

num = 3.5

if num % 1 != 0:

    num = num // 1
print(type(num))

def myfun():
    global x
    x="Jain"
    return (x+"University")
x="Welcome"
x=myfun()
print(x)


print ([8, 2, 4, 0][::-2])

print("__________________")

class A:
    def __init__(self,x=1):
        self.x=x
class der(A):
    def __init__(self,y=2):
        super().__init__()
        self.y=y
def main():
    obj=der()
    print(obj.x,obj.y)
main()  

#mod1
# def chnage(a):
#     b=[x*2 for x in a]
#     print(b)
# #mod2    
# def change(a):
#     b=[x*x for x in a]
#     print(b)
# from mod1 import change
# from mod2 import change
# #main
# s=[1,2,3]
# change(s)
        
# s = "python"

# for i in range(s):

#         print(i, end = " ")


#numpy linespace
import numpy as np
a=np.linspace(1,100,10)  #start,stop,step 
print(a)

#numpy randoem rand
import numpy as np
a=np.random.rand(2)
print(a)

#scipy pi without constants
from scipy import constants
print(constants.pi)

#CSV file
import csv
with open('data.csv','w',newline='') as file:
    writer=csv.writer(file)
    writer.writerow(["SN","Movie","Rating"])
    writer.writerow([1,"Lord of the Rings",5])
    writer.writerow([2,"Harry Potter",4.5])
    writer.writerow([3,"Avengers",4.8])
#Static method
class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def display(self):
        print(self.name,self.roll)
    @staticmethod
    def show():
        print("This is static method")
s=Student("Ram",1)
s.display()
Student.show()

#interface in python
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
        self.__side=side
    def area(self):
        return self.__side*self.__side
    def perimeter(self):
        return 4*self.__side
s=Square(5)
print(s.area())
print(s.perimeter())

#Magic or Dunder methods in python
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def __str__(self):
        return "Name: "+self.name+" Salary: "+str(self.salary)
    def __add__(self,other):
        return self.salary+other.salary
e1=Employee("Ram",1000)
e2=Employee("Shyam",2000)
print(e1)
print(e1+e2)

#Memory Allocation in python
import sys
x=10
print(sys.getsizeof(x))
y=1000000000
print(sys.getsizeof(y))
z=10.5
print(sys.getsizeof(z))
a=10.5+5j
print(sys.getsizeof(a))
b="Hello"
print(sys.getsizeof(b))
c=[1,2,3,4,5]
print(sys.getsizeof(c))
d=(1,2,3,4,5)
print(sys.getsizeof(d))
e={1,2,3,4,5}
print(sys.getsizeof(e))
f={1:1,2:2,3:3,4:4,5:5}
print(sys.getsizeof(f))
#Python Decorator
def decorator(func):
    def inner():
        print("Accessing :",func.__name__)
        return func()
    return inner
@decorator
def test():
    print("Executing test")
test()

