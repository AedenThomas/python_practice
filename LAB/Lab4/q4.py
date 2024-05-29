# Create a table by considering the column names which is mentioned below:
#          ID   INT PRIMARY KEY     NOT NULL,
#          NAME           TEXT    NOT NULL,
#          AGE            INT     NOT NULL,
#          ADDRESS        CHAR(50),
#          SALARY         REAL

# INSERT Operation
        
# Insert the following records in the table by taking user input:

#          1, 'Paul', 32, 'California', 20000.00·       
#           2, 'Allen', 25, 'Texas', 15000.00·      
#           3, 'Teddy', 23, 'Norway', 20000.00·         
#         4, 'Mark', 25, 'Rich-Mond ', 65000.00


# SELECT Operation
# Write the python code to fetch and display records from the COMPANY table.


# UPDATE Operation
# Update COMPANY table with salary =25000 where ID=1  then print all the values.


# DELETE Operation  
# delete ID=2 row and then fetch and display the remaining records from the COMPANY table


import sqlite3
import os 

if os.path.exists("company.db"):
    os.remove("company.db")

conn = sqlite3.connect('company.db')

cursor = conn.cursor()

# Create a table
cursor.execute("""CREATE TABLE COMPANY (
    ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    AGE INT NOT NULL,
    ADDRESS CHAR(50),
    SALARY REAL
)""")

# User input 4 records
for i in range(4):
    id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    address = input("Enter Address: ")
    salary = float(input("Enter Salary: "))
    cursor.execute("INSERT INTO COMPANY VALUES (?,?,?,?,?)", (id, name, age, address, salary))
    conn.commit()

    
# Select
cursor.execute("SELECT * FROM COMPANY")
print("Printing all\n", cursor.fetchall())

# Update
cursor.execute("UPDATE COMPANY SET SALARY = 25000 WHERE ID = 1")
cursor.execute("SELECT * FROM COMPANY")
print("Printing all after updating\n", cursor.fetchall())

# Delete
cursor.execute("DELETE FROM COMPANY WHERE ID = 2")
cursor.execute("SELECT * FROM COMPANY")
print("Printing all after deleting\n", cursor.fetchall())


conn.close()
