import math
import datetime

discount_code = None

name= input("Enter name: ")
while True:
    try:
        age= input("Enter age: ")
        age_int=int(age)
        break
    except:
        print("Invalid age. Age must be a valid number.")


ticket_price=5000
gravity_surcharge=math.sqrt(age_int)*10
total=ticket_price+gravity_surcharge


now= datetime.datetime.now()
booking_date=now.strftime("%d-%m-%Y")


print("\n")
print("Booking Details: ")
print(f"Name: {name}")
print(f"Booking Date: {booking_date}")
print(f"Total Cost: {total:.2f}")
