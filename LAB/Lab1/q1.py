# Create a list which contains[1,2,3,4,5]then do the following:
# a. Append 6 to the list
# b. Make the copy of the list using copy()
# c. Empty the list using clear().

list1=[1,2,3,4,5]

# a
list1.append(6)
print("After append: ", list1)

# b
list2=list1.copy()
print("List 2: ", list2)

# c
list1.clear()
print("After clearing list1: ", list1)