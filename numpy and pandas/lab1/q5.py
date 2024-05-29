# Define the size of the matrix
n, m = 8, 8

# Create an empty matrix
matrix = [[0 for _ in range(m)] for _ in range(n)]

# Fill the matrix with a checkerboard pattern
for i in range(n):
    for j in range(m):
        if (i + j) % 2 == 0:
            matrix[i][j] = 0
        else:
            matrix[i][j] = 1

# Print the matrix
for row in matrix:
    print(row)

