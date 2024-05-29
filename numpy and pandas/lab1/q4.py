# Create a 2d array with 0 on the border and 1 inside.

# Define the size of the 2D array
n, m = 5, 5

# Create an empty 2D array
arr = [[0 for _ in range(m)] for _ in range(n)]

# Set the border to 0
for i in range(n):
    arr[i][0] = 0
    arr[i][m-1] = 0
for j in range(m):
    arr[0][j] = 0
    arr[n-1][j] = 0

# Set the inside to 1
for i in range(1, n-1):
    for j in range(1, m-1):
        arr[i][j] = 1

# Print the array
for row in arr:
    print(row)
