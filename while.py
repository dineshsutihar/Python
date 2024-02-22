#wap to display number in reverse order 10 to 1
n=10
while(n > 0):
    print(n)
    n=n-1

print("--------------------------------")

#wap to find the sum of the digit 
n=int(input("Enter the Number"))
add=0
while(n>0):
    num=n % 10
    add= add+num
    n=int(n/10)
print("sum is ", add)


#to reverse the digti
#palondreme or not
#armstorme or not

n=124
p=0
while(n>10):    
    num=n%10
    p=num
    p=int(p/10)
print(p)
