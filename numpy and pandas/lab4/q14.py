# Add 202 to all the values in given array
# Start with:
# exercise_3 = np.arange(4).reshape(2,-1)

# Desired output:
# [[202, 203]
# [204, 205]]

import numpy as np

exercise_3 = np.arange(4).reshape(2,-1) # 2x2 array with values 0-3

# Add 202 to all the values in the array
exercise_3 = exercise_3 + 202

print(exercise_3)