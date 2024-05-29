# x=1
# print(x)

# x=5.6
# print(x)


# multiLineString='''0123456789
# '''
# print(multiLineString)


# str1="0123456789"

# slicing
# print(str1[-1:-3:-1]) 

# 
list1=["sd", 1, 5.6, "i"]

# print(type(list1))
# print(list1*3)
# print(len(list1))

# list2=["sd", 1, 5.6, "i"]
# print(list1==list2)

# max list
# print(max(list1))



# list function
# print(list(list1))

# Take 4 inputs and store into a list using list()
# a=1
# b=2
# c=3
# l=[a,b,c]
# print(l)

# 
# tuple1=(1,3,4,2,5,6,7,8,9,10,1)

# count
# print(tuple1.count(1))

# index
# print(tuple1.index(2))


# tup=(1,"asd", True, "False", "asdad2")
# print(tup)

# Tuple slicing
# print(tup[1:3])

# Tuple multiplication
# print(tup*3)

# Tuple length
# print(len(tup))

# Tuple concatenation
# print(tup+tup)


# Dictionary
dict1={"name":"Aeden", "age": 23, "city":"Bangalore"}
print(dict1)

# Printing value of a key
print(dict1["name"])

# Update value of a key
dict1["name"]="Geo"
print(dict1["name"])

# Delete a key value
del dict1["name"]
print(dict1)

# Use get method to get value of a key
print(dict1.get("age"))

# Length
print(len(dict1))

# Compare
dict2={"name":"Aeden", "age": 23, "city":"Bangalore"}
print(dict1==dict2)

a=str(dict1)
print(type(a))


# Sets
set1={"apple", "banana", "cherry"}
print(set1)
set1.add("orange")
print(set1)
set1.remove("apple")
print(set1)