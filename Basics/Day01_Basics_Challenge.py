import random

# Variables & Types
item_name="iPhone"
price=5600.23
quantity=2

# Casting: Convert the quantity to a float before doing calculations
quantity_f=float(quantity)

# Math: Calculate the total_bill
bill=price*quantity_f

# Random Number: Use import random to generate a "Lucky Number" between 1 and 10
lucky_number=random.randint(1,10)

# Type Checking: Use type() to print and verify the data type of your total_bill and lucky_number.
print("Type Checking:")
print("Total Bill:", type(bill))
print("Lucky Number:", type(lucky_number))

print("\n")
print("Item Description: ")
print("Name: ",item_name)
print("Price: ",price)
print("Quantity: ",quantity)
print("Total Bill: ",bill)
print("Your Lucky Number: ",lucky_number)
