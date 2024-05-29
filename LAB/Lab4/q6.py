# Create an Employee
# Database containing firstname, lastname, empsalary, city and DateofJoining. 

# Take the user input to Insert 5 tuples in database.

# Write query to extractthe following
# i)  Employee details whose name ends with “Rao”.
# ii) Employee-firstname, lastname who have joined in the year 2021.
# iii) Employee whose salary is less than 50,000.
# iv) Employee who is working in “Bangalore” city.

import sqlite3
import os

if os.path.exists("employee.db"):
    os.remove("employee.db")

conn = sqlite3.connect('employee.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE employee
                (firstname text, lastname text, empsalary integer, city text, DateofJoining text)''')


# Insert a row of data
cursor.execute("INSERT INTO employee VALUES ('A', 'B', 50000, 'Bangalore', '2021-01-01')")
cursor.execute("INSERT INTO employee VALUES ('C', 'D', 60000, 'Bangalore', '2022-01-02')")
cursor.execute("INSERT INTO employee VALUES ('E', 'F', 70000, 'Bangalore', '2020-01-03')")
cursor.execute("INSERT INTO employee VALUES ('G', 'H', 80000, 'Bangalore', '2021-01-04')")

# User input to insert 5 tuples
# for i in range(5):
#     firstname = input("Enter firstname: ")
#     lastname = input("Enter lastname: ")
#     empsalary = int(input("Enter empsalary: "))
#     city = input("Enter city: ")
#     DateofJoining = input("Enter DateofJoining: ")
#     cursor.execute('''INSERT INTO employee VALUES (?,?,?,?,?)''', (firstname, lastname, empsalary, city, DateofJoining))

# Save (commit) the changes
conn.commit()

# i)
cursor.execute('''SELECT * FROM employee WHERE lastname = "Rao"''')
print("Employee details whose name ends with “Rao”")
print(cursor.fetchall())

# ii)
cursor.execute('''SELECT firstname, lastname FROM employee WHERE DateofJoining LIKE "%2021%"''')
print("Employee-firstname, lastname who have joined in the year 2021")
print(cursor.fetchall())

# iii)
cursor.execute('''SELECT * FROM employee WHERE empsalary < 50000''')
print("Employee whose salary is less than 50,000")
print(cursor.fetchall())

# iv)
cursor.execute('''SELECT * FROM employee WHERE city = "Bangalore"''')
print("Employee who is working in “Bangalore” city")
print(cursor.fetchall())

# Close the connection
conn.close()
