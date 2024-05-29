# Create list which stores: a = [‘ML’, "python", "data science"] then do the following:
# a. Insert ‘AI’ at index 4 using insert()
# b. Retrieve index of ‘python’ using index()

list1=["ML", "python", "data science"]

# a
list1.insert(1, "AI")
print("After insert: ", list1)

# b
print("Index of python: ", list1.index("python"))
