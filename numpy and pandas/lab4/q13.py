# Convert a 1-D array into a 2-D array with 3 rows
# Start with:
# exercise_2 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])

# Desired output:
# [[ 0, 1, 2]
# [3, 4, 5]
# [6, 7, 8]]

import numpy as np

exercise_2 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])

# Reshape the array into a 3x3 array
exercise_2_2d = exercise_2.reshape((3, 3))

print(exercise_2_2d)