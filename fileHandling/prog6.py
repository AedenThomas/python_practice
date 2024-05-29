# If usn.txt contains
# 1 1BM20IS001 A first
# 2 1BM20IS002 B second

# Output should be as follows
# SLNO 1 with 1BM20IS001 named A is sitting in first row
# SLNO 2 with 1BM20IS002 named B is sitting in second row

f1 = open("fileHandling/files/usn.txt", "r")

for line in f1:
    slno, usn, name, seat = line.split()
    print(f"SLNO {slno} with {usn} named {name} is sitting in {seat} row")  

f1.close()

