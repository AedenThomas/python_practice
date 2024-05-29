# Write a program to check the grade of the student.


a=int(input("Enter the marks of the first test out of 50: "))
b=int(input("Enter the marks of the second test out of 50: "))
c=int(input("Enter the marks of the third test out of 50: "))


total=a+b+c
average=total/3

if average>=45:
    print("Grade A")
elif average>=35:
    print("Grade B")
elif average>=20:
    print("Grade C")
elif average>=15:
    print("Grade D")
else:
    print("Grade F")