#interface in python 
from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def show(self):
        pass
class B(A):
    def show(self):
        print("B")
obj=B()
obj.show()

#Customize your Python class with Magic or Dunder methods
class A:
    def __init__(self,x=1):
        self.x=x
    def __add__(self,o):
        return self.x+o.x
    def __str__(self):
        return str(self.x)
obj=A(5)
obj1=A(6)   
print(obj+obj1)
print(obj)

#method Overloading
class A:
    def display(self,x=None,y=None):
        if x!=None and y!=None:
            print(x+y)
        elif x!=None:
            print(x)
        else:
            print("Nothing to display")
obj=A()
obj.display()
obj.display(5)
obj.display(5,6)

#Garbage Collection
import gc
print(gc.isenabled())
gc.disable()
print(gc.isenabled())
gc.enable()

#Reference Counting
import sys 
class A:
    pass
obj=A()
print(sys.getrefcount(obj)) #1

#Python Decorators
def decorator(func):
    def inner():
        print("Inner function")
        func()
    return inner
@decorator
def display():
    print("Display function")
display()

#Generators in Python
def mygen():
    yield "A"
    yield "B"
    yield "C"
for i in mygen():
    print(i)

#Python Iterators
class A:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=10:
            val=self.num
            self.num+=1
            return val
        else:
            raise StopIteration
obj=A()
for i in obj:
    print(i)


#Exceptions in Python
try:
    print(10/0)
except ZeroDivisionError:
    print("Not divisible by zero")
finally:
    print("This will be executed")

#custom exception
try:
    raise NameError("Hello")
except NameError as e:
    print("An exception",e)

#Multiple exception
try:
    print(10/0)
except (ZeroDivisionError,NameError):
    print("Not divisible by zero")
finally:
    print("This will be executed")
    