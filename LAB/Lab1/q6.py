# First create an empty list then insert [‘ML’,’DL’,’APP’,’C’].
# Write the code to get the following output:
# ML
# ['ML', 'DL', 'APP', "C', 'C++']
# C++
# ['ML', 'DL', 'APP', 'C', 'C++', [2, 0, 1, 5]]
# D
# [2, 0, 1, 5]

list1=[]
list1.insert(0, "ML")
list1.insert(1, "DL")
list1.insert(2, "APP")
list1.insert(3, "C")

print(list1[0])
list1.insert(4, "C++")
print(list1)


print(list1[4])


list1.insert(5, [2,0,1,5])
print(list1)


print(list1[1][0])

print(list1[5])