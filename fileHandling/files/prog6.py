# File object variables
#

# Create a file in wb mode, 
# Print name of file, if file is closed, mode of file, and when its being closed

f1 = open("fileHandling/files/prog7.bin", "wb")
print("Name of file: ", f1.name)
print("Mode of file: ", f1.mode)
print("File is closed: ", f1.closed)
f1.close()


