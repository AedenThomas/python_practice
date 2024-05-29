# Create an integer array which includes [33,22,99,44,11,88,55,77,66]
# Perform the following operations
# a. Sort the array
# b. Reverse the array
# c. Remove last two elements from the array
# d. Delete the complete array

import array as arr

a = arr.array('i', [33, 22, 99, 44, 11, 88, 55, 77, 66])
print(a)

# a
a = sorted(a)
print(a)

# b
a.reverse()
print(a)

# c
del a[-2:]
print(a)

# d
del a

