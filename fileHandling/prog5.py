# Iterate through a directory and print all the files in it

import os

directoryToIterate = "fileHandling/files"

for file in os.listdir(directoryToIterate):
    print(os.path.join(directoryToIterate, file))


# Iterate through a directory and print all the contents of all the files in it

# import os

# directoryToIterate = "fileHandling/files"

# for file in os.listdir(directoryToIterate):
#     print("File Name: ", file)
#     with open(directoryToIterate + "/" + file, "r") as f:
#         print(f.read())

