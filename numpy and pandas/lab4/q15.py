# Extract the first four columns of this 2-D array
# Start with this: 
# exercise_6 = np.arange(100).reshape(5,-1)
#  Desired output:
# [[ 0 1 2 3]
# [20 21 22 23]
# [40 41 42 43]
# [60 61 62 63]
# [80 81 82 83]]

import numpy as np

exercise_6 = np.arange(100).reshape(5,-1) # 5x20 array with values 0-99

# Extract the first four columns of the array
exercise_6 = exercise_6[:,0:4]

print(exercise_6)