num = int(input("enter the number "))
a = 0
b = 1
print(a, end = " ")
print(b, end = " ")
for i in range(0,num-2,1):
 c = a+b
 print(c,end = " ")
 a = b
 b = c

#till the given no.
def fibonacci(n):   
    
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()

n = int(input("Enter a number n to show Fibonacci series upto n:"))
fibonacci(n)