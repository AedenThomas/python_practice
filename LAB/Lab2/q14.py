# Write a Python functions
# a. to sum all the numbers in a list
# b. to multiple all the numbers in the list.
#   Sample List : (7, 12, 13, 10, 76).


def sum_list(list1):
    sum = 0
    for i in list1:
        sum = sum + i
    return sum

def multiply_list(list1):
    multiply = 1
    for i in list1:
        multiply = multiply * i
    return multiply

list1 = [7, 12, 13, 10, 76]
print("Multiplication of all the numbers in the list is: ", multiply_list(list1))
print("Sum of all the numbers in the list is: ", sum_list(list1))