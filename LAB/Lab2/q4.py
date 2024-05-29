# Consider the list [4,6,[1,2],9,10] and convert this list to dictionary using dictionary
# comprehension.

list1 = [4, 6, [1, 2], 9, 10]

dict1 ={}


for i in range(0, len(list1)):
    dict1.update({i: list1[i]})
print(dict1)

