# How to swap two rows of an array?

import numpy as np

z = np.arange(25).reshape(5,5) # 5x5 matrix with values 0-24 in order
print(z)
z[[0,1]] = z[[1,0]] # swap the first and second rows
z[[3,4]] = z[[4,3]] # swap the fourth and fifth rows
print(z)
