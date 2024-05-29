# Printing Original array
# [ [34 43 73]
# [82 22 12]
# [53 94 66]]
# Sorting Original array by second row
# [[73 43 34]
# [12 22 82]
# [66 94 53]]
# Sorting Original array by second column
# [ [82 22 12]
# [34 43 731
# [53 94 66]]



import numpy as np

# Original array
array = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])
print(array)

# Sort the array by the second row
sorted_array = array[:, array[1, :].argsort()]
print(sorted_array)


# Sort the array by the second column
sorted_array = array[array[:, 1].argsort()]
print(sorted_array)