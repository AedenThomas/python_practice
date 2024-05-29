import numpy as np

# Create a 5x4 array with the given elements
arr = np.array([
    [3, 6, 9, 12],
    [15, 18, 21, 24],
    [27, 30, 33, 36],
    [39, 42, 45, 48],
    [51, 54, 57, 60]
])

# The array should have the row of odd number and even number of columns like below
# [ [ 6 12]
# [30 361
# [54 60]]

arr2 = arr[0::2, 1::2]
print(arr2)

