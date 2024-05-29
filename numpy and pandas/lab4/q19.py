# 19.Aggregations: Min, Max, and Everything In Between –
# a. Write the Python code to print the maximum of 4,12,43.3,19,100
# b. Check whether your able to find the minimum from the given set of values ::
# 4,12,43.3,19, "HelloProgramming"
# i. Write the python code to print the word occurring 1st among these in
# dict:: "GoodMorning", "Evening", "algorithm", "programming"

import numpy as np

a = np.array([4,12,43.3,19,100])

print(np.max(a))

# b. Find the minimum of 4,12,43.3,19
values = [4,12,43.3,19]
minimum = min(values)
print(minimum)  # prints 4

# Find the minimum of "HelloProgramming"
values = ["HelloProgramming"]
print(min(values))  # prints "HelloProgramming"

#  Find the first word in the dictionary {"GoodMorning": 1, "Evening": 2, "algorithm": 3, "programming": 4}
words = {"GoodMorning": 1, "Evening": 2, "algorithm": 3, "programming": 4}
first_word = sorted(words)[0]
print(first_word)  # prints "algorithm"
