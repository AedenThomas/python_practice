import numpy as np

array1 = np.array([[1,1],[1,1]])
array2 = np.array([[2,2,2],[2,2,2]])
array3 = np.array([[3,3,3,3],[3,3,3,3]])
array4 = np.array([[4,4,4,4,4],[4,4,4,4,4]])

# Pad array2 with additional columns of zeros
array2_padded = np.pad(array2[:, :2], ((0, 0), (0, 2)), 'constant', constant_values=0)

result = np.vstack((array1, array2_padded, array3, array4))
print(result)
