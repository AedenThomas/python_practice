import numpy as np

z_list = [z for z in range(0,5)]
y_list = [z_list for y in range(0,4)]
x_list = [y_list for x in range(0,3)]
x_array = np.array(x_list)
print(x_array.shape)