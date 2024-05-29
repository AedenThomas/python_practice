# Write a program to create a list by taking input from the user: Size of the list and also
# the elements of the list. Perform following operations on the list
# a . Append the list with the elements entered by the users
# b .  Find the min element form the list
# c .  Print the max element from the list
# d . Print the length of the list.



list1 = []
size = int(input("Enter the size of the list: "))
for i in range(0, size):
    list1.append(int(input("Enter the element: ")))

# b
print("Min element: ", min(list1))

# c
print("Max element: ", max(list1))

# d
print("Length of the list: ", len(list1))