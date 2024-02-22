num = int(input("enter no. of lines: "))
space = -1
for i in range(num-1):
 space = space + 2
s = 0
for i in range(num-1):
 print("*",end = "")
 print(" "*s,end = "")
 s+=1
 print("*", end = "")
 print(" "*space,end = "")
 space -=2
 print("*", end = "")
 print()
print("*",end = "")
print(" "*(num-1),end = "")
print("*")