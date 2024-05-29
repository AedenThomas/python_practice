# f = open("fileHandling/files/prog1.txt", "r")
# print("Reading file contents using read() method")
# print(f.read())

# print("Reading file contents by giving a number to read() method")
# f = open("fileHandling/files/prog1.txt", "r")
# print(f.read(10))

# print("Reading file using readlines() method")
# f = open("fileHandling/files/prog1.txt", "r")
# print(f.readline())

# print("Reading file using readlines() method")
# # f = open("fileHandling/files/prog1.txt", "r")
# print(f.readlines())

# We need to open the file every time we want to read it because the file pointer is at the end of the file after reading it.
# An alternative is to use the seek() method to set the file pointer to the beginning of the file


# Using write() method to write to a file

f = open("fileHandling/files/prog1.txt", "w")
print("Writing to a file using write() method")
f.write("This is a test file")
f.close()


f = open("fileHandling/files/prog1.txt", "r")
print("Reading file contents using read() method")
print(f.read())


f = open("fileHandling/files/prog1.txt", "a")
print("Appending to a file using write() method the second time")
f.write("This is the second line which is being written")
f.close()


f = open("fileHandling/files/prog1.txt", "r")
print("Reading file contents using read() method")
print(f.read())
