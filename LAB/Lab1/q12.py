# Create a list that stores ["S", 9, "A", 8, "B", 7, "C", 6, "D", 5] then convert this list to
# dictionary with key as "Grade" and value as "grade_point", finally print the dictionary.

list1 = ["S", 9, "A", 8, "B", 7, "C", 6, "D", 5]
print("Before: ", list1)

dict1={}
for i in range(0, len(list1), 2):
    dict1.update({list1[i]: list1[i + 1]})

print("After: ", dict1)