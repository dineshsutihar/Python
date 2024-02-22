Matrix = [[1, 2, 3],
          [5, 6, 8], 
          [3, 5, 7]]

# Print the matrix
print("Matrix is:")
for row in Matrix:
    print(row)

# Calculate the determinant
det = 0
for i in range(3):
    det += Matrix[0][i] * (Matrix[1][(i+1)%3] * Matrix[2][(i+2)%3] - Matrix[1][(i+2)%3] * Matrix[2][(i+1)%3])

# Print the determinant
print("Determinant of the matrix is:", det)
    