# Category, Tax Deducted, Dearness Allowance(DA)
# A, 30% of gross salary, 80% of basic salary
# B, 20% of gross salary, 50% of basic salary
# C, 10% of gross salary, 30% of basic salary

# Demonstrate the database concepts for
# the following scenario: A company management wants to compute the net salary of
# each group of employee based on the category of the employee such as Category
# A, Category B, Category C. Compute the net salary based on the attachedtable.

import sqlite3
import os # for dropping the database

# Drop the table if it exists
if os.path.exists("employee.db"):
    os.remove("employee.db")

conn = sqlite3.connect('employee.db')

c = conn.cursor()

# Create a table
c.execute("""CREATE TABLE employee (
    emp_ssn TEXT,
    emp_name TEXT,
    emp_category TEXT,
    gross_sal INTEGER,
    basic_sal INTEGER
)""")

# Insert atleast three values in to the database.
c.execute("INSERT INTO employee VALUES ('1BM20IS001', 'John', 'A', 50000, 40000)")
c.execute("INSERT INTO employee VALUES ('1BM20IS002', 'Jane', 'B', 50000, 40000)")
c.execute("INSERT INTO employee VALUES ('1BM20IS003', 'Bob', 'C', 50000, 40000)")

def compute_net_salary(emp_category, gross_sal, basic_sal):
    if emp_category == 'A':
        tax = 0.3 * gross_sal
        da = 0.8 * basic_sal
    elif emp_category == 'B':
        tax = 0.2 * gross_sal
        da = 0.5 * basic_sal
    elif emp_category == 'C':
        tax = 0.1 * gross_sal
        da = 0.3 * basic_sal
    else:
        tax = 0
        da = 0
    net_salary = gross_sal - tax + da
    return net_salary

# Select all rows
c.execute("SELECT * FROM employee")
rows = c.fetchall()
for row in rows:
    emp_ssn, emp_name, emp_category, gross_sal, basic_sal = row
    net_salary = compute_net_salary(emp_category, gross_sal, basic_sal)
    # Display all details of the employee in formatted way
    print(f"SSN: {emp_ssn}, Name: {emp_name}, Category: {emp_category}, Gross Salary: {gross_sal}, Basic Salary: {basic_sal}, Net Salary: {net_salary}")

conn.commit()


