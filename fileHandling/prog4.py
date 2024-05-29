# Write a python code the print the following output by using fole concept & input data is stored in list
# Hello, This is Delhi, This is paris, This is London

list1=["This is Delhi\n","This is Paris\n","This is London\n"]

f = open("fileHandling/files/prog4.txt", "w")
f.writelines(list1)
f.close()

# Alternative way
# Writing using with statement
with open("fileHandling/files/prog4.txt", "w") as f:
    f.writelines(list1)

# Reading using with statement
with open("fileHandling/files/prog4.txt", "r") as f:
    print(f.read())


