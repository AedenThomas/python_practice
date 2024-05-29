# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Perform slicing operations to get following output using backward slicing
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [3, 4, 5, 6, 7, 8, 9, 10]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [1, 2, 3, 4, 5, 6]
# [7, 8]
# [3, 6]
# [2, 5, 8]
# [1, 4, 7]
# [1, 4, 7, 10]


mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
print(mylist[-10:])

# [3, 4, 5, 6, 7, 8, 9, 10] 
print(mylist[-8:])

# [1, 2, 3, 4, 5, 6, 7, 8, 9] 
print(mylist[-10:-1])

# [1, 2, 3, 4, 5, 6] 
print(mylist[-10:-4])

# [7, 8] 
print(mylist[-4:-2])

# [3, 6] 
print(mylist[-8:-4:3])

# [2, 5, 8] 
print(mylist[-9:-1:3])

# [1, 4, 7] 
print(mylist[-10:-1:3])

# [1, 4, 7, 10] 
print(mylist[-10::3])