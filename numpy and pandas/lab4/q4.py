import numpy as np

a = np.array([[1,2,3], [4,5,6], [7,8,9]])
b = np.array([[2,3,4], [5,6,7], [8,9,10]])

result = np.dot(a, b)
print(result)

transposed_a = a.transpose()
print(transposed_a)
