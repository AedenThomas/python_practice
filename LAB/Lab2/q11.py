# Write a program to find largest in an n element list using recursion, take the list
# elements from the user.

def largest(n, list):
    if n == 1:
        return list[0]
    return max(list[n-1], largest(n-1, list))

n = int(input("Enter the number of elements in the list: "))
list = []
for i in range(n):
    list.append(int(input("Enter the element: ")))
    
print("The largest element in the list is", largest(n, list))
