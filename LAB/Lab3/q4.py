# Write the Python statements to open tLAB/Lab3/Answers.txt
# files and print the contents of the file:
# A text file “example.txt” in both read and write  mode  

# A binary file “bfile.dat” in write mode. A text file “try.txt” in append and read mode    

# A binary file “btry.dat” in read only mode.


f = open("LAB/Lab3/Answers.txt", "r+") 

f = open("LAB/Lab3/Answers.txt", "wb")

f = open("LAB/Lab3/Answers.txt", "a+")

f = open("LAB/Lab3/Answers.txt", "rb")



# All the modes
# r+ - Opens a file for both reading and writing. The file pointer placed at the beginning of the file.
# w+ - Opens a file for both writing and reading. Overwrites the file if the file exists. If the file does not exist, creates a new file for reading and writing.
# a+ - Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for reading and writing.
# rb - Opens a file for reading only in binary format. The file pointer is placed at the beginning of the file. This is the default mode.
# wb - Opens a file for writing only in binary format. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
# ab - Opens a file for appending in binary format. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
# r+b or rb+ - Opens a file for both reading and writing in binary format. The file pointer placed at the beginning of the file.
# w+b or wb+ - Opens a file for both writing and reading in binary format. Overwrites the file if the file exists. If the file does not exist, creates a new file for reading and writing.
# + - Opens a file for updating (reading and writing) in text or binary format. The file pointer will be at the beginning of the file.
# a+b or ab+ - Opens a file for both appending and reading in binary format. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for reading and writing.
