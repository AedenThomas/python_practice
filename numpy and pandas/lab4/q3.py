# Find 3 different functions to generate a sequence of numbers in the form of a numpy array
# from 0 to 100 with gaps of 2 numbers, for example: 0, 2, 4 ...

import numpy as np

# 1. np.arange
print(np.arange(0, 101, 2))

# 2. np.linspace
print(np.linspace(0, 100, 51))

# 3. np.arange with np.reshape
print(np.arange(0, 100, 2).reshape(25, 2))

