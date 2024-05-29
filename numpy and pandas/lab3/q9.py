# Consider a random 10x2 matrix representing Cartesian coordinates, convert them to polar
# coordinates.

import numpy as np

z= np.random.random((10,2)) # 10x2 matrix

x,y = z[:,0], z[:,1] # x and y are the first and second columns of z
r = np.sqrt(x**2+y**2) # r is the distance from the origin using the Euclidean distance formula r = sqrt(x^2 + y^2)
t = np.arctan2(y,x) # t is the angle from the x-axis using the arctan2 function
print(r) 
print(t)