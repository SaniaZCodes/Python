# The "Nested Grade & Bonus" Logic
# Goal: Use Nested If and Comparison Operators.

score=int(input("Enter your score (0-100): "))
extra_credit=input("Is Extra Credit Completed? ")
if score>=90:
    if extra_credit:
        print("Grade: A+")
    else:
        print("Grade: A")
elif score>=80 and score<=89:
    print("Grade: B")
else:
    print("Grade: C")


print("\n")


# The "Short-Hand" Ticket Price
# Goal: Use Short-hand If/Else (Ternary Operator).

age=int(input("Enter age: "))
price= 20 if age>=18 else 10
print(f"Your ticket price is ${price}")


print("\n")


# The "Complex Admission" Check
# Goal: Use Logical Operators (and, or, not) inside an if statement.


has_ticket = True
is_blacklisted = False
has_special_invite = False

if (has_ticket and not is_blacklisted) or has_special_invite:
    print("Access Granted")
else:
    print("Access Denied")
