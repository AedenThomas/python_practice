# Write a program to read the existing file and copy the contents to a new file and print the contents of the new file.


f1 = open("fileHandling/files/prog1.txt", "r")

f2 = open("fileHandling/files/prog1Copied.txt", "w")
for line in f1:
    f2.write(line)
f1.close()
f2.close()

f2 = open("fileHandling/files/prog1Copied.txt", "r")
print(f2.read())
