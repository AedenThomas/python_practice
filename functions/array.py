# Arrays in Python

import array as arr

# Create an array of 5 integers
# The type code 'i' stands for integer
a = arr.array('i', [1, 2, 3, 4, 5])
print("Array a: ", a)

# Add an element to the array
a.append(6)
print(a)

# Change the value of an element
a[0] = 0
print(a)

# Remove the last element
a.pop()
print(a)


# Insert an element at a specific index
a.insert(2, 100)
print(a)

# Create an array of 5 floats
# The type code 'd' stands for float
b = arr.array('d', [1.1, 2.2, 3.3, 4.4, 5.5])
print("Array b: ", b)

# Create an array of 5 characters

c = arr.array('u', ['a', 'b', 'c', 'd', 'e'])
print("Array c: ", c)
