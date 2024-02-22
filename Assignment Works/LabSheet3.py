def scalar_multiplication(mat, k):
    # Get the number of rows and columns in the matrix
    rows = len(mat)
    cols = len(mat[0])
    
    # Create a new matrix to store the result
    result = [[0 for j in range(cols)] for i in range(rows)]
    
    # Multiply each element of the matrix by the scalar k
    for i in range(rows):
        for j in range(cols):
            result[i][j] = mat[i][j] * k
    
    return result

# Example
mat = [[2, 3], [5, 4]]
k = 5

result = scalar_multiplication(mat, k)

# Print the resulting matrix
for row in result:
    print(row)

print("----------------------------------------------------")

#----------------------------------------------------------
#New Code Lab Sheet 3

# Example input
matrix = [[2, 3], [5, 4]]
k = 5
# Perform scalar multiplication
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        result[i][j] = matrix[i][j] * k

# Print the result
for row in result:
    print(' '.join(map(str, row)))



print("----------------------------------------------------")


#Lab Sheet 3 b
# Example input
tuple1 = (1, "Apple")
tuple2 = ("Orange", 4)

# Concatenate tuples into nested tuple
nested_tuple = (tuple1, tuple2)

# Print the nested tuple
print(nested_tuple)


