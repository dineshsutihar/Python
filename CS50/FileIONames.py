name=[]
for _ in range(3):
    name.append(input("Enter The Name: "))

for name in sorted(name):
    print(f"Hello, {name}")

#the side effect of above program is that whenever we close our program it will
#automatically delete all the names 

#so to store the names we will be using the File I/O 

