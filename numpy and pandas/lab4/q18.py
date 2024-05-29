import numpy as np

arr1 = np.array([[2, 8, 2], [3, 4, 8], [0, 2, 1]])
arr2 = np.array([[2, 1, 1], [0, 1, 0], [2, 3, 0]])

# Perform the Kronecker product of the two arrays
result = np.kron(arr1, arr2)

print(result)
