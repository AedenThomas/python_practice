# Create list a = [1,2,3,4,5]and update the code to get the following output
# [1,2,3,4,5,6,7,8,9,10]
# Hint extend() and range()

list1=[1,2,3,4,5]
list1.extend(range(6,11))
print("After extend: ", list1)
