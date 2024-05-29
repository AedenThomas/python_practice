# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Perform slicing operations to get following output using forward indexing
# a .  [3, 4]
# b .  [3, 6]
# c .  [3, 6, 9]
# d .  [1, 4, 7, 10]
# e .  Find 3 different ways to get this output - [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# a
print(mylist[2:4])

# b
print(mylist[2:7:3])

# c
print(mylist[2:10:3])

# d
print(mylist[0:10:3])

# e
print(mylist[0:10:1])
print(mylist[0:10])
print(mylist[:])
