# 1a. Write a program that accepts the file name as an input from the user and count the number of times the character appears in the file
# and display only those sentences, which begin with an uppercase alphabet.


fileName = input("Enter the file name: ")
char = input("Enter the character: ")
count = 0
with open(fileName, "r") as f:
    for line in f:
        if line[0].isupper():
            print(line)
        for c in line:
            if c == char:
                count += 1
print("The character appears", count, "times")
