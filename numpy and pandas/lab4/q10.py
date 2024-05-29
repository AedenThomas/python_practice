# Create random vector of size 10 and replace the maximum value by 0.

import numpy as np

arr = np.random.randint(0, 100, size=10)
print(arr)
arr[arr.argmax()] = 0
print(arr)
