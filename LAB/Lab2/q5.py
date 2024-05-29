# Create a dictionary which includes (subject name: price) as {“c”: 566, “c++” :600}.
# Perform the following operations
# a. Append the dictionary to include APP: 900, ML: 750 and DL:1600.
# b. Print the min and max value in the dictionary.
# c. Print the dictionary in reverse order
# d. Based on the price of the book, print the dictionary in ascending order.
# e. Based on the price of the book, print the dictionary in descending order.

dict1 = {"c": 566, "c++": 600}

# a
dict1.update({"APP": 900, "ML": 750, "DL": 1600})
print(dict1)

# b
print("Min value: ", min(dict1.values()))
print("Max value: ", max(dict1.values()))

# c using reversed()
print("Reversed: ", dict(reversed(dict1.items())))

# d
print("Ascending: ", dict(sorted(dict1.items(), key=lambda item: item[1]))) 

# e
print("Descending: ", dict(sorted(dict1.items(), key=lambda item: item[1], reverse=True)))