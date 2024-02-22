#program for loop
for i in '12345':
    print(i)
    print("this is loop ",i)

print("--------------------------------")

#for loop Using Range
print("With Range")
for i in range(1,15,3):
    print("Test ",i)

#wap to display 5th multiplication table 10 rows
print("Multiplication table 5")
for i in range(1,11):
    r=i*5
    print(i,"* 5 =",r)

print("--------------------------------")

#wap to display 2th multiplication table 10 rows
for i in range(1,11):
    r=i*2
    print(i,"* 2 =",r)

print("--------------------------------")

for i in range(1,11):
    for j in range(1,11):
        r=i*j
        print(i,"*",j,"=",r)
    print("++++++++++++++++++++")


print("--------------------------------")

#wap to display number in reverse order 10 to 1
for i in range(10,0,-1):
    print(i)