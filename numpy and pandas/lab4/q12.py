# Replace all odd numbers in the given array with -1

import numpy as np

z = np.arange(10) # array with values 0-9
print(z)
z[z%2==1] = -1 # replace all odd numbers with -1
print(z)
