# Write a python program to do the following:
#  User should enter a number.
#  Reverse the number entered by the user
#  Then check whether the reversed number is palindrome or not.

num=int(input("Enter a number: "))
temp=num
# reverse the number
rev=0
while num>0:
    rem=num%10
    rev=rev*10+rem
    num=num//10

print("Reverse of the number is: ",rev)

# check whether the reversed number is palindrome or not
if rev==temp:
    print("The number is palindrome")
else:
    print("The number is not palindrome")
