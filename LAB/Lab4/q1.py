# Create an Employee table with attributes
# such as emp_ssn, emp_name, emp_category, gross_sal, basic_sal.

import sqlite3

conn = sqlite3.connect('employee.db')
c = conn.cursor()
c.execute("DROP TABLE IF EXISTS employee")
c.execute("""CREATE TABLE employee (
    emp_ssn TEXT,
    emp_name TEXT,
    emp_category TEXT,
    gross_sal INTEGER,
    basic_sal INTEGER
)""")

# Insert atleast three values in to the database. 
c.execute("INSERT INTO employee VALUES ('1BM20IS001', 'John', 'Manager', 50000, 40000)")
c.execute("INSERT INTO employee VALUES ('1BM20IS002', 'Jane', 'Manager', 50000, 40000)")
c.execute("INSERT INTO employee VALUES ('1BM20IS003', 'Bob', 'Manager', 50000, 40000)")


conn.commit()
conn.close()
