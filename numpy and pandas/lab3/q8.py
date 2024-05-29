# Printing Original array
# [[34 43 73]
# [82 22 12]
# [53 94 66]]
# Printing amin Of Axis 1
# [34 12 53]
# Printing amax Of Axis 0
# [82 94 73]

import numpy as np

# Original array
array = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])
print("Printing Original array" )
print(array)

# Printing amin Of Axis 1
print("Printing amin Of Axis 1")
print(np.amin(array, 1))

# Printing amax Of Axis 0
print("Printing amax Of Axis 0")
print(np.amax(array, 0))
