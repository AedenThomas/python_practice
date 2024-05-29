# Write a python program to check the type of triangle

a=input("Enter first side: ")
b=input("Enter second side: ")
c=input("Enter third side: ")

if a==b==c:
    print("Equilateral triangle")
elif a==b or a==c or b==c:
    print("Isosceles triangle")
else:
    print("Scaler")