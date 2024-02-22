class Students:
    def Show(self):
        print("Name is", self.name)
        print("USN is", self.usn)
    def input(self):
        self.name = input("Enter the Name :")
        self.usn = input("Enter the USN :")
s = Students()
s1 = Students()
s.input()
s1.input()

s.Show()
s1.Show()

#Older
#wap to get 2 students USN an Name of students
'''
class Students:
    def Show(self,name,usn):
        print("Name is",self.name)
        print("USN is", self.usn)
    def input(self,name,usn):
        self.name = input("Enter the Name :")
        self.usn = input("Enter the USN :")

s=Students()
s.input()
s.Show()
s1=Students()
s1.input()
s1.Show()
'''