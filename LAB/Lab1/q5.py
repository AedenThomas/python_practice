# Create list which stores: a = [3,1,2,6,4,5,9,6,7,8]then do the following:
# a. Sort the list using sort().
# b. Reverse the list using reverse().
# c. Pop the last element using pop()
# d. Remove element 3 from list using remove().
# e. Reverse the list using reverse().
# f. Empty the list using clear().

list1=[3,1,2,6,4,5,9,6,7,8]

# a 
list1.sort()
print("a. After sort: ", list1)

# b
list1.reverse()
print("b. After reverse: ", list1)

# c
list1.pop()
print("c. After pop: ", list1)

# d
list1.remove(3)
print("d. After remove: ", list1)

# e
list1.reverse()
print("e. After reverse: ", list1)

# f
list1.clear()
print("f. After clear: ", list1)
