import numpy as np


# 1. Find sine value in terms of degree when angle = 90
print(np.sin(np.deg2rad(90)))

# 2. Find sine value in terms of radians when angle = 90
print(np.sin(90))

# 3. Find the sine value for array of angles ([0., 30., 45., 60., 90.])
print(np.sin(np.array([0., 30., 45., 60., 90.])))

# 4. Find cosine value in terms of degree when angle = 180
print(np.cos(np.deg2rad(180)))

# 5. Find cosine value in terms of radians when angle = 180
print(np.cos(180))

# 6. Find the cosine value for array ([3.14, 3.14/2, 6.28])
print(np.cos(np.array([3.14, 3.14/2, 6.28])))

# 7. Find tangent value in terms of degree when angle = 60
print(np.tan(np.deg2rad(60)))

# 8. Find tangent value in terms of radians when angle = 60
print(np.tan(60))

# 9. Find tangent  value for array ([3.14, 3.14/2, 6.28])
print(np.tan(np.array([3.14, 3.14/2, 6.28])))

# 10. find sine value for the array 0,np.pi /2, np.pi /3, np.pi
print(np.sin(np.array([0, np.pi /2, np.pi /3, np.pi])))

# 11. find the arcsine value for the numpy array [0, 1, 0.3, -1]
print(np.arcsin(np.array([0, 1, 0.3, -1])))

