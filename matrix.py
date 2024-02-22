values = [[1, 2, 20], [4, 5, 60], [7, 8, 9]]

for row in values:
    for element in row:
        print(element,end=" ")
    print()

#ADD two matrices
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
result = [[0, 0], [0, 0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j] = A[i][j] + B[i][j]

print(result)
