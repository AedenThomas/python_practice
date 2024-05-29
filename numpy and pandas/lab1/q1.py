import numpy as np

# Create an array with all elements set to one
x = np.ones((10, 10, 3))

# Reshape x so that the size of the second dimension equals 150
x = x.reshape(15, 20)

# Print the shape of x
print(x.shape)
