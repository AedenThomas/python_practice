import numpy as np

# Create the first array
array1 = np.array(['Python', 'PHP'])

# Create the second array
array2 = np.array([' Java', ' C++'])

# new array:
# ['Python Java' 'PHP C++']

# Concatenate the arrays
result = np.char.add(array1, array2)

print(result)
