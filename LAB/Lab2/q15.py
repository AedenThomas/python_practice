# Write a Python program that accepts a hyphen-separated sequence of words as input
# and prints the words in a hyphen-separated sequence after sorting them
# alphabetically. 
# Sample Items : green-red-yellow-black-white.
# Expected Result : black-green-red-white-yellow.


list1 = input("Enter a hyphen-separated sequence of words: ").split("-")
list1.sort()
print("-".join(list1))
