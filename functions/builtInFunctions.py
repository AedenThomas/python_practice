# Examples of all()
list1 = [1, 2, 3, 4, 5]
list2 = [1, True, 3, 4, 5]
print("all() on list1: ", all(list1))
print("all() on list1: ", all(list2))


# abs
# bool
print("abs(-1): ", abs(-1))


print("bool(0): ", bool(0))
print("bool(1): ", bool(1))
print("bool(2): ", bool(2))
list1 = [1, 2, 3, 4, 5]
print("bool(list1): ", bool(list1))
list2 = []
print("bool(list2): ", bool(list2))

# ascii
print("ascii('a'): ", ascii('a'))
strContent = '''
asdsd
asd
'''
print("ascii(strContent): ", ascii(strContent))
print("ascii(∑): ", ascii('∑'))


# enumerate
list1 = [10,20,30,40]
for index, value in enumerate(list1):
    print("index: ", index, "value: ", value)


# format
print("format(1.2345, '.2f'): ", format(1.2345, '.2f'))


# bin
print("Binary of 10 after slicing first 2 character: ", bin(10)[2:])


# eval
print("eval('1+2'): ", eval('1+2'))
print("eval('1+2*3'): ", eval('1+2*3'))


# filter
def isOdd(x):
    return x % 2 == 1
list1 = [1, 2, 3, 4, 5]
list2 = filter(isOdd, list1)
for value in list2:
    print("value: ", value)
