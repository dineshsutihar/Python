#Roman no. V
num_lines = int(input("Enter the number of lines: "))
space = -1
for i in range(num_lines-1):
    space = space + 2
s = 0
for i in range(num_lines-1):
    print(" "*s,end = "")
    s+=1
    print("*", end = "")
    print(" "*space,end = "")
    space -=2
    print("*", end = "")
    print()
print(" "*(num_lines-1),end = "")
print("*")