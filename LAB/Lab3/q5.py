# Demonstrate object serialization in
# python by creating a custom class called employee.  This stores Employee name, age, salary,
# married and having kid. Save it and load it up into a separate object and
# display the new object.

class Employee:
    def __init__(self, name, age, salary, married, kid):
        self.name = name
        self.age = age
        self.salary = salary
        self.married = married
        self.kid = kid

    def __str__(self):
        return "Name: " + self.name + " + Age: " + str(self.age) + " + Salary: " + str(self.salary) + " + Married: " + str(self.married) + " + Kid: " + str(self.kid)

import pickle

f = open("LAB/Lab3/employee.dat", "wb")

emp = Employee("John", 25, 10000, True, False)
pickle.dump(emp, f)

f.close()

f = open("LAB/Lab3/employee.dat", "rb")

emp = pickle.load(f)

print(emp)

f.close()


