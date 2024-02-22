rows = int(input("Enter the number of rows: "))

for i in range(1, rows+1):
    for j in range(i-1, -1, -1):
        print(2**j, end=" ")
    print()