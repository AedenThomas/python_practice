# SORTING:

# i. Create a list [[4,3,2],[2,1,4]], convert it to a numpy array and sort it
# along axis 1.
# ii. Implement a program to take fruits names from array of fruits.
# To sort the array in alphabetical manner and display their index
# position.

import numpy as np

# i. Create a list [[4,3,2],[2,1,4]], convert it to a numpy array and sort it
# along axis 1.
list = [[4,3,2],[2,1,4]]
array = np.array(list)
print(np.sort(array, axis=1))

# ii. Implement a program to take fruits names from array of fruits.
# To sort the array in alphabetical manner and display their index
# position.
fruits = np.array(["apple", "banana", "kiwi", "orange"])

# Get the indices of the elements in sorted order
sorted_indices = np.argsort(fruits)

# Use the sorted indices to index into the original array and print the index and value of each element
for index in sorted_indices:
    print(f"Index: {index}, Fruit: {fruits[index]}")

