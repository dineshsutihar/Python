n = int(input("Enter the number of lines: "))

# Top half of the diamond pattern
for i in range(1, n+1):
    print(" "*(n-i) + "*"*(2*i-1))

# Bottom half of the diamond pattern
for i in range(n-1, 0, -1):
    print(" "*(n-i) + "*"*(2*i-1))
