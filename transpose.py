#code to transpose matrix
matrix = [[1, 2], [3, 4]]
transposed_matrix = matrix

for i in range(2):
    for j in range(2):
        transposed_matrix[i][j]=matrix[j][i]
print(transposed_matrix)


## Print the diagnol matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(len(matrix)):
    print(matrix[i][i])
#Alternate way
l=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(matrix)):
    l[i][i]=1
print(l)

#Print 