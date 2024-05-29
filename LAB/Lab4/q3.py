# Write a python code to connect to an existing database. If the database does not exist, then create it and finally a database
# object will be returned.

import sqlite3
import os

# Check if the database exists
if os.path.exists("employee.db"):
    conn = sqlite3.connect('employee.db')
else:
    conn = sqlite3.connect('employee.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE employee (
        emp_ssn TEXT,
        emp_name TEXT,
        emp_category TEXT,
        gross_sal INTEGER,
        basic_sal INTEGER
    )""")
    conn.commit()
    

