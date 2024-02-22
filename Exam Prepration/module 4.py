

#module
# from mod2 import change
# print(change([1,2,3]))

#datetime
import datetime
x=datetime.datetime(2020, 5, 17) #year,month,day
print(x)
x=datetime.datetime.now()   #current date and time
print(x)
print(datetime.datetime.today())

#date
from datetime import date
print(date(2020, 5, 17))
print(date.today())

#Current time
from datetime import time
print(time(5, 45, 2, 10000)) #hour,minute,second,microsecond

#callender
import calendar
print(calendar.month(2020, 5))
print(calendar.calendar(2020))

#Sound
import winsound
winsound.Beep(500,1000) #frequency,duration
winsound.PlaySound("sound.wav",winsound.SND_FILENAME)


# #sound form playsound module
# from playsound import playsound
# playsound("H:\Parchai (320 kbps).mp3")

#Download image from internet
import requests
url="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"
r=requests.get(url)
with open("python.png","wb") as f:
    f.write(r.content)

#file handling
with open ("text.txt","w+") as f:
    f.write("Hii Dinesh") #write in file
    f.seek(0) #move cursor to the beginning of the file
    print(f.read()) #read file
    f.writelines("\nHow are you") #write in file
    f.seek(0) #move cursor to the beginning of the file
    print(f.read()) #read file
    f.write("\nI am fine") #write in file
    f.seek(0) #move cursor to the beginning of the file
    print(f.read()) #read file

#Command Line Arguments
import sys
print(sys.argv)

# # #Command Line Arguments
# import sys
# print(sys.argv[0])
# print(sys.argv[1])
# print(sys.argv[2])

#csv file
import csv
with open('data.csv','w+') as file:
    writer=csv.writer(file)
    writer.writerow(["SN","Movie","Rating"])
    writer.writerow([1,"Lord of the Rings",5])
    writer.writerow([2,"Harry Potter",5])
    writer.writerow([3,"Avengers",5])
    #read csv file
    reader=csv.reader(file)
    for row in reader:
        print(row)

#Inheritance Derived class
class A:
    def __init__(self,x=1):
        self.x=x
class der(A):
    def __init__(self,y=2):
        super().__init__() #A.__init__(self)
        self.y=y
def main():
    obj=der()
    print(obj.x,obj.y)
main()

#inner class
class A:
    def __init__(self):
        self.x=1
        self.y=2
    class B:
        def __init__(self):
            self.i=3
        def display(self):
            print(self.i)
obj=A()
obj1=obj.B()
obj1.display()

#overriding method
class A:
    def __init__(self,x=1):
        self.x=x
    def __add__(self,o):
        return self.x+o.x  
obj=A(5)
obj1=A(6)
print(obj+obj1)

#overriding method example 2
class A:
    def __init__(self,x=1):
        self.x=x
    def __str__(self):
        return str(self.x)
obj=A(5)
print(obj)

# Is a relationship vs Has a relationship

# Is a relationship
class A:
    def display1(self):
        print("A")
class B(A):
    def display2(self):
        print("B")
obj=B()
obj.display1()
obj.display2()
# Has a relationship
class A:
    def display1(self):
        print("A")
class B:
    def __init__(self):
        self.a=A()
    def display2(self):
        print("B")
        self.a.display1()
obj=B()
obj.display2()

#mixins
class A:
    def display1(self):
        print("A")
class B:
    def display2(self):
        print("B")
#Python code to combine two files into single file using file handling. 
with open ('file1.txt',"w+") as file1:
    with open ('file2.txt',"w+") as file2:
        with open ("output.txt","w+") as output:
            for line in file1:
                output.write(line)
            for line in file2:
                output.write(line)
            print(output.read())
