# Write the python code to get the following output:
# Input:
# array([6,2])
# array([2,5])
# Output:
# [[12 30]
# [ 4 10]]

import numpy as np

a = np.array([6,2])
b = np.array([2,5])

print(np.outer(a,b)) # outer product of a and b
