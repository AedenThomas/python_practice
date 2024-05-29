# Extract the integer part of a random array using 5 different methods.

import numpy as np

# 1. np.floor
arr = np.random.uniform(0, 10, 10) # first argument is the lower bound, second argument is the upper bound, third argument is the number of elements
print(np.floor(arr))

# 2. np.ceil
arr = np.random.uniform(0, 10, 10)
print(np.ceil(arr) - 1)

# 3. np.trunc
arr = np.random.uniform(0, 10, 10)
print(np.trunc(arr))

# 4. np.rint
arr = np.random.uniform(0, 10, 10)
print(np.rint(arr))

# 5. np.modf
arr = np.random.uniform(0, 10, 10)
print(np.modf(arr)[1])


