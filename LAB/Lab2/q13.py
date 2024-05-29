# Write a Python program to sort a list of tuples using Lambda.
# Original list of tuples:
# [("Python", 88), ("C++", 90), ("ML", 97), ("AI", 82)]
# Sorted List of Tuples:
# [(‘AI", 82), ("Python", 88), ("C++", 90), ("ML", 97)]


list1 = [("Python", 88), ("C++", 90), ("ML", 97), ("AI", 82)]
print("Original list of tuples:")
print(list1)
list1.sort(key = lambda x: x[1])
print("Sorted List of Tuples:")
print(list1)
