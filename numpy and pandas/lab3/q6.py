# Creating 8x3 array using numpy.arange 
# [[10 11 12]
# [13 14 15]
# [16 17 18]
# [19 20 21]
# [22 23 24]
# [25 26 27]
# [28 29 30]
# [31 32 33]]

# Dividing 8x3 array into 4 sub-arrays
# [array([[10, 11, 12], [13, 14, 15]]), array([[16, 17, 18], [19, 20, 21]]), array([[22, 23, 24], [25, 26, 27]]), array([[28, 29, 30], [31, 32, 33]])]

import numpy as np
array = np.arange(10,34).reshape(8,3)
print(array)
print(np.split(array,4))
