import sqlite3


# Delete the database file if it exists
import os
if os.path.exists("data.db"):
    os.remove("data.db")

# Connect to the database
connection = sqlite3.connect('data.db')

# Create a cursor
cursor = connection.cursor()


# Delete a table
cursor.execute("DROP TABLE IF EXISTS users")


# Create a table
cursor.execute("""CREATE TABLE users (
    name TEXT,
    age INTEGER,
    USN TEXT
)""")

# Insert a row of data
cursor.execute("INSERT INTO users VALUES ('John', 25, '1BM20IS001')")
cursor.execute("INSERT INTO users VALUES ('Jane', 22, '1BM20IS002')")
cursor.execute("INSERT INTO users VALUES ('Bob', 27, '1BM20IS003')")

# Using insert many
users = [
    ('Abhi', 21, '1BM20IS004'),
    ('Rahul', 22, '1BM20IS005'),
    ('Raj', 23, '1BM20IS006') 
]

cursor.executemany("INSERT INTO users VALUES (?,?,?)", users)



# Save (commit) the changes
connection.commit()

# We can also close the connection if we are done with it.
connection.close()


# Connect to the database
connection = sqlite3.connect('data.db')

# Create a cursor
cursor = connection.cursor()

# Select all rows 
cursor.execute("SELECT * FROM users")
print("Printing all\n", cursor.fetchall())


# Select all rows and newline after each row
cursor.execute("SELECT * FROM users")
print("Printing all with newline after each row")
for row in cursor.fetchall():
    print(row)


# Select a row
cursor.execute("SELECT * FROM users WHERE name='John'")
print("Printing John\n", cursor.fetchone())

# Update
cursor.execute("UPDATE users SET age=24 WHERE name='John'")
cursor.execute("SELECT * FROM users WHERE name='John'")
print("Printing John after updating\n", cursor.fetchone())


cursor.execute("SELECT * FROM users WHERE age=22")
print("Printing age 22\n", cursor.fetchall())


# Using fetchmany
cursor.execute("SELECT * FROM users")
print("Printing 2 rows\n", cursor.fetchmany(2))


