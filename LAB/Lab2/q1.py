# Write a python code to do the following:
# a. Create a Dictionary with 3 keys and values a 0 using dict.fromkeys().
# Output: ["key1": 0, "key2": 0, "key3": 0]

# b. Create a Dictionary with 3 keys but without specifying the value.
# Output: ["key1": None, "key2": None, "key3": None]

# c. Create a Dictionary with key:value as
# i. {"brand": "Ford", "model": "Mustang", "year": 1964}
# ii. Print the model of car using get()


# a
d = dict.fromkeys(["key1", "key2", "key3"], 0)
print(d)

# b
d = dict.fromkeys(["key1", "key2", "key3"])
print(d)

# c
d = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(d.get("model"))