# Implement Library management where students can borrow as well as donate books.


# Books table:

# id INTEGER PRIMARY KEY
# name TEXT
# total_count INTEGER


# a) Insert values to the table

# 34,king,5
# 123,Harry Potter,3


# b) Update the table based on user inputs: 
# based on book id
# I) BORROW
# II) RETURN

import sqlite3
import os

if os.path.exists("library.db"):
    os.remove("library.db")

conn = sqlite3.connect('library.db')

cursor = conn.cursor()

# Create a table
cursor.execute("""CREATE TABLE BOOKS (
    ID INTEGER PRIMARY KEY,
    NAME TEXT,
    TOTAL_COUNT INTEGER
)""")
conn.commit()

# User input 2 records
for i in range(2):
    id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    total_count = int(input("Enter Total Count: "))
    cursor.execute("INSERT INTO BOOKS VALUES (?,?,?)", (id, name, total_count))
    conn.commit()

# Select
cursor.execute("SELECT * FROM BOOKS")
print("Printing all\n", cursor.fetchall())

# Update
# Before updating insert a record with id 1
cursor.execute("INSERT INTO BOOKS VALUES (?,?,?)", (1, "AGT", 5))
cursor.execute("UPDATE BOOKS SET TOTAL_COUNT = 25000 WHERE ID = 1")
cursor.execute("SELECT * FROM BOOKS")
print("Printing all after updating\n", cursor.fetchall())

# Borrow means totalcount increases by 1
# Return means totalcount decreases by 1

# Borrow book with id 1 and 2
cursor.execute("UPDATE BOOKS SET TOTAL_COUNT = TOTAL_COUNT + 1 WHERE ID = 34" )
cursor.execute("UPDATE BOOKS SET TOTAL_COUNT = TOTAL_COUNT + 1 WHERE ID = 123" )
cursor.execute("SELECT * FROM BOOKS")
print("Printing all after borrowing 34 and 123\n", cursor.fetchall())

# Return book with id 1 and 2
cursor.execute("UPDATE BOOKS SET TOTAL_COUNT = TOTAL_COUNT - 1 WHERE ID = 34" )
cursor.execute("UPDATE BOOKS SET TOTAL_COUNT = TOTAL_COUNT - 1 WHERE ID = 123" )
cursor.execute("SELECT * FROM BOOKS")
print("Printing all after returning\n", cursor.fetchall())