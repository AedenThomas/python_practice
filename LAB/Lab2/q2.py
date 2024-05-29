# Create a List which includes numbers from 1 to 10
# a. Append the list to include 11
# b. Extend the list to include 12,13,14,16
# c. Insert the element 15 at index 14
# d. Delete element 16
# e. Delete element from index 0 to index 4

l = list(range(1, 11))

# a
l.append(11)
print(l)

# b
l.extend([12, 13, 14, 15])
print(l)

# c
l.insert(14, 15)
print(l)

# d
l.append(16)
l.remove(16)    
print(l)

# e
del l[0:5]
print(l)




