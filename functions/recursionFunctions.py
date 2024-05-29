# Pallindrome using recursion
str1 = "36763"
def isPalindrome(str1):
    if len(str1) == 0 or len(str1) == 1:
        return True
    if str1[0] == str1[-1]:
        return isPalindrome(str1[1:-1])
    else:
        return False
        

    
if isPalindrome(str1):
    print("String is palindrome")
else:
    print("String is not palindrome")

