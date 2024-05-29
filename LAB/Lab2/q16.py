# Write a Python program to calculate the geometric sum of n-1. 
# Note: In mathematics, a geometric series is a series with a constant ratio between
# successive terms.


def geometric_sum(n):
    if n < 0:
        return 0
    else:
        return 1 / (2 ** n) + geometric_sum(n - 1)


n = int(input("Enter the value of n: "))
print("The geometric sum of n-1 is: ", geometric_sum(n))