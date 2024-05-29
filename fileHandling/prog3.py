# Create a program to overwrite the contents of the file with the following text: "HELLOOOOOO"

f= open("fileHandling/files/prog1Copied.txt", "w")
f.write("THis is file handling program! Now we are appending the content to the file")
f.close()

f= open("fileHandling/files/prog1Copied.txt", "w")
f.write("Whoops! I have deleted the content!")
f.close()