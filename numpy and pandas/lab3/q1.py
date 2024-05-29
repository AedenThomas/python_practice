import numpy as np

array1 = np.array([[4.5, 3.5], [5.1, 2.3]])
array2 = np.array([[1], [2]])

result = np.concatenate((array1, array2), axis=1)

print(result)
