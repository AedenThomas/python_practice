# Suppose we have created a file with 500 lines of data and the file
# object reference is   “f”. Illustrate
# what each of these following operations does:
#  
# a.      
# F.seek(0,)
# b.     
# F.seek(100,1)
# c.      
# F.seek(-10,2).
# d.     
# F.seek(0,2)

f=open("example.txt","r+")

f.seek(0,) #goes to the beginning of the file
f.seek(100,1) #goes 100 characters from the current position
f.seek(-10,2) #goes 10 characters from the end of the file 
f.seek(0,2) #goes to the end of the file

