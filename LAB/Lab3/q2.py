# Write a program to enter the following records in a binary file:

# Item No integer       
# Item_Name string        
# Qty integer        
# Price float
# Number of records to be entered should be accepted from the user. Read the file to display the records in the following format:

# Item No:
# Item Name :
# Quantity:
# Price per item:
# Amount: ( to be calculated as Price * Qty)

import pickle

f = open("LAB/Lab3/item.dat", "wb")

n = int(input("Enter the number of records: "))
for i in range(n):
    item_no = int(input("Enter the item number: "))
    item_name = input("Enter the item name: ")
    qty = int(input("Enter the quantity: "))
    price = float(input("Enter the price: "))
    pickle.dump(item_no, f)
    pickle.dump(item_name, f)
    pickle.dump(qty, f)
    pickle.dump(price, f)

f.close()

f = open("LAB/Lab3/item.dat", "rb")

for i in range(n):
    item_no = pickle.load(f)
    item_name = pickle.load(f)
    qty = pickle.load(f)
    price = pickle.load(f)
    print("Item No:", item_no)
    print("Item Name:", item_name)
    print("Quantity:", qty)
    print("Price per item:", price)
    print("Amount:", price * qty)

f.close()

